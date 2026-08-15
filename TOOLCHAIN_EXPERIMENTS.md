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

---

## Recovery entry — KiroGraph investigation

**Investigation date:** 9 August 2026
**Recovered into journal:** 15 August 2026
**Candidate:** `davide-desio-eleva/kirograph`
**Upstream examined:** `main`
**Stable release independently identified during the investigation:** `v0.28.1`, published 3 July 2026

This investigation examined KiroGraph source-first against the capability baseline established by the preceding MCP Filesystem, Code Pathfinder and GitNexus investigations.

The important result was that KiroGraph substantially overlaps with GitNexus in repository indexing and retrieval, but extends the investigated capability model into a broader form of **persistent agent/project knowledge**.

The investigation therefore changed the meaning of "persistent repository knowledge" in the developing Orthoptera toolchain vocabulary.

### Implementation character

Current KiroGraph was found to be a local TypeScript MCP server built around a persistent SQLite repository graph with optional vector retrieval and a broad set of surrounding modules.

The source tree contained dedicated facilities for areas including:

* architecture analysis;
* compression;
* context construction;
* data indexing;
* documentation;
* graph storage and traversal;
* memory;
* patterns;
* reference resolution;
* search;
* security;
* synchronisation;
* vectors;
* wiki/project knowledge.

The public API constructed components including a graph database, reference resolver, vector manager, context builder, architecture analyser, indexing pipeline and searcher directly.

This established that KiroGraph was not merely an MCP wrapper around an external search service.

### Structural repository representation

KiroGraph uses Tree-sitter parsing and constructs a persistent structural repository representation.

Demonstrated graph concepts included:

* functions;
* methods;
* classes;
* interfaces;
* types and enums;
* variables and constants;
* modules;
* imports and exports;
* calls;
* references;
* inheritance and implementation relationships;
* instantiation;
* overrides;
* decorators;
* type relationships;
* return relationships.

It also exposes higher-level derived representations including packages, architecture/layer information, graph snapshots, communities and hotspots.

This places KiroGraph clearly within the previously established **structural repository-navigation** capability class.

However, no evidence sufficient to establish a general program-dependence graph, complete control-flow model or general inter-procedural taint/data-flow system was found.

### Structural MCP navigation

The investigated MCP surface included structural operations for concepts such as:

* search;
* context construction;
* callers;
* callees;
* impact;
* node details;
* files;
* paths;
* type hierarchy;
* module API;
* rename preview;
* flows;
* communities;
* architecture/package analysis;
* dead-code and circular-dependency analysis;
* hotspots and surprising relationships;
* snapshots and differences.

The structural query schemas provided bounded caller/callee and impact operations and different source/detail levels.

The conclusion was therefore:

> **KiroGraph demonstrably provides Level-2 structural repository navigation.**

This capability itself was not novel after Code Pathfinder and GitNexus.

### Semantic retrieval

KiroGraph also demonstrated optional semantic/vector retrieval.

Its context-building path combined:

1. symbol-token extraction;
2. exact-name lookup;
3. semantic/vector search;
4. full-text search;
5. deduplication;
6. import resolution;
7. result trimming to a configured node limit.

Multiple vector implementations/backends were present.

This established:

> **Hybrid exact + semantic + lexical retrieval is implemented.**

An important qualification was retained: the implementation examined did not establish GitNexus-style BM25/vector Reciprocal Rank Fusion specifically. Exact, semantic and full-text results were combined and prioritised, but the stronger RRF claim was not demonstrated.

Semantic retrieval therefore places KiroGraph in the Level-3 capability class already established by GitNexus rather than introducing a new retrieval primitive.

### Persistent repository representation

KiroGraph stores normal project state under:

```text
.kirograph/
```

including a SQLite graph database.

The API can initialise a project and subsequently reopen that persisted representation.

This demonstrated reuse beyond a single query or MCP process:

> **Persistent repository representation: demonstrated.**

The investigation also found synchronisation/staleness operations including full indexing, synchronisation, dirty-state checks and pending-sync information.

