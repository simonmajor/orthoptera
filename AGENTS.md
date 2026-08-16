# Orthoptera AI Agent Instructions

This document contains the persistent instructions that AI coding agents must follow when operating in the Orthoptera repository.

The repository is the persistent project record. Do not rely on an earlier conversation, another agent's transient state, or personal memory when the relevant information can be recorded or recovered from the repository.

---

## 1. Before making changes

Read this document first.

Then identify and read the other project documents relevant to the task.

At minimum:

* `DESIGN.md` for intended architecture, interfaces and scientific design;
* `ROADMAP.md` for current development priorities and planned work;
* `DECISIONS.md` for significant architectural, methodological and scientific decisions;
* `EXPERIMENTS.md` for exploratory work, measurements and unresolved empirical questions;
* `CONTRIBUTING.md` for development and AI-collaboration workflow;
* the relevant `TOOLCHAIN_*.md` documents when the task concerns the AI/development toolchain.

For substantial work, read the relevant documents rather than assuming that a filename, previous conversation, summary, or remembered context is sufficient.

Do not infer current architecture or priorities from `README.md` alone. It is an orientation document for humans, not the authoritative source for architecture, decisions, experiments, workflow or priorities.

For work scoped to the provisional `project_structure_research/` sub-project, read `project_structure_research/AGENTS.md` before making changes there. This is an explicit discovery path for that provisional boundary, not a general decision about subordinate-instruction layout or automatic discovery.

---

## 2. Use the appropriate project record

Different kinds of knowledge belong in different places. These documents are complementary, not interchangeable.

### `DESIGN.md`

Use for intended architecture, interfaces and scientific design.

### `DECISIONS.md`

Use for significant architectural, methodological or scientific decisions.

Where useful, record the alternatives considered and the rationale for the decision.

### `EXPERIMENTS.md`

Use for exploratory analysis, measurements, hypotheses, failed approaches and empirical observations.

Distinguish measured results from interpretation. Do not silently turn exploratory observations into production assumptions.

### `ROADMAP.md`

Use for planned work, milestones and outstanding tasks.

### `CONTRIBUTING.md`

Use for development workflow and collaboration practices, particularly practices that help humans and AI coding agents work effectively together.

### `TOOLCHAIN_*.md`

Use for research into the AI and development toolchain.

Toolchain documentation should preserve enough information for another investigator to understand:

* what was investigated;
* why it was investigated;
* what evidence was obtained;
* what was directly observed or otherwise established;
* what was inferred from that evidence;
* what remains unknown;
* and how the result relates to other investigated tools or capabilities.

Toolchain research should remain separate from Orthoptera's software architecture unless a deliberate decision promotes a result into the appropriate project documentation.

---

## 3. Preserve knowledge and provenance

When changing documentation, preserve useful existing knowledge unless deliberately superseding or relocating it.

A shorter document is not necessarily a better document if shortening removes:

* provenance;
* historical context;
* evidence;
* rationale;
* unresolved questions;
* references to investigated tools;
* or information needed to reproduce or understand earlier work.

Do not rewrite historical records merely to make them shorter or cleaner.

Where later work changes the interpretation of earlier work, preserve enough of the earlier record to understand how the investigation developed.

Where relevant, record concrete references such as:

* repository paths;
* filenames;
* symbols or other source locations;
* commits or revisions;
* external repositories or projects;
* tool names and versions;
* MCP servers or other relevant components;
* experiment identifiers;
* commands or prompts;
* measurements;
* and links or other pointers to the investigated capability.

Avoid reducing a researched tool or capability to an unexplained shorthand name when the identity or provenance of the thing being discussed would otherwise be lost.

When evidence is incomplete, preserve that uncertainty rather than filling the gap with a plausible explanation.

---

## 4. Distinguish evidence from inference

When describing behaviour or capabilities, distinguish between:

* **observed** — directly established from the repository, tool output, execution or other evidence;
* **documented** — explicitly stated by the relevant documentation or source;
* **inferred** — a plausible interpretation of available evidence that has not itself been established;
* **unknown** — not currently established.

Do not present an inference as an observation.

In particular, the existence of:

* session state;
* agent state;
* MCP connections;
* command history;
* generated files;
* persistent databases;
* or context outside the visible prompt

does not by itself establish that an AI model has memory of their contents.

---

## 5. Keep changes focused

Prefer small, independently understandable changes.

A change should have a clear purpose and should not include unrelated refactoring merely because the surrounding code could be improved.

Do not introduce speculative architecture in anticipation of requirements that do not yet exist.

When a task can be completed without changing an existing algorithm, prefer not to change the algorithm.

For documentation recovery or improvement, separate recovery, structural reorganisation, and substantive new policy where practical so that each change remains independently understandable.

---

## 6. Minimise unnecessary context

AI agents should receive the minimum context necessary to perform their task correctly.

Do not load large amounts of project history merely because it exists.

