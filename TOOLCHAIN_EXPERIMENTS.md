# AI Toolchain Experiments

This document records experiments conducted while developing and evaluating the AI-assisted workflow used by Orthoptera.

It is a **research record**, not project architecture. Findings here do not automatically become requirements for the Orthoptera implementation.

The experiments are primarily concerned with:

* how different AI roles and tools behave in practice;
* how context and repository knowledge are supplied to coding agents;
* the cost of delegation and broad reconnaissance;
* how persistent knowledge affects subsequent work;
* and which tool capabilities might improve the workflow.

The project's durable architectural decisions remain in the main project documentation. Toolchain decisions are recorded separately in `TOOLCHAIN_DECISIONS.md`.

---

## Experimental constraints

The experiments operate under the following practical constraints:

* The preferred tooling should remain within the user's existing **zero-cost / established account tiers** where reasonably possible.
* Experiments should avoid modifying the Orthoptera repository unless modification is itself the subject of the experiment.
* Experiments should distinguish **observed behaviour** from assumptions about how an AI product works internally.
* Expensive or broad experiments should be isolated from normal development where possible.
* Findings should be captured while they are fresh rather than relying on conversational history as the permanent record.

---

## Initial two-tier workflow

The initial Orthoptera workflow established two complementary AI roles:

* **ChatGPT** as the architectural/research AI, responsible for reasoning about design, reviewing evidence, identifying unresolved decisions, and directing investigations.
* **Codex** as the implementation/local-workspace AI, responsible for repository inspection and implementation work where direct access to the local corpus or checkout is useful.

This separation was not intended to imply that either tool is inherently incapable of the other's tasks. It was a practical division based on capabilities, access to the local environment, and the desire to keep architectural reasoning separate from implementation activity.

The local acoustic-corpus investigation demonstrated both the usefulness and the cost of this arrangement: using Codex for a substantial ad hoc survey was operationally appropriate because it had direct access to the local corpus, but it consumed a significant amount of model context and token budget.

This led to a broader investigation of whether specialist roles and delegated agents could provide better isolation.

---

## Copilot reconnaissance experiments

### Repository reconnaissance

A Copilot CLI session was used to investigate the repository and report on the state of the production acoustic-event work.

The experiment deliberately asked the agent to:

* inspect the authoritative project documentation;
* compare the documentation with exploratory code and production stubs;
* distinguish explicit decisions from experimental evidence and unresolved questions;
* cite repository-relative paths;
* and avoid inventing architectural solutions.

The investigation was delegated to an `explore` agent.

### Result

The agent successfully established a useful distinction between:

* **decided** — explicitly established by project documentation;
* **experimentally demonstrated** — demonstrated by exploratory work;
* **unresolved** — not established by the repository and therefore unsafe for an implementation agent to infer.

The investigation also demonstrated that delegation can produce a useful implementation-oriented report without requiring the main agent to perform every repository inspection itself.

However, it was substantially more expensive than initially expected.

The explore agent made approximately 30 tool calls and consumed roughly 290,000 tokens according to the subsequent session diagnosis. The resulting material was sufficiently large that temporary-file handling and paging were required.

### Finding

Delegation is therefore **not equivalent to free context isolation**.

A specialist subagent has its own context and can keep exploratory material out of the main conversation, but it performs additional model work. Delegation can therefore trade main-context cleanliness for additional token and AI-credit consumption.

This is an experimentally observed workflow consideration, not a reason to avoid delegation.

---

## Copilot context and cost observations

The Copilot CLI provides several useful measurements.

### `/context`

The observed `/content`-style context display showed a breakdown along the lines of:

* system prompt;
* system tools;
* MCP tools;
* messages;
* free space;
* response buffer.

This establishes an important distinction between **current context occupancy** and cumulative model usage.

The exact `/content` command is not currently treated as a documented experimental interface; the more general observation is that Copilot exposes the composition of the active context.

### `/usage`

The session exposed cumulative usage, including AI credits and model activity.

