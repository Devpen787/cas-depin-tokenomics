# Elem_Talmon_2026_LegitimateOverridesInDecentralizedProtocols.pdf

## Page 1

Legitimate Overrides in Decentralized Protocols
Oghenekaro Elem1 and Nimrod Talmon2
1Parametrig, karo@parametrig.com
2BGU, IOG, talmonn@bgu.ac.il
Abstract
Decentralized protocols claim immutable, rule-based execution, yet
many embed emergency mechanisms such as chain-level freezes, proto-
col pauses, and account quarantines. These overrides are crucial for
responding to exploits and systemic failures, but they expose a core
tension: when does intervention preserve trust and when is it perceived
as illegitimate discretion? With approximately $10 billion in technical
exploit losses potentially addressable by onchain intervention (2016–
2026), the design of these mechanisms has high practical stakes, but
current approaches remain ad hoc and ideologically charged. We ad-
dress this gap by developing aScope×Authoritytaxonomy that maps
the design space of emergency architectures along two dimensions: the
precision of the intervention and the concentration of trigger authority.
We formalize the resulting tradeoffs of a standing centralization cost
versus containment speed and collateral disruption as a stochastic cost-
minimization problem; and derive three testable predictions. Assessing
these predictions against 705 documented exploit incidents, we find
that containment time varies systematically by authority type; that
losses follow a heavy-tailed distribution (α≈1.33) concentrating risk
in rare catastrophic events; and that community sentiment measurably
modulates the effective cost of maintaining intervention capability.
The analysis yields concrete design principles that move emergency
governance from ideological debate towards quantitative engineering.
1
arXiv:2602.12260v1  [cs.CR]  12 Feb 2026

---

## Page 2

1 Introduction
Hacks and exploits are a persistent feature of blockchains and DeFi protocols,
repeatedly producing losses that are large relative to protocol treasuries
and TVL. E.g., according to Charoenwong and Bernardi (2021; revised
2025) [12], cumulative losses from protocol failures, exploits, and market
manipulation approaches $88 billion. While much of this value derives from
systemic market failures (e.g., Terra/Luna), a significant persistent strata (≈
$10 billion) consists of technical exploits potentially addressable by onchain
emergency mechanisms.
A canonical early episode is the 2016DAOexploit [20], whose aftermath
culminated in a socially coordinated chain reconfiguration (the Ethereum
hard fork) [21], illustrating that “immutability” is ultimately mediated by
governance when stakes are high. In response, many systems embedemer-
gency mechanismsintended to limit damage under time pressure: protocol-
or module-level pauses and shutdown procedures, issuer- or contract-level
blacklisting/freeze controls, and (in some networks) chain-level transaction
restrictions. Such mechanisms can be effective in containment, but they
introduce a legitimacy and centralization tension: intervention power creates
an additional attack/abuse surface and changes the system’s trust model;
moreover, even when never exercised, the mereexistenceof privileged override
capability may reduce perceived trustlessness and thus depress utility or
valuation.
Remark 1.Consistent with this, a recent large-scale scan of 166 blockchain
networks reports that 16 chains contain active fund-freezing functions and
another 19 could introduce similar capabilities with relatively minor changes
(35/166≈21%) [11]; the same report highlights prominent deployments
of these capabilities in practice, including the use ofhardcodedblacklists
(addresses embedded directly in the chain’s configuration, as used during
the $570M BNB Chain bridge exploit [10]) andconfig-basedmechanisms
(runtime-configurable lists, as deployed in the $162M freeze of stolen assets
on Sui after the Cetus hack [48]).
Immutability–intervention paradox.Emergency mechanisms are intro-
duced to prevent catastrophic safety failures, yet they also create a second-
order governance risk: they alter the trust model by introducing privileged
discretion (or privilegedoptionality) over state transitions. This yields an
2

---

## Page 3

immutability–intervention paradox: in crises, communities oftendemandinter-
vention to protect users and integrated systems, but outside crises, the same
intervention capability can be viewed as a standing centralization backdoor
whose very existence reduces credibility.
Safety–liveness tradeoff (SLT).We use the standard distributed-systems
distinction:safetyprohibits “bad” state transitions (e.g., theft or invalid
state), whereaslivenessguarantees that “good” progress eventually happens
(e.g., transactions continue to be processed). Emergency overrides typically
improve safety by restricting transitions, but thereby reduce liveness (and
often censorship resistance). Here, we are mainly interested in quantifying
this tradeoff towards optimizing emergency mechanisms for different settings.
Contributions.These are our main contributions:
• Design-space taxonomy.We propose a compactScope×Authority
taxonomy that organizes emergency governance architectures into a
single design space.
• Incident mapping.We document prominent override episodes (in-
cluding chain-level responses and governance-led reconfigurations) and
use them to “fill” the taxonomy, highlighting legitimacy tensions that
recur across ecosystems.
• Decision support framework.We formalize the trade-offs between
standing centralization and blast radius into a quantitative cost model
and provide an open-sourceIntervention Mechanism Calculator. This
tool enables protocol designers to calibrate mechanism selection based
on community sentiment and estimated threat probabilities.1
Roadmap.Section 2 positions our work within relevant literatures. Sec-
tion 3 draws on constitutional democratic theory for conceptual foundations.
Section 4 presents our Scope×Authority taxonomy. Section 5 formalizes the
decision problem as a stochastic optimization. Section 6 assesses the model
with comprehensive empirical analysis. Section 7 extracts design principles
for practitioners.
1The tool is available here.
3

---

## Page 4

2 Related Work
Our work intersects four bodies of literature.
Blockchain security and incident response.The security community
has documented exploit patterns and proposed defensive mechanisms [12]. Re-
cent comprehensive reviews by Dwivedi et al. [17] and Siam et al. [42] system-
atically categorize vulnerabilities across blockchain layers – from network-level
attacks to smart contract exploits – yet most work focuses on documentation
andex-postanalyses rather than prevention, preemption, or post-incident
governance. Notable exceptions include analyses of the DAO fork [9] and
studies of bug bounty programs as coordinated disclosure mechanisms [5]. Im-
portantly,legitimate overridesand the broader design of formal intervention
mechanisms remain significantly under-studied in both academic and practi-
tioner literature; our work aims to fill this gap by providing a quantitative
framework.
Pre-execution prevention primitives.An emergent class of mechanisms
operatesbeforetransaction execution, shifting the intervention point from
reactive pauses to deterministic pre-execution enforcement. The Phylax
Credible Layer [37] exemplifies this paradigm: protocols define “assertions”
– Solidity-written invariants that specify states which should never occur
(e.g., “a healthy account cannot become liquidatable in a single transaction”).
The network’s sequencer then simulates every transaction against registered
assertions and drops violations before execution. This architecture inherits
the chain’s trust assumptions (no external oracle or monitoring service)
and provides zero false positives by construction. Early adopters include
Euler Finance (“Holy Grail” invariant for account liquidity) [23], Malda
Protocol, Turtle/Lagoon, and Denaria, each deploying 1–6 assertions to
protect critical protocol invariants. Linea’s integration of the Credible Layer
into its sequencer (January 2026) [37] demonstrates institutional appetite for
infrastructure-level security guaranties. This primitive occupies a distinct
cell in our taxonomy: Network Scope (sequencer-level enforcement) with
Signer Set Authority (sequencer operator controls assertion enforcement),
offering a compelling alternative to reactive pauses in risk-averse environments.
Unlike reactive mechanisms that respond after exploit detection, pre-execution
prevention operates deterministically at the transaction level before execution,
4

---

## Page 5

