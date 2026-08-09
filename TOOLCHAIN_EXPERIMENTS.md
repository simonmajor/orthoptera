# Toolchain Experiments

This document records experiments investigating the behaviour of the AI coding toolchain used alongside the Orthoptera project, principally GitHub Copilot CLI and its agents, models, MCP servers, session state, context handling, and persistence.

It is deliberately separate from the main project documentation. The purpose is to record observations and experimental results without allowing assumptions about the toolchain to become project requirements or architectural decisions.

## Experimental principles

The experiments should distinguish:

* **Observed** — directly visible in the CLI or otherwise independently established.
* **Reported** — information explicitly returned by a tool or command.
* **Inferred** — a plausible interpretation which has not yet been established.
* **Unknown** — something we have not yet determined.

We should avoid treating an apparent explanation of tool behaviour as established merely because it is plausible.

Where practical, record:

* exact prompt or command used;
* model displayed by the CLI;
* AIC usage displayed by the CLI;
* relevant `/content`, `/session`, or other command output;
* active agents/subagents;
* MCP servers;
* relevant session or repository state;
* whether the experiment was performed in a fresh or continuing session;
* the outcome, including failures or stalls.

---

## Current observations

### Copilot CLI session

The CLI can display the currently selected model in the bottom-right corner of the interface.

In the experiments so far, the model displayed was:

`gpt-5-mini`

The model may change during a session or between delegated tasks. This has not yet been systematically tested.

The CLI also displays a session-level indicator above the prompt:

`Session: 69.3 AIC used`

The meaning of AIC and the relationship between this figure, individual model calls, agents, and token usage has not yet been experimentally characterised.

### Context reporting

The `/content` command reports context usage. An observed output was:

```text
Context Usage

auto · 49k/128k tokens (38%)

System Prompt     6.9k   (5%)
System Tools      7.3k   (6%)
MCP Tools         1.1k   (1%)
Messages         33.2k  (26%)
Free Space       73.0k  (57%)
Buffer            6.4k   (5%)
```

This establishes that the CLI exposes a breakdown of the current context, including messages, system material, MCP tools, and remaining context space.

It does **not**, by itself, establish what information is retained outside this context or how session persistence interacts with it.

### Session reporting

The `/session` command can show active sessions/activities.

An observed output included:

```text
Sessions

❯ ● Review Available Tools and MCP Servers (active)
```

The relationship between this session/activity representation and the underlying model context, agent state, or persistent state remains to be established.

### Plugin reporting

The correct command observed so far is:

```text
/plugin list
```

An observed response was:

```text
No plugins installed.
```

The CLI also reported that plugins can be installed from a marketplace.

The presence or absence of plugins is therefore observable independently of MCP server availability.

### MCP server state

Following successful sign-in, the CLI reported:

```text
Signed in successfully as simonmajor!

GitHub MCP Server: Connected

MCP Servers reloaded: 1 server connected
```

A subsequent tool inventory reported GitHub MCP functionality including:

* code search;
* repository file retrieval;
* user search;
* Copilot Spaces access.

The exact distinction between MCP tools, GitHub CLI functionality, and other CLI tools should be treated as an experimental question rather than assumed from their names.

### Agents/subagents

The CLI can delegate work to an `explore` agent.

For example:

```text
Explore(gpt-5-mini) Inspect repo and report production acoustic-event representation and detection status...
```

The CLI subsequently displayed agent/task state separately from the main interactive prompt.

Completed agents may remain represented in session state after completion. The persistence and reuse semantics of completed agents have not yet been established.

---

# Experiment A — Initial reconnaissance

## Objective

Determine what an `explore` agent can discover about the repository and how much repository-specific context it can establish without being given detailed implementation instructions.

## Method

The task was delegated to an explore agent with instructions to inspect the repository, identify files relevant to acoustic-event representation, explain the actual data flow, and distinguish established facts from inference.

The resulting investigation identified:

* `DESIGN.md`
* `DECISIONS.md`
* `exploratory/acoustic_survey.py`
* `src/orthoptera/xcapi/download.py`
* production signal/database/analysis stubs
* relevant tests

The agent also ran the exploratory acoustic survey.

## Observation

The explore agent was capable of:

1. inspecting multiple repository files;
2. running repository code;
3. producing a cross-file interpretation;
4. distinguishing, at least in principle, established facts from inference.

However, the first resulting implementation brief subsequently contained several assertions which went beyond what the repository actually established.

A later, more restrictive reconnaissance prompt produced a substantially more cautious analysis.

## Result

The important experimental finding is therefore not simply that the agent can inspect the repository, but that **prompt constraints materially affect whether it reports repository facts or fills gaps by inference**.

This motivated subsequent experiments using explicit prohibitions against:

* proposing implementation details;
* inferring APIs;
* inferring data structures;
* inferring algorithms;
* inferring schemas;
* filling unspecified design gaps.

---

