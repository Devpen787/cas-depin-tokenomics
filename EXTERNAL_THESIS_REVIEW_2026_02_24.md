# Claude Opus 4.6 — External Thesis Review — "DePIN Tokenomics Under Stress"

**Reviewer posture:** First-time external reader, CAS/master-level academic assessor.  
**Thesis version reviewed:** `main.pdf` compiled from LaTeX sources as of 2026-02-24.  
**Review date:** 2026-02-24

---

## A) Executive Verdict

| Dimension | Assessment |
|---|---|
| **Overall rating** | **6.0 / 10** |
| **Confidence** | **Medium** — strong methodological scaffolding, but critical evidence gaps and figure-level concerns lower confidence that external assessors will reach the same verdict without additional fixes. |
| **Submit now?** | **No — submit after Pass 1 fixes (est. 2–3 days).** |
| **Top 3 blocking issues** | 1. **Baseline collapse is unexplained:** Fig 3 shows ONO price → $0 and providers 3000 → ~0 within 52 weeks under *neutral* conditions. The thesis never discusses why the baseline itself fails, which undermines every subsequent stress-deviation claim. 2. **Bibliography credibility:** ~50% of citations are grey literature (blog posts, Medium articles, exchange reports). Multiple bib entries are incomplete stubs (`Sartori2022`, `BrouwerBurg2016`, `Mardikes2025`). One entry (`EconAgentic2025`) credits "ResearchGate" as author. 3. **Absent research question declaration:** No explicit, numbered research question or hypothesis appears anywhere. The reader must infer the question from scattered prose in Introduction and Conclusion. |

---

## B) Findings by Severity

### B.1 — CRITICAL

#### Finding B.1.1: Baseline Collapse Not Addressed

- **Severity:** Critical
- **Location:** Section 8 (Simulation Results), Fig 3 (`fig_baseline_ono_price_providers.png`)
- **Issue:** The baseline — i.e. *no stress applied* — shows the modeled ONO price decaying from $0.10 to ~$0.001 and the active provider count declining from 3,000 to near zero over 52 weeks. If the neutral reference run already exhibits total system failure, then "deviations from baseline" under stress are meaningless: you are comparing stressed-failure to unstressed-failure.
- **Why it matters:** Every result in Chapter 8 is reported as a deviation from this baseline. If the baseline itself is a death spiral, the comparative framework collapses. An assessor will ask: "Is DTSE modeling a healthy system under stress, or a broken model collapsing everywhere?"
- **Fix:** Add a dedicated subsection (e.g., §8.2.1 "Baseline Dynamics and Interpretation") that:
  1. Explicitly acknowledges the baseline decay pattern.
  2. Explains whether this is an intentional modeling choice (e.g., "the baseline represents a subsidy-dependent startup trajectory without demand maturation") or a parameterization artifact.
  3. Clarifies how deviation-based reporting remains meaningful when the baseline is already declining. Consider using relative-rate-of-decline comparisons rather than absolute deviations.

#### Finding B.1.2: No Explicit Research Question

- **Severity:** Critical
- **Location:** Section 1 (Introduction)
- **Issue:** The thesis states a "research focus" (§1.3) but never formulates a crisp research question, e.g. *"RQ: How do alternative DePIN tokenomic mechanisms differ in their sensitivity to standardized stress inputs?"* The closest formulation appears only in the Conclusion (§9.1), retroactively.
- **Why it matters:** CAS/master-level work requires a stated question to which the thesis provides an answer. Without it, the assessor cannot evaluate whether the work actually answers what it claims.
- **Fix:** Insert a numbered research question at the end of §1.2 or §1.3. Keep it one sentence. Mirror it verbatim in §9.1 when answering.

#### Finding B.1.3: Bibliography Integrity

