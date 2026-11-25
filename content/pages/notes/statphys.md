# Statistical Physics Notes

These notes focus on phase transitions, numerical sampling, and the two-dimensional Potts model.

## The Potts Model

In the $q$-state Potts model, each lattice site carries one of $q$ discrete spin states. Neighboring spins contribute a lower energy when they agree.

A common Hamiltonian is

$H = -J \sum_{\langle i,j\rangle} \delta_{s_i,s_j}$,

where $J > 0$ favors aligned neighbors and the sum runs over nearest-neighbor pairs.

## Phase Transitions in Two Dimensions

For the ferromagnetic square-lattice Potts model in the thermodynamic limit, transitions are continuous for $q \le 4$ and first-order for $q > 4$.

For the usual choice $k_B = J = 1$, the exact transition temperature is

$T_c = \frac{1}{\ln(1+\sqrt{q})}$.

## Monte Carlo Sampling

Representative approaches include local updates, cluster algorithms, and replica-exchange or parallel-tempering methods. Sampling near a first-order transition is difficult because configurations may remain trapped in one phase for long periods.

## Practical Diagnostics

- Energy histograms and coexistence near the transition
- Autocorrelation and effective sample size
- Round trips between temperatures in parallel tempering
- Overlap between neighboring temperature ensembles
- Consistency between independently initialized replicas
- Finite-size behavior of peaks and free-energy barriers

## Machine Learning as an Analysis Tool

Dimensionality reduction and generative models can provide alternative views of phase structure, but quantitative physical conclusions require validation against known thermodynamic observables and well-mixed Monte Carlo baselines.

## Planned Extensions

- Finite-size scaling across lattice sizes
- Barrier estimation and uncertainty quantification
- Comparison of generative approaches with Monte Carlo references
