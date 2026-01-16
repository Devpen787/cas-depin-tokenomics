# CAS Transferarbeit Rules & Guidelines

## Purpose of this Document
- Define the quality standards and constraints for the CAS Transferarbeit.
- Distinguish between mandatory requirements (Hard Rules) and best practices.
- Guide human authors in writing consistent, academic content.

## Scope and Non-Scope
- **Scope**: Tokenomics logic, stress testing simulations, and DePIN market analysis.
- **Non-Scope**: Marketing copy, financial investment advice, production code deployment.

## Hard CAS Rules
- **Language**: Academic English. Formal tone. No slang or "crypto-bro" terminology.
- **Claims**: Every claim must be substantiated by evidence, citation, or formal logical derivation. Hand-waving is strictly prohibited.
- **Structure**: Follow the provided LaTeX template (`main.tex`). Do not alter the top-level sectioning without approval.
- **Length**: Report must be concise. Quality over quantity.

## Methodology Constraints
- **Stress Testing**: Scenarios must include at least one "Critical Failure" case.
- **Assumptions**: All modeling assumptions must be explicitly listed in `sections/personC_modeling.tex` and cross-referenced in foundations.
- **Data**: Verification data should be reproducible where possible.

## Citation and Plagiarism Rules
- **Sources**: Use `biblatex` in `bibliography.bib`.
- **Plagiarism**: Zero tolerance. All external concepts must be cited.
- **AI Usage**: AI may be used for drafting and structure but NOT for generating novel intellectual insights or final verification.

## Figures, Tables, and Evidence Rules
- **Captions**: Every figure and table MUST have a descriptive caption.
- **Referencing**: All figures/tables must be referenced in the text (e.g., "see Figure 1").
- **Quality**: Vector graphics preferred for charts. No fuzzy screenshots.

## Group Work Attribution Rules
- **Person A (Foundations)**: Responsible for definitions, context, and literature review.
- **Person B (Tokenomics)**: Responsible for mechanism design, supply/demand logic, and flow.
- **Person C (Modeling)**: Responsible for scenarios, simulation implementation, and quantitative results.
- **Collective Responsibility**: Overall coherence and reconciling inconsistencies between sections.

## What this document does NOT do
- **No Auto-Fixing**: This document lists rules; it does not automatically correct violations in the text.
- **No Rewriting**: It does not generate content or rewriting sections for you.
- **No Magic**: Compliance is the responsibility of the human authors.
