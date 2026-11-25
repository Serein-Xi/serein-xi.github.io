# Probing Metastability and Free-Energy Barriers with Discrete Diffusion Models

## Overview

This project investigates metastability and free-energy barriers in the two-dimensional Potts model using Monte Carlo benchmarks and discrete generative models. The objective is to understand whether a learned distribution can reproduce physically meaningful phase coexistence and rare configurations.

## Physics Motivation

At a first-order phase transition, ordered and disordered phases may coexist. The suppression of intermediate configurations provides information about the free-energy barrier separating the phases. Capturing this suppression is an important test of a generative model beyond reproducing average observables.

## Methodology

- Generate equilibrium reference configurations using cluster Monte Carlo and parallel tempering.
- Analyze energy histograms, phase coexistence, finite-size effects, and free-energy barriers.
- Investigate discrete diffusion models suited to categorical spin configurations.
- Compare generated and reference distributions, including rare configurations and symmetry-sensitive observables.

## Research Questions

- Can discrete generative models faithfully represent both coexisting phases and the low-probability region between them?
- How does model performance depend on lattice size and the strength of the first-order transition?
- What can denoising trajectories reveal about the learned statistical structure?

## Status

Ongoing research; quantitative comparisons and figures will be added when validated.
