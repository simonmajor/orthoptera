# AI Toolchain Planned Experiments Sequence

This document records the **forward-looking sequence of planned and candidate AI-toolchain experiments** for Orthoptera.

It is a planning document, not a historical journal.

## Purpose

The completed-experiment journal records what has actually happened.

This document records what we intend to investigate next, what is currently queued, what dependencies or prerequisites exist, and how the investigation should be sequenced.

This is the mutable record of **current experimental intent**.

Historical journal entries may legitimately contain the proposals, hypotheses, unresolved questions, implications and suggested future experiments that formed part of an investigation at the time. Those statements remain historical evidence and are not removed merely because they are forward-looking.

An experiment belongs here when it remains part of the current planned or candidate sequence.

## Relationship to the toolchain journals

The toolchain records have distinct purposes:

* `TOOLCHAIN_EXPERIMENTS.md` — completed experiments and historical evidence;
* `TOOLCHAIN_FINDINGS.md` — durable findings;
* `TOOLCHAIN_DECISIONS.md` — decisions actually made;
* `TOOLCHAIN_WISHLIST.md` — candidate capabilities;
* `TOOLCHAIN_PLANNED_EXPERIMENTS_SEQUENCE.md` — planned future experiments.

A planned experiment is not evidence.

A capability appearing on the wishlist is not necessarily an experiment that should be run.

A completed experiment should be removed from the active planning sequence only when its outcome has been recorded in the completed-experiment journal. The historical experiment itself must never be deleted from that journal.

## Planning principles

Prefer small, bounded experiments over broad exploratory sessions where the latter are likely to consume substantial model resources.

Where a proposed experiment depends on another experiment having established a capability or baseline, retain that dependency explicitly.

Do not plan experiments merely to compare products by feature count. Prefer experiments that answer a specific Orthoptera-relevant question.

Do not treat token, context or cost savings as established merely because a tool provides a mechanism that might produce them. Where those outcomes matter, make them explicit experimental measurements.

Do not create an experiment solely because a capability exists. There should be a question whose answer could change our understanding or a decision.

## Current planned sequence

### No experiment is promoted here merely because it appeared in historical discussion

Historical experiment proposals are deliberately preserved in the completed-experiment journal as part of the contemporary investigation record. They should only be placed in the active sequence when they remain intentionally planned after the current documentation checkpoint.

### Candidate: structural repository navigation comparison

**Purpose:** Determine whether structural repository navigation provides an operational advantage over the lexical filesystem/search baseline for representative Orthoptera repository-navigation tasks.

**Relevant prior investigations:** Code Pathfinder; GitNexus.

**Candidate tasks:** caller discovery, dependency tracing, and change-impact analysis.

**Possible control:**

```text
agent
 ├── filesystem
 └── rg/shell
```

**Possible treatment:**

```text
agent
 ├── filesystem
 ├── rg/shell
 └── structural repository navigation
```

**Potential measurements:**

* model turns;
* tool calls;
* cumulative input tokens;
* cumulative output tokens;
* cached tokens;
* AI credits;
* observable context occupancy;
* source volume retrieved;
* local indexing time;
* index/storage overhead;
* query latency;
* wall-clock time;
* task correctness;
* structural-navigation errors or incomplete relationships.

The useful success criterion is not simply fewer tool calls. The meaningful question is whether task correctness is maintained or improved while total model-side work is reduced after relevant local tooling costs are included.

### Candidate: persistent hybrid structural + semantic retrieval

**Purpose:** Determine whether persistent hybrid structural and semantic repository retrieval provides an Orthoptera-relevant capability beyond structural navigation alone.

**Relevant prior investigation:** GitNexus.

This should remain conceptually separate from the structural-navigation comparison. A persistent semantic/structural representation introduces additional capabilities and costs that should not be attributed to structural navigation generally.

Run or otherwise resolve the structural-navigation comparison first unless there is a specific reason to skip it. Otherwise a successful treatment could conflate the effects of structural navigation, semantic retrieval and persistent reuse.

### Candidate: persistent project/agent knowledge

**Purpose:** Determine whether persistent agent-generated project knowledge provides an operational advantage over reconstructing the same knowledge from repository-derived context in a later session.

**Relevant prior investigation:** KiroGraph.

This is a Level-4C knowledge-lifecycle experiment rather than another repository-index or semantic-retrieval comparison. The important distinction is between rediscovering project knowledge from source-derived context and selectively retrieving knowledge that an earlier agent session deliberately persisted.

**Possible control:**

```text
later agent session
        ↓
repository-derived rediscovery
        ↓
task
```

**Possible treatment:**

```text
earlier agent session
        ↓
persistent project/agent knowledge
        ↓
later agent session retrieves relevant knowledge
        ↓
task
```

The experiment should test whether the persisted knowledge is actually retrieved and used, whether unnecessary rediscovery is avoided, and whether correctness is maintained or improved. Token, context, turn or cost reductions should only be claimed if directly measured.

### Candidate: Nella stale-knowledge mechanism comparison

**Purpose:** If still considered worthwhile, compare the operational handling of directly invalidated persistent knowledge between Nella and the existing KiroGraph baseline.

**Scope:** mechanism comparison only; not a general productivity benchmark.

This is an optional refinement experiment **within Level 4C**, not an investigation of a new capability level. It should follow the KiroGraph persistent-project-knowledge experiment so that the treatment baseline has first been established.

**Potential measurements:**

1. Was stale knowledge surfaced?
2. Did the agent see or retrieve the stale state?
3. Did it avoid relying on the stale proposition?
4. Was the resulting answer or implementation correct?

This experiment should only be run if the question remains materially unresolved after the recovered KiroGraph and Nella investigations.

The existence of Nella's richer internal context-sharing implementation is not by itself a reason to schedule an experiment; its exposure as an agent-facing capability remains unestablished.

## Sequence maintenance

This document may be edited as plans change.

Unlike the completed-experiment, findings and decisions journals, it is intentionally **not append-only**: obsolete plans may be removed, reordered or rewritten as the investigation evolves.

When an experiment is completed, its historical record belongs in `TOOLCHAIN_EXPERIMENTS.md`. Durable conclusions belong in `TOOLCHAIN_FINDINGS.md`, and any resulting actual decision belongs in `TOOLCHAIN_DECISIONS.md`.

Do not move an unfinished experiment into the completed-experiment journal merely because its rationale or proposed method has been written down.

