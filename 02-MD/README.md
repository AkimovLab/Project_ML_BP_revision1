# 02_md – Molecular Dynamics Simulations

This directory contains **DFT-based molecular dynamics (MD)** simulations of monolayer black phosphorus using **CP2K**. Simulations were performed on two systems:

- `pristine` – defect-free monolayer black phosphorus
- `divacancy` – monolayer black phosphorus with a divacancy defect

These simulations generate atomic trajectories used in subsequent TD-DFT and nonadiabatic coupling calculations.

---

## 🧪 General Simulation Setup

- **Software**: CP2K
- **Method**: DFT (GPW)
- **XC Functional**: PBE with DFT-D3 dispersion
- **Basis Set**: DZVP-MOLOPT-GTH
- **Pseudopotential**: GTH-PBE
- **Time Step**: 1 fs
- **Total Steps**: 3000
- **Ensemble**: NVT (Constant volume and temperature)
- **Thermostat**: CSVR, 300 K, time constant 15 fs

---