- **Severity:** Critical
- **Location:** `bibliography.bib` (entire file)
- **Issue:** Multiple problems:
  - `Mardikes2025`: listed as "Forthcoming" and "Internal or upcoming thesis usage" — this is a self-citation to a non-existent source.
  - `Sartori2022`: note says "Citation provided in text" with no journal, publisher, or URL. Unverifiable.
  - `BrouwerBurg2016`: same stub pattern — "Citation provided in text."
  - `SantaFeInstitute`: no date, no specific publication, just "{Santa Fe Institute}" and "Agent-based models working papers."
  - `EconAgentic2025`: author field is "ResearchGate" — this is a platform, not an author.
  - `PMC2022`: title is "Event studies in international finance research" but the author field just says "PubMed Central." PubMed is a database, not an author.
  - `FrontiersDePIN2025`: missing author field entirely.
  - Approximately 25 of 49 entries are blog posts, Medium articles, exchange reports, or crypto project docs.
- **Why it matters:** Academic assessors will check bibliography quality. Stub entries and platform-as-author entries signal sloppiness. Heavy grey-literature dependence weakens defensibility of conceptual claims.
- **Fix:**
  1. Remove `Mardikes2025` entirely or replace with published source.
  2. Complete `Sartori2022`, `BrouwerBurg2016`, and `SantaFeInstitute` with full publication metadata or remove.
  3. Fix `EconAgentic2025` and `PMC2022` with actual author names and publication details.
  4. Add `author` field to `FrontiersDePIN2025`.
  5. For every grey-literature citation supporting a substantive claim, add a co-citation to a peer-reviewed source where possible (see §C Claim-Evidence Audit).

---

### B.2 — MAJOR

#### Finding B.2.1: Retention Figure Shows <3% Final Retention Across All Profiles

- **Severity:** Major
- **Location:** Fig 7 (`fig_cross_scenario_retention_profiles.png`)
- **Issue:** The cross-profile retention chart shows final retention values ranging from ~0.001 to ~0.033 (i.e. 0.1% to 3.3%) for all profiles under all scenarios, including baseline. This means virtually every provider exits even without stress. The thesis never comments on these extremely low absolute values.
- **Why it matters:** A reader comparing "retention across profiles" will see all profiles ending at near-zero and conclude the model is broken, not that ONO is relatively more or less robust.
- **Fix:** Either (a) add text explaining why such low absolute retention is expected and emphasize that the comparison is ordinal/relative, or (b) re-examine parameterization if this outcome is unintended. If it's intentional, explain it prominently.

#### Finding B.2.2: Empirical Chapter (§6) Lacks Quantitative Data

- **Severity:** Major
- **Location:** Section 6 (Empirical Stress Analysis)
- **Issue:** Despite promising "event-study methodology" and "abnormal churn rates," the chapter contains zero quantitative results. No actual on-chain data, no computed abnormal churn values, no elasticity estimates. The Helium section cites price drop from ~$55 to ~$2 but provides no retention-rate calculation. The "Static Stress Test" framework is described but never executed with numbers.
- **Why it matters:** The chapter title promises empirical analysis, but delivers qualitative narrative with scattered price-level citations. This creates a gap: the thesis claims empirical grounding for DTSE, but no empirical result is actually produced.
- **Fix:** Either:
  1. Retitle the chapter to "Comparative Case Analysis" and explicitly state it is qualitative/descriptive.
  2. Or add at least one quantified metric per case (e.g., Helium 30-day retention during 2022 winter from on-chain data, Geodnet node growth rate during GEOD rally).

#### Finding B.2.3: Three-Author Split Creates Redundancy

- **Severity:** Major
- **Location:** Sections 2–4 vs. Section 6 vs. Section 5
- **Issue:** The chapter structure reveals a three-author split (Person A: foundations + Onocoy case; Person B: framework; Person C: methodology + results + discussion). This creates:
  - Section 4 (Theoretical Framework) and Section 6 (Empirical Analysis) both define BME, stress factors, and project archetypes with significant overlap.
  - "DePIN as CPS" appears in §4.2 but is not referenced by the methodology chapter that follows it.
  - The Onocoy descriptive chapter (§5, 1 page long) is disconnected — too short to stand alone, too thin to justify a full section number.
