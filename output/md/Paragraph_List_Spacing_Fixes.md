# Paragraph, List, and Spacing Audit

**Date:** 2026-02-25
**Scope:** `main.tex`, `preamble.tex`, all files in `sections/` (including `import_*` files)

---

## 1. `\parskip` / `\parindent` Consistency

**Finding:** No `\parskip`, `\parindent`, or `\setlength{...par...}` commands appear anywhere in `preamble.tex`, `main.tex`, or any `sections/*.tex` file.

**Effect:** LaTeX defaults apply — `\parindent` is non-zero (standard first-line indent), `\parskip` is zero (no inter-paragraph space beyond normal baseline skip). Combined with `\onehalfspacing` from `setspace`, this produces standard academic paragraph formatting.

**Status:** ✅ Consistent. No manual overrides, so spacing is uniform across all sections. No fix needed.

---

## 2. List (`itemize` / `enumerate`) Spacing

**Inventory:** 49 list environments total (39 `itemize`, 10 `enumerate`) across 11 files.

**Finding:** No list environment uses custom spacing options (`[itemsep=...]`, `[topsep=...]`, etc.). No `\setlength` commands for `\itemsep`, `\topsep`, `\parsep`, or `\partopsep` appear anywhere. The `enumerate` package is loaded (not `enumitem`), so list-spacing customisation options are limited.

**Status:** ✅ Uniform — all lists use LaTeX default spacing. No deviations.

### One non-standard override

| # | File | Line | Current | Proposed | Rationale |
|:-:|:-----|:----:|:--------|:---------|:----------|
| 1 | `sections/personC_results.tex` | 36 | `\def\labelenumi{\arabic{enumi}.}` | `\begin{enumerate}[1.]` (using the `enumerate` package already loaded) | Raw `\def` overrides the label format globally for the remainder of the scope. The `enumerate` package provides `[1.]` as a clean per-environment option. Using `\def` is fragile and could leak into subsequent `enumerate` environments if scope is not carefully managed. |

---

## 3. `\vspace` Audit

| # | File | Line | Current | Proposed | Rationale |
|:-:|:-----|:----:|:--------|:---------|:----------|
| 2 | `main.tex` | 22 | `\vspace*{1cm}` | No change | Inside `titlepage` — standard for title layout. |
| 3 | `main.tex` | 26 | `\vspace{0.5cm}` | No change | Inside `titlepage` — subtitle spacing. |
| 4 | `main.tex` | 29 | `\vspace{1.5cm}` | No change | Inside `titlepage` — author block spacing. |
| 5 | `main.tex` | 40 | `\vspace{0.8cm}` | No change | Inside `titlepage` — date spacing. |
| 6 | `main.tex` | 56 | `\vspace{1cm} ` (with trailing space) | Remove entirely, or replace with `\vfill` | This `\vspace{1cm}` follows the Abstract and precedes the `% End of Abstract` comment. It creates a fixed 1 cm gap at the bottom of the abstract page. Since `\newpage` follows immediately (line 59), the space is invisible in output — it has no visual effect. The trailing whitespace is also a minor lint issue. If vertical fill is intended, `\vfill` is more idiomatic. |

**No `\vspace` commands appear in any `sections/*.tex` file.** All five instances are in `main.tex`, four of which are in the `titlepage` environment (standard and correct).

---

## 4. `\newline` in Prose

All 13 `\newline` instances are in `sections/personC_results.tex`, in the archetypes section (lines 1096–1182).

| # | File | Lines | Current | Proposed | Rationale |
|:-:|:-----|:-----:|:--------|:---------|:----------|
| 7 | `sections/personC_results.tex` | 1098, 1100, 1102 | `\textbf{Definition:} ...\newline\n\textbf{Rationale:} ...\newline\n\textbf{Interaction:} ...` | Replace each `\newline` with a blank line (standard paragraph break) or use `\paragraph{Definition}`, `\paragraph{Rationale}`, etc. | `\newline` forces a line break without inter-paragraph spacing. This produces tighter-than-normal layout that is visually inconsistent with the rest of the thesis, where blank lines create standard `\parskip`-separated paragraphs. The archetype definitions in §8 (lines 1096–1182) are the only place in the entire thesis where `\newline` is used in prose. |
| 8 | `sections/personC_results.tex` | 1115, 1117 | Same pattern in Archetype II-A | Same fix | Same rationale. |
| 9 | `sections/personC_results.tex` | 1127, 1129 | Same pattern in Archetype II-B | Same fix | Same rationale. |
| 10 | `sections/personC_results.tex` | 1139, 1141 | Same pattern in Archetype III | Same fix | Same rationale. |
| 11 | `sections/personC_results.tex` | 1146, 1148 | Same pattern in Archetype IV | Same fix | Same rationale. |
| 12 | `sections/personC_results.tex` | 1178, 1180 | Same pattern in Excluded Archetypes | Same fix | Same rationale. |

**Total:** 13 `\newline` instances, all in one section, all following the same `\textbf{Label:} text\newline` pattern. A single find-and-replace pass resolves all of them.

