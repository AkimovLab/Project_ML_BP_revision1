04-NACs Directory Overview
This directory (04-NACs) is part of the Project_ML_BP_revision1 repository and focuses on computing non-adiabatic couplings (NACs) for the ML-BP project using the Libra package. It contains two subdirectories, pristine and divacancy, which have similar file structures and workflows for NAC calculations in Kohn-Sham and excited state bases for periodic systems. This README provides an overview of the directory and a detailed breakdown of the pristine.ipynb notebook.
Directory Structure

pristine/: Contains files and scripts for NAC calculations on the pristine system.
divacancy/: Contains files and scripts for NAC calculations on the divacancy defect system.

Common Files in pristine/ and divacancy/

pristine.ipynb (or equivalent in divacancy/): A Jupyter notebook that outlines the workflow for computing NACs and analyzing results. See the detailed breakdown below.
res/: Directory for storing calculation results, including NAC data and molecular orbital overlaps.
res-ks-DFT/: Directory for saving NACs computed in the Kohn-Sham basis.
res-mb-sd-DFT/: Directory for saving NACs computed in the many-body and single-particle excited state bases.
all_logfiles/: Directory containing log files from electronic structure calculations (e.g., CP2K outputs).

Detailed Breakdown of pristine.ipynb
The pristine.ipynb notebook provides a comprehensive workflow for computing non-adiabatic couplings (NACs) in Kohn-Sham and excited state bases, followed by analysis and visualization of the results. Below is a detailed description of its structure and functionality:
Notebook Structure
1. Introduction and Table of Contents

Purpose: The notebook focuses on computing NACs using molecular orbital overlap files (from prior steps, e.g., 03-OVERLAPS) and analyzing the results.
Bases: NACs are computed in:
Kohn-Sham (KS) states.
Single-particle (SP) and many-body (MB) excited state bases.


Analysis: Includes plotting energy vs. time, average density of states, NAC maps, NAC distributions, and influence spectra.
Table of Contents:
Importing needed libraries.
Overview of required files.
Computing NACs:
3.1. Kohn-Sham basis.
3.2. Excited state basis.


Plotting results:
4.1. Energy vs. time.
4.2. Average density of states.
4.3. NAC map.
4.4. NAC distribution.
4.5. Influence spectrum.




Learning Objectives:
Compute NACs in KS and excited state bases.
Plot excited state energies vs. time, average partial density of states, NAC maps, distributions, and influence spectra.


Use Cases:
Computing NACs.
Plotting and analyzing results.


Functions Used:
libra_py modules: data_stat.cmat_distrib, influence_spectrum.recipe1, workflows.nbra.step3 (including run_step3_ks_nacs_libint and run_step3_sd_nacs_libint), units.au2ev.



2. Importing Needed Libraries

Libraries:
os, glob: For file handling.
numpy, scipy.sparse: For numerical computations and sparse matrix handling.
matplotlib.pyplot: For plotting.
liblibra_core: Core Libra functionality.
libra_py: Custom Libra modules (units, data_stat, influence_spectrum, workflows.nbra.step3).
libra_py.packages.cp2k.methods: CP2K-specific methods for parsing log files.


Warnings: The notebook may output warnings related to duplicate Python converters for certain std::vector types, which can be ignored as they do not affect functionality.

3. Overview of Required Files

MO Overlap Files:
Located at: ../../03-OVERLAPS/pristine/2000-4000/res.
These files contain molecular orbital overlap data from prior CP2K calculations (e.g., from 03-OVERLAPS).


Log Files:
Located at: ../../03-OVERLAPS/pristine/2000-4000/all_logfiles.
CP2K log files containing electronic structure and TD-DFT data, used to extract Kohn-Sham HOMO indices and TD-DFT results.



4. Computing NACs
The notebook computes NACs in two bases: Kohn-Sham and excited states (both single-particle and many-body).
4.1. Kohn-Sham Basis

Function: step3.run_step3_ks_nacs_libint(params).
Purpose: Computes NACs between pairs of Kohn-Sham states using molecular orbital time-overlaps.
Key Parameters:
lowest_orbital, highest_orbital: Define the range of orbitals (e.g., 130 to 191, centered around HOMO).
num_occ_states, num_unocc_states: Number of occupied (HOMO to lower) and unoccupied (LUMO to higher) states in the active space (e.g., 30 each).
use_multiprocessing, nprocs: Enable multiprocessing with 32 processors.
time_step: Time step in femtoseconds (e.g., 1.0 fs).
es_software: Specifies the electronic structure software (e.g., cp2k).
path_to_npz_files, logfile_directory: Paths to MO overlap files and CP2K log files.
path_to_save_ks_Hvibs: Output directory for KS NACs (e.g., res-ks-DFT).
start_time, finish_time: Time step range (e.g., 2000 to 4000).


