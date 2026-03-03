# V2 Figure and Table Registry

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This registry defines the V2 visual system before drafting. Every visual must have a single analytical job and a clear chapter home. If a visual is mainly audit or completeness oriented, it should move to the appendix rather than burden the main text.

## Visual Design Rules

1. One figure / table, one analytical job.
2. Use one consistent color family per metric group across the thesis.
3. Legends should be ordered consistently.
4. Captions must explain analytical relevance, not just describe content.
5. All visuals must be referenced in the text.
6. Interpretation-heavy visuals should be paired with a short explanatory paragraph.
7. Main text visuals should be kept lean; audit-heavy materials move to appendix.

## Main Text Registry

| ID | Type | Working Title | Job | Canonical Chapter | Source Base / Inspiration | Keep / New / Move |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| V2-F01 | Figure | DePIN CPS Coordination Loop | define the four-actor and hardware-incentive feedback system | Chapter 2 Foundations | current foundations; B007-E visual logic | new / redesign |
| V2-T01 | Table | Stress Factor Definitions | define Reward Addiction, Subsidy Gap, Speculative Fragility | Chapter 2 Foundations | current `tab:stress_factors` | keep with prose cleanup |
| V2-T02 | Table | Comparator Archetypes | classify comparator projects by infrastructure and incentive profile | Chapter 3 Framework | B007-A comparative tables | new / derived |
| V2-T03 | Table | Emission Regime Archetypes | compare emission schedule families | Chapter 3 Framework | B007-A | new / derived |
| V2-T04 | Table | Verification and Reward Logic Typology | compare action-based, outcome-based, and other verification logics | Chapter 3 Framework | B007-A; B005-D | new / derived |
| V2-T05 | Table | Sink and Accrual Typology | classify usage-burn, revenue-buyback, and weak-accrual models | Chapter 3 Framework | B007-A | new / derived |
| V2-T06 | Table | Demand Regime Typology | compare enterprise, consumer, and API-heavy demand profiles | Chapter 3 Framework | B007-A | new / derived |
| V2-F02 | Figure | Onocoy Mechanism Diagram | explain ONO, Data Credits, routing, and reward logic | Chapter 4 Onocoy | current Onocoy chapter; B005-C | new |
| V2-T07 | Table | Onocoy Case at a Glance | summarize Onocoy actor, demand, token, and reward structure | Chapter 4 Onocoy | current `tab:onocoy_case_at_a_glance` | keep with refinement |
| V2-T08 | Table | Empirical Stress Windows | summarize historical windows and why they matter | Chapter 5 Empirical | current empirical summary | keep |
| V2-T09 | Table | Metric Applicability Matrix | show what can and cannot be observed empirically | Chapter 5 Empirical | current empirical matrix | keep |
| V2-T10 | Table | Comparator Lineage Funnel | show how broad comparator set narrows to DTSE-relevant profiles | Chapter 5 Empirical | current comparator lineage | keep |
| V2-F03 | Figure | DTSE Architecture | show inputs, protocol rules, agents, outputs, and boundaries | Chapter 6 Methodology | current methods; B007-C slide 4 | new / redesign |
| V2-T11 | Table | Scenario Grid | define baseline plus four stress channels | Chapter 6 Methodology | current methodology / appendix | move summary into main text |
| V2-T12 | Table | Metric and Threshold Logic | explain Stage 1 and Stage 2 metric roles | Chapter 6 Methodology | current methods / appendix | new / condensed |
| V2-F04 | Figure | ONO Baseline Reference Trajectories | establish baseline drift | Chapter 7 Results | current `fig:dtse_baseline_reference` | keep |
| V2-F05 | Figure | Demand Contraction Response | show utilization, sinks, and provider-profit deviation | Chapter 7 Results | current `fig:dtse_demand_contraction_ono`; B007-C slide 6 | keep / redesign captioning |
| V2-F06 | Figure | Liquidity Shock Transmission | show price dislocation and churn response | Chapter 7 Results | current `fig:dtse_liquidity_shock_ono`; B007-C slide 7 | keep / redesign captioning |
| V2-F07 | Figure | Competitive Yield Pressure | show participation collapse under outside yield | Chapter 7 Results | current `fig:dtse_competitive_yield_ono`; B007-C slide 8 | keep / redesign captioning |
| V2-F08 | Figure | Provider Cost Inflation | show profit compression and provider decline | Chapter 7 Results | current `fig:dtse_cost_inflation_ono`; B007-C slide 9 | keep / redesign captioning |
| V2-F09 | Figure | Cross-Profile Final-Week Comparison | compare retention and solvency by scenario | Chapter 7 Results | current `fig:dtse_cross_profile_retention`; B007-C slide 10 | keep |
| V2-F10 | Figure | Signal Timing by Stress Channel | show first-moving metrics and timing windows | Chapter 7 Results | current `fig:dtse_signal_timing_chart`; B007-C slide 12 | keep / possibly split |
| V2-T13 | Table | Cross-Scenario Synthesis | map channels to earliest and secondary detection fields | Chapter 7 Results | current `tab:dtse_cross_scenario_synthesis` | keep |
| V2-T14 | Table | Failure-Mode Diagnostic Matrix | formalize Reward-Demand Decoupling, etc. | Chapter 7 Results | current `tab:failure_modes`; B007-C slide 13 | keep |
| V2-T15 | Table | Limitation-to-Claim Map | make claim boundaries explicit | Chapter 8 Discussion | current `tab:limitation_claim_impact_map` | keep |
| V2-T16 | Table | Governance Archetypes Summary | map archetypes to failure signatures and intervention type | Chapter 8 Discussion | current discussion + corpus notes | new / derived |

