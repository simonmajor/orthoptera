# Provisional Project-Structure Research Plan

This is the mutable record of current intended work and sequencing for the provisional sub-project. Planned work is not evidence, a finding or a decision. Completed work should be recorded in `JOURNAL.md`. A completed-work entry may retain the implications, unresolved questions, speculation and possible follow-up work produced at that time; later changes to current intent modify this plan without rewriting that historical entry.

## Initial research questions

* How do submodule, subtree, nested ordinary-directory and sibling/workspace attachment models differ for reusable AI infrastructure?
* How do AI agents behave in multi-repository projects and in local/nested versus peer/sibling layouts?
* How do subordinate `AGENTS.md` files behave, and what instruction-discovery, inheritance and conflict semantics are reliable across relevant agents?
* Which documentation templates, skills and guidance can be reused without transferring ownership of instantiated documents away from the host?
* What host-side attachment metadata is needed, and where should it live?
* Which attachment update policies suit projects that evolve at different rates?
* How should experiments preserve exact host, reusable-project, tool, model and environment provenance as attachments advance?
* How can an existing repository be inspected, recovered and adapted without replacing accumulated knowledge or disrupting existing external relationships?
* Which journal and mutable-document topology best preserves history while keeping current state usable?
* How can an initially embedded provisional sub-project later be extracted into an independently reusable repository?

The investigation must cover both a new-host path and an existing-host path. Orthoptera's completed documentation-recovery work is a candidate case study for the latter, but recovering that history into this journal is a separate next phase.

## Deferred candidate deliverables

Future work may produce tools to:

* bootstrap a new project;
* adapt or bootstrap an existing project;
* audit project documentation and instruction structure;
* migrate or upgrade project-structure conventions through explicit, reviewable changes.

These are candidate outcomes, not implemented interfaces or adopted designs. This initial iteration deliberately contains no scripts or code.

## Unresolved structural choices

The sub-project's final name, repository location, physical attachment mechanism, update policy, host metadata format, provenance syntax, document topology, template format and extraction process remain unresolved. Peer reusable projects must not be represented through recursive physical nesting.
