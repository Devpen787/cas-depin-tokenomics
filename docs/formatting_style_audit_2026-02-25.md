# Formatting & Style Audit Report

**Date:** 2026-02-25
**Scope:** All `.tex` files in `sections/`, `main.tex`, and `preamble.tex`

---

## 1. Citation Formatting

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| Moderate | `sections/empirical_analysis.tex` | throughout | Uses ASCII straight double-quotes (`"..."`) for inline terms (e.g. `"Event Study Methodology"`, `"Equilibrium Price"`). | Replace with LaTeX curly quotes: ` ``...'' `. Other chapters already use ` ``...'' ` correctly. |
| Minor | `sections/personB_framework.tex` | 16, 22, 54, 60, 66 | Also uses ASCII `"..."` instead of ` ``...'' `. | Same fix as above. |
| Minor | All files with `\cite{}` | throughout | Citation placement is **consistently end-of-sentence** (e.g. `...under stress \cite{X}.`). No mid-sentence `\cite{}` instances found. Uniform and correct for `numeric` biblatex style. | No fix needed — consistent. |
| Minor | All files | throughout | Only `\cite{}` is used (78 instances). No `\citep`, `\citet`, `\autocite`, `\parencite`, or `\textcite` present. | No fix needed — consistent with `style=numeric` in preamble. |
| Minor | `main.tex` | 56 | Trailing space after `\vspace{1cm}` on the Abstract closing line: `\vspace{1cm} `. | Remove trailing whitespace. |

---

