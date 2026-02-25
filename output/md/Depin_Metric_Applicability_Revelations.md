# DePIN Metric Applicability Revelations

**Session date:** 2026-02-25  
**Context:** Discussion triggered by "Based on this DOC how does Onocoy rank against other DePINs?" (Onocoy Intelligence Dossier)  
**Purpose:** Capture findings and structural gaps identified for thesis revision and reference.

---

## 1. Onocoy Ranking Against Other DePINs

### Direct GNSS/RTK Competitor: Geodnet

| Dimension | Onocoy (ONO) | Geodnet (GEOD) |
|-----------|--------------|----------------|
| Revenue (2025) | Early stage | $5.1M annualised |
| Model | Capped supply + deflationary | BME / burn-linked |
| Density control | Location Scale (penalty >3) | Location NFTs |
| Chain | Native Solana | Bridge to Solana |

Geodnet leads on revenue and traction. Onocoy is early stage.

### Broader Solana DePIN Ecosystem (2025)

| DePIN | Scale | Revenue / Activity |
|-------|------|--------------------|
| Helium | 176k+ mobile subscribers, 69k active nodes | $2.3M/month on-chain |
| Render | 3.8k+ GPU nodes | 121M+ RNDR burned |
| Hivemapper | 77k nodes | 20M+ km mapped; clients Lyft, Trimble, TomTom |
| Geodnet | — | $5.1M annualised |
| Onocoy | Target 100k stations | Early stage |

### Archetype Placement

Onocoy is **Archetype A** (Commodity Sensor Networks: Low OpEx, Moderate CapEx) alongside Helium and Geodnet.

### Bottom Line

Onocoy ranks as early-stage relative to Geodnet and other Solana DePINs. Strengths: architecture and tokenomics design. Weakness: revenue and traction lag.

---

## 2. Tokenomics and Stress Endurance

### Current Tokenomics

- **Design:** Capped supply, deflationary (16% annual decay), buyback-and-burn, Data Credits (fiat-purchased, consumed and burned).
- **Strengths:** Capped supply reduces hyperinflation risk vs pure BME; outcome-based rewards; fiat front-end with burn-linked sinks.
- **Weaknesses:** Less flexibility to subsidise early growth; Burn-to-Mint expected below 1 in early phases (subsidy dependence); staking/collateral rules not fully specified.

### Stress Endurance Summary

| Stress Factor | Onocoy Exposure |
|---------------|-----------------|
| Subsidy gap | High |
| Speculative fragility | Moderate |
| Competitive yield pressure | High |
| Sunk cost moat | Moderate–strong |
| Liquidity-driven compression | Moderate |

### Operational Failure Modes

1. Reward–demand decoupling  
2. Latent capacity degradation  
3. Elastic provider exit  
4. Dilution feedback loop  

---

## 3. Framework Calibration: Generic DePIN vs RTK/GNSS

### What the Thesis Uses

- **Archetypes by hardware cost** (OpEx/CapEx), not by vertical (GNSS vs IoT vs compute).
- **Standardised metrics** (Burn-to-Mint, 30-Day Retention, Revenue per Node, Token Turnover, FDV/Revenue) applied across all DePINs.
- **RTK/GNSS** appears as context: Geodnet as competitor, triple mining, Location governance, B2B demand, sunk cost.

### What the Thesis Does NOT Model

- Calibration quality and maintenance discipline  
- Geographic dispersion requirements (15–50 km radius rules)  
- Installer and rooftop real-estate dynamics  
- Surveyor vs enterprise vs agriculture demand segments  
- RTK-specific quality metrics  

### Conclusion

The thesis evaluates Onocoy primarily with **generic DePIN stress metrics**, not a dedicated RTK/GNSS business model. It answers "how does this DePIN behave under stress?" rather than "how does this RTK/GNSS business perform vs its vertical peers?"

---

## 4. Not All Metrics Are Relevant to Onocoy

### Metric Relevance for Onocoy (Current State)

| Metric | Relevance | Why |
|--------|-----------|-----|
| Burn-to-Mint Ratio | Partially relevant | Onocoy uses capped supply, not BME. Analogue is Burn / Emissions from inventory. |
| 30-Day Node Retention | Relevant | Provider stickiness matters; early-stage data may be limited. |
| Revenue per Node | Weak today | Early stage, little revenue. Geodnet has $5.1M; Onocoy near zero. |
| Token Turnover | Weak today | Requires liquid secondary market. ONO TGE 2025; liquidity may be thin. |
| FDV / Annualised Revenue | Not useful yet | With near-zero revenue, ratio explodes or is undefined. |

### What Fits Onocoy Better

- Competitive yield pressure (Geodnet vs Onocoy)  
- Subsidy gap (OpEx + CapEx vs fiat revenue)  
- Elastic provider exit (triple mining)  
- Sunk cost / retention (installation and calibration friction)  

