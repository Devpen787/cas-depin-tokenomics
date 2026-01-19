::: titlepage
**DePIN Tokenomics Under Stress**

A Simulation-Based Sustainability Analysis Using the Onocoy Network as a
Case Study

**Author A**\
**Author B**\
**Author C**

CAS Blockchain\
Lucerne University of Applied Sciences and Arts (HSLU)

2026-01-20
:::

# Abstract {#abstract .unnumbered}

Decentralized Physical Infrastructure Networks (DePIN) rely on
token-based incentive systems to bootstrap and sustain real-world
infrastructure operated by independent providers. While tokenomics is
frequently discussed in terms of growth and market valuation,
significantly less attention has been paid to how these mechanisms
behave under adverse conditions such as demand shocks, liquidity events,
or deteriorating provider economics [@Messari2024]. This gap is
particularly consequential for DePIN systems, where infrastructure churn
can lead to irreversible losses in service capacity due to physical
deployment constraints.

This thesis evaluates the robustness of DePIN tokenomic mechanisms under
standardized stress conditions using a reproducible, simulation-based
framework. Rather than forecasting token prices or predicting network
success, the analysis focuses on comparative, directional behavior: how
different incentive structures respond when subjected to adverse
scenarios [@Morris2019]. An agent-based simulation model is employed to
represent heterogeneous infrastructure providers interacting with a
rule-based protocol under exogenous demand and macroeconomic regimes
[@Braakman2022].

The framework is applied to the Onocoy network and its ONO token as a
primary case study. Results are interpreted as conditional insights into
mechanism resilience, not as claims of causal certainty or real-world
prediction. The contribution of this work lies in demonstrating how
stress-testing can be systematically applied to DePIN tokenomics,
offering a tool for researchers and builders to evaluate incentive
robustness before failure occurs.

# Introduction {#sec:introduction}

## Motivation

Decentralized Physical Infrastructure Networks (DePIN) represent an
emerging class of blockchain-enabled systems that coordinate the
deployment and operation of real-world infrastructure through
cryptographic incentives [@Messari2024]. Unlike purely digital
protocols, DePIN networks depend on physical assets, such as sensors,
antennas, or positioning stations, that require upfront capital
expenditure, ongoing operational costs, and geographic placement. These
characteristics fundamentally alter the economic and risk profile of the
network [@BrouwerBurg2016].

In such systems, tokenomics is not merely a mechanism for value transfer
or speculative participation; it is the primary coordination tool
through which infrastructure is deployed, maintained, and retained. When
incentive structures fail under adverse conditions, providers may exit
the network, leading to degraded service quality and potentially
permanent loss of coverage. Unlike software-based protocols, where
participation can be restored with minimal friction, the reinstallation
of physical infrastructure involves logistical delays, sunk costs, and
regulatory constraints.

Despite this fragility, most discussions of DePIN tokenomics focus on
growth-phase dynamics or long-term valuation narratives. Few researchers
examine how these systems behave under stress, precisely the conditions
that determine long-term viability.

## Problem Statement

Most rigorous tokenomic evaluations assume average conditions---stable
demand and growing participation. This approach ignores the volatility
inherent to physical networks. Real-world networks operate in
environments characterized by volatility and uncertainty. DePIN networks
may face sudden drops in demand, adverse macroeconomic regimes,
liquidity shocks caused by token unlocks, or increased competition for
infrastructure operators [@Ho2022].

When such stresses occur, the incentive system must continue to perform
three essential functions: retain providers, sustain service capacity,
and prevent incentive collapse. Failure in any of these dimensions can
initiate feedback loops, such as provider churn reducing service
quality, that accelerate network degradation. Similar dynamics have been
observed in other incentive-driven systems, where poorly calibrated
mechanisms amplify shocks rather than absorb them [@Mardikes2025].

## Research Focus and Scope

This thesis focuses on the stress-testing of tokenomic mechanisms in
DePIN networks through simulation-based analysis. The objective is to
evaluate how different incentive structures behave under adverse
scenarios, rather than to predict future outcomes or token prices.

Several deliberate scope constraints are imposed. The thesis does not
attempt to forecast token prices or market capitalization, following
critiques of predictive overreach in crypto-asset valuation literature
[@CFA2018]. It does not claim causal certainty regarding real-world
network behavior. Nor does it propose novel tokenomic designs; instead,
existing mechanisms are evaluated through controlled experimentation.

The Onocoy network and its ONO token serve as the primary empirical
anchor. ONO is treated as a representative DePIN implementation with
clearly defined incentive mechanisms and observable infrastructure
constraints. While the analysis is grounded in this case, the modeling
framework is designed to be extensible to other DePIN systems.

## Contribution

This thesis makes three contributions: a structured simulation approach
for stress-testing DePIN tokenomics under adverse conditions, drawing on
established evaluation frameworks for complex systems modeling
[@Sollaci2004; @Morris2019]; the application of this framework to a
real-world DePIN case, translating conceptual incentive mechanisms into
testable model parameters; and an emphasis on comparative robustness and
trade-off analysis over prediction, offering a practical evaluation tool
for both researchers and protocol designers.

# DePIN Fundamentals {#sec:depin_fundamentals}

*\[INSTRUCTIONS FOR PERSON A: Define the core concepts here. Distinguish
DePIN from normal crypto.\]*

## Defining DePIN

- **Definition:** Define Decentralized Physical Infrastructure Networks.

- **Key Difference:** Contrast it with DeFi (purely digital/capital) vs
  DePIN (physical/labor/hardware).

## The Physical Constraint (Hardware)

- **Sunk Costs:** Explain that buying a \$1,000 miner is a sunk cost
  that creates \"stickiness\" (unlike staking tokens which can be unsold
  instantly).

- **Geographic Friction:** moving a miner is hard.

# Theoretical Definitions of Stress {#sec:theoretical_definitions}

*\[INSTRUCTIONS FOR PERSON A: This is critical. You must define the
\"Disease\" so Person C can test the \"Cure\". Use these exact
definitions.\]*

## Summary of Stress Factors

Table [1](#tab:stress_factors){reference-type="ref"
reference="tab:stress_factors"} summarizes the core theoretical
definitions of stress used throughout this thesis.

::: {#tab:stress_factors}
  ----------------------------------------------------------------
  **Concept**       **Definition**               **Risk Driver**
  ----------------- ---------------------------- -----------------
  **Reward          A state where maintaining    If incentives
  Addiction**       supply requires              flatten,
                    exponentially increasing     mercenary supply
                    token incentives.            churns
                                                 immediately.

  **The Subsidy     The delta between real       Early-stage gaps
  Gap**             operating costs (CapEx +     are bridged
                    OpEx) and real fiat revenue  entirely by
                    entering the system.         speculative token
                                                 value, creating
                                                 solvency risk.

  **Speculative     The correlation between      High fragility
  Fragility**       network security (provider   implies that
                    uptime) and token price      price drops
                    volatility.                  trigger immediate
                                                 hardware churn
                                                 ($>10\%$ drop
                                                 $\to >10\%$
                                                 churn).
  ----------------------------------------------------------------

  : Theoretical Definitions of Stress Factors
:::

## Positioning Within the Overall Research {#sec:positioning}

### Relationship to the Broader Research

This work forms part of a larger collaborative research effort examining
the sustainability of DePIN networks. Within that context, this thesis
occupies a clearly defined role: the evaluation of tokenomic mechanisms
through formal modeling and stress testing.

Foundational definitions of DePIN, hardware constraints, and empirical
observations of the Onocoy network are established elsewhere in the
broader research. Analytical descriptions of tokenomic design patterns
and market logic are likewise addressed in parallel work. This thesis
builds upon those components by translating conceptual mechanisms into a
formal simulation environment and evaluating their behavior under
stress, following best practices for simulation-based evaluation of
complex socio-technical systems [@Braakman2022].

### Unique Analytical Responsibility

The unique contribution of this thesis lies in the operationalization of
stress-testing. Conceptual definitions of stress are converted into
explicit model inputs, and tokenomic mechanisms are evaluated through
their simulated effects on provider retention, incentive solvency, and
service continuity. By grounding all claims in explicit assumptions,
transparent metrics, and reproducible experimental design, the thesis
aligns with established methodological standards for simulation-based
research [@Sartori2022].

# Theoretical Tokenomic Framework {#sec:theoretical_framework}

## Introduction {#introduction}

\[TODO: Define the scope of Tokenomics in DePIN. Key themes:
Sustainability, Mechanism Design, and the 'Physical' constraint.\]

## Comparative Scope: The Solana DePIN Ecosystem {#subsec:solana_scope}

This section analyzes the tokenomic design patterns of eight leading
DePIN protocols on Solana to establish a baseline for industry
standards.

### Project Archetypes

\[TODO: Analyze the following projects based on Hardware Sunk Cost vs.
Active Work:\]

1.  **Helium (IoT/Mobile):** The Burn-and-Mint Standard.

2.  **Hivemapper (Mapping):** Active labor constraints.

3.  **Render (Compute):** High-end GPU economics.

4.  **io.net (Aggregated Compute):** Cluster economics.

5.  **Geodnet (GNSS):** Location NFT and hex-based capping.

6.  **Grass (Bandwidth):** Zero-marginal cost participation.

7.  **Nosana (CI/CD):** Compute grid incentives.

8.  **Aleph.im (Storage/Compute):** Infrastructure persistence.

## Tokenomic Building Blocks {#subsec:building_blocks}

### Emission Schedules & Inflation

\[TODO: Compare 'Halving' models (Bitcoin style) vs. 'Linear Decay' vs.
'Dynamic Minting'.\]

### The Burn-and-Mint Equilibrium (BME)

\[TODO: Detailed definition of BME. How Dual-Token systems (Token + Data
Credits) separate volatility from utility cost.\]

### Work Verification Mechanisms

\[TODO: Define how 'Proof of Physical Work' is validated on-chain (e.g.,
Proof of Coverage, Proof of Mapping).\]

## Monetization and Demand Regimes {#subsec:demand_regimes}

### The Value Capture Funnel

\[TODO: Map the flow of Fiat -\> Buy Pressure -\> Burn -\> Supply
Reduction.\]

### Demand Cyclicality: Enterprise vs. Consumer

\[TODO: Contrast steady B2B demand (Geodnet) vs. cyclical consumer
demand (Helium).\]

## Detailed Analysis of the ONO Mechanism {#subsec:ono_mechanism}

\[TODO: Deep dive into Onocoy's specific 'Capped Supply' architecture
vs. the BME industry standard defined above.\]

## Conclusion

\[TODO: Summarize the theoretical vulnerabilities identified in these
models, setting the stage for the specific Empirical Stress Analysis in
Section 6.\]

# Empirical Case: Onocoy {#sec:onocoy_case}

*\[INSTRUCTIONS FOR PERSON A: Please fill this section with descriptive
facts. Do not analyze the token price or success yet. Focus on the
business and the hardware.\]*

## System Overview

- **GNSS & RTK Technology:** Explain what Real-Time Kinematics (RTK) is
  and why it improves GPS accuracy (centimeter-level precision).

- **The Physical Network:** Describe the density of stations required
  (e.g., 20km baseline) and why a distributed network makes sense versus
  a centralized one.

## Network Participants

- **Miners (Reference Stations):** Define the hardware requirements.
  Cost of entry? (e.g., \$1,000+). Install requirements? (Roof access,
  clear sky view).

- **Users (Rovers):** Who buys the data? (Surveyors, drones, agriculture
  machines). How do they access it? (NTRIP caster).

## Tokenomic Mechanics (Descriptive)

- **The ONO Token:** Describe the emission schedule (halving? decay?).

- **Burn/Sink Mechanism:** How does the system capture value? (e.g.,
  Data Credits or burn-and-mint).

- **Staking Rules:** Are there staking requirements for miners to
  participate?

# Empirical Stress Analysis {#sec:empirical_analysis}

## Introduction {#introduction-1}

Decentralized Physical Infrastructure Networks (DePIN) represent a
fundamental shift in the deployment and maintenance of critical
real-world infrastructure, leveraging cryptographic incentives to
coordinate distributed hardware provision across sectors ranging from
wireless connectivity to geospatial mapping [@FrontiersDePIN2025].
Unlike purely digital assets within the Decentralized Finance (DeFi)
ecosystem, DePIN protocols introduce a complex layer of physical
constraints---including hardware sunk costs, geographic friction, and
logistical latency---that fundamentally alters their economic risk
profile [@RapidInnovation2024]. Consequently, the sustainability of
these networks is not merely a function of code, but of the intricate
interplay between tokenomic mechanism design and the behavioral
economics of hardware operators under stress [@HackMD2025].

Historically, the evaluation of such systems has relied heavily on
Agent-Based Modeling (ABM) and stochastic simulations to forecast
network behavior [@RapidInnovation2024]. While valuable for exploring
theoretical bounds, simulations often operate on rational agent
assumptions that fail to capture the nuances of human panic, the
\"stickiness\" of physical deployments, or the unpredictability of
exogenous market shocks. There is a growing recognition within the
research community that empirical analysis---grounded in the historical
performance of live networks under actual stress---offers a more
rigorous and actionable methodology for assessing resilience
[@Coincub2025].

This section establishes a comprehensive methodology for comparative
DePIN analysis without the use of simulation. By operationalizing the
\"Event Study Methodology\" utilized in financial econometrics
[@Hacken2024], we construct a static stress-testing framework that
benchmarks the Onocoy network against the historical performance of
mature Solana-based DePIN peers, including Helium, Hivemapper, Render,
and Geodnet. This approach replaces probabilistic forecasting with
deterministic observation, analyzing how different incentive
structures---such as Burn-and-Mint Equilibrium (BME) versus Capped
Supply---have historically responded to demand contractions, liquidity
crises, and competitive yield pressures [@FrontiersDePIN2025].

The objective is to provide a diagnostic tool that is equally valuable
for the academic thesis and the broader DePIN community. By isolating
specific \"Failure Modes\" such as Reward-Demand Decoupling and Latent
Capacity Degradation [@RapidInnovation2024], and mapping them to
observable on-chain metrics, this report offers a nuanced framework for
evaluating whether a protocol's incentive mechanism can retain
providers, sustain service capacity, and prevent economic collapse in
the absence of speculative growth.

## Theoretical Framework: Operationalizing Stress Without Simulation

To effectively analyze DePIN robustness without the generative
capabilities of simulation, one must adopt a framework based on
Comparative Statics and Empirical Event Studies. This involves defining
\"stress\" not as a variable in a model, but as a specific set of
historical market conditions (regimes) and analyzing the elasticity of
network supply and demand in response to those conditions [@PMC2022].

### The \"Disease\": Defining Stress Factors in Physical Networks

In the context of this static analysis, stress factors are exogenous
shocks that challenge the economic viability of the network. We
categorize these stressors into three primary buckets that determine
long-term sustainability [@RapidInnovation2024]:

- **The Subsidy Gap (Reward Addiction):** This represents the structural
  deficit between the real operating costs (OpEx) plus capital
  expenditures (CapEx) of infrastructure providers and the actual fiat
  revenue entering the system. In early-stage networks, this gap is
  bridged by speculative token incentives. A critical stress point
  occurs when token prices decline, widening this gap and forcing
  providers to operate at a loss. Static analysis measures this by
  tracking the historical divergence between \"Real Yield\" (burn-based
  revenue) and \"Dilutive Yield\" (inflationary rewards) over time
  [@RapidInnovation2024].

