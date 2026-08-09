# AI Toolchain Wishlist

This document records capabilities that could improve Orthoptera's AI-assisted development workflow.

Items here are **wishlist ideas, not commitments**. Inclusion does not imply that a capability should be implemented, that a particular product should be adopted, or that expenditure is justified.

The primary constraint is the established preference to use existing **zero-cost / account-tier capabilities** where practical. A capability can therefore be worth recording even when it is currently unavailable or would require a paid service.

Toolchain decisions are recorded in `TOOLCHAIN_DECISIONS.md`. Experimental evidence is recorded in `TOOLCHAIN_EXPERIMENTS.md`.

---

## Repository context and orientation

### Scoped repository access

**Desired capability:** Give an AI role access to explicitly selected repository roots or directories rather than implicitly exposing everything available in the workspace.

**Why useful:** Different AI roles should be able to receive only the repository material relevant to their task. This would support specialist roles and reduce accidental access to unrelated material.

The MCP Filesystem reference implementation demonstrates explicit filesystem roots and read/write capability distinctions.

**Potential benefit:** high.

**Current status:** demonstrated as an MCP capability; not adopted.

---

### Bounded repository retrieval

**Desired capability:** Retrieve repository information incrementally through operations such as:

* search;
* directory structure;
* file metadata;
* selected line ranges;
* file heads/tails;
* multiple related files;
* filtered results.

**Why useful:** Broad reconnaissance has already demonstrated substantial token consumption. An agent should be able to establish orientation cheaply and progressively retrieve only the material needed for the current question.

**Potential benefit:** high.

**Current status:** demonstrated by MCP reference implementations; candidate for future experimentation.

---

### Selective Git context

**Desired capability:** Allow an AI to ask focused questions about repository history and state, such as:

* what changed since a particular revision;
* recent commits;
* staged/unstaged changes;
* a particular revision;
* branch state.

**Why useful:** Repository history is often relevant context, but replaying broad history is unnecessary.

**Potential benefit:** medium-high.

**Current status:** demonstrated by the MCP Git reference implementation; not adopted.

---

## Knowledge management

### Selectively retrievable persistent knowledge

**Desired capability:** Store durable toolchain or project knowledge as small, queryable units rather than requiring an agent to replay an entire conversation or read every historical document.

**Why useful:** Orthoptera deliberately treats repository documentation as durable project knowledge, but specialist AI roles should not necessarily load all historical knowledge for every task.

The MCP Memory reference implementation demonstrates one possible model using entities, relations and atomic observations.

**Important constraint:** this is a capability to investigate, not a recommendation to introduce a separate memory database. Repository documentation remains the authoritative source for project decisions.

**Potential benefit:** medium-high.

**Current status:** conceptual capability demonstrated; architecture unresolved.

---

### Contextual resources separate from executable tools

**Desired capability:** Distinguish between:

* instructions/prompts;
* contextual resources;
* executable tools.

**Why useful:** Not everything an agent needs to know should be represented as an executable tool or injected into every conversation.

MCP reference implementations explicitly demonstrate these separate concepts.

**Potential benefit:** medium-high.

**Current status:** protocol capability demonstrated; implications for Orthoptera workflow remain under investigation.

---

### Discover-then-fetch context

**Desired capability:** Allow a tool or agent to identify a potentially relevant resource first, then retrieve its contents only when required.

**Why useful:** This could reduce unnecessary context consumption when a resource is large but only occasionally relevant.

MCP resource links provide a concrete example of this pattern.

**Potential benefit:** medium.

**Current status:** demonstrated as an MCP capability; no Orthoptera implementation yet.

---

## Agent safety and role separation

### Machine-readable tool safety

**Desired capability:** Tools should expose whether an operation is:

* read-only;
* destructive;
* idempotent;
* or otherwise consequential.

**Why useful:** Orthoptera may eventually use different AI roles with different authority. Machine-readable capability information could supplement natural-language guardrails.

The MCP Filesystem reference implementation demonstrates such annotations.

**Potential benefit:** medium-high.

**Current status:** demonstrated as an MCP capability; workflow implications unresolved.

