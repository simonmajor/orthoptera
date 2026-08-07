# Experimental history

This document records exploratory signal-processing work carried out before
the Orthoptera project was formalised.

The scripts in `pre_project_prototypes/` are preserved historical snapshots.
They are not part of the production analysis API and should not be treated as
successive production implementations. They document hypotheses, failed or
misleading approaches, and measurements that informed the subsequent project
design.

## 1. Original mystery recording

The original recording was made on 2026-07-11 at 23:08:17 in NW Kent, on the
North Downs. The original WAV is approximately 87.83 s long, 48 kHz, 24-bit
PCM.

A 7.40 s repetitive section was extracted as `creature7s.wav` for exploratory
analysis. This sample is preserved in `pre_project_prototypes/`.

The objective was to identify an unknown Orthoptera sound and, in particular,
to distinguish between acoustically similar species rather than merely
determine that the sound was a cricket.

## 2. Evidence and limits of the reconstruction

The sequence is established by the snapshot names and the supplied results in
this document, not by development commits: all five scripts and the WAV were
imported together in commit `a076a1f`. There is no Git history between them.

The WAV is mono, 48 kHz, and 24-bit PCM. The current test copy has the same
SHA-256 digest as `pre_project_prototypes/creature7s.wav`.

No saved console output or generated plots for analyses 4--5 are present.
They were therefore rerun, without source changes, on the preserved WAV using
the repository's `.venv`; the results are identified below as rerun results,
not as previously preserved historical output. The rerun reproduced the
existing recorded results for analyses 1--3. Terms such as *carrier*, *chirp*,
and *syllable* are working labels, not validated biological annotations.

## 3. analyse1.py — global-spectrum pulse analysis

The script converts the WAV to mono floating point, removes its mean, and
selects the maximum of the full-recording magnitude spectrum. It makes a
fourth-order band-pass ±500 Hz around that maximum, takes the Hilbert-magnitude
envelope, smooths it with a 501-sample Savitzky--Golay filter, and detects
peaks above mean + 0.5 SD with a 20 ms minimum separation. It plots
autocorrelation but does not calculate a value from it.

Observed result:

- Sample rate: 48,000 Hz
- Duration: 7.40 s
- Global spectral maximum: 104.1 Hz
- Detected peaks (called pulses): 180
- Mean interval: 0.0412 s
- Pulse rate: 24.26 Hz

The existing record judged the 104.1 Hz result unlikely to be the audible
cricket carrier and interpreted it as a lower-frequency periodic component or
modulation. That is an interpretation, not a biological identification. It
motivated the explicit change in `analyse2.py`: restrict the spectral search.

## 4. analyse2.py — constrained high-frequency peak

Relative to `analyse1.py`, the only signal-processing change is selection of
the spectral maximum within 3.5--7 kHz. The same ±500 Hz filter, envelope,
smoothing, peak detection, and plots are then used.

Observed result:

- Spectral maximum within 3.5--7 kHz: 4638.8 Hz
- Detected peaks (called pulses): 132
- Mean interval: 0.0558 s
- Pulse rate: 17.93 Hz

The record considered this high-frequency maximum more plausible than the
104.1 Hz whole-spectrum maximum, but did not validate it as a species-specific
carrier. `analyse3.py` then separates a narrow carrier estimate from slower
envelope measurements rather than using one result for both purposes.

## 5. analyse3.py — narrow carrier and envelope-modulation analysis

This script uses a Hann window before estimating the maximum in a 3--7 kHz
search region, then a sixth-order ±150 Hz band-pass around it. Its Hilbert
envelope is low-pass filtered at 80 Hz and mean-centred. It separately finds
the largest non-DC component of the windowed envelope spectrum below 100 Hz
and detects envelope peaks with 0.5-SD prominence and 25 ms minimum spacing.

Observed result:

- Carrier estimate: 4688.11 Hz
- Largest reported envelope modulation component: 2.97 Hz
- Detected envelope peaks: 105
- Mean spacing: approximately 0.0702 s
- Equivalent envelope peak rate: approximately 14.24 Hz

