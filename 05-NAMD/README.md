05-NAMD Directory Overview
This directory (05-NAMD) focuses on performing non-adiabatic molecular dynamics (NA-MD) simulations within the neglect-of-back-reaction approximation (NBRA) framework using the Libra package. It contains two subdirectories, pristine and divacancy, which share similar workflows for running NA-MD simulations on the pristine and divacancy defect systems, respectively.
Directory Structure

pristine/: Contains files and scripts for NA-MD simulations on the pristine system.
divacancy/: Contains files and scripts for NA-MD simulations on the divacancy defect system.

Common Files in pristine/ and divacancy/

NAMD.ipynb: A Jupyter notebook that outlines the workflow for setting up and running NA-MD simulations, precomputing properties like decoherence times, and visualizing results. A detailed breakdown is provided below.
NAMD-PR-S1.py: A Python script that automates the NA-MD simulations for the pristine system starting from state 1, using methods like FSSH and GFSH. It reads vibronic Hamiltonian data, sets up simulation parameters, and runs dynamics with multiprocessing.
recipes/: Directory containing Python scripts defining NA-MD method recipes (e.g., fssh_nbra.py, gfsh_nbra.py), which specify parameters for various surface hopping methods.
CP2K_v23/: Directory containing results from prior steps (e.g., 04-NACs), including vibronic Hamiltonian files in res-mb-sd-DFT/.
decoherence_times.txt, decoherence_rates.txt, average_gaps.txt: Output files containing precomputed decoherence times, rates, and energy gaps.
<method>_icond_<number>/mem_data.hdf: Output directories and HDF5 files containing simulation results (e.g., populations) for each initial condition and method (e.g., FSSH_icond_1/mem_data.hdf).

Detailed Breakdown of NAMD.ipynb
The NAMD.ipynb notebook provides a comprehensive workflow for setting up NA-MD simulations, precomputing key properties, running dynamics, and visualizing results. Below is a detailed description of its structure and functionality:
Notebook Structure
1. Introduction and Table of Contents

Purpose: The notebook focuses on running NA-MD simulations within the NBRA framework using various surface hopping methods available in Libra.
Methods Covered:
Tully's Fewest Switches Surface Hopping (FSSH)
Global Flux Surface Hopping (GFSH)
Instantaneous Decoherence at Attempted hops (ID-A)
Modified Simplified Decay of Mixing method (MSDM)
Decoherence-Induced Surface Hopping (DISH_rev2023)
Mapping Approach to Surface Hopping (MASH)
Fewest Switches Surface Hopping revised (FSSH2)


Table of Contents:
Generic setups.
Theoretical background for NA-MD methods.
File-based Hamiltonian setup.
Precomputing and visualizing key properties (dephasing times, NAC maps).
Dynamics (setup, running, and visualization).


Learning Objectives:
Understand NA-MD methods in Libra for NBRA workflows.
Set up NBRA NA-MD calculations for different methods.
Precompute properties like dephasing rates and energy gaps.
Define file-based Hamiltonian computation functions.
Set up initial conditions for electronic degrees of freedom.
Plot dephasing times, couplings, and population decay curves.
Fit population decay curves and compute confidence intervals.
Set up multithreading NA-MD calculations.


Use Cases:
Read vibronic Hamiltonian data files.
Compute time-averaged nonadiabatic couplings.
Define adiabatic file-based model Hamiltonian.
Compute and plot trajectory-averaged dephasing times and energy gaps.
Plot population decay curves and fit them.


Functions Used:
libra_py.data_visualize: colors, clrs_index.
libra_py.dynamics.tsh.compute: generic_recipe.
libra_py.workflows.nbra.decoherence_times: energy_gaps_ave, decoherence_times_ave.



2. Generic Setups

Imports:
Standard libraries: os, glob, time, h5py, multiprocessing, matplotlib.pyplot, numpy, scipy.sparse, scipy.optimize.
Libra modules: liblibra_core, util.libutil, libra_py.units, libra_py.data_conv, libra_py.dynamics.tsh.compute, libra_py.workflows.nbra.decoherence_times, libra_py.data_visualize.
Recipes: Imports various NA-MD method recipes (e.g., fssh_nbra, gfsh_nbra, ida_nbra).


