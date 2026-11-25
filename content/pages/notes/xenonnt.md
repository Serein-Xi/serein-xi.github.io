# XENONnT Analysis Notes

These notes summarize concepts and checks that are useful in dual-phase xenon TPC analysis. They are general study notes rather than a record of collaboration-internal results.

## Detector Signals

### S1: Prompt Scintillation

An interaction in liquid xenon produces prompt scintillation photons. Their detected signal is commonly called S1. Its measured area depends on light collection, photon detection, and signal reconstruction.

### S2: Proportional Scintillation

Ionization electrons drift toward the liquid–gas interface. Electrons extracted into the gas generate proportional scintillation, observed as S2. The signal depends on electron survival, extraction, and amplification.

## Energy Reconstruction

A standard combined-energy estimator is

$E = W \left(\frac{\mathrm{S1}}{g_1}+\frac{\mathrm{S2}}{g_2}\right)$.

The parameter $g_2$ incorporates effects associated with electron extraction and the detected single-electron response. The exact convention should be checked against the analysis software and calibration definitions.

## Reconstruction versus Cut Acceptance

- *Reconstruction efficiency:* fraction of truth-level interactions with a correctly identified reconstructed candidate.
- *Conditional ACE:* fraction of reconstructed candidates that survive analysis cuts.
- *Joint efficiency:* fraction of all generated truth interactions that are reconstructed and pass the required cuts.

The denominator is critical: a cut efficiency conditioned on successful reconstruction is not identical to a total signal acceptance.

## Diagnostic Checklist

- Verify matching between injected truth and reconstructed peaks.
- Check S1/S2 classification and pairing windows.
- Separate failed reconstruction from failed cuts.
- Inspect drift-time, position, and signal-size dependence.
- Quantify uncertainty in low-statistics energy bins.
- Test whether simulated and observed waveform features are consistent.

## Further Reading

For detector and experiment background, consult the public XENONnT collaboration papers and the official documentation relevant to the analysis version in use.