# Experiment B — Controlled reconnaissance

## Objective

Determine whether a fresh/repeated explore task can independently recover the repository's established state when explicitly instructed not to infer missing architecture.

## Prompt

The current controlled prompt is:

```text
Delegate this to the explore agent. Inspect the repository and report the current state of the production acoustic-event representation and detection work.

Compare DESIGN.md, DECISIONS.md, ROADMAP.md, EXPERIMENTS.md, the exploratory acoustic implementation, relevant tests, package interfaces, and existing production stubs.

For each aspect that appears to be specified, identify the exact repository-relative file and passage that establishes it, and classify it as:

- decided
- experimentally demonstrated
- unresolved

In particular, distinguish what the repository actually establishes from what could merely be inferred from the exploratory implementation.

Do not propose code changes, APIs, data structures, algorithms, schemas, or solutions. Do not fill gaps by inference.

The purpose is to determine the smallest set of facts that a coding agent can safely act on without making a new architectural decision.

Cite repository-relative file paths throughout.
```

## Observed execution

The CLI initially reported:

```text
Explore Executing task
```

and then:

```text
Explore(gpt-5-mini) Inspect repo and report production acoustic-event representation and detection status...
```

The agent began by reading:

* `tests/test_xcapi.py`
* `tests/test_package.py`

The run subsequently appeared to stall while the TUI itself remained responsive and allowed tab changes.

## Current status

The run has not yet established whether:

* the agent itself stopped;
* a tool invocation stalled;
* background work continued;
* the CLI was waiting for a result;
* model execution changed;
* the session remained active despite the apparent stall.

These are **unknown**, not established explanations.

---

# Persistence questions

The experiments have raised several separate persistence questions.

### Repository persistence

Repository files obviously persist independently of the AI session.

The important question is whether an agent is drawing only on the current repository state or also on additional session-level state.

### Session persistence

The CLI exposes a session-state directory and session-related commands.

An observed session-state location has included:

```text
/Users/simonmajor/.copilot/session-state/...
```

This directory has contained files produced during agent work, including generated analysis documents.

This establishes that at least some agent-generated artefacts can exist outside the repository.

It does **not** establish that the model automatically reads all such files on subsequent tasks.

### Agent persistence

Completed agents have appeared in session listings after their work finished.

It is currently unknown whether this represents:

* retained conversational state;
* retained task metadata;
* retained tool state;
* merely historical session information;
* or some combination.

### MCP persistence

An MCP server can remain connected after authentication and can be reloaded by the CLI.

It is not yet established whether MCP connections themselves provide persistent conversational memory.

### Model persistence

The model displayed in the interface has so far been observed as `gpt-5-mini`.

It is not yet established whether:

* model selection is fixed for a session;
* delegated agents independently select models;
* Auto mode can change models during a task;
* model changes affect retained context;
* or model changes are relevant to the observed repository results.

---

# Experimental controls still needed

Future experiments should vary one factor at a time where possible.

Useful comparisons include:

1. **Same session, repeated reconnaissance**

   * Tests what survives naturally within a continuing session.

2. **Fresh CLI session, same repository**

   * Tests what is available without the previous conversational context.

3. **Fresh session with the same repository but no session-state artefacts**

   * Tests whether external session artefacts affect results.

4. **Same task with different models**

   * Tests model-dependent behaviour.

5. **Same task with and without delegated agents**

   * Tests whether delegation changes available context or behaviour.

6. **Same task with MCP connected/disconnected**

   * Tests the contribution of MCP availability.

7. **Same task with deliberately minimal context**

   * Tests how much repository understanding comes from the repository itself versus accumulated session context.

The purpose of these comparisons is to establish observations, not to assume a particular internal architecture.

---

# Working terminology

For this experiment, the following terms should not be treated as interchangeable:

* **context** — information supplied to the model for a particular invocation;
* **conversation/session** — the interactive CLI state visible through session commands;
* **agent** — a delegated unit of model work;
* **MCP server** — an external tool/service connection;
* **repository state** — files and other persistent project contents;
* **session-state** — files or state maintained outside the repository by the CLI;
* **memory** — reserved term for persistence demonstrated to affect a later model invocation.

In particular, the existence of session-state files or completed-agent records is **not sufficient evidence that the model has memory of their contents**.

---

# Status

This document records the state of the toolchain investigation as observations accumulate.

It should not be treated as documentation of Copilot's internal architecture. Where behaviour has not been experimentally established, it should remain explicitly marked as unknown or inferred.

The principal experimental question is:

> **When an AI coding agent appears to "remember" repository-specific information, where did that information actually come from?**

The competing sources to distinguish experimentally are:

1. the current prompt;
2. current conversation context;
3. repository files;
4. tool/MCP results;
5. persistent session state;
6. delegated-agent state;
7. model-level or service-level memory.

No assumption should be made that any one of these is responsible until an experiment demonstrates it.

