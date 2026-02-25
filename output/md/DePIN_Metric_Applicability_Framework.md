# DePIN Metric Applicability Framework

**Consolidated reference document**
**Date:** 2026-02-25
**Source files:** `Depin_Metric_Applicability_Revelations.md`, `sections/empirical_analysis.tex`, `sections/personC_methodology.tex`

---

## Table of Contents

1. [Metric × Project Relevance Matrix](#1-metric--project-relevance-matrix)
2. [Failure Mode → Metric Mapping](#2-failure-mode--metric-mapping)
3. [Stress Scenario → Metric Mapping](#3-stress-scenario--metric-mapping)
4. [DTSE Metric Applicability Catalogue](#4-dtse-metric-applicability-catalogue)
5. [Onocoy Applicability Draft (LaTeX)](#5-onocoy-applicability-draft-latex)
6. [Thesis Insertion Points](#6-thesis-insertion-points)

---

## 1. Metric × Project Relevance Matrix

For each of the five standardised metrics, applicability is rated per project as **Applicable**, **Partially applicable**, or **N/A**.

### Matrix

| Metric | Helium | Geodnet | Onocoy | Render | Hivemapper |
|:-------|:------:|:-------:|:------:|:------:|:----------:|
| **Burn-to-Mint Ratio** | Applicable | Applicable | Partially applicable | Applicable | Applicable |
| **30-Day Node Retention** | Applicable | Applicable | Partially applicable | Applicable | Applicable |
| **Revenue per Node** | Applicable | Applicable | N/A | Applicable | Partially applicable |
| **Token Turnover** | Applicable | Applicable | N/A | Applicable | Partially applicable |
| **FDV / Annualised Revenue** | Applicable | Applicable | N/A | Applicable | Partially applicable |

### Project Totals

| Project | Applicable | Partially | N/A |
|:--------|:----------:|:---------:|:---:|
| Helium | 5 | 0 | 0 |
| Geodnet | 5 | 0 | 0 |
| Onocoy | 0 | 2 | 3 |
| Render | 5 | 0 | 0 |
| Hivemapper | 2 | 3 | 0 |

### Rationale by Metric

**Burn-to-Mint Ratio**

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | Canonical BME design; DC burn and HNT mint are directly observable on-chain. Helium Mobile has approached 1:1 in specific months. |
| Geodnet | Applicable | BME / burn-linked model with documented buyback-and-burn from enterprise revenue ($5.1M annualised). Burn and emission flows are publicly traceable. |
| Onocoy | Partially applicable | Capped-supply model, not pure BME. The analogue is Burn (Data Credit consumption + buyback-burn) divided by Emissions from fixed inventory. Requires adaptation; the resulting ratio is not directly comparable to BME networks without noting the mechanism difference. |
| Render | Applicable | BME model with usage-linked burns (121M+ RNDR burned). Burn-to-mint ratio directly computable. |
| Hivemapper | Applicable | Burn-linked Map Credits consumed on usage. Historically low ratio (high emissions, low burn) but improving with enterprise deals. |

**30-Day Node Retention**

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | 69k+ active nodes with historical data spanning the 2022–2023 crypto winter. Retention under 95% price drop is empirically documented; sunk-cost moat ($500 hotspots) validated. |
| Geodnet | Applicable | Active node count observable. B2B-oriented provider base with Location NFT density controls provides retention signal. |
| Onocoy | Partially applicable | Provider stickiness matters and is conceptually measurable, but the network is early stage with limited historical stress windows. Baseline retention data may be too short for robust 30-day post-shock analysis. |
| Render | Applicable | 3.8k+ GPU nodes. High OpEx (electricity) makes providers sensitive to price drops; retention under stress is directly observable and informative. |
| Hivemapper | Applicable | 77k nodes. Active-labour model means contributors stop immediately when incentives fall below effort threshold. Churn response under HONEY price dips is empirically documented. |

**Revenue per Node**

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | $2.3M/month on-chain revenue across 69k nodes. Per-node revenue is computable and economically interpretable. |
| Geodnet | Applicable | $5.1M annualised revenue. Per-node revenue indicates viability of professional B2B GNSS service without speculative rewards. |
| Onocoy | N/A | Early-stage network with near-zero revenue. Dividing negligible revenue by node count produces a number that conveys no meaningful economic signal. Metric becomes applicable only once demand-side revenue materialises. |
| Render | Applicable | Documented compute revenue and GPU node count allow per-node calculation. Indicates whether compute rewards justify high electricity OpEx. |
| Hivemapper | Partially applicable | Enterprise deals (Lyft, Trimble, TomTom) generate revenue, but mapper compensation is labour-based (fuel + time), making "revenue per node" less precise than "revenue per active contributor-hour". |

**Token Turnover**

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | HNT has deep liquidity and years of trading history. Turnover during price drops distinguishes mercenary exit from utility usage. |
| Geodnet | Applicable | GEOD is traded and observable. Turnover signal is interpretable alongside burn data. |
| Onocoy | N/A | ONO TGE occurred in 2025; secondary market liquidity may be thin. Turnover on an illiquid market reflects market-microstructure noise, not economic behaviour. Metric becomes applicable once sustained trading volume is established. |
| Render | Applicable | RNDR has deep liquidity. High turnover during drawdowns signals speculative exit pressure. |
| Hivemapper | Partially applicable | HONEY is traded but with lower liquidity than HNT or RNDR. Turnover is computable but should be interpreted cautiously given thinner order books. |

**FDV / Annualised Revenue**

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | Annualised revenue ($27.6M) and FDV are both observable. Ratio indicates speculative premium and is directly comparable across mature DePINs. |
| Geodnet | Applicable | $5.1M annualised revenue provides a denominator. Ratio is finite and interpretable. |
| Onocoy | N/A | With near-zero annualised revenue the ratio is either undefined or astronomically large. It conveys no comparative information. Metric becomes applicable once Onocoy generates sustained service revenue. |
| Render | Applicable | Documented compute demand and FDV allow direct calculation. |
| Hivemapper | Partially applicable | Enterprise revenue is growing but still modest relative to FDV. The ratio is computable but may overstate speculative premium while B2B pipeline is ramping. |

**Key finding:** Only 2 of 5 standardised metrics are currently applicable to Onocoy, and both require adaptation caveats. The three revenue- and liquidity-dependent metrics are not meaningful for an early-stage network.

---

## 2. Failure Mode → Metric Mapping

Each of the five empirical failure modes is mapped to the metrics that best detect it.

### Mapping Table

| Failure Mode | Primary Metric(s) | Secondary Metric(s) | Rationale |
|:-------------|:-------------------|:---------------------|:----------|
| **Reward–Demand Decoupling** | Burn-to-Mint Ratio | Revenue per Node; FDV / Annualised Revenue | A declining Burn-to-Mint ratio is the direct signal: emissions continue while usage-driven burns weaken. Revenue per Node confirms whether individual providers are receiving economically meaningful demand-side income. FDV/Revenue contextualises how much speculative premium is propping up valuation relative to actual usage. |
| **Liquidity-Driven Incentive Compression** | Token Turnover | 30-Day Node Retention; Burn-to-Mint Ratio | Spiking Token Turnover during a price drawdown signals mercenary-capital exit. 30-Day Retention captures the lagged downstream effect: providers exit after reward value collapses in fiat terms. Burn-to-Mint deteriorates secondarily as the fiat value of burns shrinks while nominal emissions persist. |
| **Latent Capacity Degradation** | 30-Day Node Retention | Revenue per Node; Burn-to-Mint Ratio | Retention that appears stable while quality/uptime scores decline is the defining signature. Revenue per Node provides the economic context: when per-node income falls below maintenance thresholds, providers remain online but stop servicing hardware. |
| **Elastic Provider Exit** | 30-Day Node Retention | Token Turnover; Revenue per Node | Elevated churn without a corresponding price crash or demand shock is the primary signal — providers are leaving for better yield elsewhere. Revenue per Node on the competitor network quantifies the yield gap driving exit. |
| **Dilution Feedback Loop** | Burn-to-Mint Ratio; 30-Day Node Retention | Token Turnover; FDV / Annualised Revenue | Compound failure requiring simultaneous deterioration. A falling Burn-to-Mint ratio combined with falling retention are both primary — the loop requires both legs. Token Turnover spikes confirm sell-pressure acceleration. |

### Metric Coverage Summary

| Metric | Primary signal for | Secondary signal for | Total |
|:-------|:------------------:|:--------------------:|:-----:|
| Burn-to-Mint Ratio | 2 | 3 | 5 |
| 30-Day Node Retention | 2 | 1 | 3 |
| Token Turnover | 1 | 2 | 3 |
| Revenue per Node | 0 | 3 | 3 |
| FDV / Annualised Revenue | 0 | 2 | 2 |

**Key observation:** Burn-to-Mint Ratio is the single most diagnostic metric — it participates in all five failure modes (twice as primary). Revenue per Node and FDV/Revenue serve exclusively as secondary contextual indicators.

### Onocoy Failure-Mode Monitorability

With 3 of 5 metrics currently N/A for early-stage Onocoy:

- **Reward–Demand Decoupling** — detectable via adapted Burn-to-Mint but lacks secondary confirmation.
- **Liquidity-Driven Incentive Compression** — not reliably detectable until ONO has sustained trading volume.
- **Latent Capacity Degradation** — detectable via retention alone, but without Revenue per Node the economic trigger is invisible.
- **Elastic Provider Exit** — detectable via retention; the most observable failure mode for Onocoy today.
- **Dilution Feedback Loop** — largely unmonitorable until Onocoy matures.

---

## 3. Stress Scenario → Metric Mapping

Four stress scenarios are mapped to which metrics are most and least informative.

### Scenario Definitions

| Scenario | Empirical Anchor | DTSE Dimension |
|:---------|:-----------------|:---------------|
| **Liquidity Shock** | Crypto Winter 2022–2023; Helium 95% price drop | S2: Discrete token unlock into finite AMM depth |
| **Competitive Yield Pressure** | Geodnet vs Onocoy vampire-attack dynamics (2024–2025) | S3: External competitor yield parameter |
| **Demand Collapse** | Implied by subsidy-gap framing; high-to-decay demand regime | S1: Demand contraction; volatile / high-to-decay regimes |
| **Cost / Provider Economics** | Hivemapper 2024 OpEx shock (fuel + time) | S4: Provider cost inflation; differential by tier |

### Mapping Table

| Stress Scenario | Most Informative Metrics | Least Informative Metrics | Rationale |
|:----------------|:-------------------------|:--------------------------|:----------|
| **Liquidity Shock** | Token Turnover, 30-Day Node Retention | Revenue per Node, FDV / Annualised Revenue | Token Turnover spikes reveal whether sell-off is mercenary exit or utility circulation. Revenue per Node is uninformative because the shock is price-driven, not demand-driven. FDV/Revenue is distorted by price-driven FDV swings. |
| **Competitive Yield Pressure** | 30-Day Node Retention, Revenue per Node | Token Turnover, FDV / Annualised Revenue | Retention is the direct observable: providers leave for better yield without a price crash. Token Turnover is uninformative because competitive exit is provider-side behaviour, not a market-trading signal. |
| **Demand Collapse** | Burn-to-Mint Ratio, Revenue per Node | Token Turnover, 30-Day Node Retention (initially) | Burn-to-Mint is the earliest signal: burns fall as usage declines while emissions continue. 30-Day Retention is a lagging indicator — providers exit only after sustained unprofitability. |
| **Cost / Provider Economics** | 30-Day Node Retention, Revenue per Node | Token Turnover, FDV / Annualised Revenue | Retention captures the direct outcome: providers exit when margins turn negative. Token Turnover is uninformative because the stress is provider-side economics, not market liquidity. |

### Metric Signal Strength

| Metric | Most Informative | Least Informative | Net Signal |
|:-------|:----------------:|:-----------------:|:----------:|
| 30-Day Node Retention | 3 | 1 | Strong |
| Revenue per Node | 3 | 1 | Strong |
| Burn-to-Mint Ratio | 1 | 0 | Moderate–Strong |
| Token Turnover | 1 | 3 | Weak (scenario-specific) |
| FDV / Annualised Revenue | 0 | 4 | Weak |

**Burn-to-Mint as a confirming metric:** While it appears as "most informative" only under Demand Collapse, it participates in all five failure modes as a second-order confirmation that a shock is propagating into incentive solvency.

### Onocoy Scenario Monitorability

| Scenario | Onocoy Status |
|:---------|:--------------|
| Liquidity Shock | Primary metric (Token Turnover) is N/A post-TGE. **Partially monitorable.** |
| Competitive Yield Pressure | Retention usable; yield-gap quantification requires Revenue per Node. **Partially monitorable.** |
| Demand Collapse | Burn-to-Mint partially applicable; Revenue per Node is N/A. **Weakly monitorable.** |
| Cost / Provider Economics | Retention usable; Revenue per Node N/A but cost-side analysis can substitute. **Partially monitorable.** |

No scenario is fully monitorable for Onocoy today.

---

## 4. DTSE Metric Applicability Catalogue

All 10 DTSE metrics catalogued by mechanism assumption, data requirement, and temporal applicability.

### Summary Matrix

| DTSE Metric | Mechanism | Data Requirement | Temporal Applicability |
|:------------|:---------:|:----------------:|:----------------------:|
| Provider Retention | Both | Public | Both |
| Churn | Both | Public | Both |
| Capacity Utilisation | Both | Internal / Simulated | Mature |
| Burn-to-Mint Ratio | BME (native); Capped (adapted) | Public | Mature (primarily) |
| Net Emissions | Both | Public | Both |
| Token Velocity | Both | Public | Mature |
| Incentive Efficiency | Both | Public + Simulated | Both |
| Volatility Proxy | Both | Public / Simulated | Mature |
| Death Spiral Probability | Both | Simulated | Both (simulation only) |
| Revenue / Profitability | Both | Public (partial) / Internal | Mature |

### Detailed Notes

**Provider Retention** — Mechanism-agnostic. Public data. Meaningful from launch.

**Churn** — Complement of retention. Public data. Early-stage churn may be dominated by setup failures rather than economic stress.

**Capacity Utilisation** — Requires demand served (typically internal). Near-zero demand in early-stage makes the ratio uninformative.

**Burn-to-Mint Ratio** — Natively BME; requires adaptation for capped supply (Data Credit consumption + buyback-burn / emissions from fixed inventory). Directional trends useful even early-stage; cross-project comparison requires maturity.

**Net Emissions** — Public. Computable from launch. Diagnostically useful when trends deviate from the expected emission curve.

**Token Velocity** — Public but requires sustained liquidity. Post-TGE tokens with thin order books produce noise, not signal.

**Incentive Efficiency** — Emissions (USD) / Capacity. High early-stage values are expected (bootstrap overpaying). Useful when comparing protocol profiles under identical stress.

**Volatility Proxy** — Requires trading history for reliable dispersion statistics. Within DTSE simulation, generated endogenously.

**Death Spiral Probability** — Simulation-only. Requires multiple Monte Carlo runs. Not computable from real-world single-trajectory observation.

**Revenue / Profitability** — Revenue is near-zero early-stage. Per-provider profitability requires OpEx/CapEx cost data (typically internal or interview-derived).

### Key Observations

1. **8 of 10 metrics are mechanism-agnostic.** Only Burn-to-Mint requires adaptation for capped supply.
2. **Data splits into two tiers.** Retention, churn, net emissions, and burn-to-mint are fully public. Capacity utilisation, profitability, and death spiral probability require internal data or simulation.
3. **Temporal applicability is the binding constraint.** 5 of 10 metrics only work for mature networks. For early-stage Onocoy, only Retention, Churn, Net Emissions, Incentive Efficiency, and Death Spiral Probability (sim) produce reliable signal.

---

## 5. Onocoy Applicability Draft (LaTeX)

~190-word subsection ready for insertion into the thesis. Per [§6 Insertion Points](#6-thesis-insertion-points), this goes into `sections/personA_onocoy.tex` before the import block.

```latex
\subsection{Metric Applicability for Onocoy}
\label{subsec:onocoy_metric_applicability}

The five standardised metrics defined in Table~\ref{tab:comparative_metrics} are not uniformly applicable to Onocoy. As a capped-supply network with a recent token generation event and near-zero annualised service revenue, several metrics fail to produce interpretable values.

\textbf{30-Day Node Retention} is directly applicable. Provider stickiness is central to GNSS infrastructure sustainability, and retention under stress can be observed from on-chain participation data once a sufficient observation window exists.

\textbf{Burn-to-Mint Ratio} is partially applicable. Onocoy does not use pure Burn-and-Mint Equilibrium; the analogue is Data Credit consumption plus buyback-burn revenue divided by emissions from capped inventory. The resulting ratio is directionally informative but not directly comparable to BME-native networks without noting the mechanism difference.

\textbf{Revenue per Node}, \textbf{Token Turnover}, and \textbf{FDV / Annualised Revenue} are not currently applicable. With negligible service revenue, per-node ratios are undefined. Token Turnover requires sustained secondary-market liquidity, which may be insufficient post-TGE. FDV divided by near-zero revenue produces values that cannot support comparative inference.

These limitations redirect analytical attention toward stress dimensions where Onocoy-specific signals are stronger: competitive yield pressure relative to Geodnet, the subsidy gap between provider costs and realised fiat revenue, elastic provider exit under triple-mining conditions, and sunk-cost retention friction from physical installation requirements.
```

---

## 6. Thesis Insertion Points

Three exact insertion points for adding applicability content to the thesis `.tex` files.

### 6a. "Don't Grade on N/A" Rule

| Field | Value |
|:------|:------|
| **File** | `sections/personC_methodology.tex` |
| **Section** | `\subsection{Interpretation and Limitations of Metrics}` (line 225) |
| **Insert** | **After** line 228: *"This cautious interpretation aligns with best practices in simulation-based research and supports the thesis's evaluative rather than predictive orientation \cite{Braakman2022}."* |

**Suggested text:**

> Not all metrics are equally applicable to all protocol profiles or maturity stages. Where a metric's preconditions are not met — for example, where annualised revenue is near zero or secondary-market liquidity is insufficient for meaningful turnover measurement — the metric is excluded from comparative evaluation for that profile rather than computed with a misleading or undefined value. This ensures that protocols are assessed only on dimensions where the metric produces an interpretable signal.

### 6b. Onocoy Metric Applicability Subsection

| Field | Value |
|:------|:------|
| **File** | `sections/personA_onocoy.tex` |
| **Section** | After `\subsection{Tokenomic Mechanics (Descriptive)}` (ends at line 27) |
| **Insert** | **Before** the import block at line 29 |
| **New label** | `\subsection{Metric Applicability for Onocoy}` |

**Suggested text:** Use the LaTeX draft in [§5](#5-onocoy-applicability-draft-latex) above.

### 6c. Metric Applicability Framework

| Field | Value |
|:------|:------|
| **File** | `sections/personC_methodology.tex` |
| **Section** | `\section{Evaluation Metrics}` → after `\subsection{Principles for Metric Selection}` (ends at line 176) |
| **Insert** | **After** line 176, **before** line 178 (`\subsection{Core Sustainability Metrics}`) |
| **New label** | `\subsection{Metric Applicability Conditions}` |

**Suggested text:**

> Before defining individual metrics, this section specifies the conditions under which each metric produces a meaningful signal. Applicability depends on three dimensions: mechanism class (whether the protocol uses BME, capped supply, or hybrid designs), maturity stage (whether sufficient revenue and trading history exist to compute the metric), and data availability (whether the required inputs are publicly observable or require internal data). Metrics that fail one or more preconditions for a given protocol profile are excluded from comparative evaluation of that profile, consistent with the interpretation boundaries defined in Section \ref{sec:evaluation_metrics}. The full applicability matrix is provided in the supplementary materials.

### Summary of Insertion Points

| Addition | File | Location | New Subsection? |
|:---------|:-----|:---------|:----------------|
| "Don't grade on N/A" rule | `personC_methodology.tex` | After line 228 | No — append to existing |
| Onocoy metric applicability | `personA_onocoy.tex` | Before line 29 | Yes |
| Metric applicability framework | `personC_methodology.tex` | After line 176, before line 178 | Yes |

---

## Superseded Files

This consolidated document replaces the following individual files, which remain in the repository for git history but should no longer be referenced independently:

| File | Consolidated Into |
|:-----|:------------------|
| `output/md/Metric_Relevance_Matrix.md` | [§1](#1-metric--project-relevance-matrix) |
| `output/md/Failure_Mode_Metric_Mapping.md` | [§2](#2-failure-mode--metric-mapping) |
| `output/md/Stress_Scenario_Metric_Mapping.md` | [§3](#3-stress-scenario--metric-mapping) |
| `output/md/DTSE_Metric_Applicability.md` | [§4](#4-dtse-metric-applicability-catalogue) |
| `output/md/Onocoy_Applicability_Draft.tex` | [§5](#5-onocoy-applicability-draft-latex) |
| `output/md/Applicability_Insertion_Points.md` | [§6](#6-thesis-insertion-points) |

---

*Generated 2026-02-25 from DePIN Tokenomics Thesis (cas-depin-tokenomics).*
