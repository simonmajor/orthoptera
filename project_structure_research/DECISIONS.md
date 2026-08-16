# Project-Structure Decisions Journal

This document is the append-only historical journal of actual decisions made by the provisional project-structure investigation.

It is not a findings record, experiment record or mutable plan. Only choices or requirements that have actually been adopted belong here. Candidate mechanisms, hypotheses, practices and unanswered research questions remain outside this journal until an explicit decision is made.

Each entry should preserve the decision, scope, context, rationale, constraints and relevant evidence. Later decisions may qualify, supersede or reverse earlier decisions through later entries; earlier decisions are not retrospectively rewritten.

## Initial extraction from the Orthoptera documentation-recovery case study

**Review date:** 17 August 2026  
**Evidence base:** `project_structure_research/JOURNAL.md`, reviewed against Orthoptera `main` at `f8cd0aaf9450e632cbd23c5f1862b9f560631466`.

### Recover before broad structural reorganisation

**Decision:** Historical recovery and verification precede broad documentation reorganisation, naming, moves and repository extraction.

**Rationale:** Structural churn can obscure provenance and make accidental information loss harder to detect. Targeted correctness fixes remain permissible when current guidance is actively misleading.

### Separate historical journals from mutable planning

**Decision:** Journals preserve completed work in its contemporary epistemic state; mutable planning documents record current intent and sequencing.

Historical entries may retain implications, hypotheses, unresolved questions, speculation and possible follow-up work understood at the time. Later planning changes do not rewrite those entries.

### Maintain a minimal provisional research boundary

**Decision:** Begin the project-structure investigation with a minimal embedded boundary consisting of `AGENTS.md`, `README.md`, `JOURNAL.md`, `PLAN.md`, and—once justified by extraction—dedicated findings and decisions journals.

No bootstrap, audit, migration or upgrade implementation and no final attachment mechanism, metadata syntax, repository name or final topology is selected by this decision.

### Treat new-host and existing-host adoption as first-class paths

**Decision:** Reusable project-structure infrastructure must support both:

* initialising and scaffolding a new host; and
* inspecting, preserving and explicitly adapting an existing host with accumulated source, documentation, history, knowledge and external relationships.

The existing-host path must not be reduced to applying a generic new-project template.

### Host projects own instantiated documentation

**Decision:** Documentation or configuration instantiated from reusable templates becomes host-owned project state.

Reusable-infrastructure updates must not silently overwrite accumulated host knowledge. Future upgrades or migrations must produce explicit, reviewable transformations.

### Keep reusable projects as conceptual peers

**Decision:** The project-structure and AI-toolchain projects are conceptual peers. Either may logically use the other, but reciprocal logical use must not be represented as recursive physical containment.

Their current embedding in Orthoptera is provisional emulation and does not select nested repositories as the final architecture.

### Keep attachment properties distinct

**Decision:** Treat attachment identity, physical mechanism, update policy and evidence provenance as separate properties.

No physical mechanism or update policy is selected by this decision. Historical evidence must retain exact provenance even when a host advances an attachment.

### Provide an explicit provisional instruction-discovery path

**Decision:** Root `AGENTS.md` explicitly directs work scoped to `project_structure_research/` to read its subordinate `AGENTS.md`.

**Scope:** This makes the current provisional boundary operational. It is not a general decision about automatic subordinate-instruction discovery, inheritance or conflict resolution.
