import os
import sys
from libra_py.workflows.nbra import step2 
import libra_py.packages.cp2k.methods as CP2K_methods 



path = os.getcwd()
params = {}
# number of processors
params['nprocs'] = 32
# The mpi executable
params['mpi_executable'] = 'mpirun'
params['restart_file'] = True
# The istep and fstep
params['istep'] = 
params['fstep'] = 
# Lowest and highest orbital, Here HOMO is 512
params['lowest_orbital'] = 160-30
params['highest_orbital'] = 161+30
# extended tight-binding calculation type
params['isxTB'] = False
# DFT calculation type
params['isUKS'] = False
# Periodic calculations flag
params['is_periodic'] = True
# Set the cell parameters for periodic calculations
if params['is_periodic']:
    params['A_cell_vector'] = [18.21,         0.0000000000,         0.00000000000]
    params['B_cell_vector'] = [0.0000000000,         13.22,         0.0000000000]
    params['C_cell_vector'] = [0.0000000000,         0.0000000000,        35.00]
    params['periodicity_type'] = 'XYZ'  
   # Set the origin
    origin = [0,0,0]
    tr_vecs = params['translational_vectors'] = CP2K_methods.generate_translational_vectors(origin, [1,1,1],
                                                                                            params['periodicity_type'])
    
    print('The translational vectors for the current periodic system are:\n')
    print(tr_vecs)
    print(F'Will compute the S^AO between R(0,0,0) and {tr_vecs.shape[0]+1} translational vectors')

# The AO overlaps in spherical or Cartesian coordinates
params['is_spherical'] =  True
# Remove the molden files, which are large files for some systems, 
# after the computaion is done for tha system
params['remove_molden'] = True
# Cube visualization using VMD
params['cube_visualization'] = True
if params['cube_visualization']:
    # The only parts that we will change in this template are loading the cubes and rendering the images.
    params['vmd_input_template'] = '../vmd.tcl'
    params['states_to_plot'] = list(range(159,163))#list(range(380,383))
    params['plot_phase_corrected'] = True #True
    params['vmd_exe'] = 'vmd'
    params['tachyon_exe'] = '/opt/vmd/lib/tachyon_LINUXAMD64'
    params['x_pixels'] = 1024
    params['y_pixels'] = 1024
    params['together_mode'] = False
    params['image_format'] = 'tga'
    params['remove_cube'] = True
    params['all_images'] = path + '/../all_images'

# The results are stored in this folder
params['res_dir'] = path + '/../res'
params['all_pdosfiles'] = path + '/../all_pdosfiles'
params['all_logfiles'] = path + '/../all_logfiles'
# CP2K executable 
params['cp2k_exe'] = '/home/98722002/cp2k-2025.1/build/bin/cp2k.psmp'
# If the xTB calculations are needed, we need an OT procedure 
params['cp2k_ot_input_template'] = path + '/../es_ot_temp.inp'
params['cp2k_diag_input_template'] = path + '/../es_diag_temp.inp'
# The trajectory xyz file path
params['trajectory_xyz_filename'] = path + '/../MD_pristiine-pos-1.xyz'

step2.run_cp2k_libint_step2(params)

