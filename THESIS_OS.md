# Thesis Operating System (THESIS_OS)

**CRITICAL INSTRUCTION FOR ALL AI AGENTS (Cursor, Antigravity, Codex, etc.):**
Before assisting the user with any thesis-related writing, coding, or planning, you MUST read this document to understand the project structure, the "Golden Thread" of the argument, and the established Standard Operating Procedures (SOPs).

---

## 1. The "Golden Thread" (Argument Flow)
*Every chapter must directly contribute to answering the main thesis question.*

- **Main Thesis Question:** How do DePIN tokenomic mechanisms (specifically BME vs. Capped Supply) behave under physical and economic stress, and how can we evaluate their robustness before catastrophic failure?
- **Ch 1. Foundations:** Establishes why DePINs are fragile (physical hardware sunk costs) and defines "stress" theoretically (e.g., Reward Addiction, Subsidy Gap).
- **Ch 2. Theoretical Framework:** Defines the tokenomic "cures" (e.g., Burn-and-Mint Equilibrium, Emission Decay) using the Solana ecosystem as a baseline.
- **Ch 3. Empirical Case (Onocoy):** Grounds the theory in a real-world subject: Onocoy's specific Capped Supply GNSS network.
- **Ch 4. Empirical Analysis:** Proves that stress failures exist historically (e.g., Helium in 2022) using event studies. *Bridge to Ch 5: Historical data shows failure modes, but to test future thresholds of new networks like Onocoy, we need simulation.*
- **Ch 5. Methodology:** Sets up the **DTSE (DePIN Tokenomic Stress Evaluator)**. Translates theories from Ch 1 & 2 into simulation code parameters.
- **Ch 6. Results:** Answers the main question by showing how the mechanisms performed under the simulated stress.

---

## 2. Core Architecture Decisions & Lexicon
- **Simulation Engine Name:** We use **DTSE (DePIN Tokenomic Stress Evaluator)**. *DO NOT use the outdated acronym "ORSTE".* The engine is a generalized framework for testing DePINs, using Onocoy as the primary empirical anchor.
- **Theory-to-Model Translation:**
  - *Reward Addiction* $\rightarrow$ Burn-to-Mint Ratio $< 1$ $\rightarrow$ `burn_fraction`, `emission_cap`
  - *Subsidy Gap* $\rightarrow$ Real Yield vs. Dilutive Yield $\rightarrow$ `provider_opex`, `fiat_revenue_baseline`
  - *Speculative Fragility* $\rightarrow$ 30-Day Retention vs. Price Drop $\rightarrow$ `churn_threshold`, `price_drift`

---

## 3. The Knowledge Hub (Core Files)
Do not duplicate tracking. Always refer to and update these master files:
1. **`THESIS_STRUCTURE.md`**: The Kanban board for chapter status, ownership (Person A/B/C), and structural mapping.
2. **`REFERENCE_MAPPING.md`**: The master checklist and page-level tracking tables for all 80+ citations.
3. **`bibliography.bib`**: The master LaTeX citation database.
4. **`.agent/knowledge-skill-graph.json`**: The task-to-skill routing graph used by agents to select checks and workflows consistently.

---

## 4. Standard Operating Procedures (SOPs)

### A. The Writing & Citation Workflow
- When writing in `.tex` files, do not break flow to find page numbers. Use inline tags:
  - `% TODO-CITE: [Author/Concept] [Note]` (e.g., `% TODO-CITE: [Morris 2019] need page for MCSE formula`)
  - `% TODO-LINK: [Section/Figure]` (e.g., `% TODO-LINK: see Methodology section for parameters`)
- Periodically, run a global search for `% TODO-CITE`, look up the source in `REFERENCE_MAPPING.md`, fill in the page-level table, and replace the tag with a formal `\cite{...}`.

### B. Environment Independence
- This thesis is developed across **Cursor, Antigravity, and Codex**.
- Rely on standard Markdown files, Python scripts, and `.tex` files. Avoid IDE-locked formats where possible.
- If running scripts (like orphan checkers or reference linkers), standard Python 3 is assumed.

---

## 5. Custom Toolbelt & Agent Skills
When working on specific domains of this project, agents must leverage the installed `.codex/skills/` and `.cursor/plugins/`:
- **For Simulation & Math:** Use `depin-simulation-optimizer` and `math-rigor`.
- **For Planning & Workflow:** Use `depin-planning-with-files` and `depin-verification-before-completion`.
- **For Document Analysis:** Use `doc` and `pdf` skills to extract page-level data for `REFERENCE_MAPPING.md`.
- **For UI/Dashboards (if applicable):** Use Figma MCPs and `frontend-design`.

### Knowledge-Skill Graph Operations
- Use the thesis graph at **`.agent/knowledge-skill-graph.json`** for deterministic routing from tasks to required skills.
- Validate graph integrity before and after edits:
  - `python3 scripts/knowledge_skill_graph.py --validate`
- Resolve required skill sequence for a task:
  - `python3 scripts/knowledge_skill_graph.py --task <task-id>`