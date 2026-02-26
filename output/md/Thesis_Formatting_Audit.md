# Thesis Formatting Audit (No Edits Applied)

This report lists formatting deviations and consistency issues observed in `main.tex`, `preamble.tex`, and `sections/*.tex` relative to `CAS_FORMATTING_AND_STYLE.md`. No `.tex` files were modified.

## TF-AUDIT-001 (Font stack conflicts with stated default)
- **File:** `preamble.tex`
- **Location:** Lines 6–9 (font packages)
- **Current:**
```tex
% Fonts: Time-tested academic choices (Times-like)
\usepackage{times}     % Use Times font for text (simpler, avoids math font errors)
\usepackage{courier}  % Courier for monospace
\usepackage{helvet}   % Helvetica for sans-serif
```
- **Proposed:**
```tex
% Fonts: LaTeX default (Computer Modern)
% (Remove explicit Times/Courier/Helvetica packages to align with CAS_FORMATTING_AND_STYLE.md defaults)
```
- **Rationale:** `CAS_FORMATTING_AND_STYLE.md` states “Main Text Font: Computer Modern (LaTeX default)”. The current preamble forces Times/Courier/Helvetica, which is inconsistent with that stated convention and affects the entire compiled document.
- **Approved:** NO (Global typography change; likely intentional and should be confirmed by authors before altering.)

## TF-AUDIT-002 (Caption label bolding vs “italics-only” emphasis rule)
- **File:** `preamble.tex`
- **Location:** Line 34 (`caption` package options)
- **Current:**
```tex
\usepackage[font=small,labelfont=bf]{caption}
```
- **Proposed:**
```tex
\usepackage[font=small]{caption}
```
- **Rationale:** If the thesis convention is “italics only” for emphasis, bold caption labels may be considered a deviation. Removing `labelfont=bf` makes caption labels consistent with non-bold text styling.
- **Approved:** NO (Policy-level style choice; caption label bolding is also a common academic convention—needs author decision.)
