# DelgadoFernandez_Barbereau_Papageorgiou_2022_AgentBasedModelOfInitialTokenAllocations_WealthConcentrationInFairLaunches.pdf

## Page 1

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS:
EVALUATING WEALTH CONCENTRATION IN FAIR
LAUNCHES
JOAQUIN DELGADO FERNANDEZ , TOM BARBEREAU ,
AND ORESTIS PAPAGEORGIOU
Abstract. With advancements in distributed ledger technologies and smart
contracts, tokenized voting rights gained prominence within Decentralized Fi-
nance (DeFi). Voting rights tokens (aka. governance tokens) are fungible to-
kens that grant individual holders the right to vote upon the fate of a project.
The motivation behind these tokens is to achieve decentral control. Because
the initial allocations of these tokens is often un-democratic, the DeFi project
Yearn Finance experimented with a fair launch allocation where no tokens are
pre-mined and all participants have an equal opportunity to receive them. Re-
gardless, research on voting rights tokens highlights the formation of oligarchies
over time. The hypothesis is that the tokens’ tradability is the cause of concen-
tration. To examine this proposition, this paper uses an Agent-based Model to
simulate and analyze the concentration of voting rights tokens post fair launch
under diﬀerent trading modalities. It serves to examine three distinct token
allocation scenarios considered as fair. The results show that regardless of the
allocation, concentration persistently occurs. It conﬁrms the hypothesis that
the disease is endogenous: the cause of concentration is the tokens tradablility.
The ﬁndings inform theoretical understandings and practical implications for
on-chain governance mediated by tokens.
1. Introduction
The digital representation of value and ownership, in the form of fungible and
non-fungible tokens respectively, provides the basis for the token economy. Unlike
traditional economies, the token economy does not rely on trusted third parties
to verify transactions [48], instead distributed ledger technology (DLT) and smart
contracts ensure integrity in a pseudonymous peer-to-peer network of interactions
[6, 57]. Advancements in the token economy with a focus on ﬁnancial services and
products materialized under the heading of Decentralized Finance (DeFi) [55].
DLT enables people to coordinate themselves on-chain, that is, transactions and
interactions are “mediated by a set of self-executing rules [i.e., smart contracts]
deployed on a public blockchain” independently from central control [24, p. 1].
To achieve decentral control in DeFi, , developers created and allocated so-called
voting rights tokens – (fungible) tokens that stipulate voting entitlements to initiate
changes to a public blockchain platform [32]. An example is the decentralized
exchange (DEX) Uniswap, a platform which uses smart contracts to automate the
exchange of fungible tokens of the Ethereum protocol. Its voting rights token, UNI,
allows holders to cast votes and decide upon the use of resources stored in a treasury
(deﬁned in a smart contract). The distribution of voting rights tokens, however, is
considered as controversial given that the initial allocation often favors a minority of
1
arXiv:2208.10271v1  [cs.CR]  15 Aug 2022

---

## Page 2

2 DELGADO, BARBEREAU, AND PAPAGEORGIOU
insiders (e.g., developers, investors, etc.). Tokens allocated to insiders are common
within Initial Coin Oﬀerings (ICOs) [10], hence a diﬀerentiation between initial
allocations that favor insiders (labeled, “private”) or those that do not (labeled,
“public”) [19, p. 10]. History repeats itself as insider allocations of voting rights
tokens are common in DeFi [5].
One outlier to insider allocations is Yearn Finance. Its core developer, Andre
Cronje, denoted that in DeFi voting rights tokens are majoritarily allocated to a
community of “friends and family” [14] – impossibly leading to decentral control.
As solution, he used a type of initial token allocation for the voting rights tokens of
Yearn Finance (YFI) — the fair launch – whereby all community members have an
equal opportunity to receive a portion of the initial supply [46]. Though in theory
this allocation strategy achieves equity through principles of fairness [39], reality
looks dire in the long run: Barbereau et al. [4] demonstrate how, as with all other
voting rights tokens in DeFi, for YFI concentration of wealth and voting power
persists.
Because holders rarely use these to cast votes, Barbereau et al. [5] denote a com-
mon theme and propose a purposefully descriptive theory of voting rights tokens as
justiﬁcation for concentration: they are tradable assets on cryptocurrency markets.
This description may not seem surprising against the consideration that wealth
in the token economy is concentrated (c.f. concetration in Bitcoin and Ethereum
[22]), and so are capital markets more broadly [37]. Indeed, the common feature of
tradability appears to justify, on an intuitive level, the expectations that “wealth
trickles up in free-market economies” [8].
The hypothesis whether the experiment of Andre Cronje’s fair launch was inher-
ently doomed to fail given that the underlying tokens are tradable remains untested.
Taking the principle of a ’fair’ launch (n.b., all tokens are allocated fairly at initial-
ization), one can consider weather alternative allocations are successful in achieving
decentral control in the long run. Correspondingly, to challenge this hypothesis,
this article addresses the following research questions:
RQ1: Does trading behavior aﬀect voting rights token distributions over time?
RQ2: Do alternative, ’fair launch’ token allocations aﬀect voting rights token
distributions over time?
Provided the ﬁnancial context in which these novel governance structures are
deployed, our research topic – ’fair launch’ token allocations – is of importance to
Information System (IS) and requires multidisciplinary perspectives [49]. Hence, we
lean on previous theory on governance of public protocols and token design, and use
quantitative methods rooted in simulation. Guided by an ambition “for discovery
and explanation” [7, p. 516], we adopt agent-based modeling (ABM) to simulate
the trade and eventual distribution of voting rights tokens post three distinct ‘fair
launch’ allocations (n.b., scenarios denoted Sn). The developed model is going
from “real world to simulation world” [7, p. 516], an approach that is particularly
suitable to the exploration of novel phenomena – here, the fair launch. Within
IS, the utility of ABM for the study of phenomena with “nonlinear behavior” [23,
p. 158] is well-recognized. At large, the discipline is receptive of contributions
emerging from simulation research [15, 56, 7], justifying the use of ABM for this
study.
Davis et al. [15, p. 482] advise to ground the model within “simple theory”;
theory, that provides the “basic concepts and process that describe a phenomenon”

---

## Page 3

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 3
[7, p. 506]. Here, we focus on governance of public protocols (Section 2). To
establish further “epistemic credibility in the simulation model” [7, p. 517], aside
from theory (deductive approach) we use empirical data (inductive approach) from
Yearn Finance (Section 3).
The development of our model (Section 4) is informed by the artiﬁcial cryp-
tocurrency markets designed in Cocco et al. [13] and Ro¸ su and Saleh [42]. Therein,
agents represent traders that are endowed with an amount of ﬁat currency and seek
to acquire the (artiﬁcially created) voting rights tokens (TKNs). The market rules
are loosely based on understandings of clearing houses [27]. To investigate RQ2,
we developed two alternative scenarios to Andre Cronje’s fair launch scenario ( S0)
which respectively consider fairness in egalitarian terms (S1) and ’at random’ (S2).
The principles underlying these allocations build on political philosophy [29, 38].
We measure concentration in terms of the Gini Coeﬃcient [21] and the Shannon
Entropy [45]. With our work we make the following contributions:
• An agent-based model for the analysis of token distributions under various
market conditions reﬂective of trading.
• Simulation results showing how over time, regardless of initial token allo-
cation, concentration is imminent.
• Extended understandings on tokenomics to formerly include token alloca-
tions as part of governance parameters.
2. Related Work
2.1. Governance in Public-protocols. Bitcoin [31] led to a burgeoning move-
ment of developers that saw decentralization beyond technical terms; not least, as
an ambiguous mix of political, economic, and organizational ideals [44] that mate-
rialized in the emergence of alternative protocols. Commonly the next generation
of DLT includes smart contracts and the possibility to deploy tokens [6, 57]. While
in public protocols, ’decentralization’ in technical terms is achieved, in political
terms, it is often contentious [44]. Over the decision to increase the size of Bitcoin
blocks, community debates led to an outright ”civil war” [16, p. 8] that pitted par-
ties against each other over socio-political motives. The core developers, who act
as gatekeepers to protocol changes, eventually took an autocratic decision against
that increase – a behavior pejoratively described as ”senatorial” [34]. The Ethereum
protocol, too, faced its share of controversy: following an exploited smart contract
bug the Ethereum Foundation’s leaders decided to irreversibly fork the ledger [18].
Against this backdrop, Penzo and Selvadurai [36, 19] denote how in public permis-
sionless protocols, governing communities resort to informal adjudications, typically
“immune [...] from state scrutiny”.
Consequently, scholars distinguish between on-chain and oﬀ-chain governance.
The former refers to rules that enforce the ’code-is-law’ dictum [54]; in other
words, using smart contracts to deﬁne governance mechanisms and structures (“now
the code runs itself”) [40]. The informal resolution mechanisms in Bitcoin and
Ethereum, however, are examples that demonstrate the shortcomings of the ditcum
and shed light on ulterior power structures [54, 16, 18]. Oﬀ-chain governance refers
to the formalization of control via the intermediary of endogenous (e.g., through
the foundation of institutions such as consortia, cooperatives, etc.) or exogenous
(e.g., national laws, regulations, standards, etc.) structures [40, 58].

