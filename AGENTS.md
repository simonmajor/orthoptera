# AGENTS.md

## Project context

Orthoptera is a research-oriented acoustic analysis project. The repository
is the authoritative persistent project state. Do not assume that context from
a previous AI session remains available.

Before significant changes:
1. Read AGENTS.md.
2. Read DESIGN.md.
3. Read ROADMAP.md.
4. Read DECISIONS.md.

When a significant architectural or methodological decision is made, record
it in DECISIONS.md rather than relying on conversation history.

When a feature is completed, update ROADMAP.md and record important experimental
or methodological results in the appropriate documentation.

Prefer small, independently testable changes and avoid speculative
architecture.

## Purpose

This repository develops a reproducible toolkit for analysing Orthoptera
acoustic recordings.

The emphasis is on scientific correctness and reproducibility rather than
producing a classifier quickly.

## Coding principles

- Keep functions small.
- Prefer pure functions.
- Avoid hidden state.
- Every analysis should be reproducible.
- Preserve raw recordings.
- Never hard-code paths.

## Scientific principles

- Feature extraction and classification are separate.
- All parameters should be configurable.
- Random sampling must accept a seed.
- All outputs should include analysis version.

## Scientific philosophy

- Do not optimise for classification accuracy.
- Optimise for reproducible feature extraction.
- Classifier development comes later.

## Preferred libraries

numpy
scipy
matplotlib
sqlite3
pandas

Avoid introducing large dependencies without discussion.

## Testing

Run all Python commands in the repository's `.venv`, initialised by
`setup.sh`, including when inspecting or running historical prototypes. Do not
rely on packages available to the system Python.

New feature extraction code should include tests.

Existing behaviour should not regress.

## Commit style

One logical change per commit.
