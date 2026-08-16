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

The investigation must cover both a new-host path and an existing-host path. Orthoptera's documentation-recovery first pass is the founding case study for the latter. Its recovery-derived documentation second pass remains a separate planned phase.

## Deferred candidate deliverables

Future work may produce tools to:

* bootstrap a new project;
* adapt or bootstrap an existing project;
* audit project documentation and instruction structure;
* migrate or upgrade project-structure conventions through explicit, reviewable changes.

These are candidate outcomes, not implemented interfaces or adopted designs. This initial iteration deliberately contains no scripts or code.

## Unresolved structural choices

The sub-project's final name, repository location, physical attachment mechanism, update policy, host metadata format, provenance syntax, document topology, template format and extraction process remain unresolved. Peer reusable projects must not be represented through recursive physical nesting.

---

## Checkpoint — inherited documentation work and sub-project bootstrap

This checkpoint captures current intent inherited from the Orthoptera documentation recovery and the discussions that created this provisional sub-project.

It is deliberately a planning record rather than a finding or decision. The recovered history in `JOURNAL.md` remains the evidence base.

### Extraction checkpoint completed

The first bounded extraction review of the recovered documentation-recovery journal completed on 17 August 2026.

It:

1. identified evidence-supported durable findings;
2. distinguished actual decisions from provisional practices that merely worked during the recovery;
3. concluded that dedicated findings and decisions journals were justified;
4. recorded practices deliberately not promoted and candidate experiments that could test the most material ones;
5. refined this plan without summarising away the historical evidence.

Further findings and decisions may emerge from later research. The initial extraction is a checkpoint, not a claim that the case study can produce no further knowledge.

### Target attachment outcome

The long-term target is reusable AI infrastructure that can be attached to arbitrary development repositories.

The intended usage includes both:

```text
new repository
    ↓
attach reusable project-structure infrastructure
attach reusable AI-toolchain infrastructure
    ↓
bootstrap host-owned project documentation,
agent guidance, reusable skills/templates and integration
```

and:

```text
existing repository
    ↓
inspect existing source, documentation, history,
knowledge and external relationships
    ↓
attach reusable infrastructure
    ↓
adapt/migrate through explicit reviewable changes
without replacing accumulated host knowledge
```

A future project-structure bootstrap facility is expected to orchestrate or guide this process.

Likely bootstrap inputs include reusable documentation conventions, templates, skills and `AGENTS.md` guidance from the project-structure repository.

Instantiated documentation belongs to the host project and must not subsequently be overwritten merely because the reusable templates evolve.

The exact bootstrap interface and attachment mechanism remain unresolved.

### Attachment velocity is separate from provenance

Different reusable projects may intentionally use different attachment-update policies.

A working hypothesis is:

* the AI-toolchain attachment may evolve rapidly and may often be advanced by a host to obtain recently validated tooling capabilities;
* the project-structure attachment may become comparatively stable and should probably advance through more deliberate structural migrations.

This is a hypothesis to investigate rather than an adopted attachment policy.

Regardless of update policy, historical journal and experimental evidence must retain exact provenance sufficient to identify the host and reusable-project revisions under which the evidence was produced.

A moving attachment must not make earlier evidence ambiguous.

### Emulated attachments while the architecture evolves

For now, the reusable projects remain physically within the Orthoptera Git repository.

This deliberately emulates future attachment while retaining a single repository during rapid structural evolution and while multi-repository AI-agent behaviour remains under investigation.

Do not infer from the current embedding that nested repositories are the intended final architecture.

The project-structure and AI-toolchain projects are conceptual peers. Logical reciprocal use must not create recursive physical attachment.

### Repository-wide documentation second pass remains outstanding

The historical knowledge recovery first pass for Orthoptera and the toolchain has been completed.

A repository-wide recovery-derived documentation second pass was deliberately deferred until after that first pass.

Known work includes:

* review explicit front matter, document purpose and invariants;
* review journal versus mutable-document roles;
* make document authority and cross-reference rules explicit where useful;
* improve external/source provenance and links back to underlying investigations;
* distinguish current state from historical evidence consistently;
* review duplication, misplaced material and any residual knowledge loss explicitly;
* review temporal claims such as `complete`, `current`, `next`, `deferred` and `initial` against the recovery checkpoint;
* refresh the provisional project-structure orientation documents where their seed-era wording no longer states the first-pass/second-pass distinction clearly;
* revisit subordinate `AGENTS.md` discovery, scope, inheritance and conflict semantics;
* investigate whether folders improve context scoping and future extraction;
* review naming once document roles have stabilised;
* perform renames and moves only after content/role decisions, preferably in isolated commits.

The earlier assumption that this second pass should immediately precede the subordinate-`AGENTS.md` and folder decisions has been superseded by the creation of this sub-project.

Those structural questions are now research inputs to this project. Broad restructuring should wait for useful findings rather than prejudging the investigation.

Targeted correctness fixes may still precede the full structural pass where current guidance is known to be misleading.

