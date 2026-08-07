# orthoptera

A reproducible research project for investigating the acoustic signals of Orthoptera — crickets, grasshoppers and related insects.

The project began with an unidentified nocturnal insect recording made in Kent, UK. The longer-term aim is to develop tools that can compare Orthoptera recordings using measurable acoustic characteristics, supported by a reproducible reference corpus of recordings.

The emphasis is on **understanding and validating acoustic features before attempting reliable species identification**. This is a research project, not yet a finished classifier.

## Current status

The project has moved beyond the original exploratory scripts into a structured Python package.

At present:

* the repository has a normal `src/`-layout Python package;
* the original exploratory recordings and analysis scripts have been preserved as historical material;
* a cached Xeno-canto client is implemented for searching and downloading reference recordings;
* the beginnings of the signal, analysis and database layers are in place;
* automated tests cover the implemented package functionality;
* the production acoustic-analysis pipeline is **not yet complete**.

The current development priorities are tracked in [`ROADMAP.md`](ROADMAP.md).

In particular, the next stages are to establish the database layer and build tested production components for chirp detection, feature extraction and comparison. The eventual roadmap includes species comparison and a dashboard, but these are future work rather than current capabilities.

## Where the project came from

The original recording was made on 11 July 2026 at 23:08:17 in north-west Kent, on the North Downs.

A 7.40-second repetitive section of the approximately 87.83-second recording was extracted for the initial investigation. The recording is preserved in:

`pre_project_prototypes/creature7s.wav`

Several Python scripts (`analyse1.py` through `analyse5.py`) document the exploratory analysis that preceded the project being formalised.

These scripts are **historical artefacts**. They are useful because they record observations, hypotheses, failed approaches and the reasoning that led to the current design. They are not the production analysis pipeline and their parameters should not be treated as scientifically validated.

The distinction is documented in [`EXPERIMENTS.md`](EXPERIMENTS.md).

## Current scientific approach

The project is deliberately being developed incrementally.

The intended analysis pipeline is broadly:

```text
WAV recording
    ↓
signal filtering
    ↓
envelope / chirp detection
    ↓
per-chirp feature extraction
    ↓
reference database
    ↓
comparison
```

The project is interested in features such as:

* carrier frequency;
* chirp duration;
* inter-chirp interval;
* the relationship between chirp and gap duration;
* variability in these measurements;
* amplitude and envelope shape;
* internal pulse structure;
* slower grouping or phrasing patterns.

These are **candidate features**, not established species discriminators.

A central methodological principle is that measurements from one recording should not automatically be interpreted as characteristics of a species. Multiple recordings and measurements of within-species variability are needed before apparent differences between species can be considered meaningful.

For comparing temporal signal shapes, the project has selected **Dynamic Time Warping (DTW) on chirp envelopes** as the current intended approach. The rationale is that DTW can accommodate modest differences in timing or tempo that would otherwise make direct correlation less useful. This is an architectural/methodological decision recorded in [`DECISIONS.md`](DECISIONS.md).

The detailed scientific history and limitations are in [`EXPERIMENTS.md`](EXPERIMENTS.md), while the intended architecture is described in [`DESIGN.md`](DESIGN.md).

## Xeno-canto reference recordings

The project uses recordings from [Xeno-canto](https://xeno-canto.org/) as reference material.

The repository contains a small number of reference recordings for testing. The Xeno-canto client can search the public API, optionally authenticate with an API key, page through results, cache responses, download recordings and cache downloaded audio.

For initial corpus development, the project has deliberately restricted the search to:

```text
gen:Gryllus q:A id?:no len:"10-90"
```

This provides a manageable initial corpus of approximately 173 recordings rather than attempting to download an entire genus indiscriminately.

The client and its tests are under:

`src/orthoptera/xcapi/`

The cached corpus itself is kept separate from the committed source tree.

## Repository structure

```text
orthoptera/
├── src/
│   └── orthoptera/
│       ├── analysis/       Analysis and comparison
│       ├── database/       Database schema and queries
│       ├── signal/         Signal processing and chirp analysis
│       └── xcapi/          Xeno-canto API integration
│
├── tests/
│   └── data/               Small reference recordings
│
├── pre_project_prototypes/
│   ├── analyse1.py ...     Historical exploratory analyses
│   └── creature7s.wav      Original mystery recording excerpt
│
├── AGENTS.md               Guidance for AI coding agents
├── CONTRIBUTING.md         Development and human/AI collaboration workflow
├── DESIGN.md               Intended architecture and scientific design
├── DECISIONS.md            Significant decisions and their rationale
├── EXPERIMENTS.md          Historical experiments and observations
├── ROADMAP.md              Current and planned work
└── README.md               Human-oriented project overview
```

## Getting started

The project uses a repository-local Python virtual environment.

From the repository root:

```bash
./setup.sh
source .venv/bin/activate
```

Alternatively, development dependencies can be installed with:

```bash
pip install -e ".[dev]"
```

Run the test suite with:

```bash
python -m pytest
```

Development and historical analysis commands should be run using the repository's `.venv`, rather than relying on packages installed into the system Python environment.

## Project documentation

The repository deliberately separates different kinds of knowledge.

* [`DESIGN.md`](DESIGN.md) — the intended architecture and scientific design.
* [`DECISIONS.md`](DECISIONS.md) — significant architectural and methodological decisions and their rationale.
* [`EXPERIMENTS.md`](EXPERIMENTS.md) — exploratory work, measurements, hypotheses, failed approaches and limitations.
* [`ROADMAP.md`](ROADMAP.md) — planned development and outstanding work.
* [`CONTRIBUTING.md`](CONTRIBUTING.md) — development workflow and collaboration practices, including work with AI coding agents.
* [`AGENTS.md`](AGENTS.md) — instructions specifically for AI coding agents working in the repository.

These documents are complementary, but they are not interchangeable.

**This README is an orientation document for humans. It should not be treated as the authoritative source for architecture, decisions, experiments, workflow or project priorities.** Those are defined by the documents above.

## Development philosophy

Orthoptera is intended to become a reproducible research tool rather than a one-off analysis script.

The project therefore prioritises:

* reproducible measurements;
* explicit and configurable analysis parameters;
* preservation of raw recordings;
* separation of feature extraction from classification;
* tests for production analysis components;
* reference data with identifiable provenance;
* caching of external data where practical;
* preservation of useful exploratory work;
* clear separation between measured observations, interpretations and future hypotheses.

Passing tests establishes that implemented software behaves as specified. It does not establish that an acoustic feature is biologically meaningful or that an identification method is reliable.

The scientific conclusions of the project must therefore remain grounded in recordings, measurements and experiments rather than in the fact that software produces plausible results.

## For AI coding agents

If you are an AI coding agent entering this repository, start with [`AGENTS.md`](AGENTS.md).

It identifies the project documents that should be consulted and explains which document is authoritative for which kind of information.

In particular, do not infer the current architecture or development priorities from this README alone. Read the relevant project documents before making changes, and use the repository itself rather than an earlier conversation as the persistent project record.