At the same time, do not omit authoritative or task-relevant information merely to save context.

The objective is **sufficient, relevant context**, not minimum context at any cost.

Repository documentation should therefore make it possible to distinguish:

* project-wide invariants that an agent should normally know;
* task-specific documentation that should be consulted when relevant;
* role-specific instructions that may only apply to particular agents or tasks;
* historical records that are useful when investigating history but should not normally be loaded for unrelated implementation work.

Experimental history should not become mandatory background context for ordinary implementation tasks merely because it is recorded in the repository.

---

## 7. Agent instruction hierarchy and subordinate documents

`AGENTS.md` is the repository-wide baseline for AI coding agents.

It should remain concise enough that an agent entering the repository can read it before deciding what additional context is required.

Subordinate agent-instruction documents may be introduced where there is a demonstrated need to scope instructions to:

* a particular role;
* a particular area of the repository;
* a particular workflow;
* or another clearly bounded context.

The existence of a possible subordinate document is not by itself a reason to create one.

Before introducing subordinate instruction documents, establish:

1. what information genuinely needs narrower scope;
2. why keeping it in `AGENTS.md` would impose unnecessary context or ambiguity;
3. what files or tasks the subordinate instructions govern;
4. how an agent is expected to discover the subordinate instructions;
5. how conflicts between instructions are resolved;
6. and whether the resulting hierarchy is easier to understand than the existing arrangement.

Do not create subordinate documents merely to divide a long document into smaller files.

Do not use subordinate documents to hide project-wide invariants that every coding agent needs.

Do not duplicate instructions across levels unless the duplication is deliberate and necessary to make the hierarchy operationally reliable.

The exact subordinate-document structure is therefore a workflow/design question, not an implicit repository convention. No particular directory layout or naming scheme is mandated by this document.

---

## 8. Instructions versus knowledge

Agent instructions and project knowledge serve different purposes.

Use instructions to tell an agent what it **must do or must not do**.

Use project documentation to record what the project **is, has decided, has observed, or has learned**.

Do not turn every useful fact into an agent instruction.

Likewise, do not weaken a mandatory instruction by moving it into a document that an agent is only expected to consult conditionally.

In particular:

* `AGENTS.md` should not become a general-purpose project history;
* experiment journals should not become instruction manuals;
* findings should not silently become mandatory policy;
* wishlist items should not be treated as current requirements;
* decisions should not be inferred merely from experiments.

---

## 9. Toolchain documentation boundaries

When working on the AI/development toolchain, use the appropriate toolchain record.

The toolchain documentation distinguishes between:

* experimental history;
* established findings;
* decisions;
* and candidate capabilities.

A toolchain experiment may reveal a useful capability without implying that Orthoptera should depend on it.

Conversely, an experiment may reveal a limitation without requiring an immediate change to the project architecture.

Project requirements belong in the project documentation; toolchain observations belong in the toolchain documentation until a deliberate decision promotes a result into the appropriate project record.

Prefer the cheapest adequate capability consistent with the project's established zero-cost preference and existing account tiers.

This does not mean avoiding experiments with more capable or paid tooling. It means distinguishing:

* what is useful to know;
* what is useful to have;
* and what the project is actually prepared to adopt.

---

## 10. Freshness and uncertainty

Do not assume that persistent state is current merely because it exists.

When a task depends on potentially changing information, prefer current repository state and current authoritative documentation over remembered or historical information.

When persistent knowledge, generated material, cached state or tool-provided context may be stale, treat that possibility explicitly.

When the repository does not establish an answer, say that it is unresolved rather than manufacturing certainty.

---

## 11. Working with other AI agents

Different AI systems or roles may be used for different tasks.

Do not assume that another agent:

* has seen the current conversation;
* has the same tool access;
* has the same repository context;
* has the same persistent state;
* has the same model;
* or has independently reached the same conclusions.

When handing work between agents, leave sufficient durable information in the repository or task handoff for the receiving agent to understand the relevant state.

Do not rely on conversational continuity between separate agents as the project's knowledge-transfer mechanism.

---

## 12. Verification before completion

Before declaring a task complete:

* inspect the resulting changes;
* check that only intended files changed;
* run relevant tests or verification where appropriate;
* distinguish successful execution from scientific or architectural validation;
* and leave the repository in a state that another developer or AI agent can understand.

For documentation changes, preserve the distinction between historical evidence, current understanding, unresolved questions and future work.

A documentation edit is not successful merely because the resulting text is shorter, cleaner or more internally consistent.

---

## 13. Authority

This document defines mandatory instructions for AI coding agents operating in the repository.

Other project documents provide the information needed to apply those instructions.

Where project documentation conflicts, do not silently choose whichever document is most convenient. Identify the conflict and resolve it through the appropriate project decision/documentation process.

Toolchain documentation does not silently override repository instructions or project architecture.

The repository, rather than any individual AI conversation, remains the persistent project record.

