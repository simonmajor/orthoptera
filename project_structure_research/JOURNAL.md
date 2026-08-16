# Project-Structure Research Journal

This is the append-only historical journal for completed investigations and their contemporary conclusions within the provisional project-structure sub-project. It is not the mutable plan and does not by itself establish current architecture or decisions.

## Journal invariants

In normal operation, add entries as direct, contiguous paste blocks at the end of this file. Do not rewrite, reorder or remove earlier entries to align them with later understanding. Later entries may qualify, supersede or contradict earlier interpretations while preserving the earlier evidence, uncertainty and provenance.

An entry records completed work in its contemporary epistemic state. It may therefore include implications, unresolved questions, speculation and possible follow-up work produced by that work. Such content remains historical evidence; it does not make the journal the mutable record of what is currently intended or sequenced. Later changes to current intent belong in `PLAN.md` and do not rewrite the earlier entry.

An entry should retain enough context to distinguish observation, documentation, inference and unknowns. Where relevant, it should identify the host project and repository, exact host revision, exact revision of this reusable project, exact revisions of other relevant reusable projects, and relevant tool, model and environment versions.

No final entry template or metadata syntax has been chosen. Until evidence supports one, preserve the required provenance in a clear human-readable form appropriate to the investigation.

## Entries

No completed project-structure investigation has yet been recorded here. The prior Orthoptera documentation-recovery history is deliberately deferred to a subsequent recovery phase rather than summarised into this seed.

---

## Recovered history — Orthoptera documentation recovery begins

**Host project:** Orthoptera
**Host repository:** `https://github.com/simonmajor/orthoptera`
**Recovery period represented by this entry:** 9–16 August 2026
**Recovered into this journal:** 16 August 2026
**Evidence used for this reconstruction:** Orthoptera Git history, recovered documentation, repository state captured during the recovery, and the architectural conversation that drove the work.

This entry reconstructs the documentation-recovery sequence that directly motivated this project-structure sub-project.

It is deliberately historical rather than a cleaned-up statement of current best practice. Later subsections record rules that were discovered only after earlier approaches failed.

### Trigger: a documentation checkpoint exposed knowledge loss

The immediate trigger was an attempted toolchain documentation checkpoint following the Nella investigation.

The requested checkpoint was intended to preserve the wider accumulated toolchain investigation.

The draft instead behaved partly like a replacement current-state summary:

* recent Nella conclusions were emphasised;
* earlier investigative detail and provenance were compressed;
* comparisons referred to tools by shorthand names while losing some pointers to what those tools actually were;
* planned and completed experiments were mixed;
* historical experiments risked disappearing when later understanding made their detail appear redundant.

The human review rejected that approach.

The key correction at this stage was:

> The toolchain experiment, findings and decisions documents were not merely current-state reference documents. They had become historical research records.

This changed the recovery objective from:

> improve the current toolchain documentation

to:

> recover the historical knowledge first, then redesign the documentation model without losing that history.

### Repository history became evidence

A large history capture was generated as `req2.txt`.

It contained:

* all current Markdown files;
* the complete `TOOLCHAIN_*.md` patch history;
* the wider Markdown patch history.

The regenerated capture on 9 August was approximately:

```text
12,665 lines
72,343 words
527,721 characters
```

A smaller `git log --stat` summary was later captured as `req3.txt`.

These files were recovery aids, not intended project documentation.

The exercise demonstrated that Git history is valuable archaeological evidence, but that relying on Git history as the *normal* way to recover project knowledge is expensive and unsuitable as a documentation strategy.

### First recovery principle: preserve before reorganising

The recovery discussion established an early sequencing rule:

```text
recover historical knowledge
        ↓
verify recovery
        ↓
separate historical and mutable roles
        ↓
refine structure
        ↓
rename / move last
```

Renames and moves were explicitly deferred so that Git history would remain intelligible and structural churn would not obscure knowledge recovery.

The same reasoning deferred possible folder reorganisation until the subordinate-`AGENTS.md` question had been investigated.

### Journals become explicit

Three toolchain documents were recognised as essentially journal-like:

* experiments;
* findings;
* decisions.

The intended future model became:

* historical journal entries are preserved;
* new historical entries are appended;
* later understanding does not rewrite earlier evidence;
* mutable current planning lives separately;
* a completed historical entry may still contain the implications, open questions and possible follow-up work understood at that time.

The experiment record was also conceptually narrowed toward **completed experiments**, while a separate mutable planned-experiment sequence was introduced.

At this stage the terminology and exact filenames were still evolving.

The important change was semantic:

> historical record and current intent are different kinds of project state.

### Initial recovery commits

The recovery was intentionally split into small commits so that each class of restored knowledge could be inspected independently.

Significant checkpoints included:

```text
5d6ad75  Strengthen documentation and knowledge capture guidance
6f02e2c  Recover toolchain findings and provenance
daa014c  Recover toolchain experiment history and evidence
26538cc  Recover toolchain decisions and provenance
bf48862  Recover toolchain wishlist and capability vocabulary
f645d3f  Clarify agent instruction hierarchy and context boundaries
```

The sequence recovered substantial material that had become compressed or vulnerable in prior whole-document rewrites.

The work also strengthened `AGENTS.md` and `CONTRIBUTING.md` so that documentation preservation became an explicit agent/workflow concern rather than merely a conversational preference.

### A major failure during the recovery itself

The recovery then reproduced the same class of error it was meant to repair.

A restructuring commit:

```text
ddd7d7e  Establish journal and planned-experiment documentation structure
```

reported:

```text
446 insertions(+)
1195 deletions(-)
```

across the affected toolchain documentation.

The net loss was immediately recognised as implausibly large for a change whose purpose was to establish journal structure while preserving history.

This was a critical event in the evolution of the project.

The problem was not simply a bad individual edit.

The failure exposed a systematic weakness in the working method:

```text
whole-document replacement drafting
        +
AI preference for concise synthesis
        +
evolving document roles
        ↓
large accidental historical deletion
```

The fact that this happened *during an explicit recovery for earlier knowledge loss* demonstrated that discursive instructions such as "preserve knowledge" were not strong enough on their own.

### Explicit preservation invariants

The response was to strengthen the repository guidance into explicit invariants rather than relying on tone or general intent.

A subsequent commit:

```text
3bebdf6  Strengthen documentation preservation invariants
```

made preservation constraints much more formal.

The resulting rules included concepts such as:

* historical preservation;
* evidence preservation;
* provenance preservation;
* interpretation preservation;
* journal immutability;
* restructuring without information loss;
* no implicit deletion merely because material is recoverable elsewhere;
* uncertainty preservation;
* checkpoints as knowledge-preservation operations.

One important later correction was that the initial "planning-separation invariant" was too strong if interpreted literally.

The refined rule became:

> A journal records completed work in its contemporary epistemic state and may preserve implications, speculation, unresolved questions and possible follow-up work. A mutable plan records what is currently intended or sequenced.

This distinction was later encoded explicitly in the project-structure bootstrap.

### Mechanical recovery replaces redrafting

After the failed restructuring commit, the recovery method became more mechanical.

For the completed-experiments journal, the pre-restructure version was restored from Git and then adapted minimally.

A key recovery commit was:

```text
b541ce9  Recover completed toolchain experiment journal
```

The operation restored the earlier historical body rather than asking an AI to resynthesise it from memory.

This led to another important principle:

> When historical material already exists in Git, restore it mechanically where practical; do not recreate it through summarisation.

The same approach was applied to other toolchain records.

### Restoration commits as explicit historical steps

For later recovery work, restoration and adaptation were sometimes separated into distinct commits.

For example, the decisions recovery used:

```text
179612d  Restore historical toolchain decisions
02f0d86  Adapt recovered toolchain decisions to journal structure
```

This made the transformation path visible:

```text
known historical source
        ↓
mechanical restoration
        ↓
small structural adaptation
```

rather than hiding both operations inside a single opaque rewrite.

The value of the intermediate restoration commit was primarily forensic and review-oriented: it allowed the evolution from the same historical starting point to be compared directly.

### Editing workflow evolved by change type

The recovery gradually converged on two different editing workflows.

#### Append-only journal changes