Notes:
Sparse matrices (scipy.sparse) are used due to the mostly zero overlap matrices.
No spin-orbit coupling is considered, resulting in zero blocks in the NAC matrix.



4.2. Excited State Basis

Function: step3.run_step3_sd_nacs_libint(params).
Purpose: Computes NACs between excited state Slater determinants (SDs) in single-particle (SP) and many-body (MB) bases.
Key Parameters (additional to those in KS):
isUKS: Flag for unrestricted spin calculations (set to 0 for restricted).
is_many_body: If True, computes MB NACs using TD-DFT data; otherwise, only SP NACs (set to True).
number_of_states: Number of TD-DFT states to consider (e.g., 10).
tolerance: Threshold for selecting excitations based on CI coefficients (e.g., 0.01).
verbosity: Controls output verbosity (e.g., 0 for minimal).
sorting_type: Sorting method for SDs (energy or identity, set to identity).
path_to_save_sd_Hvibs, outdir: Output directories for SD NACs (e.g., res-mb-sd-DFT).


Notes:
For MB basis, NACs are computed using TD-DFT CI coefficients.
For SP basis, NACs are derived from num_occ_states and num_unocc_states.
If TD-DFT data is available, Libra automatically generates SDs from log files, overriding user-defined num_occ_states and num_unocc_states.



5. Plotting Results
The notebook includes sections for visualizing the results, though only the influence spectrum plotting is fully implemented in the provided code.
5.1. Energy vs. Time
Plot energies of SP and MB excitation bases over time.


5.2. Average Density of States
Plot the average partial density of states.

5.3. NAC Map
Visualize the NAC matrix as a heatmap.

5.4. NAC Distribution
Plot the distribution of NAC values using data_stat.cmat_distrib.

5.5. Influence Spectrum
Compute and plot the influence spectrum for selected state pairs.

Implementation:
Uses influence_spectrum.recipe1 to compute the spectrum.
Parameters:
dt: Time step (1.0 fs).
wspan: Frequency range (4000 cm⁻¹).
dw: Frequency step (1.0 cm⁻¹).
do_output, do_center, acf_type, data_type: Control computation settings.


Selects state pairs (e.g., 0-1, 0-2, 1-2) to compute energy gaps.
Plots frequency (cm⁻¹) vs. intensity (a.u.) with a title indicating the state pair.


Output: A matplotlib plot showing the influence spectrum for the selected states.

6. Additional Code

A commented section converts sparse matrices (St_ci_{i}_re.npz) to dense format and saves them as text files in EXP-res-mb-sd-DFT/ for steps 2000 to 3997.

Notebook Metadata

Python Version: 3.9.20 (though the environment uses 3.7 as per warnings).
Dependencies: Includes ipykernel, varInspector for Jupyter functionality.

Dependencies

Libra: AkimovLab version (for NAC computations).
Python 3.x: With numpy, scipy.sparse, matplotlib.pyplot, liblibra_core, libra_py.
Jupyter Notebook: For executing pristine.ipynb.
CP2K: For generating MO overlap and log files (assumed from prior steps).

Setup and Execution

Environment Setup:

Activate the Libra Python environment:source activate /path/to/libra/environment


Install required packages:pip install numpy scipy matplotlib jupyter




Prepare Input Data:

Ensure res/ contains MO overlap files (e.g., from ../../03-OVERLAPS/pristine/2000-4000/res).
Verify all_logfiles/ contains CP2K log files with TD-DFT data.


Run the Notebook:

Navigate to the subdirectory:cd 04-NACs/pristine


Launch Jupyter Notebook:jupyter notebook pristine.ipynb


Execute the cells to compute NACs and generate plots.


Output:

NAC results are saved in res-ks-DFT/ and res-mb-sd-DFT/.
Plots (e.g., influence spectrum) are displayed inline.



Notes

The pristine and divacancy subdirectories follow the same methodology but apply to different systems.
Adjust file paths in the notebook to match your local setup.
Some plotting sections (e.g., energy vs. time) are not implemented; users can extend the notebook to include these visualizations.
For detailed parameter descriptions, refer to the notebook's markdown sections.

For further details, explore the pristine.ipynb notebook or the main project documentation.