A later `/session info` reported:

* 75.7 AI credits used;
* approximately 2.2 million cumulative tokens;
* approximately 1.7 million cached tokens;
* approximately 191.8k written/output tokens;
* approximately 10.5k reasoning tokens.

These figures demonstrate why a single "context size" figure must not be interpreted as total token consumption.

A context window is a **current working set**. Token usage is **cumulative across model calls**.

### AI credits

The session reported AI-credit usage independently of the context-window measurement.

The important experimental distinction is therefore:

> **Context size, cumulative token usage, cached-token usage and AI credits are different measurements.**

They should not be treated as interchangeable.

### `/limits`

The Copilot CLI provides an optional session AI-credit limit.

The experiment reported:

* actual usage: **75.7 AI credits**;
* suggested session limit: **112 AI credits**.

The limit is a soft cap, so a model call may exceed it before the next call is blocked.

This provides a useful mechanism for deliberately bounded future experiments.

### Finding

Future toolchain experiments that may consume substantial model resources should preferably have an explicit AI-credit limit.

---

## Caching and controlled experiments

The Copilot investigation established that model input can include cached material as well as newly processed input.

This matters because repeated context does not necessarily have the same cost as entirely new context.

The investigation also established that changing aspects of the model/tool configuration can affect cache behaviour.

For controlled experiments, the following should therefore normally remain fixed unless they are themselves the experimental variable:

* model;
* context tier;
* reasoning configuration;
* enabled tools;
* MCP servers.

Otherwise, cache effects can become confounding variables.

---

## Large tool output

Copilot's handling of large tool output provides another useful observation.

Large outputs may be written to temporary files with only a preview presented directly to the model. The complete output can subsequently be retrieved when required.

This means that:

> **The size of a tool's raw output is not necessarily the same as the amount of that output immediately occupying model context.**

Conversely, repeatedly reading large temporary artefacts can bring substantial material back into subsequent model context.

This is relevant to repository reconnaissance and other corpus-scale investigations.

---

## MCP reference implementation survey

A separate investigation examined the official MCP reference implementations repository:

https://github.com/modelcontextprotocol/servers

The investigation was treated as a **capability/reference survey**, not as a recommendation to adopt particular servers.

Several useful patterns were identified.

### Scoped filesystem access

The Filesystem reference implementation demonstrates explicit filesystem roots and separation between read-only and mutating operations.

The useful concept for Orthoptera is not the server itself, but the ability to constrain an agent's accessible workspace independently of its natural-language instructions.

### Bounded context retrieval

The Filesystem and Fetch implementations demonstrate deliberately small retrieval operations:

* search;
* directory inspection;
* metadata;
* head/tail retrieval;
* multiple-file retrieval;
* bounded web retrieval;
* resumable retrieval.

This provides concrete evidence for a useful principle:

> **Context acquisition can itself be decomposed into narrow, bounded operations.**

This is particularly relevant because broad repository reconnaissance has already proved expensive.

### Selective Git context

The Git reference implementation exposes status, diffs, history and revisions as structured queries.

This demonstrates that repository state can be obtained selectively rather than by repeatedly supplying broad repository context.

### Persistent, queryable knowledge

The Memory reference implementation demonstrates persistent entities, relations and atomic observations with selective retrieval.

This is interesting as a capability pattern, but does not establish that Orthoptera should adopt a knowledge graph or external memory system. Orthoptera's repository documentation remains the authoritative home for project knowledge.

### Resources, prompts and tools

The MCP reference implementations demonstrate a distinction between:

* prompts;
* resources;
* executable tools.

This is useful vocabulary for thinking about how an AI workflow can separate stable contextual material from operations.

### Discover then fetch

MCP resource links demonstrate that a tool can identify a potentially useful artefact without immediately embedding its complete contents into model context.

This is another concrete example of context acquisition being separated from context consumption.

### Long-running tasks

