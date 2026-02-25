# Table Formatting Audit

**Date:** 2026-02-25
**Scope:** All `\begin{table}` environments in `sections/*.tex` and `appendix.tex`
**Tables found:** 4 (none in `appendix.tex`, `personB_framework.tex`, `personA_onocoy.tex`, `personC_methodology.tex`, or `import_*` files)

---

## Table Inventory

| # | File | Lines | Caption | Label | Environment |
|:-:|:-----|:-----:|:--------|:------|:------------|
| T1 | `sections/personA_foundations.tex` | 56–73 | Theoretical Definitions of Stress Factors | `tab:stress_factors` | `tabular` |
| T2 | `sections/empirical_analysis.tex` | 69–90 | Standardized Metrics for Comparison | `tab:comparative_metrics` | `tabular` |
| T3 | `sections/personC_results.tex` | 490–515 | Operational Failure Modes: Diagnostic Matrix | `tab:failure_modes` | `tabularx` |
| T4 | `sections/personC_results.tex` | 1059–1085 | Human Decision-Making Archetypes Under Stress | `tab:archetypes` | `tabularx` |

---

## Property Comparison

| Property | T1 | T2 | T3 | T4 | Consistent? |
|:---------|:--:|:--:|:--:|:--:|:-----------:|
| `booktabs` rules | No (`\hline` ×5) | No (`\hline` ×7) | Yes | Yes | **No** |
| `\caption` present | Yes | Yes | Yes | Yes | ✅ |
| `\label` present | Yes | Yes | Yes | Yes | ✅ |
| `\label` after `\caption` | Yes | Yes | Yes | Yes | ✅ |
| `\arraystretch` | 1.5 | 1.5 | 1.3 | 1.3 | **No** |
| Environment | `tabular` | `tabular` | `tabularx` | `tabularx` | **No** |
| Pipe separators `\|` | Yes | Yes | No | No | **No** |
| Placement | `[ht]` | `[ht]` | `[ht]` | `[ht]` | ✅ |
| `\centering` | Yes | Yes | Yes | Yes | ✅ |
| `\small` | Yes | Yes | Yes | Yes | ✅ |
| Row separation | `\hline` | `\hline` | `\addlinespace` | `\addlinespace` | **No** |
| Column spec style | `\|p{...}\|` | `\|p{...}\|` | `@{} >{\raggedright}X @{}` | `@{} >{\raggedright}X @{}` | **No** |

---

## Deviations

### Deviation 1: T1 uses `\hline` instead of `booktabs`

| Field | Value |
|:------|:------|
| **File** | `sections/personA_foundations.tex` |
| **Location** | Lines 56–73 (Table `tab:stress_factors`) |
| **Current** | `\hline` used 5 times (1 after header, 1 after each of 3 data rows, 1 as bottom rule). `tabular` with `\|p{...}\|` column spec. |
| **Proposed** | Replace opening `\hline` with `\toprule`, header-row `\hline` with `\midrule`, inter-row `\hline` with `\addlinespace`, closing `\hline` with `\bottomrule`. Remove pipe separators from column spec. Switch to `tabularx{\textwidth}` with `X` columns. |
| **Rationale** | `booktabs` is loaded in `preamble.tex` and used in T3/T4. `\hline` + pipes produce a boxed grid that is inconsistent with the professional open-rule style in the results chapter. |

### Deviation 2: T2 uses `\hline` instead of `booktabs`

| Field | Value |
|:------|:------|
| **File** | `sections/empirical_analysis.tex` |
| **Location** | Lines 69–90 (Table `tab:comparative_metrics`) |
| **Current** | `\hline` used 7 times. `tabular` with `\|p{...}\|` column spec. |
| **Proposed** | Same migration as T1: `\toprule` / `\midrule` / `\addlinespace` / `\bottomrule`. Remove pipes. Switch to `tabularx`. |
| **Rationale** | Same as T1. Additionally, this is the standardised metrics table referenced throughout the thesis — it should be the exemplar of the chosen table style. |

### Deviation 3: Inconsistent `\arraystretch`

| Field | Value |
|:------|:------|
| **File** | T1 (`personA_foundations.tex` L59), T2 (`empirical_analysis.tex` L72) vs T3 (`personC_results.tex` L493), T4 (`personC_results.tex` L1062) |
| **Location** | All 4 tables |
| **Current** | T1, T2: `\renewcommand{\arraystretch}{1.5}`. T3, T4: `\renewcommand{\arraystretch}{1.3}`. |
| **Proposed** | Standardise to `1.3` across all tables. |
| **Rationale** | `1.5` combined with `\onehalfspacing` (document-level 1.5× line spacing) produces excessive vertical padding in T1 and T2. The `1.3` used in T3/T4 is the better default when `booktabs` `\addlinespace` provides row separation. |

