# Zhang_Wang_Zheng_Cartlidge_2026_SystemicRiskInDeFi_NetworkBasedFragilityAnalysisOfTVLDynamics.pdf

## Page 1

Systemic Risk in DeFi: A Network-Based Fragility
Analysis of TVL Dynamics
Shiyu Zhang, Zining Wang, Jin Zheng and John Cartlidge
School of Engineering Mathematics and Technology
University of Bristol, Bristol, UK
{shiyu.zhang, zining.wang, jin.zheng, john.cartlidge}@bristol.ac.uk
Abstract—Systemic risk refers to the overall vulnerability
arising from the high degree of interconnectedness and interde-
pendence within the financial system. In the rapidly developing
decentralized finance (DeFi) ecosystem, numerous studies have
analyzed systemic risk through specific channels such as liquidity
pressures, leverage mechanisms, smart contract risks, and histor-
ical risk events. However, these studies are mostly event-driven
or focused on isolated risk channels, paying limited attention
to the structural dimension of systemic risk. Overall, this study
provides a unified quantitative framework for ecosystem-level
analysis and continuous monitoring of systemic risk in DeFi.
From a network-based perspective, this paper proposes the DeFi
Correlation Fragility Indicator (CFI), constructed from time-
varying correlation networks at the protocol category level. The
CFI captures ecosystem-wide structural fragility associated with
correlation concentration and increasing synchronicity. Further-
more, we define a Risk Contribution Score (RCS) to quantify
the marginal contribution of different protocol types to overall
systemic risk. By combining the CFI and RCS, the framework
enables both the tracking of time-varying systemic risk and
identification of structurally important functional modules in risk
accumulation and amplification.
Index Terms—Decentralized Finance (DeFi), Systemic Risk,
Correlation Networks, Financial Fragility, Network-Based Risk
Measurement
I. INTRODUCTION
Decentralized finance (DeFi) has developed rapidly in recent
years, evolving from a relatively isolated set of protocols
into an on-chain financial ecosystem with economic activity
reaching hundreds of billions of U.S. dollars at its peak, and
encompassing a wide range of financial functions [1]. As the
number of DeFi protocols grows and composability becomes
a defining design principle, interdependencies across different
protocols types have intensified [2], [3]. In this environment,
shocks originating from a single protocol or market segment
may propagate through shared collateral, common units of
account, and tightly coupled smart contracts, amplifying lo-
calized disturbances into system-wide stress [4]. Compared
with traditional financial systems, the programmable and com-
posable nature of DeFi renders these propagation channels
more explicit yet potentially more fragile, making systemic
risk particularly salient in this environment.
A large literature in traditional finance establishes that
systemic risk is fundamentally a network phenomenon, aris-
ing from patterns of interdependence rather than the size
of individual institutions [5], [6]. Correlation-based network
representations have been widely used to uncover latent market
structures and collective dynamics [7], and to develop quantita-
tive measures of interconnectedness and systemic risk [8], [9].
Subsequent work emphasizes that network topology, density,
and synchronization shape systemic vulnerability, showing that
increased connectivity can amplify fragility during stress peri-
ods [10], [11]. These insights motivate the use of structural and
time-varying network indicators for systemic risk monitoring.
As crypto-asset markets and DeFi have matured, systemic
risk research has increasingly extended to on-chain envi-
ronments [12]. Existing studies highlight several features
that distinguish DeFi from traditional systems and discuss
their impact on exacerbating systemic vulnerability, including
protocol composability [13], shared collateral and collateral
reuse [14], and automated liquidation mechanisms that create
endogenous feedback between prices and liquidations [15].
While this literature provides important insights into specific
risk mechanisms, it typically focuses on individual protocols,
assets, or crisis episodes, offering limited tools for unified and
time-consistent ecosystem-level risk measurement.
Related work applies network-based methods to study de-
pendence structures and shock propagation in crypto and DeFi
markets. Correlation and dependence networks constructed
from prices or on-chain activity reveal that interconnections
strengthen during stress periods, signaling elevated systemic
vulnerability [16]–[18]. Other studies construct explicit ex-
posure networks or simulate contagion through liquidation
cascades [19], [20]. Although these methods are valuable in
revealing specific risk transmission mechanisms, their analysis
often relies on scenario assumptions or model settings, focus-
ing more on local shocks or short-term propagation processes,
making them difficult to use for continuous and comparable
structural monitoring of systemic risk in DeFi.
Overall, the literature provides rich insights into the mecha-
nisms and transmission channels through which systemic risk
emerges in DeFi, yet remains fragmented in how such risks are
summarized and monitored at the ecosystem level. Most exist-
ing approaches focus on localized mechanisms, specific assets,
or crisis episodes, and therefore offer limited guidance on how
structural vulnerabilities accumulate and persist over time. In
particular, the literature lacks a measurement perspective that
treats systemic risk as a dynamic structural state—one that can
be tracked continuously, compared across market phases, and
decomposed across functional modules.
To address these limitations, we adopt a network-based
Page 1 of 9
arXiv:2601.08540v1  [q-fin.RM]  13 Jan 2026

---

## Page 2