## 2. Table and Figure Style

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| Moderate | `sections/personA_foundations.tex` | 56–73 | Table uses `\hline` throughout (6 instances). | Replace with `\toprule`, `\midrule`, `\bottomrule` from `booktabs` (already loaded in preamble). |
| Moderate | `sections/empirical_analysis.tex` | 69–90 | Table uses `\hline` throughout (7 instances). | Same — migrate to `booktabs` rules. |
| ✅ Correct | `sections/personC_results.tex` | 490–515, 1059–1085 | Both tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`, `\addlinespace`) and `tabularx`. | No fix needed — this is the target style. |
| Moderate | Mixed | — | **Inconsistent table framework:** `personA_foundations` and `empirical_analysis` use `tabular` + `\hline` + pipe column separators (`\|p{...}\|`); `personC_results` uses `tabularx` + `booktabs` + `@{}` padding. | Standardise all tables to `tabularx` + `booktabs`. Remove all pipe separators. |
| Minor | All tables | — | All four tables use `[ht]` placement. | Consistent — no fix needed. |
| Minor | All tables | — | Caption style is **title case** throughout (e.g. "Theoretical Definitions of Stress Factors"). | Consistent — no fix needed, but check submission guidelines for sentence-case requirements. |
| Minor | No files | — | **Zero `\begin{figure}` environments** exist in the thesis. The results chapter references figures in prose ("All figures follow the same conventions...") but none are included. | Flag for content review — figures are expected but missing. |

---

## 3. Section and List Formatting

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| Moderate | `sections/personC_methodology.tex` | 99, 170 | Contains 3 `\section{}` commands in a single file (`Methodology`, `Stress Scenario Design`, `Evaluation Metrics`). These render as top-level numbered sections. | Verify intentionality. If these should be sub-sections of the methodology chapter, downgrade to `\subsection`. |
| Moderate | `sections/personC_results.tex` | 13, 1054 | Contains 2 `\section{}` commands (`Simulation Results`, `Human Decision-Making Under Stress`). | Same — verify whether the archetypes section is a separate top-level chapter or a subsection of results. |
| Minor | `sections/personC_results.tex` | 36 | Uses `\def\labelenumi{\arabic{enumi}.}` to override `enumerate` numbering. | Use `\begin{enumerate}[1.]` (the `enumerate` package is already loaded) instead of raw `\def`. |
| Minor | `sections/personC_results.tex` | 535, 553, 563, 582, 589, 608, 617, 635, 643, 661 | Uses bare `Definition:\\` and `Observed context:\\` patterns — label followed by `\\` linebreak for inline definitions. | Use `\paragraph{Definition.}` or a custom environment for consistency. No other file uses this pattern. |
| Minor | `sections/personC_results.tex` | 694, 714, 735, 753, 773, 815, 834, 854, 875, 893 | Uses bare `Design implication:\\` and `Actionable suggestion:\\` patterns with forced linebreaks. | Same — `\paragraph{}` would be more idiomatic and avoids manual spacing. |
| Minor | `sections/personC_results.tex` | 1098–1180 | Uses `\newline` (13 instances) as paragraph separator between definition/rationale/interaction subsections within archetypes. | Replace with blank lines (paragraph breaks) or `\paragraph{}` commands. `\newline` does not insert proper paragraph spacing. |

---

## 4. Spacing and Typography

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| Moderate | `sections/empirical_analysis.tex` | 8, 10, 12, 32–34, 38, 40, 103, 126, 170 | Uses **Unicode em-dash** character `—` (U+2014) instead of LaTeX `---`. ~15 instances. | Replace with `---`. |
| Minor | `sections/personB_framework.tex` | 16, 22, 54 | Also uses Unicode em-dash `—`. | Same fix. |
| Minor | `sections/personA_foundations.tex` | 15 | One Unicode em-dash instance. | Same fix. |
| Minor | `preamble.tex` | 67 | Extra blank line between `lstdefinestyle` closing brace and `% Hyperref setup` comment. | Remove one blank line. |
| Minor | `sections/personC_results.tex` | 1002–1007, 1052–1053 | Multiple consecutive blank lines (4–6) between sections. | Collapse to single blank lines. |
| Minor | — | — | No raw `...` ellipsis or `\ldots` found anywhere. | Clean — no fix needed. |
| Minor | — | — | No `---` LaTeX em-dashes found — codebase uses only Unicode `—`. Internally consistent within `empirical_analysis.tex` and `personB_framework.tex` but differs from chapters that avoid dashes entirely. | Pick one convention and apply globally. LaTeX `---` is the safer choice for portability. |

---

## 5. Terminology and Lexicon

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| ✅ None | All `.tex` files | — | **ORSTE does not appear** in any `.tex` file. DTSE is used correctly everywhere it appears. | No fix needed. |
| Minor | `sections/empirical_analysis.tex` | 133, 155 | Uses plural **"DePINs"** (2 instances). | Standardise to "DePIN networks" if the style prefers invariant "DePIN". |
| Minor | `sections/personC_results.tex` | 1099, 1171 | Uses **"DePINs"** (2 more instances). | Same. |
| Moderate | `sections/personC_methodology.tex`, `sections/personC_results.tex` | throughout | DTSE is **never named** in these chapters despite them defining and executing the simulation the DTSE describes. They use only generic phrasing: "simulation framework", "this model", "the framework". | Add at least one introductory reference to DTSE, e.g. "...the DePIN Tokenomic Stress Evaluator (DTSE) framework described in Section 4". |

---

## 6. Comment and Tag Consistency

| Severity | File | Lines | Issue | Suggested Fix |
|----------|------|-------|-------|---------------|
| ✅ Minor | 6 files | line 1 each | `% SCOPE CONTRACT:` headers are applied consistently to all main chapters and `empirical_analysis.tex`. | No fix needed — well-maintained convention. |
| Minor | `sections/personC_results.tex` | 1–9 | Has an extended multi-line `% MUST: / MUST NOT:` comment block unique to this file. Other scope contracts are 1–2 lines. | Consider standardising or removing — reads as a development note rather than a permanent marker. |
| ✅ None | All files | — | **No `% ARCHIVE-CITE-NOTE:` tags exist** anywhere. All citation-pending markers use the standard `% TODO-CITE:` pattern. | Clean — no fix needed. |
| ✅ Minor | Import files | headers | The 4 `import_*.tex` files all have a consistent `% Provisional source-preserving import` header pattern. | No fix needed. |

---

## Summary

| Severity | Count |
|----------|-------|
| **Critical** | 0 |
| **Moderate** | 7 |
| **Minor** | 22 |

### Overall Assessment

The thesis codebase is in good structural health for an active multi-author collaborative draft. The most impactful formatting inconsistency is the **split between `\hline`-based tables** (`personA_foundations`, `empirical_analysis`) **and `booktabs`-based tables** (`personC_results`); this is straightforward to unify. The **Unicode em-dash vs. LaTeX `---`** split and **ASCII `"..."` vs. TeX ` ``...'' `** quoting inconsistency are the main typography issues — both are concentrated in `empirical_analysis.tex` and `personB_framework.tex`, suggesting those chapters were drafted in an environment that auto-substituted characters.

The `\newline` / `Definition:\\` patterns in `personC_results.tex` are functional but non-idiomatic and would benefit from `\paragraph{}` wrappers. Critically, **no ORSTE terminology drift exists**, citation style is uniform (`\cite{}` + `numeric`), and the `% TODO-CITE:` / `% SCOPE CONTRACT:` conventions are cleanly maintained.

The most substantive content-level finding is the **absence of the DTSE name in Chapters 5–6** despite those chapters implementing the simulation it describes.

---

### Quick-Fix Checklist

- [ ] Migrate `personA_foundations.tex` and `empirical_analysis.tex` tables from `\hline` to `booktabs`
- [ ] Replace Unicode em-dashes (`—`) with LaTeX `---` globally
- [ ] Replace ASCII `"..."` with ` ``...'' ` in `empirical_analysis.tex` and `personB_framework.tex`
- [ ] Replace `\newline` with `\paragraph{}` or blank lines in `personC_results.tex` archetypes section
- [ ] Add explicit DTSE naming in `personC_methodology.tex` and `personC_results.tex`
- [ ] Standardise "DePINs" → "DePIN networks" (4 instances across 2 files)
- [ ] Remove trailing whitespace on `main.tex` line 56
- [ ] Collapse excessive blank lines in `personC_results.tex`
- [ ] Verify `\section{}` hierarchy in `personC_methodology.tex` (3 sections) and `personC_results.tex` (2 sections) is intentional