- **Why it matters:** Redundancy wastes the reader's time and signals unintegrated group work to assessors.
- **Fix:**
  1. Merge §5 (Onocoy Case) into §4 as a subsection, e.g. "4.6 Detailed Analysis: Onocoy as Case Implementation."
  2. In §6, remove re-definitions of BME and stress factors, replacing with cross-references to §3 and §4.
  3. Add a forward-reference from §4.2 (CPS framing) to §7 (DTSE methodology).

#### Finding B.2.4: Missing Formal Research Design or Method Justification

- **Severity:** Major
- **Location:** Section 7 (Methodology)
- **Issue:** The methodology chapter describes DTSE's structure and assumptions but never justifies *why* agent-based simulation was chosen over alternatives (analytical models, system dynamics, empirical regression, etc.). There is no methods-comparison section or literature-grounded argument for ABM as the appropriate tool.
- **Why it matters:** An assessor expects a methodology chapter to defend the method choice, not just describe the chosen tool.
- **Fix:** Add a subsection "7.1.1 Method Selection Rationale" (0.5 page) that:
  1. Lists alternatives considered (analytical models, system dynamics, econometric approaches).
  2. Explains why ABM is appropriate for heterogeneous provider behavior under stress.
  3. Cites Collins2024 or McCulloch2022 as methodological support.

---

### B.3 — MEDIUM

#### Finding B.3.1: Citation Formatting Artifacts

- **Severity:** Medium
- **Location:** Multiple sections (e.g., §2.1, §2.2, §4.1)
- **Issue:** Many citations appear as standalone `\cite{...}.` sentences where the citation tag is placed *after* a period on a new line, e.g.:
  ```
  ...path-dependent.
  \cite{Halaburda2021, Arthur1989}.
  ```
  This produces orphaned citation lines that are grammatically disconnected from the preceding sentence.
- **Why it matters:** It looks unpolished and suggests automated paste-and-cite rather than integrated writing.
- **Fix:** Integrate citations into sentence flow, e.g. "...path-dependent (Halaburda et al., 2021; Arthur, 1989)." Search for all `\cite{` preceded by a period and rewrite.

#### Finding B.3.2: Onocoy Chapter Too Thin

- **Severity:** Medium
- **Location:** Section 5 (Empirical Case: Onocoy), 33 lines of LaTeX
- **Issue:** At ~1 page, this is the thinnest section in the thesis. It provides a descriptive overview but adds nothing beyond what the whitepaper citation already contains. Key operational details (real station count, geographic distribution, actual revenue data, current token metrics) are absent.
- **Why it matters:** As the primary case study anchor, this chapter should demonstrate deep empirical familiarity. Its brevity suggests the authors rely entirely on the whitepaper.
- **Fix:** Expand to ~2–3 pages by adding:
  1. Current network statistics (station count, geographic coverage, daily transaction volume if available).
  2. Key governance events since launch.
  3. Comparison of whitepaper projections vs. observed reality.

#### Finding B.3.3: Discussion Archetypes Are Untethered to Results

- **Severity:** Medium
- **Location:** Section 9.2 (Human Intervention Archetypes)
- **Issue:** The five archetypes (Subsidy Continuation, Broad Incentive Increase, Incentive Re-Targeting, Non-Structural Response, Coordinated Operational Intervention) are presented as "interpretive layer" but are not linked to specific DTSE outputs from Chapter 8. No archetype says "under the demand-contraction scenario, the Subsidy Continuation pattern was observed when…"
- **Why it matters:** Without concrete links to results, the archetypes read as theory invented post-hoc rather than grounded interpretation.
- **Fix:** For each archetype, add one concrete mapping to a Chapter 8 result (scenario + metric + observed pattern).

#### Finding B.3.4: No Sensitivity Analysis Figures

