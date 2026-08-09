# Toolchain Wishlist

This document records AI/development-tool capabilities that appear useful for Orthoptera but are not currently part of the project's adopted tooling.

The project has a zero-cost preference. Items here are therefore not commitments to purchase or subscribe to anything.

The list is deliberately broader than immediate project requirements: discovering a useful capability is worthwhile even when it is currently out of scope.

---

## AI workflow

### More predictable model selection

A capability to explicitly select and pin the model used for an experiment or workflow would be useful for reproducibility.

Our Copilot experiments have demonstrated that the active model can be observed and may change during a session, but the mechanism and controls have not yet been established.

---

### Reproducible / isolated AI sessions

A convenient way to start an AI session with explicitly controlled:

* conversation history;
* repository state;
* model;
* tool configuration;
* MCP servers;
* persistent session state;

would be useful for controlled workflow experiments.

---

### Better experiment-level usage accounting

A tool which clearly attributed AI cost to:

* parent-agent work;
* delegated-agent work;
* tool calls;
* cached context;
* reasoning;
* output;

would make it easier to compare alternative AI workflows.

Copilot exposes AI credits and token statistics, but their precise relationship has not yet been established.

---

### Efficient repository reconnaissance

A low-cost mechanism for giving an agent a reliable, concise repository orientation without repeatedly reading large amounts of documentation would be useful.

This is particularly relevant as the project develops multiple AI tiers and specialist roles.

---

## Agent organisation

### Hierarchical agent instructions

A mechanism for sharing a common baseline of agent instructions while allowing specialist roles to load only the instructions relevant to their task would be useful.

The project is currently investigating how best to structure this without creating duplicated or conflicting sources of truth.

---

### Better subagent control

Useful capabilities would include explicit control over:

* delegated model;
* delegated context;
* delegation cost;
* task scope;
* returned output size.

The current experiments show that delegated reconnaissance can be expensive even when the requested result is relatively small.

---

## Development tooling

### Additional useful paid capabilities

Potentially useful paid services or features discovered during the project should be recorded here rather than silently becoming workflow assumptions.

Any such capability would need to be evaluated against the project's zero-cost preference before adoption.

---

## Status

This is a wishlist, not a roadmap.

Items may remain here indefinitely. An item should move into the adopted workflow only after an explicit decision is made and the relevant project documentation is updated.

