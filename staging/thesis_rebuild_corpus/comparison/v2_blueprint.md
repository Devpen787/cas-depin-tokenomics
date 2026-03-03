# V2 Blueprint

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

V2 is a controlled recomposition of the thesis, not a cleanup pass and not a literal rewrite from memory. The current thesis, rebuild corpus, uploaded assets, and Person A/B/C materials are treated as mined intelligence. The V2 thesis should read like an intentionally composed submission document rather than a record of live discovery.

## V2 Objective

V2 should deliver:

1. cleaner argument flow
2. cleaner chapter boundaries
3. cleaner claim discipline
4. cleaner visual grammar
5. cleaner authorship and readability
6. lower formatting friction during drafting

## Non-Negotiables

These remain fixed unless explicitly revised:

1. `THESIS_OS.md` remains the governing operating system for the thesis.
2. DTSE remains the canonical simulation engine name.
3. The Golden Thread remains the macro argument order:
   - Foundations
   - Theoretical Framework
   - Empirical Case (Onocoy)
   - Empirical Analysis
   - Methodology (DTSE)
   - Results
   - Discussion / Conclusion
4. Submission text must not render internal workflow artifacts by default.
5. Mechanism facts, modeled assumptions, DTSE outputs, and interpretation must remain distinguishable.

## Design Principles

1. Compose globally, not surgically.
2. Route each major concept to one canonical home.
3. Build visuals as part of argument design, not as late-stage decoration.
4. Use rich context to shape explanation, but not to carry unsupported load-bearing claims.
5. Humanize the prose without weakening evidence discipline.
6. Separate planning, drafting, and submission surfaces.

## Source Architecture

V2 uses a three-layer source model.

### 1. Evidence Layer

Use for load-bearing thesis claims.

- peer-reviewed papers
- protocol documentation
- official governance records
- frozen DTSE artifacts
- auditable datasets
- verified tables and figures already grounded in the thesis

### 2. Context Layer

Use to think, explain, orient the reader, and improve flow before citation closure.

- transcripts
- blogs
- dashboards
- market notes
- interviews
- old thesis drafts
- NotebookLM reformulations
- user observations and working hypotheses

Rule:
- context may shape writing and section design
- context may not carry a final load-bearing claim unless later upgraded into the evidence layer

### 3. Design Layer

Use to build the thesis object well.

- slide decks
- mindmaps
- chart styles
- legends
- table structures
- layout patterns
- explanatory visuals

Rule:
- design assets influence presentation, sequencing, and narrative architecture
- design assets are not thesis evidence anchors by default

## Drafting / Build Workflow

V2 should not be drafted entirely inside the final LaTeX surface.

### Surface Model

1. Planning surface
   - blueprint documents
   - claim-routing notes
   - keep / rewrite / drop decisions
   - figure / table registry

2. Drafting surface
   - markdown or doc-compatible rough section drafts
   - section experiments
   - prose reshaping before LaTeX hardening

3. Submission surface
   - canonical LaTeX chapter files
   - citations
   - appendix
   - figure / table numbering
   - final PDF build

### Workflow Rule

Do not solve discovery-stage writing problems inside the final submission surface unless the section contract is already stable.

## Humanization System

The V1 thesis suffered from over-constrained, overly compact, and mechanically repetitive prose. V2 must correct this intentionally.

### New Writing Rules

1. One paragraph, one job.
2. Explain before compressing.
3. Difficult concepts get one concrete example before abstraction where useful.
4. Vary sentence length and rhythm.
5. Do not force identical paragraph sizes or fixed sentence counts.
6. Use analogy only when it clarifies a hard concept.
7. Transitions must connect ideas, not just sections.
8. Remove repeated AI-style framing formulas.
9. Break overpacked sections even if they are technically correct.
10. If a section feels mechanically symmetrical, rewrite it.

### Humanization Pass

A dedicated late-stage pass must:

- remove AI texture
- reduce sentence pattern repetition
- restore natural transitions
- insert context or examples where comprehension is thin
- align the prose voice across Person A, B, and C contributions
- preserve the thesis lexicon while relaxing rigid stylistic artifacts

## Dual-Model Writing Strategy

V2 should explicitly use a split between structural control and prose improvement.

### Codex / Current Model

Primary responsibilities:

- architecture and chapter design
- claim routing
- evidence discipline
- LaTeX integration
- figure / table system
- compliance and QA
- final acceptance / rejection of drafted text