---

## Page 4

4 DELGADO, BARBEREAU, AND PAPAGEORGIOU
2.2. Governance in Decentralized Finance. Early research on DLT praised
the “ability to cut out the middleman” [50] in ﬁnancial applications. With Decen-
tralized Finance (DeFi), expectations became reality in early 2020. The certainly
powerful premise to interact without intermediaries to lend or stake tokens (in ex-
change for high interest and other rewards) generate a signiﬁcant buzz. Uniswap
and SushiSwap are DEXs; Aave and Compound oﬀer decentralized lending services;
Synthetix and UMA oﬀer decentralized derivatives; and Nexus Mutual provides a
decentralized insurance model [2]. All of these include a respective Decentral-
ized Autonomous Organization (DAO) plus voting rights tokens and belong to
the Bloomberg Galaxy DeFi Index (Total value locked approximately $43 billion in
late April 2022). Rightfully, Subramanian [47] denoted how decentralized electronic
marketplaces can, “if successful, complement and rival” traditional ones.
Within DeFi, beyond improvements made to the ﬁnancial value chain [43], ex-
periments were made at implementing governance structures fully on-chain; most
notably, by embedding voting rights into tokens. These tokens grant holders the
capacity to cast votes on proposals. While the features of these tokens are con-
textual to the platform, the majority of these follow the fungible token standard
ERC-20. Like most cryptocurrencies, they are tradable on regular and decentralized
exchanges [4]. By nature, the study of these tokens is at the intersection of research
on blockchain governance and tokenomics – a subdomain of cross-disciplinary re-
search on DLT.
Oliveira et al. [32, p.8] deﬁne ”Governance Parameters” of tokens as those pa-
rameters that ”relate to what [it] eﬀectively represents and how this connects to the
way the platform is governed and managed”. The authors introduce three param-
eters (Table 1): (1) ”Representation” (the type of asset represented by a token),
(2) ”Supply” (the way tokens are distributed), and (3) ”Incentive system” (the
way a token exerts inﬂuence over the network and/or its holder). Our scope is on
token allocations and distributions, hence of primary relevance being the ”Supply”
parameter. Oliveira et al. [32, p. 9] note how ”Supply” strategies can either be on
a one-time basis (”ﬁxed”) or following increments (”schedule-based”). Tokens can
also be ”pre-mined” (or ”pre-sold” [19]), that is a portion of the tokens is created
and distributed before the oﬃcial launch date.
Table 1. Excerpt of the Token Classiﬁcation proposed in Oliveira
et al. [32].
Governance Parameters
Representation Digital Physical Legal
Supply Schedule-basedPre-mined,scheduleddistribution
Pre-mined, one-oﬀdistribution Discretionary
Incentive systemEnter PlatformUse PlatformStay Long-TermLeave Platform
For the supply of voting rights tokens, whose fair deployment is motivated by
a normative ambition of political decentralization, the story is more ambiguous.
Uniswap developers pre-mined a part of all voting rights tokens (UNI) and allocated
some to a group of insiders. Among others, the DeFi projects SushiSwap (SUSHI)
and MakerDAO (MKR) followed similar paths, opting for an allocation that favored
insiders. Over time, in all of these cases, wealth concentration was eminent [5].

---