perspective and conceptualize systemic risk in DeFi as a
structural state variable that evolves over time and can be con-
tinuously monitored at the ecosystem level. We construct time-
varying correlation networks at the protocol category level to
capture evolving interdependencies and synchronization across
functional modules, moving beyond scenario-driven or event-
specific analyzes. Based on these networks, we propose the
Correlation Fragility Indicator (CFI), which provides a time-
consistent and cross-period comparable measure of ecosystem-
wide structural vulnerability implied by increasing correlation
concentration and synchronization. To link system-level risk
measurement with its structural origins, we further intro-
duce the Risk Contribution Score (RCS), which decomposes
changes in systemic risk into marginal contributions from
functional modules, enabling structural attribution of risk
accumulation and amplification across the DeFi ecosystem.
The main contributions of this paper are:
•We propose a unified analytical framework that treats
systemic risk in DeFi as a structural and time-evolving
state variable for continuous ecosystem-level monitoring.
•We develop CFI, a time-consistent and cross-period com-
parable measure that captures ecosystem-wide structural
vulnerability arising from evolving dependency and syn-
chronization patterns.
•We propose the RCS, which structurally decomposes
system-level risk into marginal contributions of different
functional modules, providing a module-level attribution
of systemic risk.
•Using on-chain data, we conduct an empirical analysis
that documents the time-varying nature of systemic risk in
DeFi and identifies protocol categories that play a critical
role in risk accumulation and amplification.
Data and Code Availability.Data and code used in this study
are available in an anonymous GitHub repository for review. 1
II. DATA ANDPREPROCESSING
A. Data Source and Sample Construction
We construct a comprehensive dataset of Total Value Locked
(TVL) for the DeFi ecosystem using the public API provided
by DeFiLlama. 2 TVL measures the aggregate value of assets
deposited in DeFi protocols and is widely used as a core indi-
cator of capital allocation and economic activity. The raw data
consist of daily U.S. dollar–denominated TVL observations at
the protocol level, covering more than 5,000 DeFi protocols.
To analyze the structural evolution of the ecosystem, we
map each protocol to one of the standardized protocol types
provided by DeFiLlama (e.g.,Lending,DEX,Liquid Staking).
Protocols categorized asCEXandChainare excluded because
they do not represent DeFi-native activities. After filtering
and aggregation, the final dataset spans 2021-01-01 to 2025-
10-31 and comprises 70 protocol types. 3 For each category,
daily TVL is obtained by summing the TVL of all constituent
1https://github.com/defiresearchanonymous/defi-systemic-risk
2https://defillama.com
3https://defillama.com/categories
protocols, yielding a balanced panel in which each node
corresponds to a DeFi protocol type.
B. Data Cleaning and Anomaly Detection
Raw DeFi TVL data contain substantial irregularities due to
oracle disruptions, API glitches, contract upgrades, or tempo-
rary reporting errors. To mitigate such noise while preserving
true market dynamics, we apply a two-step anomaly detection
procedure based on relative and absolute daily TVL changes
and deviations from the median absolute deviation (MAD).
Specifically, an observation at timetis flagged as anomalous
if it satisfies any of the following conditions:
|∆TVLt|> τ abs,
TVLt
TVLt−1
−1
 > τrel,
|∆TVLt −median(∆TVL)|
MAD(∆TVL) > τMAD.
(1)
We setτ abs = 5million USD,τ rel = 200%, andτ MAD = 12.
In practice, 3.31% of protocol-day observations are flagged as
technical anomalies, typically corresponding to abrupt spikes
followed by immediate reversals, and are repaired via local
interpolation, whereas only 0.34% are classified as large,
persistent changes and retained as economically meaningful
liquidity shifts.
C. Return Construction and Winsorization
Following standard practice in financial time series analysis,
we construct daily log returns from category-level TVL:
ri,t = log (TVLi,t +ε)−log (TVL i,t−1 +ε),(2)
whereε= 10 −11 ensures numerical stability. Remaining
gaps are filled using forward and backward interpolation, and
returns are symmetrically winsorized at the 0.5% level to mit-
igate the undue influence of extreme observations. Categories
with zero return variance are excluded, yielding a balanced
panel of 70 categories. This processed return matrix serves as
the input for constructing dynamic correlation networks in the
subsequent analysis.
III. NETWORKCONSTRUCTION
A. Correlation Estimation
To capture cross-category dependence, we estimate corre-
lations based on daily TVL log returns, which proxy the
synchronization of capital flows in the DeFi ecosystem. How-
ever, direct sample correlations are often unstable in this
setting due to volatile on-chain activity, heterogeneous liquid-
ity across protocols, and the limited number of observations
available within each rolling window. We therefore employ the
Ledoit–Wolf shrinkage estimator [21], which is widely used
in high-dimensional financial return data [22], [23].
Letr i,t denote the log return of categoryion datet, and let
St be the sample covariance matrix computed over the rolling
window ending att. The shrinkage estimator is given by
ˆΣt = (1−λ t)St +λ tTt,(3)
Page 2 of 9

---

## Page 3

