---
description: Hostile CAS Reviewer
---

# Hostile CAS Reviewer Workflow

This workflow triggers a "hostile" academic review of a specific LaTeX section file.

## Input
- The user should specify which file to review (e.g., "Review Person A" or "Review personB_tokenomics.tex").

## Steps

1.  **Identify Target File**: specific `.tex` file in `sections/`.
2.  **Read File**: Use `view_file` to read the content of the target section.
3.  **Analyze**: Perform a critical review acting as a "hostile CAS reviewer". Look specifically for:
    - Unclear claims
    - Implicit assumptions
    - Scope violations (check against the "SCOPE CONTRACT" at the top of the file)
    - Missing definitions
    - Over-claiming
4.  **Output Report**:
    - **Do NOT rewrite the text.**
    - Provide a numbered list of issues.
    - Format each issue with:
        - **Issue**: Description of the flaw.
        - **Severity**: [Low / Medium / High]
        - **Reference**: Exact line number or quote from the text.

## Example Output Format

1. **Issue**: The claim that "DePIN solves all scalability issues" is unsubstantiated and hyperbolic.
   **Severity**: High
   **Reference**: Paragraph 2, "DePIN is the ultimate solution..."

2. **Issue**: "Token velocity" is used without a formal definition.
   **Severity**: Medium
   **Reference**: Section 2.1, Line 45
