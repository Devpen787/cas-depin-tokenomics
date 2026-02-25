# Thesis Formatting Audit vs CAS_FORMATTING_AND_STYLE.md

**Date:** 2026-02-25
**Scope:** `main.tex`, `preamble.tex`, all files in `sections/`
**Reference:** `CAS_FORMATTING_AND_STYLE.md` (on `fix/repin-graph` branch)

---

## 1. Compliance (What Matches)

### §2 Document Layout

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| Paper size | A4 | `a4paper` in `\documentclass` and `geometry` | ✅ |
| Font size | 12pt | `12pt` in `\documentclass` | ✅ |
| Line spacing | 1.5 | `\onehalfspacing` via `setspace` | ✅ |
| Page numbers | Enabled, consistent placement | `\pagenumbering{roman}` / `\pagenumbering{arabic}` | ✅ |

### §5 Structure and Sectioning

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| Numbered sections | Yes | `secnumdepth=3`, `tocdepth=3` | ✅ |
| No results before methods | Correct ordering | `main.tex` includes methodology (Ch 5) before results (Ch 6) | ✅ |

### §6 Figures, Tables, and Visuals

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| Every table has a caption | Yes | All 4 tables have `\caption{}` | ✅ |
| Tables referenced in text | Yes | All 4 tables are referenced via `\ref{}` | ✅ |

### §7 Citations and References

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| Numeric style `[1]` | Yes | `style=numeric` in biblatex | ✅ |
| One style only | Yes | Only `\cite{}` used (78 instances). No mixed `\citep`/`\citet`. | ✅ |
| BibTeX management | `bibliography.bib` | `\addbibresource{bibliography.bib}` | ✅ |

### §4 Language and Tone

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| English, consistent variant | US or UK, consistent | US spelling used consistently (66 instances of `standardized`, `organized`, `behavior`, etc.; 0 British variants) | ✅ |
| Cautious verbs | Prefer "indicates", "suggests", etc. | 16 instances of cautious phrasing across thesis. Methodology and results chapters consistently use hedged language. | ✅ |
| No colour/decorative emphasis | No colours for emphasis | `hypersetup` sets all link colours to black. No `\textcolor` used in prose. | ✅ |

### §8 External Tools

| Convention | Required | Actual | Status |
|:-----------|:---------|:-------|:------:|
| AI not treated as primary source | Yes | No AI tool is cited as a primary source. | ✅ |
| Simulators cited as tools | Yes | DTSE and cadCAD are cited as methodological tools, not evidence. | ✅ |

---

## 2. Deviations (What Differs from the Style Guide)

### §2 Margins — DEVIATION

| Convention | Required | Actual | Severity |
|:-----------|:---------|:-------|:--------:|
| ~2.5 cm all sides | 2.5 cm | `geometry` sets `top=3cm, bottom=3cm, left=3cm, right=3cm` | **Moderate** |

**Detail:** The style guide specifies "approx. 2.5 cm on all sides". The thesis uses 3 cm on all sides — 20% wider than specified. This reduces the text area and may affect page count.

**Fix:** Change `preamble.tex` line 12 to `top=2.5cm, bottom=2.5cm, left=2.5cm, right=2.5cm`.

### §3 Font — DEVIATION

| Convention | Required | Actual | Severity |
|:-----------|:---------|:-------|:--------:|
| Computer Modern (LaTeX default) | Computer Modern | Times (`\usepackage{times}`), Courier, Helvetica | **Moderate** |
| No custom fonts | None | Three custom font packages loaded | **Moderate** |

**Detail:** `CAS_FORMATTING_AND_STYLE.md` §3 explicitly states "Main Text Font: Computer Modern (LaTeX default)" and "Custom Fonts: None." The thesis overrides this with `times`, `courier`, and `helvet`.

**Fix:** Remove lines 7–9 from `preamble.tex` to revert to Computer Modern.

### §3 Emphasis — DEVIATION

| Convention | Required | Actual | Severity |
|:-----------|:---------|:-------|:--------:|
| Italics only (no bold or colours for emphasis) | Italics only | `\textbf{}` used extensively for emphasis in prose | **Moderate** |

