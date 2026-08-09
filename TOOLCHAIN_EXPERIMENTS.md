# Toolchain Experiments

This document records experiments and observations about the AI tooling used to develop Orthoptera.

It is deliberately separate from the project's technical architecture. The purpose is to build an empirical understanding of how the toolchain behaves, particularly where that behaviour affects cost, context, reproducibility, delegation, and the reliability of AI-assisted development.

The distinction between **observation** and **interpretation** is important. We should not turn plausible explanations of tool behaviour into facts until they have been tested.

---

## 1. Scope and purpose

Orthoptera is being developed with AI coding assistance. We are experimenting with several AI tiers and with different ways of dividing work between them.

The experiments documented here are intended to answer questions such as:

* How much context does an agent actually receive?
* What information persists within or between sessions?
* How do models and subagents affect cost and context usage?
* When is delegation useful, and when does it introduce unnecessary cost?
* Which repository information needs to be made explicit because an agent cannot safely be expected to recover it from context?
* How reproducible is an experiment when the AI tool has its own session history, caches, or persistent state?
* Which toolchain capabilities are useful but currently unavailable within our zero-cost constraints?

These experiments concern the **toolchain**, not Orthoptera's acoustic-analysis architecture.

---

# 2. Experiment A — Initial AI workflow

## 2.1 Starting arrangement

The initial working arrangement was a two-tier approach:

1. **ChatGPT** as the architectural/reasoning AI.
2. **Codex** as the implementation AI working against the local repository.

This division reflected the desire to keep architectural decisions separate from implementation and to have the implementation agent work directly with the repository.

The arrangement predates the more recent investigation of GitHub Copilot CLI.

## 2.2 Acoustic survey

The local acoustic survey was carried out using Codex.

In retrospect, this was consistent with the established two-tier division: it was an implementation/exploration task involving the local corpus and repository tooling rather than an architectural decision.

However, it also exposed a significant cost issue. The acoustic investigation involved substantial local analysis and a large AI context, making it relatively expensive in token terms.

This prompted the current investigation into alternative AI workflows and into how context, delegation and model selection affect cost.

---

# 3. Experiment B — GitHub Copilot CLI reconnaissance

The next experiment investigated GitHub Copilot CLI as a possible additional AI tier.

The purpose was not initially to solve an Orthoptera problem. It was to understand the behaviour and capabilities of the toolchain itself.

The experiment used repository reconnaissance tasks, including inspection of:

* `AGENTS.md`
* `DESIGN.md`
* `DECISIONS.md`
* `ROADMAP.md`
* `EXPERIMENTS.md`
* exploratory acoustic-analysis code
* production stubs
* package interfaces
* tests

The experiment also investigated Copilot's session, delegation, context and usage facilities.

---

## 3.1 Model selection

Copilot displayed the active model in the CLI interface.

During the experiment the model was observed as:

> `gpt-5-mini`

Earlier output associated with the delegated reconnaissance work identified another model:

> `claude-haiku-4.5`

The later `/diagnose` output explicitly reported:

> Model switch noted earlier (claude-haiku-4.5 → gpt-5-mini)

### Established observation

The model used by Copilot can be observed through the CLI and may change during the lifetime of the work being investigated.

### Not established

We have not established:

* what causes a model change;
* whether the change is automatic model routing;
* whether it is related to context, cost, availability or task type;
* whether all parts of a session necessarily use the same model;
* whether the displayed model describes every underlying operation.

These should remain open experimental questions.

---

# 4. Copilot context accounting

Copilot provides a `/content` command showing a breakdown of context usage.

One observation during the experiment was:

```text
Context Usage

auto · 49k/128k tokens (38%)

System Prompt       6.9k   (5%)
System Tools        7.3k   (6%)
MCP Tools           1.1k   (1%)
Messages           33.2k  (26%)
Free Space         73.0k  (57%)
Buffer              6.4k   (5%)
```

### Established observation

The CLI exposes at least these categories of context:

* system prompt;
* system tools;
* MCP tools;
* messages;
* free space;
* buffer.

The displayed context window in this observation was 128k tokens.

### Not established

The display does not by itself establish:

* exactly which historical material is included in `Messages`;
* whether session-state information is included there;
* whether MCP information shown here represents persistent MCP state or merely tool definitions;
* how the buffer is used;
* whether all context shown is sent to every model call;
* how context is reconstructed after compaction or model switching.

Those questions require further experimentation.

---

# 5. Copilot session state

Copilot exposes session information through `/session`.

The investigated session reported:

```text
Session ID: 8d49da86-255d-44b8-9494-548a2b72164c

Name: Review Available Tools and MCP Servers
Duration: 10h 24m 15s
Created: 08/08/2026, 20:15:27
Modified: 08/08/2026, 20:15:27
Directory: /Users/simonmajor/gh/chatgpt/orthoptera
Log: /Users/simonmajor/.copilot/logs/process-1786216527485-28840.log
Session: /Users/simonmajor/.copilot/session-state/8d49da86-255d-44b8-9494-548a2b72164c/events.jsonl
```

