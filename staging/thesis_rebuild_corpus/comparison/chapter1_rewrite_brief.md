## Chapter 1 Rewrite Brief

Status: synthesis control document  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This brief records the reader-first rewrite logic used to rebuild Chapter 1 in the V2 shell. It exists so the introduction is not judged only by the final prose. It also preserves what the first failed draft taught the workflow.

Core instruction:

**You are rewriting prose, not architecture.**

### Target

- Target thesis file: `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/v2/sections/01_introduction_research_contract.tex`

### Mission

The introduction must make the reader feel why DePIN tokenomics cannot be treated as a purely financial mechanism. The section has to motivate the thesis question, not just define the thesis structure.

### Felt Problem the Introduction Must Make the Reader Feel

DePIN tokenomics cannot be understood as a purely financial mechanism because the physical layer does not move with token-market speed. A token position can be exited immediately. A rooftop GNSS station, wireless node, or other installed asset cannot. That asymmetry is what makes stress, not growth alone, the core analytical problem.

### Frozen Elements

The following must not change:

1. the chapter's role as the V2 introduction and research contract,
2. the central research-question logic,
3. the bounded comparative, non-predictive thesis stance,
4. the overall roadmap logic already frozen by the V2 chapter contracts,
5. the core DTSE lexicon defined in `THESIS_OS.md`,
6. the existing citations unless explicitly moved for readability.

### Keeper Ideas

The rewrite had to preserve these ideas from the failed draft:

1. DePIN robustness in this thesis is interpreted through three coupled functions:
   - provider retention
   - service continuity
   - incentive--usage alignment
2. The central research question compares BME-oriented and capped-supply designs under physical and economic stress.
3. The thesis is comparative and bounded. It does not claim to forecast live-network outcomes directly.

### Material Deliberately Delayed or Reduced

The rewrite had to delay or reduce the following:

1. Full interpretive-contract taxonomy as a named subsection.
2. Heavy scope and compliance language in the first half of the introduction.

### Allowed Improvements

The rewrite is allowed to improve:

1. sentence rhythm,
2. transitions,
3. paragraph splitting,
4. explanation density,
5. reader pull,
6. concrete grounding before abstraction.

### Forbidden Changes

The rewrite must not:

1. invent sources or citations,
2. add new claims,
3. strengthen claims beyond the supplied text,
4. redesign chapter architecture,
5. rewrite the roadmap into a new chapter sequence,
6. introduce new methodology specificity that belongs later,
7. convert analytical framing into empirical-sounding proof.

### Rhetorical Order

The rewrite used this order:

1. concrete DePIN tension
2. why that tension matters analytically
3. problem setting
4. research question
5. contribution
6. bounded scope
7. roadmap

This replaced the earlier, weaker order:

1. define topic
2. define structure
3. define scope
4. state contract
5. motivate late

### What the First Failed Draft Got Wrong

The rejected draft failed for structural reasons, not because the core ideas were wrong.

Main failures:

1. It opened too abstractly and explained the category before the problem landed.
2. It introduced compliance and interpretive-boundary language too early.
3. It repeated thesis-machine sentence stems such as `This thesis...` and `The thesis...`.
4. It compressed the contribution logic into overly dense prose.
5. It made the reader experience structure faster than meaning.

### Rewrite Strategy

The accepted rewrite used these corrections:

1. Start from a concrete physical asymmetry.
2. Earn the DePIN abstraction after the opening tension lands.
3. Use the three coupled functions as a framing lens, not as an early taxonomy dump.
4. Move bounded-scope language to the end of the section.
5. Keep the introduction readable before making it fully contractual.

### Output Format

The preferred GPT 5.2 output format is:

1. `Reader-First Rewrite`
2. `Why This Is Stronger`
3. `Drift Risks`

### Workflow Notes

This chapter was the first real test of the V2 writing-behavior system. It showed that:

1. a clean LaTeX shell alone does not prevent V1 prose habits,
2. the section quality gate is useful because it can justify `REWRITE FROM SCRATCH`,
3. a section can pass text quality before the process artifacts are fully synced,
4. Chapter 1 should be used as the specimen for what a full V2 pass looks like.