## Page 5

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 5
Concentration of wealth and power is inherent to human societies and economic
systems [37]. Pareto [33] exposed the land concentration in the Italian novecento;
subsequently lending his name to the Pareto Principle. Financial markets are no
exception to the principle [28]. In cryptocurrency markets the same occurs: both
Bitcoin and Ethereum have centralized token distributions, and the trend appears to
only increase [22]. This is true even in the case of Proof-of-Stake cryptocurrencies
where the project’s security is closely tied to the level of dispersion [42]. When
it comes to voting rights tokens, Barbereau et al. [4] identiﬁed that the level of
concentration among voting rights tokens is even higher, highlighting cases where
a handful of people hold more than 50% of all tokens.
Andre Cronje’s project Yearn Finance (YFI) sought to eliminate favoritism and
insider allocations [46]. By opting for the ﬁrst, ﬁxed supply strategy, YFI were
not allocated to a minority of insiders. The implemented fair launch followed the
principle of ’fair equality of opportunity’ [39]; eﬀectively, the idea that each user
has the same opportunity to obtain YFIs. Despite its failure to achieve an equitable
distribution over time [4], at least in theory, a ﬁxed initial token allocation that is
’fair’ would help achieve ambitions of decentral control.
2.3. Agent-based modeling. ABM is a computational method used to simulate
the actions and/or interactions of autonomous agents in order to understand how
systems behave and what determines outcomes [26]. As analytical method, appli-
cations of ABM are found in a variety of disciplines from energy and pathology
to risk management and ﬁnance. Scholars acknowledged the value and potential
of ABM for IS research given its methodological and analytical versatility to in-
vestigate systems whose ”emergent properties unfold over time” [23, p. 158] and
value to generate theory [15]. The literature review of Beese et al. [7] illustrates the
breadth of ABM applications in IS – citing the potential for researchers to embed
theory in the exploration of complex phenomena.
For the study of cryptocurrencies and blockchain-based systems at large, schol-
ars applied ABM in several contexts. Bornholdt and Sneppen [9] proposed a model
to study the emergence of cryptocurrencies vis-` a-vis Bitcoin – considering factors
such as trading, mining of new coins, and agent-to-agent interactions. Their ﬁndings
show that Bitcoin may be interchangeable with cryptocurrencies of similar charac-
teristics. Cocco et al. [13] built an artiﬁcial cryptocurrency marketplace based on
an order book simulation of the Bitcoin market where agents trade autonomously.
Their model is able to reproduce real price formations and market volatility; hence,
our adaptation of it in this work. Ro¸ su and Saleh [42] propose an environment to
model the behavior of investors/agents in a Proof-of-Stake (PoS) based blockchain
of cryptocurrency issuance. They denote, contrary to expectations, that agents
seek to stabilize their portfolio instead of accumulating more wealth.
3. Data preparation
DeFi platforms, for the most part, are built on public-permissionless ledgers.
Generally, these ledgers provide a rich source for the collection and analysis of
quantitative data [5]. Chen and Bellavitis [12] observe that 80% of DeFi platforms,
are in fact, built on the Ethereum ledger. Ethereum records a variety of details,
not least on tokens, data about their creation, initial distribution to exchanges, and
transaction history between addresses. The fair launch was originally created as

---

## Page 6

6 DELGADO, BARBEREAU, AND PAPAGEORGIOU
part of Yearn Finance, hence it’s practice informs our study inductively [7]. Specif-
ically, data on Yearn Finance is used to (1) deﬁne the base scenario S0 (”Cronje”),
(2) ’feed’ our model based on reality, (3) calibrate the model, and (4) validate our
model. For (2), we also extracted the price of YFI (from CoinGecko.com) and the
Crypto Fear & Greed Index (FGI). The graphs for these two additional data sources
are presented in Figure 1.
2020-07 2020-10 2021-01 2021-04 2021-07 2021-10 2022-01 2022-04
Time(t)
20
40
60
80FGI
Fear & Greed Index
2020-07 2020-10 2021-01 2021-04 2021-07 2021-10 2022-01
Time(t)
0
10000
20000
30000
40000
50000
60000
70000
80000YFI/USD
YFI/USD
Figure 1. Graphs for the Crypto FGI and YFI price.
Yearn Finance is built on Ethereum and uses the ERC-20 token standard for
its voting rights token YFI. YFI was launched with a ﬁxed supply with no early
allocation of tokens to insiders. Instead, the initial supply of 30,000 tokens in cir-
culation was distributed via a liquidity providing scheme. Users could earn YFI by
supplying liquidity into three distinct pools, allowing every user, regardless of their
initial capital or other restrictions, to earn a portion of YFI’s supply proportion-
ate to the contributed liquidity. This allocation was originally described as a fair
launch [46].
To generate data for our model, we used Dune to extract the addresses that hold
YFI from Ethereum’s public ledger. Then, we organized the data such that we could
determine how many tokens are owned daily by each address. Finally, we excluded
a number of address ’types’ from the dataset: smart contracts (since they never
utilized their voting rights, despite holding YFI [5]); addresses holding YFI valued
less than $1 (since these rarely vote or trade their tokens owing to Ethereum’s gas
fees being signiﬁcantly higher than the token’s value), and; addresses used to burn
tokens (e.g., 0x000. . . 0000) (since no one controls them and YFI is eﬀectively taken
out of circulation). Table 2 presents our ﬁnal data set.
Table 2. Overview of data extraction.
Extracted Addresses 96,227
Addresses used in Analysis 86,752
Extraction Period 2020-07-17 - 2021-08-15
Following the ﬁnalization of our data set, we utilized Exploratory Data Analysis
(EDA) to determine the model’s initial conditions and variables. We chose Sep-
tember 1st, 2020 (i.e., 45 days after the project’s launch) as the starting date since

---

## Page 7

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 7
at that point the Yearn Finance fair launch took place; in other words, all tokens
were allocated to users, but the market’s inﬂuence on the token distribution was
still limited. Using the Anderson-Darling test [3] and the Akaike information crite-
rion [1], we identiﬁed that the probability distribution of the initial YFI allocation
follows a Lomax distribution (λ = 0.4,α = 0.5). Relying on the same methods, we
found that the daily number of new addresses that hold YFI increases following an
asymmetric Laplace distribution ALap(0.71, 58, 76).
4. The model
The proposed model for initial allocations builds on an agent-based artiﬁcial
cryptocurrency market (c.f. [13]). Subsequently, we describe the model in terms
of the agents, the market rules, and the trading behavior. Then, we describe the
initial token allocations of the three fair launch scenarios. Finally, we introduce the
metrics used to evaluate concentration over time.
4.1. The agents. For our model, we take time steps t∈ N+ ={1, 2, 3,...} which
correspond to a day and a new trading round. The ﬁrst time step in our model
is at t = 45. For each time step, we deﬁne agents i∈ I as the addresses that
hold voting rights tokens (TKNs) at the beginning of each trading round. The
number of agents at time step t is given by NA(t)∈ N+. At the beginning of each
trading round, a subset of I is selected to trade TKNs (the selection mechanism
as well as the trading strategy of agents is described subsequently) and new agents
(endowed solely with ﬁat currency) enter the market with the desire of placing buy
orders to acquire TKNs. The new agents entering ( NA(t + 1)−NA(t)) follows
ALap(0.71, 58, 76) for every t > 45. In other words, at each trading round the
95% conﬁdence interval (CI) of the number of new agents is [114 , 119]. We run
our model for 347 days ( t = 392) and the 95% CI for the ﬁnal number of agents
(NA(392)) is [47113, 50890].
Agents are endowed with ﬁat holdings fi(t) and TKN holdings yi(t). Based on
Dragulescu and Yakovenko [17] and Brzezinski [11], the amount of ﬁat held by both,
individual agents at t = 45 and those agents entering the market at each trading
round, is drawn from a Pareto distribution with α = 2.1 and min(fi(t)) = $400k
for the richest 10% of our agents and from an Exp( 1
40000) for the remaining bottom
90%. The amount of TKNs held by agents at t = 45 depends on the chosen fair
launch scenario Si with i∈{ 0, 1, 2}.
Independently of ﬁat or TKN holdings, each agent i is assigned to one of two
populations, Diamond Hands (DH) and Random Traders (RT), representative of
respective trading strategies. DHs are risk averse traders, who pragmatically invest
in the market and are more likely to not incur in trades. RTs, then, are agents who
enter to market for a variety of reasons (e.g., portfolio diversiﬁcation, gambling,
etc.). Following Cocco et al. [13], the agent populations is divided into 30% DHs
and 70% RTs.
4.2. The market rules. The TKN market is given by a mechanism comparable
to a clearing house; whereby, buy and sell orders are accumulated over time and
cleared (’matched’) periodically [27]. The purpose of the model and developed
market is not exploring how price is formed; instead, it is to simulate how tokens
circulate (and concentrate) based on clear conditions. The mechanism we utilize
is not a formal clearing house as it does not account for price formation, nor does

---

## Page 8

8 DELGADO, BARBEREAU, AND PAPAGEORGIOU
it include adjustments of price after every transaction over time. Instead, at each
time step the TKN price Tp(t) is updated based on YFI’s historical price data.
Agents can autonomously decide whether they are willing to trade. Agents do not,
however, have information about the orders other agents are placing. The scope of
this work and the developed ABM is on token concentration, and not the way price
is formed. Clearing houses oﬀer an easy to deploy mechanisms to match orders
between agents with limited computation overhead and a realistic movement of the
tokens.
At t≥ 45, the total number of tokens in circulation is given by the constant
Ts = 36666. For the trade of TKNs, we model a two-sided market with a num-
ber of buyers, each willing to buy TKNs, and several sellers, each willing to sell
TKNs. Additionally, at every time step the buy/sell orders created by the agents
are matched in a ﬁrst in ﬁrst out method, and at the end, the unmatched orders
are canceled.
4.3. Trading behavior. Depending on the population agents belong to, they exert
a choice – to trade ( T ) or not to trade – at every time step t. This decision is
given by the probability Pi(T ). For RTs, who randomly wish to trade following a
uniform distribution,Pi(T ) = 0.5. For DHs,Pi(T ) is dependent on two independent
variables. First, the Fear & Greed Index (FGI (t)) which ﬂuctuates between a value
of 0 (“Extreme Fear”) and 100 (“Extreme Greed”) [53]. In our case, we consider
the values of the index as “Extreme” (FGIe) when FGI (t)>th h orFGI (t)<th l,
and “Normal” (FGIn) when thh > FGI(t) > thl with thh and thl thresholds for
the extreme values of Fear & Greed Index. Second, the agent’s wealth ( W ), given
by an agent’s individual holding denominated in ﬁat fi(t). An agent’s wealth at
time t is considered “High” ( Wh) when fi(t) is above the 90th percentile of the
wealth distribution and “Low” otherwise. Therefore, the probability of a DH agent
to trade is given by:
Pi(T ) =P (T∥FGIe,Wh)P (FGIe)P (Wh) +P (T∥FGIe,Wl)P (FGIe)P (Wl)
+P (T∥FGIn,Wh)P (FGIn)P (Wh) +P (T∥FGIn,Wl)P (FGIn)P (Wl)
(4.1)
If an agent is willing to trade, the subsequent decision to execute a buy or sell
order depends on the population they belong to. For RT, the buy and sell orders
follow a Bernoulli distribution with p = 0.5. Initially, the same holds for DH but in
their case the probability is calibrated at a later stage based on the data from Yearn
Finance (c.f. Section 5). In the trading behavior, we do not consider protocols that
allow to stake/sell voting rights token entitlements (e.g., Bribe Protocol) as these
add yet another degree of complexity.
At each time step the amount of ﬁat an agent spends on buying tokens follows
aN (µ = fi(t)
2 , σ= µ
3 ) and the number of TKNs an agent sells follows a N (µ =
yi(t)
2 , σ= µ
3 ).
4.4. The fair launch scenarios. Our simulation is set up around three distinct
scenarios representative of initial token allocations understood as ’fair’. Their de-
sign is informed on the basis of the epistemic dichotomy described in Beese et al.
[7]. The base scenario S0 is created following an inductive approach (its design
is informed by data extracted from Yearn Finance) and the distribution of Ts is

---

## Page 9

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 9
modeled to follow a Lomax distribution with λ = 0.4 and α = 0.5. The artiﬁcially
created fair launch scenariosS1 andS2 are designed following a deductive approach
on the basis of theory.
The ﬁrst alternative scenario S1 (“Bentham”) considers ’fairness’ in egalitarian
terms: equity is achieved in terms of uniformity such that the total supply of tokens
is divided equally among the participants. Formerly, it considers Jeremy Bentham’s
dictum that “everybody to count for one, nobody for more than one” [29], without
consideration of individual interests or material situation. For S1, Ts is uniformly
distributed such that each agent i at t = 45 holds yi(45) = Ts
NA(45).
The second alternative scenario S2 (“Rawls”) considers randomness, and more
speciﬁcally, the principle of a lottery as ’fair’: equity is achieved in terms of a
token allocation – at random –, and in our case, following a Normal distribu-
tion. It re-hashes the idea that the outcome of each individual’s position, like
the outcomes of ordinary lotteries, is a matter of good or bad “luck” [38, p. 74-
5]. Randomness and chance are central to the theory of Darwinian evolution [51].
ForS2, Ts is distributed among agents following a truncated Normal Distribution
(µ = 0.103,σ = 0.192) deﬁned on [0,∞].
In sum, we thus investigate two additional scenarios aside (Table 3). While
keeping the market conditions and parameters ﬁxed, changing the initial allocation
of tokens provides further insight into the concentration of wealth.
Table 3. Initial token allocation scenarios.
Scenario Allocation Perspective
S0 “Cronje” (Yearn Finance) Everyone gets the same opportunity Social liberalism
S1 “Bentham” Everyone gets the same Egalitarianism
S2 “Rawls” Everyone gets a random amount Darwinism
4.5. Metrics. Given the aim of analyzing the distribution of voting rights tokens
post fair launch, select metrics are computed at every time step. These metrics are
the Gini Coeﬃcient [21] and the Shannon Entropy [45]. This choice was made based
on an evaluation of related works seeking to quantify and measure the distribution
of tokens in a system; notably, as discussed in Gervais et al. [20], Gochhayat et al.
[22], and Barbereau et al. [4].
The Gini Coeﬃcient is typically used to assess the distribution of wealth in a
given country. It was, however, also applied to study wealth distribution in Bitcoin
and Ethereum [22] as well as DeFi platforms and voting rights tokens distribu-
tions [4]. For our model, the Gini G indicates the concentration of wealth, and in
particular the concentration of TKNs amid agents. The Gini is given by:
(4.2) G =
NA∑
i=1
NA∑
j=1
|pi−pj|
2NA·
NA∑
j=1
pj
wherepi corresponds to the share of TKNs held by agenti andNA the total number
of agents. It is maximized through the Dirac distribution δi0, i.e., pi0 = 1 for some

---

## Page 10

10 DELGADO, BARBEREAU, AND PAPAGEORGIOU
i0∈{ 1,...,N A} and pi = 0 for all i̸= i0, and minimized through the uniform
distribution, i.e., pi = 1
NA
for all i.
The Shannon Entropy was developed to assess the information loss in telecom-
munication networks [45]. The Normalized Shannon Entropy (NSE), then, takes
values between 0 and 1, and determines the unpredictability of a distribution. We
assume that a system where the voting tokens are distributed can exhibit high
unpredictability (1), given that more agents inﬂuence the outcomes. The NSE is
given by:
(4.3) NSE = −
NA∑
i=1
pi log(pi)
logNA
where 0 log(0)≡ 0 by convention since lim
p→0
p log(p) = 0. It is 0 for δi0 and 1 for
the uniform distribution (i.e., the extremes are interchanged compared to the Gini
coeﬃcient). To ease graphical observation, we opted to consider 1-NSE instead of
NSE such that, as in Gini, higher values correspond to higher degrees of centrality.
5. Implementation and Calibration
The model was implemented in Python using the MESA framework [25]. The
simulation took about 4.5 hours in a 10 Cores M1-Pro CPU with 32GB of RAM.
Due to this computational burden. The calibration of the model was performed in
a High Performance Computing (HPC) facility. The hardware provided, depending
on the allocation of the HPC, were a Dual Intel Xeon Broadwell or Skylake with
128GB of RAM.
For the calibration, we followed the recommendations of Richiardi et al. [41,
p. 4] whereby a “full exploration” of the parameters is required. To do so, we
implemented a grid search (GS) to ﬁnd a set of optimal values of parameters. GS
performs an exhaustive search over all the possible combinations of parameters
until ﬁnding the optimal one. The goodness of the ﬁt and the stopping condition
of GS are computed using Root Mean Squared Error (RMSE) and Mean Absolute
Percentage Error (MAPE) between the actual (extracted from the dataset) and
calibrated model. The respective equations are given by:
(5.1) RMSE =
√
(1
n
) n∑
i=1
(xi− ˆxi)2 and MAPE = 100
n
n∑
t=1
⏐⏐⏐⏐
xi− ˆxi
xi
⏐⏐⏐⏐
where xi is the actual observation and ˆxi is the simulated value.
The optimization was executed over all eligible parameters. The FGI threshold
takes values from 0 to 100. For all other parameters, we considered values between
0 and 1. The optimal parameter values are displayed in Table 4.
The optimal values of the DH/RT population ratio were close to the ratio used
by Cocco et al. [13]. Therefore, we ﬁxed it at 30% DHs and 70% RTs. Similarly,
the buy probability was optimized to be 70% for DH. For the DHs, we found
that high trading probabilities indeed lead to lower error rates (Table 5). This,
as demonstrated in Ro¸ su and Saleh [42], represents an expected behavior as more
trading is linked with higher wealth concentration. Diametrically opposed to the
high trading probability parameter set, is an artiﬁcially created parameter set,
with relatively low trading probabilities. The error rates for this parameter set
are relatively worse than the optimal set of high trading probabilities. We also

---

## Page 11

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 11
Table 4. Optimal parameter values.
Parameter Description Optimal Value
PDH(Buy) Buy probability of DH 0.7
DH/NA(t) Population share of DH 0.3
thh FGI threshold high 80
thl FGI threshold low 20
P(T∥FGIe) Trading probability under extreme market conditions 0.7
P(T∥Wh) Trading probability under high wealth 0.7
P(T∥FGIn) Trading probability under normal market conditions 0.8
P(T∥Wl) Trading probability under low wealth 0.9
artiﬁcially generated and investigated a compromise between the two sets without
extreme trading probabilities.
Table 5. Diamond Hand trading probabilities parameter sets
with their correspondent error rates
Parameters High probability Medium probability Low probability
P(T∥FGIe) 0.7 0.3 0.1
P(T∥Wh) 0.7 0.4 0.1
P(T∥FGIn) 0.8 0.3 0.2
P(T∥Wl) 0.9 0.5 0.2
Pi(T) 0.77 0.38 0.15
MAPE 0.1859 0.224 0.255
RMSE 0.007 0.009 0.012
In sum, we investigate three scenarios (Table 3) under three trading probabil-
ities (Table 5). The results might vary due to the stochastic nature of ABM. In
anticipation of this variance and to ensure the robustness of our results, we applied
a Monte-Carlo method by repeating the experiment of the three simulation sets
within the HPC; resulting in more than 1000 simulations (or, approximately 300
per set of trading probabilities). For all simulations, the agents can place buy or
sell orders depending on the probability deﬁned in PDH = 0.7 for DH (optimized
value) and PRT = 0.5 for RT (constant) respectively.
6. Simulation results
6.1. Eﬀects of trading probability on the three scenarios. The ﬁrst simula-
tion considers the model’s behavior under high trading probability (Figure 2). High
trading probability refers to a relatively high likelihood for DH agents to place an
order. The second simulation is the artiﬁcially created edge case with low trading
probabilities (Figure 3). It is diametrically opposed to the former simulation and
explores the behavior of DH agents when the market dictates a relatively low like-
lihood to place a trade. (The graphs for S0 and S2 are visually coinciding.) The
third simulation set was created artiﬁcially as middle ground between the high and
low trading probabilities (Figure 4).

---

## Page 12

12 DELGADO, BARBEREAU, AND PAPAGEORGIOU
45 103 161 219 277 335 392
Time(t)
0.0
0.2
0.4
0.6
0.8
1.0Gini
45 103 161 219 277 335 392
Time(t)
0.0
0.1
0.2
0.3
0.4
0.51-NSE
Extracted S0 Cronje S1Bentham S2 Rawls
Figure 2. Simulations for the parameter set representative of
high trading probabilities.
45 103 161 219 277 335 392
Time(t)
0.0
0.2
0.4
0.6
0.8
1.0Gini
45 103 161 219 277 335 392
Time(t)
0.0
0.1
0.2
0.3
0.4
0.51-NSE
Extracted S0 Cronje S1Bentham S2 Rawls
Figure 3. Simulations for the parameter set representative of low
trading probabilities.

---

## Page 13

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 13
45 103 161 219 277 335 392
Time(t)
0.0
0.2
0.4
0.6
0.8
1.0Gini
45 103 161 219 277 335 392
Time(t)
0.0
0.1
0.2
0.3
0.4
0.51-NSE
Extracted S0 Cronje S1Bentham S2 Rawls
Figure 4. Simulations for the parameter set representative of
medium trading probabilities.
Across all trading probabilities, for S0 and S2, the Gini values of the simulated
data overlap considerably with the extracted YFI data fort≥ 100. Until the end of
the simulation time frame, the Gini values of the extracted data diverge by at most
by 1.1% on S0 and 1.7% on S2 across all trading probability scenarios. The close
ﬁt between the extracted data from Yearn Finance and the three simulations, and
in particular for S0, is expected given the performed optimizations. The exception
to the convergence is S1, whose graph is below the extracted data in all three
simulations. It appears that an egalitarian initial token allocation would then lead
to relatively less concentration in the time frame of the simulation.
We expect variations in the initial values of Gini and NSE because, even though
our model starts with the same number of agents at each simulation, the initial
token allocation is not ﬁxed and as discussed above, the token distribution in S0
follows a Lomax distribution. Regardless of the scenario and trading probability,
after the 1-NSE stabilizes, all distributions move in a lateral and parallel direction
with regards to the extracted 1-NSE values from YFI.
Although our simulation results seem to coincide with the Yearn Finance data
for Gini we observe high variations of the NSE. This divergence may be interpreted
in two ways. At inception of Yearn Finance some contracts held a large amount of
YFI and distributed them shortly after. Given the scope of our model we did not
consider such behavior. We argue that the smart contracts that emitted YFI rapidly
result in sharper rises in the metrics’ values. This is consistent with our ﬁndings
which indicate that when there is a large amount of YFI accessible for trading in
a short period of time, the metrics rise. The second interpretation pertains to the
token supply (Ts). Formerly, the supply of YFI was “schedule-based” [32]: it began
with a supply of 30000 FYI allocated following the fair launch, and subsequently
an additional 6666 YFI tokens were distributed the same way. For simplicity, we
start with 36666 supply dispersed to the starting holders in our simulations. Again,
the distribution of 6666 YFI in a short period of time theoretically results in higher
concentration than our model, which in contrast, distributes YFI more slowly over
time. The schedule-based supply of YFI can be observed in the ’bumps’ around
t=100. While the change is more subtle in Gini, within 1-NSE the change is more

---

## Page 14

14 DELGADO, BARBEREAU, AND PAPAGEORGIOU
clearly observable. This is due to the comparatively higher sensitivity of the latter
metric with regards to minor ﬂuctuations [5] which can also be observed in the
Figures above, where the standard deviation of NSE is substantially higher than
that of Gini.
6.2. Actual concentration of wealth amid whales. Following the three simu-
lation sets focusing on the trading probabilities, we performed a more granular anal-
ysis of the actual concentration of TKNs amid the population of agents (NA(392)).
Particularly, we sought to investigate the share of agents that hold 90% of all to-
kens in circulation. These agents are so called whales, “ ‘wealthy’, above-average
token-holders” [5, p. 20]. In consideration of the amount of available data following
the Monte-Carlo simulations, here we present a more feasible analysis on the basis
of the results from the ﬁrst simulation round. The results are presented in Table 6.
Table 6. Share of agents that control 90% of TKNs in circulation
at t=392.
High probability Medium probability Low probability
Scenario Percentage Actual Percentage Actual Percentage Actual
S0Cronje 2,59% 1137 / 43830 2,63% 1188 / 45092 3,63% 1499 / 41248
S1Bentham 10,80% 4777 / 44214 10,73% 4847 / 44950 11,38% 4999 / 43895
S2Rawls 0,76% 376 / 49397 1,29% 572 / 44300 2,83% 1250 / 44056
Unsurprisingly, in consideration of the values metrics took in the previous anal-
ysis, we observe a concentration of TKNs in the hands of the few. These few
individuals are de facto in control as they may exert signiﬁcant political pressure.
In relative terms, as reﬂected in the metrics, the egalitarian allocation S1 shows
that the actual number of whales is higher. Regardless, our results are aligned with
the timocratic description of Barbereau et al. [4].
6.3. Extending the simulation of S 1 “Bentha”. After running the ﬁrst set
of simulations, we opted to run a separate simulation to explore whether S1 indeed
demonstrates more or less concentration over time. To do so, we extended the
simulation rounds from t=392 (August 15th 2021, the last data point extracted
from Yearn Finance) to t=545 (March 1st 2022, the last point of the simulations).
This represents an extension of 44.39%. The results of the simulation are in Figure
5.
From our previous simulations on the eﬀects of diﬀerent trading probabilities, we
observe how S1 Bentham’s initial token allocation positively aﬀects both metrics.
It is to be expected that an equal distribution of tokens at origination will reduce
concentration, at least early on. In this simulation we observe similar phenomena
to what was demonstrated in Ro¸ su and Saleh [42]: even though the delayed eﬀect
that an egalitarian initial token allocation like the one simulated might generate,
concentration is, at least judging from our simulations, inevitable in the long run.
To corroborate that, we ﬁtted linear regressions (LR) on Gini from the three trading
scenarios. In the worst case scenario, the slope of the LR is 4 ∗ 10−4.

---

## Page 15

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 15
45 105 165 225 285 345 405 465 525 590
Time(t)
0.0
0.2
0.4
0.6
0.8
1.0Gini
45 105 165 225 285 345 405 465 525 590
Time(t)
0.0
0.1
0.2
0.3
0.4
0.51-NSE
Extracted
High Trading Probability
Medium Trading Probability
Low Trading Probability
Figure 5. Simulation for the Bentham scenario under the three
trading probabilities.
7. V alidation and verification of the model
Validation is an essential part of ABM [15]. There are numerous techniques
for validation, all of which are used to establish credibility in the simulations [7].
To validate our model we opt to use the event validity and parameter variability
(sensibility analysis) techniques.
For the event validity, simulated events are compared with those occurring in
real world systems [7]. Speciﬁcally, we take the share of agents that control 90% of
TKNs in circulation between t=1 and t=392 for S0 Cronje. (The values at t=392
are identical to those displayed in Table 6.) The real world (extracted) data is
taken from Yearn Finance (c.f. Section 3). The comparison between these datasets
is displayed in Figure 6.
45 103 161 219 277 335 392
Time(t)
0
10
20
30
40Percentage
Simulated agents
Extracted addresses
Figure 6. Veriﬁcation through event validity for the share of
agents that control 90% of the circulation between Yearn Finance
and S0.

---

## Page 16

16 DELGADO, BARBEREAU, AND PAPAGEORGIOU
The model during calibration was not given any information regarding the token
concentration. From the Figure, we visualize how both the simulated and real world
values converge after approximately 100 steps (100 natural days). At the end of
the simulations the diﬀerence is 0.4 percent points. These results present a solid
base for the validity of the model as it closely replicates reality [15].
For the parameter variability, input parameters are modiﬁed and the resulting
changes analyzed [7]. We evaluated the impact of alternative DH/RT population
ratios – with 10%, 30%, and 50% DH – on the scenario S0 relative to reality. The
change was observed in terms of the metrics. Here too, we applied the Monte-Carlo
method using the HPC. Figure 7 gives the simulated metrics for the three ratios
along the actual distribution of Yearn Finance.
45 103 161 219 277 335 392
Time(t)
0.65
0.70
0.75
0.80
0.85
0.90
0.95
1.00Gini
45 103 161 219 277 335 392
Time(t)
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.451-NSE
Extracted 10% DH 30% DH 50% DH
Figure 7. Impact of diﬀerent population allocations on NSE and
Gini
The procedure yields variability between the diﬀerent population ratio and re-
ality. We deﬁne the ∆ as the diﬀerence between the simulated scenario and the
extracted data. The simulations with 50% DH (∆ Gini=0.71%, ∆NSE =25%) per-
forms relatively worse than those with 10% (∆Gini=0.4%, ∆NSE =16.52%) and 30%
(∆Gini=0.015%, ∆NSE =19.65%). In consideration of the ∆ values and Cocco et al.
[13] (who take 70% irrationality), the 30% DH is most appropriate and therefore
justiﬁes the models’ validity [15].
8. Discussion
Using agent-based analysis, we evaluated how trading probabilities aﬀect concen-
tration over time within three distinct scenarios representative of ’fair’ initial token
allocations. Our ﬁndings are consistent with Barbereau et al. [5] timocratic descrip-
tion as the ability to trade voting rights tokens appears to be one of the causes of
concentration (RQ1). Amid all three simulation sets with high, medium, and low
trading probabilities, the scenarios tend towards concentration (RQ2). The con-
centration of wealth in the long term as observed in our constructed ABM aligns
with ﬁndings on the concentration of wealth in Bitcoin and Ethereum [22], and
general understandings of the concentration of wealth and inequalities [37]. The
implications of our ﬁndings are both of theoretical and practical nature.

---

## Page 17

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 17
Our ﬁndings allow to “sharpen” theory [15, p. 440] on tokenomics. Speciﬁcally,
by contributing to the token classiﬁcation of Oliveira et al. [32] and reﬁne the “Gov-
ernance Parameters” in favor a distinction of the “Supply” parameter in terms of
“Distribution” and “Allocation”. The “Distribution” parameter is accounted for
already as it is equivocally used for the “Supply” of tokens. For “Allocations” we
distinguish between “Fair Launch” allocations (such as the ones described) and all
other token allocations that may favor a minority of insiders (e.g., like Uniswap
did). This contribution parallels research on ICOs which account for these ’un-
fair’ allocations as so-called “private pre-sale[s]” [19, p. 10] – a terminology we
adopt here. Table 7 showcases our reﬁnement vis-` a-vis the original classiﬁcation
of Oliveira et al. [32]. While our ﬁndings do not allow to distinguish causation or
correlation between allocation and concentration of tokens over time, the inclusion
of “Allocations” in the token classiﬁcation provides an indication for the normative
ambitions of on-chain governance systems.
Table 7. Italicized reﬁnements to the Token Classiﬁcation of
Oliveira et al. [32].
Governance Parameters
Representation Digital Physical Legal
SupplyDistributionSchedule-basedPre-mined,scheduleddistribution
Pre-mined, one-oﬀdistributionDiscretionary
Allocation Fair Launch ’Unfair’ launch, pre-sale
Incentive systemEnter PlatformUse PlatformStay Long-TermLeave Platform
The practical implications of our ﬁndings are for the design of future gover-
nance systems that leverage voting rights tokens. Our work provided additional
evidence that trading largely determines the extent to which governance power is
concentrated. Hence, the possibility to transfer tokens must be addressed. In prac-
tice, this can be achieved through a new class of tokens described as soulbound.
The introduced deﬁnition refers to “accounts, or wallets, that hold publicly visible,
non-transferable (but possibly revocable-by-the-issuer) tokens” [52, p. 2]. In other
words, the (albeit pseudonymous) identity of a holder is encrypted into an Soul-
bound Token (SBT) that is linked to the respective wallet. The opportunities for
on-chain governance are promising:
• They mitigate Sybil attacks.
• They (could) grant more voting power to reputable holders.
• They enable for “proofs-of-personhood”.
• They allow to correlate between SBTs which support particular causes and
prevent a “tyranny of the majority” [30].
These opportunities provide avenues for research as they require contextual anal-
ysis. To date, we note the application of SBTs for Know-Your-Customer processes
and user credentials as the crypto-asset exchange Binance stipulated the intend to
explore SBT on its native blockchain. Notably, Binance’s SBT BNB would grant
access to speciﬁc functions of the BNB Chain [35].
9. Conclusion
Within the DeFi space, recent scholarship observed the implementation of on-
chain governance mechanisms for DAOs. Voting rights tokens are a key ingredient