- **Severity:** Medium
- **Location:** Section 7 (Methodology), Section 8 (Results)
- **Issue:** The methodology repeatedly references "sensitivity analysis over key parameter families" but no sensitivity analysis figure or table appears in the results. The appendix references `dtse_config_register` but within the main body, sensitivity is only described, never shown.
- **Why it matters:** Sensitivity analysis is a stated methodological commitment. Its absence from results undermines the reproducibility claim.
- **Fix:** Add at least one sensitivity analysis figure to Chapter 8 (e.g., varying churn threshold or emission cap and showing impact on retention).

---

### B.4 — MINOR

#### Finding B.4.1: Title Page Date Uses `\today`

- **Severity:** Minor
- **Location:** `main.tex`, line 42
- **Issue:** The title page prints `\today`, which changes every compilation. Submission documents should have a fixed date.
- **Fix:** Replace `\today` with a fixed submission date, e.g. `February 2026`.

#### Finding B.4.2: Author Names Are Placeholders

- **Severity:** Minor
- **Location:** `main.tex`, lines 31–33
- **Issue:** Authors listed as "Author A," "Author B," "Author C." This should be replaced before submission.
- **Fix:** Insert real names, or if using this for anonymous review, note this convention in a preface.

#### Finding B.4.3: Provenance Archive in Appendix Is Noise

- **Severity:** Minor
- **Location:** Appendix §A.1 (Contributor Draft Archive)
- **Issue:** The SHA256 hashes and repo-path table for raw contributor snapshots is internal process documentation, not content an assessor needs.
- **Fix:** Move to a supplementary materials file or remove from the submitted PDF. Keep the appendix focused on DTSE technical details.

#### Finding B.4.4: Inconsistent Section Numbering References

- **Severity:** Minor
- **Location:** Throughout
- **Issue:** The thesis refers to "Chapter 5" and "Chapter 6" and "Chapter 8" in the text, but LaTeX sections are numbered as §1 through §9 plus Appendix. This mismatch will confuse readers if section numbers shift.
- **Fix:** Use `\ref{}` cross-references instead of hardcoded chapter numbers, or verify numbering matches.

---

## C) Claim-Evidence Audit

| # | Claim (paraphrased) | Evidence Type | Appropriate? | Risk | Fix Needed |
|---|---|---|---|---|---|
| C1 | "DePIN networks depend on physical assets that fundamentally alter their risk profile" (§1.1) | Mechanism fact + grey-lit citation (Messari2024) | Partial — needs peer-reviewed support | Med | Co-cite with Ballandies2023 or Lin2024 (both already in bib) |
| C2 | "Few researchers examine how these systems behave under stress" (§1.1) | Assertion / gap claim | No — no systematic lit review shown | High | Add 2–3 sentence lit review gap statement citing actual DePIN stress-testing papers (or their absence) from Scopus/Google Scholar |
| C3 | "Poorly calibrated mechanisms amplify shocks rather than absorb them" (§1.2) | Grey-lit (Mardikes2025 — forthcoming/internal) | No — source does not exist publicly | High | Replace with Braakman2022 or a general systems-resilience reference |
| C4 | "BlockScience has established the industry standard for modeling complex cryptoeconomic systems" (§4.2) | Interpretation / industry claim | No — opinion presented as fact | Med | Rewrite as "BlockScience is among the recognized practitioners…" and cite Zargham's actual publications |
| C5 | "Helium hotspot count did not collapse proportionally" during 2022 winter (§6.3.1) | Empirical claim | Partial — cited via GateSquare2025 blog post | High | Provide actual on-chain data reference or Helium Foundation report. If unavailable, caveat as "reported by" |
| C6 | "Onocoy's capped supply is theoretically less exposed to hyperinflationary dilution loops than pure BME" (§6.4.1) | Modeled assumption / mechanism reasoning | Partial — no formal proof or simulation evidence presented in this section | Med | Cross-reference to DTSE results that test this exact comparison |
| C7 | "Death spiral probability is defined operationally as the frequency with which simulations exhibit concurrent degradation…" (§7.4) | DTSE output definition | Yes — clearly bounded | Low | None |
| C8 | "Under demand contraction, the first utilization deviation event appears at week 12, while provider-count degradation is delayed to week 49" (§8.3) | DTSE output | Yes — directly from simulation tables | Low | None |
| C9 | "Demand regimes are exogenous stylizations" (§9.4) | Modeled assumption (acknowledged limitation) | Yes — appropriate transparency | Low | None |
| C10 | "The thesis contributes a reproducible structure for such evaluation" (§9.5) | Interpretation / contribution claim | Partial — code repo referenced but not publicly linked or submitted | Med | Include DTSE code repository URL or submit as supplementary material |

