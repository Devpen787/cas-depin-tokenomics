## V2 Chapter Iteration Heuristics

Status: synthesis control document  
Date captured: 2026-03-01  
Mode: `MODE: SYNTHESIS`

### Purpose

This file captures the chapter-iteration learnings that emerged while rebuilding V2 Chapters 1--4.

It exists so future chapter work does not depend on thread memory alone.

This is not a replacement for:
- the style guide,
- the quality gate,
- the claim ledger,
- or chapter contracts.

It is the practical layer that explains how to use those controls well during live chapter iteration.

### Governing Principle

The goal is not to make every chapter cleaner in the abstract.  
The goal is to make every chapter:
- more teachable,
- more defensible,
- more source-aware,
- and less mechanically “correct.”

If a revision makes prose smoother but makes the chapter harder to understand, less chosen in tone, or less faithful to the source hierarchy, reject it.

### 1. When the Current Stack Is Enough

Do not force GPT 5.2 into every chapter.

The current V2 stack is sufficient when:
- the chapter already lands on first read,
- the rationale for major turns is clear,
- the prose sounds chosen rather than auto-completed,
- density is helping explanation rather than hiding it,
- and the chapter is passing the gate for the right reasons.

In those cases, prefer:
- source review,
- claim-ledger control,
- style-guide review,
- quality-gate review,
- and targeted local revisions.

### 2. When GPT 5.2 Is Worth Using

Use GPT 5.2 selectively, not automatically.

Reach for it when a section is:
- correct but stiff,
- structurally sound but under-teaching,
- too abrupt at a major analytical turn,
- polished but generic,
- or mechanically tidy in a way that weakens reader pull.

Use it for:
- reader-first rewrites,
- transition alternatives,
- paragraph-level humanization,
- or light phrase testing.

Do not use it to:
- redesign architecture,
- rewrite roadmaps,
- redefine chapter sequencing,
- or silently alter the evidentiary role of a section.

### 3. Do Not Trade Teachability for Smoothness

This is one of the most important V2 lessons.

Smoother prose is not automatically better prose.

If a rewrite:
- weakens stance,
- removes explanatory context,
- replaces useful density with generic smoothness,
- or makes a chapter less teachable,

then reject it even if it sounds more polished.

### 4. Good Density vs Bad Compression

Do not treat all dense prose as a problem.

#### Good density

Keep density when it:
- carries real explanatory value,
- reflects source richness,
- teaches the mechanism more clearly,
- or gives the reader the context needed to understand later chapters.

#### Bad compression

Revise when density:
- collapses multiple jobs into one paragraph,
- introduces key terms before they are earned,
- makes the reader work harder without gaining understanding,
- or hides rationale behind compact academic phrasing.

The question is not “is this dense?”  
It is “is this density helping or hurting?”

### 5. Major Turns Must Feel Earned

A major analytical turn should not appear before the reader understands why it is appearing.

This applies especially to:
- research questions,
- contribution statements,
- methodological pivots,
- case-selection moves,
- and evidence-boundary transitions.

Before accepting a section, ask:
- Why here?
- Why this formulation?
- Has the section earned this move?

If not, add rationale before structure.

### 6. Form Must Serve Comprehension

Do not choose a form because it looks neat.

Choose the form that teaches best:
- prose,
- split prose,
- paragraph plus list,
- compact table,
- or figure.

This means:
- do not automatically turn three items into a list,
- do not automatically compress three items into one paragraph,
- and avoid bureaucratic list prose such as:
  - `bold label + period + explanation`

The right question is:
- what form helps the reader understand this fastest and most accurately?

### 7. Source Richness Before Reduction

Before compressing a source into thesis prose, mine it properly.

This was especially important for:
- Person B’s comparative tables,
- Person A’s foundations and Onocoy draft,
- and the wider Onocoy docs corpus.

The workflow should be:
1. source-preserving review,
2. identify what the source adds,
3. identify what belongs in main text / appendix / context / synthesis only,
4. only then reduce into chapter prose.

Do not reduce rich sources too early just because a chapter outline already exists.

### 8. Promote Now vs Park for Later

Not every useful fact should become a load-bearing thesis claim immediately.

Use this distinction actively:

#### Promote now
Promote items that:
- later chapters will clearly depend on,
- are strongly documented,
- are likely to recur in reasoning or model framing,
- or need explicit claim control now.

#### Park for later
Park items that:
- are interview-heavy,
- are contextually interesting but not yet necessary,
- are weakly supported,
- or may belong better in appendix, discussion, or later empirical/method chapters.

This keeps the thesis selective without discarding valuable context.

### 9. Evidence Layers Must Stay Separate

When chapter writing gets richer, evidence classes can blur.  
Do not let them blur.

For Onocoy, the distinction is:
- Tokenomics docs = primary ONO/DC flow source
- Explorer = operational/spatial transparency
- Dune = dated on-chain/accounting transparency
- Interview = bounded practitioner context
- Community/Ambassador material = ecosystem context
- Internal working memory = synthesis only

This chapter-iteration lesson generalizes:
- context can enrich,
- but it should not silently upgrade into mechanism fact.

### 10. Use Reviewer Judgment, Not Just Rule Compliance

If a section passes every formal check but still feels:
- dead,
- overly processed,
- oddly abrupt,
- or too tidy for what it is trying to teach,

stop and review it again.

The workflow is not meant to replace judgment.  
It is meant to focus judgment.

### 11. Practical Review Order for Later Chapters

For future chapters, use this review order:

1. source opportunity review  
2. chapter contract check  
3. claim-ledger alignment  
4. style-guide review  
5. quality-gate review  
6. reverse-outline or form-fit review if needed  
7. decide whether GPT 5.2 is actually necessary  
8. promote-now vs park-for-later review  
9. full-pass audit if the chapter is being closed

### 12. Default Rule for Future V2 Chapters

If the section is:
- understandable,
- source-rich,
- earned,
- and human on the page,

prefer targeted refinement over full rewrites.

If the section is:
- correct but not landing,
- abrupt at a key turn,
- or polished but generic,

then use the full rewrite-brief workflow.

### 13. Compaction and Handoff Rule

Assume context compaction will happen during long rebuild sessions.

To prevent re-deriving the live state from thread memory:
- maintain a small current-state baton in
  - [v2_active_handoff.md](/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_active_handoff.md)
- update that baton after each meaningful milestone
- use the baton to restart work in a fresh thread or after compaction

The baton should contain only:
- current branch
- chapters frozen so far
- current next chapter
- exact pending patch set
- active posture decisions
- parked items
- do-not-reopen notes

Do not rely on repeated narrated setup checks as a substitute for the baton.

`THESIS_OS.md` remains the controller of the thesis, but it should not be treated as a repeatedly narrated ritual at every small step. Re-check it when entering a new major phase or after genuine drift; otherwise rely on the baton plus the persisted control stack.