whereT t =µ tIis a scaled identity matrix, withIdenoting the
identity matrix andµ t equal to the average variance (i.e., the
mean diagonal element ofS t). The shrinkage intensityλ t ∈
[0,1]is selected to minimize expected mean-squared error. The
correlation matrix is then obtained by standard normalization
Cij,t =
ˆΣij,tq
ˆΣii,t ˆΣjj,t
.(4)
These shrinkage-based correlation matrices provide stable
and economically interpretable dependence estimates and form
the basis of our network analysis. Robustness to alternative
network specifications is examined in Section VI-A.
B. Rolling Window Framework
Empirical evidence suggests that dependence among DeFi
protocols is highly time-varying, driven by fluctuations in
user activity, liquidity migration, and market-wide shocks.
A single full-sample correlation matrix would obscure these
temporal dynamics and fail to capture periods of elevated
synchronization or structural breaks [24], [25].
To capture these dynamics, we adopt a rolling-window
estimation scheme, computing shrinkage correlation matrices
over overlapping windows of lengthW= 120days with a step
size of∆ = 7days. This choice, guided by sensitivity analysis,
balances smoothness and responsiveness, allowing the network
to track gradual expansions and contractions in connectivity
while remaining sensitive to sustained co-movement during
stress periods.
C. Network Definition
Given the shrinkage correlation matrixC t for each rolling win-
dow, we construct a weighted, undirected network to capture
co-movement among protocol types. For each window ending
at timet, letC ij,t denote the correlation between typesiand
j. We construct a weighted adjacency matrixA t = (w ij,t)
applying a monotone transformation of the correlations:
wij,t =|C ij,t|,(5)
for alli̸=j, andw ii,t = 0.
Using absolute correlations ensures that both positive and
negative co-movements are treated as potential channels of risk
transmission, consistent with systemic risk applications where
the magnitude of dependence is of primary interest [26]. The
resulting network is fully connected and weighted, allowing us
to retain the complete dependence structure among protocol
types types and avoiding arbitrary correlation thresholds that
may distort global network measures.
For transparency and robustness, we also consider thresh-
olded networks that retain only strong dependencies. These
networks are used for visualization and robustness analysis,
while all baseline systemic risk measures rely on the fully
connected weighted network. Fig. 1 shows a representative
snapshot, revealing a clear core–periphery structure: strong
dependencies cluster around major DeFi functions such as
lending and liquid staking, whereas peripheral types drop out
under thresholding. Notably, the persistent centrality of CDP
management and synthetic asset types highlights less obvious
but systemically important channels of interconnectedness.
IV. SYSTEM-LEVEL: CORRELATIONFRAGILITY
INDICATOR(CFI)
Here, we develop a network-based systemic risk indicator,
termed CFI, to capture the structural fragility of the DeFi
ecosystem. Unlike conventional risk measures centered on
returns [1], prices [2], or event-driven shocks [4], CFI quan-
tifies the evolving dependence structure embedded in time-
varying correlation networks. By construction, it reflects how
tightly coupled the ecosystem becomes, capturing persistent
co-movements in liquidity across protocol categories as mea-
sured by rolling-window correlation networks spanning several
weeks to months, rather than short-lived transitory shocks.
A. Network Metrics and Design Principles
To quantify structural fragility in correlation networks, we se-
lect four complementary metrics grounded in the spectral and
network analysis of financial correlation matrices. Together,
they capture key dimensions of dependence concentration
and diversification, including system-wide synchronization,
dominance of common factors, prevalence of extreme bilateral
linkages, and dispersion of the dependence spectrum [27].
This yields a parsimonious and economically interpretable
representation of correlation-network fragility.
First,average strengthsummarizes the overall intensity
of pairwise dependence across protocol types and captures
system-wide synchronization [28]:
¯st = 1
N
NX
i=1
X
j̸=i
wij,t.(6)
Second, themaximum eigenvalueof the weighted adjacency
correlation matrix captures the dominance of a common latent
factor in the dependence structure:
λmax,t = max{λk(At)}.(7)
In correlation-based financial networks, the largest eigenvalue
is commonly interpreted as a market-wide or systemic mode
reflecting collective behavior [29], [30].
Third,strong-edge densitymeasures the prevalence of un-
usually strong bilateral dependencies by computing the frac-
tion of correlations exceeding a given threshold:
dstrong
t = 1
N(N−1)
X
i̸=j
1{|Cij,t|> ρ}, ρ= 0.3,(8)
whereρ= 0.3reflects a conservative cutoff for economically
meaningful co-movements; robustness to alternative thresholds
is assessed in Section VI-B. This metric captures whether
strong co-movements form a tightly connected core, consistent
with filtered correlation-network approaches [31].
Page 3 of 9

---

## Page 4

Algo-Stables
Bridge
Bug Bounty
CDP
CDP Manager
Canonical Bridge
Charity Fundraising
Cross Chain Bridge
DCA Tools
DEX Aggregator
Decentralized BTC
Derivatives
Dexs
Dual-Token Stablecoin
Farm
Gaming
Governance Incentives
Indexes
Insurance
Launchpad
Lending
Leveraged Farming
Liquid Staking
Liquidations
Liquidity manager
Luck Games
NFT Lending
NFT Marketplace
Options
Options Vault
Partially Algorithmic Stablecoin
Payments
Ponzi
Prediction Market
Privacy
RWA
RWA Lending
Reserve Currency
Services
SoFi
Staking Pool
Synthetics
Uncollateralized Lending
Yield
Yield Aggregator
Yield Lottery
Bridge
Bug Bounty
CDP
CDP Manager
Canonical Bridge
Cross Chain Bridge
Decentralized BTCDexs
Dual-Token Stablecoin
Indexes
Insurance
Lending
Leveraged Farming
Liquid Staking
NFT Lending
NFT Marketplace
Payments
Prediction Market
Privacy
Services
Synthetics
Yield
Yield Aggregator
2
4
6
8
10
Node strength (sum of absolute correlations)
-1
0
1
Correlation (signed)
Fig. 1: DeFi correlation networks (snapshot at rolling-window end date: 11 May 2022). The left panel shows the fully weighted
correlation network constructed from category-level TVL log returns over the rolling window, where each edge weight equals
the absolute correlation|C ij|. The right panel shows the thresholded network retaining only edges with|C ij|>0.3to highlight
the core of strong dependencies. Node size is proportional to category-level TVL, node color denotes node strength (sum of
absolute correlations), edge color indicates signed correlation, and edge width reflects correlation magnitude.
Finally,eigenvalue entropysummarizes the dispersion of
the eigenvalue spectrum and provides a compact measure of
diversification in network dependence:
Ht =− 1
logN
NX
k=1
pk,t logp k,t, p k,t = λk,t
PN
j=1 λj,t
.(9)
Lower entropy indicates a more concentrated spectrum and
thus a more fragile dependence structure [32].
Taken together, higher average strength, a larger maximum
eigenvalue, greater strong-edge density, and lower eigenvalue
entropy consistently indicate a more tightly coupled and less
diversifiable correlation network.
B. Construction of the CFI
To summarize multiple dimensions of correlation-network
fragility into a single and interpretable measure, we construct
the DeFi CFI using Principal Component Analysis (PCA).
PCA-based aggregation of co-moving stress indicators is
standard in systemic risk measurement, most notably in the
construction of composite financial stress indices [33]. By de-
sign, the CFI captures the dominant common variation across
network metrics that reflect synchronization, concentration,
and diversification in the dependence structure.
Letx k,t denote metrick∈ {1, . . . ,4}at windowt. Each
metric is computed over a rolling window and assigned to
the corresponding window end date, so thatx k,t captures
the average structural properties of the correlation network
over that window rather than instantaneous fluctuations. Each
metric is then standardized to ensure comparability across
dimensions,
˜xk,t = xk,t −µ k
σk
,(10)
whereµ k andσ k are the sample mean and standard deviation
of metrick. Let ˜xt = (˜x1,t, . . . ,˜x4,t)⊤ collect the standardized
metrics. We then apply PCA to the covariance matrix of ˜xt
and define the CFI as the first principal component:
CFIt =w ⊤
1 ˜xt,(11)
wherew 1 is the eigenvector associated with the largest
eigenvalue. By construction, the CFI represents the dominant
common component underlying the four fragility dimensions.
The sign of the component is oriented such that higher
values correspond to stronger network-wide synchronization,
i.e., a positive association with average strength. To facilitate
interpretation and comparability across time and empirical
specifications, the resulting CFI series is subsequently stan-
dardized to have zero mean and unit variance.
Table I reports the PCA diagnostics underlying the construc-
tion of the CFI. The first principal component explains an over-
whelming share of the joint variation in the four standardized
metrics, and its loadings exhibit a coherent and economically
intuitive pattern: average strength, maximum eigenvalue, and
strong-edge density load positively, while eigenvalue entropy
loads negatively. This empirical structure confirms that the
CFI effectively aggregates the core dimensions of correlation-
network fragility into a single state variable.
C. Dynamics and Risk-Monitoring Relevance
Fig. 2 plots the standardized CFI over time. Each observation
corresponds to the end date of a rolling estimation window and
summarizes the dependence structure of the DeFi ecosystem
within that window. The CFI exhibits pronounced medium-
run variation and evolves smoothly across time, reflecting the
Page 4 of 9

