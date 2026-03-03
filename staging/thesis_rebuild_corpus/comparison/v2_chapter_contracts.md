# V2 Chapter Contracts

Status: synthesis blueprint
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This document defines the chapter-contract system for V2. Each chapter has a fixed job, allowed claim classes, preferred source layers, core visual roles, forbidden spillover, and handoff obligations. No chapter drafting should begin until these contracts are accepted as the working architecture.

## Claim Classes

These labels govern the contracts below:

1. `mechanism fact`
2. `modeled assumption`
3. `DTSE output`
4. `empirical observation`
5. `interpretation`
6. `context`

## Chapter 1: Introduction and Research Contract

### Job

State the thesis problem, explain why DePIN tokenomics requires stress-oriented analysis, define the research question, and state the contribution and interpretive contract.

### Allowed claim classes

- context
- mechanism fact
- interpretation

### Preferred source layers

- evidence for the thesis question and contribution framing
- context for market relevance and motivation

### Core visual roles

- optional thesis-overview figure
- optional research-design summary figure

### Forbidden spillover

- no detailed DTSE outputs
- no long comparative taxonomy tables
- no deep Onocoy mechanics beyond brief framing

### Handoff

Must leave the reader understanding why DePIN is different and why the thesis is structured the way it is.

## Chapter 2: Foundations - DePIN as a Cyber-Physical System

### Job

Define DePIN as a cyber-physical coordination problem. Explain hardware CapEx/OpEx, sunk costs, geographic friction, path dependence, recovery asymmetry, and core stress concepts.

### Allowed claim classes

- context
- mechanism fact
- interpretation

### Preferred source layers

- evidence for DePIN theory, CPS framing, and physical constraints
- context for explanatory examples

### Core visual roles

- CPS / coordination-loop figure
- stress-factor definition table

### Forbidden spillover

- no DTSE run timing
- no parameter-level simulation detail
- no detailed empirical stress windows

### Handoff

Must establish why physical infrastructure makes tokenomics under stress analytically distinct from software-only crypto systems.

## Chapter 3: Comparative Tokenomic Framework

### Job

Define the comparative mechanism vocabulary: emission logic, BME versus capped supply, work verification, sink/accrual pathways, monetization models, demand regimes, and comparator archetypes.

### Allowed claim classes

- mechanism fact
- context
- interpretation

### Preferred source layers

- evidence for comparative tokenomics claims
- context for explanation and typology design
- design layer for table architecture

### Core visual roles

- comparator archetype table
- emission regime table
- verification / reward logic table
- sink / accrual typology table

### Forbidden spillover

- no DTSE outputs
- no weakly sourced market-cap tables in the main text unless strictly necessary
- no results interpretation disguised as theory

### Handoff

Must leave the reader with a structured vocabulary that can cleanly feed Onocoy, empirical analysis, and DTSE parameterization.

## Chapter 4: Onocoy as the Anchor Case

### Job

Explain why Onocoy is the anchor case and present its verified mechanism design: ONO, Data Credits, outcome-based rewards, reward logic, and decay-path implications.

### Allowed claim classes

- mechanism fact
- tightly bounded interpretation
- context

### Preferred source layers

- evidence layer only for load-bearing mechanism claims
- context only for explanatory framing

### Core visual roles

- Onocoy mechanism figure
- concise Onocoy case-summary table

### Forbidden spillover

- no unsupported protocol claims
- no simulation outputs
- no broad comparative claims that belong in Chapter 3

### Handoff

Must translate Onocoy into a thesis-safe mechanism description that can later be mapped into empirical and DTSE language.

## Chapter 5: Empirical Stress Layer

### Job

Demonstrate what is historically observable, define metric-applicability limits, and justify why simulation is necessary.

### Allowed claim classes

- empirical observation
- context
- tightly bounded interpretation

### Preferred source layers

- evidence layer
- design layer for empirical comparison tables

### Core visual roles

- empirical stress-window table
- metric-applicability matrix
- comparator-lineage table

### Forbidden spillover

- no DTSE outputs
- no methodology assumptions presented as empirical facts
- no governance-future-work expansion

### Handoff

Must justify the move from empirical partial observability to DTSE-based counterfactual testing.

## Chapter 6: DTSE Methodology

### Job

Define DTSE, its modeling assumptions, scenario grid, metrics, calibration boundaries, Stage 1 and Stage 2 logic, and the limits of what the simulator can claim.

### Allowed claim classes

- modeled assumption
- mechanism fact where directly mapped from protocol rules
- interpretation of method scope

### Preferred source layers

- evidence for methodological precedent and mapped mechanism facts
- context for explanation
- design layer for architecture figures and scenario tables

### Core visual roles

- DTSE architecture figure
- scenario-grid table
- threshold / metric logic table

### Forbidden spillover

- no real results except minimal illustrative examples required to explain metrics
- no future-work sprawl in the main methodological flow

### Handoff

Must make the reader understand exactly what DTSE does, what it does not do, and how to interpret the outputs correctly.

## Chapter 7: Results

### Job

Report baseline behavior, stress-channel outputs, cross-profile comparison, signal timing, and failure-signature classification under the frozen DTSE setup.

### Allowed claim classes

- DTSE output
- tightly bounded descriptive interpretation

### Preferred source layers

- evidence layer in the form of frozen DTSE artifacts
- design layer for chart sequencing and legends

### Core visual roles

- baseline chart
- four stress-channel charts
- cross-profile comparison figure
- signal-timing figure
- cross-scenario synthesis table
- failure-signature matrix

### Forbidden spillover

- no new theory chapter content
- no heavy future-work discussion
- no unsupported market analogies presented as evidence

### Handoff

Must leave the reader with a clear understanding of which subsystems move first under which stress channels and how failure signatures differ.

## Chapter 8: Discussion, Governance, Limitations, Conclusion

### Job

Interpret what the results mean for DePIN robustness, map failure signatures to governance archetypes, define the limitations, and close with the contribution and future work.

### Allowed claim classes

- interpretation
- context
- limitation framing
- future extension logic

### Preferred source layers

- evidence where needed for support
- context for explanation and synthesis
- design layer for limitation maps or summary visuals

### Core visual roles

- limitation-to-claim map
- optional summary governance-response table

### Forbidden spillover

- no new foundational mechanism definitions
- no hidden new results
- no architecture drift away from the thesis question

### Handoff

Must answer the thesis question clearly, define the boundaries of the claims, and show why the contribution matters without overclaiming.

## Global Enforcement Rules

1. One canonical home per major concept.
2. Do not let chapters compensate for earlier chapter weakness by absorbing material they do not own.
3. Separate mechanism facts, modeled assumptions, empirical observations, DTSE outputs, and interpretation as cleanly as possible.
4. Use appendix material for auditability, not to carry the main narrative.
5. If a paragraph combines multiple claim classes, rewrite it unless the combination is unavoidable and explicitly signposted.

## Immediate Follow-On Documents

These contracts should be followed by:

1. `v2_claim_routing_map.md`
2. `v2_figure_table_registry.md`
3. `v2_keep_rewrite_drop_matrix.md`
4. `v2_workflow_playbook.md`
