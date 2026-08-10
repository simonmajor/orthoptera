# AI Toolchain Wishlist

This document records AI/development-tool capabilities that appear useful for Orthoptera but are not currently part of the adopted workflow.

It is deliberately a **wishlist rather than a roadmap**. An item may remain here indefinitely. Inclusion does not imply that a capability should be implemented, that a particular product should be adopted, or that expenditure is justified.

The project has an established preference for existing **zero-cost / account-tier capabilities**. A capability may nevertheless be worth recording when it is currently unavailable, requires additional infrastructure, is paid, or has not yet demonstrated sufficient benefit.

The purpose of the wishlist is partly to prevent useful capability ideas from being lost or repeatedly rediscovered.

Toolchain decisions are recorded in `TOOLCHAIN_DECISIONS.md`. Experimental evidence is recorded in `TOOLCHAIN_EXPERIMENTS.md`. The wishlist should not silently become either.

---

## Repository context and orientation

### Scoped repository access

**Desired capability:** Give an AI role access to explicitly selected repository roots or directories rather than implicitly exposing everything available in the workspace.

**Why useful:** Different AI roles may need access to different parts of the repository. Explicit scoping could reduce accidental access to unrelated material and make specialist roles easier to reason about.

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

**Why useful:** Broad reconnaissance has demonstrated substantial token and context consumption. An agent should be able to establish orientation cheaply and progressively retrieve only the material needed for the current task.

**Potential benefit:** high.

**Current status:** demonstrated by MCP reference implementations; candidate for future experimentation.

---

### Selective Git context

**Desired capability:** Allow an AI to ask focused questions about repository history and state, such as:

* what changed since a particular revision;
* recent commits;
* staged and unstaged changes;
* a particular revision;
* branch state;
* focused historical context for a file or change.

**Why useful:** Repository history is often relevant context, but replaying broad history is unnecessary.

**Potential benefit:** medium-high.

**Current status:** demonstrated by the MCP Git reference implementation; not adopted.

---

### Persistent structural repository representation

**Desired capability:** Maintain a persistent representation of repository structure that can be reused between AI sessions rather than repeatedly reconstructing repository relationships from source.

Useful forms may include:

* symbols;
* imports;
* callers/callees;
* dependencies;
* inheritance;
* references;
* impact relationships;
* execution/process relationships.

**Why useful:** Structural relationships can provide context that is difficult and expensive for an agent to reconstruct repeatedly from raw source.

The GitNexus investigation demonstrated that persistent structural representation can be combined with semantic retrieval and reused across subsequent processes.

**Potential benefit:** high.

**Current status:** capability demonstrated by investigated tooling; adoption not decided.

---

### Persistent hybrid structural and semantic retrieval

**Desired capability:** Combine persistent structural repository knowledge with lexical and/or semantic retrieval so that an agent can discover relevant code through both program relationships and meaning.

**Why useful:** Structural navigation and semantic retrieval answer different questions. Combining them could provide a more effective discovery mechanism than either alone.

The GitNexus investigation demonstrated this capability as a toolchain pattern.

**Potential benefit:** high.

**Current status:** demonstrated capability; Orthoptera-specific cost and productivity benefit not established.

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

**Current status:** protocol capability demonstrated; implications for the Orthoptera workflow remain under investigation.

---

### Discover-then-fetch context

**Desired capability:** Allow a tool or agent to identify a potentially relevant resource first, then retrieve its contents only when required.

**Why useful:** This could reduce unnecessary context consumption when a resource is large but only occasionally relevant.

MCP resource links provide a concrete example of this pattern.

**Potential benefit:** medium.

**Current status:** demonstrated as an MCP capability; no Orthoptera implementation yet.

---

### Validity-aware persistent project knowledge

**Desired capability:** Represent durable project knowledge together with enough provenance and validity information to identify knowledge that may have become stale after relevant project changes.

Possible mechanisms include:

* explicit source association;
* dependency association;
* validity state;
* invalidation;
* review or revalidation;
* conflict detection.

**Why useful:** Persistent knowledge is only useful if an agent can distinguish information that remains applicable from information that may have been superseded.

The investigations of persistent-memory and assumption-tracking tools have demonstrated several different implementations of this general capability.

**Important constraint:** invalidation based on an associated file or dependency changing is not equivalent to proving that a proposition is false.

**Potential benefit:** medium-high.

**Current status:** capability class demonstrated by investigated tooling; no Orthoptera-specific benefit established.

---

## AI workflow and reproducibility

### Predictable model selection

**Desired capability:** Explicitly select and pin the model used for an experiment or workflow.

**Why useful:** Model selection can affect context limits, behaviour, reproducibility and cost. Controlled experiments should not inadvertently compare different models.

The Copilot investigations demonstrated that the active model can be observed and that model selection is available, but the precise implications for all workflows have not been established.

**Potential benefit:** high for experiments.

**Current status:** capability available in investigated tooling; experimental use is desirable.

---

### Reproducible / isolated AI sessions

**Desired capability:** Start an AI session with explicitly controlled:

