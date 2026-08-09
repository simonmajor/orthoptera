## Structural repository navigation is a distinct toolchain capability

**Finding:** Repository navigation should be distinguished into at least three levels:

1. **Lexical navigation** — filesystem paths, filename discovery, text search and source retrieval.
2. **Structural navigation** — AST/static-analysis-derived symbols and relationships such as definitions, callers/callees, imports, dependencies and source locations.
3. **Semantic retrieval** — task-aware relevance selection, potentially using embeddings, vector search, LLM-generated representations or other semantic retrieval mechanisms.

A fourth, orthogonal capability is **persistent repository knowledge**: retaining a reusable repository representation across processes or AI sessions and updating it as the repository changes.

Recent investigation of Code Pathfinder demonstrates that structural navigation can be implemented as a local analysis/indexing layer and exposed through compact MCP queries. This can support a **discover → fetch** workflow in which an agent establishes relevant structural relationships before retrieving source.

This is materially different from both ordinary filesystem/`rg` search and embedding/vector semantic retrieval.

No evidence from the investigation establishes that structural navigation by itself reduces model context, cumulative tokens, cached tokens, AI credits or monetary cost. Those are empirical outcomes requiring controlled measurement.

**Implication:** Orthoptera should treat structural repository navigation as an independent toolchain capability rather than subsuming it under "semantic search" or "repository retrieval".

## GitNexus — persistent hybrid repository retrieval

**Investigation date:** 9 August 2026
**Candidate:** upstream `abhigyanpatwari/GitNexus`, `main`
**Latest identifiable stable release:** 1.6.9, 4 July 2026

### Finding

GitNexus is a local repository-analysis and retrieval system that combines four capabilities relevant to the Orthoptera toolchain:

1. lexical navigation;
2. structural repository navigation;
3. optional semantic/vector retrieval;
4. persistent repository knowledge.

Its core repository representation is constructed through static analysis and stored persistently in a local graph database. The system can expose structural relationships such as symbols, calls, imports, dependencies, inheritance, processes and impact relationships. Optional embedding/vector retrieval adds a semantic discovery layer over the repository representation.

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

The persistence dimension is orthogonal to the three retrieval levels: a repository can have lexical, structural or semantic indexes without necessarily retaining them across sessions. GitNexus demonstrably combines persistence with the higher-level retrieval capabilities.

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

GitNexus should not be described as merely a graph visualiser or search wrapper.

It should also not be described as an LLM-generated repository memory system. Its core structural representation is produced by static analysis and can be queried without an LLM. Semantic retrieval uses embeddings, but that is distinct from LLM reasoning about the repository.

Its Git integration should not be described as a comprehensive Git-history knowledge graph. The demonstrated Git capability is primarily the mapping of current repository state and changes onto structural repository knowledge.

### Discover → fetch

GitNexus supports a useful progressive-retrieval pattern:

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

This is relevant to Orthoptera's bounded-retrieval objective because discovery need not immediately return large amounts of source.

Ordinary filesystem access remains useful for arbitrary file and line-range retrieval.

### Persistence

The repository representation is stored locally and can be reused after the original indexing process and across subsequent MCP processes/sessions. The implementation also contains mechanisms for detecting stale repository state and updating the index.

This is materially different from an in-memory structural-analysis server that reconstructs its graph at startup.

### Efficiency claims

The investigation demonstrates the **mechanism** by which GitNexus could reduce exploratory model work: precomputed relationships and semantic retrieval can identify relevant repository material before the model reads large amounts of source.

It does **not** demonstrate, for Orthoptera:

* lower cumulative input tokens;
* lower cumulative output tokens;
* lower cached-token usage;
* lower context occupancy;
* fewer model turns;
* lower AI credits;
* lower monetary cost;
* better correctness per unit of cost.

Those remain empirical questions.

Product-level token-efficiency claims should therefore not be recorded as Orthoptera findings.

### Relationship to Code Pathfinder

Code Pathfinder established that structural repository navigation is a distinct capability beyond lexical filesystem/search tooling.

GitNexus confirms and extends that distinction.

Both provide Level-2 structural analysis, but GitNexus additionally demonstrates:

* persistent repository representation;
* optional semantic/vector retrieval;
* hybrid lexical/semantic ranking;
* integrated structural + semantic discovery;
* persistent reuse and update handling.

The significant new capability for Orthoptera is therefore:

> **persistent hybrid structural + semantic repository retrieval**

rather than "another structural code-search tool".

### Orthoptera implication

The capability is sufficiently demonstrated to justify a small controlled experiment comparing ordinary lexical repository exploration with persistent structural/semantic retrieval.

No toolchain adoption decision is justified by the investigation alone.

The appropriate durable conclusion is:

> GitNexus demonstrates a persistent repository knowledge layer combining static structural analysis with optional semantic/vector retrieval. This is a distinct capability from both lexical search and structural navigation alone. Its potential to reduce model context, tokens or AI cost for Orthoptera remains an empirical hypothesis.

