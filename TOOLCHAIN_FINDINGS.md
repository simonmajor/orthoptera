# AI Toolchain Findings Journal

This document is the **historical journal of durable findings from the AI-toolchain investigation** for Orthoptera.

It is a research record, not project architecture, a completed-experiment record, a wishlist, or a planning document.

## Journal invariants

This journal is **append-only in its normal operation**.

An entry preserves a durable finding as it was established at that point in the investigation.

Later findings may qualify, refine, supersede or contradict earlier findings. They do so through **later journal entries**. Earlier findings are not retrospectively rewritten merely to produce a cleaner current synthesis.

Historical qualification and uncertainty are information. Where a finding depended on an interpretation, limitation or unresolved question, that context remains part of the historical record.

The journal records findings that have actually been established. It is not the mutable sequence of experiments currently planned.

Forward-looking implications, speculation and unresolved questions may nevertheless appear when they are part of the finding produced by an investigation. They are historical evidence of what that investigation established or implied at the time; they must not be removed merely because later work resolved or superseded them.

A concrete experiment that remains worth running may separately appear in `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md`. That does not require removing the historical rationale or implication from this journal.

## What a finding should preserve

Where applicable, a finding should retain:

* the subject of the finding;
* the evidence supporting it;
* the distinction between direct observation and inference;
* relevant tool, repository, component and version pointers;
* relevant experiment references;
* important limitations or uncertainties;
* relationships to earlier findings;
* implications and unresolved questions produced by the investigation;
* and the scope within which the finding is valid.

Do not reduce a researched tool to an unexplained shorthand name when doing so would lose the identity, provenance or origin of the thing investigated.

The distinction between evidence and interpretation is important. A capability may be:

* directly demonstrated during an investigation;
* reported by a tool or its documentation;
* inferred from observed behaviour;
* identified as potentially useful;
* or still unresolved.

Those states are not interchangeable. Where a finding depends on an interpretation, that dependency should remain visible.

A finding about a tool does not automatically establish a benefit for Orthoptera.

A finding should not be treated as a project requirement or adoption decision unless the appropriate project or toolchain decision record says so.

## Relationship to the other toolchain records

The toolchain documentation is deliberately divided by function:

* `TOOLCHAIN_EXPERIMENTS.md` — completed investigations, experiments and their contemporary evidence;
* `TOOLCHAIN_FINDINGS.md` — durable findings and their historical development;
* `TOOLCHAIN_DECISIONS.md` — actual toolchain decisions;
* `TOOLCHAIN_WISHLIST.md` — useful capabilities that are not currently adopted;
* `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md` — the mutable current sequence of experiments still worth considering or running.

These records may legitimately overlap where they preserve different aspects of the same investigation. That overlap must not be eliminated merely for concision.

In particular, the findings journal must not be rewritten merely because a later finding provides a better current synthesis. The later finding should instead record the refinement, qualification or supersession.

## Findings journal

The historical findings record follows.

---

## Structural repository navigation

**Investigation:** Code Pathfinder
**Candidate:** `shivasurya/code-pathfinder`

### Finding

The Code Pathfinder investigation established **structural repository navigation** as a distinct capability beyond ordinary filesystem and lexical search.

The investigated system can construct a local representation of source structure including symbols, modules and program relationships such as callers and callees, and expose compact structural queries to an AI agent.

This establishes a useful capability distinction:

```text
Level 1 — lexical repository navigation
    filesystem / shell / text search
            ↓
Level 2 — structural repository navigation
    symbols / modules / relationships / graph
```

Structural navigation should therefore not be subsumed into a generic description such as "repository search".

### Demonstrated capability

The investigation established evidence for:

* structural analysis of source repositories;
* symbols and modules;
* program relationships;
* caller/callee relationships;
* compact structural queries;
* use as a discovery layer before retrieving source text.

### Important qualification

The existence of a structural repository index does **not** establish:

