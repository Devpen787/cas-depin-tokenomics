# DTSE Metric Applicability Catalogue

**Source:** `sections/personC_methodology.tex` (§Evaluation Metrics), `output/md/Depin_Metric_Applicability_Revelations.md` §8
**Date:** 2026-02-25

---

## Applicability Dimensions

| Dimension | Values | Definition |
|:----------|:-------|:-----------|
| **Mechanism assumption** | BME / Capped / Both | Which token-design class the metric natively assumes. |
| **Data requirement** | Public / Internal / Simulated | Whether the inputs are publicly observable on-chain, require internal/private data, or are only available inside the DTSE simulation. |
| **Temporal applicability** | Early-stage / Mature / Both | When the metric produces a meaningful signal. Early-stage = pre-revenue or post-TGE with thin liquidity. Mature = established revenue and trading history. |

---

## Core Sustainability Metrics

### Provider Retention

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Retention is mechanism-agnostic — it measures provider participation regardless of whether emissions are BME or capped. Applicable to any DePIN with observable node counts. |
| Data requirement | **Public** | Active node counts are observable on-chain or through protocol dashboards. No internal data required. |
| Temporal applicability | **Both** | Meaningful from launch once a baseline node count exists. Early-stage networks have shorter observation windows, reducing statistical confidence in post-shock retention rates, but the metric itself is computable. |

### Churn

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Churn is the complement of retention — provider exit events are observable regardless of emission design. |
| Data requirement | **Public** | Derived from changes in active node counts between periods. Requires sufficiently granular time-series data (weekly or finer). |
| Temporal applicability | **Both** | Computable from launch. Early-stage churn may be dominated by setup failures or experimental participants rather than economic stress, requiring careful interpretation. |

### Capacity Utilisation

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Utilisation = demand served / available capacity. Independent of emission design; depends on whether demand and capacity are observable. |
| Data requirement | **Internal / Simulated** | Aggregate capacity may be publicly estimable (node count × average throughput), but actual demand served is typically internal to the protocol or only available in the DTSE simulation. |
| Temporal applicability | **Mature** | Requires sustained demand to produce a meaningful ratio. In early-stage networks with negligible demand, utilisation is near zero by definition and conveys no diagnostic signal about mechanism health. |

### Burn-to-Mint Ratio (Incentive Solvency)

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **BME (native); Capped (adapted)** | Natively defined for BME designs where burn and mint are explicit protocol operations. For capped-supply designs (e.g. Onocoy), the analogue is Data Credit consumption + buyback-burn divided by emissions from fixed inventory. The resulting ratio is directionally comparable but not numerically equivalent across mechanism classes. |
| Data requirement | **Public** | Burn events and emission schedules are on-chain observables for most DePINs. Buyback-burn routing may require protocol-specific dashboard data. |
| Temporal applicability | **Mature (primarily)** | In early-stage networks the ratio is expected to be well below 1.0 by design (subsidy phase). While computable, its value is uninformative for cross-project comparison until the network has meaningful demand-driven burn volume. Directional trends (improving vs worsening) remain useful even early-stage. |

### Net Emissions and Inflation Dynamics

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Net emissions = gross issuance − burns/destruction. Computable for both BME (continuous mint/burn) and capped-supply (scheduled emissions − buyback-burn). Interpretation differs: for BME, net emissions reflect demand coupling; for capped supply, they reflect the rate at which the fixed inventory is being consumed. |
| Data requirement | **Public** | Emission schedules are documented in protocol whitepapers. Burn volumes are on-chain. Net emissions are derived. |
| Temporal applicability | **Both** | Computable from launch. Early-stage networks exhibit high net emissions by design; the metric becomes diagnostically useful when trends deviate from the expected emission curve, signalling stress or demand shifts. |

### Token Velocity (Proxy)

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Transaction turnover is mechanism-agnostic in principle. However, interpretation differs: high velocity in a BME system may indicate healthy utility cycling, while high velocity in a capped-supply system may signal speculative churn. |
| Data requirement | **Public** | Requires on-chain transfer volume and circulating supply. Both are publicly available for tokens listed on exchanges. |
| Temporal applicability | **Mature** | Requires sustained secondary-market liquidity to distinguish economic signal from microstructure noise. Post-TGE tokens with thin order books produce turnover values dominated by a few large transactions, which do not reflect systemic velocity. The thesis notes this metric should be "interpreted comparatively and cautiously". |

