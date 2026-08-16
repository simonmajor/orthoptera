# Project-Structure Findings Journal

This document is the append-only historical journal of durable findings from the provisional project-structure investigation.

It is a research record, not an architecture specification, decision record, instruction file or mutable plan. A finding belongs here only when the available evidence supports it. Later findings may qualify, supersede or contradict earlier findings through later entries; earlier entries are not rewritten merely to express a cleaner current synthesis.

Each finding should preserve its evidence, epistemic status, scope, limitations, provenance and relationship to later work. A recovery practice that happened to work is not automatically a durable finding.

## Initial extraction from the Orthoptera documentation-recovery case study

**Review date:** 17 August 2026  
**Evidence base:** `project_structure_research/JOURNAL.md`, reviewed against Orthoptera `main` at `f8cd0aaf9450e632cbd23c5f1862b9f560631466`.

### Document role determines whether deletion is knowledge loss

**Finding:** Whether removed text represents knowledge loss depends on the semantic role of the document, not on deletion count alone.

**Evidence:** The Orthoptera audit found materially different outcomes across document roles. `EXPERIMENTS.md` required no recovery; an earlier `DESIGN.md` formulation had been deliberately superseded while its evidence and rationale survived elsewhere; mutable `README.md` and `ROADMAP.md` text did not automatically require in-place preservation; but two actual decisions removed from `DECISIONS.md` had to be restored.

**Scope and limitation:** This finding does not make deletion from mutable documents harmless. It requires review against the document's role, authority, retained evidence and intended transformation.

### Historical epistemic state and mutable current intent are distinct project state

**Finding:** A completed investigation's contemporary epistemic state and the project's current intended sequence are distinct kinds of durable state.

A historical entry may legitimately preserve implications, hypotheses, unresolved questions, speculation and proposed follow-up work produced by completed work. A mutable plan records which work remains currently intended and how it is sequenced. Later planning changes do not retrospectively change the historical entry.

**Evidence:** The recovery exposed repeated ambiguity when experiments, findings, decisions and planned work were treated as interchangeable current-state summaries. Separating completed-work journals from mutable planning resolved that ambiguity without deleting contemporary interpretation.

### Whole-document synthesis is hazardous for evidence-bearing documentation

**Finding:** Whole-document AI redrafting can create a material knowledge-loss hazard when applied to evidence-bearing documentation.

**Evidence:** During an explicit historical recovery, commit `ddd7d7e` combined whole-document replacement, concise synthesis and evolving document roles, producing 446 insertions and 1,195 deletions. This repeated the class of loss that triggered the recovery.

**Epistemic status:** Observed in this case study and supported by the earlier rejected toolchain checkpoint.

**Scope and limitation:** This does not establish that every whole-document AI edit is unsafe. The demonstrated risk is strongest when the source contains historical evidence, provenance, changed interpretations or unresolved questions.

### Instruction-file existence and reliable discovery are separate properties

**Finding:** Creating a scoped instruction file does not establish that relevant agents will reliably discover it.

**Evidence:** The provisional bootstrap created `project_structure_research/AGENTS.md` with reasonable local semantics, but its discovery path remained implicit. A later root instruction was required to make reading it operational for work scoped to the sub-project.

**Limitation:** The explicit root pointer establishes a provisional route for this repository. It does not establish general automatic subordinate-`AGENTS.md` discovery semantics across agents.

### Task-context transfer and workspace transfer are separate

**Finding:** Successful transfer of an architectural task or prompt does not by itself establish transfer of the intended repository workspace, checkout or filesystem state.

**Evidence:** A ChatGPT-to-Codex handoff carried the requested work but opened in a generic project workspace without the Orthoptera checkout. The task had to be relaunched explicitly from the intended repository workspace.

**Scope and limitation:** This is directly observed for the tested handoff path. Behaviour of other products, versions and handoff mechanisms remains to be tested.

### Attachment state and evidence provenance must remain independent

**Finding:** Moving an attachment to a newer revision and identifying the revisions under which historical evidence was produced are separate concerns.

**Rationale:** A host may intentionally advance reusable infrastructure at different rates. If historical experiments identify only the current attachment state, earlier evidence becomes ambiguous as those attachments move.

**Consequence:** Experimental records need exact host, reusable-project, tool, model and environment provenance where relevant, regardless of the selected attachment mechanism or update policy.