---

## Page 18

18 DELGADO, BARBEREAU, AND PAPAGEORGIOU
to implement these mechanisms. The initial allocation of voting rights tokens ought
to follow principles of fairness in order to achieve normative goals of political de-
centralization. The fair launch allocation of Andre Cronje gained prominence as it
did not allocate any tokens to a minority of insiders. However, in practice it fell
short as over time YFI tokens became highly concentrated. On the basis of Cocco
et al. [13] and Ro¸ su and Saleh [42], in this paper we propose an agent-based mod-
eling (ABM) to simulate fair launch initial token allocation. Using the model, we
simulated alternative initial token allocation scenarios understood as ’fair’ [29, 38].
In all of them, independently of market conditions and agents’ willingness to trade,
concentration looms.
The research is subject to a number of limitations. The ﬁrst pertains to the
deﬁned market rules. Though these followed the principles stipulated in Mendelson
[27], the clearing mechanism lacks a formal price clearing method. Additionally,
despite having designed our model on the basis of Cocco et al. [13], we did not
implement limit orders. The second pertains to the awareness of agents. In the
designed model the decision making of individual agent’s does not depend on past
decisions or those of other agents. To address these shortcomings, future work may
build upon and extend our model to include a public order book where agents are
aware about other orders. Further, a distinction may be made between trading
mechanisms and clearing methods on centralized and decentralized exchanges. The
third pertains to the trading behavior of agents. For our simulations, we heavily
rely on the FGI as a proxy for market conditions. Subsequent work could opt for
the use of more granular indicators, such as the price of diﬀerent DeFi assets or
social media data.
Acknowledgments
The authors thank Reilly Smethurst for his friendly review and contributions to
literature. The authors also thank Gilbert Fridgen for his valuable feedback as part
of the ﬁrst submission.
Joaquin Delgado Fernandez is supported by the European Union (EU) within its
Horizon 2020 programme, project MDOT (Medical Device Obligations Taskforce),
Grant agreement 814654. Tom Barbereau is supported by PayPal and the Luxem-
bourg National Research Fund (FNR) – (P17/IS/13342933/PayPal-FNR/Chair in
DFS/ Gilbert Fridgen). PayPal’s ﬁnancial support is administered via the FNR,
and by contractual agreement, PayPal has no involvement in Tom Barbereau’s re-
search. Orestis Papageorgiou is supported by the Luxembourg National Research
Fund (FNR) (C20/IS/14783405/FIReSpARX).

