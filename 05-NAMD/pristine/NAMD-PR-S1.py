import os, glob, time, h5py, warnings

import multiprocessing as mp
import matplotlib.pyplot as plt   # plots
import numpy as np
import scipy.sparse as sp
from scipy.optimize import curve_fit

from liblibra_core import *
import util.libutil as comn

import libra_py
from libra_py import units, data_conv #, dynamics_plotting
import libra_py.dynamics.tsh.compute as tsh_dynamics
#import libra_py.dynamics.tsh.plot as tsh_dynamics_plot
#import libra_py.data_savers as data_savers
import libra_py.workflows.nbra.decoherence_times as decoherence_times
import libra_py.data_visualize

from recipes import  gfsh_nbra, fssh_nbra, fssh2_nbra, ida_nbra, idf_nbra, ida_gfsh_nbra, msdm_gfsh_nbra, msdm_nbra 

#from matplotlib.mlab import griddata
#%matplotlib inline 
warnings.filterwarnings('ignore')

path_to_save_ci_Hvibs = '/home/98722002/Desktop/WORK-DIRECTORY/ML-BP/PBE0/04-NACs/pristine/CP2K_v23/res-mb-sd-DFT'

###########################################
istep = 2000    # the first timestep to read
fstep = 2500 # the last timestep to read
###########################################

nsteps = fstep - istep
NSTEPS = nsteps
print(F"Number of steps = {nsteps}")

x = sp.load_npz(F"{path_to_save_ci_Hvibs}/Hvib_ci_2000_im.npz")
nstates = x.shape[0]
NSTATES = nstates                                                            
print(F"Number of states = {nstates}")

#================== Read energies =====================
                                                       
E = []
for step in range(istep,fstep):
    energy_filename = F"{path_to_save_ci_Hvibs}/Hvib_ci_{step}_re.npz"
    energy_mat = sp.load_npz(energy_filename)
    # For data conversion we need to turn np.ndarray to np.array so that 
    # we can use data_conv.nparray2CMATRIX
    E.append( np.array( np.diag( energy_mat.todense() ) ) )
E = np.array(E)
NSTATES = E[0].shape[0]
#================== Read time-overlap =====================
St = []
for step in range(istep,fstep):        
    St_filename = F"{path_to_save_ci_Hvibs}/St_ci_{step}_re.npz"
    St_mat = sp.load_npz(St_filename)
    St.append( np.array( St_mat.todense() ) )
St = np.array(St)
#================ Compute NACs and vibronic Hamiltonians along the trajectory ============    
NAC = []
Hvib = [] 
for c, step in enumerate(range(istep,fstep)):
    nac_filename = F"{path_to_save_ci_Hvibs}/Hvib_ci_{step}_im.npz"
    nac_mat = sp.load_npz(nac_filename)
    NAC.append( np.array( nac_mat.todense() ) )
    Hvib.append( np.diag(E[c, :])*(1.0+1j*0.0)  - (0.0+1j)*nac_mat[:, :] )

NAC = np.array(NAC)
Hvib = np.array(Hvib)

print('Number of steps:', NSTEPS)
print('Number of states:', NSTATES)
class abstr_class:
    pass

def compute_model(q, params, full_id):
    timestep = params["timestep"]
    nst = params["nstates"]
    obj = abstr_class()

    obj.ham_adi = data_conv.nparray2CMATRIX( np.diag(E[timestep, : ]) )
    obj.nac_adi = data_conv.nparray2CMATRIX( NAC[timestep, :, :] )
    obj.hvib_adi = data_conv.nparray2CMATRIX( Hvib[timestep, :, :] )
    obj.basis_transform = CMATRIX(nst,nst); obj.basis_transform.identity()  #basis_transform
    obj.time_overlap_adi = data_conv.nparray2CMATRIX( St[timestep, :, :] )
    
    return obj
   
# ================= Computing the energy gaps and decoherence times ===============
# Prepare the energies vs time arrays
HAM_RE = []
for step in range(E.shape[0]):
    HAM_RE.append( data_conv.nparray2CMATRIX( np.diag(E[step, : ]) ) )

# Average decoherence times and rates
tau, rates = decoherence_times.decoherence_times_ave([HAM_RE], [0], NSTEPS, 0)

# Computes the energy gaps between all states for all steps
dE = decoherence_times.energy_gaps_ave([HAM_RE], [0], NSTEPS)

# Decoherence times in fs
deco_times = data_conv.MATRIX2nparray(tau) * units.au2fs

# Zero all the diagonal elements of the decoherence matrix
np.fill_diagonal(deco_times, 0)

# Saving the average decoherence times [fs]
np.savetxt('decoherence_times.txt',deco_times.real)

# Computing the average energy gaps
gaps = MATRIX(NSTATES, NSTATES)
for step in range(NSTEPS):
    gaps += dE[step]
gaps /= NSTEPS

rates.show_matrix("decoherence_rates.txt")
gaps.show_matrix("average_gaps.txt")



####################
####################
####################================== Model parameters ====================
#================== Model parameters ====================
model_params = { "timestep":0, "icond":0,  "model0":0, "nstates":NSTATES }

