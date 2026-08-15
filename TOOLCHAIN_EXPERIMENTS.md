# AI Toolchain Completed Experiments Journal

This document is the **historical journal of completed AI-toolchain investigations, experiments and their contemporary conclusions** for Orthoptera.

It is a research record, not project architecture and not the mutable sequence of work currently planned.

## Journal invariants

This journal is **append-only in its normal operation**.

An entry preserves the epistemic state produced by the work at the time it was recorded. That can include:

* purpose and provenance;
* observations and measurements;
* interpretation;
* limitations and negative findings;
* relationship to earlier investigations;
* contemporary conclusions;
* implications and speculative consequences;
* hypotheses;
* unresolved questions;
* and possible or proposed follow-up experiments.

Forward-looking material is therefore **not prohibited from this journal** when it records what a completed investigation caused us to think at that point.

A proposed experiment may subsequently also appear in `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md`. The two records have different purposes:

* this journal preserves the historical fact that an investigation suggested the experiment, together with its contemporary rationale and proposed form;
* `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md` represents the mutable current state and ordering of experiments that remain worth considering or running.

Removing, changing or reordering an experiment in the planned sequence does not alter the historical journal entry that originally suggested it.

Later investigations may qualify, supersede or contradict earlier interpretations. They do so through **later journal entries**. Earlier entries are not retrospectively rewritten to make them consistent with later knowledge.

Historical uncertainty is information. An unresolved question, hypothesis, limitation or mistaken contemporary interpretation remains part of the journal record when it helps explain how the investigation developed.

A capability demonstrated by a tool is not the same thing as a benefit demonstrated for Orthoptera. Where relevant, entries should retain the distinction between:

```text
capability
    ↓
observed mechanism
    ↓
experimental outcome
    ↓
measured benefit
```

---

## 1. Scope and purpose

Orthoptera is being developed with AI coding assistance. The work has involved several AI roles and different ways of dividing work between them.

The experiments documented here are intended to answer questions such as:

* How much context does an agent actually receive?
* What information persists within or between sessions?
* How do models and subagents affect cost and context usage?
* When is delegation useful, and when does it introduce unnecessary cost?
* Which repository information needs to be made explicit because an agent cannot safely be expected to recover it from context?
* How reproducible is an experiment when the AI tool has its own session history, caches, or persistent state?
* Which toolchain capabilities are useful but currently unavailable within the established zero-cost preference?

The investigations deliberately distinguish:

```text
capability
    ↓
observed mechanism
    ↓
experimental outcome
    ↓
measured benefit
```

The existence of a capability does not establish a benefit.

---

## 2. Initial AI workflow

The initial Orthoptera workflow used two principal AI roles:

1. **ChatGPT** for architectural reasoning, design discussion and higher-level analysis.
2. **Codex** for implementation work against the local repository and for work requiring direct access to local data.

This separation was established for practical reasons rather than because either system was considered inherently incapable of performing the other's tasks.

The toolchain experiments arose partly because this two-role arrangement exposed questions about:

* context availability;
* local repository access;
* model-resource consumption;
* delegation;
* specialist roles;
* and persistent knowledge.

---

## 3. Ad hoc local-corpus acoustic survey

The local-corpus acoustic survey was carried out using the implementation/local-data tier because the work required direct access to the local recording corpus.

This was operationally appropriate under the established workflow.

However, the work also demonstrated that the AI role which is most suitable operationally is not necessarily the one with the lowest model-resource consumption.

This became one of the motivations for investigating:

* specialist AI roles;
* delegation;
* bounded repository context;
* and alternative mechanisms for repository exploration.

The lesson was not that local implementation agents should be avoided for large surveys.

The relevant observation was:

> **Tool-role selection and model-cost optimisation are separate considerations and may sometimes conflict.**

---

## 4. Copilot CLI reconnaissance

A reconnaissance investigation was performed using GitHub Copilot CLI to understand the relationship between repository instructions, repository exploration, session context and delegated agents.

The investigation was deliberately concerned with **where observed repository knowledge came from**, rather than assuming that apparent memory had a single explanation.

The investigation considered several possible sources:

1. the current prompt;
2. current conversation context;
3. repository files;
4. tool/MCP results;
5. persistent session state;
6. delegated-agent state;
7. model-level or service-level memory.

No assumption was made that any one of these was responsible until evidence supported it.