---

## Page 19

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 19
References
[1] H. Akaike. A new look at the statistical model identiﬁcation. IEEE Transac-
tions on Automatic Control , 19(6):716–723, Dec. 1974. ISSN 1558-2523. doi:
10.1109/TAC.1974.1100705. Conference Name: IEEE Transactions on Auto-
matic Control.
[2] H. Amler, L. Eckey, S. Faust, M. Kaiser, P. Sandner, and B. Schlosser. Deﬁ-
ning deﬁ: Challenges & pathway. In 2021 3rd Conference on Blockchain Re-
search & Applications for Innovative Networks and Services (BRAINS) , pages
181–184. IEEE, 2021.
[3] T. W. Anderson and D. A. Darling. Asymptotic Theory of Certain ”Goodness
of Fit” Criteria Based on Stochastic Processes. Ann. Math. Statist. , 23(2):
193–212, June 1952. ISSN 0003-4851. doi: 10.1214/aoms/1177729437. URL
http://projecteuclid.org/euclid.aoms/1177729437.
[4] T. Barbereau, R. Smethurst, O. Papageorgiou, A. Rieger, and G. Fridgen.
Deﬁ, not so decentralized: The measured distribution of voting rights. In
Proceedings of the 55th Annual Hawaii International Conference on System
Sciences, 2022.
[5] T. Barbereau, R. Smethurst, O. Papageorgiou, J. Sedlmeir, and G. Fridgen.
Decentralised Finance’s Unregulated Governance: Minority Rule in the Digital
Wild West. SSRN Electronic Journal, (ID 4001891), Jan. 2022. URL https:
//papers.ssrn.com/abstract=4001891.
[6] R. Beck, C. M¨ uller-Bloch, and J. L. King. Governance in the blockchain
economy: A framework and research agenda. Journal of the Association for
Information Systems, 19(10):1, 2018.
[7] J. Beese, M. K. Haki, S. Aier, and R. Winter. Simulation-based research in
information systems. Business & Information Systems Engineering , 61(4):
503–521, 2019.
[8] B. M. Boghosian. Is inequality inevitable? Scientiﬁc American, 321(5):70–77,
2019.
[9] S. Bornholdt and K. Sneppen. Do bitcoins make the world go round? on the
dynamics of competing crypto-currencies. arXiv preprint arXiv:1403.6378 ,
2014.
[10] T. Bourveau, E. T. De George, A. Ellahie, and D. Macciocchi. The role of
disclosure and information intermediaries in an unregulated capital market:
evidence from initial coin oﬀerings. Journal of Accounting Research , 60(1):
129–167, 2022.
[11] M. Brzezinski. Do wealth distributions follow power laws? Evidence from
‘rich lists’. Physica A: Statistical Mechanics and its Applications, 406:155–162,
July 2014. ISSN 03784371. doi: 10.1016/j.physa.2014.03.052. URL https:
//linkinghub.elsevier.com/retrieve/pii/S0378437114002544.
[12] Y. Chen and C. Bellavitis. Blockchain disruption and decentralized ﬁ-
nance: The rise of decentralized business models. Journal of Business Ven-
turing Insights , 13:e00151, June 2020. ISSN 23526734. doi: 10.1016/j.
jbvi.2019.e00151. URL https://linkinghub.elsevier.com/retrieve/pii/
S2352673419300824.
[13] L. Cocco, G. Concas, and M. Marchesi. Using an artiﬁcial ﬁnancial market
for studying a cryptocurrency market. Journal of Economic Interaction and
Coordination, 12(2):345–365, 2017.