This processing chain produced distinct several-kHz, roughly 14 Hz, and
2.97 Hz quantities. It does not assign those quantities to biological carrier,
syllable, chirp, or phrase levels. The record therefore retained the slower
modulation's interpretation as uncertain. `analyse4.py` changes the target
unit from envelope peaks to threshold-defined intervals labelled chirps, then
attempts within-interval structure; no preserved result states a more specific
observation that required that change.

## 6. analyse4.py — threshold-defined chirps and attempted internal counts

This is the key transition to per-interval measurements. It fixes a
fourth-order 3.5--7 kHz band-pass before estimating its spectrum maximum. It
calculates a Hilbert envelope, smooths it with a 2 ms moving average, and uses
consecutive samples above mean + 0.8 SD as start/end pairs labelled chirps;
unmatched boundary pairs are discarded.

For each interval of at least 15 ms, it finds peaks in the absolute filtered
waveform at least 30% of that interval's maximum and at least `fs / 600`
samples apart. It labels their count “syllables,” divides it by interval
duration for a “syllable rate,” and reports mean retained duration, count,
rate, and reciprocal mean spacing of all detected interval starts.

Compared with `analyse3.py`, it replaces the 80 Hz envelope low-pass,
modulation FFT, and envelope `find_peaks` procedure with threshold crossings,
per-interval duration, and an attempted internal-peak count. It also replaces
the data-centred ±150 Hz filter with a fixed broad band.

### Rerun results

The unmodified snapshot reports:

- Carrier-frequency estimate: 4638.8 Hz
- Detected threshold intervals (called chirps): 294
- Retained intervals of at least 15 ms: 4
- Mean retained interval duration: 17.8 ms
- Mean labelled syllables per retained interval: 9.0
- Mean labelled syllable rate: 508.2 Hz
- Reciprocal mean spacing of all interval starts: 40.04 Hz

The contrast between 294 detected intervals and four retained intervals is a
measured result of this processing chain. In particular, “syllable” remains
only a code label: it is a peak count in the absolute band-passed waveform,
not an independently annotated syllable count. The summary mixes populations:
duration/count/rate exclude intervals shorter than 15 ms, while repetition
uses all detected starts. These are prototype limitations, not measured
biological results.

## 7. analyse5.py — smoothed-envelope peak and width statistics

`analyse5.py` keeps the fixed 3.5--7 kHz filter and spectrum maximum but
replaces `analyse4.py`'s threshold intervals and internal waveform-peak
counts. It normalises the Hilbert envelope, low-pass filters it at 30 Hz,
renormalises it, and detects prominent envelope maxima with prominence 0.15
and at least 150 ms spacing. Half-prominence widths are used as chirp-width
estimates; the script reports mean interval, reciprocal interval, interval SD,
CV, and mean and median widths.

### Rerun results

The unmodified snapshot reports:

- Carrier-frequency estimate: 4638.8 Hz
- Detected envelope peaks (called chirps): 24
- Mean interval: 0.304 s
- Repetition rate: 3.29 Hz
- Interval SD: 0.065 s
- CV: 0.215
- Mean half-prominence width: 31.4 ms
- Median half-prominence width: 27.3 ms

This supports a move toward chirp-centred duration and variability statistics,
but does not record why 30 Hz, 150 ms, and 0.15 were chosen or establish that
the peaks are biological chirps. The later reference summaries use similar
statistics, but the repository does not prove that this script generated them.

## 8. Comparison recordings

To assess whether apparently distinctive measurements are actually
species-discriminating, reference recordings were obtained from Xeno-canto.

Initial comparison material includes:

- `XC1085943` — *Acheta domesticus* (House Cricket)
- `XC940663` — *Gryllus bimaculatus* (Two-spotted Cricket)
- `XC925129` — *Gryllus campestris* (Field Cricket)
- `XC924802` — *Roeseliana roeselii*
- `XC924980` — *Roeseliana roeselii*

