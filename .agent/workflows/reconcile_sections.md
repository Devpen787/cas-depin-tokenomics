---
description: Reconcile Sections A, B, and C
---

# Section Reconciliation Workflow

This workflow compares the three main thesis sections to ensure consistency, specifically checking if modeling assumptions are grounded in earlier definitions and mechanisms.

## Input
- Implicitly uses:
    - `sections/personA_foundations.tex`
    - `sections/personB_tokenomics.tex`
    - `sections/personC_modeling.tex`

## Steps

1.  **Read All Sections**: Use `view_file` to read the content of all three section files.
2.  **Extract Key Elements**:
    - **From A**: Definitions of stress, DePIN context, market assumptions.
    - **From B**: Tokenomic mechanisms, supply/demand drivers, value flow.
    - **From C**: Modeling parameters, scenarios, specific assumptions used in simulations.
3.  **Cross-Reference Analysis**:
    - **Check 1: Terminology**: Are terms used in B and C formally defined in A?
    - **Check 2: Mechanism Alignment**: Does the model in C accurately reflect the mechanisms described in B?
    - **Check 3: Assumption grounding**: Are the assumptions in C (e.g., "user growth rate", "market crash depth") justified or discussed in A or B?
4.  **Output Reconciliation Checklist**:
    - Output a markdown checklist.
    - Group by "Mismatch", "Undefined Term", or "Hidden Assumption".
    - **Format**:
        - `[ ] Issue Description` (Ref: Section X vs Section Y)
        - `    - Suggestion: ...`

## Example Output

# Reconciliation Checklist

### Mismatches
- [ ] Person B describes a "burn-and-mint" model, but Person C models a "staking-only" economy.
    - Suggestion: Update C to include burn mechanics.

### Undefined Terms
- [ ] Person C uses "Velocity of Money" as a key variable, but Person A never defined it.
    - Suggestion: Add definition to Section A foundations.

### Hidden Assumptions
- [ ] Person C assumes "10% monthly retention", which contradicts Person B's claim of "high churn incentives".
    - Suggestion: Align retention targets.
