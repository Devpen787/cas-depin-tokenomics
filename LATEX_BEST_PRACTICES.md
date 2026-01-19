# LaTeX Best Practices for this Repository

## 1. Import Workflow (From Docx to LaTeX)
When importing content from Google Docs or Word:
1.  **Format First**: Use `pandoc source.docx -f docx -t latex -o rough.tex`.
2.  **Clean Metadata**: Strip embedded TOCs, author blocks, and hardcoded dates.
3.  **Clean Headers**:
    - Remove hardcoded numbering (e.g., "5. Methodology" -> "Methodology"). LaTeX handles numbering.
    - Remove manual bolding/wrapping inside headers (e.g., `\section{\textbf{Title...}}` -> `\section{Title}`).
    - Replace `\paragraph{...}` with proper hierarchy (`\subsubsection`) if the content is structurally significant.
4.  **Fix Citations**:
    - Convert `[CITE:Key]` placeholders to `\cite{Key}` or `\textcite{Key}`.
    - Ensure citation keys match `bibliography.bib` exactly.
    - Check for malformed syntax like `\cite{Key{}}` or extra brackets.
5.  **Merge**: Place cleaned content into `sections/filename.tex` using `\input{sections/filename}` in `main.tex`.

## 2. Formatting & Hierarchy
-   **Headers**:
    -   Level 1: `\section{...}` (e.g., "Methodology")
    -   Level 2: `\subsection{...}` (e.g., "Model Scope")
    -   Level 3: `\subsubsection{...}` (e.g., "Agent Representation")
    -   Avoid `\paragraph{...}` for headers unless you strictly want inline, run-in headers.
-   **Lists**: Use `itemize` for bullet points and `enumerate` for numbered lists.
-   **Floats**: Always use `\begin{figure}[htbp] ... \end{figure}` for images and `\begin{table}[htbp] ... \end{table}` for tables.
-   **Punctuation**: Use real dashes (`---`—em dash, `--`—en dash) instead of hyphens where appropriate.

## 3. Compilation & Debugging
-   **Tool**: Use `latexmk -pdf main.tex` for reliable compilation. It automatically handles multiple passes for TOC and bibliography references.
-   **Cleaning**: If you see "Runaway argument" or mysterious errors, run `latexmk -C` to clean build artifacts (`.aux`, `.toc`, `.bbl`) and start fresh.
-   **Debugging TOC**: If TOC numbering looks wrong (e.g., double "4.5 7.1"), check the source `.tex` file for hardcoded numbers in the `\section` command.
-   **Bibliography**: Use `biber` (via latexmk) for modern BibLaTeX management. Ensure your `.bib` file has clean keys (no spaces or weird chars).

## 4. Repository Structure
-   `main.tex`: Root file. Contains preamble inputs and `\input{sections/...}` calls.
-   `sections/`: One `.tex` file per chapter/section.
-   `figures/`: Organized by chapter (e.g., `figures/ch3/`).
-   `bibliography.bib`: Single source of truth for references.
-   `staging/`: Python scripts for cleaning imports (`import_script.py`, etc.).

## Common Pitfalls
-   **Manual Spacing**: Avoid `\\`, `\newline`, or `\vspace` for paragraph separation. Use a blank line in the source.
-   **Hardcoded Numbers**: Never write `\section{3. Methodology}`. Write `\section{Methodology}`.
-   **Escaped Characters**: Watch out for `\%` vs `%`, `\$` vs `$`, and `\_` vs `_` in URLs or text.
