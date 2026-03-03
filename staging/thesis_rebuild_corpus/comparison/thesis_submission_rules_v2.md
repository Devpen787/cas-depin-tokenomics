# Thesis Submission Rules V2

Status: synthesis reference
Date captured: 2026-02-28
Mode: `MODE: SYNTHESIS`

## Purpose

This document consolidates the thesis compliance expectations currently distributed across:

- `CAS_COMPLIANCE_CHECKLIST.md`
- `CAS_RULES.md`
- `CAS_FORMATTING_AND_STYLE.md`

Its purpose is to give the V2 rebuild one authoritative rules reference that distinguishes:

1. hard CAS / HSLU requirements
2. project defaults already chosen by the authors
3. derived formatting conventions
4. open verification points that should not be mistaken for settled rules

This file is not a replacement for the source documents. It is the working compliance map for the rebuild.

## A. Hard CAS / HSLU Requirements

These should be treated as non-negotiable unless superseded by more recent official program guidance.

### A1. Core Submission Artifacts

- A final thesis PDF must exist.
- A separate `Arbeitsjournal` must exist and be submitted with the thesis.
- Group work must preserve identifiable individual contribution.

### A2. Minimum Academic Structure

The thesis must clearly contain:

- starting position / context
- problem statement
- goals
- scientific methods
- main analytical / empirical / design work
- interpretation / discussion
- conclusion

### A3. Scientific Standards

- Claims must be traceable and checkable.
- Methods must be named, justified, and actually applied.
- Assumptions must be explicit where relevant.
- Sources must be cited transparently.
- Direct quotes and paraphrases must both be cited correctly.
- Plagiarism is unacceptable.

### A4. AI Usage

- If AI was used, a disclosure statement must exist.
- If AI was not used, an explicit no-AI statement should exist.
- AI does not replace substantial personal contribution.

### A5. Title Page / Declaration / Classification

- Title page must exist.
- Declaration of originality / independent work must exist.
- Confidentiality classification must be clear in the submitted materials.

### A6. Submission / Presentation

- Submission is electronic via the CAS process.
- Presentation is part of completion.
- Confidential work still must be presented in an anonymized or suitably adapted way if needed.

### A7. Document Hygiene

- No unresolved citations or references.
- No placeholder text such as `TODO`, `TBD`, or equivalent.
- No LaTeX compile errors in the final build.
- Figures and tables must be numbered, captioned, and referenced in the text.

## B. Chosen Project Defaults

These are not necessarily universal CAS rules, but they are current project-level decisions and should be treated as fixed unless deliberately changed.

### B1. Language and Tone

- Thesis language: English.
- Tone: academic, neutral, non-promotional.
- Avoid marketing or speculative language.
- Prefer cautious verbs such as `indicates`, `suggests`, `is consistent with`.

### B2. Canonical Build Surface

- The canonical thesis master remains LaTeX via `main.tex`.
- Top-level section ordering should not change casually.
- Section ownership remains split across Person A / B / C, but coherence is collective responsibility.

### B3. Typography / Layout Defaults

- Paper size: A4
- Base font size: 12pt
- Line spacing: 1.5
- Main text font: Computer Modern (LaTeX default)
- Emphasis default: italics rather than decorative styling

### B4. Figure / Table Defaults

- Every figure and table must be referenced in the text.
- Every figure and table must have a descriptive caption.
- Visuals support arguments; they do not replace explanation.
- Prefer clean, high-quality graphics rather than screenshot-heavy visuals.

### B5. Citation Management

- Reference management remains in `bibliography.bib`.
- AI outputs are not primary sources.
- Dashboards and software tools should not be treated as evidence on their own without proper evidentiary framing.

## C. Derived Formatting / Layout Conventions

These are defensible academic conventions, but they should not be confused with hard CAS law unless confirmed by official guidance.

### C1. Readability

- Consistent heading hierarchy.
- Consistent page numbering.
- Auto-generated table of contents and directory sections.
- Clear paragraph separation.

### C2. Figure / Table Placement

- Table captions above tables.
- Figure captions below figures.
- Forward-reference visuals in the text before or at first discussion.

### C3. Structural Ordering

A common academic ordering is:

1. Title page
2. Declaration
3. Abstract
4. Table of contents
5. Lists of figures / tables
6. Main text
7. Appendix
8. Bibliography

This is compatible with the current LaTeX structure and should remain the working default unless the CAS specifies otherwise.

## D. Open Verification Points

These items should be treated as provisionally understood, but not overclaimed as settled if official program-specific confirmation is missing.

### D1. Citation Style

Current project default:
- numeric citations

Potential ambiguity:
- some CAS guidance may allow APA / Harvard / DIN style depending on program management

Working rule for V2:
- remain consistent with the existing thesis citation system unless the program director or official documentation clearly requires a different style

### D2. Detailed Typography Preferences

Items such as:
- left-aligned vs justified text
- exact line-spacing interpretation
- exact directory placement

are best treated as strong conventions, not as absolute rules, unless formally required.

### D3. Presentation Language

If a presentation-language constraint exists at the CAS level, it should be verified separately for final defense preparation. This does not currently change the thesis rebuild itself.

## E. V2 Build Implications

These rules imply the following rebuild constraints:

1. V2 must preserve a clear distinction between evidence-bearing claims and contextual explanation.
2. V2 must include an explicit AI-usage disclosure strategy.
3. V2 must keep an `Arbeitsjournal` workflow in mind from the start rather than treating it as an afterthought.
4. V2 must keep the final submission in LaTeX even if rough drafting occurs elsewhere.
5. V2 must not introduce formatting rules that create friction without contributing to compliance or readability.
6. V2 must avoid decorative overdesign that harms scientific clarity.

## F. Practical Compliance Checklist for the Rebuild

Before V2 is considered submission-ready, confirm:

1. thesis PDF builds cleanly
2. `Arbeitsjournal` is complete and individually attributable
3. AI disclosure is present and accurate
4. declaration and title-page elements are correct
5. all figures and tables are captioned and referenced
6. no unresolved references or placeholders remain
7. bibliography and in-text citations match
8. tone is scientific, neutral, and consistent
9. individual and collective contributions remain defensible

## G. Recommended Use

Use this file as the primary compliance reference during V2 planning and rebuild.

If a rule in this file appears to conflict with updated official HSLU / CAS instructions, the official instruction overrides this working reference and this file should be updated accordingly.