---

## Page 5

TABLE I: PCA Diagnostics for the CFI Construction
PC1 loading PC1 variance share
Average strength0.5054
0.9673Maximum eigenvalue0.5052
Strong-edge density (|C ij |>0.3)0.4983
Eigenvalue entropy−0.4909
2022 2023 2024 2025 2026
Date
1
0
1
2
CFI (standard deviations)
CFI (PC1, standardized)
Fig. 2: Time series of the standardized DeFi CFI based on
rolling correlation networks of category-level TVL log returns.
The series is oriented so that higher values indicate stronger
network-wide synchronization and higher structural fragility.
gradual accumulation and release of structural dependence in
the correlation network. This smooth evolution is consistent
with the interpretation of the CFI as a structural state variable
capturing persistent shifts in ecosystem-wide synchronization,
rather than high-frequency market fluctuations.
To assess whether the CFI tracks contemporaneous systemic
conditions, we relate it to a set of realized risk proxies via,
Riskt =α+βCFI t +γ ⊤Zt +ε t,(12)
where Riskt denotes a contemporaneous risk proxy andZ t in-
cludes standard market controls. While the CFI is constructed
using a 120-day rolling window, the dependent variables are
measured over shorter horizons to reflect realized risk condi-
tions at the same time. Inference is based on heteroskedasticity
and autocorrelation consistent (HAC) standard errors.
Table II shows that the CFI is not significantly associated
with contemporaneous ETH volatility once controls are in-
cluded, indicating that it does not merely proxy short-term
price-based risk. In contrast, the CFI is positively associated
with rolling aggregate TVL volatility, suggesting that peri-
ods of elevated correlation fragility coincide with heightened
system-wide liquidity instability. Overall, the results highlight
the distinct informational content of the CFI as a network-
based structural indicator, capturing dimensions of systemic
vulnerability not fully reflected in asset price dynamics.
To assess whether the CFI contains forward-looking in-
formation beyond contemporaneous conditions, we conduct
a lightweight predictive check relating the CFI to future
realized volatility of aggregate TVL growth. For horizons
h∈ {7,14,30}, we estimate
V (h)
t =α h +β h CFIt +δ h V (h)
t−1 +γ ⊤
h Zt +ε t,h,(13)
whereV (h)
t denotes the realized volatility of aggregate TVL
log growth over the nexthdays. The control vectorZ t
TABLE II: Risk Monitoring Regressions: Contemporaneous
Systemic Conditions
(1) (2)
ETH V olatilityt TVL V olatilityt
CFIt −0.026 0.0020 *
(0.060) (0.0011)
ETH V olatilityt (control)1.574 ** 0.0069
(0.707) (0.0095)
BTC Return t −2.199*
(1.245)
Gas Fee t −18.348 0.338
(12.219) (0.219)
Constant0.307 *** 0.0224***
(0.076) (0.0017)
Observations 236 240
R2 0.138 0.044
HAC SE Yes Yes
Notes: Dependent variables capture contemporaneous systemic
conditions. ETH volatility is annualized 30-day realized volatil-
ity of ETH returns; TVL volatility is the 30-day rolling
volatility of aggregate TVL growth. CFI is the standardized
DeFi Correlation Fragility Indicator constructed from correla-
tion networks estimated over a 120-day rolling window and
evaluated at the window end date. All regressions use HAC
standard errors. ***, **, and * denote statistical significance at
the 1%, 5%, and 10% levels, respectively.
includes standard market controls, and inference uses HAC
standard errors with Newey–West lag length set to2h.
We find that the CFI is positive and statistically significant
across horizons, even after controlling for volatility persis-
tence. The estimated coefficients ˆβh are0.0028(h= 7),
0.0017(h= 14), and0.0010(h= 30), all significant at the
1% level withn= 239observations. These results indicate
that elevated correlation fragility precedes increases in system-
wide liquidity instability, supporting the CFI as a slow-moving
structural state variable rather than a purely contemporaneous
risk proxy.
V. NODE-LEVEL: RISKCONTRIBUTIONSCORE(RCS)
While CFI summarizes ecosystem-wide synchronization and
structural fragility, it does not reveal how this fragility is
distributed across protocol categories. For risk monitoring
and stress testing, identifying structurally important nodes is
therefore essential. This section moves from the network level
to the node level and introduces RCS, a counterfactual measure
of each category’s marginal contribution to the overall CFI.
A. Definition of RCS
LetC(·)denote the fixed CFI mapping established in Sec-
tion IV-B, which transforms a network snapshot into the scalar
CFI using (i) the same four network metrics, (ii) the same
standardization constants(µ k, σk), and (iii) the same PCA
loading vectorw 1 estimated once in the main pipeline.
For each nodei∈ {1, . . . , N}, define the counterfactual
network obtained by removing nodei(and all incident edges)
from the window-tnetwork:
A(−i)
t ∈R (N−1)×(N−1) .(14)
Page 5 of 9

