## V2 Rewrite Brief Template

Status: synthesis control template  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This template is used when handing a section to GPT 5.2 for a reader-first rewrite.

Its job is to improve readability, humanization, pacing, and sentence rhythm without allowing structure drift, claim inflation, or architecture redesign.

Core instruction:

**You are rewriting prose, not architecture.**

### Template

#### 1. Mission

State what the section must make the reader understand or feel.

Include:

1. the core tension,
2. the desired reader effect,
3. the role of the section in the chapter.

#### 2. Frozen Elements

List what must not change.

Typical items:

1. subsection names,
2. chapter order or roadmap logic,
3. research question wording,
4. fixed terminology,
5. chapter contract boundaries,
6. claim boundaries already established,
7. citations already present, unless explicitly allowed to move.

#### 3. Keeper Ideas

List the ideas that must survive, even if the prose changes completely.

These should be content anchors, not sentence-level constraints.

#### 4. Material to Delay, Reduce, or Keep Light

List the elements that tend to make the section mechanical or overloaded.

Typical items:

1. compliance language,
2. scope disclaimers,
3. methodological caveats,
4. interpretive-contract taxonomy,
5. overloaded contribution paragraphs.

#### 5. Allowed Improvements

State what GPT 5.2 is explicitly allowed to improve.

Typical items:

1. sentence rhythm,
2. transitions,
3. paragraph splitting,
4. explanation density,
5. reader pull,
6. concrete grounding before abstraction.

#### 6. Forbidden Changes

State what GPT 5.2 must not do.

Typical items:

1. do not invent sources or citations,
2. do not add new claims,
3. do not strengthen claims beyond the supplied material,
4. do not redesign chapter architecture,
5. do not rewrite the roadmap structure,
6. do not introduce new categories, taxonomies, or mechanism definitions,
7. do not add stronger methodology language than already present,
8. do not change the evaluator role or thesis contribution logic.

#### 7. Required Rhetorical Order

If the section has a required sequence, state it here.

Example:

1. concrete tension
2. why that tension matters
3. problem setting
4. research question
5. contribution
6. bounded scope
7. roadmap

#### 8. Current Draft

Paste the current section text here.

#### 9. Output Format

Require exactly these outputs:

1. `Reader-First Rewrite`
   - full rewritten section only
2. `Why This Is Stronger`
   - max 5 short bullets
3. `Drift Risks`
   - any sentences or moves that may have drifted too far from the supplied structure, claims, or evidence

### Operating Rule

After GPT 5.2 returns a rewrite:

1. do not adopt it directly,
2. run a Codex discipline pass,
3. check chapter contract,
4. check claim ledger,
5. check style guide,
6. run the section quality gate,
7. only then decide whether to patch the thesis file.
