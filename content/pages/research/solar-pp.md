# Solar pp Neutrino ACE

## Overview

Low-energy electronic-recoil events are relevant to solar pp neutrino measurements in liquid-xenon detectors. At low signal sizes, a physically produced event may fail to be reconstructed or may be rejected by an analysis selection.

This project studies reconstruction efficiency and analysis-cut efficiency (ACE), with emphasis on separating losses arising at different stages of the event-processing pipeline.

## Motivation

A reliable efficiency model should account not only for cuts applied to reconstructed events, but also for the probability that a simulated signal is recognized and correctly paired as an event in the first place.

A useful decomposition is

$\epsilon_{\mathrm{joint}} = \epsilon_{\mathrm{reco}}\times\epsilon_{\mathrm{ACE}\mid\mathrm{reco}}$.

Here, the reconstruction term measures whether an injected interaction produces a valid reconstructed candidate, while the conditional ACE term measures acceptance among candidates for which cut decisions are available.

## Methodology

### 1. Signal Simulation

Generate electronic-recoil signals using Fuse with controlled truth information, including deposited energy and interaction position.

### 2. Waveform Injection

Use Saltax to embed simulated signals into detector data so that reconstruction is tested in the presence of realistic background activity and neighboring signals.

### 3. Reconstruction and Matching

Process the resulting waveform streams through the straxen reconstruction chain. Match reconstructed objects to injected truth and diagnose missing or mispaired S1/S2 signals.

### 4. Efficiency Estimation

Estimate energy-dependent reconstruction efficiency, conditional ACE, and their combined efficiency. Statistical uncertainties and sampling weights must be handled consistently.

### 5. Failure Diagnostics

Study failure categories such as unresolved or misclassified peaks, unsuccessful S1–S2 pairing, proximity-related losses, and shadow or veto selections. Examine correlations with drift time and interaction position.

## Analysis Questions

- How does reconstruction efficiency behave near the lowest detectable energies?
- Which classes of failure dominate when energy increases?
- Can waveform-level diagnostics identify systematic event-building losses?
- How do signal size, drift time, detector position, and local background activity influence efficiency?

## Status

Active methodological study. Results shown on this public site will be limited to material cleared for public release.