For strict EOF journal additions, direct paste became preferable to generating a patch.

The checks were lightweight:

```text
wc -lwc before
paste at EOF
wc -lwc after
git diff --check
git diff --numstat
git diff --stat
git status
```

The strongest invariant for an append-only operation was:

```text
deletions = 0
```

Multi-block pastes introduced a separate human failure mode: one block could be duplicated while another was omitted.

The mitigation became:

* deliberately asymmetric block sizes;
* cumulative `git diff --numstat` between paste sessions;
* paste blocks beginning with a blank line;
* final zero-deletion verification.

#### Refinements to existing text

For edits to existing material, direct replacement text was judged too risky.

The preferred workflow became:

```text
AI supplies or helps construct a patch
        ↓
human reviews patch
        ↓
git apply --check
git apply --stat / --numstat
        ↓
apply
        ↓
git diff --check
git diff --stat
```

The important distinction was:

> Append operations are structurally simple enough to verify by shape. Refinements require review of what is being removed or replaced.

### Patch-generation failures also became evidence

Hand-authored unified diffs produced their own failures.

One patch had an incorrect hunk header and failed with:

```text
error: corrupt patch
```

The apparent diff statistics could still look plausible even though `git apply --check` rejected the patch.

This established that:

* `diffstat` is useful for human orientation;
* `git apply --stat` is useful only for a syntactically valid patch;
* `git apply --check` is an essential gate;
* hunk arithmetic should be generated mechanically rather than counted by an AI where possible.

A later attempt to transport long Markdown through a shell here-document also failed in the chat UI.

The actual cause was not the here-document itself: nested triple-backtick Markdown fences terminated the assistant's outer triple-backtick code block.

The same failure recurred when the payload was presented as a normal fenced Markdown block.

The robust transport convention became:

> Use an outer four-backtick fence when the payload itself contains triple-backtick Markdown fences.

This was a presentation-layer failure rather than a Git failure, but it materially affected the reliability of the human/AI editing workflow.

### Recovery branches become the default safety boundary

As the recovery became more complex, changes were moved onto short-lived recovery branches before being merged back to `main`.

A typical sequence became:

```text
clean main
        ↓
create recovery branch
        ↓
restore / append / refine
        ↓
commit
        ↓
push branch
        ↓
remote review against main
        ↓
fast-forward merge
```

Branches were retained until the wider recovery completed.

This produced several benefits:

* the raw recovery result could be inspected remotely;
* a bad recovery did not immediately alter `main`;
* multiple recovery commits could preserve mechanical restoration and later adaptation separately;
* GitHub comparison statistics provided a cheap independent check of file scope and deletion counts.

### Toolchain history recovered chronologically

The toolchain journals were then extended to recover later investigations that had occurred after the earlier journal history.

These included:

* focused MCP Filesystem and Tier-1 file-search investigations;
* KiroGraph;
* Nella's first pass;
* the KiroGraph comparison refinement;
* the adversarial Nella second pass.

The recovery deliberately preserved the *evolution* of interpretation.

For example, Nella was not rewritten directly into its final conservative conclusion.

The journal retained the progression from:

```text
potentially distinctive validity-aware Level-4C mechanism
        ↓
specialised implementation within KiroGraph's Level 4C
        ↓
adversarial conclusion:
no new Orthoptera capability boundary demonstrated
```

This became an example of the interpretation-preservation invariant in practice.

### Findings were recovered separately from experiments

The recovery then appended durable findings rather than treating the experiment journal as the only persistent record.

KiroGraph led to the persistent-knowledge vocabulary:

```text
Level 4A — persistent structural representation
Level 4B — persistent semantic representation
Level 4C — persistent project/agent knowledge
```

Nella then refined Level 4C by demonstrating an explicit validity/invalidation lifecycle without establishing a new capability boundary.

The distinction between experiment history and durable findings was preserved rather than collapsing both into a single summary.

### Main-project archaeology followed the toolchain recovery

Once the toolchain recovery was stable, the same knowledge-loss concern was applied to Orthoptera's main project documentation.

The audit classified documents according to role rather than assuming every deletion was bad.

`EXPERIMENTS.md` was found to have evolved append-only in substance and required no historical recovery.

