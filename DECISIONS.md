## 2026-08-06

Decision:

Use DTW on chirp envelopes.

Reason:

More robust to tempo variation than correlation.

Alternatives considered:

Cross-correlation.

## 2026-08-07 — Xeno-canto corpus restriction

For initial development we will use recordings satisfying:

    gen:Gryllus q:A id?:no len:"10-90"

rather than downloading the entire genus.

Rationale:
- manageable corpus (~173 recordings)
- avoids overwhelming early testing
- recordings are long enough for multiple independent chirp samples
- excludes recordings with uncertain identification
- quality A gives a relatively homogeneous starting point