---

## Page 6

0.00 0.02 0.04
Average RCS Score
Liquid Staking
Insurance
Token Locker
Privacy
Indexes
AI Agents
Lending
NFT Marketplace
Liquid Restaking
Restaking
0.055
0.053
0.048
0.047
0.047
0.044
0.043
0.037
0.036
0.035
(a) Top-10 protocol categories
ranked by average RCS.
0 50 100 150
Occurrence Count
Liquid Staking
Insurance
Privacy
Indexes
NFT Marketplace
CDP Manager
Token Locker
Liquid Restaking
CDP
Lending
176
173
148
136
113
111
102
98
95
89
(b) Appearance frequency of top-
10 RCS rankings.
Fig. 3: Systemically important protocol categories based on
RCS. Panel (a) ranks protocol types by their average marginal
contribution to system-wide fragility. Panel (b) reports the
frequency with which each category appears in the top-10 RCS
ranking across rolling windows.
We compute the counterfactual fragility state as
CFI(−i)
t ≡ C

A(−i)
t

,(15)
using the same fixed mappingC(·)to ensure comparability
acrossiand acrosst.
We define the node-level RCS as the marginal contribution
of nodeito system-wide fragility:
RCSi,t ≡CFI t −CFI (−i)
t .(16)
Under our sign convention,RCS i,t >0means that removing
categoryireduces the CFI, implying that categoryiincreases
ecosystem-wide synchronization and fragility in windowt.
Conversely,RCS i,t <0indicates a stabilizing role.
For scale-free comparisons across system states, we also
report
RCSrel
i,t = RCSi,t
|CFIt|+ε ,(17)
whereε >0is a small constant to avoid division by zero.
To produce stable rankings, we aggregate RCS over time:
RCSi = 1
|T |
X
t∈T
RCSi,t.(18)
We also compute a high-fragility ranking focusing on windows
in the upper tail of the CFI distribution:
RCSHigh
i = 1
|THigh|
X
t∈THigh
RCSi,t,
THigh ={t: CFI t ≥q 0.75(CFI)}.
(19)
B. Empirical Properties and Rankings
We next examine the identity and stability of systemically
important protocol categories using the RCS.
Fig. 3a ranks protocol types by their time-averaged RCS
(Eq. 18), capturing their average marginal contribution to
system-wide fragility. Several economically central categories
consistently emerge as highly important, yet these need not be
TABLE III: Structural Importance versus Economic Scale
Category Rank RCS RankTVL RankRCS, High
Liquid Staking 1 3 1
Insurance 2 30 3
Token Locker 3 28 4
Privacy 4 27 6
Indexes 5 20 8
AI Agents 6 35 14
Lending 7 1 10
NFT Marketplace 8 39 5
Liquid Restaking 9 10 2
Restaking 10 5 13
the largest by TVL (see TABLE III), underscoring that node-
level systemic importance is driven by dependence structure
rather than economic size. Fig. 3b complements this static
ranking by reporting how frequently each protocol type ap-
pears in the top-10 RCS ranking across rolling windows. High
re-occurrence frequencies indicate that systemic importance is
a persistent structural feature rather than a transient artifact
of short-lived shocks. Taken together, the two panels provide
a joint characterization of node-level systemic importance in
terms of both magnitude and temporal stability.
Finally, we test whether structural importance simply prox-
ies for economic scale. Table III compares the top-10 cate-
gories by RCS with their TVL ranks and their ranks under
high-fragility conditions (Eq. 19). The divergence between
RCS-based ranks and TVL ranks indicates that systemic
importance is not reducible to balance-sheet size. Moreover,
the high-fragility ranking highlights state-dependence: stress
episodes reshape the hierarchy of importance rather than
uniformly amplifying existing ranks.
C. Attack Tests: Counterfactual De-Risking via Targeted Node
Removal
The RCS is designed to identify protocol types that most sus-
tain ecosystem-wide fragility. We validate this interpretation
via counterfactual attack tests that quantify how much fragility
can be reduced by removing a small number of categories.
For each rolling windowt, we removek∈ {1,3,5,10}
nodes and recompute the CFI using the same fixed mapping
C(·). The de-risking effect is defined as
∆CFIt(k) = CFI full
t −CFI (−k)
t ,(20)
whereCFI (−k)
t denotes the CFI after removingknodes.
We compare three removal rules: (i)Targeted, removing
the top-kcategories by date-specific RCS; (ii)Strength-based,
removing the top-kcategories by node strength; and (iii)
Random, removingkcategories uniformly at random (Monte
Carlo). Fig. 4 shows that targeted removal produces substan-
tially larger reductions in CFI than random removal across all
k, and the gap widens withk. Table IV summarizes average
effects and quantifies this excess de-risking impact through the
Targeted−Random difference.
Finally, we repeat the attack tests by across rolling windows,
conditioning on system state by splitting the sample into high-
Page 6 of 9

---

## Page 7

