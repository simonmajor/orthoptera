# Toolchain Decisions

This document records decisions about how AI tools are used in the development of Orthoptera.

It is deliberately separate from the technical architecture of Orthoptera. Technical design decisions belong in `DECISIONS.md`; observations from experiments with the AI toolchain belong in `TOOLCHAIN_EXPERIMENTS.md`.

Only actual decisions belong here. Observations, hypotheses and unresolved questions should remain in `TOOLCHAIN_EXPERIMENTS.md`.

---

## Decisions

### 2026-08 — Cost constraints are a project constraint

The project has a **zero-cost preference** for AI and development tooling.

This preference predates the Orthoptera project and therefore forms part of the background constraint within which the AI workflow is being developed.

"Zero-cost" does not mean that only free software may ever be used. It means that paid services or upgrades should not be assumed to be available when designing the workflow. Useful paid capabilities may instead be recorded for future consideration in `TOOLCHAIN_WISHLIST.md`.

---

### 2026-08 — Initial two-tier AI workflow

The initial AI workflow uses two principal tiers:

1. **ChatGPT** for architectural reasoning, design discussion and higher-level analysis.
2. **Codex** for implementation work against the local repository.

The division is intended to keep architectural decisions and implementation work distinct while allowing the implementation tier to work directly with the repository.

This is a working arrangement rather than a claim that these are the only appropriate tools for the project.

---

### 2026-08 — Working with AI coding agents belongs in contributor documentation

The operational workflow for AI-assisted development should be documented as part of the project's contributor/agent guidance rather than in a separate toolchain guide.

The principal locations are:

* `CONTRIBUTING.md` for human-facing workflow and contributor guidance;
* `AGENTS.md` for instructions that must be available to coding agents.

This avoids creating a second workflow document that could diverge from the actual project instructions.

---

### 2026-08 — The local acoustic survey was appropriately delegated, but exposed a cost issue

Given the established two-tier workflow, using Codex for the ad hoc local-corpus acoustic survey was the appropriate allocation of work.

The task involved local files, exploratory analysis and implementation-oriented investigation, all of which fit the implementation tier.

However, the work also demonstrated that a technically appropriate allocation can still be expensive in token/context terms.

This observation motivated investigation of alternative AI workflows, including GitHub Copilot CLI, delegation and session-level usage controls.

The decision is therefore not that Codex should or should not be used for similar work in future. The decision is that **tool allocation should be evaluated both for task suitability and for resource cost**.

---

### 2026-08 — Toolchain knowledge should be captured explicitly

The investigation of AI tooling has itself become a project concern worth documenting.

Tool behaviour can affect:

* reproducibility;
* context availability;
* model selection;
* delegation;
* token consumption;
* AI-credit consumption;
* recovery of work;
* the amount of background context required by an agent.

Useful knowledge discovered through experiments should therefore be persisted in the repository rather than relying on conversation history.

The toolchain documentation is divided as follows:

* `TOOLCHAIN_EXPERIMENTS.md` — observations and experimental results;
* `TOOLCHAIN_DECISIONS.md` — decisions made as a consequence;
* `TOOLCHAIN_WISHLIST.md` — useful capabilities that are not currently adopted;
* `CONTRIBUTING.md` — human-facing workflow;
* `AGENTS.md` — agent-facing workflow and guardrails.

---

### 2026-08 — Avoid unnecessary background context

The AI workflow should avoid loading large amounts of background material merely because it exists.

The project is expected to use multiple AI tiers and potentially different specialist roles. Instructions and supporting material should therefore be structured so that an agent receives the context necessary for its particular task without automatically receiving the entire history of the project.

The precise structure of agent-specific instructions remains an experimental/workflow question and is not prescribed here.

---

## Open questions

The following are deliberately **not decisions**:

* the final number and division of AI tiers;
* whether GitHub Copilot CLI becomes part of the regular workflow;
* the exact role of delegated/subagent workflows;
* how fresh an AI session must be for reproducible experiments;
* how AI credits relate to token consumption;
* which repository instructions should be shared by all agents;
* whether specialist agent instructions should be split into subordinate documents;
* which paid capabilities, if any, would justify departing from the zero-cost preference.

These remain subjects for `TOOLCHAIN_EXPERIMENTS.md` and future decisions.

