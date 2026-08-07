# orthoptera

Tools for investigating and analysing the acoustic recordings of Orthoptera
(crickets, grasshoppers and related insects).

This is a personal research project arising from the investigation of an
unidentified nocturnal insect recording made in Kent, UK. The eventual aim is
to combine reproducible signal analysis with a reference corpus of recordings,
including material obtained from Xeno-canto, to help identify and compare
Orthoptera calls.

The project is deliberately being developed incrementally. The current code
base is infrastructure rather than a finished identification system.

## Current status

The repository currently contains:

- a Python package under `src/orthoptera/`;
- signal-processing, analysis, database and Xeno-canto API components;
- a cached client for searching and downloading Xeno-canto recordings;
- unit tests using `pytest`;
- a small set of reference recordings under `tests/data/`;
- historical prototype analysis scripts and their source recording under
  `pre_project_prototypes/`.

The Xeno-canto client currently supports:

- searching the public Xeno-canto recordings API;
- optional API-key authentication;
- paging through search results;
- caching search responses;
- downloading recordings;
- caching downloaded audio;
- avoiding accidental replacement of existing recordings.

Feature extraction and automated species identification are **not yet
implemented**.

## Getting started

The project uses a local Python virtual environment.

From the repository root:

```sh
./setup.sh
source .venv/bin/activate
```

The development dependencies can also be installed directly with:

pip install -e ".[dev]"

Run the test suite with:

python -m pytest

The repository is structured as a normal src-layout Python package, so code
should be imported through the orthoptera namespace rather than by relying on
repository-root module paths.

## Repository layout

orthoptera/
├── src/
│   └── orthoptera/
│       ├── analysis/       Analysis and comparison
│       ├── database/       Database schema and queries
│       ├── signal/         Signal-processing components
│       └── xcapi/          Xeno-canto API integration
│
├── tests/
│   ├── data/               Small local/reference recordings
│   └── ...                 Automated tests
│
├── pre_project_prototypes/
│   ├── analyse1.py
│   ├── analyse2.py
│   ├── analyse3.py
│   ├── analyse4.py
│   ├── analyse5.py
│   └── creature7s.wav
│
├── AGENTS.md               Guidance for coding agents
├── CONTRIBUTING.md         Development and vibe-coding workflow
├── DESIGN.md               Current architecture and design
├── DECISIONS.md            Architectural and project decisions
├── EXPERIMENTS.md          Historical experiments and observations
├── ROADMAP.md              Planned development
└── README.md               This document
The recordings

The original mystery recording is a short extract from a longer field
recording made in north-west Kent. It is retained in the repository as
pre_project_prototypes/creature7s.wav because it is the principal specimen
that motivated the project.

The prototype analysis scripts (analyse1.py through analyse5.py) record
the early exploratory work performed before the repository existed. They are
historical artefacts rather than part of the current package and should not be
treated as the project's production analysis pipeline.

A small number of Xeno-canto recordings are also retained under
tests/data/ as local reference material. Larger datasets should not normally
be committed to the repository.

## Xeno-canto

The project uses recordings from Xeno-canto as a
reference corpus.

The current client is intentionally small. For example, a search can be
expressed using Xeno-canto's query syntax, such as:

gen:Gryllus q:A id?:no len:"10-90"

This provides a useful way of constructing controlled reference sets rather
than downloading an entire genus or family indiscriminately.

Downloaded recordings and API responses are cached locally so that subsequent
analysis does not repeatedly depend on the remote service. Cache and dataset
management are intentionally kept separate from the committed source tree.

Consult src/orthoptera/xcapi/ and its tests for the current API interface.

## Development philosophy

The project is being developed as a reproducible research tool rather than as
a one-off script.

In particular:

exploratory work should be preserved when it provides useful scientific
context;
algorithms should be developed incrementally and tested against known
recordings;
reference data should be identifiable and reproducible;
external API activity should be cached where practical;
architectural changes should be documented rather than inferred from
implementation history;
automated coding agents should make small, reviewable changes;
experimental results should not silently become production assumptions.

The project deliberately separates what the system is intended to become
from what has actually been demonstrated. The latter is especially
important for acoustic identification, where apparently useful measurements
can turn out to be artefacts of a particular recording or analysis method.

## Project documentation

The other Markdown files provide the detailed project context:

AGENTS.md — instructions and constraints for coding agents. Start here
when working on the codebase with an AI coding agent.
CONTRIBUTING.md — practical development and vibe-coding workflow,
including guidance for humans collaborating with coding agents.
DESIGN.md — the current architectural design.
DECISIONS.md — significant decisions and their rationale.
EXPERIMENTS.md — historical experiments, observations and results.
ROADMAP.md — intended future development.

These documents are complementary rather than interchangeable. In particular,
the README is intended to explain the project to a human encountering it for
the first time; it is not intended to duplicate the detailed instructions
given to coding agents.

## Status and expectations

This project is exploratory. Passing tests demonstrate that the implemented
software behaves as specified; they do not establish that a particular signal
feature is biologically meaningful or that an identification method is
reliable.

Scientific conclusions should therefore be supported by the recordings,
measurements and experiments that produced them, rather than by the existence
of code which happens to produce a plausible result.

## Licence

See LICENSE.

