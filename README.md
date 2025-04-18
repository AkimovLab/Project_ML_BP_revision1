# Project_ML_BP_revision1

**Quantum Confinement Effects in Monolayer Black Phosphorus: Revision of the Nonradiative Recombination Dynamics**

This project investigates the nonradiative recombination dynamics in monolayer black phosphorus using a combination of molecular dynamics, time-dependent DFT, and nonadiabatic coupling calculations.

## Folder Structure and Descriptions

- **01_structure_preparation**  
  Files for structure setup, including the original CIF and generated supercell.

- **02_md**  
  Molecular dynamics simulations: trajectory generation, initial setup, and structural evolution.

- **03_tddft**  
  Time-dependent DFT and hybrid functional calculations. Functionals used: **BHandLYP**, **B3LYP**, **PBE0**.

- **04_nacs**  
  Computation of nonadiabatic couplings in the **SD** and **CI** bases. Also includes plotting tools for spectra, energy vs. time, and NAC maps using data from TD-DFT and MD steps.

- **05_namd**  
  Nonadiabatic molecular dynamics (NA-MD) simulations using the **C++ implementation in Libra**.

## Instructions

Each folder include a `README.md` with:
- A short description of its purpose
- Detailed steps for running the code
- Expected input/output files

Ensure dependencies are met before running simulations (e.g., ASE, DFTB+, Libra, Python 3.x, etc.).