---

## Page 20

20 DELGADO, BARBEREAU, AND PAPAGEORGIOU
[14] A. Cronje. Fair launches, decentralized collaboration, and Fixed Forex.
Medium, July 2021. URL https://andrecronje.medium.com/.
[15] J. P. Davis, K. M. Eisenhardt, and C. B. Bingham. Developing theory through
simulation methods. Academy of Management Review , 32(2):480–499, 2007.
[16] P. De Filippi and B. Loveluck. The invisible politics of Bitcoin: governance
crisis of a decentralised infrastructure. Internet Policy Review , 5(3), Sept.
2016. ISSN 2197-6775. doi: 10.14763/2016.3.427.
[17] A. Dragulescu and V. M. Yakovenko. Exponential and power-law probability
distributions of wealth and income in the United Kingdom and the United
States. Physica A: Statistical Mechanics and its Applications , 299(1-2):213–
221, Oct. 2001. ISSN 03784371. doi: 10.1016/S0378-4371(01)00298-9. URL
http://arxiv.org/abs/cond-mat/0103544. arXiv: cond-mat/0103544.
[18] Q. DuPont. Chapter 8: Experiments in algorithmic governance – A history and
ethnography of “The DAO,” a failed decentralized autonomous organization.
In Bitcoin and Beyond: Cryptocurrencies, Blockchains and Global governance ,
RIPE series in global political economy. Routledge, Taylor & Francis Group,
London; New York, 2017. ISBN 978-0-415-79214-1.
[19] G. Fridgen, F. Regner, A. Schweizer, and N. Urbach. Don’t slip on the initial
coin oﬀering (ico): A taxonomy for a blockchain-enabled form of crowdfunding.
In 26th European Conference on Information Systems (ECIS) , 2018.
[20] A. Gervais, G. O. Karame, V. Capkun, and S. Capkun. Is Bitcoin a decen-
tralized currency? IEEE Security & Privacy , 12(3):54–60, May 2014. ISSN
1540-7993. doi: 10.1109/MSP.2014.49. URL https://ieeexplore.ieee.org/
document/6824541.
[21] C. Gini. Variabilit` a e mutabilit` a. 1912. URL https://ui.adsabs.harvard.
edu/abs/1912vamu.book.....G.
[22] S. P. Gochhayat, S. Shetty, R. Mukkamala, P. Foytik, G. A. Kamhoua, and
L. Njilla. Measuring Decentrality in Blockchain Based Systems. IEEE Access,
8:178372–178390, 2020. ISSN 2169-3536. doi: 10.1109/ACCESS.2020.3026577.
URL https://ieeexplore.ieee.org/document/9205256/.
[23] K. Haki, J. Beese, S. Aier, and R. Winter. The evolution of information systems
architecture: An agent-based simulation model. MIS Quarterly, 44(1), 2020.
[24] S. Hassan and P. De Filippi. Decentralized autonomous organization. Internet
Policy Review, 10(2):1–10, 2021.
[25] J. Kazil, D. Masad, and A. Crooks. Utilizing python for agent-based modeling:
The mesa framework. In R. Thomson, H. Bisgin, C. Dancy, A. Hyder, and
M. Hussain, editors, Social, Cultural, and Behavioral Modeling, pages 308–317,
Cham, 2020. Springer International Publishing. ISBN 978-3-030-61255-9.
[26] C. M. Macal. Everything you need to know about agent-based modelling and
simulation. Journal of Simulation , 10(2):144–156, 2016.
[27] H. Mendelson. Market behavior in a clearing house. Econometrica: Journal
of the Econometric Society , pages 1505–1524, 1982.
[28] L. J. Mester. Some thoughts on the evolution of the banking system and the
process of ﬁnancial intermediation. Economic Review-Federal Reserve Bank of
Atlanta, 92(1/2):67, 2007.
[29] J. S. Mill. Chapter V - Of The Connection Between Justice and Utility ,
page 62–96. Cambridge Library Collection - Philosophy. Cambridge University
Press, 1864. doi: 10.1017/CBO9781139923927.005.