representing a fundamentally different paradigm that extends beyond our core
5×3 framework of reactive interventions (which operate at network, asset,
protocol, module, or account scope).
DAO governance.Recent empirical work examines onchain governance
mechanisms, voting behavior, and the tension between efficiency and decentral-
ization [51, 34, 52]. Wang et al. [51] analyzed 581 DAOs and 16,246 proposals
to document governance dynamics, while Ma et al. [34] examined 3,348 DAOs
across 9 blockchains, revealing widespread governance vulnerabilities including
contract backdoors and malicious proposals. Qian [39] demonstrated how
flash loan attacks, offchain voting manipulation, and token-based coercion
led to over $300M in losses across major DAOs. Werbach et al. [52] surveyed
23 blockchain projects to compare onchain and offchain governance practices,
highlighting the gap between pristine abstractions and messy realities. Our
focus onemergencygovernance-decisions under time pressure complements
this literature.
Political science of emergency powers.The political science literature
on states of emergency, constitutional constraints, and executive overreach
provides conceptual tools for analyzing blockchain emergency mechanisms.
Scholars have long studied how democracies balance speed and accountability
during crises, a tension that maps directly to our Authority dimension [24, 27].
We bridge this connection to open a dialogue between blockchain governance
and formal constitutional theory of exception.
3 Relation to Constitutional Democracies
Emergency override capabilities in blockchains are often discussed as technical
“circuit breakers” or governance exceptions. A closely related debate exists
in constitutional democracies, where emergency powers are introduced to
address rare, high-stakes crises while preserving the legitimacy of the ordinary
constitutional order. The parallel is substantive: in both settings, emergencies
intensify the tradeoff betweenspeed and containmenton the one hand, and
constraint and legitimacyon the other. Our goal is not a full comparative
political-theory analysis, but rather to (i) acknowledge this established body
of work, and (ii) use it as conceptual inspiration for organizing and analyzing
blockchain emergency mechanisms.
5

---

## Page 6

A minimal taxonomy in constitutional democracies.A useful starting
point is a two-part taxonomy, common in the law-and-politics literature on
emergencies:
1. Emergency legislation (ad hoc statutes).The legislature enacts
special, typically time-limited rules aimed at a specific crisis (e.g.,
public-health emergencies such as COVID-19). This approach keeps
the ordinary constitutional structure formally “on,” while temporarily
expanding executive capabilities via statute.
2. Declared exceptional regime (state of emergency).A formally
declared exceptional state activates extraordinary powers that would be
unavailable under normal conditions. A canonical normative rationale
isconservative/commissarial: extraordinary powers are justified to
neutralize the threat and restore the ordinary order “as soon as possible,”
rather than to permanently reconstitute the regime [24] (the canonical
example would be Rome’s dictator).
A recurring conceptual issue isdeclaration authority: whether the exception
is treated as objectively detectable (threshold-triggered) or as requiring an
institution with epistemic authority to declare that an exceptional situation
exists [24].
Canonical risks and safeguards.Even when emergency powers are
formally enacted, the democratic literature emphasizes that emergency gover-
nance is not “lawless”; rather, it is designed (or at least justified) through
constraints and procedures. Two themes are particularly relevant for our
setting.
• Stickiness (ratchet risk).A central concern is that extraordinary
powers, once activated, may persist through repeated renewals or insti-
tutional drift. Comparative evidence illustrates how formally temporary
declarations can become routine; for example, Israel’s general state of
emergency has been repeatedly renewed since 1948, and the contin-
ued validity of various legal provisions may depend on the declaration,
creating structural incentives for renewal [27].
• Boundedness principles (legality, proportionality, purpose lim-
itation).Many constitutional systems articulate principles limiting
6

---

## Page 7

emergency action, including exceptionality/last-resort, legality (no im-
plied powers), proportionality, and purpose limitation (actions should
aim at combating the threat and restoring ordinary functioning). For
instance, a synopsis of the Polish framework lists these principles ex-
plicitly [27]. Similarly, Israel’s emergency regulations regime contains
explicit restrictions tied to proportionality/necessity (“only to the ex-
tent warranted by the state of emergency”) and protections for core
rights [27].
4 Taxonomy: Scope×Authority
Our central organizing device is a two-dimensional taxonomy of emergency
mechanisms along two orthogonal design dimensions: (i)Scope(the precision
/ blast radius of the intervention), and (ii)Authority(who can trigger it, and
how). The safety–liveness profile is treated as an induced property of these
design choices, rather than an axis in itself.
4.1 Dimension I: Scope (Hierarchy of Precision)
We model scope as a discrete hierarchy of precision levels. Moving downward
increases precision (reduces blast radius) and typically reduces collateral dis-
ruption, but may require stronger instrumentation and may increase response
complexity.
1. Network scope.Chain-wide restriction or reconfiguration affect-
ing all applications (e.g., halt/pause, chain-wide censorship rules, re-
org/rollback, global fork-based remediation).
2.Asset scope.Actions targeting a specific asset across holders/venues
(e.g., issuer blacklisting, asset-specific freezes/burns, bridge-wide caps
on a given token).
3. Protocol scope.Application-wide restriction within a specific protocol
(e.g., pausing all markets in a lending protocol; emergency shutdown of
a stablecoin system).
4. Module scope.Feature-specific restriction within a protocol (e.g.,
pausing liquidations while allowing deposits/repayments; pausing oracle
updates).
7

---

## Page 8

5. Account scope.Targeted restriction or remediation affecting spe-
cific addresses/accounts only (e.g., freezing or quarantining addresses
implicated by evidence).
4.2 Dimension II: Authority (Trigger Holder)
We distinguish three authority modes, ordered from concentrated to broadly
distributed:
1. Signer set (key-based).A fixed keyholder set (e.g., 1-of-n or m-of-n
multisig) can trigger the mechanism.
2. Delegated body.A designated council/committee (typically multi-
party) holds bounded emergency powers, often with mandates, reporting
duties, and ex post accountability.
3. Governance process.The intervention requires a formal vote or
a broadly coordinated social process (e.g., token-holder governance,
validator/community coordination for upgrades).
Remark 2(Political Analogy).This authority spectrum maps naturally to
classical political theory classifications:Signer Setcorresponds toOligarchy
(power vested in a small, self-selected or appointed group);Delegated Body
corresponds toRepresentative Democracy(power exercised by elected represen-
tatives within constitutional bounds); andGovernance Processcorresponds
toDirect Democracy(power exercised directly by the citizenry/token-holders).
We use the technical nomenclature throughout the main text for precision,
but the political analogy illuminates the legitimacy trade-offs inherent in each
mode.
4.3 Intuition for the Taxonomy
Two basic intuitions motivate the taxonomy. First,scopegoverns collateral
disruption: higher-precision interventions affect fewer uninvolved users and
contracts, but typically require stronger instrumentation and more careful
evidence. Second,authoritygoverns speed and contestability: concentrated
authority can respond quickly but increases perceived discretion; governance-
heavy authority can increase legitimacy and accountability but may be too
slow for rapidly unfolding incidents.
8

---

## Page 9

