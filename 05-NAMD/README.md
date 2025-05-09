# README for 05-NAMD

This directory focuses on performing non-adiabatic molecular dynamics (NA-MD) simulations using the neglect-of-back-reaction approximation (NBRA) framework within the Libra package. It is organized into two main subdirectories:

## Directory Structure

* **pristine/** - Contains input files, scripts, and notebooks for NA-MD simulations on the pristine system.
* **divacancy/** - Contains similar files and workflows but for the divacancy defect system.

### Common Files in `pristine/` and `divacancy/`

* **NAMD.ipynb:** A Jupyter notebook that guides the user through setting up and running NA-MD simulations, precomputing decoherence times, and visualizing results.
* **NAMD-PR-S1.py:** A Python script that automates the NA-MD simulations starting from state 1 using methods such as FSSH and GFSH.
* **recipes/** - Directory containing method-specific scripts (e.g., `fssh_nbra.py`, `gfsh_nbra.py`).
* **decoherence\_times.txt, decoherence\_rates.txt, average\_gaps.txt:** Output files with precomputed decoherence times, rates, and energy gaps.

### NAMD.ipynb Breakdown

1. **Introduction:** Overview of NA-MD simulation methods (FSSH, GFSH, MSDM, DISH, MASH).
2. **Setup and Imports:** Defines the necessary Libra modules and custom functions.
3. **Hamiltonian Setup:** Reads Hamiltonian, NAC, and time-overlap matrices from `04-NACs` results.
4. **Precomputation:** Calculates average decoherence times, rates, and energy gaps. Saves data to text files.
5. **Dynamics Execution:** Sets up and runs NA-MD simulations for specified initial states and methods.
6. **Visualization:** Plots population decay, energy gaps, and decoherence times.

### NAMD-PR-S1.py Overview

* **Input Data:** Reads vibronic Hamiltonian data from `04-NACs` and prepares it for NA-MD simulations.
* **Methods Implemented:** FSSH and GFSH.
* **Simulation Parameters:** Defines initial states, number of trajectories, and simulation time steps.
* **Output:** Saves population data and Hamiltonian information in HDF5 files for each initial condition.

### Setup and Execution

1. **Environment Setup:**

```bash
source activate /path/to/libra/environment
```

2. **Run the Jupyter Notebook:**

```bash
cd 05-NAMD/pristine
jupyter notebook NAMD.ipynb
```

3. **Run the Python Script:**

```bash
python NAMD-PR-S1.py
```

### Output Files

* **decoherence\_times.txt, decoherence\_rates.txt, average\_gaps.txt:** Precomputed property files.
* **method\_icond\_num/mem\_data.hdf:** Simulation results organized by method and initial condition.

### Notes

* Adjust paths to executable files and data directories as necessary.
* Ensure that the `CP2K_v23` folder is populated with required vibronic Hamiltonian data from `04-NACs`.
* Follow the notebook step-by-step for detailed parameter setups and data visualization.

For further information, refer to the main project documentation (https://github.com/AkimovLab/Project_ML_BP_revision1).
