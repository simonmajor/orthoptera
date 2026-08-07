## 2026-08-07 — Neutral acoustic-event representation

Decision:

Production detection will initially represent **acoustic events** rather than assuming that every detected event is a biological chirp, syllable or pulse.

Reason:

The initial six-recording survey found materially different temporal structures. *Gryllus campestris* provides clear short separated events; *Gryllus bimaculatus* shows short events that may form pairs or larger groups; the two *Roeseliana roeselii* recordings contain sustained activity and modulation in which the exploratory short candidates are not credible standalone chirps; and the mystery recording does not yet provide a stable event definition.

A neutral computational event allows the signal-processing layer to report reproducible observations without embedding an unvalidated biological interpretation.

The architecture may expose multiple temporal levels, including activity segments, event sequences and finer structure where resolvable. These levels must be treated as computational observations until independently supported as biological units.

Consequences:

* The production detector must not require a universal chirp definition.
* Source timestamps and detection provenance are primary; derived clips are secondary artefacts.
* Event quality/confidence should be retained.
* Biological labels such as chirp, syllable and phrase should only be assigned by later analysis when justified by evidence.
* Detection must be validated against independently reviewed intervals before exploratory parameters become production defaults.

## 2026-08-07 — DTW applies to validated temporal event representations

The existing decision to use Dynamic Time Warping remains in force, but "chirp envelope" is no longer assumed to mean a universally defined biological chirp.

DTW is intended for comparing suitable normalised temporal representations of acoustic events once the relevant event unit and segmentation have been established empirically.

Reason:

The initial corpus survey demonstrated that the same exploratory event detector does not identify equivalent biological units across all recordings. Applying DTW to an incorrectly defined unit would give a precise comparison of the wrong thing.

The event representation supplied to DTW must therefore be selected and documented as part of the validated feature-extraction methodology.

