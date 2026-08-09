# Toolchain Decisions

This document records deliberate decisions about how AI tools are used to develop and investigate Orthoptera.

It is not a record of every observation or experiment. Experimental evidence belongs in `TOOLCHAIN_EXPERIMENTS.md`; conclusions supported by that evidence belong in `TOOLCHAIN_FINDINGS.md`.

Decisions here govern the workflow unless explicitly superseded.

## Retrospective decisions

### 2026-08-09 — Work within established account tiers and a zero-cost preference

The project predates the current toolchain experiments and the preference to avoid additional expenditure on AI tooling is an established constraint.

We should therefore first investigate what can be achieved with the existing account tiers, locally available tools, open-source software, and already-connected services.

Discovering a potentially useful paid service does not imply that it should be adopted. Such discoveries belong in `TOOLCHAIN_WISHLIST.md`.

### 2026-08-09 — Use a two-tier ChatGPT + Codex workflow

The established workflow separates:

* **ChatGPT** as the architectural/reasoning AI, responsible for understanding the project, making or reviewing architectural decisions, and directing implementation work.
* **Codex** as the implementation AI, responsible for repository-local implementation and associated coding tasks.

This division is a working arrangement rather than a claim that either tool is intrinsically incapable of the other's tasks.

The current toolchain experiments are investigating how this division should evolve as additional AI tiers, models and agent roles become available.

### 2026-08-09 — Document the AI coding workflow in CONTRIBUTING.md

The practical workflow for contributors and AI coding agents should ultimately be documented in `CONTRIBUTING.md`.

`AGENTS.md` should contain instructions that an agent must follow when operating in the repository; `CONTRIBUTING.md` should explain the wider working practices.

Toolchain experimentation should therefore inform these documents rather than creating a competing permanent workflow manual.

### 2026-08-09 — The local-corpus acoustic survey was correctly delegated to Codex, but exposed a cost problem

Given the established two-tier workflow, using Codex to perform the ad hoc local-corpus acoustic survey was the correct allocation of responsibility: it required repository-local execution, local files and computational experimentation.

However, the task also consumed a substantial amount of model context/token budget.

This is an important distinction:

* the **tool choice was appropriate** under the established workflow;
* the **way the task was conducted may not have been efficient**.

The toolchain experiments should therefore investigate whether such computationally intensive exploratory work can be performed more economically without weakening the architectural/implementation separation.

### 2026-08-09 — Establish a separate toolchain knowledge base

The AI workflow has now generated enough observations, methodological lessons and tool-specific knowledge that keeping them solely in conversation history is no longer adequate.

A separate toolchain documentation set will therefore be maintained outside the core Orthoptera design documentation:

* `TOOLCHAIN_EXPERIMENTS.md` — experimental record and observations
* `TOOLCHAIN_DECISIONS.md` — deliberate workflow decisions
* `TOOLCHAIN_FINDINGS.md` — established knowledge derived from experiments
* `TOOLCHAIN_WISHLIST.md` — useful capabilities identified but not currently adopted

This separation is itself a deliberate decision.

The purpose is to preserve useful knowledge without allowing toolchain-specific observations, transient capabilities, or currently unaffordable tooling to pollute the project's architectural documentation.

## Decision-making principles

### Evidence before architecture

Tool behaviour should be established experimentally where practical rather than inferred from appearances, model explanations, or assumptions about internal architecture.

In particular, the existence of:

* session state,
* agent state,
* MCP connections,
* command history,
* generated files,
* or context outside the visible prompt

must not automatically be interpreted as model memory.

### Keep experiments separate from project requirements

A toolchain experiment may reveal a useful capability without implying that Orthoptera should depend on it.

Conversely, an experiment may reveal a limitation without requiring an immediate change to the project architecture.

Project requirements belong in the project documentation; toolchain observations belong in the toolchain documentation until there is a deliberate decision to promote them.

### Prefer the cheapest adequate capability

Where several available approaches can perform a task adequately, prefer the approach consistent with the project's established zero-cost constraint and existing account tiers.

This does not mean avoiding experimentation with more capable tools. It means distinguishing:

* what is useful to know,
* what is useful to have,
* and what we are actually prepared to adopt.

### Minimise unnecessary context

As the workflow develops multiple AI tiers and potentially specialised roles, agents should receive the minimum context necessary to perform their task correctly.

Repository documentation should therefore be structured so that:

* project-wide invariants are easy to discover;
* role-specific instructions can be scoped appropriately;
* experimental history does not become mandatory background context;
* historical observations are not repeatedly injected into implementation tasks.

This principle will inform future experiments concerning `AGENTS.md` and subordinate instruction documents.

## Relationship to other documentation

`AGENTS.md` contains mandatory repository instructions for AI agents.

`CONTRIBUTING.md` contains the practical development workflow, including the eventual documented approach to working with AI coding agents.

`TOOLCHAIN_EXPERIMENTS.md` records what we tried and what happened.

`TOOLCHAIN_FINDINGS.md` records knowledge that has survived the distinction between observation and inference.

`TOOLCHAIN_WISHLIST.md` records useful capabilities that are not currently adopted.

None of the toolchain documents should silently override project architecture or repository instructions.