---

## 5. Does the Thesis Mention This?

**No.** The thesis does not explicitly state that not all metrics are equally relevant to Onocoy.

### What the Thesis Does Say

- BMR adaptation for capped supply (distribution from fixed inventory)  
- Early-stage BMR often below parity  
- Token velocity "used comparatively and interpreted cautiously"  

### What the Thesis Does NOT Say

- FDV/Revenue is meaningless for early-stage Onocoy  
- Revenue per Node is weak or undefined for early-stage  
- Token Turnover requires liquid markets and may not apply post-TGE  
- That not all metrics are equally relevant, or which are more/less applicable  

---

## 6. Proposed Explicit Structure (4+2 Steps)

### Core Steps

1. **Identify** DePIN tokenomic stress metrics for DePINs  
2. **Understand** how to apply these stress metrics and analysis  
3. **See** how they perform across DePINs—**only where relevant** (don't grade on inapplicable metrics)  
4. **See** which DePIN stress metrics are relevant for Onocoy  

### Additional Steps

5. **Stress-scenario mapping** — Which metrics matter under which stress regimes (liquidity vs competitive yield vs demand collapse)?  
6. **Data availability / computability** — Which metrics can be computed from public data vs require internal data?  

---

## 7. Gap Audit: What Exists vs Missing

| Step | Exists | Missing |
|------|--------|---------|
| 1. Identify metrics | Stress factors, standardised metrics table, DTSE metric set | Single "DePIN stress metrics catalog" with applicability conditions |
| 2. How to apply | Event-study methodology, comparative statics, DTSE scenario design, BMR adaptation | Explicit "application guide" (when to use which metric, preconditions) |
| 3. Perform where relevant | Archetype grouping, event-study application to Helium/Hivemapper/Render/Geodnet | Relevance matrix (metric × project); explicit "don't grade on N/A" rule |
| 4. Onocoy applicability | BMR adaptation, early-stage BMR, token velocity "cautiously" | Dedicated Onocoy applicability section; table of strong/weak/not applicable |

---

## 8. Additional Gaps Beyond the 4+2 Structure

| Gap | Why It Matters |
|-----|----------------|
| **Failure-mode → metric mapping** | Which metrics signal which failure modes? (e.g. Reward–demand decoupling → BMR; Elastic provider exit → churn/retention) |
| **Mechanism-class applicability** | Which metrics assume which mechanism? BMR is BME-native; FDV/Revenue assumes revenue; Token Turnover assumes liquid markets. |
| **Temporal applicability** | When does a metric become meaningful? Early-stage vs mature. FDV/Revenue not useful until revenue exists. |
| **Interpretation boundaries** | Same metric value across mechanisms—different meaning? BMR = 0.5 for BME vs capped supply. |
| **Vertical vs horizontal comparison** | When to compare Onocoy to Geodnet (GNSS) vs Helium (Archetype A)? |
| **Conflicting signals** | What if BMR improves but retention worsens? Trade-off handling. |
| **Threshold vs directional use** | Pass/fail or directional? Thesis leans directional; not stated explicitly. |
| **Reproducibility / application guide** | How would another researcher apply this framework? Stepwise "how to apply" missing. |

---

## 9. Why Didn't We Think of This Before?

| Reason | Explanation |
|--------|--------------|
| **Focal case drove design** | Onocoy was the anchor; comparative framework was secondary. Applicability assumed rather than designed. |
| **Academic convention** | "Define metrics → apply → interpret" is standard; explicit "when does this apply?" is less common. |
| **Simulation-first framing** | DTSE focused on internal validity; external validity (do these metrics fit real networks?) was secondary. |
| **Distributed authorship** | Person A (foundations, Onocoy), Person B (framework), Person C (methodology, results). Each piece coherent; cross-cutting "applicability" had no owner. |
| **Generic framework assumption** | "Standardised for heterogeneous systems" implied broad applicability; limits not questioned until raised. |
| **Scope discipline** | Adding applicability framework felt like scope creep. |
| **Question emerged from use** | "Are all metrics relevant for Onocoy?" arose from applying the framework, not from initial design. |

---

## 10. Recommended Additions to Thesis

1. **Metric applicability framework** — When each metric applies; preconditions; mechanism-class mapping.  
2. **Relevance matrix** — Metric × project/archetype; explicit N/A where inapplicable.  
3. **"Don't grade on N/A" rule** — Stated explicitly in methodology.  
4. **Onocoy metric applicability section** — Dedicated subsection or table in empirical analysis or methodology.  
5. **Failure-mode → metric mapping** — Which metrics signal which failure modes.  
6. **Stress-scenario mapping** — Which metrics matter under which stress regimes.  

---

*Generated from conversation thread 2026-02-25. Reference: `output/md/Onocoy_Intelligence_Dossier.md` for source dossier.*
