# Thesis Structure & Tracking Matrix

This document is the central hub for the thesis. It maps out the "Golden Thread" (the core argument), tracks progress and ownership, defines the variables translating theory to code, and outlines the chapters.

## 1. The "Golden Thread" (Argument Flow)
*This section ensures every chapter directly answers the main thesis question.*

- **Main Thesis Question:** How do DePIN tokenomic mechanisms (specifically BME vs. Capped Supply) behave under physical and economic stress, and how can we evaluate their robustness before catastrophic failure?
- **Foundations:** Establishes why DePINs are fragile (physical hardware sunk costs) and defines "stress" theoretically.
- **Framework:** Defines the tokenomic mechanisms ("the cures") currently used to manage this stress.
- **Onocoy Case:** Provides the empirical baseline—what does a real capped-supply GNSS network look like?
- **Empirical Analysis:** Proves that we can observe these stress failures historically in other networks without simulations.
- **Methodology:** Sets up the simulation environment to test Onocoy's specific mechanics against hypothetical future stress.
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
| 6. Results | Person C | `Not Started` | Waiting on simulation runs |
| 7. Appendix | All | `Ongoing` | Add proofs and raw data |

## 3. Theory-to-Model Glossary (Variable Mapping)
*Ensures consistency when translating theoretical concepts into simulation code.*

| Theoretical Concept (Person B) | Empirical Metric (Person A) | Simulation Parameter (Person C) |
| :--- | :--- | :--- |
| **Reward Addiction** | Burn-to-Mint Ratio $< 1$ | `burn_fraction`, `emission_cap` |
| **Subsidy Gap** | Real Yield vs. Dilutive Yield | `provider_opex`, `fiat_revenue_baseline` |
| **Speculative Fragility** | 30-Day Retention vs. Price Drop | `churn_threshold`, `price_drift` |
| **Elastic Provider Exit** | Competitive Yield Switching Rate | `competitor_yield_opportunity` |

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
