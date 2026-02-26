# Caption & Cross-Reference Audit

**Date:** 2026-02-25
**Scope:** All `\begin{table}` and `\begin{figure}` environments in `sections/*.tex`, `appendix.tex`, and `main.tex`
**Reference:** `CAS_FORMATTING_AND_STYLE.md` §6: "Every figure/table must be referenced in the text. Every figure/table must have a caption. Must state a source."

---

## Float Inventory

| # | Type | File | Lines | Caption | Label | `\ref` in text | Source note |
|:-:|:----:|:-----|:-----:|:-------:|:-----:|:--------------:|:----------:|
| T1 | Table | `personA_foundations.tex` | 56–73 | ✅ | ✅ `tab:stress_factors` | ✅ (L54) | ❌ |
| T2 | Table | `empirical_analysis.tex` | 69–90 | ✅ | ✅ `tab:comparative_metrics` | ❌ | ❌ |
| T3 | Table | `personC_results.tex` | 490–515 | ✅ | ✅ `tab:failure_modes` | ✅ (L488) | ❌ |
| T4 | Table | `personC_results.tex` | 1059–1085 | ✅ | ✅ `tab:archetypes` | ✅ (L1057) | ❌ |
| — | Figure | — | — | — | — | — | — |

**Zero figures exist** in the thesis. No `\begin{figure}` environment appears in any file.

---

## Issues Found

### Issue 1: Table T2 is not referenced in text

| Field | Value |
|:------|:------|
| **File** | `sections/empirical_analysis.tex` |
| **Location** | Lines 69–90 (Table `tab:comparative_metrics`, "Standardized Metrics for Comparison") |
| **Current** | The table has `\caption` and `\label{tab:comparative_metrics}`, but no `\ref{tab:comparative_metrics}` appears anywhere in the thesis. The introductory sentence (L67) reads: "To compare these diverse networks without simulation, we standardize specific metrics that serve as proxies for health and stress resilience" — then the table appears with no cross-reference. |
| **Proposed** | Add a reference in the introductory sentence, e.g.: "...we standardize specific metrics, summarised in Table~\ref{tab:comparative_metrics}, that serve as proxies for health and stress resilience." |
| **Rationale** | `CAS_FORMATTING_AND_STYLE.md` §6 requires every table to be referenced in the text. This is the thesis's primary metrics table, referenced in the supplementary `Onocoy_Applicability_Draft.tex` via `Table~\ref{tab:comparative_metrics}` but never in the thesis `.tex` files themselves. Without a `\ref`, the table floats unanchored. |

### Issue 2: No source attribution on any table

| Field | Value |
|:------|:------|
| **File** | All 4 tables (T1–T4) |
| **Location** | After each `\caption{}` line |
| **Current** | No table includes a source note. No instance of "Source:", "own illustration", "own compilation", or "own analysis" appears in any table or caption in the thesis. |
| **Proposed** | Add a source note below each caption. For author-created tables: `\smallskip\noindent\textit{Source: own illustration.}` For tables derived from literature: `\smallskip\noindent\textit{Source: compiled from [citations].}` |
| **Rationale** | `CAS_FORMATTING_AND_STYLE.md` §6 states: "Must state a source ('own illustration' if applicable)." All four tables are author-created compilations and should be marked accordingly. |

**Per-table proposed source notes:**

| Table | Proposed Source Text |
|:------|:--------------------|
| T1 (`tab:stress_factors`) | *Source: own illustration based on thesis theoretical framework.* |
| T2 (`tab:comparative_metrics`) | *Source: own illustration; metric definitions compiled from cited sources.* |
| T3 (`tab:failure_modes`) | *Source: own illustration based on simulation results.* |
| T4 (`tab:archetypes`) | *Source: own illustration based on empirical observation and simulation.* |

### Issue 3: Zero figures in the thesis

| Field | Value |
|:------|:------|
| **File** | `sections/personC_results.tex` |
| **Location** | Lines 65–73 (prose referencing figure conventions) |
| **Current** | The results chapter states: "All figures follow the same conventions: identical time horizons, shared axes where comparison is intended, and standardized scenario labels." However, no `\begin{figure}` environment exists anywhere in the thesis. |
| **Proposed** | Either add the planned figures or remove/qualify the prose referencing them. If figures are not yet ready, add a comment: `% TODO: Insert simulation output figures here`. |
| **Rationale** | `CAS_FORMATTING_AND_STYLE.md` §6 requires every figure to be captioned and referenced. Prose referencing non-existent figures creates an expectation the document does not fulfill. This is a content gap, not a formatting error — flagged for completeness. |

---

## Non-Issues (Compliant)

| Check | Status | Detail |
|:------|:------:|:-------|
| `\caption` present on all tables | ✅ | All 4 tables have captions. |
| `\label` present on all tables | ✅ | All 4 tables have labels. |
| `\label` placed after `\caption` | ✅ | Correct in all 4 tables (verified in `Table_Formatting_Fixes.md`). |
| T1 referenced in text | ✅ | `personA_foundations.tex` L54: `Table \ref{tab:stress_factors}` |
| T3 referenced in text | ✅ | `personC_results.tex` L488: `Table \ref{tab:failure_modes}` |
| T4 referenced in text | ✅ | `personC_results.tex` L1057: `Table \ref{tab:archetypes}` |
| No dangling `\ref` targets | ✅ | All 6 `\ref{}` targets found in the thesis resolve to existing `\label{}` commands. |

---

## All `\ref` Targets in the Thesis

| Target | Referenced From | Resolves To |
|:-------|:----------------|:------------|
| `tab:stress_factors` | `personA_foundations.tex` L54 | T1 caption |
| `tab:failure_modes` | `personC_results.tex` L488 | T3 caption |
| `tab:archetypes` | `personC_results.tex` L1057 | T4 caption |
| `sec:methodology` | `personC_methodology.tex` L117 | Section heading |
| `subsec:depin_cps` | `personC_methodology.tex` L24 | Subsection heading |
| `subsec:contributor_draft_archive` | 4 import files | Appendix subsection |

**No `\autoref` or `\eqref` commands are used anywhere.**

---

## Summary

| # | Issue | Severity | Files |
|:-:|:------|:--------:|:------|
| 1 | T2 (`tab:comparative_metrics`) not referenced in text | **Moderate** | `empirical_analysis.tex` |
| 2 | No source attribution on any table (0/4) | **Moderate** | All 4 table files |
| 3 | Zero figures despite prose referencing them | **Minor** (content gap) | `personC_results.tex` |

**3 of 4 tables are fully compliant** (caption + label + `\ref`). T2 is the only table missing a text reference. Source attribution is missing on all 4 tables — a single-pattern fix.

---

*Audited against `CAS_FORMATTING_AND_STYLE.md` §6 and internal `\ref` / `\label` consistency.*