Notes:
Warnings about duplicate Python converters for std::vector types are expected and can be ignored.
Key sections for user modification are marked with hash-sign lines (#####).



3. Theoretical Background

Overview: Discusses the NBRA approach, where NA-MD simulations use precomputed energy, coupling, and time-overlap files from ground-state molecular dynamics trajectories.
Common NBRA Parameters:
ham_update_method: 2: Recompute only adiabatic Hamiltonian.
ham_transform_method: 0: No Hamiltonian transformations.
time_overlap_method: 0: Do not update time-overlaps (precomputed).
nac_update_method: 0: Read NACs from files.
hvib_update_method: 0: Do not update vibronic Hamiltonian.
force_method: 0, rep_force: 1: Do not compute forces.
hop_acceptance_algo: 32, momenta_rescaling_algo: 0: Use Boltzmann probability for hop acceptance, no velocity rescaling.



4. File-based Hamiltonian

Reading Files:
Path: /home/98722002/Desktop/WORK-DIRECTORY/ML-BP/PBE0/04-NACs/di_vacancy/res-mb-sd-DFT.
Time range: Steps 2000 to 3998.
Files read:
Energies: Hvib_ci_{step}_re.npz (diagonal elements).
Time-overlaps: St_ci_{step}_re.npz.
NACs: Hvib_ci_{step}_im.npz.


Outputs: Arrays E (energies), St (time-overlaps), NAC (nonadiabatic couplings), Hvib (vibronic Hamiltonian).
Dimensions: 1998 steps, 11 states.


Hamiltonian Function:
Defines compute_model to return Hamiltonian properties by retrieving precomputed matrices (E, NAC, Hvib, St) for a given timestep.



5. Precompute and Visualize Key Properties

Dephasing Times and Rates:
Computes average decoherence times (tau) and rates using decoherence_times.decoherence_times_ave.
Computes energy gaps (dE) using decoherence_times.energy_gaps_ave.
Converts decoherence times to femtoseconds and saves to decoherence_times.txt.
Saves rates to decoherence_rates.txt and average gaps to average_gaps.txt.


Visualization:
A section for visualizing the decoherence times map is included but commented out in the provided notebook.



6. Dynamics (Incomplete in Notebook)

Setup: Defines simulation parameters, initial conditions, and methods (e.g., FSSH, GFSH).
Running: Uses tsh_dynamics.generic_recipe to run dynamics (not implemented in the notebook).
Visualization:
Plots population decay curves for various methods (FSSH, FSSH2, GFSH, IDA, IDF, IDA_GFSH, MSDM, MSDM_GFSH).
Fits curves using exponential (exp_funct) or Gaussian (Gau_funct) functions.
Computes average timescales and error bars (95% confidence interval).
Saves the plot as dynamics-Divacancy-state1.png.



Notebook Metadata

Python Version: 3.9.20 (though the environment may use 3.7, as per warnings).
Dependencies: Includes ipykernel, varInspector for Jupyter functionality.

Overview of NAMD-PR-S1.py
The NAMD-PR-S1.py script automates NA-MD simulations for the pristine system starting from state 1, using the FSSH and GFSH methods. Key features include:

Input Data:
Path: /home/98722002/Desktop/WORK-DIRECTORY/ML-BP/PBE0/04-NACs/pristine/CP2K_v23/res-mb-sd-DFT.
Time range: Steps 2000 to 2500 (500 steps).
Reads energies, time-overlaps, and NACs, similar to the notebook.


Precomputation:
Computes decoherence times, rates, and energy gaps, saving them to decoherence_times.txt, decoherence_rates.txt, and average_gaps.txt.


Simulation Setup:
Number of states: 11.
Simulation parameters:
nsteps: 5 × NSTEPS (2500 steps).
ntraj: 250 trajectories.
dt: 1.0 fs (converted to atomic units).
Initial state: 1.


Methods: Runs FSSH and GFSH sequentially.


Multithreading:
Uses 10 threads to run simulations for initial conditions (ICONDS: 1 to 901, step 100).
Results are saved in directories like FSSH_icond_1/mem_data.hdf.


Output:
Saves simulation results (e.g., sh_pop_adi, se_pop_adi) in HDF5 files for each initial condition.



Dependencies

Libra: AkimovLab version (for NA-MD simulations).
Python 3.x: With numpy, scipy.sparse, matplotlib.pyplot, h5py, multiprocessing, liblibra_core, libra_py.
Jupyter Notebook: For executing NAMD.ipynb.
CP2K: For generating vibronic Hamiltonian files (assumed from prior steps, e.g., 04-NACs).

Setup and Execution

Environment Setup:

Activate the Libra Python environment:source activate /path/to/libra/environment


Install required packages:pip install numpy scipy matplotlib jupyter h5py




Prepare Input Data:

Ensure the CP2K_v23/res-mb-sd-DFT/ directory contains vibronic Hamiltonian files (e.g., from 04-NACs).


Run the Notebook:

Navigate to the subdirectory:cd 05-NAMD/pristine


Launch Jupyter Notebook:jupyter notebook NAMD.ipynb


Execute cells to precompute properties and (optionally) visualize results.


Run the Script:

Execute the Python script to run NA-MD simulations:python NAMD-PR-S1.py


The script will run FSSH and GFSH simulations with 10 threads, saving results in directories like FSSH_icond_1/.


Output:

Precomputed properties: decoherence_times.txt, decoherence_rates.txt, average_gaps.txt.
Simulation results: HDF5 files in <method>_icond_<number>/mem_data.hdf.



Notes

The pristine and divacancy subdirectories follow similar workflows but apply to different systems.
Adjust file paths in the notebook and script to match your local setup.
The notebook’s dynamics and visualization sections are incomplete; the script (NAMD-PR-S1.py) provides a working implementation.
For detailed parameter descriptions, refer to the notebook’s markdown sections or the recipes in the recipes/ directory.

For further details, explore the NAMD.ipynb notebook or the main project documentation.