### Delegated exploration

Part of the reconnaissance was delegated to an `explore` agent.

The delegated agent was instructed to:

* inspect the authoritative project documentation;
* compare the documentation with exploratory code and production stubs;
* distinguish explicit decisions from experimental evidence and unresolved questions;
* cite repository-relative paths;
* and avoid inventing architectural solutions.

### Result

The delegated agent successfully established a useful distinction between:

* **decided** — explicitly established by project documentation;
* **experimentally demonstrated** — demonstrated by exploratory work;
* **unresolved** — not established by the repository and therefore unsafe for an implementation agent to infer.

The investigation also demonstrated that delegation can produce a useful implementation-oriented report without requiring the main agent to perform every repository inspection itself.

However, it was substantially more expensive than initially expected.

The explore agent made approximately 30 tool calls and consumed roughly **290,000 tokens** according to the subsequent session diagnosis. The resulting material was sufficiently large that temporary-file handling and paging were required.

### Finding

Delegation is therefore **not equivalent to free context isolation**.

A specialist subagent has its own context and can keep exploratory material out of the main conversation, but it performs additional model work.

Delegation can therefore trade:

```text
less material in the parent context
```

for:

```text
additional model invocation
+ additional token consumption
+ additional AI-credit consumption
```

This is an experimentally observed workflow consideration, not a reason to avoid delegation.

---

## 5. Copilot context and cost observations

The Copilot CLI provides several useful measurements of model activity.

### `/context`

The observed context display showed a breakdown along the lines of:

* system prompt;
* system tools;
* MCP tools;
* messages;
* free space;
* response buffer.

This established an important distinction between **current context occupancy** and cumulative model usage.

The exact command/interface used during the investigation is not treated as a stable documented experimental interface. The durable observation is that the CLI exposes information about the composition of the active context.

### `/usage`

The session exposed cumulative usage, including AI credits and model activity.

A later `/session info` reported:

* **75.7 AI credits used**;
* approximately **2.2 million cumulative tokens**;
* approximately **1.7 million cached tokens**;
* approximately **191.8k written/output tokens**;
* approximately **10.5k reasoning tokens**.

These figures demonstrate why a single context-window figure must not be interpreted as total model consumption.

A context window is a **current working set**.

Token usage is **cumulative across model calls**.

### AI credits

The session reported AI-credit usage independently of context-window occupancy.

The important experimental distinction is:

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

## 6. Caching and controlled experiments

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

The practical lesson is:

> A token count alone does not fully describe the cost or experimental condition of a model interaction.

---

## 7. Large tool output

Copilot's handling of large tool output provides another useful observation.

Large outputs may be written to temporary files with only a preview presented directly to the model. The complete output can subsequently be retrieved when required.

This means:

> **The size of a tool's raw output is not necessarily the same as the amount of that output immediately occupying model context.**

Conversely, repeatedly reading large temporary artefacts can bring substantial material back into subsequent model context.

This is relevant to repository reconnaissance and other corpus-scale investigations.

It also means that:

```text
tool output size
```

and:

```text
model context growth
```

should not automatically be treated as identical quantities.

---

## 8. Copilot session state and persistence

The investigation found several forms of state associated with Copilot sessions.

These included:

* conversation context;
* session state;
* checkpoints/compaction;
* repository state;
* MCP/tool state;
* model/cache state;
* CLI command history.

The existence of these different forms of state means that the phrase **"fresh session"** is ambiguous unless the relevant state is controlled.

### Session-state artefacts

The investigation observed session-state files associated with the Copilot session.

These demonstrated that information can be persisted outside the immediately visible conversation.

However:

> **The existence of session-state files is not sufficient evidence that the model has memory of their contents.**

The file's existence establishes persistence of an artefact, not its causal role in a subsequent model response.

### Checkpoints and compaction

The checkpoint mechanism preserved a substantial summary of:

* work already performed;
* files created;
* repository inspection results;
* established design facts;
* unresolved questions;
* technical details;
* suggested continuation information.

### Established observation

Conversation compaction does not necessarily mean that all useful session information is simply lost.

Copilot can create a checkpoint containing a summary of preceding work.

### Not established

The investigation did not establish:

* exactly how checkpoint contents are incorporated into subsequent model context;
* whether the original messages remain accessible to the model;
* how much information is lost during compaction;
* whether compaction behaviour differs between models.