Scope\
Authority
Signer set Delegated body Governance process
NetworkKey-triggered chain-wide
restriction
(e.g., halt/pause; global
censorship toggle)
Examples:Harmony
Horizon (Jun 2022,
$100M) [30]; BNB Chain
halt (Oct 2022, $570M) [40];
Berachain halt (Nov
2025) [8]
Council-coordinated
network action
(e.g., bounded emergency
council mandate)
Examples:Poly Network
validator coordination (Aug
2021, $611M returned) [19]
Governance-led chain
reconfiguration
(e.g., coordinated
upgrade/fork-based
remediation)
Examples:Ethereum
DAO fork (Jun 2016) [20];
Gnosis Chain hard fork
(Dec 2025, $9.4M) [29]
Asset Issuer/admin asset controls
(e.g., blacklist/freeze/burn
hooks)
Examples:Tether USDT
freezes (PDVSA
$182M) [53]; Circle USDC
blocked addresses (Tornado
Cash $75K) [13]; WLFI
blacklist of Justin Sun
($107M) [14]
Delegated asset committee
(e.g., bridge/operator
council enforces
caps/blocks)
Examples:Gnosis Bridge
Board freeze (Nov
2025) [28]; Curve
Emergency DAO
(emissions/PSR only) [33]
Governance changes asset
rules
(e.g., parameter change,
migration, social recovery)
Examples:Yearn
governance-approved
pxETH burn [54]
ProtocolAdmin pause / shutdown
(e.g., protocol-wide circuit
breaker)
Examples:Balancer
CSPv6 auto-pause (Nov
2025) [7]; Liqwid Kill
Switch [32]; Beanstalk
shutdown (Apr 2022,
$182M); Superfluid
agreement halt (Feb 2022)
Security-council pause
(e.g., bounded emergency
mandate)
Examples:Aave Protocol
Guardians [2]; Balancer V3
Emergency subDAO [6];
Liqwid Pause Guardian
(4-of-X)
DAO-administered
emergency action
(e.g., vote to
pause/upgrade/settle)
Examples:MakerDAO
ESM (deprecated) [43];
Anchor Protocol
(defunct) [4]
ModuleAdmin disables a feature
(e.g., stop liquidations /
withdrawals)
Examples:Compound
price oracle pauses (2021);
FEI/Rari DAI borrow
pause (Apr 2022, $80M);
Elephant Money TRUNK
minting pause (Apr 2022)
Delegated feature-specific
pauses
(e.g., guardian pauses
liquidations)
Examples:Aave V3
reserve/pool pauses [3];
Liqwid market pause (Oct
2025); dYdX YFI circuit
breaker [18]
Governance toggles module
parameters
(e.g., vote to enable /
disable a feature
temporarily)
Examples:MakerDAO
(Sky) USDC-PSM pause
(Mar 2023) [45]; Aave asset
parameter updates [1];
Solend USDH LTV set to 0
(Nov 2022)
AccountKey-based targeted
restriction
(e.g., freeze/quarantine
addresses)
Examples:Tether/Circle
address blacklists; Sonic
freezeAccount (Nov
2025) [46]; Ronin attacker
freeze [44]
Delegated targeted
remediation
(e.g., council-authorized
quarantines)
Examples:StakeWise
multisig burn/mint
($20.7M) [47]; Flow Isolated
Recovery (Dec 2025, 1,060
addresses) [25]
Governance-authorized
targeted action
(e.g., vote-based
remediation against
identified addresses)
Examples:Sui/Cetus
90.9% stake vote (May
2025, $162M) [48]; VeChain
blocklist (Dec 2019) [50]
Table 1:Emergency mechanisms mapped to Scope (precision)×
Authority (trigger holder).The table defines the design space used
to structure the narrative evidence and, later, the formal analysis. Some
incidents span cells (e.g., Sui/Cetus: Delegated Body freeze→Governance
recovery vote).
9

---

## Page 10

Table 1 “fills” the design space with prominent episodes and isolates
recurring legitimacy tensions that appear across ecosystems and across cells of
the table. The empirical analysis in Section 6 examines these cases in detail.
4.3.1 Relation to Constitutional Democracies
We discuss a bit more our taxonomy and contribution with relation to consti-
tutional democracies.
Mapping to the blockchain setting.These democratic themes naturally
translate to decentralized protocols:
• Authority↔who may trigger the exception.Democratic debates
about the locus of emergency authority (executive discretion vs. legisla-
tive delegation and oversight) correspond to ourAuthoritydimension:
concentrated keyholder triggers, delegated emergency bodies, and full
governance processes.
• Scope↔proportionality and collateral impact.The constitu-
tional demand for proportionality/purpose limitation corresponds to
ourScopedimension: more precise mechanisms reduce blast radius and
collateral disruption, but may require stronger instrumentation and
evidence.
In this sense, our Scope×Authority taxonomy can be viewed as a protocol-
design analogue of core questions studied in constitutional emergency gover-
nance:who is empowered to act, andhow far the intervention may reach.
Positioning our contribution.In the blockchain space, emergency mech-
anisms are widespread but heterogeneous (pauses, freezes, emergency councils,
forks/rollbacks), and design choices are often justified ad hoc, incident by
incident. Here we impose structure by (i) organizing mechanisms into a
unified design space (Scope×Authority), and (ii) connecting design choices
to explicit tradeoffs.
10

---

## Page 11

5 A Stochastic Model of Emergency Gover-
nance
The Scope×Authority taxonomy (Section 4) suggests that emergency gover-
nance is, fundamentally, adesign problem under time pressure and uncertainty.
A protocol must choose ex ante which override capabilities to embed (if any),
how precise they can be, and who can trigger them; then, when an inci-
dent occurs, the chosen architecture constrains which responses are feasible
and how quickly they can be executed. The empirical cases in Section 6.9
demonstrate that similar threat events yield very different interventions, and
that perceived legitimacy depends not only on outcomes but also on scope,
authority, and procedural safeguards.
Design objective (informal).At a high level, an emergency mechanism
trades off three ingredients: (i)containmentof losses from an unfolding inci-
dent (which typically favors fast, powerful triggers), (ii)collateral disruption
to uninvolved users and applications (which typically favors higher precision),
(iii) thestanding centralization costof privileged override capability (which is
incurred even when no emergency occurs, since it changes the trust model
and increases perceived discretion).
5.1 A Minimal Stochastic Model
A protocol designer chooses an emergency governance architecturem∈M.
Future adverse events are modeled by a finite set of typesH and a distribution
Pr[·]over H (optionally including a “no-incident” type; think of it as a static
decision for the next timestep).
If an event of type h∈ Hoccurs and is not yet contained, it gen-
erates loss at rate DamageRate(h)≥0per unit time (the “no-incident”
type has DamageRate(h) = 0). Architecture m contains the event after
Time(m)≥0time units. Exercising m also induces a collateral disruption
cost BlastRate(m)≥0(capturing the fixed, one-time shock of its scope).
Finally,m imposes a standing centralization costCentralizationCost(m)≥0,
incurred regardless of whether an incident occurs (Chekhov’s gun).
Thus, given a distribution over bad-event typesh∈H– specified by
their probabilities Pr[h]and damage rates DamageRate(h)– and given an
emergency governance architecturem∈Mwith containment timeTime(m),
11

---

## Page 12

standing centralization cost CentralizationCost(m), and blast-radius cost
BlastRate(m), the designer’s task is to minimize the expected cost. We define
the expected cost of architecturemby
ExpectedCost(m) := CentralizationCost(m)
+
∑
h∈H
Pr[h]·
(
Time(m)·DamageRate(h) + BlastRate(m)
)
,
and study the design problem
min
m∈M
ExpectedCost(m).
Interpretation.The blast rate BlastRate(m)is aone-timecost because
the scope decision is about width, not duration: pausing a protocol or chain
freezes activity causing a one-time shock: indeed, extending a pause from, e.g.,
1 hour to 3 hours does not make the blast radius 3×larger. If we multiplied
Blast Rate by Time continuously, a Governance decision taking 3 days versus
a Signer Set decision in 30 minutes would translate mathematically as 144×
more destructive, even though the impact of intervention is effectively the
same as a one-time event.
5.2 Three Theoretical Predictions
Our model yields three testable predictions that we assess in Section 6:
1. Prediction 1 (Speed-Centralization Tradeoff):Faster architec-
tures (Signer Set) minimize exploit losses but impose higher standing
centralization costs than slower architectures (Governance).
2. Prediction 2 (Scope-Blast Relationship):Higher-precision inter-
ventions (Account, Module scope) achieve comparable containment
outcomes with substantially lower collateral disruption than broader
interventions (Protocol, Network scope).
3. Prediction 3 (Sentiment-Cost Modulation):Positive community
sentiment toward emergency mechanisms reduces their effective standing
centralization cost; negative sentiment increases it.
12

---

## Page 13

6 Empirical Analysis and Assessment
Building on the theoretical framework in Section 5, we now present compre-
hensive empirical evidence using data from 705 documented exploit incidents
(2016–2026). Motivated by Pearson’s Law that“that which is measured and
reported improves exponentially,”we develop measurement frameworks to
illuminate how legitimate emergency interventions can reduce protocol losses
and protect users.
Remark 3(Datasets).We draw on multiple complementary datasets. First,
we aggregate data on 705 documented exploit incidents from 2016–2026, record-
ing date, chain, loss magnitude, and attack vector for each event. From these
705 total cases, we identify 640 technical exploits. Of these technical cases,
601 represent our intervention-eligible universe – technical exploits where
emergency mechanisms could theoretically apply. The remaining 39 technical
cases lack viable intervention points and are excluded from effectiveness anal-
ysis. From these 601 intervention-eligible cases, 130 involve actual emergency
mechanism activations (reactive responses to exploits and proactive measures),
representing the complete universe of intervention responses in our dataset.
Second, we use a curatedIntervention Incidentssubset of 52 high-fidelity
cases with verified timing, authority type, scope, and outcome data. This
subset – which includes both reactive exploit responses and proactive interven-
tions – represents the highest-quality cases selected for detailed effectiveness
analysis. This subset was constructed through manual verification of incident
reports, cross-referencing with multiple security databases, and validation
of intervention details through official post-mortems and governance forum
discussions.
6.1 Dataset Overview and Stratification
A critical distinction in our analysis is the separation between “systemic
failures” and “intervention-eligible exploits.” We stratify the 705 documented
cases into four categories:
1. Systemic Failures(10 cases, $61.80B): Massive economic design col-
lapses (e.g., Terra/Luna, FTX) where no emergency pause mechanism
could prevent loss.
13

