# Thesis Formatting Audit Prompts (Audit-Only, No Edits)

**Purpose:** Produce reports of potential formatting changes. No edits to `.tex` files. Codex reviews and approves before any changes are applied.

**Workflow:**
1. Run these prompts → agents produce reports in `output/md/`
2. Codex reads reports → approves or rejects each proposed change
3. Separate "apply" step (manual or approved agent) → edits only approved items

**Output format for each report:** Use this structure so Codex can approve item-by-item:

```markdown
## [Change ID]
- **File:** `path/to/file.tex`
- **Location:** Line X (or "Section Y")
- **Current:** [exact current text/code]
- **Proposed:** [exact proposed replacement]
- **Rationale:** [why this change]
- **Approved:** [ ] (Codex fills this)
```

---

## Prompt 1: Full Formatting Audit

```
Audit the thesis LaTeX files (main.tex, preamble.tex, sections/*.tex) against CAS_FORMATTING_AND_STYLE.md. Produce a checklist report listing: (1) compliance items (what matches), (2) deviations (what differs from the style guide), and (3) inconsistencies across sections (e.g. table formatting, heading levels, list styles). Do NOT edit any files. Output to output/md/Thesis_Formatting_Audit.md.
```

---

## Prompt 2: Section Hierarchy Audit

```
Audit section hierarchy in sections/*.tex and main.tex. Check: (1) no section jumps levels (e.g. \subsubsection directly under \section), (2) numbering depth is consistent, (3) \subsubsection* is used only where unnumbered is intended. For each issue found, output in the format:
- **File:** path
- **Location:** line/section
- **Current:** [exact LaTeX]
- **Proposed:** [exact replacement]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Section_Hierarchy_Fixes.md.
```

---

## Prompt 3: Table Formatting Audit

```
Audit all tables in sections/*.tex and appendix.tex. For each table, check: (1) booktabs (\toprule, \midrule, \bottomrule), (2) \caption present, (3) \label after \caption, (4) consistent \arraystretch and column specs. For each deviation, output:
- **File:** path
- **Location:** line number or table label
- **Current:** [relevant snippet]
- **Proposed:** [exact replacement]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Table_Formatting_Fixes.md.
```

---

## Prompt 4: Paragraph and List Spacing Audit

```
Audit paragraph spacing, list spacing, and first-line indentation across sections/*.tex. Check: (1) \parskip or equivalent consistency, (2) itemize/enumerate spacing uniform, (3) no orphaned \vspace or \hfill creating visual gaps. For each issue:
- **File:** path
- **Location:** line/section
- **Current:** [snippet]
- **Proposed:** [replacement]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Paragraph_List_Spacing_Fixes.md.
```

---

## Prompt 5: Math and Inline Formatting Audit

```
Audit math usage in sections/*.tex: (1) inline math \( \) vs display \[ \], (2) consistent \mathrm for multi-letter subscripts (e.g. BMR_t), (3) equation numbering where equations are referenced. For each issue:
- **File:** path
- **Location:** line
- **Current:** [snippet]
- **Proposed:** [replacement]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Math_Formatting_Fixes.md.
```

---

## Prompt 6: Figure and Table Caption/Reference Audit

```
Per CAS_FORMATTING_AND_STYLE.md: every figure/table must have a caption and be referenced in text. Audit sections/*.tex and appendix.tex. For each figure and table, verify: (1) \caption exists, (2) \label exists, (3) at least one \ref or \autoref in body text. For each missing item:
- **File:** path
- **Location:** figure/table label or line
- **Current:** [what exists]
- **Proposed:** [exact LaTeX to add, with placement]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Caption_Reference_Fixes.md.
```

---

## Prompt 7: Final Readability Audit

```
After reviewing the compiled PDF (or inferring from source), audit for: (1) widows/orphans, (2) table/figure whitespace, (3) long URLs in bibliography. For each issue:
- **File:** path (or "preamble" / "compiled output")
- **Location:** section or element
- **Current:** [description]
- **Proposed:** [preamble tweak or note]
- **Rationale:** [why]
Do NOT edit any .tex files. Output to output/md/Thesis_Formatting_Final_Notes.md.
```

---

## Codex Approval Prompt (Run After Audits)

```
Read the following audit reports in output/md/:
- Thesis_Formatting_Audit.md
- Section_Hierarchy_Fixes.md
- Table_Formatting_Fixes.md
- Paragraph_List_Spacing_Fixes.md
- Math_Formatting_Fixes.md
- Caption_Reference_Fixes.md
- Thesis_Formatting_Final_Notes.md

For each proposed change, add "**Approved:** YES" or "**Approved:** NO" with a brief reason if NO. Output the approved subset to output/md/Thesis_Formatting_Approved_Changes.md in the same structured format, including only items marked Approved: YES. Do NOT apply any changes to .tex files.
```