- **Speculative Fragility:** This metric defines the correlation between
  network security (provider uptime/retention) and token price
  volatility. High fragility implies that a drop in token price triggers
  immediate and proportional infrastructure churn. In a non-simulated
  framework, this is measured by calculating the \"Beta\" of active node
  counts relative to the token's price drawdown during specific bear
  market windows (e.g., the 2022-2023 crypto winter)
  [@RapidInnovation2024].

- **Competitive Yield Pressure:** This refers to the elasticity of
  provider participation when alternative networks offer higher returns
  for similar hardware. As DePIN hardware becomes more generalized
  (e.g., GPUs for Render vs. io.net, or GNSS receivers for Geodnet vs.
  Onocoy), the switching costs decrease, increasing the risk of
  \"vampire attacks\" where supply migrates instantly to the highest
  bidder [@RapidInnovation2024].

### The \"Cure\": Mechanism Design as a Static Defense

If stress is the disease, the tokenomic mechanism is the immune system.
In a static analysis, we evaluate the architectural capacity of
different mechanisms to absorb shock. The primary designs observed in
the Solana DePIN ecosystem include:

- **Burn-and-Mint Equilibrium (BME):** Utilized by Helium and Render,
  this dual-token model requires users to burn the native token to
  create non-transferable data credits (fixed in fiat value). This
  theoretically caps supply based on demand [@RenderBME]. The static
  stress test involves calculating the \"Equilibrium Price\"---the token
  price at which the burn rate from usage exactly offsets the mint rate
  for provider rewards---and comparing it to the actual market price.

- **Capped Supply with Emissions Decay:** Employed by Onocoy (and
  Bitcoin), this model enforces scarcity via a hard cap and diminishing
  returns (halvings) [@OnocoyToken]. The stress test here focuses on the
  \"Security Budget Analysis\"---determining whether the diminishing
  block reward remains sufficient to cover aggregate provider OpEx in
  the absence of significant fee revenue.

- **Sunk Cost Moats:** A crucial differentiator for DePIN is that the
  hardware itself often acts as a \"staked\" asset. The analysis must
  quantify \"Economic Friction\"---the financial loss incurred by a
  provider who exits the network due to the illiquidity of the hardware.
  This sunk cost acts as a retention buffer, often more effective than
  on-chain staking during liquidity crises [@RapidInnovation2024].

### Methodology: Empirical Event Studies

To replace simulation, we utilize the Event Study Methodology, a
standard approach in financial econometrics used to measure the impact
of specific events on asset value and participant behavior
[@Hacken2024]. By treating historical market shocks---such as the FTX
collapse, Helium's migration to Solana, or Hivemapper's reward
restructuring---as distinct \"events,\" we can quantify the abnormal
churn or abnormal returns associated with these stressors.

This method allows us to infer the future behavior of a network like
Onocoy by benchmarking it against the past empirical behavior of
comparable networks under similar conditions. We look for \"Abnormal
Churn Rates\"---deviations from the expected baseline of provider
exits---following negative price shocks to determine the true
\"Elasticity of Provider Exit\" [@RapidInnovation2024].

## Comparative Scope: The Solana DePIN Ecosystem {#comparative-scope-the-solana-depin-ecosystem}

Solana has emerged as the dominant execution layer for DePIN due to its
high throughput, low transaction costs (\$0.00025), and state
compression capabilities, which allow for the cost-effective management
of millions of physical nodes [@Coincub2025]. To answer the thesis
questions regarding robustness, we establish a comparative set of key
projects representing different hardware profiles and stress responses.

### The Comparative Set

We categorize the projects into three distinct \"archetypes\" based on
their hardware cost profile and service model, as these factors dictate
their response to economic stress:

#### Archetype A: Commodity Sensor Networks (Low OpEx, Moderate CapEx)

- **Helium (IoT/Mobile):** The mature market leader with over 1 million
  hotspots. It serves as the primary case study for long-term retention
  behavior and the transition from L1 to Solana [@Coincub2025].

- **Geodnet:** A direct competitor to Onocoy in the GNSS/RTK sector.
  Focused heavily on stable B2B revenue and industrial utility,
  utilizing \"Location NFTs\" to manage density [@GeodnetIP7].

- **Onocoy:** The thesis subject. An emerging GNSS network with a
  distinct governance approach and capped token supply model
  [@RapidInnovation2024].

#### Archetype B: High-Performance Compute (High OpEx, High CapEx)

- **Render:** Decentralized GPU rendering focused on the creator
  economy. High electricity costs make these providers highly sensitive
  to token price drops, serving as a proxy for \"mercenary\" capital
  behavior [@NewtonRender].

- **io.net:** Aggregated GPU compute for AI/ML workloads. A newer
  entrant experiencing massive growth but untested in a prolonged bear
  market, dealing with potential supply shocks from \"cluster\"
  migration [@IoNet2025].

#### Archetype C: \"Proof of Physical Work\" (Active Labor)

- **Hivemapper:** Dashcam mapping. Unlike passive sensor networks, this
  requires active human labor (driving). Incentives must cover fuel and
  time, creating a higher churn risk during price downturns
  [@CoinMarketCapHM].

### Metric Standardization for Static Comparison

To compare these diverse networks without simulation, we standardize
specific metrics that serve as proxies for health and stress resilience
[@Coincub2025].

