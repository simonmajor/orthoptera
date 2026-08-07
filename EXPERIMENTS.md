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
