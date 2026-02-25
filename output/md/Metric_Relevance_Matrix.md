# Metric × Project Relevance Matrix

**Source:** `output/md/Depin_Metric_Applicability_Revelations.md`, `sections/empirical_analysis.tex`
**Date:** 2026-02-25

---

## Applicability Legend

| Rating | Meaning |
|:-------|:--------|
| **Applicable** | Metric is directly computable from available data and interpretable for this project's mechanism design. |
| **Partially applicable** | Metric can be adapted or computed with caveats (e.g. mechanism mismatch, limited data, early-stage distortion). |
| **N/A** | Metric is not meaningful for this project due to mechanism design, maturity stage, or data availability. |

---

## Metric × Project Matrix

| Metric | Helium | Geodnet | Onocoy | Render | Hivemapper |
|:-------|:------:|:-------:|:------:|:------:|:----------:|
| **Burn-to-Mint Ratio** | Applicable | Applicable | Partially applicable | Applicable | Applicable |
| **30-Day Node Retention** | Applicable | Applicable | Partially applicable | Applicable | Applicable |
| **Revenue per Node** | Applicable | Applicable | N/A | Applicable | Partially applicable |
| **Token Turnover** | Applicable | Applicable | N/A | Applicable | Partially applicable |
| **FDV / Annualised Revenue** | Applicable | Applicable | N/A | Applicable | Partially applicable |

---

## Rationale

### Burn-to-Mint Ratio

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | Canonical BME design; DC burn and HNT mint are directly observable on-chain. Helium Mobile has approached 1:1 in specific months. |
| Geodnet | Applicable | BME / burn-linked model with documented buyback-and-burn from enterprise revenue ($5.1M annualised). Burn and emission flows are publicly traceable. |
| Onocoy | Partially applicable | Capped-supply model, not pure BME. The analogue is Burn (Data Credit consumption + buyback-burn) divided by Emissions from fixed inventory. Requires adaptation; the resulting ratio is not directly comparable to BME networks without noting the mechanism difference. |
| Render | Applicable | BME model with usage-linked burns (121M+ RNDR burned). Burn-to-mint ratio directly computable. |
| Hivemapper | Applicable | Burn-linked Map Credits consumed on usage. Historically low ratio (high emissions, low burn) but improving with enterprise deals. |

### 30-Day Node Retention

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | 69k+ active nodes with historical data spanning the 2022–2023 crypto winter. Retention under 95% price drop is empirically documented; sunk-cost moat ($500 hotspots) validated. |
| Geodnet | Applicable | Active node count observable. B2B-oriented provider base with Location NFT density controls provides retention signal. |
| Onocoy | Partially applicable | Provider stickiness matters and is conceptually measurable, but the network is early stage with limited historical stress windows. Baseline retention data may be too short for robust 30-day post-shock analysis. |
| Render | Applicable | 3.8k+ GPU nodes. High OpEx (electricity) makes providers sensitive to price drops; retention under stress is directly observable and informative. |
| Hivemapper | Applicable | 77k nodes. Active-labour model means contributors stop immediately when incentives fall below effort threshold. Churn response under HONEY price dips is empirically documented. |

### Revenue per Node

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | $2.3M/month on-chain revenue across 69k nodes. Per-node revenue is computable and economically interpretable. |
| Geodnet | Applicable | $5.1M annualised revenue. Per-node revenue indicates viability of professional B2B GNSS service without speculative rewards. |
| Onocoy | N/A | Early-stage network with near-zero revenue. Dividing negligible revenue by node count produces a number that conveys no meaningful economic signal. Metric becomes applicable only once demand-side revenue materialises. |
| Render | Applicable | Documented compute revenue and GPU node count allow per-node calculation. Indicates whether compute rewards justify high electricity OpEx. |
| Hivemapper | Partially applicable | Enterprise deals (Lyft, Trimble, TomTom) generate revenue, but mapper compensation is labour-based (fuel + time), making "revenue per node" less precise than "revenue per active contributor-hour". |

### Token Turnover

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | HNT has deep liquidity and years of trading history. Turnover during price drops distinguishes mercenary exit from utility usage. |
| Geodnet | Applicable | GEOD is traded and observable. Turnover signal is interpretable alongside burn data. |
| Onocoy | N/A | ONO TGE occurred in 2025; secondary market liquidity may be thin. Turnover on an illiquid market reflects market-microstructure noise, not economic behaviour. Metric becomes applicable once sustained trading volume is established. |
| Render | Applicable | RNDR has deep liquidity. High turnover during drawdowns signals speculative exit pressure. |
| Hivemapper | Partially applicable | HONEY is traded but with lower liquidity than HNT or RNDR. Turnover is computable but should be interpreted cautiously given thinner order books. |

### FDV / Annualised Revenue

| Project | Rating | Rationale |
|:--------|:------:|:----------|
| Helium | Applicable | Annualised revenue ($27.6M) and FDV are both observable. Ratio indicates speculative premium and is directly comparable across mature DePINs. |
| Geodnet | Applicable | $5.1M annualised revenue provides a denominator. Ratio is finite and interpretable. |
| Onocoy | N/A | With near-zero annualised revenue the ratio is either undefined or astronomically large. It conveys no comparative information. Metric becomes applicable once Onocoy generates sustained service revenue. |
| Render | Applicable | Documented compute demand and FDV allow direct calculation. |
| Hivemapper | Partially applicable | Enterprise revenue is growing but still modest relative to FDV. The ratio is computable but may overstate speculative premium while B2B pipeline is ramping. |

---

## Summary

| Project | Applicable | Partially | N/A |
|:--------|:----------:|:---------:|:---:|
| Helium | 5 | 0 | 0 |
| Geodnet | 5 | 0 | 0 |
| Onocoy | 0 | 2 | 3 |
| Render | 5 | 0 | 0 |
| Hivemapper | 2 | 3 | 0 |

**Key finding:** Only 2 of 5 standardised metrics are currently applicable to Onocoy, and both require adaptation caveats. The three revenue- and liquidity-dependent metrics (Revenue per Node, Token Turnover, FDV/Revenue) are not meaningful for an early-stage network with near-zero revenue and a recent TGE. This supports the recommendation in `Depin_Metric_Applicability_Revelations.md` §4–5 for an explicit applicability framework and a "don't grade on N/A" rule in the thesis methodology.

---

*Generated from `output/md/Depin_Metric_Applicability_Revelations.md` and `sections/empirical_analysis.tex`.*