Git changes could be used when determining whether the representation required synchronisation, with filesystem comparison as a fallback.

This supported:

* persistent graph reuse;
* incremental synchronisation;
* dirty/stale-state detection;
* Git-aware change detection.

It did not establish that KiroGraph has exactly the same branch-aware index semantics as GitNexus.

### Discover → inspect → fetch

KiroGraph showed a particularly explicit progressive-retrieval interface.

The investigated division was approximately:

```text
kirograph_search
    ↓
locations / discovery

kirograph_node
    ↓
symbol details
    ↓
optional source

kirograph_context
    ↓
task-oriented selection
    ↓
bounded related code
```

The search operation could return locations without source, while node/context operations provided progressively richer detail.

File-oriented operations also exposed several read modes rather than forcing every retrieval to return an entire file.

This reinforced the existing Orthoptera capability pattern:

> **discover → inspect → fetch**

and demonstrated that structural and semantic discovery can be used before source retrieval.

As with earlier tools, this mechanism did **not** demonstrate a hard bound on downstream model context or total token consumption.

### Context/cache mechanisms

KiroGraph also contained explicit mechanisms aimed at controlling repeated context.

One investigated feature cached unchanged file reads and could return a compact marker instead of repeating unchanged content immediately, with a separate retrieval operation for cached content.

The project described this in terms of reducing repeated context and improving stable-prefix/KV-cache behaviour.

The mechanism was real enough to be experimentally interesting, but the claimed downstream economics were not treated as established:

> **cache/context mechanism demonstrated; model-token or AI-credit consequence not demonstrated for Orthoptera.**

The investigation also noted a countervailing cost: enabling a large MCP tool surface itself consumes model context through tool definitions.

A separate microexperiment on this cache/read mechanism was considered potentially useful but secondary to the more important persistent-knowledge question.

### Persistent project/agent knowledge

The most important KiroGraph finding was its optional persistent-memory layer.

The implementation/documentation exposed project-memory concepts including:

* cross-session observations;
* decisions;
* errors;
* patterns;
* links between memory and code symbols;
* typed relations such as supersession, conflict and compatibility;
* stale/review mechanisms;
* conflict handling;
* prompt/session-context reconstruction.

This is materially different from merely persisting a source-derived graph.

The distinction developed during the investigation was:

```text
source
  ↓
persistent graph/index
```

versus:

```text
agent/project experience
  ↓
persistent observations / decisions / knowledge
  ↓
future retrieval
```

KiroGraph therefore supplied a concrete implementation of **persistent agent-generated project knowledge**.

### Wiki/project knowledge

KiroGraph also contained an opt-in wiki/project-knowledge mechanism supporting persistent Markdown knowledge pages and related maintenance/retrieval operations.

This provided another form of persistent project knowledge distinct from both the structural graph and episodic memory.

The investigation therefore distinguished:

* persistent source-derived structural representation;
* persistent semantic/vector representation;
* persistent agent/project knowledge;
* persistent declarative/wiki knowledge.

### Refined persistent-knowledge vocabulary

The KiroGraph investigation motivated a more precise decomposition of what had previously been called "persistent repository knowledge":

```text
Level 4A — persistent structural representation
           source-derived graph/index survives sessions

Level 4B — persistent semantic representation
           semantic/vector search representation survives sessions

Level 4C — persistent project/agent knowledge
           agent- or human-generated project knowledge survives
           independently of reconstructing it from source
```

KiroGraph demonstrably supplied examples of all three.

The genuinely interesting addition beyond the established GitNexus baseline was **Level 4C**.

### KiroGraph versus GitNexus

The investigation concluded that KiroGraph did **not** materially establish a new primitive in:

* structural graph navigation;
* persistent source-derived repository indexing;
* semantic/vector retrieval;
* incremental repository synchronisation;
* bounded discovery/context selection.

GitNexus had already established that capability envelope.

KiroGraph's important extension was:

> **persistent agent/project knowledge associated with the repository and reusable across sessions.**

This changed the next useful experimental question from:

