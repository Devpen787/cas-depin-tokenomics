# Math Formatting Fixes (No Edits Applied)

## MF-001 (Inline math uses `$...$` instead of `\\( ... \\)`)
- **File:** `sections/personA_foundations.tex`
- **Location:** Line 83 (inside Table `tab:stress_factors`)
- **Current:**
```tex
High fragility implies that price drops trigger immediate hardware churn ($>10\%$ drop $\to >10\%$ churn).
```
- **Proposed:**
```tex
High fragility implies that price drops trigger immediate hardware churn (\(>10\%\) drop \(\to\) \(>10\%\) churn).
```
- **Rationale:** Elsewhere the thesis primarily uses `\(...\)` for inline math. Standardizing reduces mixed inline-math styles and avoids edge cases with `$` inside tables/captions.
- **Approved:** YES

