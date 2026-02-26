# Thesis Structure & Tracking Matrix

This document is the central hub for the thesis. It maps out the "Golden Thread" (the core argument), tracks progress and ownership, defines the variables translating theory to code, and outlines the chapters.

## 1. The "Golden Thread" (Argument Flow)
*This section ensures every chapter directly answers the main thesis question.*

- **Main Thesis Question:** How do DePIN tokenomic mechanisms (specifically BME vs. Capped Supply) behave under physical and economic stress, and how can we evaluate their robustness before catastrophic failure?
- **Foundations:** Establishes why DePINs are fragile (physical hardware sunk costs) and defines "stress" theoretically. *Addresses Gap: Validates the physical constraint not captured by standard crypto literature.*
- **Framework:** Defines the tokenomic mechanisms ("the cures") currently used to manage this stress. *Addresses Contradiction: Highlights the tension between "sustainable economics" narratives and actual subsidy-dependence mechanics.*
- **Onocoy Case:** Provides the empirical baseline—what does a real capped-supply GNSS network look like? *Addresses Contradiction: Explores the friction between coverage expansion incentives and density-quality economics.*
- **Empirical Analysis:** Proves that we can observe these stress failures historically in other networks without simulations.
- **Methodology:** Sets up the simulation environment to test Onocoy's specific mechanics against hypothetical future stress. *Addresses Contradiction: Reconciles the gap between permissionless openness and the security/verification burden.*
- **Results:** Answers the main question by showing how the mechanisms performed under the simulated stress.

## 2. Status & Ownership Matrix
*Kanban-style tracking for chapter progress.*

| Chapter / Section | Primary Owner | Status | Blockers / Next Steps |
| :--- | :--- | :--- | :--- |
| 1. Foundations | Person A | `Drafted` | Review theoretical definitions |
| 2. Theoretical Framework | Person B | `Drafted` | Expand BME industry standard details |
| 3. Empirical Case: Onocoy | Person A | `Drafted` | Validate hardware specs |
| 4. Empirical Analysis | Person A/C | `Drafted` | Finalize Geodnet vs Onocoy comparison |
| 5. Methodology | Person C | `Drafted` | Lock down simulation parameters |
| 6. Results | Person C | `Drafted` | Close remaining `% TODO-CITE` items, complete citation-risk cleanup, and run final Chapter 8/9 coherence + publication QA pass. |
| 7. Appendix | All | `Ongoing` | Add proofs and raw data |

### 2.1 Backlog Inputs (Working Artifacts)
*Auxiliary research artifacts that should be explicitly integrated or dispositioned before final freeze.*

| Artifact | Path | Integration Status | Owner | Next Action |
| :--- | :--- | :--- | :--- | :--- |
| DePIN Metric Applicability Framework | `output/md/DePIN_Metric_Applicability_Framework.md` | `Partially Integrated` | Person C + Person A | Treat as canonical applicability source; port thesis-safe rules (mechanism/maturity/data preconditions) into methodology and Onocoy case sections. |
| DePIN Metric Applicability Revelations | `output/md/Depin_Metric_Applicability_Revelations.md` | `Archived Input` | Person C | Keep for provenance only; reference the consolidated framework for active implementation decisions. |
| Blockchain Gap Audit | `BLOCKCHAIN_GAP_AUDIT.md` | `Not Formally Integrated` | Person A + Person B | Decide whether to include blockchain-selection argument in submission scope; if yes, port only citable, primary-source claims into framework/case chapters. |
| Onocoy Intelligence Dossier | `output/md/Onocoy_Intelligence_Dossier.md` and `output/pdf/Onocoy_Intelligence_Dossier.pdf` | `Partially Integrated` | Person A + Person C | Use as structured context source for case-study consistency checks; convert any retained claims into chapter text with bibliography-backed citations only. |

### 2.2 Backlog Execution Items (Open Tasks)
*Concrete open tasks in the active writing/validation stream.*

| Task | Scope / Location | Status | Owner | Next Action |
| :--- | :--- | :--- | :--- | :--- |
| Dune query pack and outputs | Onocoy demand/burn/holders metrics (dashboard-derived) | `Open` | Person A + Person C | Run/collect agreed Dune SQL outputs and map results to Chapter 3/4 evidence language and metric tables. Canonical local workspace: `output/dune/` (`queries/`, `results/`, `snapshots/`, `notes/`). |
| Holder distribution recreation | Wallet concentration and holder segmentation | `Open` | Person A | Recreate holder distribution table/figure from Dune and extract top-holder concentration statistics for thesis-safe reporting; store exports in `output/dune/results/`. |
| Participant-type classification | Miner/operator typology (`companies`, `web3 teams`, `enthusiasts`) | `Open` | Person A + Person C | Add explicit participant-type note in Onocoy case and align terminology with provider heterogeneity assumptions in methodology/results. |
| Metric applicability conditions | `sections/personC_methodology.tex` and `sections/personA_onocoy.tex` | `Open` | Person C + Person A | Insert applicability-conditions language and Onocoy applicability subsection per `DePIN_Metric_Applicability_Framework.md` insertion guidance; keep wording model-conditional and non-prescriptive. |
| Empirical-analysis citation closure | `sections/empirical_analysis.tex` `% TODO-CITE` markers | `Open` | Person C | Replace two remaining TODO markers with primary-source citations and remove placeholders. |
| Final chapter coherence pass | Chapter 8/9 boundary language and duplication check | `Open` | Person C | Run final pass to keep interpretation-boundary protocol, scenario cards, and discussion claim classes fully aligned. |