`DESIGN.md` had undergone a substantial replacement, but the old fixed chirp-oriented design had been deliberately superseded after experimental evidence invalidated its universality. The evidence and rationale survived elsewhere, so this was treated as specification evolution rather than lost historical evidence.

`ROADMAP.md` and `README.md` were recognised as intentionally mutable current-state/orientation documents. Their historical text did not automatically require preservation in place.

`DECISIONS.md` was different.

An earlier whole-document rewrite had removed two genuine decisions:

* the original DTW-on-chirp-envelope decision and its rationale/alternative;
* the explicit decision to restrict the initial Xeno-canto development corpus.

Those decisions were recovered by an append-only journal entry on a branch and merged without deleting the later refined decisions.

The audit therefore demonstrated another important rule:

> Whether removed text represents knowledge loss depends on the semantic role of the document, not merely on the existence of deletions.

### Historical recovery first-pass checkpoint

After the toolchain and main-project archaeology, the project considered the historical knowledge recovery first pass complete.

The remaining work was explicitly reclassified as:

* documentation design/refinement;
* repository structure;
* naming;
* cross-references;
* front matter;
* attachment architecture;
* eventual moves/renames.

This prevented a second-pass cleanup from being confused with historical recovery.

### The recovery itself becomes a reusable research subject

While the recovery was underway, it became clear that the documentation problem was broader than Orthoptera.

The emerging questions included:

* how AI agents discover repository instructions;
* how historical and mutable project knowledge should be separated;
* how reusable templates can seed a project without later overwriting host-owned knowledge;
* how an existing repository can adopt improved structure without losing accumulated context;
* how reusable AI infrastructure should attach to more than one development project.

The toolchain investigation had already become a de facto sub-project.

The same conclusion was reached for project/documentation structure.

The long-term goal became two reusable peer projects:

```text
AI toolchain
AI project/repository structure
```

initially emulated inside Orthoptera but eventually capable of becoming independently attachable repositories.

The most important long-term requirement was identified as **host attachability**:

> A fresh or existing development repository should be able to attach the reusable AI projects and obtain their tooling, guidance, templates and skills without surrendering ownership of its own accumulated project knowledge.

### New-host and existing-host use both matter

The original mental model emphasised attaching reusable infrastructure when creating a new project.

During discussion, an equally important case emerged:

> attach reusable AI infrastructure to an already mature repository with source, documentation, history and external relationships.

The Orthoptera recovery itself became an obvious founding case study for that existing-host path.

This is why the present journal reconstructs the recovery before recording new attachment experiments.

### Attachment revision and evidence provenance separate

A tension was identified between the expected update rates of the reusable projects.

The AI-toolchain project may need to evolve quickly because relevant tooling appears frequently.

A host might intentionally track or regularly pull a newer toolchain state.

The project-structure repository is expected to evolve much more slowly once mature.

This established a conceptual separation:

```text
attachment identity
attachment mechanism
attachment update policy
evidence provenance
```

A host may advance an attachment.

A historical experiment must still preserve the exact revisions under which its evidence was produced.

That requirement motivated the provenance guidance in this journal's seed.

### Recursive peer dependency must not become recursive physical nesting

The reusable projects may logically depend on one another:

```text
ai-toolchain uses project-structure guidance
ai-project-structure uses toolchain capabilities
```

Naively encoding that through physical nested attachments would create recursion.

The emerging requirement was instead:

> reusable projects are peers; logical reciprocal use must not imply recursive physical containment.

Symlinks or other emulation mechanisms were left as possibilities only if later tooling evidence justified them.

### Provisional sub-project bootstrap

The minimal bootstrap was intentionally conservative.

It created only:

```text
project_structure_research/
    AGENTS.md
    JOURNAL.md
    PLAN.md
    README.md
```

No existing toolchain documents were moved.

No scripts were created.

No final attachment mechanism, metadata schema, repository name or document topology was selected.

The purpose was to create enough of a boundary for this investigation to begin preserving its own history before deciding its final structure.

### ChatGPT → Codex handoff exposed workspace-context limits

The bootstrap also produced immediate evidence about AI-agent handoff semantics.