---

## Page 14

Figure 1:Stratification of Losses (2016-2026).We stratify losses into
four layers:Systemic Failures(dark grey, e.g., Terra),Other Non-
Addressable(light grey, e.g., rug pulls),Intervention-Eligible(blue),
andActually Intervened(green). This reveals that while systemic events
dominate 2022, addressable technical exploits represent a consistent baseline
of risk.
2. Other Non-Addressable(94 cases, $7.41B): Incidents like rug pulls,
phishing, orunpausablelogicbugswhereinterventionwasnottechnically
feasible.
3. Intervention-Eligible(601 cases, $9.60B): Technical exploits (reen-
trancy, logic bugs, etc.) where emergency mechanisms were applicable.
4. Actually Intervened(130 cases, $7.51B): Cases where emergency
mechanisms were actually activated.
Our effectiveness analysis focuses strictly on the601 intervention-
eligible cases. Including systemic failures (as done in raw aggregators)
would severely distort the analysis, as a $40B collapse like Terra is not
“addressable” by the emergency governance mechanisms we study.
6.2 Loss Distribution: Power Law Validation
The resulting distribution of losses (Figure 2) follows a power law (Kolmogorov-
Smirnov test statisticD = 0.150, p< 0.001, Power Law exponentα≈1.33),
14

---

## Page 15

Figure 2:Pareto Distribution of Intervention-Eligible Losses.Approxi-
mately 80% of cumulative losses in our addressable dataset are attributable to
fewer than 50 incidents. This extreme concentration implies that intervention
capability is most valuable against rare, catastrophic events (“super-hacks”).
Note that this chart excludes $70B+ in systemic economic failures (e.g.,
Terra, FTX) which are not addressable by emergency overrides. Power law
fit:α≈1.33, KS testD= 0.150,p<0.001.
confirming that risk is driven by fat-tail events. This Pareto-like pattern
(approximately 80% of cumulative losses from fewer than 50 incidents) implies
that the expected value of intervention capability is driven primarily by its
effectiveness against “super-hacks,” where rapid containment can prevent tens
or hundreds of millions in additional losses.
Figure 3 shows the breakdown of the largest technical exploits, revealing
that a handful of “super-hacks” drive the vast majority of preventable losses,
reinforcing the power law finding. Stacked bars show losses prevented (green)
versus lost (red).
6.3 Attack Vector Characterization
Figure 4 shows the distribution of attack vectors by frequency (left panel)
and total loss value (right panel). While Logic Errors and Access Control
issues are most frequent and cause significant damage, Oracle Manipulation
and Flash Loan attacks come next among the highest severity incidents.
This has direct implications for mechanism design: protocols vulnerable to
15

---

## Page 16

Figure 3:Top 10 Intervention-Eligible Exploits.The breakdown of the
largest technical exploits reveals that a handful of “super-hacks” drive the
vast majority of preventable losses, reinforcing the power law finding. Stacked
bars show losses prevented (green) versus lost (red).
flash loan attacks (which unfold in a single transaction block) require fastest-
response mechanisms (Signer Set or Delegated Body), while slower Governance
processes may suffice for vulnerability types with longer exploitation windows.
6.4 The Speed-Centralization Tradeoff
Our intervention incidents data (Figure 5, Figure 6) confirms the model’s
Prediction 1: containment timeTime(m)varies systematically by authority
type. For the 52 verified intervention incidents:
• Signer Setinterventions achieve median containment in approximately
30 minutes.
•Delegated Bodyinterventions require approximately 60–90 minutes.
• Governanceinterventions, when they occur, operate on timescales of
days to weeks (e.g., the Gnosis hard fork required≈30 days).
16

---

## Page 17

Figure 4:Attack Vector Distribution.We observe that while ‘Logic
Errors’ and ‘Access Control’ issues are frequent and account for significant
losses; complex ‘Oracle Manipulation’ and ‘Flash Loan’ attacks often result
in the highest severity incidents, necessitating rapid intervention capabilities.
This ordering aligns with intuition: concentrated authority enables faster
response, while distributed authority introduces coordination latency.
6.5 Scope–Authority Matrix: Design Space Population
Figure 7 visualizes how real-world interventions populate the Scope×Au-
thority design space. The data shows that interventions are most frequent at
theProtocolscope. Notably, theProtocol/Governancecell (e.g., MakerDAO
Emergency Shutdown) remains largely theoretical or populated by deprecated
mechanisms; no major protocol has executed a full governance-triggered
shutdown under crisis conditions. While theGovernancecolumn contains
fewer active triggers, it includes high-recovery cases like the Gnosis hard
fork and the Ethereum DAO fork. Conversely, theProtocol/Delegated Body
cell is increasingly populated (e.g., Curve Emergency DAO), reflecting the
industry’s convergence on delegated safety councils.
6.6 Speed–Effectiveness Tradeoff
Figure 8 visualizes the relationship between reaction speed (Time(m)) and
containment success for 52 high-fidelity case studies. We defineTime(m)
using two observable timestamps: (i)time-to-detect= minutes between the
first credible alert and the first containment trigger, and (ii)time-to-contain=
17

---

## Page 18

Figure 5:Authority Distribution.Signer Set dominates incident count
(executing frequent, smaller interventions), while Governance interventions
achieve significant loss prevention through negotiation and recovery of high-
value assets. Left: interventions by count. Right: value protected by authority
type.
minutes between detection and mechanism execution (pause/freeze/halt). The
data supports Prediction 1: faster architectures (likeSigner Set) significantly
minimize loss, though they carry higher centralization costs.
6.7 Community Sentiment: Calibrating Centralization
Cost
We collected governance forum discussions (Discourse, Twitter) around in-
tervention incidents and applied an automated sentiment analysis pipeline.
For each incident, we extractedk = 20representative posts (where available)
and processed them using VADER (Valence Aware Dictionary and sEntiment
Reasoner) lexicon-based analyzer [31]. VADER is optimized for social media
and forum text as it accounts for both lexical features and structural signals
such as punctuation and intensifiers. The analyzer returns a normalizedcom-
poundscore s∈[−1, 1], where+1is maximally positive and−1is maximally
negative.
The aggregate average sentiment across 271 posts was+0.028, suggesting
that in practice, communities tend to accept emergency interventions, though
with significant variance. We benchmarked seven historical intervention cases
plus three general Twitter discussions:
18

---

## Page 19

Figure 6:Intervention Success Rates.Comparison of containment success
across authority types. Signer Set interventions (left) show higher reliability
in halting exploits compared to Delegated Bodies, likely due to reduced
coordination latency. Right panel shows total losses prevented by authority
type.
• Flow (Dec 2025):20 posts, avg sentiment +0.167 (supportive –
community acknowledged necessity of intervention)
• Liqwid (Oct 2025):20 posts, avg sentiment +0.204 (supportive –
flash crash response was seen as protective)
• StakeWise (Nov 2025):20 posts, avg sentiment +0.210 (supportive
– multisig recovery welcomed)
• Anchor (May 2022):20 posts, avg sentiment -0.004 (neutral – mixed
reactions to UST crisis response)
• Gnosis/Balancer (Nov 2025):3 posts, avg sentiment -0.034 (neutral
– complex reaction to fork proposal)
• AAVE (May 2025):20 posts, avg sentiment -0.201 (skeptical – com-
munity concerns about intervention scope)
• BNB (May 2025):20 posts, avg sentiment +0.095 (neutral – mixed
community response)
• DeFi-Hacks-General (Twitter):48 posts, avg sentiment -0.267
(skeptical – general community concerns)
19

---

## Page 20