### GPT 5.2

Primary responsibilities:

- prose improvement
- humanization
- transition rewriting
- explanation expansion
- sentence variation
- analogy generation where useful
- reducing mechanical or over-compressed writing patterns

### Role Boundary

GPT 5.2 should be treated as a writing improver, not as the source of structural truth or evidence authority.

Its outputs should be treated as context-layer draft text until they are:

1. checked against chapter contracts
2. checked against claim-class boundaries
3. checked against lexicon consistency
4. checked against evidence and citation discipline
5. integrated into the canonical LaTeX build by Codex

### Best Use Cases for GPT 5.2

1. sections that feel too compressed
2. sections with repetitive sentence rhythm
3. transitions between major concepts or chapters
4. explanations needing clearer examples or analogies
5. passages that are technically correct but do not yet read naturally

### Do Not Delegate to GPT 5.2

1. architecture decisions
2. chapter contracts
3. evidence hierarchy decisions
4. citation closure
5. final mechanism wording where protocol precision is critical
6. final acceptance of thesis-safe prose

## Figure / Table System

Every figure and table must do one clear job:

1. define
2. compare
3. diagnose
4. evidence
5. audit

### Main Text Visual Spine

The likely V2 visual spine should include:

1. CPS / coordination-loop figure
2. stress-factor definition table
3. comparator archetype table
4. sink / accrual typology table
5. Onocoy mechanism figure
6. empirical stress-window table
7. DTSE architecture figure
8. scenario-grid table
9. four stress-channel charts
10. cross-profile comparison figure
11. signal-timing figure
12. cross-scenario synthesis table
13. failure-signature matrix
14. limitation-to-claim map

### Visual Style Rules

1. The same colors must always represent the same metric families.
2. Legends should follow one fixed ordering.
3. Captions must explain analytical relevance, not just describe content.
4. Each figure / table should be followed by a short interpretation block when needed.
5. Audit-heavy tables should move to the appendix unless they are essential to the main argument.

## V2 Macro Architecture

V2 keeps the Golden Thread order but rebuilds chapter internals from scratch.

1. Introduction and Research Contract
2. Foundations: DePIN as a Cyber-Physical System
3. Comparative Tokenomic Framework
4. Onocoy as the Anchor Case
5. Empirical Stress Layer
6. DTSE Methodology
7. Results
8. Discussion, Limitations, Conclusion

## Build Sequence

The writing order should not equal the reading order.

### Writing Order

1. lock chapter contracts
2. lock figure / table registry
3. lock keep / rewrite / drop matrix
4. lock methodology and results skeleton
5. rebuild Onocoy anchor and empirical bridge
6. rebuild comparative framework
7. rebuild foundations and introduction
8. rebuild discussion and conclusion
9. run humanization pass
10. run final evidence / formatting QA

### Reading Order

Reading order should remain optimized for the final reader and defense committee, not for author convenience.

## Error Prevention Rules

To avoid V1 failure patterns:

1. no chapter drafting before chapter contracts are locked
2. no direct copy-paste from raw corpus into thesis chapters
3. no mixed claim classes inside one paragraph if that can be avoided
4. no late-stage figure dumping
5. no formatting rule creation without clear necessity
6. no local edit that creates global drift
7. no use of unsourced context as hidden evidence

## What V2 Can Exploit

V2 has advantages unavailable during V1:

1. Person C logic is already mature.
2. Person A and Person B materials are close to completion.
3. The rebuild corpus now preserves canonical keepers, duplicates, risks, and planning assets.
4. Uploaded comparative drafts are richer than the current framework chapter in raw comparative detail.
5. Uploaded visuals provide stronger narrative and figure-design patterns than parts of the current prose.
6. The current thesis already exposed where structure, flow, and explanation broke down.

## Success Criteria

V2 is successful if it:

1. reads as one authored document
2. has one lexicon and one argument path
3. eliminates visible retrofits and duplicated explanations
4. keeps evidence discipline without starving the prose of context
5. feels more teachable and more defensible than V1
6. reduces formatting friction during drafting and review

## Immediate Next Deliverables

The next synthesis artifacts should be:

1. `v2_chapter_contracts.md`
2. `v2_claim_routing_map.md`
3. `v2_figure_table_registry.md`
4. `v2_keep_rewrite_drop_matrix.md`
5. `v2_workflow_playbook.md`