The reference implementations demonstrate an asynchronous task lifecycle for operations that do not need to complete synchronously with the initiating request.

This may be relevant to future specialist investigations but has not yet been shown to be useful to Orthoptera.

### Tool safety metadata

MCP tool annotations can describe properties such as read-only, destructive and idempotent behaviour.

This is potentially relevant to workflows in which some AI roles should be inspection-only while others may modify the repository.

---

## Structural versus lexical repository navigation

**Status:** Experiment justified; not yet an adoption decision.

Recent investigation of Code Pathfinder demonstrates a concrete **structural repository-navigation** capability: a local analysis layer can construct symbols, modules and program relationships such as callers/callees and expose compact structural queries to an AI agent. This provides a potential discovery layer above filesystem/`rg` navigation.

The relevant hypothesis for Orthoptera is:

> Structural repository navigation may reduce model-side repository exploration by allowing relationships to be established locally before source is retrieved.

This hypothesis must not be conflated with the capability itself. In particular, the existence of a structural index is **not evidence** of reduced context occupancy, cumulative tokens, cached tokens, AI credits or monetary cost.

A controlled experiment should compare representative repository-navigation tasks using:

**Control**

```text
agent
 ├── filesystem
 └── rg/shell
```

**Treatment**

```text
agent
 ├── filesystem
 ├── rg/shell
 └── structural repository navigation
```

Hold constant:

* model;
* reasoning/context configuration;
* task wording;
* repository revision;
* system prompt;
* ordinary tools.

Measure independently:

1. model turns;
2. tool calls;
3. cumulative input tokens;
4. cumulative output tokens;
5. cached tokens;
6. AI credits;
7. context occupancy where observable;
8. source volume retrieved;
9. local indexing time;
10. index/storage overhead;
11. query latency;
12. wall-clock time;
13. task correctness;
14. structural-navigation errors or incomplete relationships.

The experiment should test tasks for which structural relationships are actually relevant, such as caller discovery, dependency tracing and change-impact analysis.

The success criterion should not be "fewer tool calls". The useful result would be:

> **equal or better task correctness with lower total model-side work after accounting for local indexing/query cost.**

Code Pathfinder provides a demonstrated structural treatment condition. GitNexus should be assessed separately to determine whether it provides the same capability, a broader one, or a genuinely different semantic/Git-history capability.

**Key distinction:** structural navigation is the capability under test; token/AI-credit reduction is an outcome hypothesis.

## GitNexus — persistent hybrid repository retrieval

**Status:** Candidate experiment justified; not an adoption decision.

### Question

Does a persistent repository representation combining lexical, structural and optional semantic retrieval reduce the amount of model-side repository exploration required for representative Orthoptera tasks?

### Evidence motivating the experiment

The GitNexus investigation found demonstrated support for:

* AST-derived structural repository analysis;
* symbol, reference, call and dependency relationships;
* process and impact representations;
* lexical/full-text retrieval;
* optional embeddings and vector retrieval;
* hybrid lexical/vector retrieval;
* persistent on-disk repository indexing;
* reuse across subsequent processes/sessions;
* incremental/staleness handling;
* Git-diff to structural-impact mapping;
* bounded MCP responses;
* discover → fetch workflows in which structural/search results can be returned without source content by default.

These observations establish that the treatment condition is a real capability rather than a hypothetical architecture.

They do **not** establish that the capability improves Orthoptera's AI workflow.

### Hypothesis

For repository-navigation tasks, persistent structural and semantic retrieval may reduce:

* exploratory model turns;
* source that must be retrieved and inspected;
* cumulative model context;
* cumulative model-side tokens;
* or AI cost.

These are outcome hypotheses, not established properties of GitNexus.

### Control

Use the existing repository-access pattern:

```text
agent
 ├── filesystem
 ├── shell
 └── lexical search
```

### Treatment

Add the candidate repository-index/retrieval layer:

```text
agent
 ├── filesystem
 ├── shell
 ├── lexical search
 └── persistent structural + semantic retrieval
```

