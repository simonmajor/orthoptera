# Contributing to Orthoptera

## 1. Purpose

Orthoptera is developed as a research-oriented, reproducible software project. Contributions may be made directly by a human developer or with the assistance of an AI coding agent.

The repository, rather than any individual AI conversation, is the persistent project record.

Contributors should therefore aim to leave the repository in a state from which another developer or AI agent can understand what was done, why it was done, what was observed, what remains uncertain, and how to reproduce or test the relevant work.

The same principle applies to the project's research and toolchain investigations. Useful knowledge should be captured in the repository rather than relying on conversation history, transient agent state or individual memory.

## 2. Before making changes

Read `AGENTS.md` first.

`AGENTS.md` identifies the other project documents that should be consulted according to the significance and nature of the task. In particular:

* `DESIGN.md` describes the intended architecture and scientific approach.
* `ROADMAP.md` describes current and planned work.
* `DECISIONS.md` records important architectural and methodological decisions and their rationale.
* `EXPERIMENTS.md` records exploratory work and empirical observations.
* `CONTRIBUTING.md` describes the development and AI-collaboration workflow.
* The `TOOLCHAIN_*.md` documents record the separate research, findings, decisions and candidate capabilities associated with the AI/development toolchain.

Do not rely on an earlier conversation, coding-agent session, or personal memory when the relevant information can be recorded in the repository.

For substantial work, read the documents relevant to the task rather than assuming that a filename, summary, or previous conversation provides sufficient context.

## 3. Keep changes focused

Prefer small, independently understandable changes.

A change should have a clear purpose and should not include unrelated refactoring merely because the surrounding code could be improved.

Do not introduce speculative architecture in anticipation of requirements that do not yet exist.

When a task can be completed without changing an existing algorithm, prefer not to change the algorithm.

When changing documentation, preserve useful existing knowledge unless deliberately superseding or relocating it. A shorter document is not necessarily a better document if shortening removes provenance, historical context, evidence, rationale or unresolved questions that may be useful later.

## 4. Use the appropriate project record

Different kinds of knowledge belong in different places.

The documents are complementary, not interchangeable. Do not solve a documentation problem by copying the same material into several documents merely to make it easier to find.

### Source code and tests

Use source code for implementation and tests for executable verification of behaviour.

### `DESIGN.md`

Use for the intended architecture, interfaces and scientific design.

### `DECISIONS.md`

Use when a significant architectural, methodological or scientific decision has been made.

Record the alternatives considered and the reason for the decision where useful.

### `EXPERIMENTS.md`

Use for exploratory analysis, measurements, hypotheses, failed approaches and empirical observations.

Distinguish measured results from interpretation. Do not silently turn exploratory observations into production assumptions.

### `ROADMAP.md`

Use for planned work, milestones and outstanding tasks.

### `AGENTS.md`

Use for concise, persistent instructions that an AI coding agent must follow while operating in the repository.

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

## 5. Preserve provenance and context

Durable knowledge should retain enough provenance to allow a later reader to recover where it came from.

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

A later reader should be able to distinguish between:

* a capability that was actually demonstrated;
* a capability described by the tool's documentation;
* a capability inferred from observed behaviour;
* a capability identified elsewhere as potentially useful;
* and a capability that remains unresolved.

When evidence is incomplete, preserve that uncertainty rather than filling the gap with a plausible explanation.

## 6. Preserve historical knowledge

The repository is also a research record.

Later understanding may supersede an earlier interpretation without making the earlier observation or experiment worthless. Historical material should therefore not be removed merely because a later investigation provides a better explanation or conclusion.

When later work changes the interpretation of earlier work, prefer recording the new understanding while retaining enough of the earlier record to understand how the investigation developed.

Do not rewrite history merely to make the current documentation look cleaner.

Where a document has a historical or journal-like role, additions should preserve the chronology and provenance of the underlying record. If material needs to be reorganised into a different kind of document, recover and preserve the information first; structural reorganisation should not be allowed to become accidental information loss.

## 7. Distinguish evidence from inference

Documentation concerning experiments, tools and AI behaviour should distinguish at least the following:

* **Observed** — directly observed during the work.
* **Reported** — explicitly returned or stated by a tool, command or authoritative source.
* **Demonstrated** — reproduced sufficiently to establish the relevant behaviour for the stated purpose.
* **Inferred** — a plausible interpretation that is not independently established.
* **Unknown** — not yet determined.

Do not promote an inference to a fact merely because it provides a convenient explanation.

In particular, observed persistence, state, context, caching, delegation or tool behaviour must not automatically be interpreted as evidence of an undocumented internal mechanism.

Where a conclusion depends on an assumption, make that dependency visible.

## 8. Capture durable knowledge at natural checkpoints

Useful knowledge should be captured while it is fresh rather than relying on the conversation in which it was discovered.

A checkpoint should capture the information that would otherwise be difficult or expensive to reconstruct, including where appropriate:

* observations;
* measurements;
* important negative results;
* limitations;
* changes in interpretation;
* reasons for rejecting an approach;
* relationships between investigated alternatives;
* and references needed to recover the underlying evidence.

The purpose of a checkpoint is not to produce a polished summary at the expense of detail. It is to preserve durable knowledge so that later work can build on it without replaying the entire investigation.

## 9. Working with AI coding agents

AI coding agents are useful for implementation, testing, repository exploration and repetitive engineering work. They should not be treated as the sole authority for architectural or scientific decisions.

A useful workflow is:

1. Establish the intended change with the human/project-level reasoning process.
2. Give the coding agent a bounded implementation task.
3. Tell it which project documents are relevant.
4. Ask it to inspect the existing implementation before changing it.
5. Require tests or other appropriate verification.
6. Review the resulting diff and test results.
7. Record any durable architectural, methodological, experimental or toolchain knowledge in the appropriate project document.
8. Commit one logical change at a time.

The coding agent should be given enough context to make the requested change correctly, but should not be encouraged to invent requirements.

## 10. Architectural versus execution work

For significant changes, separate **deciding what should be done** from **implementing it**.

The architectural/scientific discussion should establish:

* the problem;
* the intended behaviour;
* relevant constraints;
* alternatives and trade-offs;
* any scientific assumptions;
* what must not change.

The coding agent should then implement that decision rather than independently redesigning the project.

For small, well-understood changes this separation need not be formal.

## 11. Prompting coding agents

Prefer prompts that are:

* specific about the desired outcome;
* explicit about important constraints;
* scoped to one logical change;
* clear about which files or subsystems are relevant;
* explicit about what must not be changed;
* explicit about required verification.

For example:

> Implement X.
>
> Read `AGENTS.md` and `DESIGN.md` first.
>
> Keep the existing algorithm unchanged.
>
> Add tests covering Y and Z.
>
> Do not introduce new dependencies.
>
> Run the relevant tests and report the result.

## 12. Review and commit discipline

Before committing a documentation or implementation change:

* inspect the complete diff;
* check that no unrelated material has been changed;
* check that useful existing knowledge has not been silently removed;
* check that references and provenance remain understandable;
* run the appropriate tests or other verification;
* and confirm that the resulting document remains consistent with the repository's documentation hierarchy.

Prefer one logical change per commit.

When a larger documentation recovery or reorganisation is required, separate the work into independently understandable commits so that the evolution of the documentation remains recoverable from git history.