1 3 5 10
Number of Removed Nodes (k)
0.00
0.25
0.50
0.75
1.00
1.25RCS Drop (ΔSRI)
Targeted (RCS)
Strength-based
Random (Mean)
Random 95% CI
Fig. 4: Attack curves: average CFI drop after removingk
nodes under targeted (RCS-based), strength-based, and random
removal (random: 95% interval across dates).
TABLE IV: Attack Test Summary: Mean CFI Drop by Re-
moval Sizek
kTargeted (RCS) Strength Random Targeted−Random
1 0.122 0.116 0.017 0.106
3 0.351 0.336 0.050 0.302
5 0.568 0.550 0.082 0.486
10 1.072 1.042 0.157 0.916
Notes.∆CFI t(k) = CFI full
t −CFI (−k)
t . Targeted removes the top-k
categories by date-specific RCS. Strength removes the top-kcategories by
node strength. Random reports the Monte Carlo mean across dates.
and low-fragility regimes defined by the top and bottom 20%
of the CFI distribution (48 windows each). Fig. 5 shows that
targeted removal is markedly more effective in high-fragility
windows consistent with the interpretation that stressed states
are more sensitive to targeted de-risking.
Overall, the RCS provides a structural decomposition of
ecosystem-wide fragility by identifying protocol types whose
position in the dependence network sustains high CFI states.
Empirically, structurally important categories are not necessar-
ily the largest by TVL, and targeted removal based on RCS
yields substantially larger counterfactual fragility reductions
than random removal, especially during high-fragility regimes.
These findings support the use of RCS as a node-level tool for
structural stress testing and scenario analysis that complements
the system-level perspective offered by the CFI.
VI. ROBUSTNESSANALYSIS
This section examines the robustness of the proposed network-
based fragility measures to alternative modeling choices. We
focus on two dimensions that are most likely to affect infer-
ence in correlation-network settings: (i) dependence estimation
methods, and (ii) metric construction and threshold choices.
A. Alternative Network Specifications
We first assess robustness to alternative dependence estimators.
In addition to the baseline Ledoit–Wolf shrinkage correlation,
1 3 5 10
Number of Removed Nodes (k)
0.00
0.25
0.50
0.75
1.00
1.25RCS Drop (ΔSRI)
High-risk: Targeted
High-risk: Random
Low-risk: Targeted
Low-risk: Random
Fig. 5: Attack curves in high-fragility vs. low-fragility regimes
(defined by top/bottom CFI quantiles). Targeted removal is
markedly more effective in high-fragility states.
we re-estimate rolling networks using sample Pearson correla-
tions and partial correlations estimated via Graphical LASSO.
Fig. 6 compares the standardized time series of the pri-
mary co-movement proxy across the three specifications. The
shrinkage- and sample-correlation measures exhibit highly
synchronized dynamics throughout the sample, confirming
that aggregate synchronization is not driven by the specific
correlation estimator. By contrast, the Glasso-based (partial-
correlation) proxy deviates substantially from correlation-
based measures. This divergence is expected: partial correla-
tions remove common market-wide components and therefore
capture conditional linkages rather than overall synchroniza-
tion. Consequently, partial-correlation networks provide com-
plementary structural information but are not substitutes for
correlation-based systemic fragility indicators.
B. Threshold Sensitivity
Finally, we assess sensitivity to the correlation cutoff used to
define strong edges in the strong-edge density metric. We re-
compute strong-edge density using|ρ|>0.25,0.30(baseline),
and0.35. Fig. 7 shows that the resulting standardized series are
highly stable across these reasonable choices, implying that the
timing and relative intensity of identified high-fragility periods
are not driven by an arbitrary threshold.
Taken together, these robustness checks confirm that the
main conclusions are not driven by a particular estimator, node
universe definition, or ad hoc parameter setting. Instead, they
reflect persistent and economically meaningful changes in the
evolving correlation structure of the DeFi ecosystem.
VII. DISCUSSION
This paper studies systemic risk in decentralized finance from
a network perspective, focusing on the evolving dependence
structure across protocol types. The proposed CFI captures a
dimension of systemic risk that is structural rather than price-
based. Empirically, the CFI is weakly related to asset-level
Page 7 of 9

---

## Page 8

2021-072022-012022-072023-012023-072024-012024-072025-012025-072026-01
Window End Date
−2
−1
0
1
2
Standardized Index (Z-score)
Shrinkage Correlation
Sample Pearson Correlation
GLASSO Partial Correlation
Fig. 6: Alternative network specifications: standardized co-
movement proxy. The figure compares z-scored co-movement
proxies based on shrinkage correlation, sample Pearson corre-
lation, and Graphical LASSO partial-correlations. Shrinkage-
and sample-based measures track each other closely, while
the Glasso-based proxy differs due to its focus on conditional
dependence.
volatility, yet closely aligned with instability in aggregate liq-
uidity. This distinction highlights that network fragility reflects
synchronization and loss of diversification across functional
modules, rather than short-term market fluctuations.
The dynamics of the CFI suggest that systemic vulnerability
in DeFi accumulates gradually through endogenous synchro-
nization. High-fragility states are persistent and coincide with
increasing concentration in network dependence, supporting
the view that systemic risk emerges as a slow-moving struc-
tural condition rather than only as a response to discrete
shocks. This highlights the value of network-based indicators
for continuous risk monitoring, complementing event-driven
analyses commonly used in the literature.
At the node level, the RCS shows that systemic importance
is not determined by economic size. Protocol categories that
sustain high-fragility states are often structurally central in the
dependence network despite modest TVL. Moreover, height-
ened systemic risk is associated with greater participation in
synchronized behavior than concentration in a small core,
underscoring the ecosystem-wide nature of fragility in DeFi.
Finally, counterfactual attack tests demonstrate that RCS-
based targeted removal yields significantly larger reductions in
system-level fragility than random interventions, particularly
during high-fragility regimes. In conclusion, these results
emphasize that systemic risk in DeFi is best understood as a
structural network phenomenon, for which the CFI and RCS
provide complementary tools for monitoring and stress testing.
VIII. CONCLUSION
This paper develops a network-based framework to measure
systemic risk in decentralized finance using time-varying
correlation networks from category-level TVL dynamics. We
introduce the CFI as a measure of ecosystem-wide structural
2022 2023 2024 2025 2026
Window End Date
−1
0
1
2
Standardized Density (Z-score)
|ρ| > 0.25
|ρ| > 0.30
|ρ| > 0.35
Fig. 7: Threshold sensitivity of strong-edge density under
alternative correlation cutoffs (|ρ|>0.25,0.30,0.35). The
strong-edge density dynamics remain stable across thresholds.
vulnerability, and the RCS to decompose this vulnerability
across protocol types based on marginal structural impact.
Empirically, the framework reveals that systemic fragility in
DeFi is driven by the gradual synchronization of dependence
structures rather than short-term price volatility. Periods of
elevated CFI coincide with increased instability in aggregate
liquidity, even when market volatility remains subdued. At
the node level, systemically important protocol categories are
identified not by economic size but by their persistent struc-
tural positioning within the correlation network, highlighting
a distinction between large and systemically important actors.
By linking network-level fragility with node-level contri-
butions, the proposed framework provides a coherent and
interpretable tool for monitoring systemic risk in DeFi. More
broadly, the results underscore the importance of structural
dependence as a channel of systemic risk in decentralized
markets, with implications for risk management, protocol
design, and macroprudential oversight.
Several avenues for future research and application emerge
naturally. One extension is to compare the CFI with established
connectedness measures from the financial econometrics lit-
erature, to contrast correlation-based network fragility with
alternative, model-based notions of systemic connectedness.
Extending the framework to high-frequency data and incorpo-
rating cross-chain bridge activity would also help character-
ize the propagation of systemic risk across rapidly evolving
blockchain ecosystems. From a practical perspective, the CFI
and RCS provide a blueprint for DeFi-native macropruden-
tial tools that adjust risk parameters in response to elevated
systemic connectivity.
ACKNOWLEDGMENT
SZ’s PhD is funded by a China Scholarship Council/University
of Bristol joint scholarship, No. 202410320012. JC is partly
funded by UK Research and Innovation (UKRI) Engineering
and Physical Sciences Research Council (EPSRC) [grant num-
ber EP/Y028392/1]: AI for Collective Intelligence (AI4CI).
Page 8 of 9

