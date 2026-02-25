# Math Formatting Audit

**Date:** 2026-02-25
**Scope:** All `sections/*.tex` files (including `import_*` files)

---

## Inventory

| Category | Count | Files |
|:---------|:-----:|:------|
| Inline math (`$...$`) | ~32 expressions | `personA_foundations.tex`, `empirical_analysis.tex`, `personC_results.tex`, `import_personA_foundations_2026-02-22.tex` |
| Display math (`\[...\]`) | 2 | `personB_framework.tex` (L73–75), `personC_methodology.tex` (L207–209) |
| Numbered equations (`equation`, `align`) | 0 | — |
| Equation references (`\eqref`, `\ref{eq:}`) | 0 | — |
| `\mathrm` / `\operatorname` | 0 | — |
| Subscripts | 0 | — |

**Overall math usage is light.** The thesis uses math primarily for inline comparisons (`$< 1$`, `$> 0.1$`), arrows (`$\to$`), and two display-mode expressions.

---

## Issues Found

### Issue 1: Inline fraction should be display math

| Field | Value |
|:------|:------|
| **File** | `sections/empirical_analysis.tex` |
| **Location** | Line 144 |
| **Current** | `$\text{Ratio} = \frac{\text{Burn}}{\text{Mint}}$` — inline `$...$` containing `\frac{}{}` |
| **Proposed** | Move to display math: `\[\text{Ratio} = \frac{\text{Burn}}{\text{Mint}}\]` |
| **Rationale** | `\frac` renders at reduced size in inline mode, making the fraction hard to read. The expression is introduced as a standalone definition ("the primary indicator of long-term solvency:") followed by the formula, which is the natural pattern for display math. The two existing display-math expressions in the thesis (`personB_framework.tex` L73, `personC_methodology.tex` L207) follow this exact pattern — introductory sentence ending with colon, then `\[...\]`. |

### Issue 2: Arrow command inconsistency (`\to` vs `\rightarrow`)

| Field | Value |
|:------|:------|
| **File** | Multiple |
| **Location** | See table below |
| **Current** | `$\to$` used in `empirical_analysis.tex` and `personC_results.tex`; `$\rightarrow$` used in `import_personA_foundations_2026-02-22.tex` and `personB_framework.tex` display math |
| **Proposed** | Standardise on `\to` throughout |
| **Rationale** | `\to` and `\rightarrow` produce the same glyph, but using both is a source-level inconsistency. `\to` is the shorter, more idiomatic command for "maps to" / "leads to" in inline usage. The display-math expression in `personB_framework.tex` already uses `\rightarrow` for a chain of conceptual steps; `\to` would be equally correct and shorter. |

**Instance inventory:**

| File | Line(s) | Command | Count |
|:-----|:--------|:--------|:-----:|
| `sections/empirical_analysis.tex` | 135, 136, 162 | `$\to$` | 10 |
| `sections/personC_results.tex` | 506, 1074 | `$\to$` | 2 |
| `sections/personA_foundations.tex` | 68 | `$\to` (inside `$>10\%$ drop $\to >10\%$ churn`) | 1 |
| `sections/import_personA_foundations_2026-02-22.tex` | 40 | `$\rightarrow$` | 4 |
| `sections/personB_framework.tex` | 74 (display) | `\rightarrow` | 4 |

**Total:** 13 `\to`, 8 `\rightarrow`. Majority uses `\to`.

### Issue 3: Temporal variable formatting (`$T+30$`, `$T0$`)

| Field | Value |
|:------|:------|
| **File** | `sections/empirical_analysis.tex` |
| **Location** | Line 79 |
| **Current** | `$T+30$` and `$T0$` — bare italic letters with no subscript formatting |
| **Proposed** | `$T{+}30$` and `$T_0$` |
| **Rationale** | `$T0$` renders as italic-T followed by italic-zero, which looks like a product of two variables rather than "time zero". The subscript `$T_0$` is the standard mathematical convention for a reference time point. Similarly, `$T{+}30$` with braces around the plus prevents LaTeX from treating the plus as a binary operator with extra spacing. |

### Issue 4: Dollar-sign currency inside math mode

| Field | Value |
|:------|:------|
| **File** | `sections/empirical_analysis.tex` |
| **Location** | Line 96 |
| **Current** | `$\sim\$55$` and `$\$2$` — escaped dollar signs inside math mode to render currency |
| **Proposed** | Move currency outside math mode: `\$55` in text (or `{\sim}\$55` for the tilde) |
| **Rationale** | Using `$\sim\$55$` places the currency symbol in math-italic context, which is semantically incorrect (55 dollars is not a mathematical expression). The tilde `\sim` in math mode also produces a wider spacing than intended. The idiomatic approach is `{\sim}\$55` or simply `approximately \$55` in text. Line 100 (`$\sim\$500$`) has the same issue. |