---

### Specialist tool profiles

**Desired capability:** Different AI roles should receive different sets of tools and MCP servers according to their responsibilities.

Examples might eventually include:

* architectural/research role;
* implementation role;
* local-corpus analysis role;
* review/verification role.

**Why useful:** This could reduce both context overhead and accidental authority.

**Potential benefit:** high.

**Current status:** strongly aligned with the emerging workflow, but the final role structure remains experimental.

---

## Experimental workflow

### Bounded AI-credit experiments

**Desired capability:** Run individual toolchain experiments under an explicit AI-credit ceiling.

**Why useful:** Broad reconnaissance has already demonstrated that apparently modest requests can produce unexpectedly large model usage.

Copilot CLI's `/limits` provides a direct mechanism for this.

**Potential benefit:** high.

**Current status:** available and already demonstrated.

---

### Better experimental telemetry

**Desired capability:** Record enough information to compare experiments quantitatively, including:

* model;
* context configuration;
* MCP/tool configuration;
* current context;
* cumulative input/output tokens;
* cached tokens;
* AI credits;
* number of model turns;
* subagent invocations;
* tool calls;
* compactions.

**Why useful:** A single token figure is insufficient to explain cost or context behaviour.

**Potential benefit:** high.

**Current status:** much of this information is exposed by Copilot CLI; systematic experimental recording remains to be developed.

---

### Cheap repository orientation

**Desired capability:** Give an agent a concise, reliable repository orientation without requiring a large exploratory reconnaissance.

The orientation might establish:

* project purpose;
* authoritative documentation;
* relevant directory structure;
* current implementation status;
* active constraints;
* where specialist information lives.

**Why useful:** This directly addresses the high-cost reconnaissance observed in the Copilot experiments.

**Potential benefit:** very high.

**Current status:** explicitly desirable; solution unresolved.

---

## Long-running and asynchronous work

### Asynchronous specialist tasks

**Desired capability:** Start an investigation that can continue independently and return a result when complete, rather than keeping the initiating interaction synchronously tied to every intermediate operation.

**Why useful:** Some research and corpus-analysis tasks naturally involve many tool calls and may be better isolated from the main conversational context.

MCP reference implementations demonstrate a task lifecycle supporting this model.

**Potential benefit:** medium.

**Current status:** demonstrated as an MCP capability; no Orthoptera-specific requirement established.

---

## Tooling that is currently out of reach

The wishlist deliberately records useful capabilities even when they do not currently justify expenditure.

Potential reasons for retaining an item include:

* useful capability but paid implementation;
* useful capability but excessive operational complexity;
* useful capability but insufficient benefit for a project of Orthoptera's size;
* useful capability whose value has not yet been demonstrated.

Such items should not be treated as deficiencies in the current workflow.

The goal is to avoid rediscovering useful ideas later.

---

## Evaluation principle

A wishlist item should move toward adoption only when there is evidence that it provides a meaningful benefit relative to:

* token/AI-credit cost;
* configuration complexity;
* maintenance burden;
* security implications;
* additional background context;
* and the size and needs of the Orthoptera project.

The default should therefore remain:

> **Prefer the smallest capability that solves the demonstrated problem.**

## Structural repository navigation

**Status:** Capability identified; implementation not yet selected.

Expose a repository's structural relationships to AI roles in addition to lexical filesystem/search access. Useful structural primitives include:

* symbols and definitions;
* callers and callees;
* imports and references;
* dependency relationships;
* call sites and source locations;
* type/inheritance relationships where available;
* data-flow relationships where reliably supported.

Prefer a **discover → fetch** workflow in which structural queries identify relevant symbols, relationships and source locations before the agent retrieves source text.

This is distinct from:

* **lexical repository navigation** — finding paths and text;
* **semantic repository retrieval** — selecting repository content by natural-language relevance;
* **persistent repository knowledge** — retaining a reusable repository representation across processes/sessions.

A structural navigation layer should not be assumed to provide semantic/vector retrieval, persistent knowledge, bounded model context, or token/cost savings unless those capabilities are independently demonstrated.

