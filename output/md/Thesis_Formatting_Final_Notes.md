# Thesis Formatting: Final Notes (Widows, Whitespace, URLs)

**Date:** 2026-02-25
**Scope:** Full PDF build (`main.pdf`, 77 pages), `preamble.tex`, `bibliography.bib`, `main.log` warnings
**Method:** Clean rebuild via `latexmk -pdf main.tex`; log analysis; bibliography URL inventory

---

## 1. Widows and Orphans

### Preamble Settings

```
\widowpenalty=10000
\clubpenalty=10000
\displaywidowpenalty=10000
```

**Status:** ✅ All three penalties are set to maximum (10000) in `preamble.tex` lines 19–21. This is the strongest possible suppression — LaTeX will stretch or compress pages to avoid isolated lines at page boundaries.

### Build Verification

The `main.log` from a clean build contains **zero widow/orphan warnings**. The penalties are effective.

**No issues found. No fixes needed.**

---

## 2. Table and Figure Whitespace

### Float Spacing Settings

No `\intextsep`, `\textfloatsep`, `\floatsep`, `\abovecaptionskip`, or `\belowcaptionskip` overrides appear anywhere in `preamble.tex`, `main.tex`, or `sections/*.tex`. LaTeX class defaults apply.

**Status:** ✅ Consistent — no manual float-spacing overrides, so all 4 tables use identical spacing. No fixes needed for spacing consistency.

### Box Warnings Related to Tables

The `main.log` reports **6 underfull `\hbox`** warnings (4 at badness 10000) originating from the table in `personA_foundations.tex` lines 64–69 (Table `tab:stress_factors`).

| # | File | Line(s) | Current | Proposed | Rationale |
|:-:|:-----|:--------|:--------|:---------|:----------|
| 1 | `sections/personA_foundations.tex` | 60 | Column spec `{|p{0.25\linewidth}|p{0.4\linewidth}|p{0.25\linewidth}|}` — narrow third column (0.25) forces extreme line-breaking for short text fragments | Widen third column or switch to `tabularx` with `X` columns that auto-distribute width. See `Table_Formatting_Fixes.md` for full migration plan. | The "Risk Driver" column (0.25 linewidth) is too narrow for its content. Text like "If incentives flatten, mercenary supply churns immediately" produces badness-10000 underfull boxes because words cannot fill the line width. `tabularx` with proportional `X` columns eliminates this by distributing width dynamically. |

### Display Math Overflow

| # | File | Line | Current | Proposed | Rationale |
|:-:|:-----|:----:|:--------|:---------|:----------|
| 2 | `sections/personB_framework.tex` | 73–75 | `\[\text{Fiat/User Payment} \rightarrow \text{Protocol Settlement Layer} \rightarrow \text{Token Sink or Buy Pressure} \rightarrow \text{Net Supply Pressure}\]` — 76.9pt overfull (worst in thesis) | Break the chain across two lines using `\\` inside an `aligned` environment, or use `\begin{multline*}`. Alternatively, abbreviate labels (e.g. "Settlement Layer" → "Settlement"). | This single display-math expression extends 76.9pt (~27mm) beyond the right margin — the largest overflow in the entire thesis. It is a text-only chain with no mathematical content. Breaking it across two lines or abbreviating the labels resolves the overflow. |

---

## 3. Long URLs in Bibliography

### Preamble Settings

```
\urlstyle{same}
\setcounter{biburllcpenalty}{7000}
\setcounter{biburlucpenalty}{8000}
```

**Status:** ✅ URL line-breaking is configured. `\urlstyle{same}` prevents Courier-font URLs from blowing out line widths. The penalty counters allow breaks at lowercase (7000) and uppercase (8000) transitions, which is the standard biblatex approach.

### Build Warnings

4 overfull `\hbox` warnings originate from the bibliography (all at `lines 104--104` in the `.bbl` file, corresponding to bibliography entries). These are **title overflows**, not URL overflows — the URL break settings are working correctly.

| Warning | Width | Source Entry |
|:--------|:-----:|:-------------|
| CFA Institute: *Cryptoassets...* | 5.6pt | Title too long for single-column layout |
| Bernardineli: *...Scenarios in Filecoin* | 8.4pt | Title overflow |
| HackMD: *Simulating Token Economies* | 0.6pt | Marginal (visually invisible) |
| Gauntlet: *Financial Modeling and Simulation for Crypto* | 3.5pt | Title overflow |

