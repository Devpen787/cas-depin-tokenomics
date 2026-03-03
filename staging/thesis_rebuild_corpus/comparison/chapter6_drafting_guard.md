## Chapter 6 Drafting Guard

Status: active internal guard  
Date captured: 2026-03-02  
Mode: `MODE: PATCH`

Purpose:
- keep Chapter 6 aligned with the approved synthesis brief
- prevent drift back into V1 methodology sprawl while drafting

### Fixed Chapter Job

Chapter 6 defines DTSE as a bounded comparative evaluator.

It must own:
- DTSE purpose and scope
- evidence-layer separation
- scenario grid
- metric contract
- Stage 1 signal-detection logic
- Stage 2 failure-signature logic
- reproducibility, calibration boundary, and method limits

It must not become:
- a results chapter
- a new theory chapter
- a forecast narrative
- an appendix dump of frozen scalar values

### Approved Structure

1. `DTSE Purpose, Scope, and Interpretation Contract`
2. `Architecture, Evidence Layers, and Core Assumptions`
3. `Scenario Grid and Experimental Contract`
4. `Metric Contract and Stage 1 Detection Logic`
5. `Stage 2 Failure-Signature Logic`
6. `Reproducibility, Calibration Boundary, and Method Limits`

### Keep

- Option B language: bounded, comparative, non-predictive
- evidence layers
- exogenous versus endogenous distinction
- baseline plus four stress channels
- pre-specified metric contract
- deterministic seeds and repeated runs
- internal verification rather than empirical validation

### Demote Or Keep Out

- full scalar scenario values
- threshold registry detail
- override ledgers
- run manifests
- appendix-grade configuration registers
- results-facing language such as profile timing outcomes
- `death spiral probability` as a main-text headline metric

### Labels To Preserve

- `sec:methodology`
- `sec:dtse_methodology`
- `subsec:dtse_model_overview_assumptions`
- `sec:stress_scenarios`
- `subsec:dtse_scenario_set`
- `sec:evaluation_metrics`
- `subsec:dtse_reproducibility`

### Claim Slice To Realize

- `C37` DTSE is a rule-based comparative stress evaluator, not a forecasting tool.
- `C38` Chapter 6 separates mechanism facts, modeled assumptions, and DTSE outputs as distinct evidence layers.
- `C39` The frozen DTSE experiment set contains one neutral baseline and four stress channels.
- `C40` DTSE uses a pre-specified metric suite and baseline-relative comparison rather than absolute scoring or live-network ranking.
- `C41` Stage 1 detects first material departures from baseline, while Stage 2 classifies failure signatures from patterned deterioration.
- `C42` Reproducibility depends on frozen scenarios, deterministic seeds, repeated runs, and internal verification under stated assumptions.

### Drift Checks

- If a paragraph sounds predictive, narrow it.
- If a paragraph starts reporting outcomes, move it to Chapter 7 later.
- If a table is carrying appendix-grade scalar detail, demote it.
- If a section starts re-teaching Chapter 2 or Chapter 3 at length, compress it.
