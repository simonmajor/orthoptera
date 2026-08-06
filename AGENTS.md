# AGENTS.md

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

New feature extraction code should include tests.

Existing behaviour should not regress.

## Commit style

One logical change per commit.
