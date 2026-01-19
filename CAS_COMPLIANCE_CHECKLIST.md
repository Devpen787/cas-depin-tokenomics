# CAS Transferarbeit (HSLU Informatik) — Compliance Spec for Agent Audits
Version: 1.0
Purpose: Machine-checkable rules for content + integrity + delivery + formatting.
Provenance tags:
- DOCUMENTED: explicitly grounded in HSLU documentation provided.
- DERIVED: conservative academic/LaTeX norms (not explicitly specified in the HSLU docs).

Output statuses per rule:
- PASS | FAIL | UNKNOWN
Decision logic:
- Any FAIL on CRITICAL => NON-COMPLIANT
- >= 3 FAIL on MAJOR => HIGH RISK

---

## 0) Required Artifacts

### 0.1 Core submission artifacts
- [CRITICAL][DOCUMENTED] A final thesis PDF exists.
- [CRITICAL][DOCUMENTED] An Arbeitsjournal exists and is submitted with the thesis.
- [MAJOR][DOCUMENTED] Slides exist for the final presentation (if your CAS requires presentation; default assumption: yes). :contentReference[oaicite:0]{index=0}

### 0.2 Group-work evidence
- [CRITICAL][DOCUMENTED] If group work: individual contribution per member is documented in the Arbeitsjournal (separate protocol sheet per member). :contentReference[oaicite:1]{index=1}

---

## 1) Length & Scope (Hard Limits)

- [CRITICAL][DOCUMENTED] The character count excludes title page, indices, and appendix.
- [CRITICAL][DOCUMENTED] 2 ECTS: ~33’000 characters (≈ 13–16 pages) per person.
- [CRITICAL][DOCUMENTED] 3 ECTS: ~50’000 characters (≈ 20–25 pages) per person. 

Agent check guidance:
- If ECTS unknown => return UNKNOWN for these rules, do not guess.

---

## 2) Mandatory Academic Sections (Content Structure)

### 2.1 Required “task definition” sections
- [CRITICAL][DOCUMENTED] Ausgangslage present.
- [CRITICAL][DOCUMENTED] Problemstellung present.
- [CRITICAL][DOCUMENTED] Ziele present (goals linked to deliverables).
- [CRITICAL][DOCUMENTED] Wissenschaftliche Methoden present. 

### 2.2 Scientific “work product” sections (minimum viable thesis)
- [CRITICAL][DERIVED] Main body includes: analysis/design/implementation/results (at least one).
- [MAJOR][DERIVED] Discussion/Interpretation section exists.
- [MAJOR][DERIVED] Conclusion section exists.

Rationale (for DERIVED): HSLU requires a scientific, systematic, comprehensible treatment and practical solution relevance; these sections are the minimal structure to demonstrate that cleanly. 

---

## 3) Scientific Standards (Method & Traceability)

### 3.1 Scientific method declaration and use
- [CRITICAL][DOCUMENTED] At least one scientific method is named (e.g., literature review, evaluation, experiments/simulation, survey).
- [CRITICAL][DOCUMENTED] Method choice is described (what/why).
- [CRITICAL][DOCUMENTED] Method is actually applied (not only described). 

### 3.2 Traceability / reproducibility
- [CRITICAL][DOCUMENTED] The work is written so reasoning and results are comprehensible and checkable (transparent handling of sources and methods).
- [CRITICAL][DERIVED] Assumptions are explicitly labeled as assumptions.
- [MAJOR][DERIVED] Inputs/parameters and outputs are clearly defined (especially for simulations/evaluations). 

---

## 4) Citations, Sources, and Plagiarism Avoidance

### 4.1 Citation requirements
- [CRITICAL][DOCUMENTED] All external sources used (ideas, facts, data, text, figures) are cited correctly and transparently.
- [CRITICAL][DOCUMENTED] Direct quotes are clearly marked and cited.
- [CRITICAL][DOCUMENTED] Paraphrases are cited (source is not “hidden” or contextless). 

### 4.2 Bibliography integrity
- [CRITICAL][DOCUMENTED] A bibliography exists.
- [CRITICAL][DOCUMENTED] Every in-text citation appears in the bibliography.
- [MAJOR][DERIVED] No “unused” bibliography entries (entries never cited). :contentReference[oaicite:8]{index=8}