## Appendix Registry

| ID | Type | Working Title | Job | Current Source | Keep / Move / Drop |
| :-- | :-- | :-- | :-- | :-- | :-- |
| A-V2-T01 | Table | Full DTSE Scenario Grid | full frozen scenario inputs | current appendix | keep appendix |
| A-V2-T02 | Table | Scenario Formula Map | audit equations and rationale | current appendix | keep appendix |
| A-V2-T03 | Table | Threshold Registry Excerpt | audit thresholds | current appendix | keep appendix |
| A-V2-T04 | Table | Override Ledger | audit profile-specific overrides | current appendix | keep appendix |
| A-V2-T05 | Table | Run Manifest Excerpt | audit reproducibility | current appendix | keep appendix |
| A-V2-T06 | Table | Empirical Metric Catalogue | audit empirical applicability logic | current appendix | keep appendix |
| A-V2-T07 | Table | Onocoy Metric Applicability Profile | audit Onocoy-specific empirical applicability | current appendix | keep appendix |

## Candidate New Visuals (Optional)

These are promising but should only be added if they clearly improve the argument and do not create unnecessary workload.

| ID | Type | Working Title | Value | Risk |
| :-- | :-- | :-- | :-- | :-- |
| V2-F11 | Figure | Cross-Scenario Delta Overlay | stronger visual emphasis on deviation from baseline | may duplicate current results if not designed carefully |
| V2-F12 | Figure | Failure-Mode Library | highly teachable summary visual | risk of becoming too presentation-like |
| V2-T17 | Table | Unified Stress-to-Response Matrix | compresses channel, trigger, signature, and governance response into one cheat sheet | may duplicate T13/T14/T16 if overloaded |
| V2-F13 | Figure | Death Spiral Probability Heatmap | visually strong summary of composite risk | only valid if the metric is stable enough and clearly defined |

## Visuals to Avoid

1. Raw market-cap ranking tables in the main text unless strictly necessary.
2. Screenshot-heavy figures.
3. Decorative diagrams that do not carry analysis.
4. Duplicate summary tables that repeat the same content with different wording.

## Priority Build Order

1. Chapter 2 CPS figure
2. Chapter 3 comparative framework tables
3. Chapter 4 Onocoy mechanism figure
4. Chapter 6 DTSE architecture figure
5. Chapter 7 result figures and synthesis tables
6. Chapter 8 limitation and governance summary tables

## Use With

This registry should be read with:

- `v2_blueprint.md`
- `v2_claim_routing_map.md`
- `v2_keep_rewrite_drop_matrix.md`