### Deviation 4: Inconsistent environment (`tabular` vs `tabularx`)

| Field | Value |
|:------|:------|
| **File** | T1 (`personA_foundations.tex`), T2 (`empirical_analysis.tex`) |
| **Location** | Lines 60 and 73 respectively |
| **Current** | `\begin{tabular}{|p{0.25\linewidth}|p{0.4\linewidth}|p{0.25\linewidth}|}` (T1). `\begin{tabular}{|p{0.23\linewidth}|p{0.27\linewidth}|p{0.42\linewidth}|}` (T2). |
| **Proposed** | Switch to `\begin{tabularx}{\textwidth}{@{} X X X @{}}` with `>{\raggedright\arraybackslash}` and `\hsize` overrides matching T3/T4 pattern. |
| **Rationale** | `tabularx` with `\textwidth` width ensures tables fill the text block consistently. The `p{fraction\linewidth}` approach in T1/T2 does not guarantee the table spans the full text width and is harder to maintain. `tabularx` is loaded in `preamble.tex` and is the convention in T3/T4. |

### Deviation 5: Pipe column separators in T1 and T2

| Field | Value |
|:------|:------|
| **File** | `sections/personA_foundations.tex` (L60), `sections/empirical_analysis.tex` (L73) |
| **Location** | Column spec in `\begin{tabular}` |
| **Current** | `\|p{...}\|p{...}\|p{...}\|` — vertical rules on all column borders |
| **Proposed** | Remove all `\|` separators. Use `@{}` padding instead (as in T3/T4). |
| **Rationale** | The `booktabs` documentation explicitly advises against vertical rules: "Never use vertical rules." Pipes combined with `\hline` create a boxed grid; `booktabs` rules with open sides are the professional standard and the convention already established in T3/T4. |

### Deviation 6: Inter-row separation style

| Field | Value |
|:------|:------|
| **File** | T1 (`personA_foundations.tex`), T2 (`empirical_analysis.tex`) |
| **Location** | Between data rows |
| **Current** | `\hline` between every row (full horizontal rule) |
| **Proposed** | Replace with `\addlinespace` (vertical whitespace between rows, no rule) |
| **Rationale** | T3 and T4 use `\addlinespace` for inter-row separation, which is the `booktabs` convention. Full `\hline` between every row is visually heavy and inconsistent with the rest of the thesis. |

---

## Non-Deviations (Compliant)

These properties are consistent across all 4 tables — no fixes needed:

| Property | Value | Status |
|:---------|:------|:------:|
| `\caption` present | All 4 tables | ✅ |
| `\label` present | All 4 tables | ✅ |
| `\label` after `\caption` | All 4 tables | ✅ |
| Placement specifier | `[ht]` in all 4 | ✅ |
| `\centering` | All 4 tables | ✅ |
| `\small` font size | All 4 tables | ✅ |
| Caption style (title case) | All 4 tables | ✅ |

---

## Proposed Target Style (Based on T3/T4)

The tables in `personC_results.tex` (T3, T4) represent the target style that T1 and T2 should be migrated to:

```latex
\begin{table}[ht]
    \centering
    \small
    \renewcommand{\arraystretch}{1.3}
    \begin{tabularx}{\textwidth}{@{}
        >{\raggedright\arraybackslash\hsize=...}X
        >{\raggedright\arraybackslash\hsize=...}X
        >{\raggedright\arraybackslash\hsize=...}X
    @{}}
        \toprule
        \textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
        \midrule
        Row 1 data & ... & ... \\
        \addlinespace
        Row 2 data & ... & ... \\
        \bottomrule
    \end{tabularx}
    \caption{...}
    \label{tab:...}
\end{table}
```

**Key properties:** `tabularx` full-width, `booktabs` rules only (no `\hline`, no pipes), `\addlinespace` between rows, `\arraystretch{1.3}`, `@{}` padding to eliminate outer margins.

---

## Fix Summary

| # | File | Issue | Severity |
|:-:|:-----|:------|:--------:|
| 1 | `personA_foundations.tex` | `\hline` → `booktabs` | Moderate |
| 2 | `empirical_analysis.tex` | `\hline` → `booktabs` | Moderate |
| 3 | All tables | `\arraystretch` 1.5 → 1.3 | Minor |
| 4 | `personA_foundations.tex`, `empirical_analysis.tex` | `tabular` → `tabularx` | Moderate |
| 5 | `personA_foundations.tex`, `empirical_analysis.tex` | Remove pipe separators | Moderate |
| 6 | `personA_foundations.tex`, `empirical_analysis.tex` | `\hline` between rows → `\addlinespace` | Minor |

All deviations are in T1 and T2 only. T3 and T4 are fully consistent and serve as the target style.

---

*Audited against `booktabs` best practices and internal consistency with `personC_results.tex` tables.*
