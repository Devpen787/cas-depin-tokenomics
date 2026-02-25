# Applicability Framework — Thesis Insertion Points

**Source:** `output/md/Depin_Metric_Applicability_Revelations.md` §4–7, cross-referenced with thesis `.tex` files
**Date:** 2026-02-25

---

## 1. The "Don't Grade on N/A" Rule

**What:** An explicit statement that metrics are only applied to projects where their preconditions are met. Projects should not be penalised or ranked on metrics that are structurally inapplicable (e.g. FDV/Revenue for a network with near-zero revenue).

### Insertion point

| Field | Value |
|:------|:------|
| **File** | `sections/personC_methodology.tex` |
| **Section** | `\subsection{Interpretation and Limitations of Metrics}` (line 225) |
| **Label** | `sec:evaluation_metrics` (parent section) |
| **Insert** | **After** the existing closing sentence on line 228: *"This cautious interpretation aligns with best practices in simulation-based research and supports the thesis's evaluative rather than predictive orientation \cite{Braakman2022}."* |

### Suggested anchor text

> Not all metrics are equally applicable to all protocol profiles or maturity stages. Where a metric's preconditions are not met — for example, where annualised revenue is near zero or secondary-market liquidity is insufficient for meaningful turnover measurement — the metric is excluded from comparative evaluation for that profile rather than computed with a misleading or undefined value. This ensures that protocols are assessed only on dimensions where the metric produces an interpretable signal.

### Rationale

This subsection already discusses cautious interpretation and metric limitations. The N/A rule is a natural extension of that framing — it makes the implicit caution explicit and actionable.

---

## 2. Onocoy Metric Applicability Subsection

**What:** A dedicated subsection stating which of the five standardised metrics are applicable, partially applicable, or not applicable to Onocoy given its early-stage status and capped-supply design.

### Insertion point

| Field | Value |
|:------|:------|
| **File** | `sections/personA_onocoy.tex` |
| **Section** | After `\subsection{Tokenomic Mechanics (Descriptive)}` (ends at line 27) |
| **Label** | New: `\subsection{Metric Applicability for Onocoy}` |
| **Insert** | **Before** the import block at line 29: `\subsection{Person A Onocoy Draft Import (Provisional, Source-Preserving)}` |

### Suggested anchor text

> The standardised metrics defined in Section \ref{sec:evaluation_metrics} are not uniformly applicable to Onocoy's current state. As an early-stage network with a capped-supply model rather than pure BME, limited secondary-market liquidity following its 2025 TGE, and near-zero annualised service revenue, three of the five metrics (Revenue per Node, Token Turnover, FDV / Annualised Revenue) do not produce interpretable values. The remaining two — Burn-to-Mint Ratio (adapted for capped-supply emission logic) and 30-Day Node Retention — are applicable with noted caveats regarding data availability and observation-window length. A detailed applicability assessment is provided in the supplementary metric relevance matrix.

### Rationale

The Onocoy chapter describes the tokenomic mechanics and ends with open questions (staking rules). Metric applicability is the natural next analytical step before the import block. Placing it here ensures the reader encounters the caveats before the empirical and simulation chapters apply the metrics.

---

## 3. Metric Applicability Framework

**What:** A structured subsection defining the preconditions under which each standardised metric is applicable, including mechanism-class requirements, maturity-stage constraints, and data-availability prerequisites.

### Insertion point

| Field | Value |
|:------|:------|
| **File** | `sections/personC_methodology.tex` |
| **Section** | `\section{Evaluation Metrics}` → after `\subsection{Principles for Metric Selection}` (ends at line 176) |
| **Label** | New: `\subsection{Metric Applicability Conditions}` |
| **Insert** | **After** line 176: *"These principles align with established guidance for simulation-based evaluation, where metrics should illuminate system behavior without overstating precision \cite{Morris2019}."* and **before** line 178: `\subsection{Core Sustainability Metrics}` |

### Suggested anchor text

> Before defining individual metrics, this section specifies the conditions under which each metric produces a meaningful signal. Applicability depends on three dimensions: mechanism class (whether the protocol uses BME, capped supply, or hybrid designs), maturity stage (whether sufficient revenue and trading history exist to compute the metric), and data availability (whether the required inputs are publicly observable or require internal data). Metrics that fail one or more preconditions for a given protocol profile are excluded from comparative evaluation of that profile, consistent with the interpretation boundaries defined in Section \ref{sec:evaluation_metrics}. The full applicability matrix is provided in the supplementary materials.

### Rationale

The Evaluation Metrics section currently moves directly from selection principles to individual metric definitions. Inserting the applicability framework between these two subsections establishes the precondition logic before the reader encounters the metrics themselves. This is the gap identified in `Depin_Metric_Applicability_Revelations.md` §7 step 1 ("Single DePIN stress metrics catalog with applicability conditions").

---

## Summary of Insertion Points

| Addition | File | After / Before | New Subsection? |
|:---------|:-----|:---------------|:----------------|
| "Don't grade on N/A" rule | `personC_methodology.tex` | After line 228 (end of Interpretation and Limitations) | No — append to existing subsection |
| Onocoy metric applicability | `personA_onocoy.tex` | Before line 29 (Person A import block) | Yes — `\subsection{Metric Applicability for Onocoy}` |
| Metric applicability framework | `personC_methodology.tex` | After line 176, before line 178 (between Principles and Core Metrics) | Yes — `\subsection{Metric Applicability Conditions}` |

---

*Cross-references: `output/md/Metric_Relevance_Matrix.md`, `output/md/Failure_Mode_Metric_Mapping.md`, `output/md/Stress_Scenario_Metric_Mapping.md`, `output/md/Depin_Metric_Applicability_Revelations.md` §4–7.*