---

## Apply Prompt (Run Only After Codex Approval)

**Apply to a duplicate branch first—original thesis stays untouched.**

```
Before applying any changes:
1. Create and checkout a new branch: git checkout -b formatting/formatting-preview
2. This branch is a duplicate of your current state; the original branch (e.g. fix/repin-graph or main) is unchanged.

Then:
Read output/md/Thesis_Formatting_Approved_Changes.md. Apply ONLY the changes listed there, exactly as specified, to the files on the formatting/formatting-preview branch. Do not apply any change not in the approved list. After each edit, verify the thesis still compiles (e.g. pdflatex or latexmk). Output a summary of applied changes to output/md/Thesis_Formatting_Applied_Summary.md.

The user can then:
- Compile the PDF from formatting/formatting-preview and review
- Run git diff fix/repin-graph (or main) to see all changes
- If satisfied: git checkout fix/repin-graph && git merge formatting/formatting-preview
- If not: git checkout fix/repin-graph && git branch -D formatting/formatting-preview (discard the branch)
```

---

## Quick Reference: All Prompts (Copy-Paste)

### Prompt 1: Full Formatting Audit
```
Audit the thesis LaTeX files (main.tex, preamble.tex, sections/*.tex) against CAS_FORMATTING_AND_STYLE.md. Produce a checklist report listing: (1) compliance items (what matches), (2) deviations (what differs from the style guide), and (3) inconsistencies across sections (e.g. table formatting, heading levels, list styles). Do NOT edit any files. Output to output/md/Thesis_Formatting_Audit.md.
```

### Prompt 2: Section Hierarchy Audit
```
Audit section hierarchy in sections/*.tex and main.tex. Check: (1) no section jumps levels (e.g. \subsubsection directly under \section), (2) numbering depth is consistent, (3) \subsubsection* is used only where unnumbered is intended. For each issue found, output in the format: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Section_Hierarchy_Fixes.md.
```

### Prompt 3: Table Formatting Audit
```
Audit all tables in sections/*.tex and appendix.tex. For each table, check: (1) booktabs (\toprule, \midrule, \bottomrule), (2) \caption present, (3) \label after \caption, (4) consistent \arraystretch and column specs. For each deviation, output: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Table_Formatting_Fixes.md.
```

### Prompt 4: Paragraph and List Spacing Audit
```
Audit paragraph spacing, list spacing, and first-line indentation across sections/*.tex. Check: (1) \parskip or equivalent consistency, (2) itemize/enumerate spacing uniform, (3) no orphaned \vspace or \hfill creating visual gaps. For each issue output: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Paragraph_List_Spacing_Fixes.md.
```

### Prompt 5: Math and Inline Formatting Audit
```
Audit math usage in sections/*.tex: (1) inline math \( \) vs display \[ \], (2) consistent \mathrm for multi-letter subscripts (e.g. BMR_t), (3) equation numbering where equations are referenced. For each issue output: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Math_Formatting_Fixes.md.
```

### Prompt 6: Figure and Table Caption/Reference Audit
```
Per CAS_FORMATTING_AND_STYLE.md: every figure/table must have a caption and be referenced in text. Audit sections/*.tex and appendix.tex. For each figure and table, verify: (1) \caption exists, (2) \label exists, (3) at least one \ref or \autoref in body text. For each missing item output: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Caption_Reference_Fixes.md.
```

### Prompt 7: Final Readability Audit
```
Audit for: (1) widows/orphans, (2) table/figure whitespace, (3) long URLs in bibliography. For each issue output: File, Location, Current, Proposed, Rationale. Do NOT edit any .tex files. Output to output/md/Thesis_Formatting_Final_Notes.md.
```

### Codex Approval Prompt
```
Read the audit reports in output/md/: Thesis_Formatting_Audit.md, Section_Hierarchy_Fixes.md, Table_Formatting_Fixes.md, Paragraph_List_Spacing_Fixes.md, Math_Formatting_Fixes.md, Caption_Reference_Fixes.md, Thesis_Formatting_Final_Notes.md. For each proposed change, add Approved: YES or NO with brief reason if NO. Output approved subset to output/md/Thesis_Formatting_Approved_Changes.md. Do NOT apply any changes to .tex files.
```

### Apply Prompt (to duplicate branch)
```
Create branch: git checkout -b formatting/formatting-preview. Read output/md/Thesis_Formatting_Approved_Changes.md. Apply ONLY approved changes to files on this branch. Verify thesis compiles. Output summary to output/md/Thesis_Formatting_Applied_Summary.md. Original branch remains untouched.
```

---

*Generated 2026-02-25. Part of thesis formatting workflow.*