* conversation history;
* repository state;
* model;
* tool configuration;
* MCP servers;
* persistent session state;
* repository-level memory where applicable.

**Why useful:** A genuinely controlled experiment requires a way to distinguish fresh conversational context from persistent state and other sources of prior knowledge.

The Copilot investigation established that a fresh conversational session does not necessarily imply absence of persistent repository memory.

**Potential benefit:** high for experiments.

**Current status:** desirable capability; precise experimental controls remain tool-dependent.

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

### Experiment-level usage accounting

**Desired capability:** Attribute AI usage to meaningful units such as:

* parent-agent work;
* delegated-agent work;
* tool calls;
* cached context;
* reasoning;
* output.

**Why useful:** This would make it easier to compare alternative AI workflows and understand where resource consumption actually occurs.

**Potential benefit:** high.

**Current status:** partially available through existing tooling; precise accounting relationships remain incompletely established.

---

## Agent organisation and delegation

### Hierarchical agent instructions

**Desired capability:** Share a common baseline of agent instructions while allowing specialist roles to load only the instructions relevant to their task.

**Why useful:** Different AI roles may need different operational guidance. Scoping instructions could reduce unnecessary context while avoiding duplicated or conflicting sources of truth.

The project is separately investigating the appropriate structure of `AGENTS.md` and any subordinate instruction documents.

**Potential benefit:** high.

**Current status:** desirable capability; exact project structure unresolved.

---

### Better subagent control

**Desired capability:** Explicit control over:

* delegated model;
* delegated context;
* delegation cost;
* task scope;
* returned output size.

**Why useful:** Delegated reconnaissance can be expensive even when the requested result is relatively small. Better control could make delegation more predictable and economical.

**Potential benefit:** high.

**Current status:** capability varies by tool; no preferred implementation established.

---

### Specialist roles with bounded context

**Desired capability:** Delegate a narrowly defined task to an AI role while providing it with only the repository, documentation and other context necessary for that task.

**Why useful:** Specialist roles could isolate expensive exploratory work from the main architectural conversation while avoiding the cost of repeatedly supplying irrelevant project history.

**Potential benefit:** high.

**Current status:** demonstrated as a general workflow pattern; Orthoptera-specific cost/benefit remains an experimental question.

---

### Asynchronous specialist tasks

**Desired capability:** Start an investigation that can continue independently and return a result when complete, rather than keeping the initiating interaction synchronously tied to every intermediate operation.

**Why useful:** Some research and corpus-analysis tasks naturally involve many tool calls and may be better isolated from the main conversational context.

MCP reference implementations demonstrate a task lifecycle supporting this model.

**Potential benefit:** medium.

**Current status:** demonstrated as an MCP capability; no Orthoptera-specific requirement established.

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

### Explicit role/tool authority

**Desired capability:** Define which tools and operations a particular AI role is permitted or expected to use.

**Why useful:** Architectural, implementation, reconnaissance and specialist roles may have different appropriate authorities. Explicit boundaries could reduce accidental modification or unnecessary access.

**Potential benefit:** high.

**Current status:** desirable capability; implementation approach unresolved.

---

## Repository orientation

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

### Progressive context acquisition

**Desired capability:** Allow an agent to begin with a small orientation and progressively request additional context as the task requires it.

**Why useful:** This combines cheap orientation with bounded retrieval. It avoids the false choice between giving an agent the entire repository context and giving it no useful orientation.

The investigated MCP patterns demonstrate several ways of separating discovery from retrieval.

**Potential benefit:** very high.

**Current status:** capability demonstrated in principle; Orthoptera workflow not yet established.

---

## Other useful capabilities

### More predictable cost controls

**Desired capability:** Provide explicit limits or forecasts for AI-resource consumption before or during an expensive task.

**Why useful:** Broad reconnaissance has demonstrated that agentic exploration can consume unexpectedly large amounts of model resources.

**Potential benefit:** high.

**Current status:** partially demonstrated by Copilot CLI usage controls; broader applicability remains unresolved.

---

### Additional useful paid capabilities

Potentially useful paid services or features discovered during the project should be recorded here rather than silently becoming workflow assumptions.

Any such capability would need to be evaluated against the project's established zero-cost preference before adoption.

The presence of a paid capability in this document is therefore not a recommendation to purchase it.

---

## Evaluation principle

A wishlist item should move toward adoption only when there is evidence that it provides a meaningful benefit relative to:

* token/AI-credit cost;
* configuration complexity;
* maintenance burden;
* security implications;
* additional background context;
* operational complexity;
* and the size and needs of the Orthoptera project.

The distinction between **capability**, **usefulness**, and **adoption** should be preserved:

> A tool may demonstrate a useful capability without establishing that Orthoptera should use that tool.

Likewise, a capability may be desirable in principle without establishing that the project currently needs it.

The default should therefore remain:

> **Prefer the smallest capability that solves the demonstrated problem.**

---

## Status

This document is a wishlist, not a roadmap.

Items may remain here indefinitely.

An item should move into the adopted workflow only after an explicit decision is made and the relevant project documentation is updated.

A wishlist entry should not be treated as an outstanding project task merely because it remains present.

