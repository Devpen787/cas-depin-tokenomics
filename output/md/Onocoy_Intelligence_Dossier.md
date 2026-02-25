# Onocoy Intelligence Dossier

**Compiled from DePIN Tokenomics Thesis Research**

---

## 1. Executive Summary

Onocoy is a decentralized GNSS (Global Navigation Satellite System) correction network based on Real-Time Kinematic (RTK) positioning. It serves as the primary empirical case study for this thesis on DePIN tokenomic stress evaluation. The network uses a capped-supply token model (ONO) with Data Credits for service consumption, built on Solana.

### 1b. Key People

- **Mark C. Ballandies:** Onocoy co-founder, CTO. Author of chain selection analysis (March 2023); DePIN taxonomy research (Ballandies et al. 2023).
- **Daniel Ammann:** Founder, President of Onocoy Association. DePIN Podcast interviewee (T6); articulated Solana choice, per-second billing, GPS off-chain, 100k-station vision.
- **Prof. Li-Ta Hsu:** GNSS/RTK expert. Onocoy content on decentralised navigation future.

### 1c. Timeline & Milestones

- **2022:** Onocoy built; chain selection (Solana) before Peaq maturity.
- **Mar 2023:** Ballandies chain selection article published.
- **Apr 2023:** Helium migrated to Solana (HIP-70).
- **Jul 2024:** Manual claim transition; purged zombie nodes.
- **2025:** TGE; Streak Appreciation bonus introduced; HVA (High Value Area) activated.
- **2025:** Whitepaper 3.0.1; target: 100k-station network.

---

## 2. System Overview

**Technology:** RTK combines reference-station correction streams with rover-side measurements to reduce positioning error from meter-scale to centimeter-scale. Use cases include surveying, precision agriculture, robotics, and industrial automation.

**Architecture:** Geographically distributed reference stations operated by independent participants, connected through a common protocol layer. No single centralized infrastructure operator. Stations provide correction data aggregated and distributed through a protocol-mediated coordination layer.

**DePIN as Cyber-Physical System:** Onocoy is defined not merely as a cryptocurrency project but as a CPS. Physical hardware (GNSS reference stations) and digital state (token incentives) operate in dynamic feedback loops. The token functions as a Purpose-Driven Token (Voshmgir), a steering signal designed to coordinate collective action that traditional market mechanisms fail to bootstrap efficiently.

---

## 3. Network Participants

**Reference-station operators (miners):** Responsible for deploying compatible GNSS hardware, maintaining continuous uptime, maintaining calibration quality, and providing stable connectivity. Station operation is not purely passive: installation quality, calibration, and maintenance discipline affect delivered correction quality. Failure to maintain uptime or quality can reduce service reliability and affect reward eligibility.

**Data users (rover-side consumers):** Purchase correction access for high-accuracy positioning workflows. Demand is primarily professional and enterprise-oriented, linked to operational workflows and continuity requirements rather than speculative token narratives. Service continuity and measurement quality are operational requirements, not optional features.

**Stress-relevant interaction:** Onocoy's central stress-relevant interaction is between relatively stable industrial demand and potentially unstable token-market dynamics. Despite utility-demand anchoring, Onocoy remains exposed to broader crypto-market cycles; token volatility can influence provider-side incentives and retention behaviour. This interaction is the key bridge to stress-model parameterisation.

---

## 4. Tokenomic Mechanics

**Dual-layer design:**

- **ONO:** Transferable utility/governance token for incentives and governance.
- **Data Credits:** Non-transferable utility credits purchased with fiat, consumed and burned during service usage.

**Supply:** Capped ONO supply with deflationary release profile (16% annual deflation factor, equivalent to four-year halving). Buyback-and-burn tied to protocol-level revenue routing.

**Data Credits design intent:** This architecture attempts to separate user-side payment flows from direct exposure to secondary-market token volatility. Users purchase Data Credits for service usage; credits are consumed on use.

> **Note:** Staking/collateral rules for miner participation are not fully specified in public documentation. For this thesis, staking/collateral is treated as an unknown mechanism fact and is only admissible through explicit modelled assumptions where parameter bounds are declared.

### 4b. Technical Details

**Location Scale:** Reward factor (0--1) based on station placement. Penalty if >3 stations in 15--50 km radius; inner 15 km = full penalty, outer 50 km = quadratic decay. Designed to steer geographic dispersion and redundancy (up to 3 stations per area optimal).

**AI spoofing detection:** Research direction (Onocoy transcript); community reference networks.

**Bonus programs:** Streak Appreciation (+50% for 125 days uptime; miss a day = streak halved); HVA (High Value Area) multiplier for targeted zones (ports, cities). Availability scale: min 80% uptime required; exponential scaling to 100%.