#=============== Some automatic variables, related to the settings above ===================
#############
nsteps = NSTEPS
#############

dyn_general = { "nsteps":5*NSTEPS, "ntraj":250, "nstates":NSTATES, "dt":1.0*units.fs2au,
                "decoherence_rates":rates, "ave_gaps":gaps,                
                "progress_frequency":0.1, "which_adi_states":range(NSTATES), "which_dia_states":range(NSTATES),
                "mem_output_level":2,
                "properties_to_save":[ "timestep", "time","se_pop_adi", "sh_pop_adi" ],
                "prefix":F"NBRA", "prefix2":F"NBRA", "isNBRA":0, "nfiles": nsteps - 1
              }
##########################################################
#============== Select the method =====================

fssh_nbra.load(dyn_general); prf = "FSSH"  # FSSH
##########################################################

#=================== Initial conditions =======================
#============== Nuclear DOF: these parameters don't matter much in the NBRA calculations ===============
nucl_params = {"ndof":1, "init_type":3, "q":[-10.0], "p":[0.0], "mass":[2000.0], "force_constant":[0.01], "verbosity":-1 }

#============== Electronic DOF: Amplitudes are sampled ========
elec_params = {"ndia":NSTATES, "nadi":NSTATES, "verbosity":-1, "init_dm_type":0}

###########
istate = 1       ###########
elec_params.update( {"init_type":1,  "rep":1,  "istate":istate } )  # how to initialize: random phase, adiabatic representation

if prf=="MASH":
    istates = list(np.zeros(NSTATES))
    istates[istate] = 1.0
    elec_params.update( {"init_type":4,  "rep":1,  "istate":3, "istates":istates } )  # different initialization for MASHes } )  # different initialization for MASH
def function1(icond):
    print('Running the calculations for icond:', icond)
    time.sleep( icond * 0.01 )
    rnd=Random()
    mdl = dict(model_params)
    mdl.update({"icond": icond})  #create separate copy
    dyn_gen = dict(dyn_general)
    dyn_gen.update({"prefix":F"{prf}_icond_{icond}", "prefix2":F"{prf}_icond_{icond}" })
    res = tsh_dynamics.generic_recipe(dyn_gen, compute_model, mdl, elec_params, nucl_params, rnd)
# ################################
################################
nthreads = 10
ICONDS = list(range(1,1000,100))
################################

pool = mp.Pool(nthreads)
pool.map(function1, ICONDS)
pool.close()                            
pool.join()



####################
####################
####################================== Model parameters ====================
#================== Model parameters ====================
model_params = { "timestep":0, "icond":0,  "model0":0, "nstates":NSTATES }

#=============== Some automatic variables, related to the settings above ===================
#############
nsteps = NSTEPS
#############

dyn_general = { "nsteps":5*NSTEPS, "ntraj":250, "nstates":NSTATES, "dt":1.0*units.fs2au,
                "decoherence_rates":rates, "ave_gaps":gaps,                
                "progress_frequency":0.1, "which_adi_states":range(NSTATES), "which_dia_states":range(NSTATES),
                "mem_output_level":2,
                "properties_to_save":[ "timestep", "time","se_pop_adi", "sh_pop_adi" ],
                "prefix":F"NBRA", "prefix2":F"NBRA", "isNBRA":0, "nfiles": nsteps - 1
              }
##########################################################
#============== Select the method =====================

gfsh_nbra.load(dyn_general); prf = "GFSH"  # GFSH
##########################################################

#=================== Initial conditions =======================
#============== Nuclear DOF: these parameters don't matter much in the NBRA calculations ===============
nucl_params = {"ndof":1, "init_type":3, "q":[-10.0], "p":[0.0], "mass":[2000.0], "force_constant":[0.01], "verbosity":-1 }

#============== Electronic DOF: Amplitudes are sampled ========
elec_params = {"ndia":NSTATES, "nadi":NSTATES, "verbosity":-1, "init_dm_type":0}

###########
istate = 1       ###########
elec_params.update( {"init_type":1,  "rep":1,  "istate":istate } )  # how to initialize: random phase, adiabatic representation

if prf=="MASH":
    istates = list(np.zeros(NSTATES))
    istates[istate] = 1.0
    elec_params.update( {"init_type":4,  "rep":1,  "istate":3, "istates":istates } )  # different initialization for MASHes } )  # different initialization for MASH
def function1(icond):
    print('Running the calculations for icond:', icond)
    time.sleep( icond * 0.01 )
    rnd=Random()
    mdl = dict(model_params)
    mdl.update({"icond": icond})  #create separate copy
    dyn_gen = dict(dyn_general)
    dyn_gen.update({"prefix":F"{prf}_icond_{icond}", "prefix2":F"{prf}_icond_{icond}" })
    res = tsh_dynamics.generic_recipe(dyn_gen, compute_model, mdl, elec_params, nucl_params, rnd)
# ################################
################################
nthreads = 10
ICONDS = list(range(1,1000,100))
################################

pool = mp.Pool(nthreads)
pool.map(function1, ICONDS)
pool.close()                            
pool.join()


