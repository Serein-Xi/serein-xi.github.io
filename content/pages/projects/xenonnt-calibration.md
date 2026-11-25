# XENONnT Detector Calibration & Energy Reconstruction

## Overview

The XENONnT experiment is a dual-phase xenon time-projection chamber designed for low-background searches. A particle interaction in the liquid xenon can produce prompt scintillation light (S1) and ionization electrons, which give rise to a secondary scintillation signal (S2) after extraction into the gas phase.

This project focuses on detector-response characterization during Science Run 2 (SR2), with particular emphasis on energy calibration and the light/charge response.

## Physics Motivation

The reconstructed energy depends on the detector response to scintillation photons and ionization electrons. Combining S1 and S2 can reduce the effect of their anti-correlation and improve the energy estimate.

A commonly used combined-energy relation is

$E = W \left(\frac{\mathrm{S1}}{g_1}+\frac{\mathrm{S2}}{g_2}\right)$,

where $W$ is the average work function for producing a quantum, $g_1$ is the detected S1 signal per produced scintillation photon, and $g_2$ is the detected S2 signal per produced ionization electron.

## Research Questions

- How do the effective gains $g_1$ and $g_2$ vary between science runs?
- What detector effects influence the electron extraction efficiency and charge response?
- How do energy scale and resolution depend on energy and detector conditions?
- Which calibration and selection effects contribute to systematic uncertainty?

## Analysis Approach

### Calibration Samples

Monoenergetic calibration lines constrain the relationship between S1, S2, and deposited energy. The calibration strategy covers a range of energies to test the combined-energy model.

### Gain Determination

The light and charge gains can be inferred from the S1–S2 anti-correlation across calibration lines, with appropriate checks for position-dependent corrections and selection biases.

### Energy Resolution

The reconstructed-energy distribution is studied around calibration peaks. Resolution trends are compared across energies and data-taking periods, with statistical and systematic effects considered separately.

## My Focus

- Gain calibration and cross-run detector-response comparisons
- Electron extraction efficiency and charge-response studies
- Energy-scale consistency and resolution characterization
- Numerical fitting, diagnostic plots, and validation checks

## Status

Ongoing analysis. Public quantitative results and figures will be linked here once approved for release by the collaboration.