**Governance:** Swiss Association (legal wrapper, B2B fiat) + On-Chain DAO (Realms). Square-Root Voting to mitigate whale dominance. Token holders vote on protocol parameters (e.g. 16% decay rate, HVA definitions).

---

## 5. Blockchain Architecture & Solana Selection

Onocoy chose Solana based on a formal chain selection analysis by co-founder Mark C. Ballandies (March 2023). 35 chains were evaluated; Solana was selected among the top 3 (Algorand, Polygon, Solana).

| Metric | Solana | Nearest Alternative |
|:-------|:------:|:-------------------:|
| Avg. tx cost | $0.00017 | ~$0.01 (59x more) |
| Daily cost at scale (2M users + 100k miners) | $364/day | $21,609/day |
| Gas spike worst-case | ~$364/day | >$1M/day |
| Theoretical TPS | 65,000 | --- |
| Onocoy TPS requirement | 22 TPS | --- |

**7 reasons Solana was chosen:** Throughput, cost, block time (0.4s), developer base, DePIN ecosystem (Helium migrated there), scalability roadmap, Rust/C for GNSS engineers.

Helium's migration from its own L1 to Solana (April 2023, HIP-70) validated the decision: maintaining a sovereign L1 diverts engineering from the DePIN product. HIP-70 states: "It is important for developers to focus on the most important thing: enabling building of data networks" rather than maintaining a chain.

**Ballandies documented risk analysis:** Funding risk (FTX fallout), Technology risk (outages), Centralisation risk (Nakamoto Coefficient = 32 at time of analysis).

**T6 transcript (Daniel Ammann, DePIN Podcast):** Primary-source claims: Onocoy chose Solana because Helium migrated there; Solana is a hotspot for DePIN projects; decision made before Peaq/app-chains existed; low tx cost enables per-second microtransactions; GPS data kept off-chain due to latency; on-chain = economic settlement only.

**Token velocity relevance:** Velocity in on-chain token economies follows a power-law distribution (alpha approx 2): as few as five addresses can account for over half of total transfer velocity. Gas-cost friction is disproportionately destructive to high-frequency microtransaction models (DeCollibus 2025).

### 5b. Why Not App-Chains (Peaq, IoTeX)?

Peaq and IoTeX are described as coordination-layer infrastructure, not battle-tested settlement layers for high-revenue DePIN applications. When Onocoy built in 2022, Peaq was pre-revenue infrastructure while Solana had a live DePIN ecosystem (Helium). The Messari 2026 data retroactively validates the bet.

| Metric | Peaq | Solana (Ballandies 2023) |
|:-------|:----:|:-----------------------:|
| TPS (current) | 10,000+ | 4,000 observed |
| Avg. tx cost | ~$0.00025 | $0.00017 |
| Nakamoto Coefficient | >130 | 32 |

**Solana DePIN ecosystem (2025 live data, Praptii):** Helium 176k+ mobile subscribers, 69k active nodes, $2.3M/month on-chain revenue; Render 3.8k+ GPU nodes, 121M+ RNDR burned; Hivemapper 77k nodes, 20M+ km mapped, clients Lyft/Trimble/TomTom. Total DePIN on-chain revenue ~$55M annualised 2025, forecast $100M+ 2026.

---

## 6. Competitive Landscape

**Geodnet:** Direct GNSS/RTK competitor. $5.1M annualised revenue (Messari 2026). Uses Location NFTs to manage density. Geodnet and Onocoy compete for the same rooftop real estate and installers.

**Geodnet yield sensitivity:** Focuses on stable B2B revenue and Location NFTs to limit supply in saturated areas, enforcing meritocracy that protects individual miner yield. When GEOD prices rallied or burns increased due to enterprise contracts, it attracted professional surveyors who prioritise stable fiat-equivalent income over speculative tokens.

**Risk --- Elastic Provider Exit:** Multi-mining (Geodnet + Onocoy on similar hardware) is possible but introduces complexity. Providers may exhibit short-horizon allocation behaviour. If Onocoy's rewards lag significantly behind Geodnet's for prolonged periods, dual-mining setups may convert to single-mining for the competitor to optimise bandwidth or hardware stability.

**Triple Mining:** Geodnet, Onocoy, and RTKDirect can run on similar hardware (SimeonOnSecurity 2025). As GNSS hardware becomes more generalised, switching costs decrease, increasing vampire-attack risk.

**Archetype placement:** Onocoy is categorised as Archetype A (Commodity Sensor Networks: Low OpEx, Moderate CapEx) alongside Helium and Geodnet.