**Detail:** The style guide states "Emphasis: Italics only (no bold or colors for emphasis)." The thesis uses `\textbf{}` heavily for emphasis in running text — particularly in `empirical_analysis.tex` (labels like `\textbf{Context:}`, `\textbf{Helium's Response:}`, `\textbf{Assessment:}`) and `personC_results.tex` (archetype definitions like `\textbf{Definition:}`, `\textbf{Rationale at the Time:}`). Bold in table headers and `\item \textbf{...}` labels is standard and not a deviation, but bold used as inline emphasis in body paragraphs violates the convention.

**Affected files and approximate counts:**
- `sections/empirical_analysis.tex` — ~15 instances of bold-as-emphasis in prose
- `sections/personC_results.tex` — ~20 instances in archetype/failure-mode definitions
- `sections/personC_methodology.tex` — 1 instance (line 24, `\textbf{Cyber-Physical System}`)
- `sections/personA_foundations.tex` — bold in table cells only (acceptable)

**Fix:** Replace prose-level `\textbf{Label:}` patterns with `\emph{Label:}` or `\paragraph{Label}`. Keep `\textbf{}` in table headers and `\item` labels.

### §6 Table/Figure Source Attribution — DEVIATION

| Convention | Required | Actual | Severity |
|:-----------|:---------|:-------|:--------:|
| Must state source ("own illustration" if applicable) | Yes | No table includes source attribution | **Moderate** |

**Detail:** None of the 4 tables include a source note (e.g. "Source: own illustration" or "Source: compiled from [X]"). The style guide requires every figure/table to state a source.

**Fix:** Add `\smallskip\noindent\textit{Source: own illustration.}` or an appropriate attribution below each `\caption{}`.

### §6 Figures — DEVIATION

| Convention | Required | Actual | Severity |
|:-----------|:---------|:-------|:--------:|
| Every figure must be referenced and captioned | Yes | Zero `\begin{figure}` environments exist | **Minor** |

**Detail:** The thesis contains zero figures despite `personC_results.tex` referencing them in prose ("All figures follow the same conventions: identical time horizons, shared axes..."). This is a content gap rather than a formatting deviation — the figures are planned but not yet included.

### §7 Citation Note — INTERNAL INCONSISTENCY in Style Guide

| Convention | Style guide text |
|:-----------|:-----------------|
| Line 40 | "Style: Numeric (`[1]`, `[2]`) - Standard for technical/CS-related theses." |
| Line 44 | "Note: APA is chosen as a widely accepted academic standard; CAS permits consistent styles." |

**Detail:** The style guide references both numeric `[1]` and APA in the same section. The thesis correctly uses numeric. This is a style-guide inconsistency, not a thesis deviation.

---

## 3. Inconsistencies Across Sections

### Table Formatting — Mixed Conventions

| File | Table Style | Rules | Column Separators |
|:-----|:------------|:------|:------------------|
| `personA_foundations.tex` | `tabular` | `\hline` (6×) | Pipe `\|` |
| `empirical_analysis.tex` | `tabular` | `\hline` (7×) | Pipe `\|` |
| `personC_results.tex` (×2) | `tabularx` | `\toprule`/`\midrule`/`\bottomrule` | `@{}` padding |

**Issue:** Two table formatting conventions coexist. `personA_foundations` and `empirical_analysis` use the older `\hline` + pipe style, while `personC_results` uses professional `booktabs` rules. The `booktabs` package is loaded in `preamble.tex` but not used in all tables.

### Heading Hierarchy — Multiple Top-Level Sections in Single Files

| File | `\section{}` count | Expected |
|:-----|:------------------:|:--------:|
| `personC_methodology.tex` | 3 (`Methodology`, `Stress Scenario Design`, `Evaluation Metrics`) | 1 |
| `personC_results.tex` | 2 (`Simulation Results`, `Human Decision-Making Under Stress`) | 1 |

**Issue:** These files produce multiple numbered top-level chapters from a single `\input{}` call. Whether this is intentional or should be refactored into subsections is an authorial decision, but it creates an inconsistency where other section files (`personA_foundations`, `personB_framework`, `empirical_analysis`, `personA_onocoy`) each contain one `\section{}`.

### Emphasis Style — Mixed `\emph{}`, `\textit{}`, and `\textbf{}`

| Style | Count | Primary files |
|:------|:-----:|:--------------|
| `\emph{}` | 7 | `personC_methodology.tex`, `personC_results.tex` |
| `\textit{}` | 5 | `empirical_analysis.tex`, `personC_results.tex` |
| `\textbf{}` for emphasis | ~36 | `empirical_analysis.tex`, `personC_results.tex` |

