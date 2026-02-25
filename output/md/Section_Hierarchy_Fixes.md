# Section Hierarchy Audit

**Date:** 2026-02-25
**Scope:** `main.tex`, all files in `sections/` (including `import_*` files reached via `\input{}`)
**Method:** Automated traversal of the full document in `main.tex` include order, tracking heading levels and detecting skips, multi-section files, and orphaned paragraphs.

---

## Results Summary

| Check | Issues Found |
|:------|:------------:|
| Level skips (`\subsubsection` directly under `\section`, etc.) | 4 |
| Multi-`\section` files | 3 |
| Starred headings (`\section*`, etc.) used incorrectly | 0 |
| `\paragraph` without parent `\subsubsection` | 4 |
| Numbering depth inconsistency | 0 |
| **Total** | **11** |

---

## 1. Level Skips

All four level skips follow the same pattern: a `\paragraph{Traceability note.}` appears directly under a `\subsection{}` (level 2 → level 4, skipping level 3).

| # | File | Line | Current | Proposed | Rationale |
|:-:|:-----|:----:|:--------|:---------|:----------|
| 1 | `sections/import_personA_foundations_2026-02-22.tex` | 66 | `\paragraph{Traceability note.}` under `\subsection{Person A Draft Import}` | Remove `\paragraph{}` wrapper; use a bold or italic inline label instead (e.g. `\noindent\textit{Traceability note.}`) | `\paragraph` is a numbered level-4 heading. A traceability note is not a structural heading — it's a labelled remark. Using `\paragraph` here creates a phantom entry in the section hierarchy and skips level 3. |
| 2 | `sections/import_personB_framework_2026-02-22.tex` | 70 | `\paragraph{Traceability note.}` under `\subsection{Person B Draft Import}` | Same as above | Same pattern — traceability note is not a structural heading. |
| 3 | `sections/import_personA_onocoy_2026-02-22.tex` | 40 | `\paragraph{Traceability note.}` under `\subsection{Person A Onocoy Draft Import}` | Same as above | Same pattern. |
| 4 | `sections/import_personA_methodology_interviews_2026-02-22.tex` | 24 | `\paragraph{Traceability note.}` under `\subsection{Person A Interview Framing Import}` (via `personC_methodology.tex` L46) | Same as above | Same pattern. The parent `\subsection` is in `personC_methodology.tex`; the `\paragraph` is in the imported file, so the skip is only visible in the assembled document. |

**Root cause:** All four are identical — `\paragraph{Traceability note.}` used as a labelled remark rather than a structural heading. The fix is the same in all cases.

---

## 2. Multi-`\section` Files

Three files contain multiple `\section{}` commands, meaning a single `\input{}` call in `main.tex` produces multiple top-level numbered chapters.

| # | File | Line(s) | Current | Proposed | Rationale |
|:-:|:-----|:--------|:--------|:---------|:----------|
| 5 | `sections/personA_foundations.tex` | 4, 30, 50 | `\section{Introduction}`, `\section{DePIN Fundamentals}`, `\section{Theoretical Definitions of Stress}` | **Option A:** Split into 3 files (`personA_introduction.tex`, `personA_fundamentals.tex`, `personA_stress_definitions.tex`) with separate `\input{}` lines in `main.tex`. **Option B:** If these are intentionally one "Person A block", demote `DePIN Fundamentals` and `Theoretical Definitions of Stress` to `\subsection{}` under a single `\section{Foundations}`. | Convention in the rest of the thesis is one `\section` per file. Having three in one file is not structurally wrong but creates an inconsistency. If the three sections are meant to be independent top-level chapters, splitting files makes the structure explicit. If they are sub-parts of Person A's contribution, they should be subsections. |
| 6 | `sections/personC_methodology.tex` | 4, 99, 170 | `\section{Methodology: Simulation-Based Stress Testing}`, `\section{Stress Scenario Design}`, `\section{Evaluation Metrics}` | **Option A:** Split into 3 files. **Option B:** Demote `Stress Scenario Design` and `Evaluation Metrics` to `\subsection{}` under `Methodology`. | Same reasoning. `Stress Scenario Design` and `Evaluation Metrics` are methodological content — arguably subsections of the methodology chapter rather than independent chapters. Demoting them would make the methodology chapter internally complete and reduce the top-level section count. |
| 7 | `sections/personC_results.tex` | 13, 1054 | `\section{Simulation Results}`, `\section{Human Decision-Making Under Stress: DePIN Response Archetypes}` | **Option A:** Split archetypes into `sections/personC_archetypes.tex`. **Option B:** Demote archetypes to `\subsection{}` under Results. | The archetypes section is thematically distinct from simulation results (it introduces human-behavioural patterns). If it is a separate chapter, it should be a separate file. If it is part of the results discussion, it should be a subsection. |

