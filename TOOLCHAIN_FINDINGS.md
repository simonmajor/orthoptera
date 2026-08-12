# AI Toolchain Findings Journal

This document is the **historical journal of durable findings from the AI-toolchain investigation** for Orthoptera.

It is a research record, not project architecture, a completed-experiment record, a wishlist, or a planning document.

## Journal rules

This document is **append-only**.

A finding is a durable conclusion supported by the investigation. It may be stronger or more general than an individual experimental observation, but it must remain traceable to the evidence from which it was derived.

Later findings may qualify, refine, supersede or contradict earlier findings. They must not silently erase the earlier record.

Do not rewrite the journal merely to produce a cleaner current summary.

The journal records **findings that have actually been established**. It must not contain plans for future investigation.

In particular, do not add entries such as:

* "we should investigate...";
* "the next experiment should...";
* "this tool should be tested...";
* "future work ought to...".

Those belong in `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md`.

It is acceptable for a finding to record an unresolved question or a capability that could warrant further investigation. That is part of the finding's state, not a planning statement.

## What a finding should preserve

Where applicable, each finding should retain:

* the subject of the finding;
* the evidence supporting it;
* the distinction between direct observation and inference;
* relevant tool, repository, component and version pointers;
* relevant experiment references;
* important limitations or uncertainties;
* and the scope within which the finding is valid.

Do not reduce a researched tool to an unexplained shorthand name when doing so would lose the identity or provenance of the thing investigated.

Distinguish carefully between:

* a capability demonstrated directly;
* a capability documented by the tool;
* a capability inferred from observed behaviour;
* a capability identified as desirable;
* and a capability that remains unresolved.

A finding about a tool does not automatically constitute a finding that the tool benefits Orthoptera.

## Relationship to the other toolchain records

The toolchain documentation is deliberately divided by function:

* `TOOLCHAIN_EXPERIMENTS.md` — completed experiments and historical evidence;
* `TOOLCHAIN_FINDINGS.md` — durable findings;
* `TOOLCHAIN_DECISIONS.md` — actual decisions;
* `TOOLCHAIN_WISHLIST.md` — candidate capabilities;
* `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md` — future experiment planning.

Findings should not become a second experiment journal. Conversely, the experiment journal should not be rewritten merely to make the current findings easier to read.

## Findings journal

The durable findings record follows.

---

## Structural repository navigation is a distinct toolchain capability

**Finding:** Repository navigation should be distinguished into at least three levels:

1. **Lexical navigation** — filesystem paths, filename discovery, text search and source retrieval.
2. **Structural navigation** — AST/static-analysis-derived symbols and relationships such as definitions, callers/callees, imports, dependencies and source locations.
3. **Semantic retrieval** — task-aware relevance selection, potentially using embeddings, vector search, LLM-generated representations or other semantic retrieval mechanisms.

A fourth, orthogonal capability is **persistent repository knowledge**: retaining a reusable repository representation across processes or AI sessions and updating it as the repository changes.

The Code Pathfinder investigation established structural navigation as a concrete capability beyond ordinary filesystem and text search. It can support a **discover → fetch** workflow in which structural relationships are established before source is retrieved.

This does not establish that structural navigation by itself reduces context occupancy, cumulative tokens, cached tokens, AI credits or monetary cost.

**Implication:** Orthoptera should treat structural repository navigation as an independent toolchain capability rather than subsuming it under semantic search or generic repository retrieval.

---

## GitNexus — persistent hybrid repository retrieval

**Investigation date:** 9 August 2026

**Candidate:** upstream `abhigyanpatwari/GitNexus`, `main`

**Latest identifiable stable release at investigation time:** 1.6.9, 4 July 2026

### Finding

GitNexus demonstrated a combination of:

1. lexical navigation;
2. structural repository navigation;
3. optional semantic/vector retrieval;
4. persistent repository knowledge.

Its repository representation is constructed through static analysis and stored persistently. The investigated system exposes structural relationships including symbols, calls, imports, dependencies, inheritance, processes and impact relationships. Optional embedding/vector retrieval provides a semantic discovery layer.

This extends the structural-navigation capability established by the Code Pathfinder investigation.

### Important distinctions

GitNexus should not be described merely as a graph visualiser or search wrapper.

Its structural representation is produced through static analysis rather than being an LLM-generated repository memory.

Its Git integration should not be described as a comprehensive Git-history knowledge graph. The demonstrated capability concerns mapping repository state and changes onto structural repository knowledge.

### Demonstrated capability

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
* reuse across subsequent processes or sessions;
* incremental/staleness handling;
* Git-diff to structural-impact mapping;
* bounded MCP responses;
* discover → fetch workflows.

### Efficiency qualification

The investigation established the mechanism by which persistent structural and semantic retrieval could reduce exploratory model work.

It did **not** establish, for Orthoptera:

* lower cumulative input tokens;
* lower cumulative output tokens;
* lower cached-token usage;
* lower context occupancy;
* fewer model turns;
* lower AI credits;
* lower monetary cost;
* or better correctness per unit of cost.

Those remain empirical questions.

### Relationship to Code Pathfinder

Code Pathfinder established structural repository navigation as a distinct capability beyond lexical filesystem/search tooling.

GitNexus confirms and extends that distinction through persistent repository representation and optional semantic/vector retrieval.

The resulting capability vocabulary is therefore:

> **persistent hybrid structural + semantic repository retrieval**

rather than simply "another structural code-search tool".

---

## Subsequent findings

[Existing historical findings retained unchanged, in chronological order.]

---

## Findings journal maintenance

New findings are appended to the bottom of this document.

Do not turn this journal into a periodically rewritten executive summary. If a later investigation changes the current interpretation, append the new finding and preserve the earlier one where it remains historically relevant.

If a finding is promoted into an architectural, methodological or workflow decision, record that decision separately in `TOOLCHAIN_DECISIONS.md`.

If a capability remains merely desirable rather than demonstrated or adopted, record it in `TOOLCHAIN_WISHLIST.md`.