The comparison strategy is important: measurements should be evaluated across
multiple recordings of the same species before being treated as species-level
features.

## 9. Initial reference measurements

### Acheta domesticus

Reference recording `XC1085943`:

- Sample rate: 44,100 Hz
- Duration: 8.39 s
- Carrier frequency: 4312.2 Hz
- Detected chirps: 6
- Mean interval: 0.440 s
- Repetition rate: 2.27 Hz
- Interval SD: 0.209 s
- CV: 0.475
- Mean chirp width: 22.2 ms
- Median chirp width: 22.0 ms

### Gryllus bimaculatus

Reference recording `XC940663`:

- Sample rate: 44,100 Hz
- Duration: 29.29 s
- Carrier frequency: 4460.1 Hz
- Detected chirps: 55
- Mean interval: 0.530 s
- Repetition rate: 1.89 Hz
- Interval SD: 0.126 s
- CV: 0.238
- Mean chirp width: 24.1 ms
- Median chirp width: 24.2 ms

These measurements are exploratory only. In particular, a single recording is
insufficient to establish a species-level difference.

## 10. Useful conclusions carried into the project

The later work shifted from detecting a single global periodicity towards
analysing individual chirps and their temporal structure.

Candidate features include:

- carrier frequency;
- chirp duration;
- inter-chirp interval;
- ratio of chirp duration to gap;
- variability of each of the above;
- amplitude/envelope shape;
- internal pulse structure;
- relationships between pulses within a chirp;
- slower phrasing/grouping patterns;
- higher-order behavioural structure.

Dynamic Time Warping (DTW) is a candidate method for comparing individual
chirp envelopes or other temporal representations when small timing
differences should not dominate the comparison.

Because the target species may use similar stridulatory mechanisms and occupy
similar acoustic bands, the project should expect relatively subtle
differences. Consequently, within-species variability must be characterised
before between-species differences are interpreted.

## 11. Sampling strategy

For reference recordings containing many chirps, analysis should preferably
select several chirps at randomly separated positions rather than relying on
a single arbitrarily chosen chirp.

The analysis should report both central tendency and variability. Useful
sanity checks include:

- minimum number of successfully detected chirps;
- standard deviation;
- coefficient of variation;
- detection failures/outliers;
- consistency of carrier-frequency estimates;
- consistency of chirp boundaries;
- sensitivity to the random sample.

If a randomly selected sample produces an anomalously large variance or fails
a quality threshold, repeating the random selection is acceptable during
exploration, but the final methodology should record the selection and not
silently discard inconvenient samples.

## 12. Xeno-canto reference corpus

The project should ultimately compare multiple recordings per species rather
than treating one Xeno-canto recording as representative.

A useful initial query is:

    gen:Gryllus q:A id?:no len:"10-90"

This currently produces approximately 173 recordings and is substantially
more manageable for development/testing than an unrestricted
`gen:Gryllus` query.

The Xeno-canto client therefore supports a future corpus-building workflow
in which recordings and their metadata can be cached locally and analysed
reproducibly.

## 13. Approaches not to carry forward

The following prototype approaches must not become production analysis rules:

1. Selecting a whole-recording global spectral maximum and treating it as a
   biological carrier or species feature (`analyse1.py`).
2. Treating a frequency-window-constrained maximum as validation of a carrier;
   the window can select the desired region by construction (`analyse2.py`).
3. Treating any fixed threshold, smoothing cutoff, duration, prominence, or
   spacing parameter in analyses 3--5 as established. These were exploratory
   constants and need configurable, tested justification.
4. Treating threshold-defined intervals or peaks in an absolute filtered
   waveform as annotated chirps or syllables (`analyse4.py`).
5. Inferring a species-level feature or performance claim from the single
   7.40 s target excerpt or any single reference recording.
6. Copying the monolithic, hard-coded-filename scripts into production. Their
   plots overwrite fixed names and their analysis parameters and provenance
   are not recorded as reproducible outputs.

## 14. Status of conclusions

No feature identified during these experiments should currently be regarded
as a validated species discriminator.