### Issue 5: Display math used for non-mathematical text chain

| Field | Value |
|:------|:------|
| **File** | `sections/personB_framework.tex` |
| **Location** | Lines 73–75 |
| **Current** | `\[\text{Fiat/User Payment} \rightarrow \text{Protocol Settlement Layer} \rightarrow \text{Token Sink or Buy Pressure} \rightarrow \text{Net Supply Pressure}\]` |
| **Proposed** | No change required (acceptable) — but note that this is conceptual flow notation, not a mathematical equation. An alternative would be a centred text block without math mode. |
| **Rationale** | The content is entirely `\text{}` wrapped — no mathematical symbols or variables. Using `\[...\]` for a non-mathematical process diagram is a stylistic choice, not wrong, but worth noting for consistency. The arrows are the only math element. If changed, an unnumbered `\begin{quote}\centering` block with `$\to$` arrows would be equivalent. Low priority. |

### Issue 6: Percentage formatting inconsistency

| Field | Value |
|:------|:------|
| **File** | `sections/personA_foundations.tex`, `sections/empirical_analysis.tex` |
| **Location** | Lines 68 (foundations), 77, 79, 96 (empirical) |
| **Current** | `$>10\%$`, `$95\%$`, `$>20\%$`, `$< 0.1$` — percent sign inside math mode using `\%` |
| **Proposed** | No change required — `\%` in math mode is correct LaTeX |
| **Rationale** | `\%` renders correctly in math mode. The only minor note is that some style guides prefer `$> 10$\%` (number in math, percent in text), but the current approach is valid and internally consistent. |

### Issue 7: No equation numbering for referenced formulas

| Field | Value |
|:------|:------|
| **File** | `sections/personC_methodology.tex` |
| **Location** | Lines 207–209 (Incentive Efficiency formula) |
| **Current** | `\[\text{Efficiency} = \frac{\sum (\text{Emissions} \times \text{Price})}{\text{Total Capacity}}\]` — unnumbered display math |
| **Proposed** | If this formula is referenced elsewhere in the thesis, wrap in `\begin{equation}\label{eq:incentive_efficiency}...\end{equation}` |
| **Rationale** | Currently no equation is numbered in the thesis and no `\eqref` or `\ref{eq:}` references exist. If the Incentive Efficiency formula is referenced in the results chapter or discussion, it should be numbered for cross-referencing. If it is only defined once and not referenced, the current unnumbered `\[...\]` is acceptable. |

**Current status:** Neither display-math expression is referenced elsewhere. No fix needed unless references are added.

---

## Non-Issues (Compliant)

| Check | Status | Detail |
|:------|:------:|:-------|
| Multi-letter subscripts (`\mathrm`) | ✅ N/A | No subscripts are used anywhere in the thesis math. No `BMR_t`, `n_{sim}`, or similar expressions appear in `.tex` files (they are mentioned only in `THESIS_OS.md` as conceptual mappings, not in the LaTeX source). |
| `\text{}` in math mode | ✅ Correct | Both display-math expressions use `\text{}` for multi-word labels inside math mode, which is correct. |
| Inline vs display separation | ✅ Mostly correct | Simple comparisons (`$< 1$`, `$> 0.1$`) are correctly inline. Display math is used for standalone formulas. One exception: Issue 1 above. |
| `\emph` in math mode | ✅ Not present | No `\emph{}` or `\textit{}` appears inside math mode. |

---

## Summary

| # | File | Issue | Severity |
|:-:|:-----|:------|:--------:|
| 1 | `empirical_analysis.tex` L144 | Inline `\frac` → display math | Moderate |
| 2 | Multiple | `\to` vs `\rightarrow` inconsistency (13 vs 8) | Minor |
| 3 | `empirical_analysis.tex` L79 | `$T0$` → `$T_0$`; `$T+30$` → `$T{+}30$` | Minor |
| 4 | `empirical_analysis.tex` L96, L100 | `$\sim\$55$` — currency in math mode | Minor |
| 5 | `personB_framework.tex` L73–75 | Display math for non-mathematical text chain | Minor (acceptable) |
| 6 | Multiple | `\%` in math mode | ✅ Correct (no fix) |
| 7 | `personC_methodology.tex` L207–209 | Unnumbered display math | ✅ Correct (no references exist) |

**Total:** 4 actionable issues, 1 acceptable stylistic note, 2 confirmed non-issues.

### Key Observation

Math usage in this thesis is minimal and mostly correct. The codebase has zero subscripts, zero `\mathrm`, zero numbered equations, and zero equation references. The issues that do exist are concentrated in `empirical_analysis.tex` and relate to inline formatting of comparisons, currency values, and one misplaced fraction — all quick fixes.

---

*Audited against LaTeX math conventions and internal consistency across all thesis `.tex` files.*