### Targeted guidance correction completed

On 17 August 2026, the over-broad planning-separation invariant in root `CONTRIBUTING.md` was reconciled with the model already used by the project-structure and toolchain documents:

* journals preserve completed work in its contemporary epistemic state;
* historical entries may include implications, hypotheses, unresolved questions, speculation and proposed follow-up work understood at that time;
* mutable planning documents record current intent and sequencing;
* later changes in intent do not rewrite historical entries.

This targeted correctness fix did not execute the broader repository-wide documentation second pass.

### Known toolchain-document second-pass work

The completed toolchain historical recovery deliberately deferred current-document refinement.

Known items include:

* `TOOLCHAIN_WISHLIST.md` provenance is inconsistent across capability entries;
* the validity-aware persistent-knowledge material should identify KiroGraph/Nella explicitly rather than referring only to generic persistent-memory and assumption-tracking tools;
* relevant Wishlist entries should retain implementation pointers/back-references to the investigations that motivated them;
* MCP Filesystem safety annotations must be described as metadata/advisory semantics rather than technical authority;
* line/head/tail retrieval bounds must not be presented as hard token/context bounds;
* MCP Filesystem search should be distinguished as primarily path/filesystem discovery rather than semantic repository-content search;
* dynamic MCP Roots/runtime scope selection should be represented accurately if retained as a desired capability;
* journal filenames remain transitional and eventual `_JOURNAL` naming remains deferred;
* existing toolchain documents should not be moved into a prospective reusable-project root until the project-structure investigation provides a useful attachment/document topology.

The AI-toolchain investigation itself remains paused at its documentation checkpoint while this structure work proceeds.

### Known main-project second-pass work

The main Orthoptera documentation archaeology did not find further significant historical loss after recovery, but current-document consistency still requires review.

Known examples include:

* README/current-orientation material should be checked against the later neutral-event DESIGN and ROADMAP;
* current document purpose/authority/front matter should be made consistent with the eventual documentation model;
* cross-references and provenance should be checked after structural decisions are known.

Mutable documents should remain mutable; the second pass must not turn historical preservation into a requirement to preserve every superseded roadmap or README formulation in place.

### Structural work remains last relative to semantic decisions

Do not combine broad content refinement with repository moves/renames merely for convenience.

The preferred sequence remains approximately:

```text
recover evidence first pass      complete
        ↓
capture recovery case study      complete
        ↓
extract initial findings / decisions
                                complete
        ↓
research project structure,
attachments and agent semantics
        ↓
targeted guidance corrections
        ↓
repository-wide documentation pass
        ↓
finalise sub-project boundaries
        ↓
naming
        ↓
isolated moves / renames
        ↓
eventual real repository extraction
when evidence justifies it
```

This sequence may itself be revised by later project-structure findings. If so, record the revised understanding rather than rewriting this checkpoint.


---

## Candidate experiments arising from the extraction review

The initial extraction deliberately did not promote several recovery practices into durable findings or general decisions. The following bounded experiments could test the most material practices. They are candidates only; recording them here does not authorise their execution.

### Change-shape editing workflow experiment

Compare representative evidence-bearing documentation changes performed through:

1. direct EOF append with structural verification;
2. generated patch with syntax and deletion checks;
3. whole-document replacement with equivalent preservation instructions.

Measure:

* unintended deletions;
* omissions and duplicated blocks;
* provenance or qualification loss;
* patch/application failures;
* reviewer time;
* and defects detected before merge.

Vary append-only additions and refinements to existing text separately. This tests the broader validity of the recovery's direct-append preference, patch preference and zero-deletion checks without presuming that one workflow is universally best.

### Checkpoint and commit-granularity review experiment

Prepare equivalent recovery transformations in forms that:

1. retain a raw implementation-agent checkpoint;
2. separate mechanical restoration from structural adaptation;
3. combine the work into one otherwise equivalent commit.

Ask reviewers who did not perform the transformation to identify the historical source, explain the transformation and detect seeded loss or changed interpretation. Measure accuracy, review time and recoverability.

This tests the value of raw-agent checkpoints and restoration/adaptation commit separation. Retaining every recovery branch is not independently promoted; branch retention should be assessed only insofar as it materially changes reviewability or recovery.

### Documentation-transport robustness experiment

Where relevant chat or agent interfaces are still in scope, transport equivalent Markdown payloads containing nested triple-backtick fences using alternative outer delimiters and delivery mechanisms. Record truncation, delimiter corruption and rendering failures by tool and version.

This tests the four-backtick transport convention as a tool/version-specific reliability practice. If the relevant interfaces have changed or the failure cannot be reproduced, the historical record is sufficient and no general convention should be promoted.

### Practices without a separate experiment

Deliberately asymmetric paste-block sizes, leading blank lines on paste blocks and retaining all short-lived recovery branches do not currently justify standalone experiments. Their observed purpose and non-promotion are preserved in the extraction-review journal entry. They may be incorporated as variables in a broader workflow experiment if later evidence makes them material.