A ChatGPT desktop handoff to Work/Codex was attempted with a detailed repository task.

The new Codex task did **not** inherit the local Orthoptera checkout.

It started in a generic ChatGPT project workspace containing only generated guidance and no Orthoptera repository.

Codex correctly refused to perform the requested repository changes.

This established an observed distinction:

```text
architectural/task context transfer
        ≠
local implementation workspace transfer
```

The task had to be relaunched explicitly from the Orthoptera repository workspace.

This is relevant to reusable project attachment because apparent UI integration between AI tools must not be assumed to imply shared repository context, filesystem state or workspace selection.

### Raw Codex bootstrap preserved before review

Once relaunched in the correct workspace, Codex produced a small bootstrap change.

Before manual correction, that raw result was committed on:

```text
restructure/ai-project-structure-bootstrap
```

as a checkpoint.

The raw result added four files and did not modify existing Orthoptera or toolchain documentation.

This preserved the implementation agent's unmodified output for architectural review.

### Subordinate instruction existence did not establish discovery

Architectural review found one important flaw.

Codex created:

```text
project_structure_research/AGENTS.md
```

and defined reasonable local/conflict semantics.

However, the root `AGENTS.md` had explicitly required that subordinate instruction discovery be established before introducing subordinate instruction documents.

The bootstrap had implicitly assumed discovery rather than making it operational.

A second Codex commit therefore added an explicit root instruction:

> work scoped to the provisional `project_structure_research/` area must read its subordinate `AGENTS.md`.

The text also made clear that this was only a provisional explicit discovery path, not a general conclusion about automatic subordinate-instruction discovery.

This produced an early project-structure finding candidate:

> **The existence of a scoped instruction file and the reliable discovery of that file are separate properties.**

### Journal/planning semantics were corrected in the bootstrap

The same review noticed that the repository still contained an over-broad older planning-separation statement.

The new sub-project documentation was refined to encode the newer rule:

* journals preserve completed work in its contemporary epistemic state;
* that state may include implications, unresolved questions, speculation and possible follow-up work;
* `PLAN.md` contains mutable current intent and sequencing;
* later changes to current intent do not rewrite the historical journal.

The raw bootstrap commit and its review/refinement commit were both retained and then fast-forward merged to `main`.

### State at the end of this reconstructed history

At the time this history was recovered into the new journal:

* the historical knowledge recovery first pass for Orthoptera and its toolchain was considered complete;
* the toolchain investigation was paused at its checkpoint;
* this project-structure investigation had a minimal provisional boundary;
* no final repository attachment mechanism had been chosen;
* no bootstrap/audit/migration script existed;
* the next intended work was to extract durable findings and decisions from this recovery history, then begin new attachment research.

This recovery sequence is itself evidence.

It should not be treated as proof that every practice developed during it is optimal.

The purpose of preserving it here is to make those practices, failures and changes in understanding available for later analysis rather than requiring them to be reconstructed again from Git history and conversation logs.


---

## Extraction review — findings, decisions and unpromoted recovery practices

**Host project:** Orthoptera  
**Host repository:** `https://github.com/simonmajor/orthoptera`  
**Review date:** 17 August 2026  
**Repository revision reviewed:** `f8cd0aaf9450e632cbd23c5f1862b9f560631466` on `main`  
**Evidence reviewed:** This journal, the provisional sub-project instructions, README and plan, root `AGENTS.md` and `CONTRIBUTING.md`, and the current role/invariant sections of the Orthoptera toolchain journals and planned-experiment sequence.

### Purpose and method

This was the first bounded extraction review of the recovered Orthoptera documentation-recovery case study.

The review divided the recovered sequence into its causal episodes: the triggering knowledge loss, failed whole-document restructuring, mechanical restoration, change-specific editing workflows, main-project archaeology, reusable-project requirements, workspace handoff and subordinate-instruction discovery.

Candidate claims were classified as:

* observed or documented evidence;
* durable finding;
* actual decision;
* recovery practice;
* hypothesis;
* unresolved question;
* or current requirement.

A finding required supporting evidence, bounded scope, limitations and provenance. A decision required an actual adopted choice or requirement rather than an observation, candidate mechanism or practice that happened to work.