Figure 7:Scope ×Authority Heatmap.Intervention effectiveness (con-
tainment success %) across the taxonomy. Protocol-scope interventions are
most frequent, while account-scope actions show high precision.
• Emergency-Pause (Twitter):50 posts, avg sentiment -0.128 (skepti-
cal – concerns about pause mechanisms)
• Recovery-Actions (Twitter):50 posts, avg sentiment +0.236 (sup-
portive – community favors recovery efforts)
This validates Prediction 3 and our standing centralization cost formula-
tion:
CentralizationCost(m) =MarketCap×DiscountRate(m)×(1−¯s)
where ¯s∈[−1, 1]is the average sentiment score. Positive sentiment reduces
the effective discount rate (community accepts the mechanism), while negative
sentiment increases it (community views mechanism as overreach).
20

---

## Page 21

Figure 8:Speed-Effectiveness Trade-off.Relationship between time-to-
containment (log scale, hours) and loss prevented. Faster interventions (left
side) consistently preserve more value, empirically validating the model’s
containment term. Bubble size represents loss prevented.
6.8 Empirical Support for the Political Analogy: The
Speed-Scope-Success Paradox
The empirical performance data strongly supports the political theory analo-
gies proposed in Section 4.2. Our 52 verified intervention cases reveal distinct
performance patterns across the authority spectrum:
• Signer Set (Oligarchy):Dominates incident volume (37 cases, 71.2%)
and value protected ($0.55B, 32% of total), with 39.1% containment
success. This reflects its role as the “first responder” for routine protocol,
asset, and account-scope interventions where speed trumps deliberation.
• Delegated Body (Representative Democracy):Handles mid-
complexity cases (8 cases, 15.4%, $0.88B protected) with 48.6% success.
This intermediate performance reflects the coordination burden of repre-
sentative structures without the procedural legitimacy of full governance
or the operational agility of signer sets.
21

---

## Page 22

• Governance (Direct Democracy):Achieves highest success rate
(73.2%) but on the smallest subset (6 cases, 11.5%, $0.17B protected).
Critically, these are predominantlyNetwork-scopeinterventions (e.g.,
Gnosis Hard Fork, Sui Recovery) where deliberative processes enable
fundamental protocol state changes (forks, asset recovery) that signer
sets cannot execute. The “success” here is measured in constitutional
legitimacy and comprehensive recovery, not containment speed.
This data reframes the “Immutability Paradox” as aScope-Authority
Matchingproblem: protocols fail not because governance is “slow,” but
because they deployDirect Democraticmechanisms forOligarchictasks (fast
containment) while underutilizing them forConstitutionaltasks (network
recovery, history revision) where their deliberative strengths achieve 73.2%
success rates.
6.9 Detailed Incident Analysis
For completeness, we provide expanded narratives for representative interven-
tion cases:
6.9.1 Network-scope interventions
Signer Set: BNB Chain and Harmony.During the October 2022 BNB
Chain bridge exploit (“BSC Token Hub”) [10, 35], validators coordinated to
halt block production as an emergency containment measure. This interven-
tion reduced further drainage but temporarily suspended unrelated activity
on the network, making the collateral liveness cost immediately salient. Simi-
lar dynamics appeared in Harmony’s Horizon Bridge exploit [30] and later
Berachain’s validator-coordinated halt [8]. The episode illustrates a recurrent
legitimacy tension for network-scope actions under concentrated authority:
speed and containment are gained at the price of broad disruption and a
perception of discretionary control.
Governance: The DAO and Gnosis Forks.Following the November
2025 Balancer exploit and subsequent fund freezes, Gnosis Chain executed a
governance-approved hard fork (December 2025) to recover a reported $9.4M
in assets that remained frozen onchain [29, 28]. The episode highlights a
characteristic network-scope governance tension: a deliberate, procedurally
22

---

## Page 23

justified intervention can be perceived as protective, yet it reopens concerns
about history revision and precedent.
6.9.2 Asset-scope interventions
Signer Set: Tether and Circle.Asset issuers frequently retain contract-
level controls enabling address blocking or freezing. Circle’s USDC terms
explicitly describe “Blocked Addresses” and reserve the ability to freeze
USDC associated with such addresses [13]. This authority mode yields
high operational responsiveness but embeds discretion at the asset layer,
raising legitimacy questions for users who treat stablecoins as credibly neutral
settlement assets. In January 2026, Tether executed its largest-ever freeze,
blocking $182M in USDT wallets linked to Venezuelan state oil company
PDVSA [53].
Delegated Body: Bridge Governance.During the November 2025
Balancer exploit, the Gnosis Bridge Governance Board temporarily halted
outflows of major tokens (GNO, wstETH, USDC, WETH, and others) to
prevent asset drainage [28]. The Curve Emergency DAO provides another
example: while its actions are limited to the protocol-level, its powers are
deliberately constrained to asset-specific actions such as stopping CRV emis-
sions on gauges or pausing the Peg Stabilization Reserve while explicitly
notenabling deposit/withdrawal freezes [33]. This precision reflects a design
choice to limit blast radius: the subDAO can address inflation bugs or peg
failures without disrupting the core DEX functionality.
6.9.3 Protocol-scope interventions
Signer Set: Admin Controls and Kill Switches.The fastest protocol-
scope responses rely on concentrated key authority. Liqwid’s Proposal 44
(March 2024) explicitly granted the Core Team a single-signature “kill switch”
to halt market batching within 5–15 minutes for oracle failure scenarios [32].
The proposal notes that this power coexists with a 4-of-X Pause Guardian
multisig (Delegated Body), illustrating defense-in-depth: the kill switch
maximizes speed but concentrates trust, while the Guardian adds oversight
at the cost of coordination latency.
23

---

## Page 24

Delegated Body: Emergency subDAOs.Protocols are increasingly
converging on bounded delegation as a “sweet spot.” Aave distinguishes gov-
ernance from protocol guardians, who hold time-bounded multisig authority
to pause specific markets or the entire protocol [2, 3]. Similarly, Radiant
Capital’s response to a compromised developer wallet (October 2024) relied
on its DAO Council to execute a cross-chain pause on Arbitrum, BSC, and
Base. The $50M exploit via compromised hardware wallets began at 15:46
UTC and was contained by 17:40 UTC across all chains, with compromised
signers removed from multisig by 22:10 UTC. While the initial compromise
was severe, the Delegated Body structure allowed for a coordinated, legally
recognized response that a pure Signer Set might have disorganized and a
pure Governance vote would have delayed.
Additionally, Curve Finance’s July 2023 $62M exploit response was man-
aged via itsEmergency DAO, demonstrating that a delegated committee can
act with the speed of a signer set but with greater transparency and role
separation [33]. Latest designs, such as Balancer V3, formalize this further
with explicit mandate limits for these delegated bodies [6].
Governance Process: ESM and Shutdown.MakerDAO (now Sky)
famously specified an Emergency Shutdown Module (ESM) intended as a
last-resort protection mechanism. Shutdown was governed by protocol-defined
triggers (via the ESM) and aimed to unwind positions and return collateral
to users. However, Sky has since deprecated the ESM mechanism [43],
illustrating that such “nuclear options”, while theoretically robust, are difficult
to maintain due to the game-theoretic risks of malicious triggering and the
immense coordination cost of unwinding state.
Similarly, EulerFinance(March2023)exemplifiedthe“Protocol/Governance”
tension: lacking an immediate admin override, the protocol was drained of
$197M. Recovery required a high-pressure offchain negotiation (“social layer
intervention”) to compel the return of funds [22], highlighting that pure
governance architectures often rely on legal/social backstops when onchain
speed is insufficient.
The Balancer Case and Window Expiry.The November 2025 Bal-
ancer V2 exploit provides a nuanced illustration of protocol-scope safety.
Composable Stable Pools (CSP) in V2 were designed with fixed pause win-
dows to ensure eventual immutability. In pools where these windows had
24

---

## Page 25

