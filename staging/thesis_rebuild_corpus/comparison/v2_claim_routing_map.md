# V2 Claim Routing Map

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This document maps major concepts, claim classes, and explanatory burdens to their canonical home in V2. Its job is to stop concept drift, duplication, and cross-chapter spillover.

## Routing Rules

1. Each major concept has one canonical home.
2. Other chapters may reference the concept, but should not re-explain it at full length.
3. If a concept carries multiple claim classes, route the explanation to the chapter that owns the highest-load-bearing version.
4. If a concept is unresolved or weakly evidenced, route it to context or future-work rather than allowing it to float across the thesis.

## Canonical Routing Map

| Concept / Claim Burden | Canonical Home | Allowed Claim Class(es) | Secondary Mentions Allowed In | Notes |
| :-- | :-- | :-- | :-- | :-- |
| DePIN as cyber-physical system | Chapter 2 Foundations | context; mechanism fact; interpretation | Chapter 1 intro; Chapter 6 methodology | Define once, then reference |
| Physical hardware constraint | Chapter 2 Foundations | mechanism fact; context | Chapter 3 framework; Chapter 8 discussion | Do not keep reintroducing as if new |
| Sunk costs / geographic friction / path dependence | Chapter 2 Foundations | mechanism fact; interpretation | Chapter 5 empirical; Chapter 8 discussion | Core explanatory burden lives in Foundations |
| Recovery asymmetry | Chapter 2 Foundations | interpretation; context | Chapter 5 empirical; Chapter 8 discussion | Tie to physical deployment, not results first |
| Reward Addiction / Subsidy Gap / Speculative Fragility | Chapter 2 Foundations | mechanism fact; theoretical framing | Chapter 3 framework; Chapter 6 methodology | Define once cleanly, then operationalize later |
| Comparator universe / archetypes | Chapter 3 Framework | mechanism fact; comparative classification | Chapter 5 empirical | Do not scatter project taxonomy elsewhere |
| Emission regime archetypes | Chapter 3 Framework | mechanism fact; comparative interpretation | Chapter 6 methodology | Rich comparative tables belong here or appendix |
| BME definition | Chapter 3 Framework | mechanism fact | Chapter 4 Onocoy (brief contrast); Chapter 6 methodology | Avoid repeated full definitions |
| Capped supply definition | Chapter 3 Framework | mechanism fact | Chapter 4 Onocoy; Chapter 6 methodology | Use Framework as the canonical mechanism home |
| Burn-to-mint ratio / incentive-solvency proxy concept | Chapter 3 Framework | mechanism fact; interpretation | Chapter 6 methodology; Chapter 7 results | Concept in Framework, implementation in Methods, behavior in Results |
| Work verification taxonomy | Chapter 3 Framework | mechanism fact; comparative classification | Chapter 4 Onocoy | Action-based vs outcome-based distinction defined here |
| Sink / accrual typology | Chapter 3 Framework | mechanism fact; comparative classification | Chapter 4 Onocoy; Chapter 8 discussion | One canonical table system |
| Demand regime typology | Chapter 3 Framework | mechanism fact; comparative interpretation | Chapter 6 methodology | Enterprise vs consumer cyclicality defined once |
| Onocoy dual-layer design | Chapter 4 Onocoy | mechanism fact | Chapter 3 framework (brief preview); Chapter 6 methodology (parameter mapping) | Full explanation only once |
| ONO decay path / 16% logic | Chapter 4 Onocoy | mechanism fact; tightly bounded interpretation | Chapter 3 framework (brief comparison); Chapter 8 discussion | Requires verified mechanism evidence |
| Data Credit routing / buyback-and-burn | Chapter 4 Onocoy | mechanism fact; tightly bounded interpretation | Chapter 3 framework; Chapter 8 discussion | Avoid turning this into generic BME language |
| Onocoy outcome-based rewards | Chapter 4 Onocoy | mechanism fact | Chapter 3 framework (taxonomy); Chapter 8 discussion | Protocol-specific version lives here |
| Blockchain settlement decision boundary | Chapter 4 Onocoy | mechanism fact; bounded context | Chapter 6 methodology | Do not let this become a broad chain thesis |
| Historical stress windows | Chapter 5 Empirical | empirical observation | Chapter 6 methodology (motivation only) | No DTSE outputs here |
| Metric applicability / N-R discipline | Chapter 5 Empirical | empirical observation; interpretation boundary | Chapter 6 methodology (contrast only) | Empirical-only observability rule |
| Need for simulation / bridge to DTSE | Chapter 5 Empirical | interpretation | Chapter 6 methodology | Bridge out of empirical partial observability |
| DTSE purpose and scope | Chapter 6 Methodology | modeled assumption; interpretation boundary | Chapter 1 intro; Chapter 8 discussion | One canonical definition of what DTSE is |
| Evidence layers / interpretive contract | Chapter 6 Methodology | modeled assumption; interpretation boundary | Chapter 1 intro; Chapter 8 discussion | Define formally once |
| Exogenous demand | Chapter 6 Methodology | modeled assumption | Chapter 8 limitations | Must not drift into results narrative |
| Reduced-form price process | Chapter 6 Methodology | modeled assumption | Chapter 8 limitations | Same rule as above |
| Provider heterogeneity / Type A-B / Cost Tier 1-2 | Chapter 6 Methodology | modeled assumption; parameter mapping | Chapter 7 results | Define before using in results |
| Scenario grid | Chapter 6 Methodology | modeled assumption | Chapter 7 results | Frozen contract lives here |
| Stage 1 detection logic | Chapter 6 Methodology | modeled assumption | Chapter 7 results | Methods own the rule, results own the outputs |
| Stage 2 failure-signature logic | Chapter 6 Methodology | modeled assumption | Chapter 7 results; Chapter 8 discussion | Formal definition in Methods, observed patterning in Results |
| Calibration boundaries / historical anchoring | Chapter 6 Methodology | modeled assumption; bounded empirical linkage | Chapter 8 future work | Avoid overclaiming validation |
| Baseline behavior | Chapter 7 Results | DTSE output | Chapter 8 discussion | Results own all baseline descriptions |
| Demand contraction output | Chapter 7 Results | DTSE output | Chapter 8 discussion | Same for all four stress channels |
| Liquidity shock output | Chapter 7 Results | DTSE output | Chapter 8 discussion |  |
| Competitive yield output | Chapter 7 Results | DTSE output | Chapter 8 discussion |  |
| Cost inflation output | Chapter 7 Results | DTSE output | Chapter 8 discussion |  |
| Signal timing | Chapter 7 Results | DTSE output | Chapter 8 discussion | Results own the timings |
| Failure-signature matrix as observed DTSE pattern | Chapter 7 Results | DTSE output; bounded interpretation | Chapter 8 discussion | Methods define criteria, results instantiate them |
| Governance archetypes | Chapter 8 Discussion | interpretation; future extension logic | Chapter 6 methodology (brief boundary note) | Do not prematurely formalize in Methods |
| DTSE limitations | Chapter 8 Discussion | interpretation boundary; limitation framing | Chapter 6 methodology (brief scope notes) | Methodology states scope; discussion absorbs implications |
| Endogenous demand / governance latency / verification extensions | Chapter 8 Discussion | future work | Chapter 6 methodology (minimal scope notes) | Keep extensions subordinate |
| Final answer to research question | Chapter 8 Discussion | interpretation | Chapter 1 intro (framing only) | Only Discussion should close the argument |