### Findings promoted

The evidence justified creating `FINDINGS.md` and promoting these initial findings:

* document role determines whether deletion is knowledge loss;
* historical epistemic state and mutable current intent are distinct project state;
* whole-document AI synthesis is hazardous for evidence-bearing documentation within the demonstrated scope;
* instruction-file existence and reliable instruction discovery are separate properties;
* task-context transfer and repository-workspace transfer are separate;
* and moving attachment state and historical evidence provenance must remain independent.

The entries preserve their evidence, scope and limitations rather than presenting the recovery case as universal proof.

### Decisions promoted

The evidence justified creating `DECISIONS.md` and promoting these actual decisions or adopted requirements:

* recover and verify historical knowledge before broad structural reorganisation;
* separate append-only historical journals from mutable planning;
* maintain a minimal provisional research boundary without prematurely selecting mechanisms;
* treat new-host and existing-host adoption as first-class paths;
* make instantiated documentation host-owned;
* keep the project-structure and AI-toolchain projects as conceptual peers without recursive physical containment;
* keep attachment identity, physical mechanism, update policy and evidence provenance distinct;
* and provide an explicit provisional root discovery path for the subordinate `AGENTS.md`.

No attachment mechanism, final repository location, update policy, metadata syntax, bootstrap interface or final topology was promoted as decided.

### Practices deliberately not promoted

The review explicitly declined to promote these recovery practices into durable findings or general decisions:

* deliberately asymmetric paste-block sizes;
* beginning paste blocks with a blank line;
* retaining every short-lived recovery branch until a larger exercise completes;
* always preserving raw implementation-agent output as a commit;
* always preferring direct EOF paste over a generated patch;
* always separating mechanical restoration and structural adaptation into different commits;
* and using four-backtick outer fences as a general repository-wide convention.

These practices responded to real failure modes, but the recovered evidence does not establish that each mitigation generalises beyond its workflow and tool context.

Their exclusion is deliberate rather than accidental. The practices and their purposes remain recoverable in the earlier journal entry and in this review.

### Candidate validation experiments

The review found obvious bounded experiments for the most material non-promoted practices and added them to the end of `PLAN.md`:

* compare direct append, generated patch and whole-document replacement across append-only and existing-text changes;
* compare raw checkpoints and restoration/adaptation commit separation against an equivalent combined transformation;
* and test nested Markdown-fence transport across relevant tools and versions where the earlier failure remains reproducible.

Asymmetric block sizes, leading blank lines and universal branch retention do not currently justify standalone experiments. They may be variables in broader workflow experiments if later evidence makes them material.

These are candidate experiments only. Recording them does not authorise their execution.

### Recovery first-pass terminology

The documentation sweep established that earlier statements describing historical recovery as `complete` referred to completion of the recovery first pass, not completion of all recovery-derived documentation work.

This journal entry records that clarification. As a narrow exception to normal journal immutability, the earlier checkpoint heading and two completion statements in this reconstructed entry were refined to say `recovery first pass` explicitly. The change clarifies their intended contemporary meaning; it does not remove evidence or replace the earlier interpretation with a new one.

The broader recovery-derived documentation second pass remains outstanding. Its scope includes current-document consistency, authority and purpose, provenance, cross-references, duplication, misplaced material, residual knowledge-loss checks, subordinate-instruction semantics, structural research, naming and eventual isolated moves.

### Targeted current-guidance correction

The review confirmed that root `CONTRIBUTING.md` contained an over-broad planning-separation invariant. It could be read as excluding implications, hypotheses, unresolved questions, speculation and proposed follow-up work from completed-work journals.

The invariant was narrowly reconciled with the established journal model. This targeted correctness fix does not execute the broader documentation second pass.

### Resulting state

At this checkpoint:

* the initial findings and decisions extraction is complete;
* dedicated findings and decisions journals now exist;
* non-promoted practices and candidate validation experiments are explicitly recorded;
* the recovery first-pass/second-pass distinction is explicit;
* the root planning-separation defect is corrected;
* and the broader research, experiments and documentation second pass remain planned but unexecuted.