expired (CSPv5), the exploit succeeded because emergency pausing was no
longer technically possible. Conversely, in CSPv6 pools where pause windows
remained active, followingHypernativedetection of the attack, the team
successfully triggered a pause, containing the loss. This contrast highlights
a core design trade-off: fixed-length pause windows improve “liveness” and
perceived immutability but reduce the ability to intervene against vulner-
abilities discovered after deployment. Later iterations, such as Balancer’s
V3 newer architecture, introduced a dedicated emergency governance layer,
Emergency subDAO, to manage these powers with clearer delegation and
mandate limits [7, 6]. The Cork Protocol incident in May 2025, triggered by a
Uniswap v4 hook exploit, illustrates how a “Protocol×Signer Set” emergency
mode can still mitigate novel threats: after an alert, the team convened an
emergency war room with external security partners, SEAL911, and paused
remaining markets within roughly an hour, limiting further losses even though
the initial exploit had already drained funds from the targeted market [15].2
6.9.4 Module-scope interventions
Delegated Body: Feature-Specific Pauses.Module-scope interventions
restrict a specific function (e.g., liquidations) while allowing other protocol
activity to continue. Aave’s role-based control system explicitly supports
pausing at the pool or reserve level by emergency administrators, illustrating
the general pattern of narrowing blast radius via feature-specific switches [3, 1].
Governance Process: Function Toggles.Some protocols route feature
disabling or emergency patches through governance, trading response time for
broader legitimacy. In our framework, these episodes populate the module-
scope / governance cell when the intervention is limited to a component
but procedurally collective. MakerDAO’s emergency governance proposal to
adjust risk and governance parameters for USDC-PSM during the March 2023
USDC depeg exemplifies this pattern [45], as does dYdX’s use of margin and
2SEAL911 is a security “hotline” and rapid-response coordination channel run by
members of the Security Alliance (SEAL), where protocols, users, and auditors can raise
active or imminent incidents so that experienced responders can help triage, coordinate a
war room, and mitigate attacks as they unfold. It operates under the Whitehat Safe Harbor
Agreement (SHA), which provides legal protections for good-faith responders assisting in
incident mitigation and fund recovery [41, 16, 38].
25

---

## Page 26

position-size adjustments in the YFI-USD market as a de-facto circuit-breaker
during the November 2023 liquidation-stress incident [18].
6.9.5 Account-scope interventions
Account-scope interventions represent the highest precision in our taxonomy:
they target specific addresses or balances without disrupting the broader
system. This surgical approach minimizes collateral disruption but requires
robust evidence and instrumentation.
Signer Set: Key-Based Targeted Restrictions.Asset issuers and
protocol administrators frequently retain the ability to freeze or quarantine
specific addresses. Tether and Circle maintain address blacklists that can
be updated unilaterally by the issuer, enabling rapid response to sanctions
compliance or exploit containment. During the November 2025 Balancer
exploit, Sonic Labs deployed itsfreezeAccount mechanism within two hours
to freeze suspected attacker addresses [46]. However, the Sonic/Beets incident
uncovered a critical limitation: while the freeze blocked direct transfers,
78.5% of the funds were lost because the attacker usedpermit()signatures
to approve transfers from a different, unfrozen address. This signature-
based bypass illustrates that Account-scope interventions must block not only
transactions but also state-changing signatures to be fully effective. Similarly,
after the March 2022 Ronin Bridge exploit ($625M), attacker addresses
were identified and partially frozen, though the delayed detection (6 days)
limited recovery [44]. These cases illustrate the speed advantage of Signer Set
authority at the Account scope, though they embed significant discretionary
power.
Delegated Body: Council-Authorized Remediation.In the December
2025 Flow incident, validators halted the network after counterfeit tokens
were created and approximately $3.9M was extracted. Flow’s post-mortem
emphasizes containment without rollback, describing an “Isolated Recovery”
approach that preserved legitimate user activity while restricting only 1,060
addresses (under 0.01% of total accounts) implicated in the exploit. The
Community Governance Council (CGC), operating under validator-authorized
boundaries, executed token burns to neutralize counterfeit assets [26, 25].
This episode demonstrates that network-layer exploits can be remediated at
the account level when proper instrumentation exists.
26

---

## Page 27

The November 2025 StakeWise recovery provides a similar case at the
application layer. Following the Balancer V2 exploit, the StakeWise emergency
multisig (a 7-stakeholder body with the core team as only one signer) used
the protocol’s “controller” role to burn osETH and osGNO tokens in the
exploiter’s wallet and re-mint them to a DAO-controlled address [47]. By
manipulating state at the account level, the multisig recovered $20.7M without
disrupting stable users. The episode also illustrates the lifecycle of emergency
powers: after successful intervention, the team initiated a governance vote
to renounce these capabilities, trading future response capability for reduced
standing centralization cost.
Similar coordination occurred in the November 30, 2025 Yearn yETH
exploit. To recover assets, Yearn worked with the pxETH issuer (Redacted
Cartel) to burn 857.49 pxETH (≈$2.4M) from the attacker’s wallet and
re-mint them to protocol control [54]. This incident demonstrates how asset-
issuer authority can serve as a surgical remediation layer when protocol-level
pauses are absent or insufficient.
Governance Process: Stake-Weighted Vote.The May 2025 Cetus ex-
ploit on Sui ($220M stolen) produced the most rigorous governance-authorized
account intervention to date. After validators initially froze $162M by refusing
to process transactions from two attacker addresses (a Delegated Body ac-
tion), Cetus called for a community vote to authorize a protocol upgrade that
would recover the frozen funds. The Sui Foundation abstained to maintain
neutrality, and the vote concluded with90.9% of stakevoting “Yes” [48, 49].
The recovered funds were transferred to a 4-of-6 multisig (Cetus, Sui Founda-
tion, OtterSec) for distribution. This two-phase response – Delegated Body
freeze followed by Governance recovery – demonstrates that account-scope
remediation can achieve high legitimacy through explicit community mandate.
The VeChain Classification Dispute.The distinction between “admin
freeze” and “governance-led blocklist” is not merely semantic but central to
legitimacy. Following Bybit’s categorization of VeChain as having “hidden
freezing capabilities” [11], VeChain publicly refuted this, clarifying that
their mechanism is a validator-enforced blocklist authorized by community
governance (originally voted in December 2019 following a theft), rather
than a unilateral admin key [50]. This dispute highlights theAuthorityaxis
of our taxonomy: two mechanisms may achieve the sameScope(account
27

---

## Page 28

freezing) but differ fundamentally in theirAuthoritysource (Signer Set vs.
Governance), drastically altering their perceived centralization cost.
6.10 Summary: Theory-Empirics Alignment
Our empirical analysis supports all three core predictions of the expected cost
model:
1. Containment time varies by authority:Signer Set (30 min)<
Delegated Body (60–90 min)< Governance (days), validatingTime(m).
2. Losses follow power law:80/20 concentration validates focusing
intervention capability on rare, catastrophic events.
3. Sentiment modulates centralization cost:Positive community
acceptance reduces effective standing costs, validating the culture mul-
tiplier.
7 Design Implications
Our theoretical model (Section 5) and empirical findings (Section 6) jointly
suggest several design principles for emergency governance in decentralized
protocols.
7.1 The Delegation Sweet Spot
The expected cost functionExpectedCost(m)reveals a non-monotonic rela-
tionship between authority concentration and total social cost. Our empirical
Speed-Scope-Success Paradox data validates this theoretical prediction:
• Pure governance(mgov) minimizes standing centralization cost but
maximizes containment time, making it unsuitable for fast-moving
exploits. Empirically, this achieves 73.2% success but only on 11.5% of
cases (Network-scope interventions).
• Signer set(mkey) minimizes containment time but imposes a large
standing trust tax, reducing protocol valuation even absent any incident.
Empirically, this dominates volume (71.2% of cases) but achieves only
39.1% containment success.
28

---

## Page 29

