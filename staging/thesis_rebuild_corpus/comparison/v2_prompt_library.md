## V2 Prompt Library

Status: synthesis control document  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This file stores reusable bounded prompt patterns for the V2 rebuild.

It exists to prevent drift back into vague “write the chapter” prompting. Each prompt here should:

1. target a narrow job,
2. name the files or artifacts in scope,
3. preserve evidence discipline,
4. produce something reviewable.

These are workflow prompts, not thesis prose.

### 1. Rewrite Brief Execution

Use when sending a section to GPT 5.2 for reader-first rewriting.

Prompt pattern:

1. copy the current section,
2. insert the frozen structure and claim boundaries from the rewrite brief,
3. require exactly:
   - `Reader-First Rewrite`
   - `Why This Is Stronger`
   - `Drift Risks`

Control files:

- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_rewrite_brief_template.md`
- section-specific rewrite brief

### 2. Claim-Ledger Sync

Use when checking whether a section’s load-bearing claims match the ledger.

Prompt pattern:

`Read <TARGET_SECTION> and /Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_claim_ledger.md. List the section’s load-bearing claims, mark which are already represented in the ledger, identify any missing entries, and flag any wording that is stronger than the ledger’s evidence status allows. Do not rewrite the thesis text.`

### 3. Outline-to-Text Map

Use when checking whether a chapter or section actually performs its intended job.

Prompt pattern:

`Compare <TARGET_SECTION> against /Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_chapter_contracts.md. Report: (1) what the section is trying to do, (2) whether it fulfills the chapter contract, (3) any scope bleed, (4) what is missing, and (5) what is duplicated. Do not edit yet.`

### 4. Section Quality Gate Review

Use after drafting or rewriting a section.

Prompt pattern:

`Apply /Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_section_quality_gate.md to <TARGET_SECTION>. Return exactly: Verdict, Weak categories, Failure reason, Keep, Rewrite focus.`

### 5. Style Guide Review

Use when checking whether a section sounds like V2 rather than V1.

Prompt pattern:

`Review <TARGET_SECTION> against /Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/comparison/v2_style_guide.md. Identify where the prose matches the guide, where it still sounds mechanical or compressed, and what should change before acceptance. Do not rewrite unless asked.`

### 6. Reverse-Outline Test

Use when checking paragraph jobs and sequence.

Prompt pattern:

`Read <TARGET_SECTION>. For each paragraph, identify its single rhetorical job and assess whether the sequence is optimal. Flag any paragraph that is doing two jobs or appears in the wrong place. Do not rewrite yet.`

### 7. Figure / Table Reference Check

Use when validating thesis mechanics rather than prose.

Prompt pattern:

`Check <TARGET_SECTION> and the current LaTeX build for figures and tables. Report whether every figure and table is (1) labeled, (2) captioned, and (3) referenced in the text. Fix only broken labels and references if asked.`

### 8. Citation Integrity Check

Use when validating citation hygiene before a section is treated as stable.

Prompt pattern:

`Inspect <TARGET_SECTION>, bibliography.bib, and REFERENCE_MAPPING.md. Flag missing citation keys, likely weak source anchors, or places where prose appears to make a stronger claim than the visible evidence base supports. Do not invent citations.`

### 9. Pre-Submission Sweep

Use late in the rebuild when a chapter or the full V2 thesis needs a final hygiene pass.

Prompt pattern:

`Perform a pre-submission sweep on <TARGET_SCOPE>. Check for unresolved TODO markers, broken references, figure/table reference issues, inconsistent key terminology, and build cleanliness. Output a punch list ordered by severity. Apply only mechanical fixes if explicitly asked.`

### Final Rule

If a prompt sounds like “write my chapter,” break it down until it becomes one of the bounded jobs above or a similarly narrow task.