### ONO vs GEOD at a Glance

| Dimension | Onocoy (ONO) | Geodnet (GEOD) |
|:----------|:-------------|:---------------|
| Model | Capped supply + deflationary | BME / burn-linked |
| Revenue (2025) | Early stage | $5.1M annualised |
| Density control | Location Scale (penalty >3) | Location NFTs |
| Chain | Solana | Bridge to Solana |

### 6b. Stress Factors (Theoretical Framework)

**Subsidy Gap (Reward Addiction):** Structural deficit between provider OpEx+CapEx and fiat revenue. Token price decline widens this gap.

**Speculative Fragility:** Correlation between provider retention and token price volatility. Measured by Beta of node counts vs price drawdown.

**Competitive Yield Pressure:** Elasticity of provider participation when alternatives offer higher returns for similar hardware.

**Sunk Cost Moats:** Hardware acts as a staked asset. Economic Friction (financial loss on exit due to illiquidity of hardware) often more effective than on-chain staking during liquidity crises. Helium hotspots ($500 sunk cost) did not collapse proportionally during 95% price drop; GNSS antennas require precise placement.

### 6c. Standardised Metrics for Comparison

| Category | Metric | Definition |
|:---------|:-------|:-----------|
| Incentive Solvency | Burn-to-Mint Ratio | Burn/Mint. Below 1 = subsidy dependence. Onocoy expected below unity in early phases. |
| Provider Retention | 30-Day Node Retention | % nodes active at T+30 vs baseline under stress window. |
| Economic Efficiency | Revenue per Node | Total revenue / active nodes. Indicates viability without speculative rewards. |
| Speculative Velocity | Token Turnover | Daily volume / circulating market cap. |
| Valuation Risk | FDV / Annualised Revenue | Speculative premium. |

**Implication from Helium (2022--2023 crypto winter):** Existing GNSS stations may exhibit higher persistence during price drawdowns due to installation friction; new station growth may slow. Latent Capacity Degradation: providers stop maintaining hardware; high node count but falling quality/uptime.

---

## 7. Mechanism Design: Onocoy vs BME

Onocoy uses capped supply with deflationary elements (buyback and burn from revenue), not pure Burn-and-Mint Equilibrium (BME) where minting is unlimited.

**Assessment:** Capped supply is theoretically less exposed to hyperinflationary dilution loops than pure BME. However, it is less flexible in subsidising early growth if token price is too high (scarcity constrains adoption) or too low (insufficient reward budget to attract miners).

Onocoy's mechanism relies on outcome-based rewards (verified data) rather than action-based rewards (Lisa JY Tan taxonomy, Economics Design).

**Value capture funnel:** Fiat/User Payment → Protocol Settlement Layer → Token Sink or Buy Pressure → Net Supply Pressure. Onocoy uses fiat-front-end with tokenised backend settlement and burn-linked sinks.

**Vulnerability classes:** Reward--Demand Decoupling (emissions persist while demand weakens); Accrual Ambiguity (weak sink transparency); Demand-Regime Mismatch (architecture calibrated for one demand type fails under another).

### 7b. DTSE (DePIN Tokenomic Stress Evaluator) and Onocoy

DTSE treats Onocoy as a cyber-physical system, representing feedback between protocol incentive rules, provider participation decisions, and service capacity under exogenous stress regimes.

**Onocoy-specific interpretive signals:** (i) usage-linked sinks/credits → burn-linked measures; (ii) reward rules → emissions; (iii) eligibility/verification → participation thresholds. Two evaluation dimensions carried into DTSE: reward--demand coupling strength and provider-participation sensitivity under switching pressure.

Historical event studies cannot evaluate unobserved thresholds under controlled counterfactual stress for a novel capped-supply model like Onocoy. DTSE fills this gap as an evaluative instrument, not a forecasting tool.

---

## 8. Operational Failure Modes (Diagnostic Matrix)

**Reward--Demand Decoupling:** Emissions persist at high rate while usage flatlines. If GNSS stations deploy faster than RTK data buyers onboard, ONO rewards dilute rapidly.

**Liquidity-Driven Incentive Compression:** External market sell-offs reduce fiat value of fixed token rewards, pushing provider ROI below break-even. GNSS stations (low OpEx) less sensitive than GPU networks but more than passive staking.

**Latent Capacity Degradation:** Providers stop maintaining hardware due to low rewards. High Active Node count but falling Quality/Uptime. RTK requires precise calibration; neglect degrades network accuracy.

**Elastic Provider Exit:** Capital moves instantly to competitor (e.g. Geodnet) offering higher yield for compatible hardware.

