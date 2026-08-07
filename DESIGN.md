# Project design

## Project goals

The project aims to investigate whether measurable acoustic characteristics can support identification and comparison of Orthoptera species from sound recordings.

The immediate objective is **reproducible acoustic feature extraction**. Classification is deliberately deferred until the variability and reliability of the extracted features are understood.

## Current analysis model

The initial corpus survey showed that there is no single corpus-wide operational definition of an individual chirp.

Different recordings exhibit:

* sustained activity or bouts;
* clearly separated short acoustic events;
* grouped or paired events;
* continuous or strongly modulated activity where individual events are not yet reliably separable.

The production analysis should therefore detect and represent **acoustic observations without prematurely assigning biological labels** such as chirp, syllable or phrase.

The intended analysis is consequently:

```text
WAV
 ↓
recording validation / normalisation
 ↓
time-frequency analysis
 ↓
activity / event detection
 ↓
acoustic event representation
 ↓
feature extraction
 ↓
SQLite
 ↓
comparison
```

The analysis may expose multiple temporal levels where the signal supports them:

```text
Recording
   │
   └── activity segment
          │
          └── acoustic event sequence
                    │
                    └── optional finer structure
```

These are computational descriptions, not assumptions about biological song terminology.

An event may subsequently be interpreted as a chirp, pulse, syllable, or component of a phrase if independent evidence supports that interpretation.

## Acoustic event representation

The canonical representation should retain the source recording and precise timestamps rather than making derived audio clips the primary data.

An acoustic event should be capable of carrying, as appropriate:

* source recording identity;
* start and end timestamps;
* peak or representative time;
* detected frequency band or spectral characteristics;
* amplitude/envelope information;
* quality or confidence information;
* the analysis version and parameters that produced it.

Derived representations such as clipped WAVs, normalised envelopes and spectrograms may be generated from these source intervals for analysis and inspection.

Detection provenance must remain available so that exploratory thresholds or algorithms are not mistaken for biological annotations.

## Frequency and time-frequency analysis

The initial survey found useful event-associated spectral components around both approximately 4 kHz and 16 kHz in the small reference corpus.

A fixed frequency band must therefore not be assumed as a universal preprocessing step.

The selected spectral peak in the exploratory survey is best regarded as an **event-associated spectral feature or activity-band centre**, not automatically as a biological carrier frequency. Future production analysis should use recording-adaptive and multi-band time-frequency methods where necessary.

In particular, candidate detection should not depend on selecting a spectral peak using the same candidate events that are subsequently used to validate that peak.

## Feature extraction

Feature extraction remains separate from event detection and classification.

Candidate features include:

* event duration;
* gap duration;
* repetition and grouping patterns;
* spectral characteristics;
* amplitude/envelope shape;
* normalised temporal representations;
* internal structure where the recording resolution and signal support it;
* higher-order grouping or phrase structure.

Not every feature will be available or meaningful for every recording.

The system should preserve the distinction between:

1. a measurable acoustic property;
2. an inferred temporal grouping;
3. a biological interpretation.

## Comparison

The project has selected Dynamic Time Warping (DTW) as a candidate comparison method for temporal envelope representations because it can accommodate modest timing variation.

The unit supplied to DTW must not yet be assumed to be a biologically defined chirp. It should be selected from the documented acoustic-event representation once event segmentation has been validated.

Within-species variability must be characterised before between-species differences are interpreted.

## Design principles

* Reproducible
* Modular
* Configurable analysis parameters
* Feature extraction separated from classification
* Raw recordings immutable
* Source timestamps and provenance retained for derived observations
* No biological terminology assumed where the signal does not justify it
* Exploratory methods kept distinct from production algorithms