> Is another persistent structural/semantic code graph useful?

to:

> **Can durable agent/project knowledge be more useful or cheaper to retrieve than rediscovering the same knowledge from the repository in every session?**

### Python relevance and structural limitations

Python was supported by the Tree-sitter layer and structural graph.

However:

> **Python parser support was not treated as evidence of complete Python semantic understanding.**

The investigation did not establish language-server-grade type inference, complete dynamic call resolution or complete graph coverage for Python.

Likewise, implementation of vector search did not establish superior retrieval quality.

Graph existence and retrieval implementation were treated as capabilities requiring later empirical validation, not as evidence of correctness or task benefit.

### Local computation and resource implications

Core repository parsing, graph construction and SQLite persistence operate locally.

Optional semantic and local-synthesis facilities can impose additional runtime/model requirements.

The investigation noted that some optional local synthesis functionality could require multi-gigabyte model downloads and several gigabytes of RAM.

This mattered to Orthoptera because local computation can exchange model-context cost for local CPU, RAM, storage and indexing time rather than eliminate cost.

### Repository scoping and authority

KiroGraph accepts a project path/root and constrains its graph operations around that project representation.

This demonstrated repository configuration/scoping.

It did **not** establish a security sandbox.

The wider tool surface could also include shell execution, reinforcing the distinction between:

* repository selection;
* tool profile;
* and actual authority/isolation.

### Token/context/cost conclusion

KiroGraph demonstrated mechanisms that could plausibly reduce unnecessary model-visible material:

* compact search;
* bounded node/context selection;
* progressive detail levels;
* semantic retrieval before source retrieval;
* cached reads;
* persistent graph reuse;
* persistent project-memory retrieval.

No Orthoptera measurement established that these mechanisms actually produced:

* fewer cumulative input tokens;
* fewer cached tokens;
* fewer output tokens;
* fewer turns;
* lower AI credits;
* lower monetary cost;
* lower total latency;
* or better task correctness.

The appropriate conclusion remained:

> **Capability and mechanism demonstrated; Orthoptera efficiency benefit not demonstrated.**

### Contemporary experiment implication

A further generic structural/semantic-repository-navigation experiment was not the most useful next step because GitNexus already supplied that treatment class.

The distinct experiment justified by KiroGraph was instead:

> **Does persistent agent-generated project knowledge provide useful cross-session context that cannot be efficiently reconstructed from repository graph/search tools alone?**

A proposed design used two sessions.

In the first, an agent would establish a non-obvious project fact, decision or implementation constraint and deliberately persist it.

In a genuinely fresh second session, a related task would require that knowledge.

The control would rediscover the information using normal repository mechanisms; the treatment would retrieve the persisted project knowledge.

Any accounting should include **the cost of creating the memory**, not merely its later retrieval benefit.

Primary outcomes should include correctness and successful retrieval. Model turns, source volume, cumulative tokens, cache, AI credits, indexing costs and stale/incorrect-memory incidents could be measured separately.

### Secondary cache experiment

A smaller optional experiment was also identified around repeated unchanged file reads and KiroGraph's cached-content mechanism.

The purpose would be to measure actual host/model-visible effects rather than accept claims based on the compact cache marker itself.

This remained secondary to the Level-4C project-knowledge experiment.

### Provenance

Primary upstream repository:

`https://github.com/davide-desio-eleva/kirograph`

The investigation examined current upstream `main` on 9 August 2026.

A tagged Go-module release `v0.28.1`, published 3 July 2026, was independently identified during the investigation, but it was not silently treated as equivalent to the broader current `main` implementation.

### Historical conclusion

The investigation's final capability classification was:

```text
Level 1  lexical retrieval                   demonstrated
Level 2  structural repository navigation    demonstrated
Level 3  semantic retrieval                  demonstrated
Level 4A persistent structural index         demonstrated
Level 4B persistent semantic index           demonstrated
Level 4C persistent project/agent knowledge  demonstrated
Level 5  measured Orthoptera benefit         not demonstrated
```

