# Contributing to Orthoptera

## 1. Purpose

Orthoptera is developed as a research-oriented, reproducible software project. Contributions may be made directly by a human developer or with the assistance of an AI coding agent.

The repository, rather than any individual AI conversation, is the persistent project record.

Contributors should therefore aim to leave the repository in a state from which another developer or AI agent can understand what was done, why it was done, and how to reproduce or test it.

## 2. Before making changes

Read `AGENTS.md` first.

`AGENTS.md` identifies the other project documents that should be consulted according to the significance of the change. In particular:

* `DESIGN.md` describes the intended architecture and scientific approach.
* `ROADMAP.md` describes current and planned work.
* `DECISIONS.md` records important architectural and methodological decisions.
* `EXPERIMENTS.md` records exploratory work and empirical observations.
* `CONTRIBUTING.md` describes the development and AI-collaboration workflow.

Do not rely on an earlier conversation, coding-agent session, or personal memory when the relevant information can be recorded in the repository.

## 3. Keep changes focused

Prefer small, independently understandable changes.

A change should have a clear purpose and should not include unrelated refactoring merely because the surrounding code could be improved.

Do not introduce speculative architecture in anticipation of requirements that do not yet exist.

When a task can be completed without changing an existing algorithm, prefer not to change the algorithm.

## 4. Use the appropriate project record

Different kinds of knowledge belong in different places.

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

## 5. Working with AI coding agents

AI coding agents are useful for implementation, testing, repository exploration and repetitive engineering work. They should not be treated as the sole authority for architectural or scientific decisions.

A useful workflow is:

1. Establish the intended change with the human/project-level reasoning process.
2. Give the coding agent a bounded implementation task.
3. Tell it which project documents are relevant.
4. Ask it to inspect the existing implementation before changing it.
5. Require tests or other appropriate verification.
6. Review the resulting diff and test results.
7. Record any durable architectural, methodological or experimental knowledge in the appropriate project document.
8. Commit one logical change at a time.

The coding agent should be given enough context to make the requested change correctly, but should not be encouraged to invent requirements.

### Architectural versus execution work

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

## 6. Prompting coding agents

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

This is generally preferable to asking an agent to "improve" a subsystem without defining the intended behaviour.

For a historical or archaeological task, tell the agent explicitly whether the material is evidence to document rather than code to modernise.

## 7. Ask agents to inspect before editing

For non-trivial changes, the agent should first inspect:

* relevant project documentation;
* the existing implementation;
* existing tests;
* related interfaces;
* recent Git history when historical context matters.

When the task involves an experimental or historical artefact, distinguish carefully between:

* what the files demonstrate;
* what recorded results demonstrate;
* what is inferred;
* what remains uncertain.

Do not manufacture historical continuity from filenames or imported snapshots.

## 8. Verification

A change is not complete merely because the code has been written.

Run the relevant tests and checks using the repository's `.venv`.

For changes affecting existing behaviour, verify that existing tests still pass.

For new functionality, add appropriate tests unless there is a documented reason not to.

When external services are involved, unit tests should normally avoid requiring network access. Use injected or mocked interfaces where appropriate.

## 9. Git discipline

Keep commits logically focused.

Prefer one logical change per commit.

Commit messages should describe the change clearly. Where an architectural decision is significant, the commit body may explain the rationale, but the durable decision should also be recorded in `DECISIONS.md` where appropriate.

Do not commit:

* `.venv`;
* generated caches;
* temporary analysis output;
* credentials or API keys;
* large derived datasets unless explicitly intended.

Historical artefacts may be committed when their preservation is intentional and documented.

## 10. Experimental and scientific work

Exploratory analysis is expected to precede some production algorithms.

Do not treat an exploratory parameter as scientifically validated merely because it produced plausible output.

When developing an analysis method:

* preserve raw recordings;
* record relevant parameters;
* distinguish observations from interpretations;
* test against more than one recording where appropriate;
* measure within-class/species variability before interpreting between-class differences;
* preserve useful failed approaches when they explain an important design decision.

Production analysis should be rebuilt as reproducible, tested components rather than copied mechanically from exploratory scripts.

## 11. Suggestions for effective AI-assisted development

The following are practical suggestions rather than additional architectural rules.

### Give the agent a bounded job

A good coding-agent task often has the form:

> Implement this one component, add tests, verify it, and leave unrelated code alone.

This reduces accidental scope expansion.

### Let the repository carry context

If a piece of information will matter again, record it in the repository rather than relying on a chat transcript.

A future agent can read a concise project document much more reliably than reconstructing a long conversation.

### Use fresh sessions deliberately

A fresh coding-agent session can be preferable when starting an independent task, particularly when an earlier session contains a large amount of unrelated implementation history.

A resumed session is useful when the agent is genuinely continuing the same task and its accumulated context is valuable.

The repository should make either choice safe.

### Treat agent output as a proposal

Review:

* the diff;
* tests;
* changes to dependencies;
* changes to public interfaces;
* changes to documented assumptions.

Do not accept a plausible explanation as evidence that the implementation is correct.

### Record lessons from agent work

If an agent discovers something that will materially help future work, capture it in the appropriate project document.

Do not turn every conversation detail into documentation. Record durable knowledge, not conversational noise.