**Note:** These are architectural decisions, not errors. The current structure compiles correctly and produces valid numbered sections. The issue is inconsistency with the one-section-per-file convention used by `personB_framework.tex`, `personA_onocoy.tex`, `empirical_analysis.tex`, and `appendix.tex`.

---

## 3. Starred Headings

| # | File | Line | Current | Proposed | Rationale |
|:-:|:-----|:----:|:--------|:---------|:----------|
| — | `main.tex` | 50 | `\section*{Abstract}` | No change needed | Correctly unnumbered. The Abstract should not appear in the numbered section hierarchy. This is standard LaTeX practice. |

**No issues found.** The only starred heading is the Abstract, which is correct.

---

## 4. `\paragraph` Without Parent `\subsubsection`

These are the same four traceability notes listed in §1. They are `\paragraph{}` commands whose nearest structural ancestor is a `\subsection{}`, skipping the `\subsubsection` level.

| # | File | Line | Current Parent | Issue |
|:-:|:-----|:----:|:---------------|:------|
| 8 | `import_personA_foundations_2026-02-22.tex` | 66 | `\subsection{Person A Draft Import}` | `\paragraph` under `\subsection` — skips `\subsubsection` |
| 9 | `import_personB_framework_2026-02-22.tex` | 70 | `\subsection{Person B Draft Import}` | Same |
| 10 | `import_personA_onocoy_2026-02-22.tex` | 40 | `\subsection{Person A Onocoy Draft Import}` | Same |
| 11 | `import_personA_methodology_interviews_2026-02-22.tex` | 24 | `\subsection{Person A Interview Framing Import}` | Same |

**Note:** The three `\paragraph{Archetype ...}` entries in `empirical_analysis.tex` (lines 48, 55, 61) are **not** issues — they correctly sit under `\subsubsection{The Comparative Set}` (level 3 → level 4, no skip).

---

## 5. Numbering Depth Consistency

| Setting | Value | Effect |
|:--------|:------|:-------|
| `\setcounter{secnumdepth}{3}` | 3 | Sections, subsections, and subsubsections are numbered. `\paragraph` is unnumbered. |
| `\setcounter{tocdepth}{3}` | 3 | Table of contents includes down to `\subsubsection`. `\paragraph` is excluded from ToC. |

**No issues found.** These settings are consistent with each other and with the thesis structure. The `\paragraph` commands (archetype labels, traceability notes) are intentionally excluded from numbering and ToC, which is correct for their usage.

---

## Fix Priority

| Priority | Issues | Action |
|:---------|:------:|:-------|
| **Quick fix** | #1–4, #8–11 | Replace `\paragraph{Traceability note.}` with `\noindent\textit{Traceability note.}` in all 4 import files. Eliminates all level skips and orphaned paragraphs. |
| **Architectural decision** | #5–7 | Decide whether multi-section files should be split or demoted. Does not affect compilation but affects structural consistency. Recommend discussing with co-authors before changing. |

---

*Audited using automated hierarchy traversal of the full document in `main.tex` include order.*