Keep the model, task wording, repository revision, ordinary filesystem access and other relevant conditions fixed.

### Initial tasks

Use a small set of representative tasks covering different capability levels.

1. **Structural discovery**

   Locate a symbol and identify its callers/callees or relevant dependency relationships.

2. **Semantic discovery**

   Given a natural-language description of an Orthoptera subsystem or behaviour, identify the relevant implementation symbols/files.

3. **Persistent reuse**

   Repeat a suitable discovery task after restarting the retrieval service/process, testing whether the existing repository representation provides practical reuse rather than requiring reconstruction.

4. **Optional Git-impact task**

   Given a controlled change to a known symbol, identify affected symbols/processes using repository/Git-aware structural analysis.

### Measurements

Record independently:

1. model turns;
2. tool calls;
3. cumulative input tokens;
4. cumulative output tokens;
5. cached tokens;
6. AI credits;
7. observable context occupancy;
8. source volume retrieved;
9. local indexing time;
10. index size;
11. retrieval/query latency;
12. wall-clock time;
13. task correctness;
14. retrieval or graph errors;
15. index-staleness/update behaviour.

Indexing and local retrieval costs must be included in the comparison.

Do not use tool-call count alone as the success criterion.

The relevant comparison is approximately:

```text
local indexing/update cost
+
retrieval cost
+
model work
```

versus:

```text
ordinary repository exploration
+
model work
```

### Interpretation

A positive result requires more than a short individual retrieval response.

The strongest evidence would be:

> equivalent or better task correctness with lower total model-side work, after accounting for indexing and retrieval overhead.

A result showing only that the retrieval tool can return compact results should be recorded as a **capability observation**, not as evidence of token or cost savings.

### Relationship to the structural-navigation experiment

The earlier Code Pathfinder investigation established **structural repository navigation** as a distinct Level-2 capability.

GitNexus provides that capability plus persistent repository representation and optional semantic/vector retrieval.

The experiments should therefore distinguish:

```text
lexical navigation
        ↓
structural navigation
        ↓
semantic retrieval
        ↓
persistent reuse
```

rather than treating all repository intelligence as one capability.

### Current conclusion

The experiment is justified because the candidate demonstrably supplies capabilities not present in the filesystem/shell baseline.

No adoption decision follows from this experiment proposal.


## Current experimental conclusions

The experiments so far support the following conclusions:

1. **AI delegation can isolate exploratory context, but it is not free.**
2. **Broad repository reconnaissance can consume substantial model resources.**
3. **Current context occupancy and cumulative token usage are different measurements.**
4. **Cached context can materially affect the relationship between token counts and cost.**
5. **AI-credit limits are useful for bounding expensive experiments.**
6. **Tool output is an important contributor to context growth.**
7. **MCP provides several established patterns for scoped and incremental context acquisition.**
8. **Persistent knowledge need not be replayed wholesale as conversational history; it can be selectively retrieved.**
9. **The MCP reference implementations are more valuable to Orthoptera as a catalogue of capability patterns than as components to adopt wholesale.**
10. **Experimental findings should be captured separately from project architecture so that toolchain experimentation does not pollute the main design record.**

---

## Open experimental questions

The following remain subjects for future investigation:

* How much does delegation reduce the effective context burden on the main agent in practice?
* How much additional AI-credit cost does delegation introduce for different classes of task?
* What is the practical relationship between MCP tool definitions and context usage?
* Which forms of bounded repository retrieval provide the best cost/quality trade-off?
* Can specialist agents be given sufficiently narrow context without losing important project constraints?
* Which MCP capabilities would provide enough benefit to justify introducing additional tooling?
* How much durable knowledge should be supplied through repository documentation versus other selectively retrievable mechanisms?
* Which of these capabilities are available within the user's existing account tiers and therefore compatible with the zero-cost constraint?

Future experiments should answer these questions with small, controlled tests rather than broad exploratory sessions wherever possible.


