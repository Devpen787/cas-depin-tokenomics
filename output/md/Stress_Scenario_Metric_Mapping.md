# Stress Scenario → Metric Mapping

**Source:** `sections/empirical_analysis.tex` (§4.3 empirical stress scenarios), `sections/personC_methodology.tex` (§5.4 stress dimensions, §6.3 DTSE scenarios), `output/md/Depin_Metric_Applicability_Revelations.md`
**Date:** 2026-02-25

---

## Scenario Definitions

The four stress scenarios below consolidate the empirical events from `empirical_analysis.tex` with the DTSE simulation dimensions from `personC_methodology.tex`.

| Scenario | Empirical Anchor | DTSE Dimension |
|:---------|:-----------------|:---------------|
| **Liquidity Shock** | Crypto Winter 2022–2023; Helium 95% price drop | S2: Discrete token unlock into finite AMM depth |
| **Competitive Yield Pressure** | Geodnet vs Onocoy vampire-attack dynamics (2024–2025) | S3: External competitor yield parameter |
| **Demand Collapse** | Implied by subsidy-gap framing; high-to-decay demand regime | S1: Demand contraction; volatile / high-to-decay regimes |
| **Cost / Provider Economics** | Hivemapper 2024 OpEx shock (fuel + time) | S4: Provider cost inflation; differential by tier |

---

## Mapping Table

| Stress Scenario | Most Informative Metrics | Least Informative Metrics | Rationale |
|:----------------|:-------------------------|:--------------------------|:----------|
| **Liquidity Shock** | **Token Turnover**, **30-Day Node Retention** | Revenue per Node, FDV / Annualised Revenue | Token Turnover spikes reveal whether sell-off is mercenary exit or utility circulation — the defining signal. 30-Day Retention captures the lagged churn response as fiat-denominated reward value collapses. Revenue per Node is uninformative because the shock is price-driven, not demand-driven — service usage may be unchanged. FDV/Revenue is distorted: FDV craters with price while revenue may hold, producing misleading ratio swings. |
| **Competitive Yield Pressure** | **30-Day Node Retention**, **Revenue per Node** | Token Turnover, FDV / Annualised Revenue | Retention is the direct observable: providers leave for better yield elsewhere without a price crash or demand shock. Revenue per Node on the home network vs the competitor quantifies the yield gap driving exit. Token Turnover is uninformative because competitive exit is a provider-side behaviour, not a market-trading signal — providers may simply stop claiming rather than sell. FDV/Revenue does not capture the relative-yield dynamic across networks. |
| **Demand Collapse** | **Burn-to-Mint Ratio**, **Revenue per Node** | Token Turnover, 30-Day Node Retention (initially) | Burn-to-Mint is the earliest signal: burns fall as usage declines while emissions continue on schedule. Revenue per Node confirms the per-provider economic impact. Token Turnover is uninformative because trading behaviour may be unaffected by a demand-side contraction (price can remain stable if speculation fills the gap). 30-Day Retention is a lagging indicator — providers exit only after sustained unprofitability, so retention appears stable during the early phase of demand collapse when it matters most. |
| **Cost / Provider Economics** | **30-Day Node Retention**, **Revenue per Node** | Token Turnover, FDV / Annualised Revenue | Retention captures the direct outcome: providers exit when margins turn negative. Revenue per Node contextualises whether the profitability squeeze comes from the cost side (OpEx rising) or the revenue side (rewards falling). Token Turnover is uninformative because the stress is provider-side economics, not market liquidity — trading volume may be unaffected. FDV/Revenue is unresponsive to cost shocks because neither FDV nor protocol revenue change when provider OpEx increases. |

---

## Metric Informativeness Summary

How informative each metric is across all four scenarios:

| Metric | Most Informative | Least Informative | Net Signal Strength |
|:-------|:----------------:|:-----------------:|:-------------------:|
| **30-Day Node Retention** | 3 | 1 (lagging under demand collapse) | Strong |
| **Revenue per Node** | 3 | 1 | Strong |
| **Burn-to-Mint Ratio** | 1 | 0 | Moderate–Strong |
| **Token Turnover** | 1 | 3 | Weak (scenario-specific) |
| **FDV / Annualised Revenue** | 0 | 4 | Weak (not informative in any isolated scenario) |

### Reading the table

- **30-Day Node Retention** and **Revenue per Node** are the most broadly informative — they surface meaningful signal in 3 of 4 scenarios.
- **Burn-to-Mint Ratio** is the single strongest signal for demand-side stress but is less directly informative under liquidity, competitive, or cost shocks (where it serves as a secondary/confirming metric per the `Failure_Mode_Metric_Mapping.md`).
- **Token Turnover** is highly informative for liquidity shocks specifically but generates noise or irrelevant signal in the other three scenarios.
- **FDV / Annualised Revenue** is not the most informative metric in any of the four isolated scenarios. Its value is comparative (cross-project benchmarking at a point in time) rather than diagnostic (detecting a specific stress event).

---

## Burn-to-Mint as a Confirming Metric

While Burn-to-Mint appears as "most informative" only under Demand Collapse, the `Failure_Mode_Metric_Mapping.md` shows it participates in all five failure modes (twice as primary). The apparent tension resolves as follows: Burn-to-Mint is the best **structural health** indicator — it integrates demand, emissions, and mechanism design into a single ratio — but under scenarios where the primary shock is price-driven (liquidity), provider-driven (cost/competitive), or market-driven (turnover), the initial signal comes from other metrics first. Burn-to-Mint then deteriorates as a **second-order confirmation** that the shock is propagating into incentive solvency.

---

## Onocoy Applicability Note

Per `Metric_Relevance_Matrix.md`, three metrics are currently N/A for early-stage Onocoy:

| Scenario | Effect on Onocoy Monitoring |
|:---------|:----------------------------|
| Liquidity Shock | Primary metric (Token Turnover) is N/A post-TGE. Only 30-Day Retention is usable. **Partially monitorable.** |
| Competitive Yield Pressure | Both primary metrics (Retention, Revenue per Node) require one to be N/A. Retention alone is usable; yield-gap quantification requires Revenue per Node on both networks. **Partially monitorable.** |
| Demand Collapse | Primary metric (Burn-to-Mint) is partially applicable via adaptation. Revenue per Node is N/A. **Weakly monitorable.** |
| Cost / Provider Economics | Retention is usable. Revenue per Node is N/A but cost-side analysis can substitute internal margin data. **Partially monitorable.** |

No scenario is fully monitorable for Onocoy today. This reinforces the recommendation for Onocoy-specific proxy metrics (subsidy gap, competitive yield delta, sunk-cost friction) as complements to the standardised set.

---

*Cross-references: `output/md/Metric_Relevance_Matrix.md`, `output/md/Failure_Mode_Metric_Mapping.md`, `output/md/Depin_Metric_Applicability_Revelations.md` §6 step 5.*