• Delegated body(mcouncil) occupies the empirical sweet spot: 48.6%
success rate on 15.4% of cases with $0.88B protected, reflecting bounded
authority with faster-than-governance response but without the Signer
Set’s trust tax.
The emergence ofEmergency subDAOs(pioneered by Curve, adopted by
Balancer V3, and variants like Aave’s Protocol Guardians) reflects practitioner
convergence toward this sweet spot. These bodies operate under explicit
mandates, time-bounded powers, and reporting requirements, features that
reduceCentralizationCost(m)while preserving containment speed.
7.2 Scope Matters: Precision Reduces Blast Radius
Our taxonomy distinguishes five levels of scope, from network-wide halts to
account-level freezes.
The empirical data shows thathigher-precision interventions(Asset and
Account scope) achieve comparable containment outcomes with substantially
lower collateral disruption. For protocol designers, this implies:
• Invest ininstrumentationthat enables targeted response (e.g., per-
account freeze hooks, module-level circuit breakers).
• Avoid reliance on “nuclear options” (full chain halts) except as a last
resort.
• Design upgrade paths thatincreaseprecision over time as tooling
matures.
7.3 The Culture Multiplier
Blast radius cost is not uniform across ecosystems. Chains with strong “DeFi-
maxi” or permissionless cultures suffer disproportionate reputational damage
from interventions, even successful ones.
Conversely, chains targeting regulated use cases (RWA, payments, institu-
tional custody) may experience aregulatory premium: the presence of robust
override capability increases rather than decreases valuation.
Designers should calibrate their mechanism choice to community expecta-
tions.
29

---

## Page 30

A “culture multiplier”γcan be incorporated into the model:
BlastRate(m) =γ·Scope%·Daily Volume
1440
where γis high for permissionless chains and low for compliance-oriented
chains.
7.4 Sunset Clauses and Ossification
The Balancer CSPv5 case illustrates the risk ofpremature ossification: pause
windows that expire before all code paths are proven safe.
We recommend:
• Conditional sunsets: Pause capability should expire only after ex-
plicit security milestones (e.g., formal verification, extended bug-bounty
periods without critical findings).
• Renewable mandates: Delegated bodies should require periodic
re-authorization, preventing indefinite entrenchment.
7.5 A Decision Framework
To make the theoretical model actionable, we map observable protocol and
exploit parameters to the formal model variables in Table 2. This allows
designers to calibrate the calculator tool using evidence-based heuristics.
Remark 4(Practitioner Alignment).The parameters in Table 2 align closely
with factors independently identified by practitioners. For example, in the Gno-
sis Community AMA (January 7, 2026), Gnosis co-founder Friederike Ernst
outlined analogous decision criteria such exploit type, protocol type, exploit
novelty, security claims, audit status, and percentage of chain TVL affected,
as factors the core team may evaluate if considering potential intervention.
In a subsequent contribution to the GnosisDAO governance forum [36], we
formalized these considerations into a structured decision framework, rec-
ommending (i) pre-defined thresholds for each parameter documented in the
governance framework, (ii) weighted scoring to combine multiple factors into
a transparent decision matrix, and (iii) publication of these criteria before any
incident occurs, so that both the community and potential interveners share
a common reference point. This convergence between our theoretical model,
30

---

## Page 31

Table 2:Mapping Protocol Parameters to Model Variables.This
table standardizes the mapping between observable protocol and exploit
characteristics and formal variables in our expected cost model.
Parameter Relevance Model V ariable Short Explanation
Protocol
Type
Asset risk profile Pr[h],DamageRate(h) AMM vs Lending vs
Bridge risk profiles
Exploit Type Containment
urgency
DamageRate(h) Flash loan (fast)
vs Reentrancy
(medium)
Exploit
Novelty
Variant vs.
Zero-day
Pr[h],DamageRate(h) Zero-day = max dam-
age rate
Audit Status Preventive
security health
Pr[h] Multiple audits =
lower threat prob
Community
Sentiment
Political
legitimacy
CentralizationCost(m),
BlastRate(m)
Trust reduces politi-
cal cost
TVL Affected Economic scale
at risk
BlastRate(m) Higher TVL = larger
blast radius
Security
Claims
Breach
accountability
CentralizationCost(m) “Immutable” = high
trust tax
practitioner intuition, and the proposed governance framework supports the
actionability of the parameter space identified here.
We propose that protocol designers use our stochastic model as a decision
support tool:
1. Estimate threat parameters: Probability distribution Pr[h]and
damage ratesDamageRate(h)for plausible exploit scenarios.
2. Estimatemechanismcosts: Standingcentralizationcost CentralizationCost(m),
containment timeTime(m), and blast rateBlastRate(m)for candidate
architectures.
3. Minimize expected cost: Choose the architecturem∗that mini-
mizes ExpectedCost(m)given the protocol’s risk profile and community
culture.
This framework moves emergency governance from ideology (“decentral-
ization good, admin keys bad”) to quantitative cost-benefit analysis.
31

---

## Page 32

8 Conclusion
Emergency override mechanisms are a pervasive yet under-theorized feature
of decentralized protocols. This paper has offered three complementary
contributions toward filling that gap. First, we introduced a compactScope×
Authoritytaxonomy that organizes the heterogeneous landscape of emergency
mechanisms into a single, two-dimensional design space, and we populated it
with prominent real-world episodes spanning chain-level halts, asset freezes,
protocol pauses, module toggles, and account-level quarantines. Second, we
formalized the underlying design tradeoff as a stochastic cost-minimization
problem that balances standing centralization cost, containment speed, and
collateral disruption—and derived three testable predictions from the model.
Third, we assessed these predictions against 705 documented exploit incidents
(2016–2026), finding that containment time varies systematically by authority
type, that losses follow a power-law distribution concentrating risk in rare
“super-hacks,” and that community sentiment measurably modulates the
effective cost of intervention capability. Together, these results reframe
emergency governance as a quantitative engineering discipline rather than an
ideological binary, and provide actionable design principles, delegation sweet
spots, precision instrumentation, culture-aware calibration, and conditional
sunset clauses, for protocol designers navigating the immutability–intervention
paradox.
9 Future Directions
We outline directions for future research:
• Formalizing Heterogeneous Stakeholder Costs.Different stake-
holders (token holders, LPs, integrators, validators) bear asymmetric
costs from both exploits and interventions. Formalizing these heteroge-
neous preferences could yield more nuanced design recommendations.
•Decision Support Tooling.The expected cost framework naturally
suggests a “calculator” tool for protocol designers. Given estimates
of threat probabilities and mechanism costs, such a tool could rank
candidate architectures and perform sensitivity analysis. We have
implemented an open-source prototype of this calculator as part of this
32

---

## Page 33

research, allowing real-time calculation and sentiment-based calibration
of mechanisms.
• Extended Taxonomy Development.Our 5×3 framework captures
reactive interventions effectively, but Section 2 (e.g., Phylax Credible
Layer) suggest need for additional dimensions. Future work could
develop a comprehensive taxonomy that includes timing dimensions
(pre-execution vs. reactive) and enforcement mechanisms (assertion-
based vs. pause-based).
• Cross-Chain Coordination Protocols.As protocols operate across
multiple chains, emergency response mechanisms face new coordination
challenges. Research into standardized cross-chain emergency protocols
could enable synchronized responses while preserving chain sovereignty.
• Dynamic Mechanism Selection.The expected cost framework
assumes static mechanism selection, but real-world conditions may
require adaptive approaches. Investigating dynamic mechanism selection
based on real-time threat assessment could improve responsiveness.
References
[1] Aave Governance. Full deprecation of dpi across aave deployments, 2025.
[2] Aave Protocol. Aave protocol guardians, 2023.
[3] Aave Protocol. Aave v3 acl manager: Role-based access control, 2023.
[4] Anchor Protocol Community. Emergency Measures for Restoring Terra
Peg, May 2022. Emergency governance proposals during UST collapse.
[5] Lital Badash, Nachiket Tapas, Asaf Nadler, Francesco Longo, and Asaf
Shabtai. Blockchain-based Bug Bounty Framework. InProceedings of the
36th Annual ACM Symposium on Applied Computing (SAC ’21), pages
239–248, New York, NY, USA, 2021. ACM.
[6] Balancer Foundation. Balancer v3 governance: Emergency subdao, 2024.
[7] Balancer Foundation. Nov 3 exploit post-mortem, Nov 2025. Detailed
technical breakdown of CSP rounding bug,94.8Mtheft,45.7M recov-
ered/protected.
33

---

## Page 34

