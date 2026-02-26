# Thesis Academic Review — Against Standard Criteria

**Paper:** *DePIN Tokenomics Under Stress: A Simulation-Based Sustainability Analysis Using the Onocoy Network as a Case Study*
**Review Date:** 2026-02-23

---

## Overall Rating: 4.5 / 10

The thesis has a **strong conceptual architecture** and a well-defined "Golden Thread," but it is currently in a **late-draft / pre-submission state** with several critical gaps that would prevent acceptance under standard academic review.

---

## 1. Structure of Content (IMRaD) — Score: 6/10

### ✅ Strengths

| Element | Assessment |
|---|---|
| **Introduction** | Clear gap identification, explicit problem statement, defined scope constraints |
| **Methods (DTSE)** | Excellent separation of fact/assumption/interpretation; well-defined metrics |
| **Golden Thread** | Consistent narrative from Foundations → Framework → Empirical → Simulation → Results |
| **Modular authorship** | Clean `SCOPE CONTRACT` headers prevent role drift across Person A/B/C |

### 🔴 Critical Gaps

| Issue | Severity | Details |
|---|---|---|
| **Zero figures or charts** | 🔴 **Fatal** | `\includegraphics` appears 0 times across all sections. A simulation-based thesis with no visual data presentation is **unsubmittable**. Results Chapter 6 describes "deviations from baseline" but shows nothing. |
| **Results are prose-only** | 🔴 **Fatal** | Section 6 reads as an extended methodology paraphrase. There are no concrete numbers, no simulation output values, no time-series plots, no histograms, no sensitivity heatmaps. Every paragraph says *what would happen* rather than *what happened*. |
| **Incomplete IMRaD cycle** | 🔴 High | The "R" in IMRaD (Results) is structurally present but functionally empty. The Discussion interprets outputs that the reader has never seen. |
| **Draft imports still embedded** | 🟡 Medium | Sections end with `\input{sections/import_personA_...}` blocks labeled "Provisional, Source-Preserving." These are raw draft fragments that duplicate or conflict with the polished sections above them. |

### Verdict
> The skeleton follows IMRaD well. But a skeleton without the Results flesh is a body that can't stand.

---

## 2. Argument Layout & Defensibility — Score: 5/10

### ✅ Strengths

- **Theory-to-Model mapping** is explicit and rigorous (Table in `THESIS_STRUCTURE.md`: Reward Addiction → `burn_fraction`, `emission_cap`, etc.)
- **Failure-mode taxonomy** is well-defined with operational definitions and precursor metrics (Table 2 in Results)
- **Claim-class system** (mechanism fact / modeled assumption / DTSE output) is a genuinely strong methodological contribution
- **Cross-scenario synthesis table** maps stress channels → earliest/lagging signals → failure signatures with interpretation boundaries

### 🔴 Critical Gaps

| Issue | Severity | Details |
|---|---|---|
| **50+ unresolved `TODO-CITE` markers** | 🔴 **Fatal** | Across all sections, 50+ claims are unsupported. Many are core claims (e.g., ABM justification, price-proxy validity, provider churn modeling). A reviewer would stop reading. |
| **11 unresolved `TODO-LINK` markers** | 🟡 High | Cross-references to appendix tables, scenario grids, run manifests, and threshold definitions point to nonexistent targets. |
| **No validation / verification results** | 🔴 High | Methodology promises baseline runs, sensitivity analysis, Monte Carlo aggregation, and internal consistency checks — but Results never delivers any of these. |
| **Empirical Analysis (Ch. 4) citation quality** | 🟡 Medium | This chapter cites blog posts (MediumTokenomics2026, MediumHeliumMiner), aggregator sites (CoinMarketCap), and industry reports. Several are `HIGH` risk per the project's own citation risk register standards. |
| **No quantified uncertainty** | 🔴 High | Methodology defines IQR reporting and distributional summaries, but Results contains zero numbers — no confidence intervals, no p-values, no variance decomposition. |
| **Missing appendix content** | 🟡 High | The appendix file is 893 bytes. The scenario grid, parameter tables, run manifests, and threshold definitions referenced throughout are missing. |

### Framework Defensibility Summary