## Concepts to Remove From Floating Status

These concepts tended to drift in V1 and must be re-homed explicitly in V2:

1. Burn-to-mint ratio
2. Reward-Demand Decoupling
3. Latent Capacity Degradation
4. Onocoy dual-layer mechanism
5. outcome-based rewards
6. exogenous demand
7. governance archetypes
8. settlement-layer decision boundary

## Anti-Duplication Triggers

If any draft section starts to:

1. re-define BME outside Chapter 3
2. re-explain Onocoy mechanism facts outside Chapter 4
3. state DTSE limitations in full outside Chapters 6 or 8
4. state timing outputs outside Chapter 7
5. import governance archetypes into earlier chapters as if they are central theory

then the text should be rewritten or relocated.

## High-Risk Concept Boundaries

These require especially careful routing:

1. `Burn-to-mint ratio`
   - Framework: concept
   - Methodology: computation / proxy role
   - Results: observed movement
   - Discussion: meaning for robustness

2. `Onocoy`
   - Framework: brief comparative mention only
   - Onocoy chapter: full mechanism explanation
   - Methodology: parameter mapping
   - Results: ONO profile outputs

3. `Failure signatures`
   - Foundations: only light foreshadowing if needed
   - Methodology: formal logic
   - Results: observed signatures
   - Discussion: implications and governance

## Use With

This routing map should be read together with:

- `v2_blueprint.md`
- `v2_chapter_contracts.md`
- `v2_keep_rewrite_drop_matrix.md`