::: {#tab:comparative_metrics}
  ----------------------------------------------------------------
  **Category**   **Standardized    **Definition & Proxy Utility**
                 Metric**          
  -------------- ----------------- -------------------------------
  Incentive      Burn-to-Mint      The ratio of tokens burned
  Solvency       Ratio             (revenue) to tokens minted
                                   (incentives). A value $< 1$
                                   indicates subsidy dependence;
                                   $> 1$ indicates sustainable
                                   deflation [@Coincub2025].

  Provider       30-Day Node       Percentage of nodes active at
  Retention      Retention         $T+30$ days compared to $T0$,
                                   specifically analyzed following
                                   a token price drop of $>20\%$
                                   [@RapidInnovation2024].

  Economic       Revenue per Node  Total Network Revenue divided
  Efficiency                       by Total Active Nodes.
                                   Indicates whether the average
                                   provider is economically viable
                                   without speculative token
                                   rewards [@AlloraResearch].

  Speculative    Token Turnover    Daily Trading Volume divided by
  Velocity                         Circulating Market Cap. High
                                   turnover during price drops
                                   often signals \"mercenary
                                   capital\" exit rather than
                                   utility usage
                                   [@GateSquare2025].

  Valuation Risk FDV / Annualized  Fully Diluted Valuation divided
                 Revenue           by Annualized Revenue. A
                                   comparative valuation metric to
                                   assess the speculative premium
                                   embedded in the token price
                                   [@HeliumMobileCMC].
  ----------------------------------------------------------------

  : Standardized Metrics for Comparison
:::

## Empirical Stress Test: Historical Performance Analysis

This section executes the \"static stress test\" by analyzing how the
comparative set performed during documented historical stress events.
This empirical data replaces the need for generating synthetic stress
scenarios in a simulation.

### Stress Scenario 1: The Liquidity Shock & Crypto Winter (2022-2023)

**Context:** During the 2022 crypto winter, the market contracted
significantly. Helium (HNT) saw its price decline from highs of
$\sim\$55$ to under $\$2$, losing approximately $95\%$ of its value
[@BitDegreeHelium]. This serves as a perfect empirical case study for
Liquidity-Driven Incentive Compression [@RapidInnovation2024].

**Helium's Response:**

- **Price Impact:** Despite the catastrophic price drop, the number of
  active hotspots did not collapse proportionally. The physical nature
  of the miners (mounted on roofs with sunk costs of $\sim\$500$)
  created high exit friction [@RapidInnovation2024].

- **Provider Behavior:** Providers largely remained online because the
  marginal cost of operation (electricity) was negligible compared to
  the effort of uninstallation. This validates the \"Sunk Cost Moat\"
  theory: hardware creates resilience against immediate churn but stalls
  future capacity growth under stress.

- **Failure Mode Observed:** While retention remained high, *Latent
  Capacity Degradation* occurred. New deployments flatlined, and
  maintenance of existing nodes likely dropped (though harder to measure
  without simulation, forum sentiment confirms this), degrading actual
  coverage quality over time [@GateSquare2025].

- **Governance Reaction:** Helium proposed the migration to Solana and
  the implementation of sub-DAOs (IOT and MOBILE) to compartmentalize
  risk---a clear example of the \"Emergency Centralization\" or
  \"Narrative Pivot\" archetype [@RapidInnovation2024].

**Implication for Onocoy:** Onocoy can expect its existing GNSS stations
to be \"sticky\" during price crashes due to high installation effort
(antennas require precise placement). However, new station growth will
freeze. Resilience strategies should focus on maximizing the utility of
existing capacity rather than incentivizing new hardware during these
periods.

### Stress Scenario 2: The \"Vampire Attack\" & Competitive Yield (2024-2025)

**Context:** Emerging DePIN protocols often target the same provider
base. In the GNSS sector, Geodnet and Onocoy compete for the same
rooftop real estate and technically savvy installers
[@TripleMining2025].

**Geodnet vs. Onocoy Dynamics:**

- **Yield Sensitivity:** Geodnet focuses on stable B2B revenue (RTK
  services) and utilizes a \"Location NFT\" to limit supply in saturated
  areas, enforcing a meritocracy that protects individual miner yield
  [@GeodnetIP7].

- **Elastic Provider Exit:** Multi-mining (running both Geodnet and
  Onocoy on similar hardware) is possible but introduces complexity.
  Providers demonstrate \"mercenary loyalty,\" prioritizing the network
  offering better immediate liquidity or yield.

- **Observed Behavior:** When Geodnet token (GEOD) prices rallied or
  burns increased due to enterprise contracts, it attracted professional
  surveyors who prioritize stable fiat-equivalent income over
  speculative tokens [@GeodnetLocationNFT].

- **Failure Mode:** *Elastic Provider Exit Under External Yield
  Pressure* [@RapidInnovation2024]. If Onocoy's rewards lag
  significantly behind Geodnet's for prolonged periods, \"dual-mining\"
  setups may convert to \"single-mining\" for the competitor to optimize
  bandwidth or hardware stability.

### Stress Scenario 3: Operational Cost Shock (Hivemapper 2024)

**Context:** Unlike stationary miners, Hivemapper requires active
driving, introducing variable costs (fuel, time). This creates a higher
OpEx floor, making the network more sensitive to token price drops.

**Hivemapper's Stress:**

- **Cost Sensitivity:** When the HONEY token price dipped, the \"real
  wage\" for driving dropped below the cost of fuel/time for many casual
  mappers.

- **Churn Response:** Unlike Helium hotspots, Hivemapper contributors
  stop mapping immediately when incentives fall below the effort
  threshold. Active contributors declined or plateaued during price
  stagnation periods, illustrating *Profitability-Induced Provider
  Churn* [@Coincub2025].

- **Mitigation Strategy:** Hivemapper responded by pivoting to B2B
  enterprise deals (Map Credits) to burn tokens and support price, and
  by introducing \"Honey Bursts\" (targeted bonuses) to surge supply
  only where needed---a form of \"Incentive Re-Targeting\"
  [@RapidInnovation2024].

## Tokenomic Mechanism Analysis: Comparative Robustness

We now analyze the specific tokenomic parameters of Onocoy against the
industry standards established by the comparative set. This \"static\"
analysis evaluates the theoretical soundness of the design mechanics.

### The Burn-and-Mint Equilibrium (BME)

Most major Solana DePINs (Helium, Render, Hivemapper) utilize BME to
stabilize token value against usage.

- **Mechanism:** Users pay in Fiat/Stablecoins $\to$ System buys & burns
  Tokens $\to$ Providers mint new Tokens.

- **Stress Behavior:** In a bull market, BME is reflexive (usage burns
  supply $\to$ price goes up $\to$ usage costs less tokens). In a bear
  market, if usage is low, the \"Mint\" (inflation) outweighs the
  \"Burn,\" creating a death spiral of dilution [@MediumTokenomics2026].

**Onocoy's Variance:** Onocoy utilizes a \"capped supply\" model with
deflationary elements (buyback and burn from revenue) rather than a pure
BME where minting is unlimited to meet demand [@OnocoyToken].

**Assessment:** Onocoy's capped supply is theoretically more resilient
to hyperinflationary death spirals than pure BME. However, it is less
flexible in subsidizing early growth if the token price is too high
(scarcity can stifle adoption) or too low (insufficient reward budget to
attract miners).

### Incentive Solvency: The Burn-to-Mint Ratio

This is the \"Golden Metric\" for static analysis, serving as the
primary indicator of long-term solvency:
$\text{Ratio} = \frac{\text{Burn}}{\text{Mint}}$.

- **Helium Mobile:** Has historically approached a 1:1 or deflationary
  ratio in specific months due to high subscriber revenue, indicating
  high solvency [@HeliumMobileCMC].

- **Hivemapper:** Historically low ratio (high emissions, low burn),
  though improving with enterprise deals [@CoinMarketCapHM].

- **Onocoy:** As an early-stage network, this ratio is likely $< 0.1$
  (highly subsidized).

**Risk Assessment:** A ratio consistently below 1.0 implies the network
is consuming its own market capitalization to survive. Long-term
solvency requires this metric to cross 1.0. The comparative data
suggests that networks which fail to improve this ratio within 24 months
of launch face significant risk of \"Reward Addiction\" failure.

## DePIN Failure Modes: A Diagnostic Matrix

Based on the historical data and theoretical framework, we define five
operational failure modes for Onocoy and other DePINs. These definitions
allow for \"diagnosis\" without the need for complex simulation
[@RapidInnovation2024].

1.  **Reward-Demand Decoupling:** Emissions persist at a high rate while
    network usage (demand) flatlines or drops. If GNSS stations deploy
    faster than RTK data buyers can be onboarded, ONO rewards will
    dilute rapidly [@Coincub2025].

2.  **Liquidity-Driven Incentive Compression:** External market
    sell-offs reduce the fiat value of the fixed token rewards, pushing
    provider ROI below the break-even point. GNSS stations are low-power
    (low OpEx), so they are less sensitive to this than GPU networks but
    more sensitive than passive staking protocols [@RenderThesisLB].

3.  **Latent Capacity Degradation:** Providers stop maintaining hardware
    due to low rewards. High \"Active Node\" count but falling
    \"Quality/Uptime\" scores. RTK requires precise calibration; if
    rewards drop, providers may neglect maintenance, degrading network
    accuracy [@GateSquare2025].

4.  **Elastic Provider Exit:** Capital (hardware) moves instantly to a
    competitor offering higher yield. Significant risk if Geodnet offers
    higher yield for compatible hardware.

5.  **The Death Spiral:** Feedback loop where Price Drop $\to$ Lower
    Yield $\to$ Miner Churn $\to$ Lower Security $\to$ Lower Demand
    $\to$ Further Price Drop [@MediumHeliumMiner].

## Conclusion: Benchmarking Summary

Analyzing DePIN tokenomics without simulation is not only possible but
often more revealing than theoretical modeling. By employing a
comparative event study framework, we can observe how real-world
networks like Helium, Hivemapper, and Render have responded to the
stress of bear markets, liquidity crunches, and competitive pressure.

The empirical data indicates that physical sunk costs act as a powerful
retention buffer, preventing immediate collapse during price drops
(unlike DeFi). However, this resilience is temporary; without a
transition to Real Yield (Burn-to-Mint ratios $> 1$), networks
eventually succumb to Reward Addiction and Latent Capacity Degradation.

For Onocoy, this comparison highlights the need to tighten the coupling
between Rewards and Realized Demand, and to differentiate incentives to
reward high-commitment, professional providers---increasing the economic
moat against \"mercenary\" switching.

# Methodology: Simulation-Based Stress Testing {#sec:methodology}

## Purpose and Non-Goals

This simulation framework examines how tokenomic mechanisms in
Decentralized Physical Infrastructure Networks (DePIN) behave when
conditions deteriorate [@Messari2024]. Our aim is not to predict future
outcomes or identify winning designs, but to compare how different
incentive structures respond when exposed to the same adverse scenarios.
The emphasis is therefore on *relative behavior* under stress, rather
than on absolute performance or forecasting accuracy [@Sollaci2004].

We use simulation because DePIN systems combine several features that
are difficult to study analytically. Infrastructure providers are
heterogeneous, incentives operate through protocol rules rather than
direct contracts, and external conditions such as demand or market
sentiment can change abruptly [@Ho2022]. These elements interact in
non-linear ways, especially once feedback effects emerge. A
simulation-based approach makes it possible to examine these
interactions directly, while keeping assumptions explicit and
inspectable [@SantaFeInstitute].

To avoid over-interpretation, a number of non-goals are defined upfront.
The model does not produce token price forecasts, valuation estimates,
or projections of market capitalization [@CFA2018]. Price dynamics are
included only as internal signals that reflect supply, demand, and
liquidity assumptions. Likewise, the results are not treated as causal
claims about real-world networks. All observed patterns are conditional
on the modeled assumptions and should be understood as indicative rather
than predictive.

The framework does not identify optimal parameter settings or prescribe
specific tokenomic designs. Instead, it surfaces trade-offs and failure
modes visible under stress. Finally, the model abstracts from governance
processes, legal constraints, and off-chain behavioral factors that may
be important in practice but cannot be represented in a tractable and
reproducible way within the scope of this study.

This aligns with standard practice in complex systems research, where
controlled comparison under adverse conditions is preferred over
predictive modeling in settings characterized by uncertainty, feedback
effects, and heterogeneous agents [@Morris2019; @Braakman2022].

## Model Scope and Agent Representation

The simulation model represents DePIN dynamics through a limited set of
interacting components that capture the core economic relationships
relevant to infrastructure sustainability. The scope is defined by what
can be meaningfully stress-tested, rather than by an attempt to mirror
the full complexity of real-world networks [@BrouwerBurg2016].

At the center of the model are infrastructure providers, represented as
heterogeneous agents. Providers differ along several dimensions that
materially affect their economic outcomes, including operational costs,
effective capacity contribution, and hardware tier. This heterogeneity
is essential, as DePIN networks do not consist of interchangeable
participants but of operators with varying cost structures. Provider
behavior is limited to economically motivated decisions, primarily
continued participation, exit (churn), or entry, based on profitability
thresholds and accumulated losses [@Mardikes2025].

Users are not modeled as individual agents. Instead, service demand is
treated as an exogenous input, specified through time-varying demand
regimes. While real demand may respond endogenously to price or service
quality, introducing such feedback would require assumptions that cannot
be validated within the scope of this thesis. Demand is therefore used
as a controlled external driver, allowing the analysis to focus on how
tokenomic mechanisms respond to stress rather than on how demand itself
forms.

The protocol is represented as a rule-based system that governs
emissions, reward allocation, burn mechanisms, and price-related
dynamics. Protocol behavior is deterministic given a set of parameters
and inputs, and does not adapt strategically over time. This abstraction
is intentional: the objective is to evaluate the behavior of tokenomic
mechanisms as designed, not to model governance interventions.

Within this structure, we maintain a clear distinction between
endogenous variables (token supply, provider profitability, churn,
incentive solvency) and exogenous variables (demand regimes,
macroeconomic conditions, liquidity shocks). This separation allows
observed outcomes to be traced back to specific stress inputs and
mechanism responses.

## Inputs, Parameters, and Exogenous vs Endogenous Variables

The simulation framework operates on a clearly defined set of inputs and
parameters that determine how the system evolves over time. These inputs
are grouped by their role in the model rather than by their real-world
source, in order to make assumptions explicit. A central design
principle is that parameters are treated as *ranges and regimes*, not as
precise estimates of real-world values.

Exogenous inputs define the external environment. These include demand
regimes, macroeconomic conditions, and discrete shock events. Demand is
specified as a time series that can follow different patterns, such as
steady usage, growth followed by decay, or highly volatile behavior.
Macroeconomic conditions are represented through scenario-level
modifiers. Liquidity shocks, such as large token unlocks, are introduced
as one-time exogenous disturbances. Treating these factors as exogenous
allows the same stress conditions to be applied consistently across
different tokenomic configurations.

Protocol-level parameters define the incentive mechanisms under
evaluation. These include emission limits, burn fractions, reward
allocation rules, and treasury handling strategies. Parameters in this
category are varied across simulation runs to represent alternative
tokenomic designs or policy choices. Importantly, the model does not
assume that protocol parameters adapt dynamically in response to
outcomes. Any change in emissions or incentive structure is introduced
explicitly as part of a scenario, rather than emerging endogenously.

Provider-level parameters describe the economic characteristics of
infrastructure operators. These include capital expenditure proxies,
ongoing operational costs, and participation thresholds. Provider
heterogeneity is introduced by sampling these parameters from predefined
distributions. Where practitioner input is used (e.g., typical cost
ranges or revenue expectations), it is incorporated as broad intervals
influenced by public documentation, not as exact figures.

## Stress Dimensions and Scenario Design

Stress scenarios in the simulation are designed to represent adverse
conditions that are plausible for DePIN networks and that materially
challenge incentive alignment, provider retention, and service
continuity. The model focuses on a limited set of stress dimensions that
recur across incentive-driven infrastructure systems.

A first category of stress relates to demand conditions. Demand regimes
are specified exogenously and include stable demand, growth followed by
decay, and highly volatile usage patterns. These regimes reflect the
well-documented risk that early network adoption does not translate into
sustained utilization [@Ho2022].

A second category relates to external market shocks. Macroeconomic
regimes (Bear, Bull, Sideways) modulate the baseline assumptions for
token price drift and volatility. Liquidity shocks simulate sudden sell
pressure events, testing the system's ability to maintain incentive
alignment even in the absence of changes in underlying demand
[@Gauntlet; @ChaosLabs].

Provider-side stress is introduced through economic viability
thresholds. In scenarios where operational costs increase, rewards
decline, or token prices fall, providers may experience sustained
losses. The model represents this through probabilistic churn mechanisms
that activate after consecutive periods of unprofitability.

These stress dimensions can be applied individually or in combination,
allowing the analysis to explore compound failure conditions. Prior work
on complex systems suggests that the interaction of multiple stressors
often produces non-linear outcomes that are not apparent when shocks are
considered in isolation. By standardizing the definition and timing of
stress across scenarios, the model enables direct comparison of how
different tokenomic mechanisms absorb or amplify adverse conditions.

## Metrics and Computation

The evaluation of tokenomic robustness in this study relies on a fixed
set of metrics defined prior to analysis. Metrics are selected based on
their ability to capture incentive sustainability, provider behavior,
and system-level stress responses, rather than short-term market
performance.

A primary category of metrics captures provider sustainability and
retention. Provider retention rates and churn counts are used to assess
whether incentive structures are able to maintain infrastructure
participation under stress. These measures are particularly important in
DePIN systems, where provider exit can lead to persistent losses in
service capacity due to physical deployment constraints.

A second category relates to economic viability and incentive solvency.
Metrics such as provider profitability, net incentive balance, and
revenue-to-emission ratios are used to examine whether rewards remain
economically meaningful relative to costs over time. Rather than
interpreting these values as precise financial indicators, they are used
as *proxies* for incentive health.

System-level performance is captured through capacity and utilization
metrics, including total active capacity, demand served, and utilization
rates. These measures reflect whether the network continues to deliver
service under adverse conditions, independent of token price dynamics.

To assess broader tokenomic dynamics, the model tracks supply-side and
flow-based indicators, including net emissions, burn-to-mint ratios, and
token velocity proxies derived from transaction turnover. These metrics
are not interpreted as direct measures of market efficiency, but as
signals of whether token circulation and supply pressures remain aligned
with usage-driven demand.

Finally, distributional outcomes are examined using concentration
metrics, such as top-participant reward shares or inequality proxies.
These measures are included to detect whether stress conditions lead to
excessive centralization of rewards or capacity, which may undermine
network resilience even when aggregate metrics appear stable.

## Reproducibility and Validation Strategy

Reproducibility is treated as a core requirement of the simulation
framework. All experiments are defined by an explicit set of parameters,
scenario inputs, and random seeds, allowing results to be regenerated
and inspected without reliance on undocumented assumptions or
interactive tuning.

Stochastic elements are present in several parts of the simulation,
including demand variation, provider heterogeneity, churn decisions, and
price-related noise. To ensure that observed outcomes are not driven by
single-run artifacts, each scenario is evaluated across multiple
simulation runs using seeded pseudo-random number generation. Results
are then aggregated to examine central tendencies and dispersion rather
than relying on individual trajectories.

Validation in this context does not aim to establish empirical accuracy
with respect to real-world data. Instead, the model is validated through
internal consistency and behavioral plausibility checks. These include
baseline runs without stress, where the system is expected to exhibit
stable participation and bounded dynamics, as well as controlled
perturbations where directional responses can be anticipated based on
incentive logic.

Sensitivity analysis is used to further assess robustness. Key
parameters (cost ranges, emission limits, and churn thresholds) are
varied within predefined intervals to examine whether qualitative
outcomes persist under moderate perturbations. Outcomes that remain
stable across reasonable parameter variations are treated as more robust
signals.

## Limitations of the Model

While the simulation framework is designed to support structured stress
testing, it necessarily abstracts from many aspects of real-world
network behavior. These limitations are not incidental, but a
consequence of deliberate design choices made to preserve
interpretability and reproducibility.

Several limitations shape the model's scope. Demand is modeled as an
exogenous process; although some scenarios allow demand to vary over
time, the model does not fully endogenize user behavior or price
elasticity. Providers are represented as economically rational agents
operating under simplified decision rules, excluding strategic behavior
such as long-term speculation or coordinated action.

The price formation mechanism is a reduced-form approximation, combining
buy and sell pressure, dilution effects, scarcity signals, and
stochastic noise to generate directional price dynamics. This approach
is sufficient for comparative stress testing but does not attempt to
replicate actual market microstructure. The temporal resolution of the
model is limited to discrete time steps, obscuring intra-period dynamics
such as short-term volatility spikes.

Finally, empirical calibration is constrained by data availability.
Inputs derived from interviews or public documentation are treated as
indicative ranges rather than precise measurements. The framework is
therefore better suited to identifying relative sensitivities and
failure modes than to making absolute performance claims.

Taken together, these limitations imply that the results of the
simulation should be interpreted as comparative, conditional insights
rather than predictions. The value of the model lies in its ability to
expose how different tokenomic mechanisms respond under controlled
stress scenarios, not in asserting how any particular network will
behave in practice.

## Adversarial Stress and Future Work

A critical distinction in this framework is the assumption of
"economically rational but honest" agents. Real-world DePIN networks,
however, face existential risks from adversarial behavior, such as Sybil
attacks, GPS spoofing, and strategic governance capture
[@ResonanceSecurity2024]. While the current model captures economic
stress, it does not explicitly promote "Scenario S5: Verification
Failure," where malicious actors dilute rewards for honest participants,
potentially triggering a "Lemons Market" dynamic [@EconAgentic2025].

Future iterations of this framework should integrate adversarial agent
types to evaluate the resilience of verification mechanisms (e.g., Proof
of Physical Work) against coordinated spoofing. This would allow for a
more comprehensive assessment of "Anti-Fragile" tokenomics that includes
security vectors alongside economic ones [@GeodnetResearch].

# Stress Scenario Design {#sec:stress_scenarios}

## Operational Definition of Stress

In the context of this thesis, stress is defined operationally as an
externally imposed adverse condition that challenges the ability of a
DePIN network to maintain functional capacity through its incentive
system. Stress is not treated as an outcome, such as price decline or
provider exit, but as an input condition applied to the system.

This distinction is critical. By defining stress as an exogenous input,
the analysis avoids circular reasoning in which system failure is both
the cause and the consequence of stress. Instead, stress scenarios are
constructed as controlled perturbations to the environment in which
tokenomic mechanisms operate, allowing their responses to be observed
and compared.

Stress, as modeled here, targets three core dimensions of network
sustainability:

1.  Provider retention, reflecting the willingness of infrastructure
    operators to remain active.

2.  Service continuity, reflecting the network's ability to meet demand
    through available capacity.

3.  Incentive solvency, reflecting the balance between token issuance,
    usage-driven sinks, and economic viability.

These dimensions align with established interpretations of robustness in
complex systems, where resilience is assessed by continued function
rather than by avoidance of disturbance [@Braakman2022].

## Stress Dimensions Implemented

The simulation framework implements multiple stress dimensions, each
corresponding to real-world risk factors commonly observed in
crypto-economic systems and infrastructure networks. All stress
dimensions are treated as exogenous inputs, consistent with the scope
constraints defined in Section
[7](#sec:methodology){reference-type="ref" reference="sec:methodology"}.

### Macroeconomic Regimes

Macroeconomic conditions are represented through regime-based modifiers
that influence token price drift and volatility. Three regimes are
defined:

- Bearish, characterized by negative drift and elevated volatility.

- Sideways, characterized by neutral drift and moderate volatility.

- Bullish, characterized by positive drift and reduced volatility.

These regimes abstract broader market sentiment and liquidity conditions
without attempting to model specific macroeconomic variables. Their
purpose is to expose tokenomic mechanisms to varying background
conditions rather than to replicate real-world cycles.

### Demand Regimes

Demand for network services is modeled as a stochastic time series with
configurable structure. Four demand regimes are implemented:

- Stable demand, with low variance around a constant mean.

- Growth demand, exhibiting sustained upward trends.

- Volatile demand, characterized by high variance without long-term
  trend.

- High-to-decay demand, representing an initial surge followed by
  gradual decline.

These regimes reflect common adoption patterns observed in
infrastructure services, including early hype cycles and post-deployment
normalization. Demand remains exogenous by design, enabling isolation of
provider-side incentive responses.

### Liquidity Shocks

Liquidity stress is introduced through discrete token unlock events
combined with finite market depth. These events simulate situations in
which large token holders sell a portion of their holdings into an
automated market maker pool, producing abrupt price shocks.

Liquidity shocks are parameterized by:

- Unlock timing

- Proportion of circulating supply unlocked

- Available liquidity depth

The objective is not to model investor behavior but to evaluate how
tokenomic mechanisms respond to sudden price dislocations.

### Provider Economics Stress

Provider-side economic stress is modeled through increases in
operational costs, competitive yield opportunities, and reduced
profitability thresholds. These inputs reflect real-world pressures
faced by infrastructure operators, such as rising energy prices or
alternative revenue opportunities.

In addition, the model distinguishes between provider types (e.g.,
higher-cost professional installations versus lower-cost basic setups),
allowing differential sensitivity to stress.

### Tokenomics Parameter Stress

Finally, stress is applied directly to tokenomic parameters, including
emission caps, burn fractions, and initial supply conditions. This
allows evaluation of how sensitive system behavior is to design choices,
rather than to external shocks alone.

## Scenario Combination Rules

Stress dimensions are combined according to clearly defined rules.
Parameter-based stresses (e.g., macro regime, demand regime, provider
costs) may be combined freely, allowing compound stress scenarios to be
evaluated. In contrast, scenario-specific behaviors (such as saturation
or utility-focused modes) are treated as mutually exclusive to preserve
interpretability.

This design choice reflects a trade-off between realism and experimental
control. While real-world systems may experience overlapping structural
transitions, isolating scenario-specific behaviors reduces confounding
effects and supports clearer comparative analysis.

## Relevance of Stress Scenarios

The stress scenarios implemented in this thesis are not exhaustive
representations of all possible risks faced by DePIN networks. Rather,
they are selected to capture representative failure pressures commonly
cited in practitioner and academic literature, including subsidy
dependency, liquidity fragility, and provider churn
[@Messari2024; @Ho2022].

By standardizing these scenarios, the framework enables consistent
comparison across tokenomic mechanisms and protocol profiles.

# Evaluation Metrics {#sec:evaluation_metrics}

## Principles for Metric Selection

Evaluating the robustness of tokenomic mechanisms requires metrics that
are both interpretable and aligned with the functional objectives of
DePIN networks. Three principles guide metric selection in this thesis:
metrics must be comparative, enabling evaluation of relative performance
across mechanisms and scenarios rather than absolute success or failure;
they must be mechanism-relevant, reflecting provider incentives, service
delivery, or economic sustainability rather than speculative market
outcomes; and they must be transparent, with clearly defined computation
and interpretation.

These principles align with established guidance for simulation-based
evaluation, where metrics should illuminate system behavior without
overstating precision [@Morris2019].

## Core Sustainability Metrics

The following core metrics are used to evaluate system behavior under
stress.

### Provider Retention and Churn

Provider retention is measured as the proportion of active providers
remaining over time, while churn captures the rate and magnitude of
provider exit events. These metrics directly reflect the stability of
the infrastructure layer and are central to DePIN sustainability.

Retention is interpreted directionally: higher retention under
comparable stress indicates greater robustness, but does not imply
optimal or permanent stability.

### Capacity Utilization and Service Continuity

Service continuity is assessed through capacity utilization and demand
satisfaction rates. Capacity utilization measures the extent to which
deployed infrastructure is effectively used, while demand satisfaction
captures the proportion of demand that can be served given available
capacity.

Together, these metrics indicate whether incentive mechanisms support
not only provider participation but also functional service delivery.

### Incentive Solvency (Burn-to-Mint Ratio)

Incentive solvency is proxied by the ratio of value burned through
usage-driven sinks to value emitted through token issuance. A ratio
approaching or exceeding unity suggests reduced reliance on subsidies,
while persistent divergence indicates ongoing subsidy dependency.

This metric abstracts complex monetary dynamics into a single
comparative signal and is interpreted cautiously as an indicator rather
than a definitive threshold.

### Net Emissions and Inflation Dynamics

Net emissions capture the balance between token issuance and destruction
over time. While absolute inflation rates are not used as targets,
changes in net emissions under stress reveal how mechanisms respond to
shifts in demand and participation.

### Token Velocity (Proxy)

Token velocity is estimated using transaction turnover as a proxy. While
this does not capture all aspects of monetary velocity, it provides
insight into whether tokens circulate primarily as a medium of exchange
or accumulate as idle balances.

Velocity is interpreted comparatively across scenarios and mechanisms,
not as an absolute indicator of economic health.

### Volatility Proxy

Price volatility is measured using relative dispersion metrics derived
from simulated price series. Given the simplified market representation,
volatility is treated as a stress signal affecting provider incentives
rather than as a market performance indicator.

## Derived Summary Indicators

Several derived indicators are computed to support synthesis and
interpretation.

### Death Spiral Probability

Death spiral probability is defined operationally as the frequency with
which simulations exhibit concurrent declines in price, provider count,
and service capacity beyond defined thresholds. This indicator captures
compounded failure dynamics without asserting inevitability.

### Network Revenue and Provider Profitability

Aggregate network revenue and average provider profitability are tracked
to contextualize incentive outcomes. These metrics help distinguish
between retention driven by genuine economic viability and retention
sustained by temporary subsidies.

## Interpretation and Limitations of Metrics

All metrics used in this thesis are subject to limitations arising from
model assumptions and abstraction. In particular, simplified price
formation and exogenous demand constrain the interpretation of monetary
indicators. Accordingly, metrics are used to compare relative
robustness, not to establish optimal designs or real-world predictions.

This cautious interpretation aligns with best practices in
simulation-based research and supports the thesis's evaluative rather
than predictive orientation [@Braakman2022].

# Simulation Results {#sec:simulation_results}

## Baseline Behavior (Sanity Check)

This section presents the results of the stress-testing simulations
described in Chapter 5. The purpose is to report observed outcomes under
standardized adverse scenarios, not to evaluate their desirability or to
draw normative conclusions. Interpretation and implications are deferred
to Chapter 7.

Results are organized around comparative stress responses of tokenomic
mechanisms rather than absolute performance levels. Each experiment
evaluates how a given protocol configuration behaves relative to others
when exposed to the same stress inputs. This structure reflects the
central aim of the thesis: to assess directional robustness and failure
sensitivity, not to rank protocols by success or forecast real-world
outcomes.

The results are grouped into four thematic blocks:

1.  Baseline Behavior Under Neutral Conditions\
    Establishes reference trajectories for price, supply, provider
    participation, and incentive balance in the absence of external
    stress. These runs serve solely as comparison anchors and are not
    interpreted as equilibrium states.

2.  Response to Demand-Side Stress\
    Examines how tokenomic mechanisms react to sudden demand
    contraction, demand volatility, and high-to-decay demand regimes.
    Outcomes are evaluated in terms of provider retention, utilization,
    and emission efficiency.

3.  Response to Supply- and Liquidity-Side Stress\
    Analyzes the effects of emission pressure, burn intensity, and
    liquidity shocks such as investor unlock events. Focus is placed on
    dilution dynamics, price drawdowns, and churn amplification.

4.  Compound Stress and Failure Thresholds\
    Evaluates system behavior under combined stressors, including
    bearish macro regimes, adverse provider economics, and competitive
    yield pressure. These scenarios are used to identify tipping points
    where incentive mechanisms cease to function as intended.

For each block, results are presented using a consistent set of metrics
defined in Section 5.3. Where stochastic variation is present, outcomes
are summarized using distributional statistics (median, interquartile
range, and tail behavior) across multiple simulation runs. Individual
time series are shown only where they illustrate structurally meaningful
patterns.

All figures follow the same conventions:

- identical time horizons,

- shared axes where comparison is intended,

- and standardized scenario labels.

Unless explicitly stated otherwise, all simulations use identical demand
processes, macro regimes, and random seeds across protocol profiles to
ensure comparability.

It is important to emphasize that no result in this chapter should be
read as a performance claim about any real-world network. Observed
behaviors reflect the interaction between modeled mechanisms and imposed
stress conditions under the assumptions documented in Chapter 5. The
value of these results lies in their comparative consistency and in the
patterns they reveal across scenarios, not in their absolute magnitudes.

### Experimental Setup

Baseline simulations are conducted over a fixed horizon of 52 weeks
using a weekly timestep. For each protocol profile, 100 Monte Carlo
simulations are executed with a deterministic master seed strategy to
ensure reproducibility. All simulations use the agent-based execution
model with identical neutrality constraints applied across profiles.

Key baseline conditions include a consistent demand regime with zero
demand volatility, a sideways macroeconomic regime, and the explicit
disabling of scenario logic, investor unlocks, competitor yield effects,
and growth shocks. These constraints ensure that observed dynamics arise
solely from the interaction between protocol-specific tokenomic
mechanisms and provider-level economics, rather than from exogenous
stress factors.

The baseline profiles evaluated in this section include Onocoy (ONO) and
a set of comparator DePIN protocols representing a range of
infrastructure types and incentive designs: Helium, Render, Filecoin,
Akash, Hivemapper, DIMO, Grass, io.net, Nosana, and Geodnet.

### Baseline Trajectories

Across all profiles, baseline simulations generate stable and smooth
trajectories for core state variables such as token supply, emissions,
burns, provider count, aggregate capacity, and utilization. In the
absence of shocks or volatility, these trajectories reflect the
steady-state behavior implied by each protocol's emission logic, reward
allocation rules, and provider cost structure.

Token price series under baseline conditions exhibit limited dispersion
in early periods for some profiles, with the interquartile range
collapsing to a single value at certain timesteps. This behavior is a
direct consequence of strict neutrality assumptions, including zero
demand noise and the absence of stochastic macro or liquidity effects.
Under these conditions, price evolution becomes highly constrained by
deterministic components of the model.

By contrast, provider-level economic metrics such as average provider
profit display visible dispersion across simulations, even under neutral
conditions. For example, the interquartile range of average provider
profit for the ONO profile diverges meaningfully from the median within
the first few weeks, reflecting heterogeneity in provider costs,
capacity, and churn dynamics. This confirms that the Monte Carlo
structure is functioning as intended and that stochastic variation
persists at the agent level even when aggregate demand and macro inputs
are fixed.

### Provider Economics and Retention

Baseline retention metrics indicate that provider populations remain
largely stable over the 52-week horizon for profiles that begin with a
non-zero provider count. Where a profile's initial provider count is
zero, retention metrics are reported as undefined rather than imputed,
in order to avoid misleading normalization.

Retention is reported in two complementary forms: absolute retention,
defined as the ratio of active providers relative to the initial
provider count, and week-to-week retention rate derived from observed
churn events. Under baseline conditions, churn events are driven solely
by provider-level profitability thresholds and cost structures, without
amplification from price shocks or demand collapses.

These baseline retention trajectories serve as a reference point for
later stress scenarios, where deviations from baseline behavior can be
attributed to specific adverse conditions rather than to underlying
model instability.

### Interpretation Boundaries of Baseline Results

It is important to emphasize that baseline results are descriptive
rather than evaluative. Observed trends in price, profitability, or
provider dynamics under neutral conditions should not be interpreted as
indicators of real-world performance or sustainability. Instead, they
establish a controlled reference environment in which the internal
mechanics of each tokenomic system operate without external stress.

The baseline therefore functions as a calibration layer for subsequent
analysis. In later sections, stressed scenarios are evaluated relative
to these baseline trajectories, allowing deviations in retention,
incentive solvency, and service continuity to be attributed to specific
stress mechanisms rather than to baseline model behavior.

## Stress Scenarios: Definition and Execution

This section defines the adverse conditions under which DePIN tokenomic
mechanisms are evaluated in subsequent analyses. Each stress scenario is
designed to isolate a specific class of risk commonly encountered by
real-world DePIN deployments. Scenarios are implemented in a controlled
and standardized manner to ensure comparability across protocol profiles
and to enable attribution of observed effects to specific stress
mechanisms rather than to baseline dynamics.

All stress scenarios build directly on the neutral baseline
configuration described in Section 6.2. Unless explicitly stated
otherwise, only one scenario-specific stress mechanism is activated at a
time. All other parameters remain identical to the baseline
configuration.

### Rationale for Scenario-Based Stress Testing

DePIN networks operate at the intersection of physical infrastructure,
economic incentives, and market volatility. As a result, system failure
is rarely caused by a single factor in isolation. However, evaluating
compound shocks without first understanding individual stress responses
risks obscuring causal pathways.

Scenario-based stress testing is therefore employed to examine
directional robustness under clearly defined adverse conditions. This
approach aligns with established practices in simulation-based
evaluation of complex systems, where standardized shocks are used to
test mechanism sensitivity and failure modes before compound
interactions are introduced.

The scenarios defined below reflect empirically observed risks in DePIN
and adjacent crypto-economic systems, including demand contraction,
liquidity shocks, competitive pressure, and provider-side economic
stress.

### Scenario S1: Demand Contraction

The demand contraction scenario models a sustained reduction in service
demand relative to baseline conditions. This scenario reflects
situations such as market downturns, loss of enterprise clients,
regulatory friction, or delayed adoption of the underlying service.

Implementation:

- Demand regime is modified from consistent baseline demand to a
  declining or suppressed demand trajectory.

- No changes are made to emission schedules, provider costs, or
  liquidity conditions.

- Demand volatility may remain low to isolate level effects rather than
  noise-induced effects.

Analytical focus:

- Burn-to-emission dynamics under reduced utilization.

- Provider profitability as a function of fixed operating costs.

- Early signals of incentive insolvency without price shocks.

### Scenario S2: Liquidity Shock

The liquidity shock scenario simulates a sudden increase in sell
pressure resulting from token unlocks or large holder exits. This
scenario reflects common events in crypto markets such as investor
vesting cliffs or coordinated exits during market stress.

Implementation:

- A discrete investor unlock event is introduced at a predefined
  simulation week.

- A fixed percentage of circulating supply is sold into available
  liquidity.

- All other parameters remain identical to baseline conditions.

Analytical focus:

- Price sensitivity to sell pressure.

- Secondary effects on provider revenue denominated in token value.

- Churn amplification driven by price-mediated profitability thresholds.

### Scenario S3: Competitive Yield Pressure

This scenario introduces external competition for infrastructure
providers by simulating an alternative yield opportunity. It reflects
situations where providers can redeploy capital or hardware to competing
networks offering higher short-term returns.

Implementation:

- A competitor yield parameter is activated, increasing the opportunity
  cost of participation.

- Provider churn probability is adjusted based on relative
  profitability.

- No direct changes are made to demand or token supply.

Analytical focus:

- Elasticity of provider participation.

- Sensitivity of retention to marginal profit compression.

- Differentiation between high-commitment and low-commitment providers.

### Scenario S4: Provider Cost Inflation

The provider cost inflation scenario models increases in operating
expenses, such as energy prices, maintenance costs, or regulatory
compliance burdens. This scenario isolates supply-side stress
independent of demand or market conditions.

Implementation:

- Provider operating costs are increased uniformly or by tier.

- Tokenomic parameters remain unchanged.

- Demand and price regimes follow baseline assumptions.

Analytical focus:

- Margin compression at the provider level.

- Differential effects across provider types.

- Early indicators of infrastructure attrition driven by cost pressure.

### Execution and Comparability

All stress scenarios are executed using the same Monte Carlo structure
as the baseline, with identical simulation counts, time horizons, and
seed strategies. This ensures that observed differences between
scenarios and baseline trajectories are attributable to
scenario-specific inputs rather than to stochastic artifacts or
configuration drift.

Scenario outputs are recorded using the same metric set and data
structures as baseline simulations. This enables direct comparison
across scenarios and supports consistent visualization and statistical
summarization in subsequent sections.

## Stress Scenario Results (Comparative Outcomes)

This section reports the observed outcomes of the stress scenarios
defined in Section 6.3. Results are presented as deviations from the
neutral baseline trajectories established in Section 6.2. The focus is
on *what changes*, *when changes occur*, and *which metrics are
affected*, without attributing causality or normative judgment.
Interpretation of these outcomes is deferred to subsequent sections.

All results are aggregated across 100 Monte Carlo simulations per
protocol profile. Unless stated otherwise, reported trajectories refer
to median values, with interquartile ranges (p25--p75) used to
illustrate dispersion where relevant.

### Demand Contraction Scenario

Under demand contraction, all protocol profiles exhibit a measurable
decline in utilization, followed by a widening divergence between token
emissions and realized burns. This effect manifests earliest in metrics
directly tied to service usage, including demand served, utilization
rate, and burn-derived revenue.

Across profiles, reduced utilization leads to lower average provider
revenue while emissions continue according to protocol-specific
schedules. As a result, the burn-to-emission ratio declines relative to
baseline, particularly in protocols with fixed or weakly demand-linked
emission logic. Provider counts remain initially stable but begin to
diverge from baseline trajectories as profitability thresholds are
breached for marginal providers.

Dispersion across simulations increases over time for provider-level
metrics such as average provider profit and churn counts, indicating
sensitivity to heterogeneous cost structures even under identical demand
trajectories.

### Liquidity Shock Scenario

The liquidity shock scenario produces immediate and discrete deviations
in token price trajectories at the point of the unlock event. The
magnitude of the price response varies significantly across protocol
profiles, reflecting differences in circulating supply, liquidity depth,
and emission rates.

Following the shock, secondary effects are observed in provider
economics. In profiles where provider rewards are denominated primarily
in the native token, reductions in token price translate into compressed
real revenue, leading to increased churn in subsequent weeks. This
effect is not instantaneous but unfolds with a short lag, corresponding
to reward distribution timing and provider decision thresholds.

Notably, while price volatility spikes sharply around the unlock event,
other metrics such as utilization and capacity remain initially close to
baseline. This temporal decoupling highlights the indirect transmission
of liquidity stress from token markets to infrastructure participation.

### Competitive Yield Pressure Scenario

When external yield pressure is introduced, provider participation
becomes more elastic across all evaluated profiles. The most pronounced
effects are observed in provider churn metrics rather than in price or
utilization measures.

Provider exit accelerates in profiles where baseline profitability
margins are narrow, while protocols with higher average provider surplus
show greater resistance. The dispersion of outcomes across simulations
increases markedly, indicating that small differences in provider
economics can lead to divergent participation trajectories under
competitive pressure.

Unlike liquidity shocks, competitive yield pressure does not produce
abrupt discontinuities in token price or supply. Instead, its effects
accumulate gradually, primarily through sustained differences in
provider retention relative to baseline.

### Provider Cost Inflation Scenario

Provider cost inflation directly impacts average provider profit across
all protocol profiles. Increases in operating costs reduce margins
uniformly, but downstream effects vary depending on reward structure and
provider heterogeneity.

In several profiles, median provider profit crosses below zero earlier
than under other stress scenarios, leading to persistent negative
profitability even in the absence of price shocks or demand contraction.
Churn metrics respond accordingly, with elevated exit rates observed
once cost thresholds are exceeded.

Importantly, capacity and utilization do not decline immediately in this
scenario. Instead, reductions in active providers precede observable
changes in service capacity, indicating a lag between economic stress
and infrastructure degradation.

### Cross-Scenario Comparison

Comparing across stress scenarios reveals distinct temporal and
metric-specific signatures:

- Demand contraction primarily affects burn-linked metrics and
  utilization.

- Liquidity shocks propagate rapidly through price metrics before
  affecting provider participation.

- Competitive yield pressure manifests as gradual erosion of provider
  counts.

- Cost inflation exerts sustained pressure on provider profitability
  with delayed capacity effects.

Across all scenarios, deviations from baseline trajectories are most
pronounced in provider-level metrics, while aggregate supply and
emission variables tend to remain closer to baseline unless explicitly
modified by the scenario.

These observed patterns form the empirical basis for identifying
recurring failure modes in DePIN tokenomic systems, which are formalized
in the following section.

## Failure Modes Observed (Operational Definitions)

Table [3](#tab:failure_modes){reference-type="ref"
reference="tab:failure_modes"} provides a diagnostic matrix for
identifying the five recurring failure modes formalized in this section.

::: {#tab:failure_modes}
  **Failure Mode**                   **Operational Definition**                                      **Precursor Metric**
  ---------------------------------- --------------------------------------------------------------- -------------------------------------------------
  **Reward--Demand Decoupling**      Emissions persist despite declining usage.                      Declining burn-to-emission ratio.
  **Profitability-Induced Churn**    Exit driven by sustained negative margins (not price).          Avg provider profit $<0$ for $N$ weeks.
  **Liquidity-Driven Compression**   Price crash reduces real reward value, causing delayed churn.   Price shock $\to$ lagged exit.
  **Elastic Provider Exit**          High sensitivity to yield relative to competitors.              Elevated churn despite stable internal metrics.
  **Latent Capacity Degradation**    Service capacity drops long after economic stress begins.       Provider count drops before capacity drops.

  : Operational Failure Modes: Diagnostic Matrix
:::

This section formalizes the recurring failure modes observed across
stress scenarios by defining them in operational, measurable terms.
Failure modes are not treated as binary outcomes or protocol-level
judgments. Instead, they are defined as *patterns of metric behavior*
that emerge consistently under specific adverse conditions and indicate
increasing fragility in the incentive system.

Each failure mode is grounded in observable deviations from baseline
trajectories and is specified using explicit metric signatures. These
definitions provide a common vocabulary for comparing DePIN tokenomic
systems and serve as the analytical bridge between empirical results and
subsequent implications.

### Reward--Demand Decoupling

Definition:\
Reward--demand decoupling occurs when token emissions and provider
rewards remain elevated relative to realized service demand, resulting
in a sustained divergence between minting and burn-linked revenue.

Operational indicators:

- Persistent decline in utilization relative to baseline.

- Decreasing burn-to-emission ratio over time.

- Stable or increasing emissions despite reduced demand served.

- Compression of average provider profit without immediate price
  collapse.

Observed context:\
This pattern is most clearly observed under demand contraction
scenarios, where reduced usage does not immediately propagate into lower
emissions. The decoupling persists until provider profitability
thresholds are crossed, at which point secondary effects such as churn
begin to emerge.

### Profitability-Induced Provider Churn

Definition:\
Profitability-induced provider churn refers to accelerated provider exit
driven by sustained negative or marginal profitability, independent of
abrupt market shocks.

Operational indicators:

- Average provider profit crossing below zero for multiple consecutive
  periods.

- Gradual increase in churn count relative to baseline.

- Divergence between provider count trajectories and baseline without
  corresponding demand or price shocks.

- Increasing dispersion in provider-level outcomes across simulations.

Observed context:\
This failure mode is prominent in provider cost inflation and
competitive yield pressure scenarios, where economic pressure
accumulates slowly rather than arriving as a discrete event.

### Liquidity-Driven Incentive Compression

Definition:\
Liquidity-driven incentive compression occurs when abrupt price declines
reduce the real value of token-denominated rewards, leading to
downstream effects on provider participation despite unchanged nominal
reward structures.

Operational indicators:

- Sharp, localized price drawdowns coinciding with liquidity events.

- Lagged decline in average provider profit following price shocks.

- Increased churn after reward distribution cycles.

- Temporary decoupling between utilization/capacity metrics and provider
  participation.

Observed context:\
This pattern emerges most clearly in liquidity shock scenarios, where
price volatility precedes changes in provider behavior. The delayed
response highlights the indirect transmission of market stress into
infrastructure-level outcomes.

### Elastic Provider Exit Under External Yield Pressure

Definition:\
Elastic provider exit describes heightened sensitivity of provider
participation to marginal changes in relative yield, resulting in
sustained attrition without dramatic price or demand movements.

Operational indicators:

- Elevated churn rates under competitive yield pressure relative to
  baseline.

- Minimal contemporaneous changes in token price or utilization.

- Increasing dispersion in provider retention outcomes.

- Gradual erosion of provider count rather than abrupt collapse.

Observed context:\
This failure mode is observed when alternative opportunities are
introduced, even in the absence of internal protocol stress. It reflects
the substitutability of provider capital and labor across competing
networks.

### Latent Capacity Degradation

Definition:\
Latent capacity degradation refers to delayed reductions in service
capacity that follow earlier provider exits, resulting in a temporal gap
between economic stress and observable service degradation.

Operational indicators:

- Provider count declines preceding reductions in aggregate capacity.

- Stable utilization metrics masking declining redundancy.

- Capacity drops occurring several periods after profitability-induced
  churn.

- Reduced resilience to subsequent demand or liquidity shocks.

Observed context:\
This pattern appears across multiple stress scenarios and highlights the
non-instantaneous relationship between provider economics and
service-level outcomes in infrastructure-based systems.

### Role of Failure Mode Definitions

These failure modes do not imply protocol failure in an absolute sense.
Rather, they represent *structural stress signatures* that can
accumulate, interact, and amplify under adverse conditions. By defining
failure modes operationally, the analysis enables systematic comparison
across DePIN designs and provides a foundation for evaluating mitigation
strategies in subsequent sections.

## Implications for Builders (Design Recommendations) {#implications-7.1-implications-for-builders-design-recommendations}

The stress-testing results and observed failure modes presented in
Section 6 highlight several recurring design tensions inherent to DePIN
tokenomic systems. These implications are not prescriptive blueprints,
but design considerations derived from empirically observed behavior
under adverse conditions. They are intended to inform protocol designers
about where fragility tends to emerge and which mechanisms warrant
particular attention during design and iteration.

### Align Emissions More Tightly with Realized Demand

One of the most consistently observed failure modes is reward--demand
decoupling, in which emissions and rewards persist despite declining
utilization. This suggests that fixed or weakly demand-sensitive
emission schedules can amplify stress during periods of demand
contraction.

Design implication:\
Builders should prioritize emission mechanisms that respond meaningfully
to realized service usage rather than to participation alone. Emission
logic that adapts to utilization or burn-linked signals can reduce the
accumulation of excess supply during downturns and delay the onset of
profitability-induced churn.

This does not imply fully reactive or highly volatile emissions, but
rather bounded responsiveness that maintains incentive alignment when
demand deviates from growth assumptions.

### Design for Provider Margin Resilience, Not Peak Returns

Across multiple scenarios, provider exit is driven less by short-term
volatility and more by sustained margin compression. Once average
provider profitability crosses below zero for extended periods, churn
accelerates even in the absence of dramatic market shocks.

Design implication:\
Tokenomic systems should be evaluated against downside margin scenarios
rather than upside reward narratives. Builders should stress-test
provider economics under elevated costs, reduced demand, and compressed
prices to ensure that a meaningful subset of providers remains
marginally profitable under adverse conditions.

This may involve conservative reward baselines, differentiated
incentives for higher-commitment providers, or mechanisms that reduce
cost exposure during unfavorable regimes.

### Treat Liquidity Events as Infrastructure Risks, Not Just Market Events

Liquidity shocks primarily manifest as price events, but their
downstream effects on provider participation reveal that they function
as infrastructure risks. The lagged response between price declines and
provider churn suggests that market stress propagates through reward
valuation rather than immediate behavioral reaction.

Design implication:\
Builders should explicitly account for liquidity events when designing
reward distribution and treasury strategies. Mechanisms that smooth
reward value, delay exposure to price shocks, or introduce buffers
between market volatility and provider compensation can reduce the
indirect transmission of liquidity stress into infrastructure attrition.

Ignoring liquidity dynamics as "external" risks underestimates their
impact on long-term network stability.

### Assume Provider Capital Is Mobile

Competitive yield pressure demonstrates that provider participation is
often elastic, even when demand and protocol fundamentals remain
unchanged. Providers compare returns across networks, and small relative
differences can lead to sustained attrition over time.

Design implication:\
DePIN tokenomics should be designed with the assumption that provider
capital and labor are mobile. Retention should not rely solely on
short-term reward competitiveness but should incorporate mechanisms that
reward persistence, commitment, or sunk-cost investments where
appropriate.

This may include tenure-based incentives, differentiated rewards by
hardware tier, or gradual reward vesting that aligns provider time
horizons with network needs.

### Account for Delayed Infrastructure Degradation

Latent capacity degradation highlights a structural characteristic of
DePIN systems: infrastructure quality may appear stable even as economic
stress accumulates. By the time capacity reductions become visible,
recovery may be slow or costly due to physical deployment constraints.

Design implication:\
Builders should monitor leading indicators of stress, such as declining
provider margins or increasing churn dispersion, rather than relying
solely on utilization or capacity metrics. Early-warning indicators
embedded in protocol analytics can provide time to adjust incentives
before service degradation becomes apparent.

Designing for observability is therefore as important as designing for
incentives.

### Positioning Note (important)

These implications are intentionally framed as *design considerations*,
not as claims of optimality. They reflect tendencies observed across
modeled systems under standardized stress conditions and should be
interpreted as guidance for further testing and refinement rather than
as universal rules.

## Implications for Onocoy (Actionable Suggestions)

The failure modes and stress responses observed in this study have
direct relevance for the Onocoy network, given its reliance on
physically deployed GNSS infrastructure and a token-based incentive
system. The following implications translate the general design
considerations outlined in Section 7.1 into Onocoy-specific suggestions.
These are not presented as prescriptions, but as areas where targeted
experimentation and monitoring could improve resilience under adverse
conditions.

### Strengthen the Coupling Between Usage and Rewards

Baseline and stress simulations indicate that demand-linked metrics are
central to maintaining incentive alignment over time. For Onocoy, where
service usage can be measured with relatively high precision, there is
an opportunity to reinforce the relationship between realized RTK demand
and reward distribution.

Actionable suggestion:\
Onocoy could explore mechanisms that increase the sensitivity of rewards
to verified service usage, particularly during periods of demand
contraction. This may involve adjusting reward weighting based on
utilization signals or introducing soft constraints that limit emissions
when burn-linked revenue consistently lags behind supply issuance.

Such adjustments would not need to be abrupt or highly reactive; even
gradual modulation could reduce prolonged reward--demand decoupling.

### Monitor Provider Margins as a Leading Indicator

Across scenarios, provider exit in the Onocoy profile is preceded by
sustained deterioration in average provider profitability rather than by
immediate market shocks. This suggests that provider margins function as
a leading indicator of infrastructure risk.

Actionable suggestion:\
Rather than focusing primarily on provider count or coverage metrics,
Onocoy could incorporate provider margin distributions into internal
monitoring. Tracking how many providers operate near or below breakeven
may provide earlier warning of impending churn than aggregate
participation statistics alone.

This information could inform proactive adjustments to incentives or
cost-sharing mechanisms before infrastructure attrition becomes visible
at the network level.

### Account for Token Price Sensitivity in Reward Design

Liquidity shock scenarios show that price-mediated reward compression
can trigger delayed churn even when nominal rewards remain unchanged.
For Onocoy, where rewards are denominated in ONO, this introduces an
indirect exposure to market volatility.

Actionable suggestion:\
Onocoy may benefit from evaluating how reward timing, smoothing
mechanisms, or partial stabilization strategies affect provider exposure
to short-term price movements. While full price insulation may be
neither feasible nor desirable, reducing abrupt changes in effective
reward value could help dampen second-order churn effects following
market stress.

This consideration is particularly relevant during known liquidity
events or periods of heightened market uncertainty.

### Differentiate Incentives by Provider Commitment Level

Simulation results suggest that providers with higher sunk costs and
longer commitment horizons exhibit greater resilience under stress.
Given the physical and technical requirements of GNSS infrastructure,
Onocoy's provider base is likely heterogeneous in both cost structure
and exit friction.

Actionable suggestion:\
Onocoy could further explore incentive differentiation based on provider
commitment characteristics, such as hardware tier, installation
complexity, or operational reliability. Reward structures that recognize
long-term contribution may reduce sensitivity to short-term competitive
yield pressure and strengthen infrastructure stability.

This approach aligns incentives with the physical realities of the
network rather than assuming uniform provider behavior.

### Use Stress Testing as an Ongoing Governance Tool

One of the central contributions of this thesis is the demonstration of
how stress testing can be applied systematically to DePIN tokenomics.
For Onocoy, such tools need not be limited to academic analysis.

Actionable suggestion:\
Onocoy could adopt simplified versions of stress-testing frameworks as
part of internal governance or parameter review processes. Periodic
evaluation of how proposed changes perform under adverse scenarios may
help identify unintended consequences before they manifest in
production.

In this sense, stress testing functions less as a predictive instrument
and more as a structured way to reason about risk.

### Positioning Note

These suggestions are derived from modeled behavior under standardized
assumptions and should be interpreted as exploratory rather than
definitive. Their value lies in identifying leverage points for further
investigation and experimentation, not in asserting optimal solutions.

## Implications for Researchers (What This Enables and What It Does Not)

This thesis contributes to the growing body of research on Decentralized
Physical Infrastructure Networks (DePIN) by demonstrating how tokenomic
mechanisms can be evaluated through structured stress testing rather
than through growth-oriented or valuation-centric analysis. The
implications for researchers are twofold: the framework introduced here
enables a new mode of comparative analysis, while also highlighting
clear methodological boundaries that future work must respect.

### What This Framework Enables

This work provides a reproducible approach for translating conceptual
tokenomic designs into testable models under controlled conditions. By
formalizing incentive mechanisms, provider behavior, and demand regimes
into explicit parameters, researchers can move beyond narrative
comparisons and evaluate directional robustness across protocols and
scenarios.

This enables comparative questions that are otherwise difficult to
answer empirically, such as how different emission structures respond to
identical demand shocks, or how provider retention dynamics vary when
reward--demand coupling weakens. Importantly, the framework allows for
controlled falsification: assumptions can be varied systematically, and
their effects observed transparently.

The stress-testing approach also supports interdisciplinary research at
the intersection of economics, systems engineering, and blockchain
governance. DePIN networks operate as socio-technical systems, where
physical constraints, human behavior, and protocol rules interact.
Simulation-based evaluation offers a practical method for studying these
interactions without requiring complete or proprietary real-world data.

The framework is extensible as well. While this thesis applies the model
to Onocoy as a primary case, the underlying structure can be adapted to
other DePIN categories, alternative incentive designs, or different
demand environments. This positions the work as a methodological
contribution rather than a single-case evaluation.

### What This Framework Does Not Enable

At the same time, it is essential to clarify the limits of the approach.
The simulations presented here do not predict real-world outcomes, token
prices, or network success. All results are conditional on modeled
assumptions and should be interpreted as directional indicators rather
than forecasts.

The framework also does not establish causal certainty. While modeled
relationships between incentives, provider behavior, and outcomes are
internally consistent, they remain abstractions of complex real-world
dynamics. External factors such as regulatory changes, technological
breakthroughs, or strategic behavior by large actors are not fully
captured.

Furthermore, the model does not replace empirical validation. Stress
testing can identify plausible failure modes and robustness patterns,
but it cannot confirm whether these dynamics will manifest identically
in live networks. As such, simulation results should be viewed as
complements to empirical observation, not substitutes for it.

### Research Directions Opened by This Work

The limitations of this thesis also point toward future research
opportunities. One direction involves integrating richer empirical data,
such as observed provider churn distributions or cost heterogeneity, to
refine behavioral assumptions. Another involves extending the framework
to multi-token or cross-network interactions, which are increasingly
relevant as DePIN ecosystems mature.

Finally, there is scope for methodological refinement. Sensitivity
analysis techniques, alternative agent decision models, and formal
validation against historical network events could further strengthen
the robustness of simulation-based evaluation in this domain.

### Closing Positioning Note

Taken together, this thesis positions stress testing as a useful
analytical lens for DePIN tokenomics, while maintaining a clear
separation between evaluation and prediction. By explicitly defining
what the framework enables and where its limits lie, the work aims to
contribute responsibly to an emerging research area characterized by
both technical complexity and high uncertainty.

## Positioning of This Contribution

This thesis positions its contribution at the intersection of mechanism
design, applied simulation, and empirical observation. It does not claim
to predict the success or failure of individual DePIN projects, nor does
it propose a universal template for sustainable tokenomics. Instead, it
offers a disciplined framework for evaluating how tokenomic mechanisms
behave under stress and how those behaviors interact with human
decision-making in real infrastructure networks.

The primary contribution lies in reframing tokenomics evaluation away
from growth narratives and toward resilience analysis. By focusing on
adverse conditions rather than idealized scenarios, the framework
emphasizes directional robustness, failure modes, and trade-offs rather
than optimality. This approach aligns with established practices in
simulation-based research, where the goal is to falsify assumptions and
surface vulnerabilities rather than to optimize parameters in isolation.

A second contribution is methodological. The combination of agent-based
simulation, standardized stress scenarios, and dashboard-aligned metrics
provides a reproducible and extensible evaluation tool. All results are
explicitly conditioned on assumptions, parameter ranges, and scenario
definitions, reinforcing methodological humility and avoiding
overinterpretation. This makes the framework suitable not only for
academic inquiry, but also for practical use by protocol designers
seeking to test incentive structures before irreversible deployment
decisions are made.

Finally, the integration of stress-response archetypes extends DePIN
analysis beyond purely formal mechanisms. By explicitly acknowledging
the role of human intervention under uncertainty, the thesis bridges the
gap between modeled behavior and observed protocol trajectories. This
layered perspective (mechanisms, metrics, and decision patterns) allows
for a more realistic understanding of resilience in decentralized
infrastructure systems.

Taken together, these elements position the thesis as an evaluative
contribution rather than a prescriptive one. It does not assert what
tokenomic designs should be adopted, but it does clarify how different
designs are likely to behave when conditions deteriorate. In doing so,
it aims to improve decision quality before failure occurs, rather than
to explain outcomes after the fact.

# Human Decision-Making Under Stress: DePIN Response Archetypes {#sec:human_decision_making}

Table [4](#tab:archetypes){reference-type="ref"
reference="tab:archetypes"} summarizes the five observed stress-response
patterns, which are detailed in the following subsections.

::: {#tab:archetypes}
  **Archetype**                      **Primary Driver**     **Tokenomic Consequence**                                  **Key Signal**
  ---------------------------------- ---------------------- ---------------------------------------------------------- ----------------------------------------
  **I: Subsidy Inertia**             Retention Fear         Widens subsidy gap; dilutes provider revenue.              Declining burn-to-emission.
  **II-A: Subsidy Boosting**         Short-term Churn Fix   Accelerates insolvency; creates "incentive overfitting".   Temporary retention spike $\to$ crash.
  **II-B: Incentive Re-Targeting**   Efficiency Alignment   Preserves core solvency; squeezes marginal supply.         Improved utilization efficiency.
  **III: Narrative Pivot**           Political Evasion      Delays adjustment; decouples price from utility.           Stable messaging vs bad metrics.
  **IV: Emergency Centralization**   Survival               Suspends decentralization; externalizes governance risk.   Rising concentration.

  : Human Decision-Making Archetypes Under Stress
:::

## Why Mechanism Design Alone Is Insufficient

Tokenomic mechanisms do not operate in isolation. In real-world DePIN
deployments, protocol behavior emerges from the interaction between
formal incentive rules and human decision-making under uncertainty.
While simulation-based evaluation can illuminate how mechanisms respond
to stress in a controlled environment, actual network trajectories are
shaped by how teams interpret signals, prioritize risks, and intervene,
often under time pressure and incomplete information.

Existing DePIN analyses tend to abstract away this human layer,
implicitly assuming that protocol parameters evolve optimally or that
governance reacts smoothly to deteriorating conditions. In practice,
responses to stress are neither instantaneous nor purely rational.
Instead, they follow recurring behavioral patterns that interact with
tokenomic structures in predictable ways.

This section introduces a set of stress-response archetypes observed
across DePIN projects during periods of adverse conditions
[@Messari2024]. These archetypes are not judgments of competence or
intent. Rather, they represent recurrent decision patterns that emerge
when teams attempt to stabilize networks facing declining demand, price
shocks, or provider churn. Importantly, each archetype interacts
differently with tokenomic mechanisms and can either mitigate or amplify
structural fragility.

## Archetype I: Subsidy Inertia (Emissions Denial)

**Definition:** Subsidy inertia refers to the continued reliance on
emissions-driven provider rewards despite clear signals of demand
contraction or declining incentive solvency.\
**Rationale at the Time:** This behavior is often motivated by
short-term retention concerns. For infrastructure-heavy DePINs like
Onocoy, provider exit is costly and partially irreversible. Teams fear
that lowering rewards will signal weakness or trigger irreversible
provider exits. Emissions are thus treated as a stabilizing force rather
than as a source of dilution.\
**Interaction with Tokenomics:** Under sustained demand weakness,
emissions denial increases the gap between token issuance and
usage-driven sinks. Simulation results show that this widens
inflationary pressure and compresses real provider profitability, even
when nominal rewards remain constant. The system appears stable in the
short term but accumulates hidden fragility.\
**Dashboard Signals:**

- Declining burn-to-emission ratio.

- Increasing token velocity driven by cost-covering sales.

- Rising provider losses despite unchanged nominal rewards.

## Archetype II: Incentive Overfitting vs. Re-Targeting

This archetype splits into two materially different responses.

### II-A: Subsidy Boosting (Overfitting)

**Definition:** Broad increases in rewards or temporary bonus programs
designed to arrest churn without altering what is being rewarded.\
**Interaction with Tokenomics:** While incentive extensions can
temporarily reduce churn, simulations demonstrate that they often worsen
long-term sustainability by increasing emissions without addressing
demand-side constraints. Over time, providers become conditioned to
elevated subsidies, making later normalization more disruptive.\
**Dashboard Signals:**

- Short-lived improvements in retention metrics.

- Worsening solvency ratios.

- Increased sensitivity to subsequent shocks.

### II-B: Incentive Re-Targeting (Adaptive Alignment)

**Definition:** Modification of reward logic to better reflect
economically valuable output rather than participation volume.\
**Onocoy Context:** Onocoy's focus on quality, availability, and
location scales reflects an early commitment to incentive re-targeting.
The quadratic decay applied to dense geographic clustering serves as a
structural guardrail against over-rewarding redundant supply.\
**Dashboard Signals:**

- Improved utilization efficiency.

- Slower provider growth but higher average profitability.

- More stable burn-to-emission trajectories under demand volatility.

## Archetype III: Narrative Pivot Without Structural Adjustment

**Description:** Rather than modifying tokenomic parameters, teams shift
messaging toward future use cases, long-term vision, or upcoming
integrations. The underlying incentive structure remains largely
unchanged.\
**Rationale at the Time:** Narrative pivots are low-cost and reversible.
They are often employed when governance processes are slow or when
parameter changes are perceived as risky or controversial.\
**Interaction with Tokenomics:** Narrative changes have limited impact
on provider economics when structural conditions remain unchanged.
Simulation results indicate that, absent demand recovery, incentive
solvency continues to deteriorate regardless of narrative framing.

## Archetype IV: Emergency Centralization

**Description:** Under severe stress, extensive intervention leads to
temporary or permanent centralization of control, infrastructure, or
execution environments to preserve network functionality.\
**Comparative Evidence:** The migration of Helium to Solana represents a
clear instance where operational survivability was prioritized over
architectural purity.\
**Interaction with Tokenomics:** Emergency interventions can stabilize
capacity and reduce churn in the short term. However, they introduce
governance risk and undermine long-term decentralization incentives.
Simulations suggest that while collapse probabilities decrease, recovery
elasticity often diminishes.

## Implications for Onocoy (Diagnostic Alignment)

The primary contribution of these archetypes is not explanatory
storytelling, but diagnostic alignment. Each response pattern maps
directly to observable signals within the stress-testing dashboard
developed in this thesis.

Rather than prescribing specific decisions, the framework allows
Onocoy's operators to ask a fundamental question: *Which stress-response
pattern are we currently exhibiting?* For Onocoy, this framing clarifies
how specific design choices (such as emission decay and location
penalties) interact with human decision-making to shape resilience
trajectories.

### Onocoy-Specific Diagnostic Signals

To make these archetypes actionable for Onocoy governance, we map the
abstract patterns to concrete internal signals [@OnocoyToken]:

- **Subsidy Inertia Signal:** If the DAO votes to extend "Beta Rewards"
  or "Early Mover Boosts" indefinitely despite low data credit burns,
  this indicates a fear-driven refusal to accept demand reality.

- **Incentive Overfitting Signal:** Launching broad "Bonus Programs"
  [@OnocoyBonus] without tying them to specific high-demand geographic
  zones suggests a "bribe" response to stop churn, likely attracting
  mercenary capital.

- **Narrative Pivot Signal:** If roadmap milestones shift from core
  "Rover Integration" and "RTK Adoption" to vague "AI Data Layer"
  promises without structural substance, it warns of a distraction
  capability.

- **Emergency Centralization Signal:** If the Foundation begins
  operating a significant percentage of reference stations to maintain
  coverage metrics, the network has entered a survival mode that
  suspends decentralization.

## Counterexamples, Edge Cases, and Deliberate Exclusions

The analytical framework presented in this thesis emphasizes comparative
robustness of DePIN tokenomic mechanisms under stress. As with any
applied modeling approach, its explanatory power depends on clearly
defined boundaries.

### Counterexample I: Demand-Dominant DePIN Regimes

A first class of counterexamples arises in DePINs that successfully
reach a demand-dominant regime, where exogenous usage growth overwhelms
tokenomic stress dynamics. In such cases, increasing service demand
drives burn mechanisms and provider revenue independently of short-term
incentive tuning. Under these conditions, archetypes like subsidy
inertia become less predictive. This distinction reinforces the thesis
scope: the analysis is designed for early-to-mid-stage DePINs operating
under demand uncertainty.

### Counterexample II: Structurally Centralized Networks

Networks relying on persistent organizational centralization for
incentive coordination are excluded by design. Their stability is
organizational rather than tokenomic, governed by administrative
authority rather than decentralized feedback loops.

### Excluded Archetypes and Metrics

**Governance Paralysis:** While common, this represents a failure to
respond rather than a stable archetype.\
**Speculative Reflexivity:** Dropped to avoid conflating price momentum
with infrastructure utility.\
**Excluded Metrics:** Raw token price and market cap were excluded due
to high volatility and weak interpretability under stress [@CFA2018].
The analysis prioritizes metrics like provider retention and utilization
efficiency.

# Appendix {#sec:appendix}