The principal conclusions from the exploratory phase are methodological:

1. Broadband dominant-frequency detection can identify the wrong temporal
   structure.
2. Carrier frequency and temporal modulation should be analysed separately.
3. Individual chirps are likely to be a more useful unit of comparison than
   arbitrary fixed-duration windows.
4. Chirp duration, gap duration, envelope shape and internal structure are
   promising candidate features.
5. Higher-order phrasing/grouping may contain additional behavioural
   information.
6. Within-species variability must be measured before interpreting subtle
   between-species differences.
7. Multiple independent Xeno-canto recordings are therefore required for
   meaningful reference distributions.
8. Exploratory scripts are retained to preserve the reasoning history, but
   production algorithms should be rebuilt as tested project components rather
   than copied mechanically from the prototypes.

## 15. Initial local-corpus acoustic survey (2026-08-07)

### Scope and reproducibility

The six local WAVs in `tests/data/` were surveyed using
`exploratory/acoustic_survey.py` (analysis version
`exploratory-acoustic-survey-1`).  It is deliberately an exploratory script,
not a production `signal.detect` implementation.  It preserves raw WAVs and
writes its CSV/JSON/PNG outputs to a caller-selected directory outside Git.

The procedure first records full-waveform and spectrogram diagnostics.  For a
short-event experiment it then selects the largest Welch PSD peak above 2 kHz,
uses a 4th-order +/-600 Hz band-pass, a Hilbert envelope smoothed for 10 ms,
and finds peaks in a 200 Hz representation.  The minimum peak separation is
80 ms; prominence is 6 median absolute deviations (MAD), except 4 MAD for
`XC924802` and `creature7s`.  Event boundaries are half-prominence widths.
Those two exceptions were chosen after visual inspection and are evidence that
the procedure is parameter-sensitive.  Neither the peaks nor their boundaries
are biological chirp annotations.

### Measured observations

| Recording | WAV metadata | exploratory band centre | exploratory candidate-event result |
| --- | --- | ---: | --- |
| XC1085943, *Acheta domesticus* | 44.1 kHz, 16-bit PCM, mono, 8.390 s | 4.354 kHz | 24 candidates; median half-prominence duration 8.4 ms; median peak interval 140 ms (interval CV 1.27) |
| XC924802, *Roeseliana roeselii* | 44.1 kHz, 16-bit PCM, stereo, 16.621 s | 16.575 kHz | 40 candidates; 6.2 ms; 314 ms (CV 0.91) |
| XC924980, *Roeseliana roeselii* | 96 kHz, 24-bit PCM, stereo, 23.938 s | 16.034 kHz | 54 candidates; 5.8 ms; 120 ms (CV 3.04) |
| XC925129, *Gryllus campestris* | 48 kHz, 16-bit PCM, stereo, 52.058 s | 4.304 kHz | 246 candidates; 19.4 ms; 100 ms (CV 0.73) |
| XC940663, *Gryllus bimaculatus* | 44.1 kHz, 32-bit IEEE-float, stereo, 29.286 s | 4.439 kHz | 108 candidates; 15.3 ms; 249 ms (CV 0.67) |
| creature7s (mystery excerpt) | 48 kHz, 24-bit PCM, mono, 7.403 s | 4.639 kHz | 42 candidates; 10.3 ms; 180 ms (CV 0.37) |

Dynamic range differs substantially: RMS normalised sample level ranges from
0.00219 (`XC1085943`) and 0.00250 (`XC925129`) to about 0.073 for the two
*R. roeselii* recordings.  Detection thresholds cannot therefore be based on
an absolute WAV amplitude.

SciPy reports that the `XC1085943` RIFF data length is four bytes longer than
the file contains.  This is only two 16-bit mono samples and has no practical
effect on the reported 8.390 s analysis, but a production importer should
record or surface malformed-file warnings rather than suppress them silently.

