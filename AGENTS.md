# Codex & Antigravity Agent Configuration

You are assisting with a master's level thesis on DePIN Tokenomics. 

**CRITICAL:** Before taking any action, you MUST read the `THESIS_OS.md` file located in the root of this repository. 

The `THESIS_OS.md` file contains:
1. The "Golden Thread" (the core argument of the thesis)
2. The exact terminology (e.g., we use DTSE, not ORSTE)
3. The citation and LaTeX tagging workflows (`% TODO-CITE:`)
4. The mapping of theoretical concepts to simulation code parameters.

Always ensure your output aligns with the architecture and SOPs defined in `THESIS_OS.md`.

---

## Anti-Literal Execution Guard (Mandatory)

For strategic requests that include words like "review", "analyze", "integrate", "strengthen narrative", or "where should this go":

1. Default to `MODE: SYNTHESIS` unless user explicitly requests `MODE: PATCH`.
2. In `MODE: SYNTHESIS`, do not edit files. Produce:
   - insight extraction,
   - claim/evidence classification,
   - target-section recommendations,
   - include/exclude rationale.
3. Before any edits, provide a patch manifest and wait for explicit user approval token:
   - `APPROVE PATCH SET`
4. Patch set size limit: maximum 2 thesis source files per approved set.
5. Never render internal workflow artifacts in thesis PDF by default:
   - `output/working_memory/*`
   - planning/audit/internal investigation notes.
6. If an edit accidentally introduces internal-process content into submission chapters, rollback before commit.

---

## Cursor-Specific: Parallel Subagents

When the user requests work spanning **2+ independent thesis domains**, use `mcp_task` to dispatch subagents in parallel instead of working sequentially.

### When to Use Parallel Dispatch

| Domains in scope | Subagent strategy |
|------------------|--------------------|
| Citations + Writing | One agent on `REFERENCE_MAPPING.md` / `TODO-CITE`; one on section `.tex` |
| Simulation + Methodology | One agent on DTSE/simulation code; one on `personC_methodology.tex` |
| Review + Citations | One agent on hostile review / consistency; one on reference resolution |
| Empirical + Results | One agent on `empirical_analysis.tex`; one on `personC_results.tex` |

### Subagent Type Mapping

- **explore** — Broad codebase search, finding files, understanding structure
- **code-reviewer** — Hostile review, consistency checks, preflight quality gate
- **kieran-typescript-reviewer** / **kieran-python-reviewer** — Simulation/math code review
- **generalPurpose** — Citation resolution, REFERENCE_MAPPING updates, section drafting

### Constraints

- Do **not** dispatch when tasks share state (e.g., editing the same `.tex` file).
- Each subagent prompt must be self-contained with full context (paths, task IDs, THESIS_OS lexicon).
- Prefer parallel dispatch when the user asks for "multi-domain" work, "run X and Y", or tasks that clearly map to independent domains above.
