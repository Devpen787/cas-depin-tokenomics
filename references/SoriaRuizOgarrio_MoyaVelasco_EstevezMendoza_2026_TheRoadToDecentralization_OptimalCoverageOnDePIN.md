# SoriaRuizOgarrio_MoyaVelasco_EstevezMendoza_2026_TheRoadToDecentralization_OptimalCoverageOnDePIN.pdf

## Page 1

 
Contents lists available at ScienceDirect
Finance Research Letters
journal homepage: www.elsevier.com/locate/frl  
The road to decentralization: Optimal coverage on Decentralized 
Physical Infrastructure Networks (DePIN)
Jorge Soria Ruiz-Ogarrio a
 , Jorge Moya Velasco b
 ,∗, Carlos Estévez-Mendoza c,d
a School of Economics and Business, Faculty of Economics and Business Science, University of Navarra, Edificio Amigos, c/ Universidad 
1, Pamplona, 31009, Navarra, Spain
b Departamento de Economía y Empresa, Facultad de Derecho, Empresa y Ciencias Políticas, Universidad Cardenal Herrera-CEU, CEU 
Universities, Carrer Lluís Vives 1, Alfara del Patriarca, 46115, Valencia, Spain
c Department of Management, Economics and Business Administration Faculty, Complutense University of Madrid, Campus de 
Somosaguas, Pozuelo de Alarcón, 28223, Madrid, Spain
d Department of Management, Faculty of Business, Economics and Law, CUNEF University, Almansa 101, Madrid, 28040, Madrid, Spain
A R T I C L E  I N F O
JEL classification:
L94
D83
O33
D85
Keywords:
Decentralized Physical Infrastructure Networks
Decentralization
DePIN
Infrastructure economics
Network externalities
Blockchain
Machine learning
Decentralized Autonomous Organization
 A B S T R A C T