---

## D) Human-Voice Audit (AI-Likeness)

### D.1: Repeated Templated Phrases

| Pattern | Example Locations | Count (est.) |
|---|---|---|
| "interpretation boundary / interpretation boundaries" | §7.1, §7.4, §8.1, §8.5, §9.1, §9.3, §9.4 | 12+ |
| "model-conditional" | §7.1, §8.1, §8.5, §9.1, §9.2, §9.3, §9.4, §9.5 | 15+ |
| "DTSE-conditional" | §8.4 (Table 5), §9.2 | 6+ |
| "under the DTSE assumptions" | §8.1, §8.2, §8.3, §8.5, §9.1 | 8+ |
| "are not treated as" | §8.1, §8.5, §9.1, §9.4 | 6+ |
| "within the experiment set" | §8.1, §8.3, §9.1, §9.4 | 7+ |
| "operational failure-mode signatures" (full phrase) | §8.5, §9.1, §9.2, §9.5 | 5+ |
| "evidence boundaries / evidence hierarchy" | §7.1, §9.1, §9.2, §9.4 | 6+ |

### D.2: Where Tone Feels Sterile/Over-Defensive

- **§8 (Results) entire chapter:** Every paragraph ends with a hedge clause. The cumulative effect is that the reader encounters more disclaimers than findings.
- **§9.2 (Human Intervention Archetypes):** Each archetype paragraph ends with "The interpretation boundary is…" — identical sentence structure five times in sequence.
- **§9.5 (Closing Statement):** Uses four hedging clauses in three sentences. The thesis ends on a note of caution rather than conviction.
- **§7.1 (Purpose, Scope, Context-of-Use):** Contains a list of "non-goals" before stating what DTSE actually does. The defensiveness front-loads limitations before any positive framing.

### D.3: Ten Concrete Rewrites

