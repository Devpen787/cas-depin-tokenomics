# Section Hierarchy Fixes (No Edits Applied)

## SH-001 (Numbering depth inconsistent with starred subsubsections)
- **File:** `main.tex`
- **Location:** Lines 7–8 (section numbering depth)
- **Current:**
```tex
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{3}
```
- **Proposed:**
```tex
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{2}
```
- **Rationale:** The thesis uses a mix of numbered `\subsubsection{...}` and unnumbered `\subsubsection*{...}` across chapters, which can create inconsistent numbering/ToC depth. Setting depth to `2` enforces the convention “numbered sections and subsections” while allowing subsubsections to remain structural but unnumbered.
- **Approved:** NO (This changes document-wide numbering and ToC behavior; confirm desired numbering policy first.)