**Dilution Feedback Loop:** Price decline → lower yield → miner churn → lower security → lower demand → further price decline.

### 8b. Risks & Known Unknowns

**Documented risks (Ballandies):** Funding risk (FTX fallout); Technology risk (outages); Centralisation risk (Nakamoto Coefficient = 32).

**Known unknowns:** Staking/collateral rules for miner participation; exact ONO supply cap (docs reference it but thesis did not extract); verification/eligibility details for participation thresholds.

**Practitioner insights (interview-derived):** Provider payback expectations, churn drivers, internal demand indicators treated as calibration ranges for modelling, not empirical facts.

### 8c. Lessons from Other DePINs

**Hivemapper:** Pivoted to B2B enterprise deals (Map Credits) to burn tokens; introduced Honey Bursts (targeted bonuses) for incentive re-targeting. Profitability-induced churn when HONEY price dipped.

**Helium:** Sub-DAOs (IOT, MOBILE) to compartmentalise risk; migration to Solana; sunk cost moat ($500 hotspots) buffered retention during 95% price drop.

**Render:** 121M+ RNDR burned for compute; BME model with usage-linked burns.

---

## 9. Key Sources

- **Onocoy Whitepaper 3.0.1:** <https://onocoy.com>
- **ONO Token Guide:** <https://onocoy.com/blog/your-guide-to-understanding-the-ono-token>
- **Mining Rewards Breakdown:** <https://docs.onocoy.com/documentation/mining-rewards-breakdown>
- **Bonus Programs:** <https://docs.onocoy.com/documentation/bonus-programs>
- **Ballandies 2023 --- Chain Selection:** <https://medium.com/wihi-weather/chain-selection-for-a-decentralized-physical-infrastructure-network-depin-bf1c646d9330> (Primary: Onocoy co-founder)
- **Helium HIP-70:** <https://github.com/helium/HIP/blob/main/0070-scaling-helium.md>
- **Messari 2026 Crypto Theses:** DePIN ecosystem data; Geodnet $5.1M; Helium Mobile $21M; Peaq/IoTeX as alternatives
- **Triple Mining (SimeonOnSecurity 2025):** Geodnet, Onocoy, RTKDirect --- dev.to/simeononsecurity
- **DeCollibus 2025:** Token velocity power-law; gas-cost friction for microtransactions

### 9b. Quick Links

| Resource | URL |
|:---------|:----|
| Main | <https://onocoy.com> |
| Docs | <https://docs.onocoy.com> |
| Blog / Token Guide | <https://onocoy.com/blog/your-guide-to-understanding-the-ono-token> |
| Mining Rewards | <https://docs.onocoy.com/documentation/mining-rewards-breakdown> |
| Location Scale | <https://docs.onocoy.com/documentation/mining-rewards-breakdown/location-scale> |
| Bonus Programs | <https://docs.onocoy.com/documentation/bonus-programs> |

---

## 10. Transcript Evidence (Secondary)

- **Why Onocoy Is My #1 DePIN Pick for 2025** (Nordic Crypto, third\_party): Narrative/context; verify quantitative claims with primary sources.
- **AI-Driven GNSS Spoofing Detection** (Onocoy, official): Spoofing/ML research direction statements.
- **$ONO Tokenomics Explained** (Onocoy, official): Token model claims (cap, burn, release schedule) --- verify with docs/on-chain.
- **Prof. Li-Ta Hsu on GNSS, RTK, Decentralized Navigation** (Onocoy, official): Market/use-case framing, not hard KPI evidence.
- **Location Scale and Rewards** (Onocoy, official): High value: reward formula assumptions and variable definitions.
- **Building a 100k-Station Network | Daniel Ammann** (DePIN Podcast, interview): T6 transcript --- Solana choice, per-second billing, GPS off-chain. Confirm numeric claims independently.
- **Onocoy TGE & The Horizontal Play** (Gold Hawks, interview): TGE timing/conversion --- time-sensitive; needs primary confirmation.

> Transcripts are secondary evidence. Verify quantitative claims with primary sources (whitepaper, docs, on-chain).

### 10b. Methodology Note

This dossier draws from event-study methodology (MacKinlay 1997): historical stress events (FTX collapse, Helium migration, Hivemapper restructuring) as distinct events to quantify abnormal churn. DTSE scope: comparative evaluation under controlled stress; does not forecast prices or model governance interventions.

---

*Onocoy Intelligence Dossier v1.1 | Generated from DePIN Tokenomics Thesis (cas-depin-tokenomics)*
*Build: `scripts/build_onocoy_intelligence_dossier.py`*