---

## 9. Warm versus fresh sessions

A new visible prompt within an existing session should not automatically be assumed to be equivalent to a fresh run.

A warm session may retain:

* conversation context;
* summaries/checkpoints;
* session state;
* repository-derived context;
* tool configuration;
* or other persistent state.

A fresh process may remove some of these while leaving others intact.

This makes "freshness" an experimental condition rather than merely a user-interface operation.

A controlled comparison may therefore need to distinguish at least:

1. same session, repeated task;
2. fresh CLI session, same repository;
3. fresh session with session-state artefacts removed;
4. fresh session with controlled model/tool configuration;
5. fresh session with persistent memory disabled where applicable.

The purpose is to identify which state is responsible for any observed change in behaviour.

---

## 10. Model reproducibility

The active model may change or may be selected by a mechanism not fully exposed to the experiment.

Consequently, reproducing an experiment may require recording the model actually used rather than merely recording the prompt.

The investigation did not establish:

* whether model selection is fixed for a session;
* whether delegated agents independently select models;
* whether automatic selection can change models during a task;
* whether model changes affect retained context;
* or whether model changes explain observed repository results.

Model configuration should therefore be treated as an experimental variable unless deliberately held constant.

---

## 11. Delegation reproducibility

Delegated agents have their own execution and potentially their own model/context.

Delegation should therefore be treated as an experimental variable.

Relevant questions include:

* What context does an explore agent receive?
* Does it independently load `AGENTS.md` and other repository instructions?
* Does it inherit conversation history?
* Does it inherit session-state?
* Can delegation reduce the context burden on the parent agent, or does it primarily add another model invocation?

The completed reconnaissance experiment established the cost side of this question but did not fully isolate all of the context-sharing mechanisms.

---

## 12. Current working hypotheses

The following are **hypotheses to test, not established facts**.

### 12.1 AI-tool memory

Copilot appears to maintain information outside the immediate visible conversation because session logs, events and session-state files exist.

It is not yet known whether this should be described as "memory" in the model-facing sense.

### 12.2 Freshness of experiments

A new visible prompt within an existing session should not automatically be assumed to be equivalent to a fresh run.

There are potentially several distinct states involved:

* conversation history;
* session-state;
* checkpoints;
* repository state;
* MCP/tool state;
* model/cache state;
* CLI command history.

The degree to which each affects a model invocation remains to be established.

### 12.3 Model reproducibility

Because the active model may change, reproducing an experiment may require recording the model actually used rather than merely recording the prompt.

### 12.4 Delegation reproducibility

Because delegated agents have their own execution and potentially their own model/context, delegation should be treated as an experimental variable.

---

## 13. Experimental discipline emerging from the work

These are observations about what makes experiments more reliable, rather than requirements on Orthoptera itself.

For future toolchain experiments, record where available:

* tool and version;
* active model;
* session ID;
* repository revision;
* prompt;
* whether work was delegated;
* delegated model, if visible;
* context usage;
* AI-credit usage;
* token usage;
* relevant session-state artefacts;
* whether the run began from a fresh session;
* whether compaction occurred.

The purpose is to make it possible to distinguish a change in tool behaviour from a change in:

* prompt;
* repository state;
* model;
* accumulated context;
* caching;
* delegation;
* or persistent session state.

---

## 14. MCP reference implementation survey

A separate investigation examined the official MCP reference implementations repository:

`https://github.com/modelcontextprotocol/servers`

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

This is interesting as a capability pattern, but does not establish that Orthoptera should adopt a knowledge graph or external memory system.

Orthoptera's repository documentation remains the authoritative home for project knowledge.

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

MCP tool annotations can describe properties such as:

* read-only;
* destructive;
* idempotent.

This is potentially relevant to workflows in which some AI roles should be inspection-only while others may modify the repository.

---

## 15. Structural versus lexical repository navigation

**Status:** Experiment justified; not yet an adoption decision.

Recent investigation of Code Pathfinder demonstrates a concrete **structural repository-navigation** capability: a local analysis layer can construct symbols, modules and program relationships such as callers/callees and expose compact structural queries to an AI agent.

This provides a potential discovery layer above filesystem/`rg` navigation.

The relevant hypothesis for Orthoptera is:

> Structural repository navigation may reduce model-side repository exploration by allowing relationships to be established locally before source is retrieved.

