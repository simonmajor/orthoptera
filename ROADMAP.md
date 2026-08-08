# Orthoptera Roadmap

This roadmap describes the path from the current exploratory work to a reproducible system for analysing and comparing orthopteran acoustic recordings.

It deliberately distinguishes between three states:

* **Decided** — an architectural or methodological requirement has been explicitly established in `DESIGN.md` or `DECISIONS.md`.
* **Demonstrated** — an approach or observation has been explored in code or experiments, but this does not by itself make it the production specification.
* **Unresolved** — the repository does not yet contain enough evidence or an explicit decision to determine the production behaviour.

The roadmap therefore does **not** treat every unchecked item as an implementation task. Some items must first be resolved through experiment, annotation, or an explicit design decision.

---

## 1. Establish the acoustic-event representation

### Status: conceptually defined; production representation not yet implemented

The project has adopted a **neutral acoustic-event representation**. An event is a computational observation in a recording, not an assumed biological unit such as a chirp, syllable, pulse, phrase, or song element.

The representation is required to be capable of retaining:

* source recording identity;
* start and end timestamps;
* a peak or representative time;
* frequency-band or other spectral characteristics;
* amplitude or envelope information;
* quality or confidence information; and
* the analysis version and parameters that produced the observation.

Source timestamps and detection provenance are primary. Derived audio clips are secondary.

The representation must remain sufficiently general to accommodate both discrete acoustic events and sustained or repeated acoustic activity.

### Already demonstrated

`exploratory/acoustic_survey.py` currently produces a flat set of candidate events containing:

* peak time;
* start time;
* end time;
* duration; and
* prominence.

It also records recording-level signal and envelope statistics and the detector parameters used.

This provides a concrete experimental reference, but does **not** establish that the exploratory output is the final production data model.

### Still to establish

The repository does not yet define:

* a production `AcousticEvent` type or equivalent interface;
* the precise representation of per-event spectral characteristics;
* the precise per-event amplitude/envelope measurements;
* the semantics of quality/confidence;
* the complete provenance model; or
* the representation of higher temporal levels.

These should not be silently inferred from the exploratory implementation.

---

## 2. Independently validate acoustic-event detection

### Status: required; not yet started

Detection must be validated against independently reviewed intervals before exploratory parameters become production defaults.

The current exploratory work has generated candidate events and allowed their behaviour to be inspected, but it does not constitute independent ground-truth validation.

### Required work

Establish an independently reviewed set of recordings and intervals against which candidate-event detection can be assessed.

The validation work needs to establish, empirically:

* what constitutes an acceptable detected interval;
* how reliably the detector identifies relevant acoustic activity;
* where false detections occur;
* how sensitive results are to recording characteristics; and
* whether the exploratory detection behaviour is sufficiently reproducible to support production use.

The annotation and evaluation methodology is itself currently unresolved and should be documented when established.

### Important constraint

Exploratory detector parameters must **not** become production defaults merely because they worked on the existing examples.

The existing per-recording settings demonstrate that detector behaviour is currently corpus-dependent.

---

## 3. Establish time-frequency and activity/event detection

### Status: experimentally explored; production method unresolved

The initial experiments identified useful acoustic components around approximately 4 kHz and 16 kHz in the small reference corpus.

This demonstrated that a fixed universal frequency band should not be assumed.

The design therefore calls for recording-adaptive and, where necessary, multi-band time-frequency analysis.

### Already demonstrated

The exploratory analyses have investigated:

* spectral components at different frequencies;
* envelope-based detection;
* alternative frequency-band choices;
* peak prominence;
* event widths; and
* temporal spacing between detected events.

`exploratory/acoustic_survey.py` currently uses a recording-level spectral estimate and a single detector band rather than implementing a general multi-band event detector.

### Still unresolved

The repository does not yet establish:

* how many frequency bands should be analysed;
* how bands should be selected;
* whether an event detected in multiple bands is one event or multiple observations;
* how detections from different bands should be associated;
* what spectral representation should be retained for an event; or
* what frequency resolution is required.

These are methodological questions, not implementation details to be invented by a coding agent.

---

## 4. Establish acoustic-event features

### Status: partially demonstrated; production feature set unresolved

The exploratory work already provides several measurements, including:

* event duration;
* inter-event interval;
* peak time;
* start/end interval;
* envelope prominence; and
* recording-level amplitude and envelope statistics.

These demonstrate that temporal and envelope-derived features can be extracted from the recordings.

### Still unresolved

The production representation has not yet established exactly which per-event measurements are canonical.

In particular, the design requires the representation to be capable of carrying amplitude/envelope and spectral information, but does not currently prescribe:

* a particular amplitude measurement;
* an energy measurement;
* a normalization scheme;
* a particular spectral summary; or
* the semantics of prominence as a quality/confidence measure.

Feature extraction should therefore follow the validated event representation rather than being defined implicitly by whichever measurements happen to be convenient in the detector implementation.

---

## 5. Establish temporal structure above individual events

### Status: design principle established; representation unresolved

The design allows multiple temporal levels:

```text
Recording
└── Activity segment
    └── Acoustic event sequence
        └── Optional finer structure
```

These levels are computational observations and must not be assumed to correspond directly to biological terminology.

The exploratory implementation currently produces a **flat list of events**. Experiments have investigated interval-level and within-interval structure, but no production hierarchy has been established.

### Still unresolved

The repository does not yet define:

* what constitutes an activity segment;
* what constitutes an event sequence;
* the temporal criteria for grouping events;
* whether hierarchy is explicitly stored or derived;
* how activity at different frequencies participates in grouping; or
* what finer structure, if any, should be represented.

This work should follow empirical validation rather than being introduced merely because the conceptual hierarchy exists in the design.

---

## 6. Define reproducible analysis provenance

### Status: requirement established; production provenance model incomplete

Every derived acoustic representation must retain sufficient information to identify the analysis that produced it.

The exploratory implementation already records detector settings and an analysis version, but other analysis choices remain embedded in the exploratory code.

The production provenance requirement includes the analysis version and parameters used to produce the result.

### Still to establish

The project needs to determine the complete set of analysis information that materially affects reproducibility, including the status of currently hard-coded analysis choices.

The resulting provenance model should be established alongside the validated production representation rather than being inferred from the implementation of the exploratory prototype.

---

## 7. Store the canonical acoustic representation

### Status: SQLite selected; schema unresolved

The intended analysis pipeline includes SQLite as the persistent store for the canonical acoustic representation.

The exploratory work currently writes CSV and JSON outputs rather than a database.

Production database modules are currently stubs.

### Still unresolved

No production database schema has yet been defined for:

* recordings;
* acoustic events;
* provenance;
* temporal hierarchy; or
* relationships between observations at different levels.

The database schema therefore depends on decisions still outstanding in the event representation and temporal model.

---

## 8. Compare validated temporal representations

### Status: architectural direction established; implementation deferred

Dynamic Time Warping (DTW) is intended to operate on **validated temporal event representations**, rather than being applied directly to arbitrary raw recordings.

The event representation must therefore be established and validated before DTW becomes part of the production comparison pipeline.

### Dependency

DTW should not drive the definition of the acoustic-event representation. The representation must first be shown to be a meaningful and reproducible description of the recordings.

The precise temporal representation supplied to DTW remains dependent on the preceding feature and event-validation work.

---

## 9. Classification and clustering

### Status: downstream work; dependent on earlier stages

Classification and clustering are intended to operate on established acoustic representations rather than raw exploratory measurements.

The production approach depends on first establishing:

1. a validated event representation;
2. appropriate temporal and spectral features;
3. reproducible provenance;
4. persistent storage; and
5. validated comparison methods.

No classification or clustering method should be treated as established merely because a suitable implementation could be constructed.

---

## 10. Overall sequence

The practical progression is therefore:

```text
Exploratory observations
        │
        ▼
Independent event annotation / validation
        │
        ▼
Validated acoustic-event representation
        │
        ├── temporal features
        ├── spectral features
        ├── amplitude / envelope features
        └── quality / provenance
        │
        ▼
Temporal structure
(activity segments / event sequences, where justified)
        │
        ▼
Canonical SQLite representation
        │
        ▼
Validated temporal comparison
        │
        ├── DTW
        ├── classification
        └── clustering
```

The arrows represent dependencies, not necessarily separate software modules.

In particular, the exploratory detector should not be treated as the first production component simply because it is currently the most complete piece of code. Its main value at this stage is as an experimental reference against which the eventual production representation and detection method can be evaluated.

---

## Current position

The project has moved beyond the question of *whether* acoustic-event representation is useful. The exploratory work demonstrates that event-level temporal and spectral analysis is viable and has exposed important variation between recordings.

The immediate challenge is now to turn those observations into **validated, explicitly defined representations without accidentally promoting experimental choices into architectural decisions**.

The principal outstanding work is therefore:

* independent event annotation and validation;
* resolving the production meaning of spectral characteristics;
* resolving per-event amplitude and quality/confidence measures;
* determining whether and how temporal hierarchy is supported;
* establishing complete analysis provenance; and
* defining the persistent representation once those preceding questions are sufficiently settled.

Only after these foundations are established should the production detector, database, comparison, classification, and clustering components be treated as straightforward implementation work.