### Incentive Efficiency (Capital Efficiency)

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Defined as total emissions (USD-valued) / aggregate validated capacity. Applicable to any design where emissions and capacity are measurable. |
| Data requirement | **Public + Simulated** | Emissions are public (schedule × price). Aggregate validated capacity requires protocol-specific definitions (e.g. number of stations, TB stored, GPU-hours) which may be publicly reported or estimated. In the DTSE simulation, both are directly available. |
| Temporal applicability | **Both** | Computable from launch. Early-stage values will be high (over-paying per unit of capacity during bootstrap) by design. The metric becomes diagnostically useful when efficiency trends diverge between protocol profiles under identical stress, revealing which mechanisms bootstrap more cost-effectively. |

### Volatility Proxy

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Price dispersion is observable for any traded token. Used as a stress input signal (affecting provider incentives) rather than an outcome metric. |
| Data requirement | **Public / Simulated** | Real-world volatility is computable from exchange price data. Within DTSE, volatility is generated by the reduced-form price model and is directly available. |
| Temporal applicability | **Mature** | Requires sufficient trading history for dispersion statistics to be meaningful. Post-TGE tokens with days or weeks of price data produce unreliable volatility estimates. Within the DTSE simulation this constraint does not apply, as volatility is generated endogenously. |

---

## Derived Summary Indicators

### Death Spiral Probability

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Defined as the frequency of concurrent declines in price, provider count, and service capacity beyond thresholds. Mechanism-agnostic — it measures compound failure regardless of emission design. |
| Data requirement | **Simulated** | This is a simulation-only indicator. It requires multiple Monte Carlo runs to estimate frequency. Not computable from real-world observation of a single network trajectory. |
| Temporal applicability | **Both (simulation)** | Computable for any simulated protocol profile at any stage. Not applicable to real-world early-stage or mature networks directly — it exists only within the DTSE evaluation framework. |

### Network Revenue and Provider Profitability

| Dimension | Value | Notes |
|:----------|:------|:------|
| Mechanism assumption | **Both** | Revenue and profitability are mechanism-agnostic. Revenue sources differ (burn-linked for BME, Data Credit sales for Onocoy), but the aggregate and per-provider figures are computable for any design. |
| Data requirement | **Public (partial) / Internal** | Aggregate on-chain revenue may be estimable from burn volumes or reported figures. Per-provider profitability requires cost data (OpEx, CapEx) that is typically internal or interview-derived. DTSE computes both from modelled parameters. |
| Temporal applicability | **Mature** | Revenue is near-zero for early-stage networks, making profitability metrics undefined or misleading. The metric becomes informative once sustained demand generates measurable revenue flows. Within the DTSE simulation, profitability is computable at any stage. |

---

## Summary Matrix

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

### Key Observations

1. **Mechanism-agnostic metrics dominate.** 8 of 10 metrics are applicable to both BME and capped-supply designs. Only Burn-to-Mint requires explicit adaptation for capped-supply models — the formula changes but the concept transfers.

2. **Data availability splits into two tiers.** Retention, churn, net emissions, and burn-to-mint are fully public. Capacity utilisation, profitability, and death spiral probability require internal data or simulation access.

3. **Temporal applicability is the binding constraint.** 5 of 10 metrics are only meaningful for mature networks (Capacity Utilisation, Burn-to-Mint, Token Velocity, Volatility Proxy, Revenue/Profitability). For early-stage networks like Onocoy, only Retention, Churn, Net Emissions, Incentive Efficiency, and Death Spiral Probability (simulation) produce reliable signal.

4. **The thesis gap:** `personC_methodology.tex` defines these metrics but does not state their applicability conditions. This catalogue fills the gap identified in `Depin_Metric_Applicability_Revelations.md` §8 ("Mechanism-class applicability", "Temporal applicability").

---

*Cross-references: `output/md/Metric_Relevance_Matrix.md`, `output/md/Failure_Mode_Metric_Mapping.md`, `output/md/Stress_Scenario_Metric_Mapping.md`, `output/md/Applicability_Insertion_Points.md`.*