---

## Page 21

AGENT-BASED MODEL OF INITIAL TOKEN ALLOCATIONS 21
[30] J. S. Mill. On Liberty and other Essays . Oxford University Press, USA, 1998.
[31] S. Nakamoto. Bitcoin: A Peer-to-Peer Electronic Cash System. -, 2008.
[32] L. Oliveira, L. Zavolokina, I. Bauer, and G. Schwabe. To token or not to token:
Tools for understanding blockchain tokens. In 39th International Conference
of Information Systems , 2018.
[33] V. Pareto. Cours d’´ economie politique, volume 1. Librairie Droz, 1964.
[34] J. Parkin. The senatorial governance of Bitcoin: making (de)centralized money.
Economy and Society , 48(4):463–487, Oct. 2019. ISSN 0308-5147, 1469-5766.
doi: 10.1080/03085147.2019.1678262. URL https://www.tandfonline.com/
doi/full/10.1080/03085147.2019.1678262.
[35] H. Partz. First binance soulbound token bab targets kyc user
credentials, 2022. URL https://cointelegraph.com/news/
first-binance-soulbound-token-bab-targets-kyc-user-credentials .
[36] S. Penzo and N. Selvadurai. A hard fork in the road: developing an eﬀective
regulatory framework for public blockchains. Information & Communications
Technology Law, pages 1–27, 2021.
[37] T. Piketty. Capital in the Twenty-First Century . Belknap Press, 2014. ISBN
067443000X,9780674430006.
[38] J. Rawls. A Theory of Justice . Harvard University Press Boston, 1971.
[39] J. Rawls. Justice as fairness: Political not metaphysical. In Equality and
Liberty, pages 145–173. Springer, 1991.
[40] W. Reijers and M. Coeckelbergh. The Blockchain as a Narrative Technology:
Investigating the Social Ontology and Normative Conﬁgurations of Cryptocur-
rencies. Philosophy & Technology, 31(1):103–130, Mar. 2018. ISSN 2210-5433,
2210-5441. doi: 10.1007/s13347-016-0239-x. URL http://link.springer.
com/10.1007/s13347-016-0239-x .
[41] M. G. Richiardi, R. Leombruni, N. J. Saam, and M. Sonnessa. A common
protocol for agent-based social simulation. Journal of artiﬁcial societies and
social simulation, 9, 2006.
[42] I. Ro¸ su and F. Saleh. Evolution of shares in a proof-of-stake cryptocurrency.
Management Science, 67(2):661–672, 2021.
[43] F. Sch¨ ar. Decentralized ﬁnance: On blockchain-and smart contract-based ﬁ-
nancial markets. Federal Reserve Bank of St. Louis Review , 2021.
[44] N. Schneider. Decentralization: an incomplete ambition. Journal of Cultural
Economy, 12(4):265–285, July 2019. ISSN 1753-0350, 1753-0369. doi: 10.1080/
17530350.2019.1589553. URL https://www.tandfonline.com/doi/full/10.
1080/17530350.2019.1589553.
[45] C. E. Shannon. A mathematical theory of communication. Bell System Tech-
nical Journal , 27(3):379–423, July 1948. ISSN 00058580. doi: 10.1002/j.
1538-7305.1948.tb01338.x. URL https://ieeexplore.ieee.org/document/
6773024.
[46] L. Shin and A. Cronje. Andre cronje of yearn ﬁnance
on yﬁ and the fair launch: ‘i’m lazy’. Unchained Pod-
cast, July 2020. URL https://unchainedpodcast.com/
andre-cronje-of-yearn-finance-on-yfi-and-the-fair-launch-im-lazy/ .
[47] H. Subramanian. Decentralized blockchain-based electronic marketplaces.
Commun. ACM , 61(1):78–84, dec 2017. ISSN 0001-0782. doi: 10.1145/
3158333. URL https://doi.org/10.1145/3158333.

