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

## 2026-08-08 — Exploratory analysis is evidence, not a production interface

Exploratory acoustic analysis is used to investigate candidate representations, detection methods and measurable properties. Its results are evidence for design decisions, but exploratory code does not by itself establish a production API, data structure, algorithm, parameter semantics or storage schema.

For acoustic-event work, three statuses must be distinguished:

* **Decided** — explicitly specified by `DESIGN.md` or established by an architectural decision.
* **Experimentally demonstrated** — observed or implemented in exploratory work, but not adopted as a production contract.
* **Unresolved** — deliberately left open and requiring a further design or scientific decision.

A requirement that an event representation *carry* a property does not, by itself, determine how that property is calculated, normalised, stored or interpreted.

In particular, the exploratory acoustic survey does not establish:

* a production `AcousticEvent` class or API;
* a production event-detection algorithm;
* the semantics or calculation of frequency-band fields;
* a production amplitude or envelope metric;
* a production quality or confidence metric;
* the representation or detection of temporal hierarchy;
* a production database schema.

The structures and parameters used by `exploratory/acoustic_survey.py` may be used as experimental reference material, but must not be promoted into production interfaces by inference.

Where the design establishes a required property but leaves its semantics or implementation unresolved, production implementation requires an explicit decision rather than inference from exploratory code.

This distinction is particularly important before implementing acoustic detection, event storage or downstream comparison. Exploratory parameters must not become production defaults until the representation and detection behaviour have been independently validated, as required by the acoustic-event validation decision.


---

## Recovery entry — early decisions superseded by whole-document refinement

**Original decisions:** 6–7 August 2026
**Recovered into decision journal:** 15 August 2026

During the documentation archaeology, two early decisions were found to have been removed when `DECISIONS.md` was rewritten after the initial local-corpus survey.

The later decisions remain valid historical entries and are not altered by this recovery. This entry restores the earlier decision record and makes the subsequent relationship explicit.

### 2026-08-06 — Use Dynamic Time Warping for temporal-envelope comparison

Decision:

Use Dynamic Time Warping (DTW) on the temporal envelope representation then described as a chirp envelope.

Reason:

DTW was considered more robust to tempo variation than direct correlation.

Alternative considered:

Cross-correlation.

### Later refinement

The 7 August local-corpus survey showed that the unit being compared could not safely be assumed to be a universally defined biological chirp.

The later decision **“DTW applies to validated temporal event representations”** therefore retained DTW while refining what may legitimately be supplied to it.

The historical relationship is:

```text
initial decision
DTW on chirp envelopes
        ↓
survey exposes ambiguity in "chirp"
        ↓
refined decision
DTW on validated temporal event representations
```

The later decision refines the earlier one; it does not mean the earlier decision and its rationale never existed.

---

### 2026-08-07 — Restrict the initial Xeno-canto development corpus

Decision:

For initial development, use recordings satisfying:

```text
gen:Gryllus q:A id?:no len:"10-90"
```

rather than downloading the entire genus.

Rationale:

* keep the initial corpus manageable, at approximately 173 recordings at the time;
* avoid overwhelming early testing;
* use recordings long enough to provide multiple independent samples;
* exclude recordings with uncertain identification;
* start with quality-A material to provide a relatively homogeneous development corpus.

### Later status

This was a **development-corpus scoping decision**, not a claim that the restricted corpus was scientifically sufficient for species-level conclusions.

Subsequent experimental work retained the requirement to use multiple recordings per species and to characterise within-species variability before interpreting between-species differences.

The query and its methodological use remained present elsewhere in the repository, but the fact that its adoption was an explicit project decision had been lost from `DECISIONS.md`. This recovery restores that distinction.