The key research result was therefore not that KiroGraph was another superior code-search product.

It was:

> **GitNexus established persistent structural + semantic repository representation; KiroGraph extended the investigated capability model into persistent agent/project knowledge.**

No adoption decision followed.

---

## Recovery entry — Nella investigation and subsequent refinements

**Investigation date:** 9 August 2026
**Recovered into journal:** 15 August 2026
**Candidate:** `nella-labs/nella`
**Upstream examined:** `main`
**Latest release identified during the investigation:** `v0.2.7`, commit `d4743bf`, released 6 April 2026

Nella was investigated source-first after KiroGraph, explicitly using the KiroGraph persistent-project-knowledge result as the comparison baseline.

The investigation developed through three stages:

1. an initial source-first capability investigation;
2. a refinement that challenged whether Nella's validity-aware assumptions constituted a genuinely new Level-4C capability;
3. an adversarial second pass comparing the refined conclusion against KiroGraph's established memory, staleness and conflict mechanisms.

The historical progression matters because the first interpretation was progressively weakened by the later comparisons.

### First-pass headline

The initial investigation concluded that Nella was **not a fundamentally new repository-navigation technology** relative to GitNexus and KiroGraph.

Its repository-understanding layer combined mechanisms including:

* AST-aware chunking;
* BM25 lexical search;
* vector retrieval;
* Reciprocal Rank Fusion;
* optional neural reranking;
* persisted semantic/index artefacts;
* dependency tracking;
* MCP access.

Those capabilities largely occupied capability territory already established by GitNexus and KiroGraph.

The initially distinctive feature appeared to be elsewhere:

> **persistent, typed agent assumptions associated with source files and automatically invalidated when those declared files changed.**

The first pass therefore treated Nella's assumption lifecycle as a potentially distinctive implementation of persistent project knowledge and considered a narrowly targeted stale-knowledge experiment justified.

### Nella implementation character

Nella was found to be a TypeScript/Node.js codebase-intelligence layer intended to sit between coding agents and repositories.

The investigated monorepo contained packages for:

* indexing, retrieval and context;
* MCP/CLI integration;
* API/WebSocket access;
* benchmarking/evaluation.

Its repository-understanding architecture was approximately:

```text
repository
    ↓
code chunks
    ↓
lexical + vector indexes
    ↓
hybrid retrieval
    ↓
optional reranking
    ↓
MCP / CLI / API
```

Alongside that retrieval path was persistent project/session state containing assumptions, changes and dependency information.

### Structural limitations for Orthoptera

The first pass found that Nella's structural representation was materially narrower than Code Pathfinder, GitNexus or KiroGraph.

The AST-specific chunking path used TypeScript/JavaScript parsing and attempted to align chunks with meaningful code units such as functions, classes and interfaces.

Python was supported for retrieval, but equivalent Python-specific structural extraction was not demonstrated.

The investigated representation supported concepts including:

* files;
* code chunks;
* symbols defined by chunks;
* imports/dependencies;
* architecture/file dependency relationships.

It did **not** demonstrate a rich Python program graph containing the established structural-tool capabilities such as:

* caller/callee relationships;
* comprehensive symbol-reference relationships;
* inheritance/implementation traversal;
* general control-flow;
* general data-flow;
* taint analysis.

The first-pass classification was therefore:

> **Level 2 structural navigation: partial and materially weaker for Orthoptera than the structural tools already investigated.**

Nella's relevance to Orthoptera was consequently not primarily better Python structural analysis.

### Semantic retrieval

Nella did demonstrate a genuine hybrid retrieval implementation.

The investigated search path combined:

```text
semantic vector retrieval
        +
BM25 lexical retrieval
        ↓
weighted Reciprocal Rank Fusion
        ↓
optional neural reranking
```

The implementation used explicit lexical/vector weighting and RRF parameters and could expose component scores, combined scores, reranking results and confidence/suggestion information to an agent.

This supported the classification:

> **Level 3 semantic retrieval: demonstrated.**