This hypothesis must not be conflated with the capability itself.

In particular, the existence of a structural index is **not evidence** of:

* reduced context occupancy;
* reduced cumulative tokens;
* reduced cached tokens;
* reduced AI credits;
* reduced monetary cost.

### Control

```text
agent
 ├── filesystem
 └── rg/shell
```

### Treatment

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

The experiment should test tasks for which structural relationships are actually relevant, such as:

* caller discovery;
* dependency tracing;
* change-impact analysis.

The success criterion should not be "fewer tool calls".

The useful result would be:

> **equal or better task correctness with lower total model-side work after accounting for local indexing/query cost.**

Code Pathfinder provides a demonstrated structural treatment condition.

GitNexus should be assessed separately to determine whether it provides the same capability, a broader one, or a genuinely different semantic/Git-history capability.

---

## 16. GitNexus — persistent hybrid repository retrieval

**Status:** Candidate experiment justified; not an adoption decision.

### Candidate identity

The investigation concerned upstream **`abhigyanpatwari/GitNexus`**, branch `main`.

The latest identifiable stable release during the investigation was **1.6.9**, dated **4 July 2026**.

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

> **equivalent or better task correctness with lower total model-side work, after accounting for indexing and retrieval overhead.**

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

### Historical conclusion

The experiment was justified because the candidate demonstrably supplied capabilities not present in the filesystem/shell baseline.

No adoption decision followed from the experiment proposal.

---

## 17. Current experimental conclusions

The experiments so far support the following conclusions:

1. **AI delegation can isolate exploratory context, but it is not free.**
2. **Broad repository reconnaissance can consume substantial model resources.**
3. **Current context occupancy and cumulative token usage are different measurements.**
4. **Cached context can materially affect the relationship between token counts and cost.**
5. **AI-credit limits are useful for bounding expensive experiments.**
6. **Tool output is an important contributor to context growth, but raw output size and immediate context occupancy are not necessarily identical.**
7. **MCP provides several established patterns for scoped and incremental context acquisition.**
8. **Persistent knowledge need not be replayed wholesale as conversational history; it can be selectively retrieved.**
9. **The MCP reference implementations are more valuable to Orthoptera as a catalogue of capability patterns than as components to adopt wholesale.**
10. **Structural repository navigation is a distinct capability from lexical repository navigation.**
11. **Persistent structural/semantic repository retrieval is a distinct capability from lexical navigation alone, but its task-level benefit remains to be measured.**
12. **Experimental findings should be captured separately from project architecture so that toolchain experimentation does not pollute the main design record.**

---

## 18. Open experimental questions

The following questions remained open at this stage of the investigation:

### Context and memory

* What information from previous turns is actually supplied to each model call?
* What information survives compaction?
* What information survives `/clear`?
* What information survives `/new`?
* What information survives starting a completely new CLI process?
* What information is obtained from session-state?
* What information is obtained from repository files?
* What MCP information is persistent, and what is reconstructed per invocation?

### Models

* Under what circumstances does Copilot switch models?
* Is model selection deterministic?
* Does delegation use the same model-selection mechanism as the parent session?
* Does model selection affect AI-credit consumption?

### Cost

* How are AI credits calculated?
* How do cached tokens affect AI-credit usage?
* How do reasoning tokens affect it?
* How much of the cost of a delegated task comes from tool output versus model reasoning?
* How useful are `/limits predict` recommendations for Orthoptera's particular workloads?

### Delegation

* What context does an explore agent receive?
* Does it independently load `AGENTS.md` and other repository instructions?
* Does it inherit conversation history?
* Does it inherit session-state?
* Can delegation reduce the context burden on the parent agent, or does it primarily add another model invocation?

### Reproducibility

* What constitutes a genuinely fresh Copilot experiment?
* Is `/new` sufficient?
* Is `/clear` sufficient?
* Does a fresh process behave differently?
* Does the repository itself need to be reset?
* Should model, context and session state be treated as experimental controls?

---

## 19. Relationship to other project documentation

This document records **what we discover about the toolchain**.

It does not define how Orthoptera should be architected or how contributors should work.

The eventual workflow and guardrails for working with AI coding agents belong in the project's normal contributor/agent documentation, principally:

* `CONTRIBUTING.md`;
* `AGENTS.md`.

Decisions about the toolchain itself belong in:

* `TOOLCHAIN_DECISIONS.md`.

Useful capabilities that are identified but not currently adopted belong in:

* `TOOLCHAIN_WISHLIST.md`.

This separation is intentional:

```text
experiments
    ↓
what was observed / measured / investigated

findings
    ↓
durable capability understanding

decisions
    ↓
what the project has chosen

wishlist
    ↓
capabilities worth considering

CONTRIBUTING / AGENTS
    ↓
resulting operational practice
```

These records are complementary rather than interchangeable.

---

## 20. Status

This document is an experimental record, not a specification.

Where a statement is explicitly described as an observation, it should be treated as evidence from the experiments described here.

Where behaviour is described as unresolved, inferred or hypothetical, it should not be promoted into project policy without further evidence or an explicit decision.

Historical experiment material is retained because later investigations may change the interpretation of an earlier observation without making that observation itself worthless.
---

## Recovery entry — focused MCP Filesystem and Tier-1 file-search investigations

**Investigation date:** 9 August 2026
**Recovered into journal:** 15 August 2026
**Primary implementation:** official MCP Filesystem reference server, `modelcontextprotocol/servers`, `src/filesystem`
**Related source:** CoreStory article on MCP servers for codebase context, specifically its Tier-1 file-search capability

This recovery entry preserves two focused investigations carried out after the broader MCP reference-implementation survey:

1. a source-first investigation of the official MCP Filesystem reference server as a capability/reference implementation;
2. a follow-up investigation of the CoreStory article's Tier-1 "file search" category, traced to the official Filesystem implementation rather than treating the article itself as implementation evidence.

The investigations did **not** establish that the Filesystem server should be adopted by Orthoptera. Their value was to make several earlier MCP conclusions more precise.

### Scoped filesystem access and dynamic Roots

The Filesystem implementation maintains an explicit allowed-directory set and validates filesystem operations against it, including normalised paths and resolved symlink targets.

This demonstrates a stronger mechanism than merely instructing an agent to inspect only selected directories:

> **The workspace exposed by a tool can be constrained mechanically, independently of the agent's natural-language instructions.**

MCP Roots can also supply and subsequently change the roots exposed to the server during a session. This demonstrates **dynamic/runtime scope selection**.

Important qualifications:

* MCP Roots communicate scope; the server must enforce it.
* Roots are not themselves an operating-system sandbox.
* In the reference implementation, client-provided Roots replace the CLI-configured allowed-directory set rather than necessarily being intersected with it.
* The appropriate scope-composition semantics for an Orthoptera specialist workflow remain unresolved.
* Restricting the available search space does not by itself demonstrate lower model-token or AI-credit consumption.

The useful distinction is between **declared scope**, **tool-enforced scope**, and **environment-enforced authority**.

### Tool safety annotations are metadata, not authority

The Filesystem server annotates tools with MCP safety metadata such as `readOnlyHint`, `destructiveHint` and `idempotentHint`.

The investigation established three distinct layers:

```text
machine-readable tool semantics
        ↓
client/workflow policy
        ↓
technical enforcement
```

A read-only annotation can describe a tool to a client. A client may use that metadata when constructing a role or confirmation policy. Neither fact proves that the underlying process is technically unable to modify the workspace.

Actual read-only authority requires an enforcement mechanism such as filesystem permissions, a read-only mount, a restricted server surface, or another environment-level boundary.

The useful Orthoptera capability is therefore **machine-readable safety/behaviour metadata**, not the stronger claim that MCP annotations make an agent safe.

### Discovery and retrieval are separate operations

The implementation exposes separate operations for directory listing, recursive tree discovery, file/path search, metadata inspection, file reading and multi-file reading.

`search_files` returns matching paths rather than file contents.

This establishes a progressive-disclosure pattern:

```text
scope
  ↓
discover structure / candidate paths
  ↓
inspect metadata where useful
  ↓
select
  ↓
retrieve content
```

For Orthoptera, the important mechanism is:

> **Make orientation and selection cheap, then make source retrieval an explicit subsequent step.**

This is a more precise formulation of bounded/progressive repository retrieval than merely instructing an agent to read less.

### "Bounded retrieval" is not necessarily hard-bounded context

The implementation supports `head` and `tail` line-limited reads, which are useful progressive-inspection primitives.

However:

* the limit is expressed in lines rather than bytes or model tokens;
* a single very long line can still return a large payload;
* full-file reads remain available;
* multi-file retrieval has no demonstrated aggregate output ceiling;
* recursive directory trees and path searches can themselves return large result sets.

The implementation's internal I/O chunk size is not a model-context limit.

Therefore:

> **Retrieval can be semantically bounded without model context being hard-bounded.**

### Batching and orientation operations can themselves create large outputs

`read_multiple_files` can deliberately retrieve a coherent group such as an implementation, test and relevant documentation in one call.

This may reduce tool-call overhead, but the implementation does not demonstrate a maximum file count or combined output size. Batching can therefore create a large context payload.

Likewise, shallow directory listings, file metadata and recursive trees allow orientation without reading source, but a recursive tree is not inherently small and has no demonstrated general depth or output-size bound.

These are useful retrieval primitives, not demonstrated token-saving mechanisms.

### Tier-1 "file search" is path discovery, not semantic or content search

The CoreStory follow-up investigation traced the article's Tier-1 capability to the official Filesystem implementation.

`search_files` is fundamentally a **path/glob search**. It does not provide:

* repository-content search comparable to `rg`;
* embeddings or vector retrieval;
* AST-aware search;
* semantic ranking;
* natural-language relevance;
* persistent code intelligence.

Ordinary shell tools such as `find`, `rg`, directory listings and Git/GitHub search can provide the same broad class of lexical/path discovery, and often stronger content search.

The useful MCP distinction is therefore not:

> MCP supplies a better search engine.

It is:

> **MCP supplies a constrained, explicit, agent-callable interface to filesystem discovery and retrieval primitives.**

For an agent that already has competent shell access, no evidence was found that the MCP Filesystem search itself is intrinsically more capable or more efficient.

### No persistent index or repeated-scan solution

The Filesystem server performs filesystem traversal when searching. The investigation found no persistent content index, AST index, embedding/vector index, repository graph or cross-session repository knowledge.

It therefore does **not** solve the repeated-repository-scanning problem.

A host or client may cache results, but that would be a host/client capability rather than one demonstrated by this server.

### Context/token/cost conclusion

Taken together, the focused investigations refined Tier 1 into:

```text
explicit scope
      ↓
discover paths / structure
      ↓
select candidates
      ↓
retrieve selected content
```

This is a useful **context-acquisition discipline**. It should not be conflated with semantic repository retrieval or persistent structural code intelligence.

The mechanism makes lower model-side context consumption plausible when it prevents irrelevant source from being retrieved.

No apples-to-apples evidence was found establishing that the MCP Filesystem workflow produces, relative to disciplined shell/filesystem use:

* fewer cumulative input tokens;
* fewer cached tokens;
* fewer output tokens;
* fewer model turns;
* lower AI credits;
* lower monetary cost;
* or better task correctness.

The appropriate conclusion was:

> **Context-disciplined retrieval mechanism demonstrated; token/cost benefit not demonstrated.**

### Relationship to the earlier MCP survey

The broad MCP reference survey remains valid, but these focused investigations add important qualifications:

1. scoped access can be dynamic at runtime through Roots, but scope-composition semantics are implementation-specific;
2. safety annotations are advisory metadata, not technical authority;
3. bounded retrieval is not necessarily hard-bounded model context;
4. search-first retrieval can avoid unnecessary source reads, but `search_files` searches paths rather than source content;
5. multi-file and recursive-tree operations can themselves produce large outputs;
6. Tier-1 Filesystem MCP does not provide persistent indexing or semantic repository understanding;
7. MCP's value here is principally the constrained agent-tool interface and retrieval workflow, not superior search intelligence.

### Contemporary implications

The focused investigations did not justify a new top-level experiment on the Filesystem server itself.

They strengthened existing capability ideas around scoped access, possible dynamic/runtime scope selection, discover-then-fetch retrieval, progressive inspection, specialist tool/workspace boundaries and machine-readable safety metadata.

They also established that future context-efficiency claims must measure downstream model behaviour rather than infer savings from small individual tool responses.

### Provenance

Primary implementation reference:

`https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem`

Related article investigated:

`https://corestory.ai/post/mcp-servers-codebase-context-ai-coding-agents`

The article motivated the Tier taxonomy; implementation claims were checked against the official Filesystem server rather than accepted from the article alone.
