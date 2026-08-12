# AI Toolchain Experiments Journal

This document is the historical journal of experiments and observations concerning the AI and development toolchain used alongside Orthoptera.

It is a **journal, not a plan**.

Entries record work that has actually been undertaken, together with observations, results, interpretations, limitations and conclusions that arose during that work. They are retained as part of the project's research history.

Do not add future experiment plans, proposed experiment sequences, intended follow-up work, or other planning statements to this document. A comment that an observed result *could warrant further investigation* is acceptable when it is part of the historical record; a proposed experiment belongs in `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md`.

The chronological record is append-only in substance. Later understanding may qualify or reinterpret an earlier observation, but earlier experimental history should not be removed merely because a later experiment provides a better explanation.

This document is deliberately separate from Orthoptera's software architecture. Toolchain observations do not become project requirements or architectural decisions merely because they appear here.

The distinction between **observation** and **interpretation** is important. We should not turn plausible explanations of tool behaviour into established facts without evidence.

Where practical, experimental entries should preserve:

* what was investigated;
* why it was investigated;
* the tool, model, repository, server or other component involved;
* the relevant version or configuration;
* the prompt, command or procedure used;
* what was directly observed;
* what was reported by the tool;
* what was inferred from the evidence;
* what remains unknown;
* relevant measurements;
* and concrete pointers to the thing being investigated.

A capability described by documentation is not equivalent to a capability demonstrated experimentally. An inference is not equivalent to an observation. An unresolved possibility should remain unresolved.

---

# Experiment A — Initial AI workflow

## A.1 Starting arrangement

The initial working arrangement was a two-tier approach:

1. **ChatGPT** as the architectural/reasoning AI.
2. **Codex** as the implementation AI working against the local repository.

This division reflected the desire to keep architectural decisions separate from implementation and to have the implementation agent work directly with the repository.

The arrangement predates the more recent investigation of GitHub Copilot CLI.

## A.2 Acoustic survey

The local acoustic survey was carried out using Codex.

In retrospect, this was consistent with the established two-tier division: it was an implementation/exploration task involving the local corpus and repository tooling rather than an architectural decision.

However, it also exposed a significant cost issue. The acoustic investigation involved substantial local analysis and a large AI context, making it relatively expensive in token terms.

This prompted the subsequent investigation into alternative AI workflows and into how context, delegation and model selection affect cost.

---

# Experiment B — GitHub Copilot CLI reconnaissance

The next experiment investigated GitHub Copilot CLI as a possible additional AI tier.

The purpose was initially to understand the behaviour and capabilities of the toolchain itself rather than to solve an Orthoptera problem.

The investigation examined repository interaction, context handling, model selection, delegation and related capabilities.

The investigation also exposed an important distinction between capabilities that were theoretically available through the toolchain and capabilities that were actually available under the project's current account, cost and configuration constraints.

---

# Experiment C — Context and session behaviour

The investigation examined how AI-tool context is acquired and retained.

The important distinction was between:

* conversation context;
* repository or persistent memory;
* tool/session state;
* generated files;
* command history;
* MCP connections;
* and information explicitly present in repository documentation.

The existence of one form of persistence should not automatically be interpreted as model memory in another sense.

A fresh AI session does not necessarily imply that every other form of state has been discarded.

Similarly, an agent being able to recover information from the repository is not evidence that the information was retained in its model context from an earlier session.

These distinctions became important to later experiments concerning reproducibility and context boundaries.

---

# Experiment D — Model and context investigation

The investigation considered the relationship between model selection, context size and effective working context.

Different models may expose different context capacities and different resource/cost characteristics.

An experiment involving AI context should therefore record the model used and, where available, the relevant context configuration rather than treating "the AI" as a single interchangeable component.

The investigation also examined context compaction and the possibility that a long-running session may continue after earlier conversation material has been summarised.

This means that a session which appears continuous to a human may not necessarily retain the original representation of all earlier material.

---

# Experiment E — Delegation and specialist roles

The investigation examined delegated or specialist AI roles as an alternative to requiring one agent to acquire all background context.

The motivation was partly cost and partly context control.

A specialist agent can potentially be given a narrower task and therefore a narrower context requirement. This is attractive where a task can be expressed through a well-defined interface or bounded evidence set.

The investigation did not establish that delegation is universally beneficial.

Delegation introduces its own costs, including the cost of communicating the task and evidence, coordinating results, and ensuring that the specialist has sufficient context to avoid making unsupported assumptions.

The useful observation is therefore that **task decomposition and context decomposition are related but distinct design problems**.

---

# Experiment F — Repository navigation and context acquisition

The toolchain investigation examined tools intended to improve navigation of an unfamiliar or large repository and to provide AI agents with more structured context.

The investigation covered several approaches and tools, including repository graph/navigation tooling and AI-assisted code exploration.

The important distinction is between:

* locating relevant material;
* understanding relationships between repository elements;
* supplying that material to a model;
* and retaining knowledge for later use.

A repository-navigation capability is not automatically a persistent-memory capability.

Likewise, a graph representation is not automatically a substitute for the source material from which the graph was derived.

Concrete tool identities, repositories and other pointers should remain part of the historical record when they are relevant to understanding an experiment.

---

# Experiment G — Persistent knowledge and repository memory

The investigation considered several mechanisms by which knowledge might survive beyond a single AI interaction.

