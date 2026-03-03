# V2 Workflow Playbook

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This playbook defines how the V2 rebuild should actually be executed across planning, drafting, LaTeX integration, preview, review, and final QA. Its job is to reduce workflow friction while preserving a clean canonical submission build.

## Core Workflow Principle

Do not force discovery-stage or heavy-restructuring work directly into the final LaTeX surface unless the chapter contract is already stable.

V2 uses three surfaces:

1. planning surface
2. drafting surface
3. submission surface

## 1. Planning Surface

### What belongs here

- blueprint documents
- chapter contracts
- claim-routing map
- figure / table registry
- keep / rewrite / drop matrix
- source triage notes
- rebuild sequence decisions

### Files

Planning artifacts should live under:

- `staging/thesis_rebuild_corpus/comparison/`
- `staging/thesis_rebuild_corpus/normalized/`

### Rule

No chapter rewrite begins until the planning artifacts for that chapter are stable enough to route concepts and visuals cleanly.

## 2. Drafting Surface

### What belongs here

- rough prose experiments
- rewritten section blocks
- humanized explanatory versions
- alternative transitions
- section-specific notes before LaTeX hardening

### Suggested formats

- markdown
- doc-compatible text
- structured notes for later LaTeX insertion

### Rule

This surface is for writing freedom and readability improvement. It is not the canonical citation / numbering / appendix source.

## 3. Submission Surface

### What belongs here

- `main.tex`
- `sections/*.tex`
- `bibliography.bib`
- final figures / tables
- appendix materials

### Rule

LaTeX remains the canonical submission source. Final numbering, citations, cross-references, appendix control, and PDF output live here.

## Rebuild Sequence

### Phase 1: Lock Design

1. freeze blueprint
2. freeze chapter contracts
3. freeze claim routing
4. freeze figure / table registry
5. freeze keep / rewrite / drop matrix
6. confirm compliance rules from `thesis_submission_rules_v2.md`

### Phase 2: Source and Visual Preparation

1. identify chapter source pools
2. identify required evidence upgrades
3. identify context-only material
4. identify needed figure / table redesigns

### Phase 3: Draft in Controlled Order

Recommended writing order:

1. methodology skeleton
2. results skeleton
3. Onocoy anchor
4. empirical bridge
5. comparative framework
6. foundations
7. introduction
8. discussion / conclusion

Reason:
- methodology and results are already the most mature intellectual core
- earlier chapters can then be written with knowledge of what the thesis actually demonstrates

### Phase 4: LaTeX Integration

1. integrate rewritten sections into `sections/*.tex`
2. update figures / tables
3. update citations
4. compile and inspect after each meaningful integration block

### Phase 5: Humanization Pass

1. remove AI texture
2. reduce repetitive sentence structures
3. improve examples and transitions
4. normalize voice across Person A / B / C sections
5. break overcompressed paragraphs

### Phase 6: Final QA

1. clean compile
2. no unresolved citations / refs
3. no placeholders
4. figures/tables all referenced
5. bibliography integrity check
6. AI disclosure check
7. declaration / title page / classification check
8. Arbeitsjournal completeness check

## Practical Working Rules

### Writing Rules

1. One paragraph, one job.
2. One canonical home per concept.
3. Separate claim classes as cleanly as possible.
4. Use context to explain, not to smuggle in unsupported claims.

### Formatting Rules

1. Do not invent formatting rules unless they improve compliance or readability.
2. Do not over-optimize typography while architecture is still unstable.
3. Fix layout and polish only after section logic is stable.

### Review Rules

1. Review for argument flow before polishing style.
2. Review for duplication before refining transitions.
3. Review visuals for analytical role, not just aesthetics.
4. Review claims for class separation before final citation closure.

## Preview and Compile Strategy

The pain in V1 came partly from slow feedback during LaTeX iteration. For V2:

1. avoid doing large discovery writing directly in LaTeX
2. integrate into LaTeX in controlled chunks
3. compile after each meaningful integration block
4. review PDFs for layout only after section content is stable enough

The goal is to make LaTeX the finishing environment, not the place where conceptual exploration gets trapped.

## Humanization Protocol

Every major rewritten chapter must pass a humanization check:

1. Does it sound authored rather than generated?
2. Are the sentences rhythmically varied?
3. Are difficult ideas explained rather than merely compressed?
4. Is there enough context for a non-specialist academic reader?
5. Does the section transition naturally to the next one?

If the answer is no to multiple items, the prose is not ready even if technically correct.

## Dual-Model Workflow

V2 should explicitly use GPT 5.2 as a prose-improvement copilot while keeping Codex as the structural and compliance controller.

### Codex Responsibilities

- decide what each chapter and section must do
- maintain claim routing
- maintain evidence discipline
- maintain figure / table logic
- maintain LaTeX integration and build hygiene
- accept or reject rewritten prose before it enters the submission surface

### GPT 5.2 Responsibilities

- rewrite for readability
- improve transitions
- expand thin explanations
- reduce repetitive sentence structure
- propose analogies or clearer examples
- smooth combined multi-author text into more natural prose

### Operating Rule

GPT 5.2 output is not thesis-ready by default. It is treated as draft text in the context layer until Codex validates it against:

1. the chapter contract
2. the claim-routing map
3. the lexicon in `THESIS_OS.md`
4. citation and evidence discipline
5. formatting / integration constraints

### Best Times to Use GPT 5.2

1. after section logic is stable but before final LaTeX hardening
2. during the dedicated humanization pass
3. when a section is technically correct but still sounds mechanical
4. when multi-author text has uneven voice or rhythm

### Unsafe Uses of GPT 5.2

Do not use GPT 5.2 as the final authority for:

1. mechanism definitions
2. empirical claims
3. DTSE claim boundaries
4. citation decisions
5. chapter architecture
6. compliance interpretation

### Quality Gate After GPT 5.2 Use

After any GPT 5.2 rewrite, Codex should verify:

1. no new unsupported claims were introduced
2. no mechanism drift occurred
3. no citation-shaped placeholders were invented
4. the prose still matches the chapter's analytical job
5. the text remains thesis-safe and lexically consistent

## Role of Uploaded Assets

### Text uploads

- use as comparative or narrative source reservoirs
- do not paste directly into chapters

### Slide decks and images

- use for figure design, narrative sequencing, and visual simplification
- do not treat as primary evidence by default

## Compliance Integration

This workflow must remain aligned with:

- `thesis_submission_rules_v2.md`
- `THESIS_OS.md`
- `v2_chapter_contracts.md`

## Stop Conditions

Pause rebuild drafting if:

1. a chapter contract becomes unclear
2. a key mechanism fact lacks verification
3. multiple chapters begin to explain the same concept in full
4. figure / table design starts driving argument structure instead of supporting it
5. formatting work is consuming attention before architecture is stable

## Success Condition

The workflow is working if:

1. chapter rewrites feel easier rather than more chaotic
2. each section has a visible job
3. figures / tables are planned before prose locks
4. humanization is improving readability without weakening rigor
5. LaTeX integration is the final hardening step, not the place where structural discovery still happens