Decentralized Physical Infrastructure Networks (DePIN) represent an emerging organizational 
form for operating physical infrastructure through blockchain-based coordination. DePIN 
through decentralized protocols and token-based payment mechanisms incentivize independent 
agents to deploy, maintain, and monetize real-world infrastructure, such as wireless networks, 
storage units, or sensors. This article presents a first formal economic analysis of DePIN 
architectures, modelling investment decisions under network effects in a blockchain-native 
Decentralized Autonomous Organization (DAO), with protocol-defined reward schemes. It 
establishes the equilibrium conditions that support decentralized provision, where token prices 
internalize participation, service reliability, and network coverage. Furthermore, it identifies 
a minimum viable coverage threshold determined by costs and network effects. Through a 
multi-agent machine learning simulation, we confirm that decentralized provision improves 
efficiency compared to centralized models. The results support the economic viability of DePIN 
and provide design guidelines for future decentralized infrastructure protocols. Finally, we 
propose a DAO incentive mechanism to implement First Best provision in Decentralized Physical 
Infrastructure Networks.
1. Introduction and literature review
Decentralized Physical Infrastructure Networks (DePIN) allow individual agents to contribute physical resources to a network 
organized and managed through blockchain protocols that use native tokens as payment. DePIN hold relevance for finance 
research as they illustrate how economic benefits can arise from the decentralized coordination and allocation of infrastructure 
resources (Surve and Khandelwal, 2023; Pereira et al., 2019). In contrast to the traditional centralized provisioning by large 
corporations, governments, or monopolies, DePIN redefine markets that traditionally pose high barriers to entry such as considerable 
initial costs or regulation. In this article, we study DePIN as a decentralized network-effects industrial organization model and analyse 
the financial implications of its implementation under various markets.
Beyond reviews on advantages of blockchain technology for decentralized allocation (Ali et al., 2021; Lage et al., 2022; Islam 
and Apu, 2024; Ahmed, 2025), the literature on Distributed Energy Resources (DER) in peer-to-peer microgrids (Boumaiza, 2024a,b; 
∗ Corresponding author.
E-mail addresses: jsoriar@unav.es (J. Soria Ruiz-Ogarrio), jorge.moyavelasco@uchceu.es (J. Moya Velasco), cestev01@ucm.es (C. Estévez-Mendoza).
https://doi.org/10.1016/j.frl.2025.109115
Received 20 August 2025; Received in revised form 22 October 2025; Accepted 25 November 2025
Finance Research Letters 90 (2026) 109115 
Available online 29 November 2025 
1544-6123/© 2025 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license 
( http://creativecommons.org/licenses/by/4.0/ ). 

---

## Page 2

J. Soria Ruiz-Ogarrio et al.
Dong et al., 2022) provides a descriptive background (Pop et al., 2018; Mezquita et al., 2022; Seven et al., 2020; Bhavana et al., 
2024; Thukral, 2021; Yap et al., 2023; Karumba et al., 2023), although it does not specifically address DePIN. Building on these 
antecedents, the literature on DePIN is limited and mostly descriptive (Zheng et al., 2025). Lin et al. (2025) and Liu and Omote 
(2025) provide an exploratory approach to the design, operation, market capitalization and challenges. The first adopts a technical 
approach, focusing on algorithms to strengthen security, reduce costs and improve scalability and privacy. The latter presents a 
consensus protocol using eIDs within blockchain to increase verifiability and traceability. Other works available in repositories 
reproduce a general framework (Ballandies et al., 2023; Sarkar, 2023) and examine the transitions toward decentralized autonomous 
machines (Castillo et al., 2025). Andrew and Ballandies (2025) outlines the boundaries between DePIN and traditional collaborative 
infrastructures methods, and Mao et al. (2025) studies computing-power DePIN.
Existing contributions in conferences examine vulnerabilities in resource sharing (Caprolu et al., 2025), solutions to improve 
scalability (Fan and Xu, 2024; Fan, 2024), and comparisons of decentralized models (von der Assen et al., 2024). The pre-print 
by Milionis et al. (2025) approaches a model to strengthen security, incorporating game theory to verify the level of service provided 
in DePIN.
This article contributes to the incipient finance research on DePIN by proposing a formal network-effects model, in the style 
of Economides and Himmelberg (2013), to formalize the economic mechanism underlying DePIN (Section 2). Using a multi-agent 
machine learning approach similar to that of Soria et al. (2023), we further simulate strategic interactions between producers and 
users across different markets (Section 3). The results support the model and provide insights into prices, network effects, coverage 
levels, and the incentives and costs of participation. In Section 4, we propose an incentive mechanism to implement socially optimal 
coverage through a DePIN Decentralized Autonomous Organization (DAO). Sections Appendix A to Appendix D include more detailed 
explanations of the situation of DePIN, mathematical proofs, the simulation results and a proposal of DAO mechanism to implement 
first-best outcomes under DePIN provision.
2. Foundations of DePIN and analytical model
A DePIN is composed of physical infrastructure nodes, such as sensors, wireless access points, storage or processing units. These 
are organized through blockchain-based protocols (e.g. Proof-of-Physical-Work), that verify and record contributions in a shared 
ledger (Liu and Omote, 2025; Almadani et al., 2023; Narayanan et al., 2016). DePIN should not be confused with Distributed Energy 
Resources (DER), which integrate smart devices to optimize distribution and consumption (Karumba et al., 2023; Maksymyuk et al., 
2020). Although these systems use blockchain for transaction traceability and monitoring (Yap et al., 2023; Seven et al., 2020; Wang 
et al., 2020), they operate within centralized or institutional architectures, without providing the full decentralization that DePIN 
enables.
A token is a digital asset that can be sold or used to acquire services (Treiblmaier, 2023; Tanveer et al., 2025). In DePIN, tokens 
are distributed proportionally to contributions to the network, according to variables such as quantity or quality provided by the 
node in a contribute-to-earn manner. Tokens incentivize participation, organize cooperation and optimize the operational efficiency 
of it (Treiblmaier, 2023).
In most protocols, tokens grant voting rights to participants in the governance of the DePIN network through Decentralized 
Autonomous Organizations (DAOs), which automate and validate the decision-making process using smart-contracts (John et al., 
2023; Cong and He, 2019). Fig.  1 summarizes this intersection between infrastructure, blockchain, Tokenomics and DePIN 
applications. More information on DePIN functioning in Appendix A. Appendix B presents a summary of the main projects shaping 
this ecosystem, along with an approximation of their capitalization.
Building on these basic operational specifications, we create a dynamic model that captures the functional aspects of a DePIN 
network.
Consider a world with discrete time periods 𝑡 = 0 , 1, 2, … and an infinite horizon with common discount factor 𝛿 ∈ [0 , 1). A 
continuum of users 𝑖 ∈ [0, 1] have valuations 𝑣𝑖,𝑡 independently drawn from distribution 𝐹 with density 𝑓 , continuous on [0, 1] and 
satisfying standard regularity conditions. This captures heterogeneity in preferences and reflects a realistic market with diverse 
demand. Formally, the continuum representation simplifies aggregation while modelling a market of many small, independent 
participants whose individual decisions collectively determine network coverage.
User utility exhibits network effects, meaning that it depends not only on individual consumption but also on the overall network 
coverage, so that a higher provision level increases the value of the service for all users (Katz and Shapiro, 1994). The more providers 
participate and the broader the coverage, the greater the perceived utility, as seen in communication networks, transport and other 
infrastructures. Utility is given by 
𝑢𝑡(𝑣𝑖,𝑡, 𝑁𝑡) = 𝑣𝑖,𝑡
( 𝜙 + 𝜂𝑁 𝛼
𝑡
) − 𝑝𝑡, (1)
where 𝜙 ≥ 0 represents the intrinsic value of the service in the absence of network effects (a higher 𝜙 implies weaker dependence on 
the network, while 𝜙 = 0 means the good derives value solely from network participation). The parameters 𝜂 > 0 and 𝛼 > 0 capture 
the strength and elasticity of the network effect, respectively, and 𝑁𝑡 ∈ [0, 1] denotes DePIN coverage at time 𝑡. Intuitively, 𝑁𝑡 can 
be understood as the share of total area or users effectively covered by the network—e.g., in a Wi-Fi DePIN, it would correspond 
to the percentage of locations with active service.
We assume 𝜂 > 0, meaning broader coverage increases perceived value. If growth causes congestion or overcrowding, the 
opposite effect (𝜂 < 0) may occur (Karhu et al., 2024; Liu et al., 2022). While our framework could accommodate such cases, 
Finance Research Letters 90 (2026) 109115 
2 

---

## Page 3

J. Soria Ruiz-Ogarrio et al.
Fig. 1. DePIN architecture and examples of applications.
the positive-network-effect assumption is more suitable for DePIN architectures, where additional nodes enhance service quality 
and reliability.
The restriction 𝛼 > 0 together with 𝑁𝑡 ∈ [0 , 1] is a modelling choice ensuring monotonicity of the externality. Allowing 𝛼 < 0
would invert the relationship (e.g., 𝜂∕𝑁 |𝛼|
𝑡 ), changing its interpretation but not the model itself.
A user buys iff 𝑣𝑖,𝑡 ≥ 𝑝𝑡
𝜙 + 𝜂𝑁 𝛼
𝑡
. Hence, market demand satisfies 
𝑄𝑡 = 1 − 𝐹
( 𝑝𝑡
𝜙 + 𝜂𝑁 𝛼
𝑡
)
(2)
Solving for price using the inverse cumulative distribution function gives the inverse demand 
𝑝(𝑄𝑡, 𝑁𝑡) = ( 𝜙 + 𝜂𝑁 𝛼
𝑡
) 𝐹 −1(1 − 𝑄𝑡) (3)
In fulfilled-expectations equilibrium, quantity demanded equals coverage, 𝑄𝑡 = 𝑁𝑡, and the equilibrium inverse demand is 
𝑝(𝑁𝑡, 𝑁𝑡) = ( 𝜙 + 𝜂𝑁 𝛼
𝑡
) 𝐹 −1(1 − 𝑁𝑡) (4)
Proposition 1 (Non-monotonic Price Under Strong Network Effects). Suppose 𝑓 (1) > 0 and 𝑓 (0) > 0. If either 𝛼 < 1 with 𝜂 > 0, or 𝛼 = 1
with 𝜂 > 𝜙 ∕𝑓 (1), then 𝑝(𝑁, 𝑁 ) is increasing for small 𝑁 and decreasing for 𝑁 near 1. Hence, there exists a unique 𝑁peak ∈ (0, 1) with 
𝑑𝑝(𝑁peak , 𝑁peak )
𝑑𝑁 = 0, 𝑝 max ∶= 𝑝(𝑁peak , 𝑁peak ) = max
𝑁∈[0,1]
𝑝(𝑁, 𝑁 ) (5)
Proof in Appendix C.1.
DePIN becomes relevant in markets that (a) present network effects and (b) are traditionally organized through by monopo-
lies/oligopolies. Let I∕𝐾 ≥ 0 denote a per-period fixed/entry cost that is paid only by the provider(s) (i.e. 𝐾𝑡 ≡ |||{ 𝑖 ∈  ∶ 𝑁𝑖,𝑡 > 0 }|||.). 
The analysis goes as follows: we first describe the optimal choice by a monopoly, followed by oligopolistic competition under Cournot 
competition, which is then used to calculate the perfect competition outcome as 𝐾 → ∞. Finally, we describe the Social Optimum. 
Section 3 simulates the results and Section 4 describes the mechanism to achieve the Social Optimum through a Decentralized 
Autonomous Organization (DAO) DePIN protocol.
Finance Research Letters 90 (2026) 109115 
3 

---

## Page 4

J. Soria Ruiz-Ogarrio et al.
Monopoly
The monopolist’s discounted expected profit is 
𝛱 𝑀 =
∞∑
𝑡=0
𝛿𝑡
[
𝑁𝑡 𝑝(𝑁𝑡, 𝑁𝑡) − 𝑐 𝑁𝑡 − I ⋅ 𝟏{𝑁𝑡 > 0}
]
(6)
The per-period static problem is 
max
𝑁≥0
𝛱(𝑁) = 𝑁 𝑝(𝑁, 𝑁 ) − 𝑐 𝑁 − I ⋅ 𝟏{𝑁 > 0} (7)
For an interior choice 𝑁 𝑀 > 0, the first-order condition (FOC) is 
𝑝(𝑁, 𝑁 ) + 𝑁 𝑑𝑝(𝑁, 𝑁 )
𝑑𝑁 − 𝑐 = 0 (8)
Writing 𝑞(𝑁) ∶= 𝐹 −1(1 − 𝑁), we have 𝑞′(𝑁) = −1∕ 𝑓 (𝑞(𝑁)) and thus 
𝑑𝑝(𝑁, 𝑁 )
𝑑𝑁 = 𝜂𝛼𝑁 𝛼−1 𝑞(𝑁) − 𝜙 + 𝜂𝑁 𝛼
𝑓( 𝑞(𝑁)) (9)
Monopoly produces on the decreasing par of 𝑝(𝑁, 𝑁 ), where 𝑑𝑝(𝑁,𝑁 )
𝑑𝑁 < 0, and must cover I). If the monopoly chooses an interior 
𝑁 ∗ > 0, then 𝑑𝑝(𝑁 ∗, 𝑁∗)
𝑑𝑁 < 0 and 𝑁 ∗[ 𝑝(𝑁 ∗, 𝑁∗) − 𝑐] ≥ I. The profit with 𝑁 > 0 is 𝛱(𝑁) = 𝑁[𝑝(𝑁, 𝑁 ) − 𝑐] − I. Interior 
optimality requires 𝛱(𝑁 𝑀 ) ≥ 0, so by incentive compatibility 𝑁 𝑀 [𝑝(𝑁 𝑀 , 𝑁𝑀 ) − 𝑐] ≥ I, implying 𝑝(𝑁 𝑀 , 𝑁𝑀 ) − 𝑐 > 0. From 
(8), 𝑁 𝑀 𝑑𝑝
𝑑𝑁 = 𝑐 − 𝑝(𝑁 ∗, 𝑁∗) < 0, hence 𝑑𝑝
𝑑𝑁 < 0.
Proposition 2 (Minimum Active Coverage Under Fixed Cost). If 𝑝(𝑁, 𝑁 ) is non-monotone with unique peak at 𝑁peak, then the minimum 
coverage at which a monopoly can be active is 
𝑁min = inf
{
𝑁 ≥ 𝑁peak ∶ 𝑁[ 𝑝(𝑁, 𝑁 ) − 𝑐] ≥ I
}
(10)
Proof in Appendix C.2.
Proposition  2 implies that there is a minimum critical mass for provision of coverage that depends on 𝜙, 𝜂, 𝛼 and the distribution 
of valuations (𝐹 (𝑣).
Oligopoly (Cournot)
Let 𝐾𝑡 be the number of providers and 𝑛𝑗,𝑡 the coverage of provider 𝑗, so 𝑁𝑡 = ∑𝐾𝑡
𝑗=1 𝑛𝑗,𝑡 . With per-period fixed cost 𝐈𝐭 ∶= I∕𝐾𝑡
when active, a provider’s discounted value is 
max
{𝑛𝑗,𝑡 ≥0}
∞∑
𝑡=0
𝛿𝑡
[
𝑛𝑗,𝑡 𝑝(𝑁𝑡, 𝑁𝑡) − 𝑐 𝑛𝑗,𝑡 − 𝐈 ⋅ 𝟏{𝑛𝑗,𝑡 > 0}
]
(11)
In the static Cournot stage and for interior choices, the FOC is 
𝜕
𝜕𝑛𝑗,𝑡
[
𝑛𝑗,𝑡
( 𝑝(𝑁𝑡, 𝑁𝑡) − 𝑐) ]
= 𝑝(𝑁𝑡, 𝑁𝑡) − 𝑐 + 𝑛𝑗,𝑡
𝑑𝑝(𝑁𝑡, 𝑁𝑡)
𝑑𝑁𝑡
⋅ 𝜕𝑁𝑡
𝜕𝑛𝑗,𝑡
= 0 , (12)
where 𝜕𝑁𝑡
𝜕𝑛𝑗,𝑡
= 1. In a symmetric equilibrium 𝑛𝑗,𝑡 = 𝑁𝑡∕𝐾𝑡, so 
𝑝(𝑁𝑡, 𝑁𝑡)
⏟ ⏞⏞ ⏟ ⏞⏞ ⏟
Competitive price
+ 𝑁𝑡
𝐾𝑡
𝑑𝑝(𝑁𝑡, 𝑁𝑡)
𝑑𝑁𝑡
⏟⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏟
Markup
= 𝑐 (13)
DePIN lowers technological and organizational barriers to entry by modularizing coverage into micro-nodes and by allowing 
users to be producers. It reduces the effective per-node scale required to operate, spreads the per-period activity cost 𝐈, and (iii) 
coordinates entry via token-based rewards.
Proposition 3 (Competitive Limit). Along any sequence of symmetric Cournot equilibria with 𝐾𝑡 → ∞, the limiting coverage 𝑁 𝐶 satisfies 
𝑝(𝑁 𝐶 , 𝑁𝐶 ) = 𝑐 (14)
Proof.  Taking 𝐾𝑡 → ∞ in (13) drives the markup term 𝑁𝑡
𝐾𝑡
𝑑𝑝
𝑑𝑁𝑡
 to zero, yielding 𝑝(𝑁 ∞, 𝑁∞) = 𝑐. □
and as the number of providers 𝐾 rises, the markup term vanishes and the outcome converges to the competitive condition 
𝑝(𝑁, 𝑁 ) = 𝑐.
Finance Research Letters 90 (2026) 109115 
4 

---

## Page 5

J. Soria Ruiz-Ogarrio et al.
Proposition 4 (Multiplicity of Equilibria in the Fulfilled Coverage Levels). If 𝑝(𝑁, 𝑁 ) is non-monotone with unique peak 𝑝max at 𝑁peak, 
then for any 𝑐 ∈ (0 , 𝑝max) the equation 𝑝(𝑁, 𝑁 ) = 𝑐 has exactly two solutions 0 < 𝑁 𝓁 < 𝑁 peak < 𝑁 ℎ < 1. Under monopoly, only 𝑁ℎ can 
satisfy both the FOC and the fixed-cost coverage condition; 𝑁 = 0 is also an equilibrium if 𝑁ℎ[𝑝(𝑁ℎ, 𝑁ℎ) − 𝑐] < I. However, under DePIN, 
as 𝐾 increases, both 𝑁𝑙 and 𝑁ℎ are equilibria, with the latter becoming the main equilibrium. Furthermore, 𝑁 𝑀 < 𝑁 𝑀
ℎ → 𝑁 𝐶
ℎ .
Proof in Appendix C.3.
The decentralized move toward the competitive condition 𝑝(𝑁 𝐶 , 𝑁𝐶 ) = 𝑐 favours the high-coverage branch because the 
monopoly/oligopoly constraint that forces production onto the decreasing branch with a sizeable 𝐈 barrier is relaxed as 𝐾 rises and 
the protocol co-funds activity. DePIN increases the number of providers 𝐾 and reduces fixed costs per node, moving the market from 
monopoly (Eq.  (8)) toward the competitive limit (Proposition  3). Decentralized provision helps select the high-coverage equilibrium 
𝑁ℎ (Proposition  4). Next we analyse how Social Optimum provides even higher coverage (see Eq.  (17) and in Section 4 we present 
how governance in DePIN can achieve the social planner solution.
Social Planner (Network Externality Internalization)
We define the gross benefit under fulfilled expectations by 
𝐵(𝑄, 𝑁) = ∫
𝑞
0
𝑝(𝑥, 𝑁) 𝑑𝑥, (15)
and social welfare when 𝑄 = 𝑁 by 
𝑊 (𝑁) = 𝐵(𝑁, 𝑁 ) − 𝑐 𝑁 − I ⋅ 𝟏{𝑁 > 0} (16)
For any interior 𝑁 > 0, the planner’s FOC is 
𝑑𝑊
𝑑𝑁 = 𝑝(𝑁, 𝑁 ) + ∫
𝑁
0
𝜕𝑝(𝑥, 𝑁)
𝜕𝑁 𝑑𝑥 − 𝑐 = 0 , (17)
where ∫ 𝑁
0
𝜕𝑝(𝑥,𝑁)
𝜕𝑁 𝑑𝑥 captures the (positive) network externality that atomistic producers ignore. Hence, relative to the competitive 
condition 𝑝(𝑁, 𝑁 ) = 𝑐, the planner sets a (weakly) higher coverage because of the positive integral term. Section 4 presents how a 
DAO can internalize this positive externality and achieve Social Optimum in a decentralized manner.
3. Machine learning simulation
We use a Q-learning algorithm (Zai and Brown, 2020), where we model each of the 𝑁users users and 𝑁f irms DePIN producers as 
autonomous agents with separate Q-tables. At each discrete time 𝑡, the state observations are given by the DePIN nodes that observe 
their past supplied quantity 𝑛𝑖 and the users that observe their past binary decision. We use 𝜀–greedy action selection, where each 
agent 𝑘 selects an action 𝑎𝑘 following the rule:
We use Q-learning (Zai and Brown, 2020), modelling each of the 𝑁users users and 𝑁f irms DePIN producers as autonomous agents 
with separate Q-tables. At each discrete time 𝑡, states are observed as DePIN nodes record their previously supplied quantity 𝑛𝑖, and 
users their prior binary decision. We use 𝜀–greedy action selection, where each agent 𝑘 selects an action 𝑎𝑘 following the rule 
𝑎𝑘 =
{
random action, with probability 𝜀𝑘
arg max
𝑎
𝑄𝑘(𝑠𝑘, 𝑎), otherwise (18)
where 𝜀𝑘 decays gradually from an initial 𝜀0 toward a minimum 𝜀min, balancing initial exploration with later exploitation.
The reward for the producers are given by: 
𝑟f irm
𝑗 = 𝑛𝑗 ⋅ price − 𝑐 𝑛𝑗 − 𝐼 ⋅ 𝟏{𝑛𝑗 >0} (19)
where ‘‘price’’ is determined by the aggregate supply 𝑁𝑡 = ∑
𝑖 𝑛𝑖 and network elasticity 𝛼. Users draw a private valuation 
𝑣𝑖 ∼ Beta( 𝑎, 𝑏) each period and, if they buy, get rewards given by 
𝑟𝑖 = 𝑣𝑖 + 𝑣base
𝑖 𝑁 𝛼
𝑡 − 𝑝𝑟𝑖𝑐𝑒 (20)
After observing rewards, agents update Q-tables following the rule 
𝑄𝑘(𝑠, 𝑎) ← (1 − 𝛼) 𝑄𝑘(𝑠, 𝑎) + 𝛼( 𝑟𝑘 + 𝛾 max
𝑎′
𝑄𝑘(𝑠′, 𝑎′)) (21)
We simulate three market structures: Monopoly (𝑁f irms = 1 ), Oligopoly (𝑁f irms = 20 ) and Open DePIN Network (𝑁f irms = 100 ). 
Each with 𝑇 = 500,000 iterations and 100 users. We compare outcomes under network-effect elasticities 𝛼 ∈ {0, 0.25, 0.5}. To assess 
robustness we do two experiments: valuations from a Beta (5,5) distribution (moderate dispersion around the mean), and from a 
Beta(1,1) distribution (i.e., Uniform(0,1)). Table  1 presents the parameters. Statistics by scenario can be found in Appendix D Table 
D.4. The code is available online github.com/jsoriaro/DePIN/.
Fig.  2 shows results for the monopoly. Supply stabilizes around 50−60% of capacity under Beta valuations, and slightly lower 
under Uniform (≈0.45), rising modestly with 𝛼. Demand converges to ≈0.5–0.65, significantly lower than under DePIN. These results 
reflect the monopolist’s ability to restrict output and maintain mark-ups. As shown in Fig.  3, when we move toward oligopoly, supply 
Finance Research Letters 90 (2026) 109115 
5 

---

## Page 6

J. Soria Ruiz-Ogarrio et al.
Table 1
Simulation parameters.
 General parameters
 Number of iterations, 𝑇 500 000  
 Number of users, 𝑁users 100  
 Actions per firm, |f irm| 10  
 Discount factor, 𝛿 0.95  
 Learning rate (users), 𝛼user
lr 0.10  
 Learning rate (firms), 𝛼f irm
lr 0.10  
 Initial epsilon (𝜀user , 𝜀f irm) (1.0, 1.0)  
 Epsilon decay factor 0.9999  
 Minimum epsilon, 𝜀min 0.01  
 Firm marginal cost, 𝑐 0.05  
 Valuation distributions
 Beta (5,5) (𝑎, 𝑏) = (5 , 5)  
 Uniform (1,1) (𝑎, 𝑏) = (1 , 1)  
 Network effect elasticity, 𝛼network {0, 0.25, 0.5}  
 Monopoly
⎧
⎪
⎨
⎪⎩
𝐾 = 1,
𝐼 = 0.4∕1,
max_supply = 1∕1
 
 Oligopoly
⎧
⎪
⎨
⎪⎩
𝐾 = 20,
𝐼 = 0.4∕20,
max_supply = 1∕20
 
 Competitive
⎧
⎪
⎨
⎪⎩
𝐾 = 100,
𝐼 = 0.4∕100,
max_supply = 1∕100
 
Fig. 2. Results under Monopoly (K = 1). 500,000 iterations.
grows, demand is ≈0.85−0.95, and price drops. The number of active firms ranges between 12 and 15 (i.e., 60−75% participation). 
Figure D.5 in Appendix D shows that 𝛼’s influence notably rises with higher entry costs.
To simulate the DePIN Network, using 100 users and providers. Fig.  4 shows that aggregate supply quickly converges to 
≈0.75−0.79, with minimal variation across 𝛼. The simulation reinforces that decentralized networks can indeed provide high levels 
of coverage, even with weak network effects. Under DePIN, demand nears 1.0 in all cases. Prices drop sharply to a stable low of 
Finance Research Letters 90 (2026) 109115 
6 

---

## Page 7

J. Soria Ruiz-Ogarrio et al.
Fig. 3. Simulation under Oligopoly (K = 20). 500,000 iterations.
Fig. 4. Simulation under DePIN (K = 100). 500,000 iterations.
≈0.45, largely insensitive to 𝛼. Active firms stabilize at 75 − 78%, showing slight attrition but sustained high participation. These 
outcomes reflect competition driving output close to capacity, prices toward marginal cost, and demand to saturation.
Our multi-agent Q-learning simulations reflect our model’s insights: monopoly yields restricted supply, high prices, and unmet 
demand. Competition leads to higher supply, lower price, and full demand. This is in line with standard economic theory, and 
Finance Research Letters 90 (2026) 109115 
7 

---

## Page 8

J. Soria Ruiz-Ogarrio et al.
gives ground for the results in the next section, where we propose an innovative way to achieve Social Optimum in a decentralized 
manner.
4. Social optimum via DAO
A Decentralized Autonomous Organization (DAO) is a blockchain-native governance institution where membership, voting 
procedures, and control are specified and enforced through smart contracts. Decisions are taken collectively in a distributed way. 
Appendix A.3 provides a general presentation about tokenization and governance in decentralized protocols. In this section, we 
provide a model to implement Social Optimum Coverage for a DAO providing a DePIN.
Following Eq.  (17), the planner’s first-order condition with fulfilled expectations is
𝑝(𝑁, 𝑁 ) + ∫
𝑁
0
𝜕𝑝(𝑥, 𝑁)
𝜕𝑁 𝑑𝑥 − 𝑐 = 0,
where ∫ 𝑁
0
𝜕𝑝(𝑥,𝑁)
𝜕𝑁 𝑑𝑥 is the positive network externality. A DAO can implement a mechanism to internalize it. At period 𝑡, it estimates 
the externality term 
𝐸𝑡 ∶= ∫
𝑁𝑡
0
𝜕𝑝(𝑥, 𝑁𝑡)
𝜕𝑁𝑡
𝑑𝑥 (22)
and pays reward 𝑠𝑡 ∶= 𝐸𝑡, so that producers receive 𝑃𝑝,𝑡 = 𝑃𝑐,𝑡 + 𝑠𝑡 per unit, where 𝑃𝑐,𝑡 is the price paid by users. The lump-sum 
access fee 𝐴𝑡 per active user to fund 𝑠𝑡 and a per-node rebate 𝑅𝑡 that co-funds I is given by 
𝐴𝑡 𝑄𝑡 = 𝑠𝑡 𝑁𝑡 + 𝑅𝑡 𝐾𝑡 (23)
The access fee 𝐴𝑡 is non-distortionary at the margin (lump-sum conditional on participation), while 𝑠𝑡 changes the marginal 
condition faced by suppliers. The per-node rebate 𝑅𝑡 ∈ [0, I] dilutes the fixed burden, thus expanding 𝐾𝑡.
Proposition 5 (First-best Implementation in the Competitive Limit). Under this mechanism with 𝑠𝑡 = 𝐸𝑡 and price-taking behaviour, the 
competitive equilibrium implements the planner’s allocation. Specifically, at any period 𝑡, 𝑃𝑐,𝑡 = 𝑝(𝑁𝑡, 𝑁𝑡), 𝑃 𝑝,𝑡 = 𝑃𝑐,𝑡 + 𝑠𝑡, 𝑃 𝑝,𝑡 = 𝑐
jointly imply 𝑝(𝑁𝑡, 𝑁𝑡) + 𝑠𝑡 − 𝑐 = 0. With 𝑠𝑡 = 𝐸𝑡 this is identical to (17); hence 𝑁𝑡 = 𝑁 ∗, the planner solution.
Proof in Appendix C.4.
The mechanism is budget-balanced and feasible. If 𝑄𝑡 = 𝑁𝑡 and the DAO sets the access fee 𝐴𝑡 = 𝑠𝑡 + 𝑅𝑡 𝐾𝑡
𝑁𝑡
, then (23) holds. 
As 𝑁𝑡 rises, the per-user share 𝑅𝑡𝐾𝑡
𝑁𝑡
 falls, i.e., the fixed burden I is diluted across a growing user base.
When participants consume and supply, they internalize a share of the benefit through consumption and a share through 
production rewards. The DAO treasury (funded via 𝐴𝑡, optional fees, or token issuance) redistributes surplus. Heavier support 𝑅𝑡
accelerates 𝐾𝑡 and helps coordinate on the high-coverage equilibrium. 𝑅𝑡 decays as I is amortized and 𝑁𝑡 grows. The effect aligns 
with the simulation in Section 3.
A DePIN can collect real-time data on usage, willingness to pay, and coverage to estimate the First Best allocation (Eq.  (17)) and 
its positive externality (Eq.  (22)). This Social Optimum Pareto-dominates all feasible alternatives (Arrow and Debreu, 1954). Smart 
contracts distribute gains from any Pareto improvement, assigning rights over the externality. By the Coase theorem, this allows a 
DAO to implement the allocation in a decentralized way (Coase, 2013). Proposition  5 formalizes how this mechanism achieves a 
budget-balanced First Best outcome. Appendix E outlines its practical implementation for optimal DePIN provision.
5. Conclusion
This paper develops an economic framework for Decentralized Physical Infrastructure Networks (DePIN), positioning them as 
a blockchain-based market mode of infrastructure provision. Modelling provider entry through a network-effects framework and 
multi-agent simulations, we capture producer–user strategic interactions in markets and show how DAO token incentives can align 
decentralized outcomes with socially optimal benchmarks, characterizing the conditions under which decentralized infrastructure 
provision emerges and is sustained in equilibrium.
We present four theoretical results. First, we derive the minimum viable coverage level below which market entry is not 
individually rational as a function of fixed investment costs and token price (Proposition  2). Second, we demonstrate that network 
externalities induce path dependence, implying that early-stage interventions (e.g., subsidies or token stabilization) lead to higher 
coverage and welfare (Proposition  4 and Section 4). Third, we benchmark decentralized outcomes against monopoly and oligopolies, 
showing that it substantially mitigates welfare inefficiencies, moving outcomes toward competitive equilibrium and coordinating 
high-coverage branch (Proposition  4). Fourth, via a DAO budget-balanced mechanism, DePIN can achieve Social Optimum coverage 
outcomes in the competitive limit (Proposition  5).
These results are validated through a Q-learning simulation (Section 3). The experiment confirms DePIN supports higher 
coverage, lower prices, and near-full adoption compared to monopoly or oligopoly structures.
Our findings bridge Tokenomics, Decentralized Finance, and Industrial Organization, embedding rationality into blockchain 
coordination. They provide a basis for assessing DePIN performance and financial viability, guiding implementation. The framework 
has been validated in markets (Propositions  3, 4) and identifies conditions for long-term scalability and sustainability in decentralized 
Finance Research Letters 90 (2026) 109115 
8 

---

## Page 9

J. Soria Ruiz-Ogarrio et al.
infrastructure provision (Proposition  2). It also offers a transferable methodology. Future research could extend the framework to 
include heterogeneous demand, layered architectures, network effects, or DAO governance.
This work contributes to the finance literature on decentralized systems and establishes a basis for evaluating the economic 
viability of Decentralized Physical Infrastructure Networks.
CRediT authorship contribution statement
Jorge Soria Ruiz-Ogarrio: Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, 
Investigation, Conceptualization. Jorge Moya Velasco: Writing – review & editing, Writing – original draft, Supervision, Methodol-
ogy, Investigation, Conceptualization. Carlos Estévez-Mendoza: Writing – review & editing, Writing – original draft, Visualization, 
Supervision, Project administration, Investigation, Formal analysis, Conceptualization.
Acknowledgements
The co-author Carlos Estévez-Mendoza acknowledges the support provided by the PID2021-126516NB-I00 project funded by 
MCIN/AEI/10.13039/501100011033/FEDER, UE 
Appendix A. Essential functioning of decentralized physical infrastructure networks (DePIN)
The collaborative economy was boosted by the arrival of digital aggregator platforms, which centralised the marketing of 
similar products, including resources offered by individuals, such as accommodation or transport (Ghosh and Gorai, 2024). 
Although they decentralised supply, they concentrated management, control and technical infrastructure, centralising value capture 
in a single entity. DePIN constitutes a natural extension of the original collaborative economy model, replacing centralised 
infrastructure provision with contributions from decentralised participants, some of whom are also consumers (prosumers, i.e., 
producer-consumers), who supply resources to the DePIN network incentivised through tokens.
This integrated intersection of physical networks, blockchain, and tokenized incentives is what we will use to briefly explain the 
essential functioning of DePIN networks.
A.1. The physical infrastructure layer: Devices and resources
The foundation of each DePIN network lies in physical nodes contributed by participants, which collectively constitute the 
infrastructure for delivering decentralized services. These nodes may include sensors, routers, GPUs, storage devices, or energy assets 
such as solar panels. Users contribute resources or surplus capacity, which the network organizes through decentralized protocols 
according to service type—e.g., storage, connectivity, or energy. More advanced configurations may integrate multiple services or 
involve both individuals and companies contributing physical infrastructure simultaneously.
Such infrastructures typically fall into two main categories. The first comprises Physical Resource Networks (PRNs), formed by 
tangible, location-dependent hardware—such as sensors, wireless access points, charging stations, or mobility devices—whose value 
is determined by their physical placement and specific features (e.g., an urban surveillance camera differs in value from one located 
in a remote area). The second type, Digital Resource Networks (DRNs), consists of location-independent digital resources—such as 
computing power or bandwidth—whose value depends on performance characteristics like capacity or availability, and which are 
often interchangeable when meeting equivalent specifications.
A.2. Blockchain, smart contracts, and security in DePIN
Blockchain, as a technology based on optimal verification protocols (Narayanan et al., 2016), enables DePIN to function as 
transparent, secure, and tamper-resistant systems (Liu and Omote, 2025; Almadani et al., 2023). Its ability to create an immutable 
record of operations prevents the alteration of agreements or actions within the network, as block-based verification makes rewriting 
history difficult. Data integrity is critical in the management of decentralized physical infrastructures. Verification systems promote 
honest behaviour, enhance resilience against malicious actors, and foster trust among participants. To verify contributions and ensure 
service quality, DePIN employ specialized blockchain-based consensus mechanisms, such as Proof of Physical Work (PoPW), which 
demonstrate that a node has made a useful and measurable physical contribution.
Proof of Physical Work (PoPW) does not refer to a single protocol, but rather to a category that encompasses proofs adapted to 
physical environments. These include Proof of Coverage (PoC), used by some networks to validate the location and coverage of nodes, 
or Proof of Location (PoL) for geographical verification. Similarly, Proof of Mobility (Drive-to-Earn) is used, for example, to reward 
mobile nodes that collect data. Or Proof of Rendering Capacity, implemented to validate computational resources. These proofs vary 
depending on the network and the physical environment considered, and not all systems implement every modality.
Smart contracts are essential in this layer, functioning as self-executing agreements with coded terms. They automate conditions, 
eliminate intermediaries, and ensure efficiency and reliability (John et al., 2023; Cong and He, 2019). In DePIN, they enable 
data exchange, resource allocation, transaction verification, and reward distribution without third-party intervention. Table  A.2 
summarizes their main functions:
Finance Research Letters 90 (2026) 109115 
9 

---

## Page 10

J. Soria Ruiz-Ogarrio et al.
Table A.2
Key functions and applications of smart contracts in DePIN.
 Key function Description and application in DePIN  
 Automated Payments and Incentives Automatically distribute token rewards to contributors and process real-time payments for services rendered. 
 Resource Allocation and Management Enable interaction between physical assets and automate tasks such as resource allocation, data exchange, 
maintenance operations, or resource reassignment.
 
 Decentralized Governance Facilitate decentralized decision-making through verifiable agreements, voting mechanisms, or distribution of 
decision-making power.
 
 Service Level Agreement (SLA) Enforcement Monitor service performance, applying penalties or making adjustments according to agreed service levels.  
 Data Integrity and Verification Record and verify transactions and resource contributions, ensuring transparency and data immutability.  
Despite the sophistication of these mechanisms, DePIN face structural challenges in security and economic sustainability. Two key 
attacks stand out, although other vectors may also emerge: data spoofing, which falsifies data to obtain rewards without providing 
services (Liu and Omote, 2025), and self-dealing, where a provider acts as a client through fake identities or Sybil attacks to validate 
their own services or concentrate governance power (Caprolu et al., 2025; Sarkar, 2023).
These vulnerabilities are inherent to the contribute-to-earn model, which encourages participation but may promote opportunism. 
To counteract them, defences include node cross-verification, cryptographic location proofs, reputation systems, and distributed 
physical observers. Randomized task assignments and access controls also prevent manipulation. Many DePIN projects seek Byzantine 
Fault Tolerance (BFT) to ensure correct operation despite malicious nodes (Milionis et al., 2025). Therefore, incentives align rewards 
with integrity, since those who can compromise the system the most are the ones who have the most to lose (Savolainen and Soria, 
2019).
Technical solutions are complemented by economic mechanisms like staking and slashing. Staking locks tokens as collateral 
for node operation or data validation, aligning incentives with network performance. Slashing penalizes fraud, inactivity, or poor 
performance by forfeiting part of the stake. For instance, some networks reduce rewards if GPU nodes fail minimum availability or 
underperform relative to declarations.
A.3. Tokenized economy and decentralized governance in DePIN
A token is a digital asset that represents a set of rights associated with behaviours within the blockchain ecosystem (Treiblmaier, 
2023). In DePIN systems, tokens fulfil essential functions: they incentivize, coordinate, and govern participation (Treiblmaier, 2023).
First, tokens serve as payments for those who contribute physical resources, thus promoting the long-term sustainability of 
the network, following the contribute-to-earn model. The reward system is based on each participant’s proportional contribution, 
according to variables such as quantity, quality, uptime, or the characteristics of the resources provided and shared. A well-designed 
algorithm is crucial to encourage desired behaviours, including expansion into new or underserved areas.
Tokens also confer voting rights, enabling decentralized governance via Decentralized Autonomous Organizations (DAOs) 
managed by smart contracts automating decision-making. Polkadot’s OpenGov exemplifies on-chain proposals and voting, ensuring 
transparency, community involvement, and immutability. Token holders decide on updates, fees, and funds, aligning management 
with participant interests.
DePIN governance mechanisms draw on models from digital economy organizations, incorporating systems such as quadratic 
voting, which imposes quadratic costs to reduce the influence of large token holders and promote fairness (de Lima and Oliveira, 
2024; Dimitri, 2022). The liquid democracy model enables flexible delegation of voting power (Hassan et al., 2022), while vote-
escrowed or time-locked voting mechanisms enhance governance stability by requiring tokens to be locked for a defined period. In 
addition, DePIN architectures may implement modular governance through sub-DAOs, allowing specific network segments or service 
layers to be governed independently, thereby improving scalability, adaptability, and alignment with local conditions.
However, the structural dependence on the token can generate problems (Yousaf and Yarovaya, 2022), as declines in its value 
reduce incentives for participants (Chen et al., 2023), potentially leading to node abandonment and the weakening of physical 
infrastructure (Liu and Omote, 2025). To mitigate these risks, many DePIN projects implement vesting schedules, which gradually 
distribute the allocated tokens. This prevents their immediate liquidity in large volumes, reduces the pressure from mass sell-offs, 
and fosters long-term commitment by linking rewards to the sustained success of the ecosystem.
Altogether, the tokenized economy and decentralized governance form an interdependent system linking incentives and 
governance.
Appendix B. Real-world DePIN applications
The versatility of the DePIN model supports its adoption across multiple sectors in response to the demand for physical 
infrastructures organized in innovative ways. Although still emerging, its evolution allows for the identification of categories that 
have been grouped as follows:
• Computing Networks (Render, Golem, Akash): aggregate distributed CPUs and GPUs for on-demand computing, including 
rendering, AI, and edge computing.
Finance Research Letters 90 (2026) 109115 
10 

---

## Page 11

J. Soria Ruiz-Ogarrio et al.
Table B.3
DePIN projects capitalization by category.
Source: Authors’ elaboration based on data from DePINHub (project counts) and CoinGecko and CoinMarketCap (market caps), accessed July 
2025. B = billions, M = millions (USD).
 Category Cap Jul 
2024
Cap Jul 
2025
𝛥 Cap Proj. 
2024
Proj. 
2025
𝛥 Proj. Key Examples Use Cases  
 Computing 
Networks
$7.5 B $9.1 B +21.3% 28 43 +15 Render, Golem, Akash, 
Bittensor
GPU render; cloud compute; AI; 
decentralized training
 
 Storage 
Networks
$2.6 B $2.8 B +7.7% 24 30 +6 Filecoin, Storj, 
Arweave, Shadow
P2P data storage; permanent archive; 
decentralized cloud
 
 Wireless 
Connection
$620 M $783 M +26.3% 15 20 +5 Helium, Nodle, World 
Mobile
IoT connectivity; 5G access; public Wi-Fi 
 Mobility, geo 
and mapping
$320 M $370 M +15.6% 7 10 +3 Hivemapper, DIMO, 
GeoDNet, XYO
Crowdsourced mapping; EV data tokens; 
geolocation
 
 Sensor 
Networks
$250 M $307 M +22.8% 16 22 +6 WeatherXM, 
PlanetWatch, Silencio
Environmental data; geolocation; smart 
infrastructure
 
 Energy 
Networks
$80 M $99 M +23.8% 10 13 +3 PowerLedger, Energy 
Web, Chain4Energy
P2P energy trading; EV charging grid; 
green certificates
 
Total $11.37 B $13.46 B +18.4% 100 138 +38 —
• Storage Networks (Filecoin, Arweave, Storj): users contribute disk space as an alternative to centralized cloud solutions. 
Include, for instance, permanent archiving, distributed backup, and cyclical storage.
• Wireless Connection (Helium, Nodle, World Mobile): community hotspot networks offering IoT, 5G, and public Wi-Fi 
connectivity. Use cases are rural coverage, community Wi-Fi, and decentralized MVNOs.
• Sensor and Geospatial Networks (WeatherXM, XYO, PlanetWatch): capture physical and geolocated data for environmental 
monitoring and spatial analysis; Some subcases could be weather stations, air quality monitoring or asset geolocation.
• Mobility and Geosocial Networks (Hivemapper, DIMO, GeoDNet): community networks using dashcams, vehicular, and 
mobile data for collaborative mapping and vehicular intelligence. The subcases are, for example, dashcam mapping, automotive 
telemetry or community EV charging infrastructure.
• Energy Networks (PowerLedger, Energy Web, Penomo): decentralized energy management applied to P2P trading, renewable 
microgrids, and electric vehicle charging.
We present the active DePIN projects and the market capitalization as of the date of the analysis. Capitalization estimates a 
project’s value by multiplying token price and supply.
The goal is not only to present data (Lin et al., 2025), but to offer a snapshot of the level of consolidation, dynamism, and 
strategic attractiveness of each category, reflecting their capacity to scale and generate commercial value. Table  B.3 summarizes 
this analysis, ranking the categories by maturity and representative examples.
According to capitalization data and active projects, Computing Networks clearly lead the DePIN space, followed by Storage 
Networks and Wireless Connectivity, with more modest values. Sensor and Geospatial, Mobility Geosocial, and Energy Networks show 
lower capitalization and fewer projects, but their growing dynamism could turn them into strategic areas with high expansion 
potential.
The DePIN market is dynamic and evolving. It is likely that new categories will emerge, driven by advances in blockchain 
technology and unmet needs in centralized infrastructures, such as those related to space infrastructure (satellites, telescopes, 
communications), biotechnology (distributed computing for genomic data), robotics and automation (autonomous fleets in logistics 
or manufacturing), and water or waste infrastructure (smart water management and recycling).
The table also reports annual growth in capitalization and project count, offering a dynamic perspective of the ecosystem’s 
expansion. While total capitalization grew by about 18%, the number of projects increased by nearly 40%, suggesting that growth 
is mainly driven by the entry of new, smaller-scale initiatives rather than by large revaluations of existing tokens. This pattern 
is typical of early-stage, rapidly diversifying sectors, where experimentation and network effects precede large-scale consolidation 
(Bohnsack et al., 2024; Jacobides et al., 2018; Uche-Soria et al., 2025).
Appendix C. Proofs
C.1. Proof of Proposition  1
Using Eq.  (9) and 𝑞(0) = 1 , as 𝑁 ↓ 0, 
𝑑𝑝
𝑑𝑁 ∼
⎧
⎪
⎨
⎪⎩
+∞ if 𝛼 < 1,
𝜂 − 𝜙
𝑓 (1) if 𝛼 = 1,
(C.1)
Finance Research Letters 90 (2026) 109115 
11 

---

## Page 12

J. Soria Ruiz-Ogarrio et al.
Fig. D.5. Oligopoly simulation with doubled entry cost per firm.
so the slope is positive under the stated conditions. As 𝑁 ↑ 1, 𝑞(𝑁) → 0 and 𝑞′(𝑁) = −1∕ 𝑓 (𝑞(𝑁)) stays finite and negative; the 
second term of (9) dominates, yielding 𝑑𝑝
𝑑𝑁 < 0. By continuity, there is at least one turning point; strict quasi-concavity of 𝑝(⋅, ⋅)
here gives uniqueness. □
C.2. Proof of Proposition  2
Any interior monopoly choice must lie on the decreasing branch 𝑁 ≥ 𝑁peak and satisfy 𝑁[𝑝(𝑁, 𝑁 ) − 𝑐] ≥ I. The smallest such 𝑁
is 𝑁min. If 𝑁𝑚𝑖𝑛 doesn’t cover the entry costs I then 𝑁𝑡 = 0 and there is no coverage provided by the monopoly. □
C.3. Proof of Proposition  4
Non-monotonicity implies two intersections with the horizontal line at 𝑐: one on each side of 𝑁peak . By Proposition 1, the 
monopoly’s interior choice must be on the decreasing branch (𝑁 𝑀 ≥ 𝑁peak ). If 𝑁 𝑀 [𝑝(𝑁 𝑀 , 𝑁𝑀 ) − 𝑐] < I, provision is not incentive 
compatible and 𝑁 = 0 is optimal.
On the other hand, allowing arbitrarily small 𝑛𝑗 lets agents cover fraction 𝐈 of I and the residual fixed cost per node falls, 
making entry profitable for a larger set of agents. Thus, 𝐾 weakly increases. Taking 𝐾 → ∞ in (13) yields 𝑝(𝑁 𝐶 , 𝑁𝐶 ) = 𝑐. For 𝐾
large enough, the markup term in (13) diminishes and the realized 𝑁 must be near a solution to 𝑝(𝑁, 𝑁 ) = 𝑐, i.e., either 𝑁𝓁 or 𝑁ℎ. 
By Proposition 1, to operate, agents must cover 𝐈 from variable margins. Because 𝑝(𝑁, 𝑁 ) is decreasing for 𝑁 ≥ 𝑁peak , the per-unit 
margin is larger in the neighbourhood of 𝑁ℎ than at 𝑁𝓁, and co-funding of I further relaxes the viability constraint at higher 𝑁. 
Hence, 𝑁ℎ is selected. □
C.4. Proof of Proposition  5
In the competitive limit, each producer is a price taker and supplies until 𝑃𝑝,𝑡 = 𝑐. Users face 𝑃𝑐,𝑡 and demand 𝑄𝑡 = 𝑁𝑡 such 
that 𝑃𝑐,𝑡 = 𝑝(𝑁𝑡, 𝑁𝑡). The per-unit subsidy raises producers’ marginal revenue to 𝑃𝑝,𝑡 = 𝑝(𝑁𝑡, 𝑁𝑡) + 𝑠𝑡. Setting 𝑠𝑡 = 𝐸𝑡 aligns the 
decentralized marginal condition with the planner’s FOC. □
Appendix D. Summary of simulation results and effect of higher entry costs on equilibrium coverage
Fig.  D.5 presents a simulation for the oligopoly case, showing that the influence of 𝛼 increases substantially when the entry cost 
per firm is doubled. Table  D.4 presents the main simulation statistics for the different valuation distributions, types of competition, 
and values of 𝛼.
Finance Research Letters 90 (2026) 109115 
12 

---

## Page 13

J. Soria Ruiz-Ogarrio et al.
Table D.4
Summary of simulation statistics by scenario, distribution and 𝛼.
 Distribution 𝜶 Supply Demand Price
 Mean 𝜎 Mean 𝜎 Mean 𝜎  
 (a) DePIN 100 prosumers
 
Beta(5,5)
0.0000 0.7621 0.0260 0.9825 0.0575 0.4759 0.0519 
 0.2500 0.7561 0.0236 0.9782 0.0641 0.4712 0.0425 
 0.5000 0.7530 0.0203 0.9838 0.0499 0.4611 0.0332 
 
Uniform(1,1)
0.0000 0.7640 0.0223 0.9703 0.0571 0.4720 0.0446 
 0.2500 0.7567 0.0209 0.9704 0.0576 0.4701 0.0381 
 0.5000 0.7528 0.0218 0.9765 0.0563 0.4615 0.0358 
 (b) Monopoly
 
Beta(5,5)
0.0000 0.4467 0.0604 0.4308 0.0182 1.1067 0.1208 
 0.2500 0.5578 0.0579 0.5930 0.0187 0.8205 0.0855 
 0.5000 0.5558 0.0326 0.6893 0.0282 0.7744 0.0435 
 
Uniform(1,1)
0.0000 0.4456 0.0458 0.3485 0.0256 1.1089 0.0916 
 0.2500 0.5527 0.0546 0.5456 0.0198 0.8299 0.0749 
 0.5000 0.5538 0.0455 0.5316 0.0174 0.7759 0.0547 
 (c) Oligopoly, 20 providers
 
Beta(5,5)
0.0000 0.7409 0.0308 0.9434 0.0530 0.5181 0.0617 
 0.2500 0.7416 0.0268 0.9562 0.0564 0.4978 0.0485 
 0.5000 0.7429 0.0257 0.9810 0.0530 0.4782 0.0425 
 
Uniform(1,1)
0.0000 0.7429 0.0268 0.9145 0.0549 0.5143 0.0536 
 0.2500 0.7445 0.0264 0.9462 0.0522 0.4926 0.0478 
 0.5000 0.7410 0.0276 0.9717 0.0516 0.4814 0.0451 
 (d) Oligopoly, 20 providers, double entry cost
 
Beta(5,5)
0.0000 0.5510 0.0197 0.5701 0.0151 0.8981 0.0394 
 0.2500 0.5012 0.0190 0.4992 0.0158 0.9183 0.0314 
 0.5000 0.4819 0.0310 0.4299 0.0269 0.8769 0.0408 
 
Uniform(1,1)
0.0000 0.5495 0.0198 0.5032 0.0200 0.9010 0.0396 
 0.2500 0.4997 0.0189 0.4612 0.0171 0.9208 0.0312 
 0.5000 0.4825 0.0291 0.3691 0.0213 0.8762 0.0376 
Appendix E. Sketch of a potential DAO mechanism
(i) Externality Estimation.
Using 𝑝(𝑁, 𝑁 ) = ( 𝜙 + 𝜂𝑁 𝛼)𝐹 −1(1 − 𝑁), 
𝜕𝑝(𝑥, 𝑁)
𝜕𝑁 = 𝜂𝛼𝑁 𝛼−1𝐹 −1(1 − 𝑥) − 𝜙 + 𝜂𝑁 𝛼
𝑓 (𝐹 −1(1 − 𝑥)) , (E.1)
and the DAO computes 
𝐸𝑡 = ∫
𝑁𝑡
0
𝜕𝑝(𝑥, 𝑁𝑡)
𝜕𝑁𝑡
𝑑𝑥, (E.2)
possibly via an online estimator with smoothing, e.g., 
𝑠𝑡+1 = 𝛽 𝑠𝑡 + (1 − 𝛽) ̂𝐸𝑡, 𝛽 ∈ [0, 1). (E.3)
(ii) Rewards & Verification.
Each provider 𝑗 receives 
payout𝑗 = 𝑛𝑗,𝑡 𝑠𝑡 + 𝑅𝑡 ⋅ 𝟏{𝑛𝑗,𝑡 > 0}, (E.4)
conditional on cryptographic proofs (e.g., location/quality oracles) and subject to slashing for misreports.
(iii) Governance and Consensus.
A DAO chooses (𝑠𝑡, 𝑅𝑡, 𝐴𝑡) to maximize an on-chain proxy for welfare, 
max
𝑠𝑡,𝑅𝑡,𝐴𝑡
̂𝑊𝑡 = ̂𝐵(𝑁𝑡, 𝑁𝑡) − 𝑐 𝑁𝑡 − I 𝐾𝑡 − 𝜆 Var(𝑠𝑡) (E.5)
subject to (23) and bounds on token issuance. Voting can combine stake with usage-based credentials; quadratic voting on 𝑅𝑡 helps 
reflect dispersed user preferences while avoiding plutocracy. In steady state, the DAO targets 𝑠𝑡 ≈ 𝐸𝑡 and the competitive outcome 
implements the planner allocation by Proposition  5.
Finance Research Letters 90 (2026) 109115 
13 

---

## Page 14

J. Soria Ruiz-Ogarrio et al.
Data availability
The file uploaded as Supplementary Material with the name ‘‘DePIN python code rep’’ contains access to the Github repository 
where the code used in the simulation is hosted.
References
Ahmed, S., 2025. Enhancing data security and transparency: The role of blockchain in decentralized systems. Int. J. Adv. Eng. Manag. Sci. 11 (1), 593258. 
http://dx.doi.org/10.22161/ijaems.111.12.
Ali, O., Jaradat, A., Kulakli, A., Abuhalimeh, A., 2021. A comparative study: Blockchain technology utilization benefits, challenges and functionalities. IEEE 
Access 9, 12730–12749. http://dx.doi.org/10.1109/ACCESS.2021.3050241.
Almadani, M.S., Alotaibi, S., Alsobhi, H., Hussain, O.K., Hussain, F.K., 2023. Blockchain-based multi-factor authentication: A systematic literature review. Internet 
Things 23, 100844. http://dx.doi.org/10.1016/j.iot.2023.100844.
Andrew, D., Ballandies, J., 2025. Are you a Depin? A decision tree to classify decentralized physical infrastructure networks. http://dx.doi.org/10.48550/arXiv.
2501.17416.
Arrow, K.J., Debreu, G., 1954. Existence of an equilibrium for a competitive economy. Econometrica 22 (3), 265–290. http://dx.doi.org/10.2307/1907353.
von der Assen, J., Killer, C., Carli, A.D., Stiller, B., 2024. Performance analysis of decentralized physical infrastructure networks and centralized clouds. In: IEEE 
International Conference on Blockchain and Cryptocurrency, ICBC 2024, Dublin, Ireland, May 27-31, 2024. IEEE, pp. 1–6. http://dx.doi.org/10.5167/uzh-
262712.
Ballandies, M.C., Wang, H., Chee Law, A.C., Yang, J.C., Gösken, C., Andrew, M., 2023. A taxonomy for blockchain-based decentralized physical infrastructure 
networks (DePIN). In: 2023 IEEE 9th World Forum on Internet of Things. WF-IoT, pp. 1–6. http://dx.doi.org/10.1109/WF-IoT58464.2023.10539514.
Bhavana, N., Kumar, N., Rai, I., Reddy, C.S., Kumar, S., 2024. Applications of blockchain technology in peer-to-peer energy markets and green hydrogen supply 
chains: A topical review. Sci. Rep. 14, 21954. http://dx.doi.org/10.1038/s41598-024-72642-2.
Bohnsack, R., Rennings, M., Block, C., Bröring, S., 2024. Profiting from innovation when digital business ecosystems emerge: A control point perspective. Res. 
Policy 53 (3), 104961. http://dx.doi.org/10.1016/j.respol.2024.104961.
Boumaiza, A., 2024a. A blockchain-based scalability solution with microgrids peer-to-peer trade. Energies 17 (4), 915. http://dx.doi.org/10.3390/en17040915.
Boumaiza, A., 2024b. A blockchain-centric P2P trading framework incorporating carbon and energy trades. Energy Strategy Rev. 54, 101466. http://dx.doi.org/
10.1016/j.esr.2024.101466.
Caprolu, M., Raponi, S., Pietro, R.D., 2025. Sharing is (S)caring: Security and privacy issues in decentralized physical infrastructure networks (DePIN). In: Network 
and System Security. Springer Nature Singapore, Singapore, pp. 301–318. http://dx.doi.org/10.1007/978-981-96-3531-3_15.
Castillo, F., Castillo, O., Brito, E., Espinola, S., 2025. Trustworthy decentralized autonomous machines: A new paradigm in automation economy. http:
//dx.doi.org/10.48550/arXiv.2504.15676.
Chen, K., Fan, Y., Liao, S.S., 2023. Token incentives in a volatile crypto market: The effects of token price volatility on user contribution. J. Manage. Inf. Syst. 
40 (2), 683–711. http://dx.doi.org/10.1080/07421222.2023.2196772.
Coase, R.H., 2013. The problem of social cost. J. Law Econ. 56 (4), 837–877. http://dx.doi.org/10.1086/674872.
Cong, L.W., He, Z., 2019. Blockchain disruption and smart contracts. Rev. Financ. Stud. 32 (5), 1754–1797. http://dx.doi.org/10.1093/rfs/hhz007.
de Lima, L., Oliveira, M., 2024. Quadratic voting in peer-governance: Theory and empirical evidence. J. Innov. Knowl. 9, 45–56. http://dx.doi.org/10.1016/j.
jik.2024.01.005.
Dimitri, N., 2022. Quadratic voting in blockchain governance. Information 13 (6), 305. http://dx.doi.org/10.3390/info13060305.
Dong, J., Song, C., Liu, S., Yin, H., Zheng, H., Li, Y., 2022. Decentralized peer-to-peer energy trading strategy in energy blockchain environment: A game-theoretic 
approach. Appl. Energy 325, 119852. http://dx.doi.org/10.1016/j.apenergy.2022.119852.
Economides, N., Himmelberg, C., 2013. Critical mass and network evolution in telecommunications. In: Toward a Competitive Telecommunication Industry. 
Routledge, pp. 47–63.
Fan, X., 2024. New directions in decentralized physical infrastructure networks. In: 2024 6th International Conference on Blockchain Computing and Applications. 
BCCA, http://dx.doi.org/10.1109/BCCA62388.2024.10844432.
Fan, X., Xu, L., 2024. Towards a rollup-centric scalable architecture for decentralized physical infrastructure networks: A position paper. In: Proceedings 
of the Fifth ACM International Workshop on Blockchain-Enabled Networked Sensor Systems. Association for Computing Machinery, pp. 9–12. http:
//dx.doi.org/10.1145/3628354.3629534.
Ghosh, S., Gorai, S., 2024. The Age of Decentralization: How Web3 and Related Technologies Will Change Industries and Our Lives. Productivity Press, New 
York, NY, http://dx.doi.org/10.4324/9781003507352.
Hassan, C.A.u., Hammad, M., Iqbal, J., Hussain, S., Ullah, S.S., AlSalman, H., Mosleh, M.A.A., Arif, M., 2022. A liquid democracy enabled blockchain-based 
electronic voting system. Sci. Program. http://dx.doi.org/10.1155/2022/1383007.
Islam, S., Apu, K.U., 2024. Decentralized vs. Centralized database solutions in blockchain: advantages, challenges, and use cases. Glob. Mainstream J. Innov. 
Eng. Emerg. Technol. 3 (4), 58–68. http://dx.doi.org/10.62304/jieet.v3i04.195.
Jacobides, M.G., Cennamo, C., Gawer, A., 2018. Towards a theory of ecosystems. Strategy Manag. J. 39 (8), 2255–2276. http://dx.doi.org/10.1002/smj.2904.
John, K., Kogan, L., Saleh, F., 2023. Smart contracts and decentralized finance. Annu. Rev. Financ. Econ. 15 (1), 523–542. http://dx.doi.org/10.1146/annurev-
financial-110921-022806.
Karhu, K., Heiskala, M., Ritala, P., Thomas, L.D., 2024. Positive, negative, and amplified network externalities in platform markets. Acad. Manag. Perspect. 38 
(3), 349–367. http://dx.doi.org/10.5465/amp.2023.0119.
Karumba, S., Sethuvenkatraman, S., Dedeoglu, V., Jurdak, R., Kanhere, S.S., 2023. Barriers to blockchain-based decentralised energy trading: A systematic review. 
Int. J. Sustain. Energy 42 (1), 41–71. http://dx.doi.org/10.1080/14786451.2023.2171417.
Katz, M.L., Shapiro, C., 1994. Systems competition and network effects. J. Econ. Perspect. 8 (2), 93–115. http://dx.doi.org/10.1257/jep.8.2.93.
Lage, O., Saiz-Santos, M., Zarzuelo, J.M., 2022. Decentralized platform economy: emerging blockchain-based decentralized platform business models. Electron 
Mark. 32, 1707–1723. http://dx.doi.org/10.1007/s12525-022-00586-4.
Lin, Z., Wang, T., Shi, L., Zhang, S., Cao, B., 2025. Decentralized physical infrastructure networks (DePIN): Challenges and opportunities. IEEE Netw. 39 (2), 
91–99. http://dx.doi.org/10.1109/MNET.2024.3487924.
Liu, H., Omote, T., 2025. A traceable authentication system based on blockchain for decentralized physical infrastructure networks. Sci. Rep. 15 (16708), 
http://dx.doi.org/10.1038/s41598-025-01114-y.
Liu, X., Zhu, C., Qi, W., Wang, J., 2022. Product line and service pricing considering negative network effects. Comput. Ind. Eng. 170, 108328. http:
//dx.doi.org/10.1016/j.cie.2022.108328.
Maksymyuk, T., Gazda, J., Volosin, M., Bugar, G., Horvath, D., Klymash, M., Dohler, M., 2020. Blockchain-empowered framework for decentralized network 
management in 6G. IEEE Commun. Mag. 58 (9), 86–92. http://dx.doi.org/10.1109/MCOM.001.2000175.
Mao, H., He, Y., Li, J., 2025. LooPIN: A pinfi protocol for decentralized computing. http://dx.doi.org/10.48550/arXiv.2406.09422.
Finance Research Letters 90 (2026) 109115 
14 

---

## Page 15

J. Soria Ruiz-Ogarrio et al.
Mezquita, Y., Gil-González, A.B., Martín del Rey, A., Prieto, J., Corchado, J.M., 2022. Towards a blockchain-based peer-to-peer energy marketplace. Energies 15 
(9), 3046. http://dx.doi.org/10.3390/en15093046.
Milionis, J., Ernstberger, J., Bonneau, J., Kominers, S.D., Roughgarden, T., 2025. Incentive-compatible recovery from manipulated signals, with applications to 
decentralized physical infrastructure. http://dx.doi.org/10.48550/arXiv.2503.07558.
Narayanan, A., Bonneau, J., Felten, E., Miller, A., Goldfeder, S., 2016. Bitcoin and Cryptocurrency Technologies: A Comprehensive Introduction. Princeton 
University Press.
Pereira, J., Tavalaei, M.M., Ozalp, H., 2019. Blockchain-based platforms: Decentralized infrastructures and its boundary conditions. Technol. Forecast. Soc. Change 
146, 94–102. http://dx.doi.org/10.1016/j.techfore.2019.04.030.
Pop, C., Cioara, T., Antal, M., Anghel, I., Salomie, I., Bertoncini, M., 2018. Blockchain based decentralized management of demand response programs in smart 
energy grids. Sensors 18 (1), 162. http://dx.doi.org/10.3390/s18010162.
Sarkar, D., 2023. Generalised DePIN protocol: A framework for decentralized physical infrastructure networks. http://dx.doi.org/10.48550/arXiv.2311.00551.
Savolainen, V., Soria, J., 2019. Too Big to Cheat: Mining Pools’ Incentives to Double Spend in Blockchain Based Cryptocurrencies. SSRN, http://dx.doi.org/10.
2139/ssrn.3506748.
Seven, S., Yao, G., Soran, A., Onen, A., Muyeen, S.M., 2020. Peer-to-peer energy trading in virtual power plant based on blockchain smart contracts. IEEE Access 
8, 165996–166014. http://dx.doi.org/10.1109/ACCESS.2020.3026180.
Soria, J., Moya, J., Mohazab, A., 2023. Optimal mining in proof-of-work blockchain protocols. Financ. Res. Lett. 53, 103610. http://dx.doi.org/10.1016/j.frl.
2022.103610.
Surve, T., Khandelwal, R., 2023. The development of decentralized governance models for web 3 ecosystems. In: Concepts, Technologies, Challenges, and the 
Future of Web 3. IGI Global, pp. 91–107. http://dx.doi.org/10.4018/978-1-6684-9919-1.ch006.
Tanveer, U., Ishaq, S., Hoang, T.G., 2025. Tokenized assets in a decentralized economy: Balancing efficiency, value, and risks. Int. J. Prod. Econ. 109554. 
http://dx.doi.org/10.1016/j.ijpe.2025.109554.
Thukral, 2021. Emergence of blockchain-technology application in peer-to-peer electrical-energy trading: A review. Clean Energy 5 (1), 104–118. http:
//dx.doi.org/10.1093/ce/zkab003.
Treiblmaier, H., 2023. Beyond blockchain: How tokens trigger the internet of value and what marketing researchers need to know about them. J. Mark. Commun. 
29 (3), 238–250. http://dx.doi.org/10.1080/13527266.2021.2011375.
Uche-Soria, M., Martínez Raya, A., Muñoz Cabanes, A., Moya Velasco, J., 2025. Redefining transactions, trust, and transparency in the energy market from 
blockchain-driven technology. Technologies 13 (9), 412. http://dx.doi.org/10.3390/technologies13090412.
Wang, Z., Yu, X., Mu, Y., Jia, H., 2020. A distributed peer-to-peer energy transaction method for diversified prosumers in urban community microgrid system. 
Appl. Energy 260, 114327. http://dx.doi.org/10.1016/j.apenergy.2019.114327.
Yap, K.Y., Chin, H.H., Klemeš, J.J., 2023. Blockchain technology for distributed generation: A review of current development, challenges and future prospect. 
Renew. Sustain. Energy Rev. 175, 113170. http://dx.doi.org/10.1016/j.rser.2023.113170.
Yousaf, I., Yarovaya, L., 2022. The relationship between trading volume, volatility and returns of non-fungible tokens: Evidence from a quantile approach. Financ. 
Res. Lett. 50, 103175. http://dx.doi.org/10.1016/j.frl.2022.103175.
Zai, A., Brown, B., 2020. Deep Reinforcement Learning in Action. Manning.
Zheng, J., Lo, S.W., Xia, C., Lee, D.K.C., 2025. Navigating cryptocurrencies’ next frontier: The revolution toward decentralizing physical infrastructure. In: 
Handbook of Blockchain, Digital Finance, and Inclusion, Volume 3. Academic Press, pp. 51–59. http://dx.doi.org/10.1016/B978-0-443-34717-7.00018-0.
Finance Research Letters 90 (2026) 109115 
15 

---