Unlike KiroGraph, where the investigation did not establish RRF specifically, Nella's RRF mechanism was directly demonstrated.

This did not establish a new Orthoptera capability because GitNexus had already demonstrated hybrid semantic retrieval.

### Persistent semantic representation

Nella persisted its vector/index representation to disk and could reload it across runs.

This established:

> **Level 4B persistent semantic representation: demonstrated.**

Again, this capability was already within the GitNexus/KiroGraph baseline.

### Persistent assumptions

The first-pass investigation found a concrete persistent assumption model.

An assumption contained information including:

* description;
* type;
* related files;
* confidence;
* validity;
* creation state;
* invalidation metadata.

Assumption types included categories such as:

* schema;
* interface;
* dependency;
* behaviour;
* configuration;
* structure;
* other.

Persistent session state was stored under:

```text
.nella/session.json
```

and reloaded across process invocations.

This demonstrated genuine cross-process persistence rather than an in-memory conversational cache.

### File/path-linked invalidation

The assumption mechanism associated assumptions with explicit source paths or glob patterns.

When files changed, Nella compared the changed paths with those declared relationships and could mark matching assumptions invalid, recording information such as the invalidating run and reason.

The first-pass conceptual lifecycle was:

```text
agent establishes assumption
        ↓
assumption persisted
        ↓
declared related source changes
        ↓
assumption invalidated
        ↓
future agent can be warned
        ↓
fact should be re-established
```

This mechanism was real implementation evidence rather than merely a product claim.

### Dependency snapshots

Nella also persisted package/dependency state and could compare later dependency snapshots against earlier state.

Changes to package manifests or lockfile-derived dependency state could contribute to assumption invalidation.

This broadened the invalidation mechanism beyond simple source-path modification, but it did not amount to semantic program-dependency analysis.

### Change ledger

Nella maintained persistent records of project changes containing information such as:

* run identity;
* file;
* operation;
* reason;
* explicit dependencies;
* related assumptions;
* optional hashes.

Recorded `dependsOn` relationships could be traversed to support impact reasoning over the **recorded change history**.

An important qualification emerged even in the first pass:

> **The change ledger is a graph of recorded change relationships, not an automatically inferred source-program dependency graph.**

It therefore should not receive credit for caller/callee or semantic source-dependency analysis.

### Agent-facing context retrieval

The persistent state was not merely stored.

The normal context path could expose information including:

* valid assumptions;
* recent invalidations;
* recent changes;
* dependency snapshots;
* session statistics.

The MCP surface also included assumption/context operations, including mechanisms to check assumptions explicitly.

Later refinement established that invalidated assumptions were surfaced more operationally than initially credited: recently invalidated assumptions could appear in context, and explicit assumption checks could signal an error state when invalid assumptions were present.

Therefore:

> **Persistent assumption state and explicit agent-facing retrieval of invalidated state were demonstrated.**

What remained unestablished was automatic injection of the right persistent knowledge into every future agent interaction without an appropriate context/tool invocation.

### Multi-agent coordination

The investigated source also included multi-agent facilities such as:

* agent registration;
* heartbeats/presence;
* task creation and claiming;
* task dependencies;
* decision recording/retrieval;
* file-conflict checking.

These were concrete facilities, but no evidence established that they provided an Orthoptera advantage over the existing Architectural-AI / implementation-AI workflow.

They were therefore not promoted to a new Orthoptera capability.

### Local versus external computation

The MCP server and repository-facing components could operate locally, and local vector-index implementations existed.

However, semantic indexing/reranking was not inherently fully local.

The investigated implementation included external embedding/reranking service paths.

The appropriate conclusion was:

> **Nella can be locally hosted, but its semantic retrieval path is not necessarily locally computed.**

That distinction mattered to Orthoptera's preference for existing-tier or local capabilities where practical.

### First-pass context/cost conclusion

Nella demonstrated mechanisms that could plausibly reduce repository material supplied to the coding model:

* bounded top-K retrieval;
* lexical/vector ranking;
* filtering;
* code chunks rather than complete files;
* persistent indexes;
* persistent assumptions and changes.

