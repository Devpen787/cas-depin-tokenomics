# Table Formatting Fixes (No Edits Applied)

## TB-001 (Forced `[H]` table placement)
- **File:** `sections/empirical_analysis.tex`
- **Location:** Line 69
- **Current:**
```tex
\begin{table}[H]
```
- **Proposed:**
```tex
\begin{table}[ht]
```
- **Rationale:** `[H]` forces placement and can increase whitespace/float layout issues. The thesis already sets float placement defaults in `preamble.tex`; using `[ht]` is more consistent and typically yields better pagination.
- **Approved:** YES

