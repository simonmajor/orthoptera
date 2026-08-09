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

