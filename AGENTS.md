# AGENTS.md

## Project context

Orthoptera is a research-oriented acoustic analysis project. The repository is the authoritative persistent project state. Do not assume that context from a previous AI session remains available.

### Required project guidance

Read this file first.

Before making significant changes, read the project documents relevant to the task:

1. `DESIGN.md` — intended architecture and scientific design.
2. `ROADMAP.md` — current priorities and planned work.
3. `DECISIONS.md` — architectural and methodological decisions and their rationale.
4. `EXPERIMENTS.md` — exploratory work, measurements, hypotheses and known limitations.
5. `CONTRIBUTING.md` — development workflow and human/AI collaboration guidance.

For a substantial task, read all five rather than relying on filenames or conversation context.

If the task is historical, experimental or methodological, `EXPERIMENTS.md` is especially important.

If the task concerns an existing architectural choice, `DECISIONS.md` is authoritative.

If the task concerns intended future work, consult `ROADMAP.md`.

If development workflow or AI-agent behaviour is relevant, consult `CONTRIBUTING.md`.

Do not duplicate detailed project knowledge from these documents into this file merely to make it easier to find. This file should provide the steering needed to discover the appropriate source.

### Persistent knowledge

When new durable knowledge is created:

* record architectural or methodological decisions in `DECISIONS.md`;
* record experimental observations and methodological lessons in `EXPERIMENTS.md`;
* update `ROADMAP.md` when planned work changes;
* update `DESIGN.md` when the intended architecture changes;
* update `CONTRIBUTING.md` when development or collaboration practice changes.

Do not rely on chat history as the sole record of a decision.

## Purpose

This repository develops a reproducible toolkit for analysing Orthoptera acoustic recordings.

The emphasis is on scientific correctness and reproducibility rather than producing a classifier quickly.

## Coding principles

* Keep functions small.
* Prefer pure functions.
* Avoid hidden state.
* Every analysis should be reproducible.
* Preserve raw recordings.
* Never hard-code paths.

## Scientific principles

* Feature extraction and classification are separate.
* All parameters should be configurable.
* Random sampling must accept a seed.
* All outputs should include analysis version.

## Scientific philosophy

* Do not optimise for classification accuracy.
* Optimise for reproducible feature extraction.
* Classifier development comes later.

## Preferred libraries

* numpy
* scipy
* matplotlib
* sqlite3
* pandas

Avoid introducing large dependencies without discussion.

## Testing

Run all Python commands in the repository's `.venv`, initialised by `setup.sh`, including when inspecting or running historical prototypes. Do not rely on packages available to the system Python.

New feature extraction code should include tests.

Existing behaviour should not regress.

## Commit style

One logical change per commit.

