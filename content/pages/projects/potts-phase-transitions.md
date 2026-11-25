# Machine-Learning Detection of Potts-Model Phase Transitions


[Course Report (PDF)](https://serein-xi.github.io/assets/uploads/potts-project.pdf)


## Overview

This project explores how machine-learning methods can identify phase transitions in the two-dimensional q-state Potts model and how their predictions depend on system size and model parameters.

## Physics Motivation

The Potts model provides a controlled setting in which continuous and first-order phase transitions can be compared. Its known critical temperature provides a reference for assessing data-driven diagnostics.

## Methodology

- Generate spin configurations with cluster Monte Carlo sampling at different temperatures and lattice sizes.
- Compare machine-learning diagnostics with conventional thermodynamic observables.
- Study finite-size effects and sensitivity to the number of spin states.
- Examine where learned classifications become less reliable near phase coexistence.

## Discussion

A useful diagnostic should recover the physical transition rather than simply memorize the arbitrary numerical labels assigned to spin states. Comparisons across different lattice sizes and transition regimes help assess its robustness.
