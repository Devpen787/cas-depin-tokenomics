## V2 Metric Chapter Allocation

Status: synthesis control document  
Date captured: 2026-03-01  
Mode: `MODE: SYNTHESIS`

### Purpose

This document maps the Option B metric tiers to the chapters where they belong.

It answers five questions:

1. Which metrics belong in each chapter?
2. Which metrics should remain vocabulary only?
3. Which metrics are safe for results?
4. Which metrics should remain bounded context?
5. Which metrics belong in the appendix instead of the main narrative?

---

## Chapter 1: Introduction and Research Contract

### Use

- no formal metric system yet
- only the thesis robustness lens:
  - provider retention
  - service continuity
  - incentive-usage alignment

### Why

Chapter 1 should frame the problem, not start scoring systems or reporting proxies.

---

## Chapter 2: Foundations - DePIN as a Cyber-Physical System

### Use lightly

- provider retention
- service continuity
- incentive-usage alignment

### Keep out

- formal BMR discussion
- velocity proxy
- valuation ratios
- results-style metric language

### Why

Chapter 2 explains why these dimensions matter conceptually before they become formal evaluative metrics.

---

## Chapter 3: Comparative Tokenomic Framework

### Tier 1 metrics as vocabulary

- Burn-to-Mint Ratio
- Net Emissions
- reward / verification logic
- sinks / value-accrual pathways

### Tier 2 metrics as bounded context

- token turnover / speculative velocity
- FDV / annualized revenue
- active node count

### Best use

- define evaluative language
- show how mechanism families differ
- keep dated market context descriptive and time-stamped

### Avoid

- reporting these as results
- treating scene-setting market metrics as core evidence

---

## Chapter 4: Onocoy as the Anchor Case

### Best-fit metrics

- circulating supply
- validated / online station counts
- holder count
- total buybacks
- total burned
- dated price / market cap / FDV only as bounded snapshot context

### Use carefully

- payback period
- demand concentration
- revenue hints

These should stay bounded unless strongly supported by public docs or clearly labeled interview context.

### Why

Chapter 4 is a mechanism and case-description chapter, not a performance-score chapter.

---

## Chapter 5: Empirical Stress Layer

### Tier 1 emphasis

- provider retention
- provider churn
- adapted Burn-to-Mint logic where observable
- stress-signature framing

### Tier 2 selective use

- token turnover / speculative velocity
- FDV / annualized revenue
- revenue per node
- active node count

### Operating rule

Use the `N/R` principle aggressively.

If a metric is not reliably observable for the historical window, do not force it into inference.

### Why

This chapter is where observability discipline matters most.

---

## Chapter 6: DTSE Methodology

### Formal metric contract belongs here

Core metrics to define explicitly:
- Burn-to-Mint Ratio
- Net Emissions
- Velocity Proxy
- Provider Retention
- Provider Churn
- Average Provider Profitability
- Capacity Utilization
- Demand Satisfaction
- Volatility Proxy
- Incentive Efficiency
- First-Signal Timing
- Failure-Signature Logic

### Secondary / demoted metrics

- Death Spiral Probability should remain secondary if retained at all.

### Why

This chapter must make the evaluator transparent and defensible.

---

## Chapter 7: Results

### Main reporting spine

Use Tier 1 metrics as the core results language:
- Burn-to-Mint Ratio
- Net Emissions
- Provider Profitability
- Provider Churn / Retention
- Capacity Utilization
- Demand Satisfaction
- Volatility Proxy
- First-Signal Timing
- Failure-Signature Logic

### Use Tier 2 only when it clarifies

- token turnover
- valuation context
- revenue per node

### Avoid

- turning Tier 2 context into the main story
- relying on Tier 3 metrics for the headline result

---

## Chapter 8: Discussion / Conclusion

### Use

- interpret Tier 1 results
- selectively reference Tier 2 context where it sharpens the implication

### Avoid

- introducing new metrics
- reopening weak or optional metrics
- centering Tier 3 metrics in the thesis payoff

---

## Appendix

### Best appendix candidates

- full comparator market-context table
- demand-regime table
- utility / speculation classification table
- monetization-supporting tables
- Dune snapshot tables
- optional Tier 3 rationale note if needed

### Why

The appendix can preserve richness without forcing fragile metrics into the main-body argument.

---

## Summary Table

| Metric / Metric Family | Tier | Best Chapter Home | Role |
|---|---|---|---|
| Burn-to-Mint Ratio | Tier 1 | Ch. 6 / Ch. 7 | Core evaluative metric |
| Net Emissions | Tier 1 | Ch. 6 / Ch. 7 | Core evaluative metric |
| Provider Retention / Churn | Tier 1 | Ch. 5 / Ch. 6 / Ch. 7 | Core evaluative metric |
| Average Provider Profitability | Tier 1 | Ch. 6 / Ch. 7 | Core evaluative metric |
| Capacity Utilization / Demand Satisfaction | Tier 1 | Ch. 5 / Ch. 6 / Ch. 7 | Core evaluative metric |
| Volatility Proxy | Tier 1 | Ch. 6 / Ch. 7 | Core evaluative metric |
| First-Signal Timing / Failure Signatures | Tier 1 | Ch. 6 / Ch. 7 / Ch. 8 | Core evaluative metric |
| Revenue per Node | Tier 2 | Ch. 5 / Appendix | Bounded support |
| Token Turnover / Speculative Velocity | Tier 2 | Ch. 5 / Ch. 7 / Appendix | Bounded support |
| FDV / Annualized Revenue | Tier 2 | Ch. 3 / Ch. 4 / Appendix | Dated valuation context |
| Active Node Count / Station Counts | Tier 2 | Ch. 4 / Ch. 5 / Appendix | Descriptive support |
| Hardware Capacity | Tier 2 | Ch. 5 / Appendix | Bounded support |
| CAC / Cost Advantage / Take-Rate / SLA / Payback | Tier 3 | Appendix / bounded context only | Optional or fragile |
| Death Spiral Probability | Tier 3 | Ch. 6 / Appendix if retained | Secondary composite only |

### Final Rule

If a metric is useful but hard to defend, it should move down a tier rather than be forced into the thesis core.

That is the governing Option B principle.