| # | Before (verbatim or near-verbatim) | After |
|---|---|---|
| 1 | "Results are interpreted as model-conditional comparisons rather than as absolute performance scores or forecasts" | "Results compare relative sensitivity across mechanisms within the model, not absolute performance." |
| 2 | "The interpretation boundary is that DTSE does not represent intent, governance feasibility, or off-chain constraints; the archetype is therefore a descriptive label for a class of outcome-consistent response where the system remains on its baseline incentive trajectory despite adverse usage conditions." | "DTSE does not capture governance intent or real-world constraints, so Subsidy Continuation simply describes cases where baseline emission rules continue despite weakening demand." |
| 3 | "This claim-class framing avoids category errors in the sections that follow." | "This framing ensures we do not confuse protocol rules with model outputs." |
| 4 | "Interpretive inferences are stated as model-conditional hypotheses bounded by the stress-channel definitions" | "All interpretive claims remain conditional on the specific stress inputs used." |
| 5 | "Several non-goals bound interpretation." | "DTSE is explicitly not designed for the following purposes:" |
| 6 | "Outputs are not treated as causal claims about real-world networks; patterns reported in Chapter 6 remain conditional on the model structure, parameterization, and stress specification." | "DTSE outputs describe model behavior, not real-world causation. They depend on the chosen parameters and stress inputs." |
| 7 | "The operational linkage is stress-channel specific: cost-side interventions relate to Profitability-Induced Churn and Latent Capacity Degradation; demand-side interventions relate to Reward–Demand Decoupling; and liquidity-related interventions relate to Liquidity-Driven Compression via changes in the modeled price-process environment." | "Each intervention type maps to a specific failure mode: cost interventions address profit-driven churn, demand interventions address reward-demand decoupling, and liquidity interventions address price-driven compression." |
| 8 | "This synthesis table provides a compact mapping from stress-channel inputs to DTSE output sequences and their associated operational signatures." | "Table 5 maps each stress channel to its earliest detectable signals in the DTSE output." |
| 9 | "DTSE is presented as an evaluative instrument for reasoning about DePIN tokenomics under stress when analytic treatment is insufficient and empirical evidence is incomplete." | "DTSE fills a gap between pure theory (too simple for heterogeneous agents) and pure empirics (too scarce for novel DePIN mechanisms)." |
| 10 | "By making assumptions explicit, reporting outcomes comparatively, and defining failure modes operationally, the framework supports more disciplined discussion of robustness and sensitivity without conflating simulation outputs with empirical facts." | "By keeping assumptions transparent and reporting relative differences rather than predictions, DTSE supports honest robustness assessment." |

---

## E) Figure/Table Audit

### E.1: Legibility and Interpretability

| Figure/Table | Legible? | Issues |
|---|---|---|
| Fig 3 (Baseline price + providers) | Yes — clean, readable axes | **No IQR band visible** despite legend saying "Median (IQR)." Bands may be too narrow to see, or IQR is near-zero (which itself is informative but unremarked). |
| Fig 4 (Demand contraction) | Partially — triple-panel is small | Burned (Sinks) panel has `1e7` magnitude label that is easy to miss. Provider Profit panel Y-axis label cut off at small sizes. |
| Fig 5 (Liquidity shock) | Yes — event marker at week 20 is helpful | Churn Count right panel: "Baseline" line sits at 0 for most of the run, making it hard to see without zooming. |
| Fig 6 (Competitive yield) | Uncertain — not viewed in detail | — |
| Fig 7 (Cost inflation) | Uncertain — not viewed in detail | — |
| Fig 8 (Cross-profile retention) | Yes, readable | **Y-axis max is 0.035 (3.5% retention).** This means all bars represent near-total provider loss. The visual misleads: bars look differentiated, but the absolute scale is catastrophic for all profiles. |
| Fig 9 (Cross-profile solvency) | Uncertain — not independently viewed | — |
| Fig 10 (ONO heatmap) | Yes — heatmap is the strongest figure | Colors are distinguishable, values annotated. One concern: color scale runs −1 to +1 but "Profit" under competitive yield shows +20.23, far outside the scale. |
| Fig 11 (Signal timing) | Uncertain — not independently viewed | — |
| Table 2 (Comparative metrics) | Yes | Clear column structure. |
| Table 3 (Signal timing ONO) | Yes | "n.a." entries could benefit from a footnote explaining why. |
| Table 4 (Cross-scenario synthesis) | Partially | Very dense; may need landscape orientation or font reduction for PDF readability. |
| Table 5 (Failure modes) | Yes | Well structured. |

### E.2: Caption Sufficiency

- **Fig 3 caption:** "Baseline reference trajectories for ONO: modeled price/providers (left) and emissions versus sinks (right)." — **Insufficient.** Does not mention the dramatic collapse pattern or what the reader should note.
- **Fig 8 caption:** "Cross-profile final-state comparison by scenario: retention (left) and incentive-solvency proxy (right)." — **Insufficient.** Should note that absolute retention values are below 3.5% for all profiles.
- **Fig 10 caption:** Does not explain that +20.23 is beyond the color scale range.

### E.3: Claims Supported by Figures