[8] Berachain Foundation. Berachain post-mortem: Validator halt and
recovery, Nov 2025.
[9] Bit Novosti. Ethereum classic: keep censorship-resistant ethereum going,
2016. Ethereum Classic announcement following the DAO fork.
[10] BNB Chain. Bnb chain: A decentralized response, Oct 2022.
[11] ByBit Research. Blockchain security report 2024: Asset freezing land-
scape, 2025. Analysis of chain-level freezing capabilities.
[12] Ben Charoenwong and Mario Bernardi. A decade of cryptocurrency
“hacks”: 2011–2021, 2021. SSRN working paper, revised 2025-11-02.
[13] Circle Internet Financial. Circle usdc terms of service: Blocked addresses,
2025.
[14] CoinDesk. World liberty financial blacklists justin sun’s address with
$107m wlfi, Sep 2025.
[15] Cork Protocol. Cork protocol post-mortem, May 2025.
[16] Dedaub. Seal 911: A few lessons from the frontlines, 2025. Accessed:
February 2026.
[17] Kaustubh Dwivedi, Ankit Agrawal, Ashutosh Bhatia, and Kamlesh
Tiwari. A Novel Classification of Attacks on Blockchain Layers: Vulner-
abilities, Attacks, Mitigations, and Research Directions, 2024.
[18] dYdX. dydx: Sushi/yfi market incident report, Nov 2023. YFI market
paused during large position liquidation. Module-level circuit breaker.
[19] Elliptic. The poly network hack: $600 million in crypto stolen and
returned in 24 hours, Aug 2021.
[20] Ethereum Foundation. Critical update re: Dao vulnerability, 2016. The
DAO was a smart contract on Ethereum that raised $150M and was
exploited in June 2016, leading to the Ethereum hard fork.
[21] Ethereum Foundation. The dao hard fork (2016): Ethereum foundation
blog, 2016.
34

---

## Page 35

[22] Euler Finance. War & Peace: Behind the Scenes of Euler’s $240M Exploit
Recovery, April 2023. No emergency pause; recovery via negotiation.
Attacker returned $143M after negotiation.
[23] Euler Finance and Phylax Systems. Euler finance "holy grail" assertion:
Account liquidity invariant, 2026. Euler deployed five assertions to
protect lending protocol; primary assertion prevents healthy accounts
from becoming liquidatable.
[24] John Ferejohn and Pasquale Pasquino. The law of the exception: A
typology of emergency powers.International Journal of Constitutional
Law, 2(2), 2004.
[25] Flow Foundation. Flow network recovery: Technical implementation
plan, Dec 2025. Technical details of the Isolated Recovery plan.
[26] Flow Foundation. Flow security incident 27th december: Technical
post-mortem, Jan 2026.
[27] Ilana Gimpelson, G Karavokkyris, I Lachman, G Lurie, M Pachol-
ska, T Shwartz, Y Orpeli, A Reichman, E Salzberger, G Barzi-
lai, et al. Law and emergencies: A comparative overview,
the minerva center for the rule of law under extreme con-
ditions.Available online also at: http://minervaextremelaw.
haifa. ac. il/images/Emergency_Laws_and_Regulations_-in_Japan-
_19-_Jan2016. pdf [accessed in Bandung, Indonesia: March 2, 2016],
2016.
[28] Gnosis Bridge Governance Board. Bridge board decision: Freeze outflow
of major tokens on canonical bridges, Nov 2025. Due to BalancerV2
exploit, halted outflow of major tokens on Omnibridge & xDAI bridge
as precautionary measure.
[29] GnosisDAO. Balancer hack hard fork proposal, Dec 2025.
[30] Halborn. Explained: The Harmony Horizon Bridge Hack (June 2022),
June 2022. Horizon bridge compromised via key theft. $100M loss.
[31] Clayton Hutto and Eric Gilbert. Vader: A parsimonious rule-based
model for sentiment analysis of social media text. InProceedings of the
35

---

## Page 36

International AAAI Conference on Web and Social Media, volume 8,
pages 216–225, 2014.
[32] Liqwid Finance Governance. Proposal 44: Grant core team power to
rapidly deal with emergencies, March 2024. Proposal 44, Executed March
14, 2024.
[33] LlamaRisk. Curve finance exploit analysis: Emergency subdao response,
Jul 2023. Emergency DAO freeze CRV gauge emissions to affected pools.
[34] Junjie Ma, Muhui Jiang, Jinan Jiang, Xiapu Luo, Yufeng Hu, and Yajin
Zhou. Understanding Security Issues in the DAO Governance Process.
IEEE Transactions on Software Engineering, 51(4):1188–1204, April
2025. Analysis of 3,348 DAOs across 9 blockchains revealing governance
contract backdoors and malicious proposals.
[35] Merkle Science. Hack track: Analysis of the bnb smart chain exploit,
Oct 2022.
[36] Elem Oghenekaro. A framework for the future: Structured intervention
criteria for gnosisdao, Jan 2026. Response to GnosisDAO consultation on
emergency intervention criteria, formalizing decision parameters into a
structured framework with pre-defined thresholds and weighted scoring.
[37] Phylax Systems. Phylax partners with linea: Bringing network-native
security to the home of eth capital, Jan 2026. Linea integrates Cred-
ible Layer for pre-execution exploit prevention via sequencer-enforced
assertions.
[38] Piper Alderman. Security alliance proposes whitehat safe harbor to
secure web3, 2025. Accessed: February 2026.
[39] Lori Qian. Strengthening DAO Governance: Vulnerabilities and Solutions.
The National High School Journal of Science, 2025. Case study analysis
of Uniswap, GnosisDAO, and ArbitrumDAO governance vulnerabilities
including flash loan exploitation and off-chain voting manipulation.
[40] Reuters. Binance-linked blockchain hit by $570 million crypto hack, Oct
2022.
36

---

## Page 37

[41] Security Alliance. Seal-911 github repository, 2024. Accessed: February
2026.
[42] Md Kamrul Siam, Bilash Saha, Md Mehedi Hasan, Md Jobair Hossain
Faruk, Nafisa Anjum, Sharaban Tahora, Aiasha Siddika, and Hossain
Shahriar. Securing Decentralized Ecosystems: A Comprehensive System-
atic Review of Blockchain Vulnerabilities, Attacks, and Countermeasures
and Mitigation Strategies.Future Internet, 17(4):183, 2025.
[43] Sky / MakerDAO. Emergency shutdown (deprecated): Sky protocol doc-
umentation, 2025. Official documentation for the deprecated Emergency
Shutdown Module (ESM).
[44] Sky Mavis. Back to Building: Ronin Security Breach Post-Mortem,
March 2022. $625M bridge exploit. $30M recovered via law enforcement.
[45] Sky Money Forum. Emergency proposal: Risk and governance parameter
changes (march 11, 2023), Mar 2023. Emergency governance vote to
pause PSM during USDC depeg.
[46] Sonic Labs. Sonic chain: Defensive measures and the freeze post-mortem,
Nov 2025.
[47] StakeWise DAO. Post-mortem: Stakewise dao recovery of $20.7m os-
tokens from balancer v2 exploiter, Nov 2025. Emergency multisig (7
members) used token controller roles to burn hijacked osETH/osGNO
and re-mint to DAO addresses.
[48] Sui Foundation. Response to the cetus incident - onchain community
vote, May 2025.
[49] Unchained Crypto. Cetus relaunches protocol after recovering $162m
from exploit, Jun 2025.
[50] VeChain Foundation. Vechain refutes bybit’s allegations: Clarifying
freezing vs blocking, 2025. Official clarification on freezing capabilities.
[51] Qin Wang, Guangsheng Yu, Yilin Sai, Caijun Sun, Lam Duc Nguyen,
and Shiping Chen. Understanding DAOs: An Empirical Study on
Governance Dynamics.IEEE Transactions on Computational Social
Systems, 12(5):2814–2832, October 2025. Empirical analysis of 581 DAO
projects and 16,246 proposals from Snapshot.
37

---

## Page 38

[52] Kevin Werbach, Primavera De Filippi, Joshua Tan, and Gina Pieters.
Blockchain Governance in the Wild.Cryptoeconomic Systems, April
2024. Comparative questionnaire study of governance practices at 23
blockchain projects examining on-chain and off-chain mechanisms.
[53] Yahoo Finance. Tether freezes $182m usdt in largest-ever freeze, Jan 2026.
Tether froze wallets linked to Venezuelan state oil company PDVSA.
[54] Yearn Finance Security Team. Yearn finance post-mortem: yeth exploit
and recovery, Nov 2025.
38

---