---

## Page 22

22 DELGADO, BARBEREAU, AND PAPAGEORGIOU
[48] A. Sunyaev, N. Kannengießer, R. Beck, H. Treiblmaier, M. Lacity, J. Kranz,
G. Fridgen, U. Spankowski, and A. Luckow. Token economy. Business &
Information Systems Engineering , pages 1–22, 2021.
[49] H. Treiblmaier, M. Swan, P. De Filippi, M. Lacity, T. Hardjono, and H. Kim.
What’s next in blockchain research? -an identiﬁcation of key topics using a
multidisciplinary perspective. ACM SIGMIS Database: the DATABASE for
Advances in Information Systems , 52(1):27–52, 2021.
[50] S. Underwood. Blockchain beyond bitcoin. Commun. ACM, 59(11):15–17, oct
2016. ISSN 0001-0782. doi: 10.1145/2994581. URL https://doi.org/10.
1145/2994581.
[51] A. Wagner. The role of randomness in darwinian evolution. Philosophy of
Science, 79(1):95–119, 2012.
[52] E. G. Weyl, P. Ohlhaver, and V. Buterin. Decentralized society: Finding
web3’s soul. Available at SSRN 4105763 , 2022.
[53] J. Wood. The crypto fear and greed index, explained,
July 2022. URL https://www.coindesk.com/learn/
the-crypto-fear-and-greed-index-explained/ .
[54] A. Wright and P. De Filippi. Decentralized Blockchain Technology and the
Rise of Lex Cryptographia. SSRN Electronic Journal, 2015. ISSN 1556-5068.
doi: 10.2139/ssrn.2580664. URL https://www.ssrn.com/abstract=2580664.
[55] D. A. Zetzsche, D. W. Arner, and R. P. Buckley. Decentralized Finance.
Journal of Financial Regulation , 6(2):172–203, Sept. 2020. ISSN 2053-4841.
doi: 10.1093/jfr/fjaa010. URL https://academic.oup.com/jfr/article/6/
2/172/5913239.
[56] M. Zhang and G. Gable. Rethinking the value of simulation methods in the
information systems research ﬁeld: A call for reconstructing contribution for a
broader audience. In 35th International Conference on Information Systems .
Association for Information Systems (AIS), 2014.
[57] R. Zhang, R. Xue, and L. Liu. Security and privacy on blockchain. ACM
Computing Surveys (CSUR) , 52(3):1–34, 2019.
[58] R. Ziolkowski, G. Miscione, and G. Schwabe. Decision problems in blockchain
governance: Old wine in new bottles or walking in someone else’s shoes? Jour-
nal of Management Information Systems , 37(2):316–348, 2020.
SnT - Interdisciplinary Centre for Security, Reliability and Trust, University of
Luxembourg, 29 A v. John F. Kennedy, Luxembourg
Email address : joaquin.delgadofernandez@uni.lu
SnT - Interdisciplinary Centre for Security, Reliability and Trust, University of
Luxembourg, 29 A v. John F. Kennedy, Luxembourg
Email address : tom.barbereau@uni.lu
SnT - Interdisciplinary Centre for Security, Reliability and Trust, University of
Luxembourg, 29 A v. John F. Kennedy, Luxembourg
Email address : orestis.papageorgiou@uni.lu

---