**Issue:** Three emphasis mechanisms coexist. Per the style guide, only italics should be used, and `\emph{}` is the idiomatic LaTeX command for semantic emphasis (it adapts to context). `\textit{}` forces italics regardless of context. `\textbf{}` should not be used for emphasis per §3.

### Quoting Style — Mixed ASCII and LaTeX

| Style | Files |
|:------|:------|
| LaTeX curly quotes ` ``...'' ` | `personA_foundations.tex`, `personC_methodology.tex`, `personC_results.tex` |
| ASCII straight quotes `"..."` | `empirical_analysis.tex`, `personB_framework.tex` |

**Issue:** Two quoting conventions coexist. LaTeX curly quotes are correct; ASCII straight quotes produce visually wrong output in PDFs.

### Dash Style — Mixed Unicode and LaTeX

| Style | Files |
|:------|:------|
| Unicode em-dash `—` (U+2014) | `empirical_analysis.tex` (~15×), `personB_framework.tex` (3×), `personA_foundations.tex` (1×) |
| LaTeX em-dash `---` | None |
| En-dash `--` in ranges | `personC_results.tex` (e.g. `p25--p75`) |

**Issue:** The thesis uses Unicode em-dashes exclusively (no LaTeX `---` anywhere). While these render correctly with `\usepackage[utf8]{inputenc}`, LaTeX `---` is the portable convention. More importantly, no file uses `---`, so there is internal consistency but divergence from LaTeX convention.

### Paragraph Separators — `\newline` vs Blank Lines

| Style | File | Count |
|:------|:-----|:-----:|
| `\newline` | `personC_results.tex` | 13 |
| Blank lines (standard) | All other files | — |

**Issue:** `personC_results.tex` uses `\newline` to separate definition/rationale/interaction blocks in the archetypes section. All other files use standard blank-line paragraph breaks. `\newline` does not insert inter-paragraph spacing and produces tighter-than-normal layout.

### Tone — Occasional Strong Claims

| File | Line | Text | Issue |
|:-----|:-----|:-----|:------|
| `empirical_analysis.tex` | 173 | "Historical event studies prove *that* these failure modes exist" | "prove" is stronger than the style guide's cautious-verb recommendation |
| `empirical_analysis.tex` | 8 | "represent a fundamental shift" | Borderline promotional; "represent an emerging approach" would be more cautious |
| `empirical_analysis.tex` | 14 | "this report offers a nuanced framework" | Self-evaluative; let the reader judge |

**Note:** These are minor tone issues concentrated in `empirical_analysis.tex`. The methodology and results chapters (`personC_*`) use consistently cautious language.

---

## Summary

### By Severity

| Severity | Count | Items |
|:---------|:-----:|:------|
| **Moderate** | 4 | Margins (3 cm vs 2.5 cm), Font (Times vs Computer Modern), Bold emphasis in prose, Missing table source attribution |
| **Minor** | 7 | Mixed table styles, mixed heading hierarchy, mixed emphasis commands, mixed quoting, mixed dashes, `\newline` vs blank lines, occasional strong verbs |
| **Style-guide inconsistency** | 1 | Numeric vs APA note in §7 of the style guide itself |

### Compliance Score

| Category | Compliant | Deviant | Total |
|:---------|:---------:|:-------:|:-----:|
| §2 Document Layout | 3 | 1 (margins) | 4 |
| §3 Font/Typography | 1 (no colour) | 2 (font, bold emphasis) | 3 |
| §4 Language/Tone | 3 | 0 | 3 |
| §5 Structure | 2 | 0 | 2 |
| §6 Figures/Tables | 2 (captions, refs) | 2 (source attr, no figures) | 4 |
| §7 Citations | 3 | 0 | 3 |
| §8 External Tools | 2 | 0 | 2 |
| **Total** | **16** | **5** | **21** |

### Overall Assessment

The thesis is **largely compliant** with the CAS style guide — 16 of 21 audited conventions are met. The four moderate deviations (margins, font, bold emphasis, source attribution) are straightforward to fix. The cross-section inconsistencies (table styles, quoting, dashes, emphasis commands) are typical of multi-author LaTeX projects and are addressable in a single formatting pass. No critical or structural violations were found. The most impactful change would be reverting the font to Computer Modern and tightening margins to 2.5 cm, as these affect every page of the output.

---

*Audited against `CAS_FORMATTING_AND_STYLE.md` from `fix/repin-graph` branch.*
