## V2 Claim Ledger

Status: synthesis control document  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This ledger exists to stop V2 prose from outrunning evidentiary support.

It tracks the major claims the thesis wants to make, where those claims belong, what class of claim they are, what evidence is currently supporting them, and whether the wording is safe, risky, or still unresolved.

This is not a citation database. It is a claim-control file.

### Claim Classes

Use only these classes:

1. `mechanism fact`
2. `empirical observation`
3. `modeled assumption`
4. `DTSE output`
5. `interpretation`
6. `context`

### Evidence Status Labels

Use one:

1. `supported`
2. `partially supported`
3. `needs sourcing`
4. `modeled only`
5. `not admissible as load-bearing claim`

### Risk Levels

Use one:

1. `low`
2. `medium`
3. `high`

High risk usually means one of the following:

- claim depends on weak sourcing
- claim mixes evidence classes
- claim is currently too strong for the available support
- claim is easy to misread as empirical proof when it is only modeled or interpretive

### Operating Rules

1. If a claim is load-bearing, it must appear here.
2. If a claim lacks support, flag it instead of smoothing over it in prose.
3. If a claim is useful but not yet thesis-safe, it may stay in the context layer but must not carry the argument.
4. If a claim is modeled, say so explicitly.
5. If a claim belongs in a different chapter, route it there instead of duplicating it.

### Suggested Columns

Each claim entry should track:

1. `claim_id`
2. `chapter`
3. `section`
4. `claim_summary`
5. `claim_class`
6. `source_anchor`
7. `evidence_status`
8. `risk_level`
9. `notes`

### Initial V2 Core Claims

