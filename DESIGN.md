Project goals

The project aims to identify Orthoptera species from sound recordings.

Current pipeline

WAV
↓
Band-pass
↓
Envelope
↓
Chirp detection
↓
Feature extraction
↓
SQLite
↓
Comparison

Design principles

• Reproducible
• Modular
• Feature extraction separated from classification
• Raw recordings immutable