### 4.3 Plagiarism / academic misconduct
- [CRITICAL][DOCUMENTED] No unreferenced copying (copy/paste, translation, paraphrase without citation).
- [CRITICAL][DOCUMENTED] No ghostwriting.
- [CRITICAL][DOCUMENTED] No self-plagiarism (reusing prior submitted work without disclosure).
- [CRITICAL][DOCUMENTED] Plagiarism detection is permitted/expected; the work must withstand checks. 

---

## 5) AI Usage Disclosure (Generative AI)

- [CRITICAL][DOCUMENTED] If generative AI was used, disclosure exists describing:
  - tool(s) used
  - purpose / scope of usage
  - where it affected the writing/research process
- [CRITICAL][DOCUMENTED] If no AI was used, an explicit “no AI used” statement exists.
- [CRITICAL][DOCUMENTED] AI use does not replace a substantial personal contribution; personal contribution is demonstrable. 

Agent check guidance:
- If disclosure section is missing => FAIL (not UNKNOWN).

---

## 6) Confidentiality & IP

### 6.1 Confidentiality classification
- [CRITICAL][DOCUMENTED] Work is classified (public vs confidential) in the submitted materials.
- [CRITICAL][DOCUMENTED] Confidential work must still be presentable (public presentation is standard; anonymization required if needed).
- [MAJOR][DOCUMENTED] NDA is possible; must be clarified before the work begins if needed. 

### 6.2 Rights
- [MAJOR][DOCUMENTED] HSLU has usage/exploitation rights to student works by default; author remains creator; alternative arrangements require agreement. :contentReference[oaicite:12]{index=12}

---

## 7) Presentation & Submission Process

- [CRITICAL][DOCUMENTED] Submission is done electronically via ILIAS (as per CAS process).
- [CRITICAL][DOCUMENTED] Presentation takes place as part of completion (per CAS process).
- [MAJOR][DOCUMENTED] Confidential works are not exempt from presentation; exclusion of others is generally not possible. :contentReference[oaicite:13]{index=13}

---

## 8) Title Page & Declaration

### 8.1 Title page
- [CRITICAL][DOCUMENTED] Title page exists and includes: title, author(s), program, period/date, program management, supervisor, confidentiality classification. :contentReference[oaicite:14]{index=14}

### 8.2 Statutory declaration (Eidesstattliche Erklärung)
- [CRITICAL][DOCUMENTED] Includes declaration of independent work + proper citation + respect confidentiality + respect copyright. :contentReference[oaicite:15]{index=15}

---

## 9) Formatting & Layout (Hygiene Layer)

IMPORTANT:
- The HSLU docs emphasize scientific care and formal correctness, but do not define detailed typography.
- Therefore, the rules below are DERIVED best practices to prevent reviewer friction.

### 9.1 Readability baseline
- [MAJOR][DERIVED] Consistent font family and sizes across the document.
- [MAJOR][DERIVED] Consistent heading hierarchy (no skipping levels).
- [MAJOR][DERIVED] Figures/tables: numbered + captioned; referenced in text.

### 9.2 PDF navigation
- [MAJOR][DERIVED] Page numbers present and consistent.
- [MAJOR][DERIVED] Table of contents auto-generated and matches headings.

### 9.3 LaTeX build hygiene
- [CRITICAL][DERIVED] No LaTeX compile errors.
- [CRITICAL][DERIVED] No unresolved references (“??”, “Citation undefined”).
- [CRITICAL][DERIVED] No placeholder text (“TODO”, “lorem ipsum”, “TBD”).

---

## 10) Gender-Inclusive Language

- [MAJOR][DOCUMENTED] Gender-inclusive language is required/expected for academic writing context. 

Agent check guidance:
- If language policy is obviously violated systematically => FAIL.
- If mixed/uncertain => UNKNOWN (don’t hallucinate).

---

## 11) Appeals (If Needed)

- [DOCUMENTED] Appeals window is 20 days; signed; postal submission; rules apply. (Not a thesis quality rule, but a process rule.) 

---

## 12) Audit Output Schema (for the agent)

Return one record per rule:

```json
{
  "rule_id": "3.1-METHOD-1",
  "severity": "CRITICAL",
  "provenance": "DOCUMENTED",
  "status": "PASS",
  "evidence": "Section 4.2 'Methodik', page 8; explicitly states simulation + evaluation criteria."
}
```

---

## 13) Compliance Decision Logic

```text
IF any CRITICAL rule = FAIL -> NON-COMPLIANT
ELSE IF >= 3 MAJOR rules = FAIL -> HIGH RISK
ELSE -> COMPLIANT
```
