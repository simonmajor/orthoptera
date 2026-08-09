# AI Toolchain Decisions

This document records decisions about how AI tools are used to develop and investigate Orthoptera.

These decisions concern the **development workflow and AI toolchain**, not the architecture of the Orthoptera software itself.

Experimental observations are recorded in `TOOLCHAIN_EXPERIMENTS.md`. Potential future capabilities are recorded in `TOOLCHAIN_WISHLIST.md`.

---

## Decision 1 — Respect the established zero-cost preference

**Date:** Before Orthoptera toolchain experimentation

The AI workflow should preferentially use the user's existing account tiers and zero-cost capabilities.

Paid tooling may still be investigated when it provides useful evidence or helps establish what is technically possible, but the existence of a useful paid capability is not by itself a reason to adopt it.

### Rationale

The zero-cost preference predates Orthoptera. It is therefore a constraint on the toolchain rather than an optimisation introduced in response to a particular experiment.

This also means that discovering a useful capability that is currently unavailable or paid is still worthwhile: it can be recorded for future consideration without becoming a current dependency.

---

## Decision 2 — Use complementary AI roles rather than one universal agent

**Date:** Initial Orthoptera AI workflow

The established workflow uses two complementary AI roles:

* **ChatGPT** for architectural reasoning, research, design review and directing investigations.
* **Codex** for implementation and work requiring direct access to the local repository or local corpus.

This is a practical division of responsibilities rather than a claim that either system is inherently incapable of performing the other's tasks.

### Rationale

The separation provides a useful boundary between architectural reasoning and implementation activity, while allowing local data and repository access to be used where it provides a material advantage.

---

## Decision 3 — Capture the AI workflow in project documentation

**Date:** August 2026

The project should document how humans and AI coding agents work together in `CONTRIBUTING.md`, with more detailed toolchain experimentation and decisions kept separately in the `TOOLCHAIN_*.md` documents.

### Rationale

The AI workflow has become sufficiently important that leaving it only in conversation history would make the project difficult to reproduce and would encourage future agents to infer rules from incomplete historical context.

`CONTRIBUTING.md` should eventually contain the human-facing workflow and guardrails.

The `TOOLCHAIN_*.md` documents provide a separate research and decision record so that experimental detail does not overwhelm the project's normal contribution guidance.

---

## Decision 4 — The ad hoc local-corpus acoustic survey was appropriately assigned to the local implementation tier

**Date:** August 2026

The use of Codex for the ad hoc local-corpus acoustic survey was operationally the correct choice under the established two-tier workflow because the work required direct access to the local corpus.

However, the experiment was also a useful demonstration that the operationally correct AI role is not necessarily the cheapest one in model-resource terms.

### Rationale

The survey required capabilities available naturally in the local implementation environment. Moving that work to the architectural/research tier merely to reduce token usage would have introduced other costs and limitations.

The lesson is therefore not "do not use Codex for large surveys". It is:

> **Tool-role selection and model-cost optimisation are separate considerations and may sometimes conflict.**

This became one of the motivations for investigating specialist roles, delegation and bounded context acquisition.

---

## Decision 5 — Knowledge capture is itself part of the AI workflow

**Date:** August 2026

The project should deliberately capture durable findings from AI-toolchain experiments rather than relying on conversation history.

The `TOOLCHAIN_*.md` documents are part of that knowledge-capture mechanism.

### Rationale

The experiments have already produced useful knowledge about:

* delegation;
* context consumption;
* model usage;
* caching;
* MCP capabilities;
* repository reconnaissance;
* and tool safety.

Without explicit capture, this knowledge is likely to be lost, repeatedly rediscovered, or accidentally transformed into undocumented assumptions.

Knowledge capture should therefore occur at natural checkpoints rather than only at the end of the overall toolchain investigation.

---

## Decision 6 — Keep toolchain experimentation separate from Orthoptera architecture

**Date:** August 2026

Findings about AI tools, agent behaviour and development workflow should not automatically become requirements or architectural decisions for the Orthoptera software.

Toolchain experiments belong in `TOOLCHAIN_EXPERIMENTS.md`, toolchain decisions belong in this document, and candidate capabilities belong in `TOOLCHAIN_WISHLIST.md`.

### Rationale

The toolchain is itself experimental.

Mixing speculative tooling ideas into `DESIGN.md`, `ROADMAP.md` or other project architecture documents would make it difficult to distinguish:

* what Orthoptera requires;
* what the development workflow happens to use;
* what an AI tool demonstrated;
* and what remains merely desirable.

This separation also makes it possible to change the AI workflow without unnecessarily changing the software architecture.

---

## Decision 7 — Treat delegation as a costed capability

**Date:** August 2026

Delegated AI agents should not be treated as merely a mechanism for moving context out of the main conversation.

They are separate model invocations and may introduce substantial additional token and AI-credit usage.

### Rationale

The Copilot reconnaissance experiment demonstrated this directly: the delegated explore agent produced a useful result but consumed approximately 290k tokens in the investigation.

Delegation therefore remains useful, particularly for specialist or independently scoped investigations, but its cost must be considered when designing experiments.

---

## Decision 8 — Prefer bounded experiments when investigating tool behaviour

**Date:** August 2026

Toolchain experiments that may generate substantial model usage should, where practical, be:

* narrowly scoped;
* reproducible;
* run with stable model/tool configuration;
* bounded by an explicit AI-credit limit;
* and followed by recording of the relevant usage measurements.

### Rationale

Broad reconnaissance has demonstrated that agentic exploration can consume unexpectedly large amounts of model resources.

Copilot's `/limits` mechanism provides a practical way to prevent an exploratory experiment from becoming unbounded.

The purpose is not to optimise every interaction. It is to make deliberately expensive experiments safe enough to run.

---

## Decision 9 — Distinguish experimental evidence from inference

**Date:** August 2026

AI-toolchain documentation should explicitly distinguish:

* **observed behaviour**;
* **documented product behaviour**;
* **experimental interpretation**;
* and **unresolved implementation details**.

Agents should not infer undocumented internal behaviour merely because an observed result appears consistent with a plausible explanation.

### Rationale

The Copilot investigations exposed several layers of behaviour — context, caching, delegation, persistent sessions and subagents — for which the public documentation does not necessarily specify every internal detail.

This distinction is necessary both for reproducibility and to prevent speculative claims from becoming toolchain folklore.

---

## Current status

These decisions establish the framework for the ongoing AI-toolchain investigation.

They do **not** yet establish:

* a final three-tier AI architecture;
* permanent specialist roles;
* a particular MCP server;
* an external memory system;
* a particular agent framework;
* or a requirement for any paid service.

Those remain experimental or wishlist subjects until separately decided.