`XC925129` contains conspicuous, repeated, broadband/harmonic short events
with a stable roughly 0.1 s local cadence for much of the recording.  The
procedure follows these events reasonably well, though it also captures a
weaker later portion and misses/changes behaviour when amplitude falls.
`XC940663` contains strongly separated, similarly shaped short events with
visible harmonic bands.  It also has shorter spacings near 95 ms and longer
gaps: the 108 short candidates are therefore not equivalent to the 55
widely-spaced envelope peaks reported by the historical experiment.  This is
direct evidence of temporal hierarchy rather than a contradiction.

`XC1085943` has a globally dominant low-frequency component near 255 Hz, but
the exploratory high-frequency selection finds weak 4.35 kHz transients.  Its
large interval variation and low level make its event grouping ambiguous.

Both *R. roeselii* recordings have strong activity near 16--16.6 kHz and
visible long activity bouts separated by silence, a useful within-species
similarity at this recording level.  They differ greatly in bout timing and
level: `XC924802` is largely two sustained noisy sections separated by a
brief quiet gap, while `XC924980` has several more clearly separated bouts.
The 5--8 ms peak candidates mostly select local fluctuations inside these
bouts; they are not credible standalone chirp boundaries.  Thus their apparent
duration similarity should not be interpreted as a biological measurement.

The mystery excerpt has a persistent narrow component around 4.64 kHz and a
repeated, but uneven, short-envelope structure.  In this limited material it
is much closer in carrier range to the *Gryllus* and *Acheta* recordings than
to the high-frequency *Roeseliana* recordings.  That is not an identification:
recording conditions, behaviour and the deliberately limited corpus confound
any species conclusion.  Its 42 local candidates include visibly variable
peaks and do not establish one unambiguous chirp unit.

### Methodological consequences

There is no single corpus-wide operational definition of an individual chirp
at this stage.  A promising representation is hierarchical: (1) activity/bout
start and end, (2) short event start/end/peak/duration and gap, and (3), where
resolvable, an internal envelope or pulse/spectral representation.  Each event
should retain its source timestamp, filtering/threshold provenance and a
quality/confidence measure.  Carrier/spectral-band estimates and a
normalised, fixed-context envelope or spectrogram are complementary features;
they should not be collapsed into one scalar feature.

A future production detector will consequently need recording-adaptive noise
and activity estimation, frequency-band selection that can accommodate at
least approximately 4 and 16 kHz material, and separate handling of isolated
events versus sustained bouts.  It should expose potentially nested temporal
units rather than silently choosing one peak spacing.  Its performance must be
validated against manually reviewed intervals across more recordings before
any threshold becomes a default.  These findings do not amend the DTW-on-chirp
envelopes decision, but they do show that the unit supplied to DTW may need to
be selected from an explicitly documented level of this hierarchy.

## 16. Review of temporal hierarchy and spectral-peak interpretation (2026-08-07)

The survey outputs were re-examined to test the proposed
activity/bout -> short-event -> internal-structure hierarchy, and to test what
the largest Welch PSD peak above 2 kHz actually represents.  This is a review
of exploratory outputs, not a new detector or a carrier-frequency estimator.

### Temporal levels actually visible

The activity/bout level is well supported for the two *Roeseliana* recordings.
`XC924980` has visually distinct candidate-bearing regions at approximately
0.54--1.28, 2.71--5.15, 11.00--11.96, and 20.40--22.39 s, separated by
1.4--8.4 s gaps.  `XC924802` has two sustained high-frequency activity
regions separated by the conspicuous quiet interval around 8.18--10.09 s.
In both cases, however, the short candidates are local maxima in sustained,
noisy modulation.  The aligned candidate-envelope plots are either strongly
variable (`XC924980`) or show repeated modulation across the entire 120 ms
context (`XC924802`), rather than isolated, repeatable events.  These files
support a bout representation but do *not* support the candidate width as an
individual-chirp duration.

