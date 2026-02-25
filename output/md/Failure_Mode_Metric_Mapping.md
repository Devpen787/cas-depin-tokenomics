# Failure Mode → Metric Mapping

**Source:** `sections/empirical_analysis.tex` (§4.5 DePIN Failure Modes), `output/md/Depin_Metric_Applicability_Revelations.md`
**Date:** 2026-02-25

---

## Mapping Table

| Failure Mode | Primary Metric(s) | Secondary Metric(s) | Rationale |
|:-------------|:-------------------|:---------------------|:----------|
| **Reward–Demand Decoupling** | Burn-to-Mint Ratio | Revenue per Node; FDV / Annualised Revenue | A declining Burn-to-Mint ratio is the direct signal: emissions continue while usage-driven burns weaken. Revenue per Node confirms whether individual providers are receiving economically meaningful demand-side income. FDV/Revenue contextualises how much speculative premium is propping up valuation relative to actual usage — a high ratio amplifies decoupling risk. |
| **Liquidity-Driven Incentive Compression** | Token Turnover | 30-Day Node Retention; Burn-to-Mint Ratio | Spiking Token Turnover during a price drawdown signals mercenary-capital exit rather than utility-driven circulation — the hallmark of liquidity-driven compression. 30-Day Retention captures the lagged downstream effect: providers exit after reward value collapses in fiat terms. Burn-to-Mint deteriorates secondarily as the fiat value of burns shrinks while nominal emissions persist. |
| **Latent Capacity Degradation** | 30-Day Node Retention | Revenue per Node; Burn-to-Mint Ratio | Retention that appears stable while quality/uptime scores decline is the defining signature. Revenue per Node provides the economic context: when per-node income falls below maintenance thresholds, providers remain online but stop calibrating or servicing hardware. A simultaneously declining Burn-to-Mint ratio confirms that demand-side activity is weakening even though node counts hold steady. |
| **Elastic Provider Exit** | 30-Day Node Retention | Token Turnover; Revenue per Node | Elevated churn (falling retention) without a corresponding price crash or demand shock is the primary signal — providers are leaving for better yield elsewhere. Token Turnover may spike if exiting providers sell accumulated rewards simultaneously. Revenue per Node on the competitor network, compared to the home network, quantifies the yield gap driving exit. |
| **Dilution Feedback Loop** | Burn-to-Mint Ratio; 30-Day Node Retention | Token Turnover; FDV / Annualised Revenue | This is a compound failure: it requires simultaneous deterioration across multiple metrics. A falling Burn-to-Mint ratio (emissions outpacing burns) combined with falling retention (providers exiting) are both primary — the loop requires both legs. Token Turnover spikes confirm sell-pressure acceleration. FDV/Revenue blowing out confirms the speculative premium has decoupled from fundamentals, completing the reflexive cycle. |

---

## Metric Coverage Summary

How many failure modes each metric serves as a signal for:

| Metric | Primary signal for | Secondary signal for | Total |
|:-------|:------------------:|:--------------------:|:-----:|
| Burn-to-Mint Ratio | 2 | 3 | 5 |
| 30-Day Node Retention | 2 | 1 | 3 |
| Token Turnover | 1 | 2 | 3 |
| Revenue per Node | 0 | 3 | 3 |
| FDV / Annualised Revenue | 0 | 2 | 2 |

**Key observation:** Burn-to-Mint Ratio is the single most diagnostic metric — it participates in all five failure modes (twice as primary). 30-Day Node Retention is the primary behavioural signal for infrastructure-layer failures (Latent Degradation, Elastic Exit). Revenue per Node and FDV/Revenue serve exclusively as secondary contextual indicators — they confirm severity but do not trigger detection on their own.

---

## Onocoy Applicability Note

Per the `Metric_Relevance_Matrix.md`, three of the five metrics (Revenue per Node, Token Turnover, FDV/Revenue) are currently **N/A** for early-stage Onocoy. This means:

- **Reward–Demand Decoupling** can be detected via the adapted Burn-to-Mint ratio but lacks secondary confirmation from revenue metrics.
- **Liquidity-Driven Incentive Compression** cannot be reliably detected until ONO has sustained trading volume (Token Turnover is N/A post-TGE).
- **Latent Capacity Degradation** is detectable via retention data alone, but without Revenue per Node the economic trigger is invisible.
- **Elastic Provider Exit** is detectable via retention, making it the most observable failure mode for Onocoy today.
- **Dilution Feedback Loop** requires multiple metrics to fire simultaneously — with 3 of 5 currently N/A, this compound failure mode is largely unmonitorable until Onocoy matures.

This reinforces the thesis gap identified in `Depin_Metric_Applicability_Revelations.md` §5: the framework should explicitly state which failure modes are monitorable for early-stage networks and which require deferred evaluation.

---

*Cross-references: `output/md/Metric_Relevance_Matrix.md`, `output/md/Depin_Metric_Applicability_Revelations.md` §8 (failure-mode → metric mapping gap).*
