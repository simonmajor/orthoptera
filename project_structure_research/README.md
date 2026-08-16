# Provisional AI Project-Structure Research

This directory is the minimal seed of a provisional reusable sub-project concerned with AI-assisted project and repository structure, documentation architecture, attachment mechanisms, agent instructions and reusable project scaffolding.

Its name, internal document topology and future repository identity are working choices. The seed exists so the investigation can preserve its own history before attempting broader design or repository reorganisation. It does not select a final attachment mechanism, migrate Orthoptera's existing AI-toolchain material or establish a bootstrap implementation.

## Founding requirements

### Host-attachable, not host-dependent

Reusable AI infrastructure must be attachable to a host project without depending intrinsically on that host's paths or structure. A future host should be able to attach reusable project-structure and AI-toolchain projects, then seed or adapt project documentation and root agent guidance while retaining ownership of its accumulated knowledge.

Both new-host and existing-host bootstrap paths are first-class:

* a new host may initialise a repository, attach reusable infrastructure and seed initial documentation and instructions;
* an existing host must first inspect and preserve its source, documentation, history, project knowledge and external relationships before adapting any scaffold.

Orthoptera's documentation-recovery exercise is the founding case study for the existing-host path. A recovery first-pass reconstruction is recorded in `JOURNAL.md`; the broader recovery-derived documentation second pass remains outstanding in `PLAN.md`.

### Host-owned instantiated documentation

Reusable templates may eventually seed host documentation. Once instantiated, those documents belong to the host project. Tooling must not silently overwrite accumulated host knowledge. Any future upgrade or migration mechanism must produce explicit, reviewable changes.

### Peer reusable projects

The project-structure and AI-toolchain investigations are conceptually peer reusable projects. Either may logically use the other's guidance or capabilities, but neither should physically contain the other recursively. Possible emulation or workspace arrangements remain subjects for later investigation rather than requirements of this seed.

### Separate attachment properties

The investigation must keep these properties distinct:

* attachment identity;
* attachment physical mechanism;
* attachment update policy;
* evidence and experiment provenance.

Different reusable projects may require different update rates. A moving attachment policy must not weaken the reproducibility of experiments performed against exact earlier revisions.

### Exact experimental provenance

Journal entries and experiments must be capable of recording, where relevant:

* host project name and repository URL;
* exact host repository revision;
* exact revision of this reusable project;
* exact revisions of other relevant attached reusable projects;
* relevant tool, model and environment versions.

This seed does not impose a final metadata syntax. The requirement is that experimental context remain recoverable even after a host's attachments advance.

## Documentation roles

* `JOURNAL.md` is the append-only historical record of completed work and its contemporary understanding.
* `FINDINGS.md` is the append-only historical journal of durable findings supported by the evidence.
* `DECISIONS.md` is the append-only historical journal of actual decisions made by the investigation.
* `PLAN.md` is the mutable record of current questions, candidate work and deferred deliverables.
* `AGENTS.md` contains instructions scoped to this provisional sub-project.

Additional document roles should be introduced only when actual research demonstrates a need. Findings and decisions must not be inferred merely from journal entries or plans; the initial records were introduced only after an explicit extraction review concluded that the recovered evidence justified them.

## Current limits

No bootstrap, audit, migration or upgrade scripts exist yet. No submodule, subtree, nested-directory, sibling-workspace, symlink or other attachment model has been selected. Existing Orthoptera toolchain journals remain where they are and outside this sub-project boundary.