---

## 5. Forced Linebreaks (`\\`) in Prose

10 instances of `\\` used as paragraph separators in prose (outside tables, lists, and math environments), all in `sections/personC_results.tex`:

| # | File | Lines | Current | Proposed | Rationale |
|:-:|:-----|:-----:|:--------|:---------|:----------|
| 13 | `sections/personC_results.tex` | 694, 714, 735, 753, 773 | `Design implication:\\` followed by body text on next line | Replace with `\paragraph{Design implication.}` | `\\` after a label creates a forced linebreak with no inter-paragraph space and no indent on the continuation. `\paragraph{}` is the idiomatic LaTeX command for a run-in heading with proper spacing. This pattern is used 5 times across the "Implications for Builders" subsections. |
| 14 | `sections/personC_results.tex` | 815, 834, 854, 875, 893 | `Actionable suggestion:\\` followed by body text on next line | Replace with `\paragraph{Actionable suggestion.}` | Same rationale. This pattern is used 5 times across the "Implications for Onocoy" subsections. |

**Additionally**, the same `Label:\\` pattern appears in the failure-mode definitions:

| # | File | Lines | Current | Proposed | Rationale |
|:-:|:-----|:-----:|:--------|:---------|:----------|
| 15 | `sections/personC_results.tex` | 535, 553, 563, 582, 589, 608, 617, 635, 643, 661 | `Definition:\\ ...` and `Observed context:\\ ...` | Replace with `\paragraph{Definition.}` and `\paragraph{Observed context.}` | Same pattern — 10 instances across 5 failure-mode subsections. The `\\` produces a linebreak without proper paragraph spacing. |

**Total:** 20 instances of `Label:\\` in prose, all in `personC_results.tex`, all fixable with `\paragraph{}`.

---

## 6. Excessive Blank Lines

LaTeX treats multiple consecutive blank lines the same as one, so these have no output effect. However, they are a source-tidiness issue and can confuse diff tools.

| # | File | Lines | Count | Proposed | Rationale |
|:-:|:-----|:-----:|:-----:|:---------|:----------|
| 16 | `sections/personC_results.tex` | 10–12 | 3 | Collapse to 1 blank line | Between scope-contract comment and `\section`. |
| 17 | `sections/personC_results.tex` | 516–518 | 3 | Collapse to 1 blank line | After `\end{table}` (failure modes table). |
| 18 | `sections/personC_results.tex` | 1001–1007 | 7 | Collapse to 1 blank line | Between "Closing Positioning Note" and "Positioning of This Contribution". Largest gap in the codebase. |
| 19 | `sections/personC_results.tex` | 1051–1053 | 3 | Collapse to 1 blank line | Between "Positioning" subsection and archetypes `\section`. |
| 20 | `sections/personC_results.tex` | 1086–1088 | 3 | Collapse to 1 blank line | After archetypes summary table. |

**All 5 instances are in `personC_results.tex`.** No other file has 3+ consecutive blank lines.

---

## 7. `\hfill`, `\bigskip`, `\medskip`, `\smallskip`, `\noindent`

**Finding:** None of these commands appear in any `sections/*.tex` or `main.tex` file (outside of comments).

**Status:** ✅ Clean. No orphaned spacing commands.

---

## Summary

| Category | Issues | Files Affected |
|:---------|:------:|:---------------|
| `\parskip` / `\parindent` consistency | 0 | — |
| List spacing uniformity | 1 (`\def\labelenumi`) | `personC_results.tex` |
| Orphaned `\vspace` | 1 (ineffective `\vspace{1cm}` after Abstract) | `main.tex` |
| `\newline` in prose | 13 instances (1 pattern) | `personC_results.tex` |
| `\\` forced linebreaks in prose | 20 instances (3 label patterns) | `personC_results.tex` |
| Excessive blank lines | 5 runs (19 excess lines total) | `personC_results.tex` |
| `\hfill` / `\bigskip` / `\noindent` | 0 | — |
| **Total deviations** | **40** | **2 files** (`main.tex`, `personC_results.tex`) |

### Key Observation

**39 of 40 issues are in `personC_results.tex`.** This file was likely converted from a non-LaTeX source (Markdown or similar), which explains the `\newline`, `Label:\\`, `\def\labelenumi`, and excessive blank-line patterns. The rest of the thesis is clean.

### Fix Priority

| Priority | Issues | Action |
|:---------|:------:|:-------|
| **Single pass** | #7–15 (33 instances) | Replace all `\newline` and `Label:\\` patterns in `personC_results.tex` with `\paragraph{}` or blank-line paragraph breaks. |
| **Quick fix** | #1, #6 | Replace `\def\labelenumi` with `\begin{enumerate}[1.]`; remove or replace `\vspace{1cm}` after Abstract. |
| **Source tidiness** | #16–20 | Collapse excessive blank lines in `personC_results.tex`. |

---

*Audited against LaTeX paragraph/list spacing defaults and internal consistency across all thesis `.tex` files.*