### 2.3 Master Plan Checklist (Locked Anti-Drift Tracker)
*This is the authoritative implementation checklist agreed in the writing stream. Keep this list stable; update only statuses and evidence anchors.*

| # | Master Plan Item | Status | Evidence / Anchor | Next Action |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Lock non-negotiables: DTSE remains fixed (pre-specified metric set, frozen scenario grid, fixed horizon/aggregation, frozen manifest; no profile-based metric activation in DTSE results). | `Done` | `sections/personC_methodology.tex` and `sections/personC_results.tex` | Preserve this as a hard boundary; do not introduce DTSE metric gating. |
| 2 | Chapter 6 only: empirical observability discipline (add observability paragraph + N/R codes, apply N/R consistently, close `% TODO-CITE`). | `Partial` | `sections/empirical_analysis.tex` | Apply N/R markers in empirical comparisons and close 2 remaining `% TODO-CITE` placeholders. |
| 3 | Methodology: controlled comparability vs profile specificity contract. | `Done` | `sections/personC_methodology.tex` | Keep invariants vs profile-specific assumptions explicit. |
| 4 | Appendix audit shield tables: Override Ledger (+ optional Effective Stress Exposure summary). | `Partial` | `sections/appendix.tex` | Keep Override Ledger; decide and add optional Effective Stress Exposure table if needed. |
| 5 | Results wording cleanup: generic labels as Provider Type A/B, keep ONO mapping note where needed. | `Partial` | `sections/personC_results.tex` | Complete consistency in remaining methodology/appendix wording where rural/urban still appears as generic narrative. |
| 6 | Discussion payoff: frame contribution as empirical partial observability + controlled DTSE counterfactual layer + traceable profile specificity. | `Partial` | `sections/personC_discussion_conclusion.tex` | Add concise synthesis paragraph to make this triad explicit in the contribution narrative. |
| 7 | Backlog execution after core integration: Dune pack, holder concentration, participant-type insertion, Blockchain Gap Audit scope decision. | `Open` | `THESIS_STRUCTURE.md` backlog tables + supporting artifacts | Execute backlog items once core integration and QA gate are complete. |
| 8 | Final QA gate: compile, citation-risk sweep, cross-reference consistency, zero unresolved placeholders in submission text. | `Open` | `main.tex` build + chapter files + citation trackers | Run full final QA pass and close all unresolved placeholders before freeze. |

**Anti-drift rule:** When new feedback arrives, map it to one of the eight items above; do not create parallel plans unless this checklist is explicitly revised.

## 3. Theory-to-Model Glossary (Variable Mapping)
*Ensures consistency when translating theoretical concepts into simulation code.*

| Theoretical Concept (Person B) | Empirical Metric (Person A) | Simulation Parameter (Person C) |
| :--- | :--- | :--- |
| **Reward Addiction** | Burn-to-Mint Ratio $< 1$ | `burn_fraction`, `emission_cap` |
| **Subsidy Gap** | Real Yield vs. Dilutive Yield | `provider_opex`, `fiat_revenue_baseline` |
| **Speculative Fragility** | 30-Day Retention vs. Price Drop | `churn_threshold`, `price_drift` |
| **Elastic Provider Exit** | Competitive Yield Switching Rate | `competitor_yield_opportunity` |
| **Adversarial Verification Failure** *(Out of Scope for v1 Simulation)* | Sybil/Spoofing Incidence Rate | `malicious_actor_pct`, `verification_failure_penalty` |
| **Governance Concentration** *(Out of Scope for v1 Simulation)* | Proposal Gini Coefficient | `governance_latency_modifier` |

## 4. LaTeX Tagging Conventions
*Use these inline comments in your `.tex` files to integrate with our tracking tools.*

- `% TODO-CITE: [Author Year] [Note]` 
  *Use when you know a claim needs a citation but you don't have the page number yet.*
- `% TODO-LINK: [Section/Figure]` 
  *Use when you need to cross-reference another chapter but it isn't written yet.*
- `% SCOPE CONTRACT: [Person]` 
  *Use at the top of a file to declare who owns the content.*

---

## 5. Chapter Outlines & Primary Sources

### 1. Foundations (`sections/personA_foundations.tex`)
**Key Elements:** Table 1 (Theoretical Definitions of Stress Factors).
**Primary Sources:** Messari (2024), Brouwer & Burg (2016), Ho (2022), Mardikes (2025).

### 2. Theoretical Framework (`sections/personB_framework.tex`)
**Key Elements:** Project Archetypes (Helium, Hivemapper, Render).
**Primary Sources:** Voshmgir (2020), Bernardineli (2022), McConaghy (2020), Tan (2020).

### 3. Empirical Case: Onocoy (`sections/personA_onocoy.tex`)
**Key Elements:** Hardware requirements, ONO emission/burn mechanics.
**Primary Sources:** Onocoy documentation and whitepaper.

### 4. Empirical Stress Analysis (`sections/empirical_analysis.tex`)
**Key Elements:** Standardized Metrics for Comparison Table, Stress Scenarios.
**Primary Sources:** RapidInnovation (2024), Coincub (2025), Hacken (2024).

### 5. Methodology: Simulation-Based Stress Testing (`sections/personC_methodology.tex`)
**Key Elements:** Stress dimensions, Evaluation Metrics.
**Primary Sources:** Gauntlet (2020), Braakman (2022), Morris (2019).

### 6. Results (`sections/personC_results.tex`)
**Key Elements:** Outcomes of the simulation stress tests.