`XC925129` gives the clearest short-event evidence.  Its peaks at 0.060,
0.145, and 0.230 s form a roughly 85 ms sequence, followed by a 290 ms gap;
a similar sequence occurs at 0.520, 0.605, and 0.690 s.  The overview shows
separated broadband/harmonic events, and the normalised envelopes are broadly
similar.  It has a long active run through approximately 37.81 s, followed by
fragmented activity, so activity and event are distinguishable even though
the boundary of a smaller phrase within the long run remains a modelling
choice.

`XC940663` also has clear short events, often in pairs: 0.254/0.349 s,
0.708/0.808 s, and 1.177/1.272 s.  The within-pair spacing is about 95 ms and
the inter-pair gap about 0.36--0.45 s.  This is good evidence for event plus
event-group/phrase scales, but does not determine whether a biological chirp
is one member of a pair or the pair.  The mystery excerpt has no candidate gap
above 0.5 s; its 42 candidates form one continuous run and have inconsistent
120 ms envelope contexts.  It does not support a bout division or a stable
short-event/chirp definition.  `XC1085943` has possible trains (eight
candidates from 2.624--3.652 s) but weak signal, isolated candidates and wide
gaps, so its hierarchy is also ambiguous.

The available plots do not establish an internal-pulse level for any
recording.  Candidate peaks have a minimum 80 ms separation and are derived
from a 10 ms-smoothed envelope, which cannot resolve fine temporal structure.
Harmonic bands in the *Gryllus* spectrograms show within-event spectral
content, but are not independently validated biological pulses.

### What the selected PSD peak means

For a supplementary consistency check, a 4,096-sample Hann-windowed spectrum
was calculated around each candidate peak and its strongest 2--20 kHz
component recorded.  The 10th/50th/90th percentile frequencies (kHz) were:

| Recording | Welch-selected peak | candidate-centred local maxima, 10/50/90% | interpretation |
| --- | ---: | ---: | --- |
| XC1085943 | 4.354 | 4.215 / 4.328 / 4.482 | weak and ambiguous |
| XC924802 | 16.575 | 15.114 / 16.505 / 16.792 | high-frequency activity band, not a stable narrow peak |
| XC924980 | 16.034 | 14.693 / 15.867 / 18.427 | broad/variable high-frequency activity band, not a stable narrow peak |
| XC925129 | 4.304 | 4.172 / 4.301 / 4.324 | stable event-associated component |
| XC940663 | 4.439 | 4.414 / 4.447 / 4.468 | stable event-associated component |
| creature7s | 4.639 | 4.605 / 4.641 / 4.676 | stable component of the repeated recorded structure |

The `XC925129` and `XC940663` overview spectrograms independently show the
approximately 4.3--4.5 kHz component and harmonics turning on with visible
short events.  The selected peak is therefore strongly associated with those
recorded events.  This supports using it as an exploratory event-associated
spectral feature, but does not prove it is a biological carrier frequency or
that it belongs to the named insect rather than another coincident source.

The *Roeseliana* high-frequency energy also turns off in their quiet intervals,
so it is associated with their recorded activity bouts.  Its broad and
variable local maxima make the single largest whole-recording Welch bin an
unsuitable carrier estimate: it is better described as a convenient centre for
an activity band.  `XC1085943` is the strongest warning case.  Its global PSD
is dominated by low-frequency content near 255 Hz, while the narrow 4.35 kHz
line persists weakly outside the candidate bursts.  The bursts may contain the
insect signal, but the output cannot separate them from a stationary recording
tone or background characteristic.  The selected 4.35 kHz value must remain
unattributed.

The 4.64 kHz mystery-excerpt component is stable and rises with repeated
envelope maxima, but the excerpt contains no comparably quiet interval or
independent source annotation.  It is associated with the repeated recorded
structure, not proven to be the insect's carrier.

Finally, candidate-centred spectra are not independent validation of the
selected band: candidate times were themselves obtained from that band.  The
visual onset/offset evidence in the spectrograms is more informative for
association, and even that cannot establish biological source identity.  A
future experiment should use independently annotated activity intervals,
multi-band time-frequency measurements, and recordings with known quiet
background before any selected spectral peak is called a carrier frequency.
