# 04-NACs - Non-Adiabatic Couplings Calculation

This directory focuses on the computation of Non-Adiabatic Couplings (NACs) using the Libra package as part of the Project\_ML\_BP\_revision1 repository. It includes separate workflows for pristine and divacancy defect systems, both of which share similar file structures and calculation methodologies.

## Directory Structure

```
04-NACs/
├── pristine/
│   ├── pristine.ipynb
│   ├── res/
│   ├── res-ks-DFT/
│   ├── res-mb-sd-DFT/
│   └── all_logfiles/
├── divacancy/
│   ├── divacancy.ipynb
│   ├── res/
│   ├── res-ks-DFT/
│   ├── res-mb-sd-DFT/
│   └── all_logfiles/
```

* **pristine/** - NAC calculations for the pristine system.
* **divacancy/** - NAC calculations for the divacancy defect system.
* **res/** - Directory for storing raw NAC data.
* **res-ks-DFT/** - NACs in the Kohn-Sham basis.
* **res-mb-sd-DFT/** - NACs in the many-body and single-particle excited state bases.
* **all\_logfiles/** - CP2K log files and TD-DFT data used for NAC calculations.

## Notebooks Overview

### `pristine.ipynb` / `divacancy.ipynb`

* Workflow for computing NACs using molecular orbital overlap files generated in `03-OVERLAPS`.
* Analysis of NACs in both Kohn-Sham and excited state bases.
* Visualization of energy levels, density of states, NAC maps, and influence spectra.

### Key Analysis Sections:

* Importing Libraries
* Overview of Input Data
* NAC Computation (Kohn-Sham and Excited States)
* Plotting Energy vs. Time
* Visualizing NAC Maps and Distributions
* Influence Spectrum Analysis

## Dependencies

* Python 3.x
* CP2K (2025.1 or later)
* Libra (AkimovLab version)
* MPI (Intel MPI or OpenMPI)
* Jupyter Notebook
* numpy, scipy, matplotlib, h5py

## Setup and Execution

1. **Environment Setup:**

```bash
module load intel-mpi-7
source activate /path/to/libra/environment
export CP2K_HOME="/path/to/cp2k"
export PATH="$CP2K_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CP2K_HOME/lib:$LD_LIBRARY_PATH"
```

2. **Input Preparation:**

* Ensure overlap files from `03-OVERLAPS` are located in the respective `res/` directory.
* Update paths and parameters in the Jupyter notebooks as needed.

3. **Running the Notebooks:**

```bash
cd 04-NACs/pristine
jupyter notebook pristine.ipynb
```

4. **Output Files:**

* `res/`: Raw NAC data
* `res-ks-DFT/`: Kohn-Sham NACs
* `res-mb-sd-DFT/`: Excited state NACs
* `all_logfiles/`: Log files from electronic structure calculations

## Notes

* The pristine and divacancy workflows are structurally identical and differ only in input data.
* Modify file paths and computational parameters in the notebooks to suit your system.
* For further details, refer to the (https://github.com/AkimovLab/Project_ML_BP_revision1).
