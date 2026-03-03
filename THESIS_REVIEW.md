# Thesis Review & Unification Plan

## Current Status (Post-Integration)
I have successfully integrated the "Person A" blocks (Introduction, Positioning, Methodology, Scenarios, Metrics) into the thesis. However, this has created significant structural redundancy and highlighted gaps.

## 1. Compliance & Structural Issues
### A. The "Double Methodology" Problem
- **Issue**: We now have two "Methodology" sections.
    - **Section 3 (Person A)**: "Methodological Approach" (New, definitive text).
    - **Section 7 (Person C)**: "Methodology: Simulation-Based Stress Testing" (Old text).
- **Impact**: This confuses the reader. The "Methodology" in Person C is now redundant and often repeats the "Scope/Non-goals" logic established in Person A.

### B. The "Person B" Void
- **Issue**: Section 6 "Tokenomics" (Person B) is currently empty.
- **Impact**: The thesis jumps from "Hypothetical Stress Scenarios" (Sec 4) directly to "Results" (Sec 8), without defining the *specific* system being tested (Onocoy's Tokenomics). The results in Person C reference "Subsidy Inertia" and "Burn-to-Mint", but these mechanisms haven't been technically defined yet.

## 2. Refactoring Proposal
To unify the thesis into a single cohesive document, I recommend the following restructuring:

### Step 1: Dedup Person C
- **Action**: Delete the "Methodology" section from `sections/personC_modeling.tex` (currently Section 7).
- **Rationale**: The new Person A text covers this more formally.
- **Rename**: Change Person C's focus purely to **"Simulation Results & Analysis"**.

### Step 2: Fill Person B (Tokenomics)
- **Action**: We need to write Section 6.
- **Content Needed**:
    - Specifics of the Onocoy ONO token.
    - The "Burn-and-Mint" equilibrium mechanics.
    - The specific emission schedule and hardware requirements.

### Step 3: Renumbering
- **Structure**:
    - **1. Introduction** (Done - A)
    - **2. Positioning** (Done - A)
    - **3. Methodology** (Done - A)
    - **4. Stress Scenarios** (Done - A)
    - **5. Evaluation Metrics** (Done - A)
    - **6. Case Study: Onocoy Tokenomics** (Missing - B)
    - **7. Simulation Results** (Refactored C)
    - **8. Discussion/Archetypes** (Part of C)
    - **9. Conclusion** (Missing)

## 3. Next Steps
1.  **Approve Refactor**: Shall I strip the redundant Methodology from Person C?
2.  **Provide Person B**: Do you have text blocks for the Tokenomics/Onocoy section, or should I verify what we have?
3.  **Conclusion**: We will need a final conclusion section.

---

## TOC-Driven Hostile Review Register (2026-02-26)

### Mode
- `MODE: SYNTHESIS` (no edits from this review itself)
- Review order followed `main.toc` sequence (Abstract → Chapters 1–10 → Appendix)

### Overall Assessment
- Structural coherence is strong (approx. `8.5/10` defensibility).
- Primary risks are execution precision and evidence strength, not high-level framing.

### High-Risk Targets (Must Fix)
1. **Framework overclaim risk**: “industry standard” phrasing is attackable unless benchmarked.  
   - File: `sections/personB_framework.tex` (around line 25)
2. **Empirical signal strength risk**: some “observed pattern” language may overstate data resolution.  
   - File: `sections/empirical_analysis.tex` (around lines 214, 229)
3. **Interview-calibration method risk**: assumption-bounding logic needs explicit method defensibility.  
   - File: `sections/personC_methodology.tex` (around line 97)
4. **Deterministic numeric check risk in results**: precise values can read post-hoc unless consistently framed as frozen-rule sanity checks.  
   - File: `sections/personC_results.tex` (around lines 95, 127, 145)

### Medium-Risk Targets (Should Fix)
1. **Boundary-language repetition** across Methodology/Results/Discussion can dilute contribution signal.
   - Files: `sections/personC_methodology.tex`, `sections/personC_discussion_conclusion.tex`
2. **Archetype interpretation attack surface**: still vulnerable to “speculative taxonomy” critique unless repeatedly constrained as thesis-proposed analytical labels.
   - File: `sections/personC_discussion_conclusion.tex`

### Low-Risk / Strong Areas
1. Scope and anti-overclaim framing are explicit and generally consistent.
2. External-validity boundaries are clearly disclosed and defensible.

### Claim/Evidence Classification (Cross-Thesis)
- **Mechanism facts**: mostly safe when tied to protocol/governance primary docs.
- **Modeled assumptions**: acceptable, but interview-informed assumptions require clearer method protocol.
- **DTSE outputs**: strong when anchored to scenario IDs, metric definitions, and frozen artifacts.
- **Context claims**: highest attack surface; keep them non-load-bearing.

### Patch Manifest from this Review (if needed later)
- **Set 1**: `sections/personB_framework.tex` + `sections/empirical_analysis.tex`
- **Set 2**: `sections/personC_methodology.tex` + `sections/personC_results.tex`
- **Set 3**: `sections/personC_discussion_conclusion.tex`

### Retrieval Note for New Threads
- In a new thread, ask:  
  `Open THESIS_REVIEW.md and continue from "TOC-Driven Hostile Review Register (2026-02-26)".`

---

## Pre-Submission Execution Checklist (Critical Risk Control)

- [ ] Run formal similarity check (`Turnitin`/`iThenticate`), review flagged passages, and record accepted exclusions.
- [ ] Prepare one-page **Claims Boundary Sheet** (fact vs assumption vs DTSE output vs context; banned overclaim verbs).
- [ ] Prepare one-page **Calibration + Threshold Rationale Sheet** (why ranges/thresholds are used, what sensitivity says).
- [ ] Run traceability sweep: every major claim linked to citation and scenario/metric/figure-table anchor.
- [ ] Run submission dry-run package check: final PDF version, declarations, appendix artifacts, metadata, filename/version control.