The session also exposed a session-state workspace containing:

```text
acoustic-event-implementation-brief.md
production-status-acoustic-events.md
```

### Established observation

Copilot maintains persistent session artefacts outside the repository, including:

* a session log;
* an `events.jsonl` file;
* a session-state directory;
* files created during the session.

### Important practical observation

The session-state artefacts allowed us to recover substantial work after the terminal presentation of the model's response became difficult to capture.

The terminal display therefore should **not** be treated as the sole record of an AI experiment.

### Not established

The existence of session-state files does not by itself establish that all of their contents are supplied to subsequent model calls.

In particular, we have not established what constitutes Copilot's effective "memory" between interactions or between sessions.

---

# 6. Delegated agents

Copilot can delegate work to an `explore` agent.

During the acoustic-event reconnaissance experiment, an explore agent was launched to inspect the repository.

The session later reported:

```text
Explore subagent ran and completed (model gpt-5-mini).
Metrics: 30 tool calls, ~290,532 tokens consumed, duration ~105.6s.
```

The session also identified completed agents including:

```text
acoustic-event-representation
acoustic-event-production-stat...
```

### Established observations

* Delegated agents are separately identifiable.
* A delegated agent can use a model independently identifiable from the main session.
* Delegated work can involve substantial tool activity and token consumption.
* The resulting work can be written to session-state artefacts.
* `/diagnose` can expose execution metrics for completed delegated work.

### Important workflow observation

A delegation which appears simple from the user's perspective can consume a substantial amount of model/tool context.

The reconnaissance experiment therefore demonstrated that **delegation is not inherently a cost-saving mechanism**.

### Not established

We have not established:

* exactly what context is passed to a delegated agent;
* whether the parent conversation is passed in full;
* whether repository instructions are independently loaded;
* whether delegated agents share caches or other state with the parent;
* whether the model choice is controlled by the parent or by Copilot;
* how delegated-agent costs are calculated.

---

# 7. AI-credit accounting

Copilot exposes an AI-credit figure in the session interface.

During the experiment, the bottom-right/session area displayed:

> `Session: 69.3 AIC used`

Later, `/session info` reported:

```text
AI Credits 69.3
Tokens     ↑ 2.2m (1.7m cached, 191.8k written) • ↓ 58.4k (10.5k reasoning)
```

Subsequently `/limits` reported:

```text
Used in this session: 75.7 AI credits.
```

### Established observations

* Copilot reports AI-credit usage separately from token counts.
* A session can consume millions of tokens while displaying a much smaller AI-credit number.
* The AI-credit figure can increase as further model activity occurs.
* `/session info` exposes both AI-credit and token accounting.

### Not established

We have **not** established a conversion between:

* input tokens;
* cached tokens;
* output tokens;
* reasoning tokens;
* AI credits.

We should therefore avoid treating AI credits as a proxy for token count.

---

# 8. Session limits

Copilot provides optional session AI-credit limits through `/limits`.

The CLI reports:

```text
Session limits are opt-in.
They apply across the current conversation.
The AI credit limit is a soft cap:
usage is checked after model calls return,
so one call may exceed the limit before the next one is blocked.
```

The experiment reported:

```text
Used in this session: 75.7 AI credits.

Suggested limit: 112 AI credits.
```

The suggested limit was described as being based on historical full-session AI-credit usage for similar sessions using `claude-haiku-4.5`.

### Established observations

* Session limits are optional.
* They apply across the current conversation.
* `/clear` and `/new` reset used AI credits while retaining the configured limit.
* The limit is a soft cap rather than a hard per-call ceiling.
* Copilot can suggest a session limit based on historical usage.

### Not established

We have not established how the suggested limit is calculated in detail, nor whether the historical comparison is sufficiently similar to make it useful for Orthoptera experiments.

---

# 9. Cost of broad reconnaissance

The acoustic-event reconnaissance was intentionally broad: an explore agent was asked to compare documentation, exploratory code, tests, package interfaces and production stubs.

The resulting `/diagnose` report recorded:

```text
Explore subagent ran and completed (model gpt-5-mini).
Metrics: 30 tool calls, ~290,532 tokens consumed, duration ~105.6s.
```

The session subsequently showed:

```text
AI Credits 69.3
Tokens ↑ 2.2m ...
```

and later:

```text
Used in this session: 75.7 AI credits.
```

### Established observation

Broad repository reconnaissance can generate substantial token and AI-credit consumption even when the requested result is a relatively concise report.

### Operational consequence

Large exploratory outputs also created practical handling problems:

* output was large enough to be paged through temporary files;
* copied terminal output became difficult to recover reliably;
* the TUI presentation changed during the session;
* the useful report was ultimately recoverable from session-state artefacts.