**These are title-length overflows, not URL overflows.** The bibliography uses `\urlstyle{same}` and break penalties, so URLs wrap correctly. The title overflows are caused by long italicised titles that LaTeX cannot hyphenate within the biblatex numeric style.

### URL Length Inventory

| Category | Count |
|:---------|:-----:|
| Total URLs in `bibliography.bib` | 40 |
| URLs > 80 chars | 10 |
| URLs > 100 chars | 6 |
| URLs > 120 chars | 2 |
| Longest URL | 156 chars |

**Top 5 longest URLs:**

| Length | URL (truncated) | BibTeX Key (inferred) |
|:------:|:----------------|:---------------------|
| 156 | `https://www.bostonfed.org/-/media/Documents/events/2024/stress-testing-...` | Sarin (stress testing) |
| 121 | `https://medium.com/@done_71651/geodnet-geod-in-depth-research-report-...` | Geodnet research report |
| 107 | `https://www.rapidinnovation.io/post/depin-tokenomics-understanding-...` | RapidInnovation2024 |
| 107 | `https://sarsonfunds.com/heliums-exceptional-growth-in-2025-...` | Helium growth |
| 105 | `https://www.resonance.security/blog-posts/is-depin-just-another-...` | ResonanceSecurity2024 |

### URL Issues

| # | File | Location | Current | Proposed | Rationale |
|:-:|:-----|:---------|:--------|:---------|:----------|
| 3 | `bibliography.bib` | 10 entries | URLs > 80 chars, up to 156 chars | No code change needed — the `biburllcpenalty` / `biburlucpenalty` settings already handle line-breaking. If any specific URL still overflows in the PDF, add `\url{}` break hints or shorten the URL via a redirect service. | The current preamble settings are correct and working. The 4 bibliography overfull warnings are caused by long **titles**, not URLs. No URL-specific overflow was detected in the build output. |

---

## 4. General Overfull / Underfull Summary

Full build produced **28 box warnings** (21 overfull, 7 underfull):

| Severity | Count | Source | Action |
|:---------|:-----:|:-------|:-------|
| Critical (>20pt overfull) | 3 | Display math chain (76pt), `personC_results.tex` prose (21pt ×2) | Fix display math; check long paragraphs |
| Moderate (5–20pt overfull) | 7 | Long paragraphs in `personB_framework.tex`, `empirical_analysis.tex`, `personC_methodology.tex`, bibliography titles | Minor rewording or `\allowbreak` hints |
| Minor (<5pt overfull) | 11 | Various | Visually negligible; no action needed |
| Underfull (badness 10000) | 4 | `personA_foundations.tex` table narrow columns | Fix with `tabularx` migration (see `Table_Formatting_Fixes.md`) |
| Underfull (other) | 3 | `personA_foundations.tex` table, appendix | Low priority |

### Top 3 Priorities

| # | File | Issue | Fix |
|:-:|:-----|:------|:----|
| 1 | `personB_framework.tex` L73–75 | 76.9pt overfull display math | Break the `\text{...} \rightarrow` chain across 2 lines |
| 2 | `personA_foundations.tex` L60 | 4× badness-10000 underfull in table | Migrate to `tabularx` (per `Table_Formatting_Fixes.md`) |
| 3 | `personC_results.tex` L1019–1026 | 21.3pt overfull paragraph | Reword or add `\allowbreak` |

---

## Summary

| Category | Issues | Status |
|:---------|:------:|:------:|
| Widow/orphan penalties | 0 | ✅ Correctly set to 10000 |
| Float spacing overrides | 0 | ✅ No manual overrides — defaults consistent |
| Table column underfull | 4 warnings | Fix via `tabularx` migration |
| Display math overflow | 1 (76.9pt) | Break chain across 2 lines |
| Bibliography title overflow | 4 warnings | Minor; rewording or `\allowbreak` |
| URL line-breaking | 0 | ✅ Correctly configured; no URL overflows |
| Long URLs (>80 chars) | 10 entries | No action needed — breaks working |

**Overall:** The thesis typography is well-configured at the preamble level. The only structural issue is the 76.9pt display-math overflow in `personB_framework.tex`. The table underfull warnings are already captured in `Table_Formatting_Fixes.md` and resolve with the `tabularx` migration. Bibliography URL handling is correctly set up.

---

*Audited from clean `latexmk -pdf` build output (77 pages, 302 KB). Cross-references: `Table_Formatting_Fixes.md`, `Math_Formatting_Fixes.md`.*