---

## Page 9

The authors acknowledge the use of generative AI for
manuscript development. Specifically, ChatGPT-5 (OpenAI)
was used for editing and grammar enhancement. All content
generated by the AI was reviewed, edited, and verified for
accuracy by the human authors.
REFERENCES
[1] J. C. Le ´on and A. Lehar, “What data have told us about decentralized
finance,”Journal of Corporate Finance, p. 102916, 2025. [Online].
Available: https://doi.org/10.1016/j.jcorpfin.2025.102916
[2] F. Sch ¨ar, “Decentralized finance: On blockchain-and smart contract-
based financial markets,”Federal Reserve Bank of St. Louis
Review, vol. 103, no. 2, pp. 153–174, 2021. [Online]. Available:
https://dx.doi.org/10.20955/r.103.153-74
[3] S. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and
W. Knottenbelt, “Sok: Decentralized finance (DeFi),” inProceedings of
the 4th ACM Conference on Advances in Financial Technologies, 2022,
pp. 30–46. [Online]. Available: https://dl.acm.org/doi/abs/10.1145/355
8535.3559780
[4] Financial Stability Board, “The financial stability risks of decentralised
finance,” Financial Stability Board: Basel, Switzerland, Tech. Rep., 16
Feb 2023. [Online]. Available: https://www.fsb.org/uploads/P160223.pdf
[5] A. G. Haldane and R. M. May, “Systemic risk in banking ecosystems,”
Nature, vol. 469, no. 7330, pp. 351–355, 2011. [Online]. Available:
https://doi.org/10.1038/nature09659
[6] M. Bardoscia, S. Battiston, F. Caccioli, and G. Caldarelli, “Pathways
towards instability in financial networks,”Nature Communications,
vol. 8, no. 1, p. 14416, 2017. [Online]. Available: https://doi.org/10.1
038/ncomms14416
[7] R. N. Mantegna, “Hierarchical structure in financial markets,”
The European Physical Journal B-Condensed Matter and Complex
Systems, vol. 11, no. 1, pp. 193–197, 1999. [Online]. Available:
https://doi.org/10.1007/s100510050929
[8] M. Billio, M. Getmansky, A. W. Lo, and L. Pelizzon, “Econometric
measures of connectedness and systemic risk in the finance and
insurance sectors,”Journal of Financial Economics, vol. 104, no. 3,
pp. 535–559, 2012. [Online]. Available: https://doi.org/10.1016/j.jfinec
o.2011.12.010
[9] F. X. Diebold and K. Yılmaz, “On the network topology of variance
decompositions: Measuring the connectedness of financial firms,”
Journal of Econometrics, vol. 182, no. 1, pp. 119–134, 2014. [Online].
Available: https://doi.org/10.1016/j.jeconom.2014.04.012
[10] D. Acemoglu, A. Ozdaglar, and A. Tahbaz-Salehi, “Systemic
risk and stability in financial networks,”American Economic
Review, vol. 105, no. 2, pp. 564–608, 2015. [Online]. Available:
https://doi.org/10.1257/aer.20130456
[11] S. Battiston, M. Puliga, R. Kaushik, P. Tasca, and G. Caldarelli,
“DebtRank: Too central to fail? Financial networks, the FED and
systemic risk,”Scientific Reports, vol. 2, no. 1, p. 541, 2012. [Online].
Available: https://doi.org/10.1038/srep00541
[12] M. Aquilina, G. Cornelli, J. Frost, and L. Gambacorta, “Cryptocurrencies
and decentralised finance: functions and financial stability implications,”
Bank for International Settlements, BIS Papers 156, Apr 2025. [Online].
Available: https://www.bis.org/publ/bppdf/bispap156.pdf
[13] S. Kitzler, F. Victor, P. Saggese, and B. Haslhofer, “Disentangling
decentralized finance (DeFi) compositions,”ACM Transactions on
the Web, vol. 17, no. 2, pp. 1–26, 2023. [Online]. Available:
https://doi.org/10.1145/3532857
[14] K. Qin, L. Zhou, B. Livshits, and A. Gervais, “Attacking the
DeFi ecosystem with flash loans for fun and profit,” inFinancial
Cryptography and Data Security. FC21. Lecture Notes in Computer
Science. Berlin: Springer, 2021, vol. 12674, pp. 3–32. [Online].
Available: https://doi.org/10.1007/978-3-662-64322-8 1
[15] R. Auer and S. Claessens, “Regulating cryptocurrencies: assessing
market reactions,” Bank for International Settlements, BIS Quarterly
Review, Sep 2018.
[16] M. Fakhfekh, A. Bejaoui, A. F. Bariviera, and A. Jeribi, “Dependence
structure between NFT, DeFi and cryptocurrencies in turbulent times:
An archimax copula approach,”The North American Journal of
Economics and Finance, vol. 70, p. 102079, 2024. [Online]. Available:
https://doi.org/10.1016/j.najef.2024.102079
[17] X. Feng, M. Yu, T. Yan, J. Lin, and C. J. Tessone, “Research on the
time-varying network topology characteristics of cryptocurrencies on
Uniswap v3,”Electronics, vol. 14, no. 12, p. 2444, 2025. [Online].
Available: https://doi.org/10.3390/electronics14122444
[18] T. Yan and C. J. Tessone, “Network analysis of Uniswap: Centralization
and fragility in the decentralized exchange market,” inProceedings of
Blockchain Kaigi 2024 (BCK24). Physical Society of Japan, 2025, p.
011013. [Online]. Available: https://journals.jps.jp/doi/abs/10.7566/JP
SCP.44.011013
[19] W. Wu, K. Qian, A. Lui, C. Jack, Y . Wu, P. McBurney, F. He, and
B. Zhang, “DeXposure: A dataset and benchmarks for inter-protocol
credit exposure in decentralized financial networks,” 2025. [Online].
Available: https://arxiv.org/abs/2511.22314
[20] N. Tovanich, M. Kassoul, S. Weidenholzer, and J. Prat, “Contagion
in decentralized lending protocols: A case study of compound,” in
Proceedings of the 2023 Workshop on Decentralized Finance and
Security, 2023, pp. 55–63. [Online]. Available: https://dl.acm.org/doi/a
bs/10.1145/3605768.3623544
[21] O. Ledoit and M. Wolf, “A well-conditioned estimator for large-
dimensional covariance matrices,”Journal of Multivariate Analysis,
vol. 88, no. 2, pp. 365–411, 2004. [Online]. Available: https:
//doi.org/10.1016/S0047-259X(03)00096-4
[22] V . DeMiguel, L. Garlappi, and R. Uppal, “Optimal versus naive
diversification: How inefficient is the 1/n portfolio strategy?”The
Review of Financial Studies, vol. 22, no. 5, pp. 1915–1953, 2009.
[Online]. Available: https://doi.org/10.1093/rfs/hhm075
[23] O. Ledoit and M. Wolf, “Nonlinear shrinkage of the covariance matrix
for portfolio selection: Markowitz meets Goldilocks,”The Review of
Financial Studies, vol. 30, no. 12, pp. 4349–4388, 2017. [Online].
Available: https://doi.org/10.1093/rfs/hhx052
[24] R. Engle, “Dynamic conditional correlation: A simple class of
multivariate generalized autoregressive conditional heteroskedasticity
models,”Journal of Business & Economic Statistics, vol. 20, no. 3, pp.
339–350, 2002. [Online]. Available: https://doi.org/10.1198/07350010
2288618487
[25] K. J. Forbes and R. Rigobon, “No contagion, only interdependence:
measuring stock market comovements,”The Journal of Finance,
vol. 57, no. 5, pp. 2223–2261, 2002. [Online]. Available: https:
//doi.org/10.1111/0022-1082.00494
[26] J.-P. Onnela, A. Chakraborti, K. Kaski, J. Kertesz, and A. Kanto,
“Dynamics of market correlations: Taxonomy and portfolio analysis,”
Physical Review E, vol. 68, no. 5, p. 056110, 2003. [Online]. Available:
https://doi.org/10.1103/PhysRevE.68.056110
[27] M. Tumminello, T. Di Matteo, T. Aste, and R. N. Mantegna, “Correlation
based networks of equity returns sampled at different time horizons,”
The European Physical Journal B, vol. 55, no. 2, pp. 209–217, 2007.
[Online]. Available: https://doi.org/10.1140/epjb/e2006-00414-4
[28] A. Barrat, M. Barthelemy, R. Pastor-Satorras, and A. Vespignani,
“The architecture of complex weighted networks,”Proceedings of the
National Academy of Sciences, vol. 101, no. 11, pp. 3747–3752, 2004.
[Online]. Available: https://doi.org/10.1073/pnas.0400087101
[29] L. Laloux, P. Cizeau, J.-P. Bouchaud, and M. Potters, “Noise dressing
of financial correlation matrices,”Physical Review Letters, vol. 83,
no. 7, p. 1467, 1999. [Online]. Available: https://doi.org/10.1103/Phys
RevLett.83.1467
[30] V . Plerou, P. Gopikrishnan, B. Rosenow, L. A. N. Amaral, T. Guhr,
and H. E. Stanley, “Random matrix approach to cross correlations in
financial data,”Physical Review E, vol. 65, no. 6, p. 066126, 2002.
[Online]. Available: https://doi.org/10.1103/PhysRevE.65.066126
[31] M. Tumminello, T. Aste, T. Di Matteo, and R. N. Mantegna, “A
tool for filtering information in complex systems,”Proceedings of the
National Academy of Sciences, vol. 102, no. 30, pp. 10 421–10 426,
2005. [Online]. Available: https://doi.org/10.1073/pnas.0500298102
[32] J. Kwapie ´n and S. Dro ˙zd˙z, “Physical approach to complex systems,”
Physics Reports, vol. 515, no. 3-4, pp. 115–226, 2012. [Online].
Available: https://doi.org/10.1016/j.physrep.2012.01.007
[33] D. Hollo, M. Kremer, and M. Lo Duca, “CISS – A composite
indicator of systemic stress in the financial system,” European
Central Bank, Working Paper Series 1426, 2012. [Online]. Available:
https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1426.pdf
Page 9 of 9

---