### Not established

We have not yet measured which component contributes most to the cost:

* repository reading;
* tool-call output;
* model reasoning;
* delegated-agent context;
* repeated reads;
* output generation;
* caching behaviour.

Future experiments should measure these separately where practical.

---

# 10. Copilot command history and session tooling

The CLI provides several facilities relevant to experimentation:

```text
/session
/session id
/session info
/session checkpoints
/session files
/session plan
/diagnose

/chronicle
/chronicle standup
/chronicle search
/chronicle tips
/chronicle cost-tips
/chronicle improve

/limits
/limits set
/limits predict
/limits unset
```

### Observed behaviour

`/session id` displayed the session ID and copied the raw ID to the clipboard.

`/session info` provided particularly useful information about:

* session identity;
* duration;
* repository directory;
* logs;
* session-state;
* workspace files;
* AI credits;
* token usage.

`/session files` listed files created in the session.

`/session plan` reported whether a plan existed.

`/diagnose` inspected the session history and provided a post-hoc summary of tool failures, model activity, token consumption and other observations.

### Rough edges observed

`/chronicle search` initially produced an internal SQL error:

```text
"multiple SQL statements are not allowed"
```

It subsequently retried with a single statement and returned no matching sessions.

The terminal/TUI also proved awkward for copying long model responses into another environment.

These are operational observations only; they do not establish the underlying implementation.

---

# 11. Session compaction and checkpoints

During the experiment, Copilot compacted the conversation history and created a checkpoint:

```text
Checkpoint #1
Acoustic-event status audit
```

The checkpoint preserved a substantial summary of:

* work already performed;
* files created;
* repository inspection results;
* established design facts;
* unresolved questions;
* technical details;
* suggested continuation information.

### Established observation

Conversation compaction does not necessarily mean that all useful session information is simply lost. Copilot can create a checkpoint containing a summary of the preceding work.

### Not established

We have not established:

* exactly how checkpoint contents are incorporated into subsequent model context;
* whether the original messages remain accessible to the model;
* how much information is lost during compaction;
* whether compaction behaviour differs between models.

---

# 12. Current working hypotheses

The following are **hypotheses to test, not established facts**.

### 12.1 AI-tool memory

Copilot appears to maintain information outside the immediate visible conversation, because session logs, events and session-state files exist.

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

# 13. Experimental discipline emerging from the work

These are observations about what makes the experiments more reliable, rather than requirements on Orthoptera itself.

For future toolchain experiments we should record, where available:

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

The purpose is to make it possible to distinguish a change in tool behaviour from a change in prompt, repository state, model, accumulated context or delegation.

---

# 14. Open experimental questions

The following questions remain deliberately open.

## Context and memory

* What information from previous turns is actually supplied to each model call?
* What information survives compaction?
* What information survives `/clear`?
* What information survives `/new`?
* What information survives starting a completely new CLI process?
* What information is obtained from session-state?
* What information is obtained from repository files?
* What MCP information is persistent, and what is reconstructed per invocation?

## Models

* Under what circumstances does Copilot switch models?
* Is model selection deterministic?
* Does delegation use the same model-selection mechanism as the parent session?
* Does model selection affect AI-credit consumption?

## Cost

* How are AI credits calculated?
* How do cached tokens affect AI-credit usage?
* How do reasoning tokens affect it?
* How much of the cost of a delegated task comes from tool output versus model reasoning?
* How useful are `/limits predict` recommendations for our particular workloads?

## Delegation

* What context does an explore agent receive?
* Does it independently load `AGENTS.md` and other repository instructions?
* Does it inherit conversation history?
* Does it inherit session-state?
* Can delegation reduce the context burden on the parent agent, or does it primarily add another model invocation?

## Reproducibility

* What constitutes a genuinely fresh Copilot experiment?
* Is `/new` sufficient?
* Is `/clear` sufficient?
* Does a fresh process behave differently?
* Does the repository itself need to be reset?
* Should model, context and session state be treated as experimental controls?

---

# 15. Relationship to other project documentation

This document records **what we discover about the toolchain**.

It does not define how Orthoptera should be architected or how contributors should work.

The eventual workflow and guardrails for working with AI coding agents belong in the project's normal contributor/agent documentation, principally:

* `CONTRIBUTING.md`
* `AGENTS.md`

Decisions about the toolchain itself belong in:

* `TOOLCHAIN_DECISIONS.md`

Useful capabilities that we identify but do not currently intend to adopt belong in:

* `TOOLCHAIN_WISHLIST.md`

This separation is intentional: experiments record observations, decisions record choices, and contributor/agent documentation records the resulting operational rules.

---

## 16. Status

This document is an experimental record, not a specification.

Where a statement is explicitly labelled an observation, it should be treated as evidence from the experiments described here. Where behaviour is marked as unresolved or hypothetical, it should not be promoted into project policy without further evidence or an explicit decision.

