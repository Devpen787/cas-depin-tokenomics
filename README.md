# CAS DePIN Tokenomics Thesis

This repository contains the LaTeX source code for the CAS Transferarbeit "DePIN Tokenomics".

## Repository Structure
- `main.tex`: Master LaTeX file.
- `preamble.tex`: Configuration and package imports.
- `sections/`: Content split by author/topic.
- `bibliography.bib`: References.
- `CAS_RULES.md`: Governance and content rules.
- `CAS_FORMATTING_AND_STYLE.md`: Formatting conventions.

## Build Instructions

### Prerequisites
1.  **LaTeX Distribution**: BasicTeX (macOS) or TeX Live.
    ```bash
    brew install --cask basictex
    ```
2.  **Required Packages**:
    ```bash
    sudo tlmgr update --self
    sudo tlmgr install latexmk biblatex biber multirow longtable enumitem url csquotes
    ```

### Compilation
To generate the PDF, run:
```bash
latexmk -pdf main.tex
```
The output will be `main.pdf`.

## Workflows
- **Hostile Review**: `agent run "Review Person A"`
- **Reconciliation**: `agent run "Check consistency"`

(See `.agent/workflows/` for details)
