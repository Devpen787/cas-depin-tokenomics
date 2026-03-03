# V2 Keep / Rewrite / Drop Matrix

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This matrix classifies current thesis assets and rebuild-corpus sources into four practical dispositions:

1. `KEEP`
2. `REWRITE`
3. `DROP`
4. `MOVE TO APPENDIX / AUDIT`

The goal is to prevent V2 from inheriting V1's weak structure, duplicated explanations, and avoidable formatting debt.

## Current Thesis Chapter Disposition

| Current File | Primary Role in V2 | Disposition | Why |
| :-- | :-- | :-- | :-- |
| `sections/personA_foundations.tex` | Intro + Foundations source | REWRITE | strong concepts, but needs structural cleanup, less compression, and cleaner integration with V2 foundations contract |
| `sections/personB_framework.tex` | Framework skeleton | KEEP + REWRITE | strongest current structural alignment for framework; needs richer comparative tables and stronger comparative depth from corpus |
| `sections/personA_onocoy.tex` | Onocoy anchor chapter | KEEP + REWRITE | already disciplined, but needs verified mechanism consolidation and cleaner fit with framework/methodology handoff |
| `sections/empirical_analysis.tex` | Empirical stress layer | KEEP + REWRITE | conceptually strong and already doing important observability work; may need flow and emphasis cleanup |
| `sections/personC_methodology.tex` | DTSE methodology anchor | KEEP + REWRITE | intellectually strong anchor chapter; may need tightening and cleaner exposition, not conceptual reinvention |
| `sections/personC_results.tex` | Results anchor | KEEP + REWRITE | strongest core of the thesis; should keep most analytical structure while improving readability and visual narration |
| `sections/personC_discussion_conclusion.tex` | Discussion / conclusion anchor | KEEP + REWRITE | strong claim-boundary logic; should be made less procedural and more integrated |
| `sections/appendix.tex` | audit appendix | KEEP | already aligned with audit function; may need selective extension only |

## Current Thesis Elements to Preserve Aggressively

These are among the highest-value current assets:

1. empirical observability and N/R discipline
2. methodology contract and evidence-layer separation
3. results baseline-relative reading logic
4. failure-mode matrix
5. limitation-to-claim map
6. appendix audit artifacts

## Current Thesis Elements to Rewrite Aggressively

These are conceptually valid but compositionally weak or uneven:

1. some introduction and contribution framing in `personA_foundations.tex`
2. sections of the framework chapter that are too compressed relative to the available comparative material
3. transitions between Onocoy, empirical analysis, methodology, and results
4. parts of the discussion that still read as procedural or deferred interpretation management
5. repetitive explanation patterns across chapters

## Current Thesis Elements to Avoid Carrying Forward Literally

1. duplicated mechanism explanations
2. overly compact paragraphs created by prior drafting constraints
3. AI-sounding transition formulas
4. formatting conventions that generated friction without improving readability

## Rebuild Corpus Disposition

| Corpus Artifact | Disposition | Why |
| :-- | :-- | :-- |
| B001-A / B002-A / B006-B physical-hardware cluster | KEEP AS SOURCE / REWRITE INTO V2 | strongest foundations flow material |
| B001-B / B002-C / B002-E BME cluster | KEEP AS SOURCE / REWRITE INTO V2 | strong comparative framework logic |
| B001-C / B002-B / B004-F / B005-C Onocoy mechanism cluster | KEEP AS SOURCE / REWRITE INTO V2 | essential for Onocoy anchor, but verification-sensitive |
| B001-E / B004-G / B006-D failure-signature cluster | KEEP AS SOURCE / REWRITE INTO V2 | central to DTSE results and discussion |
| B002-D governance archetypes | KEEP AS SOURCE / REWRITE INTO V2 | useful in discussion, but not ready to paste |
| B003-A / B003-B limitations cluster | KEEP AS SOURCE / REWRITE INTO V2 | useful for method boundaries and discussion |
| B003-C / B003-D / B003-E / B003-I future-extension cluster | KEEP AS FUTURE-WORK SOURCE | should remain subordinate |
| B003-H / B004-B verification-friction cluster | KEEP AS SOURCE / SELECTIVE USE | useful but must not overpower the thesis |
| B004-E historical calibration strategy | KEEP AS SOURCE | useful for methodology framing |
| B004-I provider heterogeneity | KEEP AS SOURCE / CLEAN UP | useful for methods/results, but incomplete fragments must not be imported |
| B004-K sunk-cost moat implementation | KEEP AS SOURCE | strong methods bridge |
| B005-E missing-question inventory | KEEP AS PLANNING ONLY | rebuild checklist, not thesis prose |
| B005-F replacement TOC | KEEP AS PLANNING ONLY | architecture idea source, not canonical structure |
| B005-G visual redesign plan | KEEP AS PLANNING ONLY | supports V2 visual system |
| B006-C three-function robustness lens | KEEP AS SOURCE / OPTIONAL | strong framing candidate if integrated carefully |
| B007-A comparative tokenomics markdown draft | KEEP AS SOURCE / MINE HEAVILY | best comparative framework reservoir, but not thesis-ready |
| B007-B docx variant | KEEP AS FORMAT VARIANT ONLY | near-duplicate |
| B007-C slide deck | KEEP AS DESIGN SOURCE | useful for chart and narrative sequencing |
| B007-D mindmap | KEEP AS PLANNING SOURCE | architecture support |
| B007-E failure-signatures image | KEEP AS DESIGN SOURCE | useful for visual simplification |

## Disposition Rules for Rich But Weakly Sourced Context

Rich market context that is clearly useful but not yet thesis-safe should be:

1. kept in the context layer
2. used to improve explanation and examples
3. converted into source-tracked claims if it needs to become load-bearing
4. dropped from the main thesis if it cannot be sourced or bounded safely

## Drop List (Default)

These should be dropped unless a specific argument need emerges:

1. unstable market-cap ranking tables in the main body
2. time-sensitive token-price snapshots as major framework evidence
3. repetitive prose explanations of the same mechanism across chapters
4. decorative presentation phrases such as "Zombie Phase" or similar
5. duplicated summary visuals that do not add analytical value

## Appendix / Audit Moves

These should live in appendix or audit space rather than main narrative:

1. full frozen scenario grids
2. threshold registries
3. run manifests
4. override ledgers
5. full metric applicability catalogues
6. long project-by-project comparative tables that support but do not drive the core framework argument

## Rebuild Priority

### High priority keep-and-rewrite

1. methodology and results logic
2. comparative framework tables
3. Onocoy mechanism explanation
4. empirical bridge chapter

### Medium priority keep-and-rewrite

1. introduction flow
2. foundations readability
3. discussion humanization

### Planning-only

1. replacement TOC ideas
2. missing-question inventory
3. uploaded planning visuals

## Use With

This matrix should be read with:

- `v2_blueprint.md`
- `v2_claim_routing_map.md`
- `v2_figure_table_registry.md`