* semantic/vector retrieval;
* persistent project knowledge;
* bounded model context;
* reduced token consumption;
* reduced AI-credit consumption;
* reduced monetary cost;
* or improved task correctness.

Those are separate capabilities or outcome hypotheses and require independent evidence.

### Orthoptera relevance

Structural repository navigation is potentially important because an agent can establish relationships locally before retrieving large quantities of source text.

The relevant capability is therefore distinct from the efficiency hypothesis:

> **Structural navigation is demonstrated; any reduction in model-side work remains an empirical question.**

---

## GitNexus — persistent hybrid repository retrieval

**Investigation date:** 9 August 2026
**Candidate:** upstream `abhigyanpatwari/GitNexus`
**Branch investigated:** `main`
**Latest identifiable stable release during investigation:** `1.6.9`, 4 July 2026

### Finding

GitNexus is a local repository-analysis and retrieval system combining:

1. lexical navigation;
2. structural repository navigation;
3. optional semantic/vector retrieval;
4. persistent repository knowledge.

Its repository representation is constructed through static analysis and stored persistently in a local graph database.

The investigated system exposes structural relationships including symbols, calls, imports, dependencies, inheritance, processes and impact relationships. Optional embedding/vector retrieval provides a semantic discovery layer over the repository representation.

This makes GitNexus materially different from a filesystem/search baseline and extends beyond the Level-2 structural-navigation capability established by the Code Pathfinder investigation.

### Architectural classification

```text
Level 1 — lexical navigation
    text / FTS / BM25
            ↓
Level 2 — structural navigation
    AST / symbols / relationships / graph
            ↓
Level 3 — semantic retrieval
    embeddings / vector search / hybrid ranking
            ↓
Persistent repository representation
    reusable indexed state
```

The persistence dimension is orthogonal to the retrieval levels. A repository can have lexical, structural or semantic indexes without necessarily retaining them across processes or sessions.

GitNexus demonstrably combines persistence with higher-level retrieval capabilities.

### Demonstrated capabilities

The investigation established evidence for:

* AST-based repository analysis;
* symbol and relationship indexing;
* callers/callees and dependency traversal;
* imports and inheritance relationships;
* execution/process representations;
* impact analysis;
* lexical/full-text retrieval;
* optional embeddings;
* vector retrieval;
* hybrid lexical/vector ranking;
* persistent on-disk repository indexes;
* reuse across subsequent processes/sessions;
* incremental/staleness handling;
* Git-diff to structural-impact mapping;
* bounded MCP responses;
* discover → fetch workflows.

### Important distinctions

GitNexus should not be described merely as a graph visualiser or search wrapper.

It should also not be described as an LLM-generated repository-memory system. Its core structural representation is produced by static analysis and can be queried without an LLM. Semantic retrieval uses embeddings, which is distinct from LLM reasoning about the repository.

Its Git integration should not be described as a comprehensive Git-history knowledge graph. The demonstrated Git capability is primarily the mapping of current repository state and changes onto structural repository knowledge.

### Discover → fetch

GitNexus supports a progressive retrieval pattern:

```text
task
  ↓
search / query
  ↓
relevant symbols, processes and locations
  ↓
structural context
  ↓
targeted source
```

This is relevant to the project's bounded-retrieval objective because discovery need not immediately return large amounts of source.

Ordinary filesystem access remains useful for arbitrary file and line-range retrieval.

### Persistence

The repository representation is stored locally and can be reused after the original indexing process and across subsequent MCP processes/sessions.

The implementation also contains mechanisms for detecting stale repository state and updating the index.

This is materially different from an in-memory structural-analysis server that reconstructs its graph at startup.

### Efficiency qualification

The investigation demonstrated the **mechanism** by which GitNexus could reduce exploratory model work: precomputed relationships and semantic retrieval can identify relevant repository material before the model reads large amounts of source.

It did **not** demonstrate, for Orthoptera:

* lower cumulative input tokens;
* lower cumulative output tokens;
* lower cached-token usage;
* lower context occupancy;
* fewer model turns;
* lower AI credits;
* lower monetary cost;
* or better correctness per unit of cost.

Those remain empirical questions.

Product-level token-efficiency claims must therefore not be treated as Orthoptera findings.

### Relationship to Code Pathfinder

Code Pathfinder established structural repository navigation as a distinct capability beyond lexical filesystem/search tooling.

GitNexus confirms and extends that distinction by combining structural navigation with persistent repository representation and optional semantic retrieval.

---

## Persistent semantic retrieval

The investigations established a separate capability class for **semantic repository retrieval**.

Hybrid retrieval systems can combine lexical search with vector/embedding retrieval and, where available, reranking.

The important distinction is:

```text
lexical retrieval
    ↓
structural retrieval
    ↓
semantic retrieval
```

These should not be treated as interchangeable descriptions of repository access.

Semantic retrieval can identify repository material according to natural-language relevance without requiring the agent to formulate an exact textual search query.

However, semantic retrieval by itself does not establish:

* structural relationships;
* persistent project knowledge;
* semantic truth;
* reduced model cost;
* or improved task correctness.

Those properties require separate evidence.

---

## Persistent repository knowledge

The investigations established **persistent repository representation** as a capability distinct from transient repository analysis.

A tool can construct an indexed representation of a repository and retain it for reuse across processes or sessions.

Persistence can apply to:

* lexical indexes;
* structural indexes;
* semantic/vector indexes;
* or higher-level project knowledge.

The fact that a representation persists does not by itself establish that it is:

* automatically retrieved;
* automatically injected into model context;
* semantically current;
* source-of-truth project documentation;
* or cheaper than reconstructing the required context.

Persistence should therefore be recorded separately from retrieval and from demonstrated task benefit.

---

## MCP capability vocabulary

The MCP investigations established several useful capability patterns.

### Prompts, resources and tools

MCP reference implementations demonstrate a distinction between:

* prompts;
* contextual resources;
* executable tools.

This provides useful vocabulary for separating stable contextual material from operations.

### Discover then fetch

MCP resource links demonstrate that an agent can identify a potentially useful artefact without immediately embedding its complete contents into model context.

This is an example of context acquisition being separated from context consumption.

### Long-running tasks

MCP reference implementations demonstrate an asynchronous task lifecycle for operations that do not need to complete synchronously with the initiating request.

This may be useful to future specialist investigations, but no Orthoptera-specific benefit has been established.

### Tool safety metadata

MCP tool annotations can describe properties such as:

* read-only;
* destructive;
* idempotent.

This is potentially relevant to workflows in which different AI roles should have different authority.

No Orthoptera adoption decision follows from this capability observation.

---

## Persistent, selectively retrievable knowledge

The MCP Memory reference implementation demonstrated one possible model for storing knowledge as entities, relations and atomic observations.

This establishes a useful capability pattern:

> durable knowledge can be represented as small, queryable units rather than requiring an agent to replay an entire conversation or read every historical document.

This is potentially relevant to the Orthoptera workflow because repository documentation is deliberately durable project knowledge, while specialist AI roles may not need all historical knowledge for every task.

The existence of such a memory mechanism does **not** establish that Orthoptera should introduce a separate memory database.

Repository documentation remains the authoritative home for project decisions and durable project knowledge unless a deliberate architectural decision says otherwise.

---

## Repository context and bounded retrieval

The investigations established a set of related capability requirements around repository context acquisition.

### Scoped repository access

An AI role may benefit from access to explicitly selected repository roots or directories rather than implicitly exposing everything available in the workspace.

The MCP Filesystem reference implementation demonstrates explicit filesystem roots and read/write capability distinctions.

This is relevant to specialist roles and to reducing accidental access to unrelated material.

### Bounded repository retrieval

An AI role may benefit from retrieving repository information incrementally through operations such as:

* search;
* directory structure;
* file metadata;
* selected line ranges;
* file heads/tails;
* multiple related files;
* filtered results.

This is particularly relevant because broad repository reconnaissance has already demonstrated substantial model-resource consumption.

### Selective Git context

An AI role may benefit from focused access to repository history and state, including:

* changes since a particular revision;
* recent commits;
* staged/unstaged changes;
* a particular revision;
* branch state.

The MCP Git reference implementation demonstrates this capability.

These capabilities are related to bounded context acquisition but should not be assumed to provide token or cost savings without measurement.

---

## Agent organisation and role separation

The investigations established several potentially useful workflow capabilities.

### Specialist tool profiles

Different AI roles may benefit from different sets of tools and MCP servers according to their responsibilities.

Potential roles include:

* architectural/research;
* implementation;
* local-corpus analysis;
* review/verification.

This could reduce context overhead and accidental authority.

The final role structure remains a workflow question rather than an established Orthoptera requirement.

### Machine-readable tool safety

Tools can expose machine-readable information about whether operations are read-only, destructive, idempotent or otherwise consequential.

This may complement natural-language role restrictions.

### Delegation

Delegated agents can perform independently scoped repository exploration and return a useful cross-file interpretation.

However, delegation is not equivalent to free context isolation.

A delegated agent performs additional model work and can therefore trade main-context cleanliness for additional token and AI-credit consumption.

---

## Toolchain evidence discipline

The toolchain investigations established the importance of distinguishing several kinds of evidence:

```text
Observed
    ↓
Reported
    ↓
Demonstrated
    ↓
Inferred
    ↓
Unknown
```

These categories are not interchangeable.

In particular:

* a file or session artefact does not automatically prove model memory;
* persistent state does not automatically prove automatic retrieval;
* a structural index does not automatically prove token savings;
* a tool's documentation does not automatically prove behaviour in the Orthoptera workflow;
* a plausible explanation does not become established merely because it fits the observation.

This distinction is particularly important for AI systems because internal mechanisms are often not directly observable.

---

## Toolchain efficiency

The investigations established that **capability and efficiency are separate questions**.

A tool may demonstrably provide a capability while providing no demonstrated benefit in:

* model turns;
* input tokens;
* output tokens;
* cached tokens;
* context occupancy;
* AI credits;
* monetary cost;
* latency;
* or correctness.

Conversely, a capability that appears expensive in isolation may still be useful if it changes the overall work allocation favourably.

Efficiency claims therefore require task-level measurement rather than inference from the apparent compactness or sophistication of a tool.

---

## Current capability vocabulary

The investigations support the following broad vocabulary:

```text
Level 1
lexical repository navigation
    ↓
Level 2
structural repository navigation
    ↓
Level 3
semantic repository retrieval
    ↓
persistent repository representation / knowledge
```

Persistence is not necessarily a higher retrieval level. It is an orthogonal property that may apply to different kinds of repository representation.

Similarly, **task benefit** is separate from capability:

```text
capability
    ↓
demonstrated mechanism
    ↓
task-level experiment
    ↓
measured benefit
```

A tool should not be credited with a cost, correctness or productivity advantage merely because it possesses a mechanism that could plausibly produce one.

---

## Orthoptera-specific implication

The investigations support treating the following as distinct toolchain capabilities:

* lexical repository access;
* structural repository navigation;
* semantic repository retrieval;
* persistent repository representation;
* persistent project/agent knowledge;
* bounded context acquisition;
* specialist role separation;
* delegation;
* tool safety metadata.

The presence of one capability must not be used as evidence that another is also present.

In particular:

> **Structural repository navigation should not be assumed to provide semantic/vector retrieval, persistent knowledge, bounded model context, or token/cost savings unless those capabilities are independently demonstrated.**

The same principle applies in the other direction: semantic retrieval should not be treated as structural understanding, and persistent state should not be treated as evidence of automatic memory or retrieval.