But semantic retrieval itself can impose embedding and reranking costs.

No Orthoptera experiment established that Nella reduced:

* cumulative model input;
* cached input;
* output tokens;
* turns;
* AI credits;
* monetary cost;
* or total task time.

The first-pass conclusion therefore retained the existing methodological separation:

> **Mechanisms demonstrated; Orthoptera token/cost benefit not demonstrated.**

### First-pass experiment proposal

The initial experiment proposal focused on the apparently distinctive property rather than generic semantic retrieval.

The proposed question was:

> **Can source-linked assumptions that automatically invalidate after repository changes prevent a fresh agent from relying on stale project knowledge?**

The intended treatment compared persistent assumptions against ordinary cross-session rediscovery, with correctness and stale-knowledge avoidance as primary concerns and token/cost measures as secondary outcomes.

At this stage, Nella's assumption mechanism was still being treated somewhat generously as a potentially distinctive Level-4C capability.

### First refinement — validity-aware assumptions are not a new capability boundary

The first-pass interpretation was subsequently challenged directly against KiroGraph's established Level-4C baseline.

The revised conclusion was more conservative:

> **Nella implements a specialised form of persistent project/agent knowledge with explicit dependency-based invalidation; it does not establish a new persistent-knowledge capability level beyond KiroGraph.**

KiroGraph already demonstrated broad persistent project knowledge, source association, stale/conflict mechanisms and cross-session retrieval.

Nella's model was narrower and more explicit:

```text
assumption
    +
declared file/path dependencies
    +
confidence
    +
validity state
    +
invalidation metadata
```

The distinguishing question therefore changed from:

> Does Nella introduce a new type of persistent knowledge?

to:

> **Does Nella's explicit assumption/invalidation lifecycle produce a materially better stale-knowledge outcome than KiroGraph's existing Level-4C mechanisms?**

The available implementation evidence could not answer yes.

### Invalidation is dependency-change detection, not semantic truth maintenance

The refinement identified a crucial distinction.

Nella demonstrably knows when an explicitly declared related path changes.

It does **not** thereby know whether the proposition represented by the assumption has become false.

The mechanism is approximately:

```text
assumption
    ↓
declared related paths/globs
    ↓
matching change
    ↓
mark assumption invalid
```

It is not:

```text
assumption proposition
    ↓
infer complete semantic dependencies
    ↓
analyse changed program behaviour
    ↓
determine whether proposition remains true
```

This substantially weakened the phrase "stale-knowledge prevention".

The more accurate description became:

> **dependency-triggered invalidation of potentially stale assumptions.**

### File-level rather than symbol-level dependency

`relatedFiles` represented paths/globs.

No evidence established:

* symbol-linked assumptions;
* automatically inferred transitive semantic dependencies;
* graph-derived dependency attachment.

This creates a possible false-negative invalidation case: an assumption can depend indirectly on another file that changes without any declared related path changing.

The mechanism can also invalidate a whole assumption when any declared related file changes; no partial-proposition validity model was demonstrated.

### Revalidation is state management

Nella exposed mechanisms for revalidation.

The implementation did not independently prove that a revalidated proposition was true.

A particularly revealing implementation detail was that clearing invalidated assumptions could revalidate them as a workaround rather than semantically re-establish their propositions.

This reinforced the conclusion:

> **The mechanism manages trust/validity state; it is not a truth-maintenance system.**

### Revised experiment implication

The original Nella-versus-filesystem experiment was therefore no longer clean.

Such a comparison would mostly test whether persistent knowledge can be useful, which KiroGraph had already established as the relevant capability class.

The smallest defensible Nella-specific experiment became:

> **Nella versus KiroGraph on one controlled stale-knowledge invalidation case.**

Primary questions:

1. Was the old knowledge surfaced as stale?
2. Did the agent nevertheless use it?
3. Was the resulting answer correct?
4. How much additional interaction was required?

A larger token/cost benchmark would only be justified if the narrow mechanism comparison first demonstrated a meaningful operational difference.