```
Theory (Ch 1-2)  ———→  Empirical Anchor (Ch 3-4)  ———→  Simulation (Ch 5-6)  ———→  Discussion (Ch 7)
  ✅ Strong              ✅ Decent (citations weak)         🔴 BROKEN               ⚠️ Interprets phantom data
```

> The logical framework is sound, but the evidentiary chain breaks at Ch. 6. The discussion interprets results that don't exist yet.

---

## 3. The Human Factor — Score: 5/10

### ✅ Strengths

- **Limitations are explicit and honest** — the Discussion and Conclusion clearly bound DTSE claims (no causal certainty, no forecasts, no universal mechanism superiority)
- **Interpretation boundaries** are stated at every level (methodology, results, discussion)
- **Reproducibility intent** is strong — seeds, manifests, config registers are mentioned as requirements

### 🔴 Critical Gaps

| Issue | Severity | Details |
|---|---|---|
| **Reproducibility is promised but not delivered** | 🔴 High | No code repository is referenced. No parameter tables exist in the appendix. No run manifests are attached. The reader cannot replicate anything. |
| **AI-writing markers remain** | 🟡 Medium | The `HUMAN_STYLE_AUDIT.md` identified 38 instances: 9 em-dash abuses, 13 passive voice patterns, 14 template phrases, 2 defensive hedges. These have not been corrected. |
| **Uniform prose density** | 🟡 Medium | Every section reads at the same register and depth. There's no variation in paragraph density, no concrete examples or anecdotes, no authorial voice that distinguishes Person A/B/C writing styles. |
| **Jargon density without glossary** | 🟡 Medium | Terms like BME, DTSE, CPS, RTK, CapEx/OpEx are introduced but the paper lacks a formal glossary or abbreviation table. |
| **No concrete numbers anywhere** | 🔴 High | Despite describing a simulation system, the entire thesis avoids specifics: no actual token prices, no provider counts, no hardware costs, no real Onocoy metrics (e.g., "Onocoy has X stations in Y countries earning Z ONO/month"). |

### Transparency Assessment

| Aspect | Status |
|---|---|
| Limitations acknowledged | ✅ Thorough |
| Biases discussed | ⚠️ Mentioned abstractly, not specifically |
| Data/code shared | 🔴 Not provided |
| Parameter values disclosed | 🔴 Missing ("appendix-grade" but appendix is empty) |
| Reproducibility possible | 🔴 No — missing artifacts |

---

## Priority Action Matrix

| Priority | Action | Impact |
|---|---|---|
| 🔴 P0 | **Run simulations and populate Ch. 6 with real data** — charts, tables, numerical results | Without this, the thesis is conceptual, not empirical |
| 🔴 P0 | **Resolve all 50+ `TODO-CITE` markers** | Paper is unsubmittable with placeholder citations |
| 🔴 P0 | **Add figures** — time-series plots, heatmaps, sensitivity charts, at minimum 8-12 | A simulation thesis without visuals fails on first impression |
| 🔴 P1 | **Build the appendix** — parameter tables, scenario grids, run manifests, seeds | Required for reproducibility claims to hold |
| 🟡 P2 | **Apply `HUMAN_STYLE_AUDIT.md` fixes** — em-dashes, passive voice, ordinal lists | Medium effort, prevents AI-detection flags |
| 🟡 P2 | **Remove provisional `import_person*` sections** or properly integrate them | Prevents reviewer confusion |
| 🟡 P2 | **Add abbreviation table / glossary** | Accessibility for non-specialist readers |
| 🟢 P3 | **Inject concrete Onocoy data** — station counts, token supply, hardware costs | Grounds the abstract framework in reality |
| 🟢 P3 | **Upgrade Ch. 4 citations** — replace blog posts with peer-reviewed or official docs | Defensibility of empirical analysis |

---

## Bottom Line

> **This thesis has a genuinely excellent conceptual architecture** — the Golden Thread, claim-class system, and failure-mode taxonomy are publication-quality ideas. However, the paper is currently a **methods paper without results**. The simulation framework (DTSE) is well-specified on paper, but no simulation outputs are presented. Until Ch. 6 contains actual data and Ch. 7's discussion can point to real figures, the thesis cannot be evaluated as finished research.

> Current state: **Strong draft framework, awaiting its core empirical content.**