| Claim | Supporting Figure | Supported? |
|---|---|---|
| "Under demand contraction, the first utilization deviation event appears at week 12" (§8.3) | Fig 4 | **Partially** — the utilization panel shows divergence, but the exact week-12 onset is not visually verifiable from the figure alone. |
| "Churn deviation appears at week 1 under competitive yield" (§8.3) | Fig 6 | **Uncertain** — Fig 6 not examined at pixel level. |
| "Near-contemporaneous stress transmission" under liquidity shock (§8.3) | Fig 5 | **Yes** — the week-20 event marker aligns with visible churn spike. |

### E.4: Priority Improvements

1. **Add a note to Fig 3 caption** explaining the baseline decay pattern and its implications for deviation-based reporting.
2. **Rescale or annotate Fig 8** (retention) to make clear that all values are <3.5%; consider a log scale or an inset showing absolute provider counts.
3. **Fix Fig 10 heatmap** color scale or add a note that +20.23 is a relative delta that exceeds the color mapping range.
4. **Enlarge Fig 4** panels or split into separate figures — the triple-panel is too compressed.
5. **Add a sensitivity analysis figure** (see Finding B.3.4).

---

## F) Chapter-Coherence Audit

### F.1: Golden Thread Assessment

```
Motivation (§1) → Fundamentals (§2) → Stress Theory (§3) → Framework (§4) → Case (§5) → Empirical (§6) → Method (§7) → Results (§8) → Discussion + Conclusion (§9)
```

**Verdict: Thread holds in structure but weakens at two transitions.**

| Transition | Strength | Note |
|---|---|---|
| §1 → §2 | Strong | Motivation flows naturally to fundamentals. |
| §2 → §3 | Strong | Stress definitions follow logically. |
| §3 → §4 | Medium | §3 defines stress factors; §4 re-introduces some of the same concepts (BME, demand regimes) under "Theoretical Framework." There's conceptual overlap. |
| §4 → §5 | **Weak** | §5 (Onocoy) is too short to carry its own chapter weight. Feels like an orphaned stub. |
| §5 → §6 | Medium | §6 claims to be "empirical" but is actually qualitative comparative narrative. The transition from a 1-page descriptive case to a 5-page qualitative comparison is jarring. |
| §6 → §7 | Strong | The "Bridge to Simulation" subsection (§6.9) explicitly connects empirical gaps to DTSE rationale. This is well done. |
| §7 → §8 | Strong | Method leads clearly to results. |
| §8 → §9 | Strong | Deferred interpretation register cleanly hands off to discussion. |
| §9 → Conclusion | Medium | The conclusion is solid but repetitive of the discussion. The "Answer to the Research Question" paragraph is the first clear RQ formulation, which should have appeared in §1. |

### F.2: Chapter Role Drift

| Chapter | Intended Role | Actual Role | Drift? |
|---|---|---|---|
| §3 (Stress Theory) | Define stress constructs | Defines constructs + begins positioning relative to broader research | Minor — last subsection could move to §1 |
| §4 (Framework) | Theoretical framework | Partially re-defines concepts from §3 and §6 | **Yes — overlaps with §3 and §6** |
| §5 (Onocoy Case) | Empirical anchor description | Whitepaper summary | **Yes — too thin for its role** |
| §6 (Empirical Analysis) | Empirical event studies | Qualitative case comparison with no quantitative data | **Yes — "empirical" is misleading** |
| §8 (Results) | Report DTSE outputs | Reports outputs + includes sub-section on failure-mode definitions (§8.5) | Minor — failure-mode definitions could be in §7 |
| §9 (Discussion) | Interpret results | Introduces new analytical framework (archetypes) with limited connection to Chapter 8 | **Yes — archetypes are theory, not interpretation of results** |

### F.3: Corrected Chapter-Role Map