### Adversarial second pass — challenge against the full KiroGraph baseline

A further adversarial refinement deliberately attempted to falsify the conservative conclusion by looking for Nella mechanisms that KiroGraph did not already provide.

The pass strengthened several implementation findings but did **not** establish a new Orthoptera capability boundary.

### Assumption retrieval was more operationally complete than initially credited

The second pass confirmed that invalidated state was explicitly surfaced through the normal agent-facing context machinery.

The context path could return both active assumptions and recent invalidations.

Explicit assumption-checking operations could also return invalid assumptions in a form intended to stop or warn agent activity.

So an earlier qualification that persistence might exist without meaningful retrieval had been too cautious.

The corrected result was:

> **Cross-session assumption state is persistently stored and explicitly retrievable through agent-facing context operations.**

Still not demonstrated:

> **Every relevant future task automatically receives the appropriate assumption before the agent acts.**

That remains dependent on actual host/tool workflow.

### Invalidation surface broader than source-path changes alone

The adversarial pass also retained the dependency-snapshot mechanism.

The complete demonstrated invalidation surface included approximately:

```text
declared source/path changes
        +
package/dependency snapshot drift
        ↓
affected assumptions
        ↓
invalid state
```

This is broader than file changes alone.

It remains much narrower than automatically inferred semantic source dependencies.

### Preflight assumption conflict checking

Nella could compare planned file changes with relevant assumptions and generate warnings/errors based on overlapping assumptions and their state/confidence.

This provided a useful operational pattern:

```text
planned edit
    ↓
relevant persistent assumptions
    ↓
potential conflict
    ↓
warning / intervention
```

The mechanism was concrete.

It still belonged to the established Level-4C knowledge-lifecycle class rather than defining a new capability level.

### KiroGraph baseline proved stronger than the early comparison assumed

The adversarial comparison revisited KiroGraph's established memory mechanisms.

KiroGraph already demonstrated concepts including:

* persistent symbol-linked observations;
* decisions;
* errors;
* patterns;
* typed knowledge relations such as supersession, conflict and compatibility;
* stale-review scheduling;
* prompt/session-context reconstruction;
* persistent wiki/project knowledge;
* structural symbol association.

That considerably reduced the remaining novelty space for Nella.

The comparison therefore became approximately:

```text
KiroGraph
    broad persistent knowledge
    +
    structural/symbol association
    +
    conflict relationships
    +
    stale review
    +
    context reconstruction

Nella
    explicit assumptions
    +
    confidence
    +
    boolean validity
    +
    file/glob relationships
    +
    direct invalidation
```

Nella's design was more explicit and specialised around an assumption lifecycle.

KiroGraph's persistent knowledge model was broader and could associate knowledge with a richer structural representation.

The difference remained an implementation/workflow distinction **within Level 4C**.

### Cross-agent context-sharing subsystem discovered

The most interesting counter-finding in the adversarial pass was a separate internal Nella context-sharing subsystem backed by SQLite.

The investigated source contained a richer generic context model with facilities including:

* persistent context entries;
* source-agent identity;
* workspace identity;
* visibility controls;
* time-to-live/expiry;
* version history;
* optimistic-concurrency etags;
* channels;
* pub/sub concepts;
* schema validation;
* encryption;
* cross-workspace querying;
* import/export;
* fuzzy/value search;
* access metadata.

If exposed coherently to agents, this could represent a more specific capability:

> **shared, versioned, expiring multi-agent state.**

However, the adversarial investigation could not establish that this richer `context-sharing` manager was actually exposed through the principal Nella MCP path examined.

The agent-facing MCP server used the ordinary assumption/change/dependency context manager and multi-agent registry facilities.

The core public exports exposed the agent registry, but did not establish the richer generic context manager as an agent-facing MCP capability.

The correct historical classification was therefore:

> **Interesting implementation direction demonstrated in source; agent-facing capability not demonstrated.**

This possibility was deliberately not pursued into a further exposure investigation.