| claim_id | chapter | section | claim_summary | claim_class | source_anchor | evidence_status | risk_level | notes |
|---|---|---|---|---|---|---|---|---|
| C1 | Chapter 1 | Introduction | DePIN tokenomics should be analyzed as a stress-oriented cyber-physical coordination problem rather than as a purely financial mechanism. | interpretation | `THESIS_OS.md`; foundations literature | partially supported | medium | Strong framing claim; must stay tied to cited theory and not drift into unsupported generalization. |
| C2 | Chapter 1 | Introduction | Physical deployment constraints make DePIN participation materially more path-dependent and less liquid than software-only crypto participation. | mechanism fact | `Ballandies2023`, `Lin2024`, `Arthur1989` | supported | low | Safe if phrased comparatively rather than absolutely. |
| C3 | Chapter 1 preview; Chapter 2 | Introduction; Foundations | Provider retention, service continuity, and incentive--usage alignment are the three coupled functions used to interpret DePIN robustness in this thesis. | interpretation | thesis framework | supported | low | Internal thesis lens; previewed in the introduction and developed fully in the foundations chapter. Do not misrepresent it as a universal industry taxonomy. |
| C4 | Chapter 3 | Comparative framework | BME-oriented and capped-supply designs differ primarily in supply logic, sink coupling, and subsidy flexibility under stress. | mechanism fact | comparative mechanism sources; protocol docs | partially supported | medium | Requires careful wording so comparator claims remain documented. |
| C5 | Chapter 4 | Onocoy case | Onocoy uses a capped-supply ONO token with Data Credits as the user-facing utility layer. | mechanism fact | `OnocoyWhitepaper301`, `OnocoyToken`, `OnocoyRewards` | supported | low | Load-bearing anchor claim. |
| C6 | Chapter 4 | Onocoy case | Onocoy's dual-layer design reduces direct user-price exposure to token volatility while shifting robustness pressure toward sink strength and provider economics. | interpretation | Onocoy docs + DTSE framing | partially supported | medium | Must distinguish protocol fact from thesis interpretation. |
| C10 | Chapter 7 | Results | Different stress channels register first in different metric families, revealing distinct transmission paths across mechanism profiles. | DTSE output | frozen DTSE artifacts | supported | low | Central results claim. |
| C11 | Chapter 7 | Results | Failure-mode signatures provide a more useful comparative language than binary stable/unstable labels. | interpretation | results + discussion | supported | low | Thesis-level interpretive claim grounded in DTSE outputs. |
| C12 | Chapter 8 | Discussion / conclusion | Neither BME-oriented nor capped-supply designs escape DePIN physical constraints; they redistribute where stress appears first and how it accumulates. | interpretation | results + comparative framework | partially supported | medium | Strong closing claim; wording must remain comparative and conditional. |
| C13 | Chapter 1 | Introduction | When incentives weaken, infrastructure providers may reduce operational commitment, defer maintenance, or eventually power down hardware. | context | `Messari2024`, `FrontiersDePIN2025` | not admissible as load-bearing claim | medium | Use only as motivating context unless later grounded with stronger empirical support. Do not let later chapters rely on this as established empirical fact without additional sourcing. |
| C14 | Chapter 1 | Introduction | Public DePIN discourse often emphasizes adoption, network growth, and token appreciation more than operational stress behavior. | context | `Ho2022`, `Chiu2024` | not admissible as load-bearing claim | medium | Acceptable as a light framing observation. Do not let it become a thesis-bearing generalization without stronger systematic support. |
| C15 | Chapter 2 | Foundations | DePIN participation is materially shaped by physical deployment frictions, including CapEx, OpEx, and geographic placement. | mechanism fact | `Arthur1989`, `Lin2024`, `Ballandies2023`, `FrontiersDePIN2025` | supported | low | Core foundations claim. Safe if stated comparatively and tied to real infrastructure requirements. |
| C16 | Chapter 2 | Foundations | Sunk costs and geographic friction create asymmetric exit and recovery dynamics in DePIN networks. | interpretation | `Arthur1989`, `Lin2024`, `Ballandies2023` | partially supported | medium | Strong and useful, but should remain an interpretive claim grounded in path dependence rather than universal law. |
| C17 | Chapter 2 | Foundations | Reward Addiction, the Subsidy Gap, and Speculative Fragility are the core theoretical stress constructs used by this thesis. | interpretation | thesis framework; foundations chapter | supported | low | Internal thesis vocabulary. Present as the thesis lens, not as a universally accepted industry taxonomy. |
| C18 | Chapter 2 | Foundations | In DePIN, the token is part of a cyber-physical coordination mechanism rather than a standalone value-transfer layer. | interpretation | `Messari2024`, `FrontiersDePIN2025`, `RochetTirole2003`, `Chiu2024` | partially supported | medium | Important framing claim for Chapter 2. Keep precise and avoid overstating universality. |
| C19 | Chapter 3 | Comparator frame | A dated market snapshot can be used to situate the comparator universe descriptively, but it cannot by itself support claims about tokenomic robustness. | context | `CoinMarketCapDePIN`, `Coincub2025`, Person B final framework | supported | low | Treat market-cap context as time-stamped scene-setting only; do not let it carry the chapter's comparative argument. |
| C20 | Chapter 3 | Emission logic and supply regimes | Capped supply does not by itself imply low effective inflation or low subsidy pressure; what matters is the distribution path and its adjustment logic under stress. | mechanism fact | `RenderBME`, `GeodnetIP7`, `IoNet2025`, `OnocoyToken`, Person B final framework | partially supported | medium | Comparative claim is strong, but should remain focused on regime logic rather than precise inflation metrics unless harmonized. |
| C21 | Chapter 3 | Reward logic and work verification | DePIN reward architecture depends not only on issuance, but on what counts as valid work and how quality enters the payoff function. | mechanism fact | `Ballandies2023`, `Chiu2024`, `Tan2020`, Person B final framework | supported | low | Safe if phrased comparatively and tied to verification families rather than project-specific absolutes. |
| C22 | Chapter 3 | Monetization, sinks, and value accrual | Comparator projects differ materially between mechanistic usage-burn loops, revenue-mediated buyback regimes, and utility/payment models without systematic burn. | interpretation | `RenderBME`, `GeodnetIP7`, `IoNet2025`, `OnocoyWhitepaper301`, `OnocoyToken`, Person B final framework | partially supported | medium | Useful synthesis claim; must remain clearly interpretive where public documentation is incomplete. |
| C23 | Chapter 3 | Demand regimes and utility--speculation profiles | Demand-regime and utility--speculation classifications are bounded comparative lenses that help frame tokenomic exposure, but they do not measure realized adoption or prove robustness directly. | interpretation | `Lin2024`, `Ho2022`, Person B final framework | supported | low | Important boundary claim so heuristic tables or prose are not misread as empirical ranking. |
| C24 | Chapter 4 | Onocoy anchor case | Onocoy operates a decentralized GNSS correction network based on RTK positioning, in which distributed reference stations provide correction data for high-accuracy positioning workflows. | mechanism fact | `OnocoyWhitepaper301`; `personA_onocoy.tex` | supported | low | Core anchor-case mechanism fact. Safe when kept at the level of documented network function and not inflated into broader performance claims. |
| C25 | Chapter 4 | Onocoy anchor case | Reference-station participation is quality-sensitive rather than purely passive because hardware setup, connectivity, and uptime affect usable correction output. | mechanism fact | `OnocoyWhitepaper301`, `OnocoyRewards` | supported | low | Important for linking Onocoy back to the cyber-physical constraints in Chapter 2 without drifting into simulation language. |
| C26 | Chapter 4 | Onocoy anchor case | Onocoy's blockchain choice should be interpreted as a time-bounded settlement-layer design decision tied to throughput and cost requirements, ecosystem timing, and off-chain service delivery constraints rather than as a universal claim of chain superiority. | interpretation | `Ballandies2023ChainSelection`, `HeliumHIP70`, `personA_onocoy.tex` | partially supported | medium | Must stay explicitly bounded and time-specific. Avoid phrasing that implies a timeless chain-ranking conclusion. |
| C27 | Chapter 4 | Onocoy anchor case | Public Onocoy documentation is more explicit about ONO and Data-Credit mechanics than about staking or collateral participation rules; where those rules matter later, they must be treated as unknown mechanism facts or declared modeled assumptions. | interpretation | `OnocoyToken`, `OnocoyRewards`, `personA_onocoy.tex` | supported | low | Important evidence-boundary claim for later empirical and methodological chapters. |
| C28 | Chapter 4 | Onocoy anchor case | Public tokenomics documentation describes ONO as capped at 810 million units. | mechanism fact | `OnocoyTokenomics` | supported | low | Core tokenomics fact that later mechanism discussion and any model-facing reasoning may rely on. Keep the wording tied to public documentation. |
| C29 | Chapter 4 | Onocoy anchor case | Public tokenomics documentation describes a release path with a 16% annual reduction in newly distributed ONO. | mechanism fact | `OnocoyTokenomics` | supported | low | Core release-path fact. Use this as the canonical wording instead of paraphrasing more strongly than the docs allow. |
| C30 | Chapter 4 | Onocoy anchor case | Data Credits are non-transferable, fiat-priced units for service access and are burned on use. | mechanism fact | `OnocoyTokenomics` | supported | low | Central user-side mechanism fact for the Onocoy chapter and later comparative discussion. |
| C31 | Chapter 4 | Onocoy anchor case | Public tokenomics documentation states that fiat revenue finances operations and may be used for ONO buybacks, with bought-back ONO allocated across reward, ecosystem, and burn paths. | mechanism fact | `OnocoyTokenomics` | supported | medium | Keep the modal wording (`may`) and allocation language bounded to the documentation; do not restate this as an unconditional deterministic routing rule. |
| C32 | Chapter 4 | Onocoy anchor case | In the Onocoy evidence stack, the Explorer provides operational and spatial transparency while Dune provides dated on-chain and accounting transparency. | interpretation | `OnocoyExplorer`, `OnocoyDuneDashboard`, `onocoy_dune_qa_mapping_2026-02-26.md` | supported | low | Cross-chapter evidence-boundary claim that clarifies why these public visibility layers are both useful but not interchangeable. |
| C33 | Chapter 5 | Empirical stress layer | Historical stress windows reveal recurring DePIN stress signatures, but they do not reveal counterfactual failure thresholds for newer or only partially observable networks. | empirical observation | `empirical_analysis.tex`; historical stress-window synthesis | partially supported | medium | Safe if phrased as a limit of retrospective evidence rather than as a universal statement about all future networks. |
| C34 | Chapter 5 | Empirical stress layer | Empirical comparison in DePIN requires metric-applicability controls because not all metrics are reliably observable or harmonizable across projects and event windows. | interpretation | `empirical_analysis.tex`; metric-applicability framework | supported | low | Load-bearing Chapter 5 control claim. Keep the emphasis on observability discipline rather than on methodological novelty. |
| C35 | Chapter 5 | Empirical stress layer | For early-stage networks such as Onocoy, several market- and revenue-dependent ratios are `N/R` in the empirical layer under current observability and maturity conditions. | empirical observation | `empirical_analysis.tex`; Onocoy applicability profile | supported | low | Keep explicitly chapter-bounded and time-bounded. Do not restate as a permanent inability to observe these metrics. |
| C36 | Chapter 5 | Empirical stress layer | The empirical chapter motivates DTSE by showing where historical observability becomes insufficient for controlled threshold testing. | interpretation | Chapter 5 empirical boundary; DTSE method contract | supported | medium | Must stay bounded to the thesis architecture and avoid sounding like empirical windows are useless on their own. |
| C37 | Chapter 6 | DTSE methodology | DTSE is a rule-based comparative stress evaluator that applies matched stress inputs across fixed mechanism profiles under explicit assumptions; it is not a forecasting tool. | modeled assumption | `personC_methodology.tex`; `dtse_option_b_defense_memo.md` | supported | low | Supersedes the earlier broad Chapter 6 placeholder claim and makes the non-predictive boundary explicit. |
| C38 | Chapter 6 | DTSE methodology | Chapter 6 separates mechanism facts, modeled assumptions, and DTSE outputs as distinct evidence layers with different interpretive roles. | modeled assumption | `personC_methodology.tex`; V2 methodology architecture | supported | low | Load-bearing evidence-layer claim for the methodology chapter. |
| C39 | Chapter 6 | DTSE methodology | The frozen DTSE experiment set in this thesis consists of one neutral baseline and four stress channels: demand contraction, liquidity shock, competitive-yield pressure, and provider-cost inflation. | modeled assumption | `personC_methodology.tex`; DTSE scenario contract | supported | low | Safe if kept tied to the frozen experiment set rather than generalized beyond this thesis. |
| C40 | Chapter 6 | DTSE methodology | DTSE reports a pre-specified metric suite using baseline-relative comparison rather than absolute performance scoring or live-network ranking. | modeled assumption | `personC_methodology.tex`; `v2_metric_chapter_allocation.md` | supported | low | Core Option B metric-contract claim. |
| C41 | Chapter 6 | DTSE methodology | Stage 1 identifies first material departures from baseline through pre-specified metric thresholds, while Stage 2 classifies failure signatures from patterned deterioration across metric families. | modeled assumption | `personC_methodology.tex`; failure-signature cluster; V2 routing map | partially supported | medium | Strong and useful, but must stay phrased as formal DTSE logic rather than as empirical proof about live failure behavior. |
| C42 | Chapter 6 | DTSE methodology | Reproducibility in DTSE depends on frozen scenario definitions, deterministic seeds, repeated runs, and internal verification under stated assumptions rather than empirical validation of live networks. | modeled assumption | `personC_methodology.tex`; DTSE reproducibility contract | supported | low | Core methodological defensibility claim. |
| C43 | Chapter 7 | Results | Simulation outcomes are reported using a strict sequence-over-magnitude convention, analyzing time-order conditions and baseline-relative deviations rather than absolute magnitude rankings. | modeled assumption | `personC_results.tex`; `v2_results_discussion_defense_guide_gemini3.1.md` | supported | low | Core Option B reporting boundary. |
| C44 | Chapter 7 | Results | Under historical documentation configurations, ONO metric evaluation is subject to the 'Not Reliably Observable' (N/R) rule, requiring DTSE internal simulation to output evaluation sets. | mechanism fact / modeled assumption | `personC_results.tex`; `v2_chapter_contracts.md` | supported | low | Reminds the reader why simulation is required over empirical data. |
| C45 | Chapter 7 | Results | DTSE limits outputs to formal Stage 1 material deviations and Stage 2 failure-signature classifications, explicitly deferring unmodeled human governance interventions to interpretation. | modeled assumption | `v2_results_discussion_defense_guide_gemini3.1.md` | supported | low | Enforces the distinction between deterministic simulation outcomes and theoretical interventions. |
| C46 | Chapter 7 | Results | Baseline trajectories naturally drift due to deterministic mechanism rules, meaning stress must be defined as acceleration or reversal relative to this drift rather than static equilibrium. | modeled assumption | `personC_results.tex`; `v2_results_discussion_defense_guide_gemini3.1.md` | supported | low | Protects against "normal decay" critique. |
| C47 | Chapter 8 | Discussion / conclusion | The accepted DTSE results suggest that DePIN robustness is better interpreted through stress-transmission paths and failure-signature sequences than through binary stable/unstable labels. | interpretation | Chapter 7 accepted results; `personC_discussion_conclusion.tex` | supported | low | Closing interpretive claim. Keep it tied to the accepted experiment set rather than generalizing to all infrastructure systems. |
| C48 | Chapter 8 | Discussion / conclusion | Governance and intervention archetypes in this thesis are discussion-level interpretive categories derived from observed failure signatures; they are not themselves DTSE outputs or empirical prevalence claims. | interpretation | Chapter 7 accepted results; `personC_discussion_conclusion.tex` | supported | low | Important to keep governance discussion bounded and separate from modeled output. |
| C49 | Chapter 8 | Discussion / conclusion | The external validity of DTSE is bounded by exogenous demand stylization, reduced-form price dynamics, simplified provider behavior, and limited governance representation. | interpretation | Chapter 6 methodology limits; `personC_discussion_conclusion.tex` | supported | low | Consolidates the main limitation layer for the discussion chapter. |
| C50 | Chapter 8 | Discussion / conclusion | Within the accepted experiment set, neither BME-oriented nor capped-supply designs escape DePIN physical constraints; they differ in where stress appears first and how it accumulates over time. | interpretation | Chapters 2, 3, and 7 synthesis; `personC_discussion_conclusion.tex` | partially supported | medium | Strong closing claim. Keep explicitly comparative and conditional on the accepted experiment set. |
| C51 | Chapter 8 | Discussion / conclusion | DTSE contributes a bounded comparative evaluator and diagnostic vocabulary that can support disciplined robustness analysis before catastrophic failure without claiming live-network prediction. | interpretation | Chapters 6 and 8 synthesis; `personC_discussion_conclusion.tex` | supported | low | Contribution claim. Keep the non-predictive boundary explicit. |

### Use During Drafting

Before accepting a new section:

1. list the section's load-bearing claims
2. confirm they already exist here or add them
3. check whether the wording in prose is stronger than the evidence status allows
4. downgrade, reframe, or defer any risky claim before acceptance

### Use During Review

When a section feels too smooth or too confident, check this file.

If the prose makes a claim that the ledger still marks as:

- `partially supported`
- `needs sourcing`
- `modeled only`
- `not admissible as load-bearing claim`

then the prose is ahead of the evidence and must be revised.