| # | Current Title | Suggested Revision | Rationale |
|---|---|---|---|
| §3 | Theoretical Definitions of Stress | Keep, but move §3.2 (Positioning) into §1 | Tighten scope |
| §4 | Theoretical Tokenomic Framework | Keep, absorb §5 into §4.7 | Eliminate orphan chapter |
| §5 | Empirical Case: Onocoy | Merge into §4 | Too thin standalone |
| §6 | Empirical Stress Analysis | Rename to "Comparative Case Analysis" | Honest about qualitative method |
| §8 | Simulation Results | Move §8.5 (Failure Modes) to §7 | Definitions belong in methodology |
| §9 | Discussion | Rename §9.2 to "Interpretive Framework" and connect each archetype to a specific DTSE result | Reduce drift |

---

## G) Final Action Plan

### Pass 1: Submission Safety (est. 2–3 days, impact: +1.0–1.5 grade points)

| # | Task | Section | Effort | Impact |
|---|---|---|---|---|
| 1 | **Explain baseline collapse explicitly** — add §8.2.1 | §8 | 2h | Critical — without this, all results are questionable |
| 2 | **Insert explicit research question** in §1.3 | §1 | 15min | Critical — assessors look for this |
| 3 | **Fix broken bib entries** — remove Mardikes2025, complete Sartori2022/BrouwerBurg2016/SantaFeInstitute, fix author fields for EconAgentic2025/PMC2022/FrontiersDePIN2025 | `bibliography.bib` | 2h | Critical — broken references fail automated checks |
| 4 | **Integrate orphaned citations** — fix all `\cite{}.` formatting artifacts | All sections | 1.5h | Medium — significant polish gain |
| 5 | **Replace author placeholders** and fix `\today` date | `main.tex` | 10min | Minor but mandatory |
| 6 | **Fix Fig 8 caption** to note absolute retention <3.5% | §8 | 15min | Major — prevents misinterpretation |
| 7 | **Fix Fig 10 heatmap** — note +20.23 exceeds scale | §8 | 15min | Medium |
| 8 | **Retitle §6** to "Comparative Case Analysis" or add disclaimer about qualitative scope | §6 | 30min | Major — manages assessor expectations |
| 9 | **Remove Appendix §A.1** (provenance archive) from submitted PDF | Appendix | 15min | Minor — reduces noise |
| 10 | **Add note about Fig 3 IQR bands** — explain why they are invisible | §8 | 15min | Medium |

**Pass 1 estimated total effort: ~7 hours**  
**Expected impact: raises confidence from medium to medium-high; raises grade from 6.0 to ~7.0–7.5**

---

### Pass 2: Quality Uplift (est. 3–5 days, impact: +0.5–1.0 additional grade points)

| # | Task | Section | Effort | Impact |
|---|---|---|---|---|
| 1 | **Add method-selection rationale** subsection | §7 | 2h | Major — strengthens methodology defense |
| 2 | **Expand Onocoy chapter** with real network data | §5 (or §4.7 if merged) | 3h | Medium — grounds the case study empirically |
| 3 | **Add one sensitivity analysis figure** to results | §8 | 3h | Medium — fills stated methodological commitment |
| 4 | **Connect archetypes to specific DTSE results** with scenario-metric examples | §9 | 2h | Medium — reduces interpretation drift |
| 5 | **Add 2–3 peer-reviewed co-citations** for key grey-lit-supported claims (see C1, C5) | §1, §6 | 2h | Medium — strengthens evidence base |
| 6 | **Apply human-voice rewrites** from Section D | Throughout | 3h | Medium — reduces AI-likeness perception |
| 7 | **Merge §5 into §4** and resolve §3/§4/§6 overlap | §3–§6 | 3h | Major — tightens structure |
| 8 | **Add lit-review gap statement** for stress-testing in DePIN | §1 | 1h | Major — establishes novelty claim properly |

**Pass 2 estimated total effort: ~19 hours**  
**Expected impact: raises grade from ~7.0–7.5 to ~8.0–8.5**

---

*End of review.*