### Multi-agent coordination did not establish a new Orthoptera boundary

The second pass also reconsidered Nella's explicit agent registration, task, heartbeat, decision and conflict mechanisms.

These were real.

But the established KiroGraph baseline already contained agent utilities and persistent agent/project context, and Orthoptera already had a practical Architectural-AI / implementation-AI role separation.

No evidence showed that Nella's coordination model improved this workflow.

Therefore:

> **Multi-agent coordination implementation: demonstrated. New Orthoptera capability or benefit: not demonstrated.**

### Structural/Python conclusion survived

The adversarial pass did not change the first-pass structural conclusion.

Nella's structural representation remained substantially weaker for Orthoptera's Python code than Code Pathfinder, GitNexus or KiroGraph.

Its architecture/dependency representation was principally file/import oriented.

No demonstrated rich Python structural graph emerged containing the established caller/callee/reference/type traversal capability.

Nella therefore remained interesting for persistent state and knowledge lifecycle, not for superior Python repository understanding.

### Revised capability classification

The final adversarial classification was:

```text
Level 1  lexical access                         demonstrated
Level 2  structural navigation                  partial
Level 3  semantic retrieval                     demonstrated
Level 4A persistent structural representation   partial
Level 4B persistent semantic representation     demonstrated
Level 4C persistent project/agent knowledge     demonstrated
Level 5  measured Orthoptera benefit            not demonstrated
```

The crucial qualification was:

> **Nella's Level-4C implementation is specialised, validity-aware and file/dependency-linked; it is not a new Level-4C capability beyond KiroGraph.**

### Final experiment status

After the adversarial pass, even the Nella-specific experiment was downgraded.

The investigation no longer supported a broad Nella experiment.

If Nella were tested at all, the appropriate experiment was an **optional, low-priority falsification test**:

```text
one proposition
    ↓
store in KiroGraph and Nella
    ↓
directly change associated source so proposition becomes false
    ↓
fresh session
    ↓
ask task where stale proposition would cause an error
```

Measure primarily:

1. whether stale knowledge was surfaced;
2. whether the agent saw and used it appropriately;
3. whether stale knowledge was avoided;
4. whether the resulting answer was correct.

If KiroGraph and Nella behaved equivalently, the investigation should stop.

No token/cost benchmark would then be warranted.

### Provenance

Primary upstream repository:

`https://github.com/nella-labs/nella`

The investigation examined current upstream `main` on 9 August 2026.

The latest identified published release was:

`v0.2.7`, commit `d4743bf`, released 6 April 2026.

Current `main` contained later development beyond that release, so release and `main` were not silently treated as identical.

### Historical progression of the conclusion

The Nella investigation therefore developed as follows:

```text
first pass
    ↓
validity-aware assumptions appear
potentially distinctive within Level 4C
    ↓
KiroGraph comparison
    ↓
assumption invalidation becomes
a specialised Level-4C implementation
    ↓
adversarial pass
    ↓
KiroGraph baseline proves broader;
Nella mechanisms become implementation refinements,
not a new capability boundary
```

The final conclusion was:

> **Nella does not currently demonstrate a genuinely new Orthoptera capability beyond the KiroGraph baseline.**

Its assumption tracker is a real and potentially useful refinement of persistent project knowledge. It gives an agent-generated proposition an explicit lifecycle and can mark it invalid when declared source/dependency conditions change.

But the mechanism is dependency-triggered trust invalidation rather than semantic truth validation, and KiroGraph already occupies the relevant persistent-project-knowledge capability boundary.

The richer internal SQLite context-sharing subsystem remained an intriguing possibility **if it were exposed as an agent-facing capability**, but that exposure was not demonstrated and was not investigated further.

Accordingly:

* no Nella-specific Wishlist capability was justified;
* no adoption decision was justified;
* a narrow Nella-vs-KiroGraph stale-knowledge comparison remained optional and low priority;
* and generic Nella semantic-retrieval benchmarking was not justified after the GitNexus/KiroGraph baseline had already established that capability class.

No adoption decision followed.