These included explicit repository documentation, AI-tool persistent memory, session state and other tool-specific mechanisms.

The investigation reinforced the practical value of treating the repository as the durable project record.

Useful knowledge discovered through experimentation should therefore be captured in the repository rather than relying on conversation history, transient agent state or individual memory.

This does not establish that repository documentation is the only possible persistence mechanism. It establishes that it is the mechanism under project control.

---

# Experiment H — AI context minimisation

The investigation examined the principle that an AI agent should receive enough context to perform its task correctly without automatically receiving the entire historical context of the project.

The existence of substantial historical material does not mean that every task requires all of it.

This is particularly relevant as the workflow develops multiple AI tiers and potentially specialised roles.

The experiment established the usefulness of distinguishing:

* project-wide invariants;
* task-specific context;
* historical experimental material;
* and toolchain-specific knowledge.

The precise structure of subordinate agent instructions remained unresolved.

---

# Experiment I — Toolchain capability reconnaissance

The investigation expanded beyond GitHub Copilot CLI to other tools relevant to repository navigation, context acquisition, code understanding and AI-assisted development.

The purpose of these investigations was to determine what capabilities existed, what could actually be demonstrated, and what limitations applied.

The individual investigations are part of the historical record even where a tool was not adopted.

A capability that was not adopted can still be useful knowledge because it establishes either:

* what is technically possible;
* what was tested and found unsuitable;
* what was unavailable under current constraints;
* or what remains interesting for future investigation.

Tool names should therefore remain accompanied by sufficient identity and provenance to recover the actual tool being discussed.

---

# Experiment J — GitNexus investigation

GitNexus was investigated specifically in relation to Orthoptera's repository-navigation and context-efficiency requirements.

The investigation considered the capabilities of the `GitNexus` project and its suitability as an AI/toolchain component.

The investigation is retained here as evidence of what was examined rather than as an adoption statement.

[Historical detailed material retained from the investigation.]

---

# Experiment K — Code Pathfinder investigation

Code Pathfinder (`shivasurya/code-pathfinder`) was investigated specifically in relation to Orthoptera's repository-navigation and context-efficiency requirements.

The investigation considered its repository-understanding and navigation capabilities and the practical implications of using it within the Orthoptera workflow.

The investigation is retained here as evidence of what was examined rather than as an adoption statement.

[Historical detailed material retained from the investigation.]

---

# Experiment L — KiroGraph investigation

KiroGraph was investigated specifically in relation to Orthoptera's repository-navigation, context-efficiency and AI/toolchain experimentation.

The investigation considered the capability provided by the project and its relevance to the developing Orthoptera workflow.

The investigation is retained here as evidence of what was examined rather than as an adoption statement.

[Historical detailed material retained from the investigation.]

---

# Experiment M — Nella investigation

Nella was investigated as part of the Orthoptera AI/toolchain research.

The investigation examined its capabilities and limitations in relation to repository understanding, context acquisition and AI-assisted development.

A subsequent adversarial refinement revisited the first-pass conclusions rather than treating the initial assessment as final.

This distinction is itself useful experimental evidence: a toolchain capability assessment may need to be challenged after the initial reconnaissance has established a more precise understanding of the project's requirements.

[Historical detailed material retained from the investigation and subsequent refinement.]

---

# Experiment N — SQLite context-sharing possibility

The investigation considered whether SQLite-backed context or state could provide a useful mechanism for sharing information between AI processes or roles.

The possibility was intriguing because a shared structured store could, in principle, provide a boundary between transient model context and durable machine-readable state.

No sufficiently established capability was identified that would justify treating this as an available component of the Orthoptera workflow.

The possibility is therefore retained as an experimental observation and not as a project requirement or adopted capability.

---

# Experimental lessons retained across the investigation

The experiments have repeatedly reinforced several distinctions.

## Observation versus inference

An agent's behaviour does not by itself establish the internal mechanism that produced it.

For example, an agent recovering information after a session boundary does not establish whether that information came from model memory, persistent tool state, repository inspection, cached context, or another mechanism.

## Capability versus availability

A tool may document a capability without that capability being available in the configuration, account tier or environment being tested.

Conversely, a capability demonstrated experimentally should not automatically become a project dependency.

## Context versus persistence

Context available during a model invocation, state retained by a tool, repository knowledge, and persistent memory are different things.

Experiments should identify which of these mechanisms is actually being observed.

## Navigation versus knowledge

A tool that can locate relevant repository material is not necessarily a knowledge store.

A graph, index or search mechanism may improve context acquisition without itself constituting persistent project knowledge.

## Cost versus capability

A technically suitable tool is not necessarily the most appropriate operational choice.

The project has an established preference for zero-cost or already-available capabilities. Experiments may investigate paid or unavailable capabilities, but doing so does not imply adoption.

## Historical evidence matters

An experiment that does not produce an adopted tool or method is not necessarily a failed experiment.

Negative results, limitations, discarded approaches and superseded interpretations remain part of the evidence base.

---

# Current experimental record

This journal contains the historical record of toolchain experimentation completed to date.

Future experiments are not scheduled here. They belong in `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md`.

Future decisions arising from experiments belong in `TOOLCHAIN_DECISIONS.md`.

Candidate capabilities and useful-but-not-adopted facilities belong in `TOOLCHAIN_WISHLIST.md`.

The journal should be extended by appending new dated experiment entries rather than by repeatedly rewriting earlier entries into a new summary.
