# Cong_Rabetti_Wang_Yan_2025_CentralizedGovernanceInDecentralizedOrganizations.pdf

## Page 1

Centralized Governance in Decentralized Organizations*
Lin William Cong† Daniel Rabetti‡§ Charles C. Y. W ang¶ Yu Y an∥
This draft: August 2025
Abstract
W e systematically document governance centralization in decentralized autonomous organizations (DAOs)
and examine its drivers and economic implications. Using multiple data sources and granular on-chain trans-
action data, we find that DAOs—including most Decentralized Finance (DeFi) projects—exhibit low partic-
ipation rates and highly concentrated voting power, with the top decile of voters controlling 76.2% of total
votes. Analyzing pre-proposal trading, we observe significant abnormal trading activity: blockvoters accumu-
late tokens to influence outcomes, while proposal managers engage in insider trading, earning average market-
adjusted returns of 9.5%. These conflicts of interest can be value-destructive, particularly during crises when
effective governance is critical to organizational survival. Y et, recent innovations such as quadratic voting and
delegation mechanisms show promise in advancing the goals of decentralization by empowering minority token
holders and mitigating agency conflicts. Overall, our study highlights both the persistence of agency problems
in DAOs and the potential for well-designed governance mechanisms to improve outcomes in these emerging
digital organizations.
JEL classification: D47, D82, G12, G14, G34.
Keywords: DAOs, Blockchain, DeFi V entures, Governance, Insider T rading, Blockvoters.
* W e are especially grateful to Jillian Grennan, John Griffin, Angie Low, Roni Michaely, and Baolian W ang for many insightful discus-
sions and comments. W e also thank Soheil Ahmadi, Jan Bena (Discussant), Ben Charoenwong, Lauren Cohen, Chuck Fang, Vivian Fang
(Discussant), Dimas Fazio, Sean Foley, Cesare Fracassi (Discussant), Hanna Halaburda, Zhiguo He, Kensuke Ito, Engin Iyidogan, Poorya
Kabir, Jonathan Karpoff, Alan Kwan (Discussant), Heiko Leonhard, Yibin Liu, Roger Loh, Zhenghui Ni (Discussant), Julian Prat, Jay
Ritter, Rik Sen, T ao Shu, Michael Sockin, Johan Sulaeman, Y okio T oryama, Y ang Y ou, Jean Zeng, Yiyun Zheng, Alminas Zaldokas and
participants and discussants at the SAIF Finance Conference, 2025 Annual Conference of the Crypto and Blockchain Economics Re-
search (CBER) Forum, 18th International Behavioural Finance Conference, 4th Hong Kong Conference for Fintech, AI, and Big Data in
Business, 5th Machine Lawyering Conference, 2025 Dishui Lake International Conference in Finance, ABFER 12th Annual Conference,
2025 Conference on Financial Market Regulation at the Securities and Exchange Commission (SEC), 2025 Forensic Finance Conference
at the University of T exas at Austin, Digital Economy and Financial T echnology (DEFT) Lab meeting, ETHDenver Festival, Interna-
tional Monetary Fund (IMF), Harvard Business School seminar, 2024 T okenomics Conference, W aseda W orkshop in Decentralized
Finance, 2024 Singapore Scholars Symposium and National University of Singapore Accounting Brownbag. Rabetti thanks the Asian
Institute for Digital Finance (NUS), DEFT Labs (Cornell), and Research Center for Digital Financial Assets (T singhua) for invaluable
discussions. Y an thanks Johan Sulaeman and Stephen Dimmock, members of her dissertation committee, for their invaluable support.
Data and code will soon be available in our public repositories.
†Cornell University SC Johnson College of Business (Johnson), ABFER, and NBER, will.cong@cornell.edu.
‡Corresponding Author: National University of Singapore (NUS) Business School, 15 Kent Ridge Drive, Singapore, 119245.
§Harvard Business School (visiting), drabetti@hbs.edu.
¶Harvard Business School and European Corporate Governance Institute (ECGI), cwang@hbs.edu.
∥National University of Singapore (NUS) Business School, yu.yan@u.nus.edu.

---

## Page 2

1 Introduction
T raditional firms typically face inherent conflicts of interest, often framed as agency problems, be-
tween principals (e.g., shareholders) and agents (e.g., managers or insiders). The design of governance
systems—especially the degree of decentralization in decision-making—thus remains a central theme in
organizational economics (e.g., Jensen and Meckling, 1976, 1992). In theory, decentralized structures may
alleviate agency frictions but exacerbate collective action and information costs. Levit et al. (2024) ad-
vances this debate by formalizing the dual role of trading and voting in shaping shareholder welfare.1 One
critical implication is that decentralized voting rights—if poorly designed or insufficiently representative—
can fail to deliver efficient outcomes even in frictionless and transparent markets.
Our study extends the discussion by investigating governance in Decentralized Autonomous Orga-
nizations (DAOs), an emergent digital organizational form enabled by blockchain infrastructure. DAOs
are governed by programmable smart contracts, in which organizational rules are encoded into software
and automatically self-executed when pre-specified conditions (e.g., voting outcomes subject to quorum)
are met, and decentralized decision-making through their token holders (Cong and He, 2019; Harvey
and Rabetti, 2024). Governance token holders can directly participate in decision-making by creating
and voting on proposals, which include critical organizational choices from product design to treasury
disbursements and voting procedures. V oting outcomes are automatically enforced through smart con-
tracts on the blockchain. All decisions are recorded on the blockchain, enabling a high level of operational
transparency.
This digital organizational form appears to be gaining traction. As of early 2025, the number of active
DAOs has surpassed 10,000, with more than 3.3 million voters. From 2021 to 2025, the total value of assets
in DAO treasuries increased dramatically from $520.7 million to $22.5 billion, with substantial increases
occurring in 2023 (i.e., Figure 1).2
[Figure 1]
1Notably, the study shows that delegation to boards—a hallmark of traditional governance—can in some cases enhance
welfare by insulating decision-making from extreme shareholder preferences.
2Monthly total assets owned, based on statistics from DeepDAO, a tracking platform: https://deepdao.io/organizations.
A few DAOs were launched in 2017—2019, a period characterized by token offerings and frauds (e.g., Howell et al., 2020;
Lyandres et al., 2022; Davydiuk et al., 2023; Lyandres and Rabetti, 2024; Gefen et al., 2024; Cong et al., 2024).

---

## Page 3

If DAOs represent a truly novel organizational form to the extent that they simultaneously allow
for decentralization of decision-making at scale, it should, by design, also effectively suppress agency
costs. Such digital infrastructure could limit self-interested behavior through mechanisms of aligned
incentives, broad stakeholder involvement, and operational transparency (Davidson et al., 2016; Reijers
et al., 2016; De Filippi and Wright, 2018; Laturnus, 2023). Y et, some suggest that DAOs simply be “the
blockchain equivalent of a company” (e.g., Berg et al., 2019): instead of a revolutionary shift, they are
merely a technologically-enabled variation of traditional organizational and governance practices. This
raises a fundamental question: How novel are DAOs in practice? If DAOs are truly novel and capa-
ble of overcoming the traditional organizational trade-offs, they should empirically exhibit decentralized
decision-making at scale and demonstrate that their proposed mechanisms (smart contracts, token gover-
nance) effectively suppress agency costs, leading to minimal observable agency conflicts and more efficient
and governance outcomes.
Y et, mounting evidence suggests that conflicts of interest may be pervasive in DAOs. A notable il-
lustration occurred in the Uniswap DAO—a leading decentralized exchange—where a single delegate
wallet tied to a major venture capital firm effectively controlled the outcome of a proposal to activate the
protocol fee switch, raising industry-wide concerns about the integrity of decentralized governance.3 Mo-
tivated by such episodes, we begin our empirical analysis by assessing the actual degree of decentralization
in DAO governance. Using granular proposal and voting data from a widely used voting platform, we
find that overall participation rates in DAOs are low, averaging just 6.3%. This low turnout reflects the
combined effects of the free-rider problem—where individual token holders have little incentive to bear
the cost of voting since they can benefit from others’ efforts—and the absence of regulatory requirements
obligating token holders to vote. Further analysis reveals a striking concentration of voting power: the top
decile of voters controls 76.2% of the total realized voting power. Our initial findings support concerns
raised by practitioners and regulatory agencies.4
W e continue our analysis by mapping the main players in the DAO governance and fetching stylized
facts. Applying blockchain forensics with the Ethereum Name Service (ENS), we classify the top voters
into four primary categories: core team members, institutional investors, third-party service providers,
3See, e.g., “Uniswap DAO’s vote ignites decentralization debate,”The Deﬁant , October 2023: https://thedefiant.
io/uniswap-decentralization-a16z .
4In a recent roundtable in W ashington, D.C., organized by the Wharton Initiative on Financial Policy and Regulation,
the protection of stakeholders in decentralized ecosystems was a central topic of debate among both academics and regulators
(https://wifpr.wharton.upenn.edu/roundtables/).
2

---

## Page 4

and key opinion leaders—prominent figures, including active community members and industry ex-
perts.5 The average Gini coefficient and the share of voting power held by the top decile of voters start at
high levels— largely attributed to the token allocation schemes—and exhibit a clear upward trend over
time, indicating growing concentration of voting power as DAOs mature. At the cross-section of DAO
characteristics, we find that Yield and Lending protocols exhibit significantly lower participation rates
than other protocol types, and larger DAOs show reduced voter engagement overall. Finance-related
proposals attract higher participation, while the complexity and contentiousness of proposals do not
significantly affect turnout. Regarding voting power concentration, larger DAOs tend to be more cen-
tralized, with decentralized exchanges (DEXs) showing the highest concentration and Yield protocols
the lowest. Proposal characteristics also play a role in shaping voting concentration. Proposal complexity
is associated with greater concentration, whereas contentious proposals exhibit lower concentration of
voting power.6
Having established stylized facts shaping voting power concentration in DAOs, we move next to ana-
lyze governance token trading before proposal creation. Prior research suggests that shareholders acquire
voting rights ahead of key proposals to increase their influence, typically through direct spot market trad-
ing (Fos and Holderness, 2023; Bethel et al., 2009) or stock borrowing in the equity loan market (Christof-
fersen et al., 2007; Hu and Black, 2007; Aggarwal et al., 2015). Inspired by this literature, we examine the
pre-governance proposals’ token trading behavior of two groups of governance participants—proposal
managers and top decile voters—around proposal events on Snapshot, a widely used off-chain voting
platform. Leveraging on-chain transaction data from BigQuery, we find evidence of abnormal trading of
tokens during the month leading up to DAO proposal creation. Specifically, we observe that total trading
volume increases by 16.8% during this period. Proposal managers and top-decile voters are the primary
contributors to this volume spike, with their trading volumes increasing by 59.2% and 52.5%, respectively.
A key manifestation of the conflicts of interest arising from voting power centralization is the poten-
tial for insider trading. Active participants are deeply involved in the decision-making process and wield
substantial influence over its outcomes. As shown by Cornelli and Li (2002), where risk arbitrageurs
5The Ethereum Name Service (ENS) is a decentralized naming protocol built on the Ethereum blockchain that links user
identities to wallet addresses. Blockchain forensics refers to the analysis of on-chain data to draw economic inferences.
6Additionally, we observe that both participation and concentration metrics are higher in DAOs that experience gover-
nance hacking events compared to those that do not. Specifically, DAOs affected by hacks show participation rates, Gini index
values for concentration, and shares of votes held by top voters at 14.2%, 8.94%, and 8.41%, respectively, versus 5.9%, 7.97%,
and 7.58% in unaffected DAOs, suggesting that elevated risk awareness may be associated with more active and concentrated
governance engagement.
3

---

## Page 5

gain an information advantage by choosing to enter takeover contests, governance participants in DAOs
similarly generate private information through their active involvement in proposal and voting processes.
T wo opposing forces shape insider trading dynamics in DAOs: factors that increase its likelihood—such
as limited regulatory oversight and pseudonymous transactions—and factors that constrain it, including
blockchain transparency and the theoretically decentralized nature of governance (Sokolov, 2021; Ami-
ram et al., 2022; Makarov and Schoar, 2022; DeSimone et al., 2025). This tension between opportunity
and constraint makes the extent of insider trading in DAOs an open empirical question, which we sys-
tematically examine in the following analysis.
T o identify insider trading driven by information asymmetry, we compare the trading patterns of
proposal managers and top-decile voters (“blockvoters”) around proposal creation events, examining
whether trades occur selectively before proposals anticipated to yield positive or negative cumulative ab-
normal returns (CARs). If trading is informed, we expect increased purchases before proposals with
positive CARs and increased sales before proposals with negative CARs; in contrast, trading purely to ac-
cumulate voting power should occur regardless of expected price impacts. Consistent with information-
based trading, we find that proposal managers significantly increase purchases before proposals with pos-
itive CARs but show no abnormal activity before negative CARs, while blockvoters increase token pur-
chases indiscriminately before all proposals. This distinct pattern indicates that proposal managers likely
exploit private information to trade profitably, whereas blockvoters primarily accumulate tokens to in-
fluence governance outcomes.
Next, we examine whether governance influencers earn abnormal profits from their trading activities
before proposal creation. W e find that proposal managers achieve 9.5% higher market-adjusted returns
when trading tokens prior to proposal announcements compared to trades executed shortly afterward,
consistent with an information-based advantage. In contrast, blockvoters do not realize significant short-
term returns, supporting our interpretation that their trading is primarily motivated by accumulating
governance power rather than pursuing profits. Notably, the profitability of insider trading is more pro-
nounced in smaller DAOs characterized by limited information transparency and concentrated voting
power—environments where governance influencers are better positioned to exploit informational ad-
vantages and sway outcomes. Importantly, we show that voting mechanisms that enhance community
monitoring or limit blockholders’ voting power significantly reduce insider trading profitability, suggest-
ing that well-designed governance solutions can mitigate conflicts of interest that arise from information
4

---

## Page 6

asymmetries.
T o further separate insider trading from vote accumulation, we leverage the unique setting of the
Compound protocol, a lending platform where interest-bearing tokens (cT okens) are economically af-
fected by proposal outcomes but do not confer any voting rights. This setting allows us to disentangle
trading motivated by information from trading aimed at accumulating governance power. W e find that
Compound voters engage in 6.5 times more transactions of proposal-affected cT okens during the six days
preceding proposal creation. Because these trades cannot influence governance outcomes, this behavior
provides compelling evidence of informed trading based solely on anticipated price impacts, validating
the presence of significant conflicts of interest in the DAO ecosystem.
So far, our analysis documents pervasive centralization in DAOs, generating conflicts of interest sim-
ilar to those observed in traditional governance settings. However, whether voting power accumulation
and insider trading are ultimately detrimental to DAOs is far from straightforward. On one hand, cen-
tralization may help reduce coordination costs, improving decision-making efficiency in decentralized
systems (Shleifer and Vishny, 1986; Hansmann, 2000). On the other hand, it can increase the risk of rent
extraction by insiders and powerful stakeholders, exposing governance inefficiencies that undermine trust
and stability (Grossman and Hart, 1980; Cong and He, 2019). These opposing dynamics become espe-
cially consequential during crises, when token holders’ risk aversion tends to rise sharply (Sockin and
Xiong, 2023; Cong et al., 2023).
T o provide empirical insights into these trade-offs, we examine the economic implications of conflicts
of interest in DAOs. Following Cong et al. (2023), we analyze how the total value locked (TVL) in DAOs
with varying levels of conflicts of interest responds to market-wide negative shocks. 7 Our identification
strategy tests the impact of conflicts of interest on DAO economic performance during two major crises:
the Luna-T erra crash and the FTX collapse. W e employ a difference-in-differences design, categorizing
DAOs based on whether their abnormal trading volume in the month before proposal creation is above
(“treated”) or below (“control”) the sample median, and then comparing their TVL before and after these
events. DAOs with higher conflicts of interest experienced significantly larger TVL declines following
these shocks—18.9% more after the Luna crash and 44.6% more after the FTX collapse—compared to
DAOs with lower conflicts of interest. Overall, our results suggest that conflicts of interest generate sub-
7TVL (T otal V alue Locked) is a key metric in crypto, representing the total dollar value of assets locked in a DeFi protocol.
Conceptually, TVL is akin to a bank’s total deposits, making it useful for studying decentralized finance.
5

---

## Page 7

stantial agency costs in DAOs, which are particularly damaging during crises when effective governance
is critical for organizational survival.
W e acknowledge a few caveats accompanying these insights. First, although our study analyzes one of
the largest empirical samples in the DAO literature, our findings mainly reflect governance dynamics in
larger, more established DAOs with sufficient publicly available data. As decentralized ecosystems evolve,
future research could examine newer DAOs to capture shifting patterns in governance participation and
market dynamics. Additionally, our proxy for abnormal trading volume may include transfers across
wallets belonging to the same owner. Future research could develop more refined methods to filter out
such internal transfers. Despite these limitations, our study provides a comprehensive assessment of the
determinants and economic consequences of governance centralization in DAOs, offering a foundation
for future research on decentralized governance in an increasingly complex landscape.
Our study contributes to several threads of literature, starting with the extensive one on corporate
governance. W e study a novel organizational form that features direct democracy without centralized au-
thorities such as a board of directors or management. W e document a low governance participation rate
of 6.3%, consistent with the well-known free-rider problem in corporate governance (Grossman and Hart,
1980). At the same time, we observe a high degree of centralization, with large token holders dominating
the proposal and voting processes. These findings resonate with Shleifer and Vishny (1986), who argue
that the presence of a large shareholder provides a partial solution to the free-rider problem in corporate
governance. Moreover, we add to the extensive literature on shareholder voting. V oting is a fundamental
channel through which shareholders exercise control over corporate decisions (Y ermack, 2010; Larcker
and T ayan, 2020; Zachariadis et al., 2020). Existing studies have documented that shareholders strate-
gically acquire voting rights before record dates—either through trading or borrowing shares—to sway
proposal outcomes (Bethel et al., 2009; Christoffersen et al., 2007). However, most studies fail to match
specific investors’ trading behaviors with their voting behaviors, and thus provide only aggregate-level ev-
idence of the correlation between trading and voting. Leveraging the transparency of blockchain data, we
match investors’ trading activity with their voting behavior in DAOs, providing direct evidence of vote
trading.
Our study also expands the literature on insider trading. Prior research has extensively documented
how various stakeholders, including corporate executives (Cohen et al., 2012; Dechow et al., 2016; Black-
burne et al., 2021; Jagolinzer et al., 2020), independent directors (Arif et al., 2022; Kim and Oh, 2023),
6

---

## Page 8

industry peers (Deuskar et al., 2024), suppliers (Alldredge and Cicero, 2015), business partners (Mehta
et al., 2021), and banks (Haselmann et al., 2021), trade ahead of material, non-public information events
and earn abnormal profits from such trades. Félez-Viñas et al. (2022) find evidence of insider trading
in the crypto market before exchange coin listing announcements. Our paper extends the analysis to
DAOs—a novel environment characterized by decentralized governance, a lack of regulatory oversight,
and transparent yet anonymous trading activities. W e find that information asymmetry in DAOs allows
stakeholders with privileged access to exploit less-informed investors, adding to the broader literature on
misconducts in the crypto space (Amiram et al., 2022; Cong et al., 2023, 2024; Li et al., 2021; Rabetti, 2023;
Gefen et al., 2024). These findings offer new insights into insider trading in decentralized ecosystems,
contributing to the increasing awareness of the pros and cons of decentralized emerging technologies.
Finally, we contribute to the growing literature on blockchain-based governance by examining two
key aspects of governance and voting dynamics in DAOs. 8 First, while DAOs are designed to promote
inclusive and democratic decision-making, we find low participation rates and highly concentrated vot-
ing power. These results align with existing studies on DAO governance (Appel and Grennan, 2023b,a;
Fritsch et al., 2024; Jiang and Li, 2024; Laturnus, 2023), adding to broader discussions on economic ten-
sions in decentralized organizations (Cong and He, 2019; Sockin and Xiong, 2023; Fracassi et al., 2024).
Ferreira and Li (2024) propose a model showing that DAOs face a trilemma between autonomy, decen-
tralization, and efficiency. Our study complements this by providing empirical evidence of centralization
in DAOs and revealing the economic mechanisms driving it. Second, token-based decentralized gover-
nance can better align founders’ interests with users’ (Bena and Zhang, 2023) whereas centralized struc-
tures in DAOs can create conflicts of interest among stakeholders (Das et al., 2023a; Fan et al., 2024). Han
et al. (2025) show that concentrated ownership fosters conflicts between large participants (“whales”) and
smaller ones, negatively affecting platform growth. Similarly, Bellavitis and Momtaz (2024) finds that de-
viations from decentralization undermine DAO value. Our paper documents a new type of conflict of
interest in DAOs between informed and less informed participants, which exacerbates platform instabil-
ity during market shocks.
The remainder of this study is organized as follows: Section 2 outlines the institutional background
of DAOs and their governance structures; Section 3 details our data sources and sample construction;
Section 4 discusses voting participation rates and voting power concentration across DAOs; Section 5 ex-
8Appel and Grennan (2023b) and Han et al. (2025) provide an excellent introduction to DAOs.
7

---

## Page 9

amines the trading behavior of governance participants around proposal events; Section 6 analyzes insider
trading dynamics, including buy-sell imbalances around proposal creation, the profitability of insider
trades, and the effectiveness of governance mechanisms; Section 7 evaluates the economic implications
of conflicts of interest; and Section 9 concludes.
2 Background and Literature Review
2.1 Decentralized Governance
Interest in decentralized governance is not new. For more than two centuries, organizational forms
such as cooperatives, mutual companies, and commons-based governance systems have promoted mod-
els in which stakeholders directly participate in decision-making, a departure from the standard corpo-
rate paradigm relying on management hierarchical control. The Rochdale Pioneers’ cooperative model
(1844) is a canonical early example of this idea, inspiring generations of decentralized entities with the
goals of aligning ownership and control, fostering equitable benefit distribution, and promoting local
accountability (Hansmann, 2000). These models gained traction not only for philosophical reasons, but
also because they promised practical advantages in mitigating well-documented agency problems in tra-
ditional organizations, including managerial entrenchment, short-termism, and the marginalization of
non-shareholder stakeholders (Ostrom, 1990; Birchall, 2011).
Despite their appeal, traditional decentralized organizations have long struggled with inherent fric-
tions: collective action problems, difficulties raising capital, low participation in governance, and sus-
ceptibility to capture by vocal or strategic minorities (Holmstrom, 1999). The mechanisms that offered
participatory control often introduced inefficiencies that made scaling or adaptation to dynamic envi-
ronments difficult. As a result, decentralized governance models remain largely an ideal, as most organi-
zations continue to rely on hierarchical models of governance, whereby power is concentrated in boards
and executive leadership.
2.2 DAOs on the Blockchain
The recent emergence of Decentralized Autonomous Organizations (DAOs) builds on this legacy of
decentralization while attempting to overcome its limitations. Enabled by blockchain technology—the
8

---

## Page 10

“technology of decentralization” (Davidson et al., 2016)—DAOs are governed by programmable smart
contracts, in which organizational rules are encoded directly into software and automatically self-executed
when pre-specified conditions are met, and voting by token holders, which determine, among other
things, the specific smart contracts to install. This digital infrastructure enables the automation of orga-
nizational decisions and processes from product design to treasury disbursements and voting procedures,
facilitates global participation without geographic limitations, and promotes accountability by creating a
transparent, immutable, and auditable record of decisions (Davidson et al., 2016; De Filippi and Wright,
2018; Laturnus, 2023; Reijers et al., 2016).
Thus, the technological advances enabling modern-day DAOs can be seen as a continuation of a
centuries-long institutional trajectory: one that aspires to flatten hierarchies and reallocate control to
stakeholders. Scholars suggest that DAOs offer a novel and technologically-mediated reconciliation of
scale and participation, previously thought to be at odds in governance design (Hsieh et al., 2018). Unlike
historical cooperatives or mutuals constrained by geography or regulatory form, DAOs operate as border-
less, digitally-native entities. Anyone with internet access and governance tokens can propose, vote on, or
fund organizational decisions, enabling global coordination at previously unattainable scale (Davidson,
2025).
The theoretical rationale behind DAOs rests on their potential to mitigate core governance frictions
identified in traditional firms. Chief among these are principal-agent problems that arise from the sepa-
ration of ownership and control (Jensen and Meckling, 1976), asymmetric information, and limited ac-
countability of corporate insiders. DAOs propose to remedy these through the convergence of own-
ership and control—token holders are both residual claimants and voting participants—and through
cryptographically-enforced transparency and rule enforcement. In theory, such organizations reduce the
scope for managerial opportunism, insider collusion, or off-balance-sheet risk-taking.
2.3 Related Literature
In theory, DAOs offer several advantages over conventional corporations (e.g., Bena and Zhang, 2023).
First, DAOs promote a direct democracy governance model, where stakeholders have decision rights pro-
portional to their ownership of governance tokens. This overlap between principals and agents can poten-
tially reduce the agency problems often seen in traditional corporations, where ownership and control are
separated (Jensen and Meckling, 1976; Fama and Jensen, 1983). Moreover, DAOs intend to involve a broad
9

---

## Page 11

spectrum of stakeholders—ranging from investors and developers to consumers—in the decision-making
process, which can facilitate community building and promote a sustainable ecosystem (Li et al., 2021;
Appel and Grennan, 2023a; Cardillo et al., 2023). Another touted benefit of DAOs is transparency: as all
decisions and governance actions within a DAO are recorded on the blockchain, creating an immutable
and publicly accessible ledger (Das et al., 2023b; Appel and Grennan, 2023b). This real-time transparency
allows any member or outsider to audit or review the organization’s activities, promoting accountability,
reducing the risk of opaque decision-making, and reducing information asymmetry (Cong and He, 2019;
Landsman et al., 2025).9
While DAOs in theory offer compelling solutions to traditional governance problems, early imple-
mentations suggest that new frictions have emerged. A growing literature has begun to explore these
tensions. Bakos and Halaburda (2022) argues that despite DAOs’ decentralized ideal, the tradability of
tokens creates a strong tendency for control to concentrate in the hands of a few entities, effectively rein-
troducing intermediaries. Appel and Grennan (2023a) provide an early exploration of control dynam-
ics within DAOs, offering one of the first empirical analyses of how governance power is distributed in
these digital organizations. Using data on voting outcomes across major DAOs, they highlight the ten-
sion between theoretical decentralization and the practical concentration of control, showing that a small
number of large token holders can exert disproportionate influence over governance decisions. This foun-
dational study illustrates how centralized control can emerge even in systems designed to be decentralized,
setting the stage for subsequent research on DAO governance structures and their implications for orga-
nizational efficiency and fairness. Appel and Grennan (2023b) complements this perspective by finding
that features promoting inclusivity and security are associated with positive abnormal returns, whereas
barriers to proposal adoption correspond to negative returns, suggesting that distinctive governance fea-
tures can significantly affect organizational value.
Han et al. (2025) and Ferreira and Li (2024) deepen this line of inquiry by systematically reviewing
DAO voting data across multiple ecosystems and providing evidence of whale dominance, where a small
number of large token holders can unilaterally sway outcomes. They also highlight issues of off-chain
coordination asymmetries, where information advantages outside the protocol—such as private group
chats or venture capital networks—create unequal influence and undermine the ideal of flat, permission-
less governance. Additionally, these studies document persistent strategic voting behaviors, including
9See Lee et al. (2024) and Luo et al. (2024) for blockchain adoption benefits in the corporate setting.
10

---

## Page 12

vote-buying and delegation patterns that entrench incumbents, which together complicate the narrative
that DAOs naturally achieve genuine decentralization or fair collective choice. T aken together, these in-
sights show that while DAOs innovate on governance mechanics, they also face enduring challenges in
realizing democratic and distributed control.
Complementing these structural concerns, Laturnus (2023) provides evidence from over 2,000 DAOs
showing that while ownership concentration has little predictive power for DAO performance, voting
participation—particularly by small holders—is significantly associated with higher valuations and growth.
Fritsch et al. (2024), Jiang and Li (2024) and Fracassi et al. (2024) corroborate these concerns with em-
pirical analyses of voting power concentration in major DAOs like Compound and Ethereum, highlight-
ing the persistent gap between theoretical decentralization and practical governance dynamics. Bellavitis
and Momtaz (2024) expands the evidence by examining how deviations from decentralized ideals affect
DAO value creation and resilience. Finally, Das et al. (2023b) contributes critical insights into how gov-
ernance incentives and vote-trading behaviors can exacerbate agency conflicts, misaligning the interests
of powerful insiders and minority stakeholders, and challenging the notion of equitable governance in
decentralized systems.
While the existing literature has provided important insights into DAO governance structures, par-
ticipation patterns, and ownership concentration, our study complements this work in several key ways.
First, we examine how concentrated voting power creates conflicts of interest among stakeholders and
facilitates insider trading. Second, we evaluate the extent to which these conflicts of interest affect the
economic development and resilience of DeFi protocols, especially during times of crisis when effec-
tive governance is critical. Finally, we assess whether recent innovations designed to reduce voting power
concentration—such as quadratic voting and delegation mechanisms—are effective in mitigating agency
conflicts in a regulatory-free environment. Overall, our study provides a novel and comprehensive empir-
ical evaluation of whether DAOs fulfill their theoretical promise of overcoming traditional organizational
trade-offs or merely replicate familiar governance problems in a new technological context.
11

---

## Page 13

3 Setting
3.1 Institutional Details of DAOs
Decentralized Autonomous Organizations (DAOs) are a key innovation emerging from the cryp-
tocurrency and blockchain ecosystem. They represent a new form of governance and coordination for
blockchain-based projects. By encoding governance rules in smart contracts on the blockchain, DAOs
automate governance processes, including submission of proposals, design of voting mechanisms, and ex-
ecution of voting outcomes, removing the need for centralized management to lead the decision-making
process. DAOs establish their own governance frameworks, which outline the rules and processes of
decision-making. These frameworks typically specify participant eligibility, the methods used to calculate
voting power for token holders, the criteria for proposal acceptance, and the mechanisms for implement-
ing approved proposals on the blockchain. For instance, Gnosis DAO’s governance framework allows
any member to submit a proposal, but only members holding at least one governance token are eligible
to vote.10 Core teams of DAOs typically use online platforms, particularly social media channels such as
T witter and Discord, to facilitate communication with their members.
Decisions in DAOs are made through a token-based voting system with governance tokens as a cen-
tral component. Most projects integrate governance functions into their native tokens, while others issue
separate tokens for governance and utility purposes.11 In DAOs that implement governance using frame-
works like the Compound Governor contract, governance tokens need to be explicitly delegated—either
to the token holders themselves (self-delegation) or to representatives—to activate their voting power.
Stakeholders with (activated) governance tokens can participate in decision-making by creating and vot-
ing on proposals that determine DAOs’ operations and allocation of resources, including which new
products or features to develop, which budget structure, and which partnerships to find.
A DAO’s governance process typically consists of four phases: forum discussion, off-chain voting,
on-chain voting, and implementation. Figure 2 plots a DAO’s governance process timeline. The process
usually begins with an open discussion in a community forum. Here, a member (often referred to as
the proposer) posts a detailed proposal outlining the intended changes or initiatives. This forum serves
as a space for community members to provide feedback, ask questions, and suggest modifications to the
10https://docs.gnosis.io/docs/Goverance.
11Native tokens perform functions within each blockchain ecosystem and provide access to the platform’s services.
12

---

## Page 14

proposal. The discussion usually takes a few days to several weeks, depending on the proposal’s com-
plexity. After incorporating feedback from the forum discussion, the proposer drafts the final version of
the proposal. This draft is then submitted for voting. In some DAOs, an initial voting round may occur
off-chain using platforms like Snapshot. Off-chain voting is typically gas-free, making it a cost-effective
way for members to express their preferences. DAOs can set up voting strategies to calculate the number
of votes for each voter based on the number of governance tokens in their linked wallets prior to the pro-
posal creation date. T ypically, the more tokens an investor holds, the more vote power they have. This
stage usually lasts for 3-7 days. The proposal may move to the on-chain voting phase if it gains sufficient
preliminary support. DAO members’ votes are submitted as transactions during this phase and recorded
directly on the blockchain. Once a proposal achieves a quorum and receives a majority of affirmative votes
to pass, it is implemented through smart contracts, ensuring that the decisions made by the community
are enforced without requiring a centralized authority.
[Figure 2]
DAOs can implement governance through either off-chain voting, on-chain voting, or a combina-
tion. In a hybrid voting scheme, off-chain voting is commonly used as a preliminary phase to gauge the
community’s stance on a proposal. Only proposals that pass this initial stage move on to on-chain vot-
ing. In some DAOs, representatives or trusted members may replicate the results of off-chain votes onto
the blockchain to trigger the execution of smart contracts while saving transaction fees associated with
on-chain activity. Therefore, for DAOs using off-chain voting, substantive decision-making often occurs
during the off-chain phase. In contrast, the on-chain phase is primarily used to formalize and implement
the outcome.
3.2 Data and Sample
T o provide an empirical investigation of the governance in DAOs, we draw data from several sources.
Information on DAO proposals and voting records is obtained from Snapshot, a popular off-chain vot-
ing platform that allows DAOs to create proposals and manage votes without gas fees. W e start by down-
loading all DAOs available on Snapshot as of September 1, 2023. Given that Snapshot allows anyone to
create and feature a DAO on its voting platform, most DAOs listed are relatively small and lack substan-
tive underlying business activities. Therefore, we only keep DAOs with native ERC-20 tokens listed on
13

---

## Page 15

CoinGecko, which resulted in a reduced sample of 342 DAOs. Each DAO’s Snapshot page lists proposal
manager accounts (wallet addresses) that have been granted high-level permission to manage the space
and its proposals. They are likely core team members engaged in the DAO’s internal operations. Since
the governance rules of DAOs are enforced by smart contracts, any operational changes, even minor ones,
necessitate the creation of a proposal. W e only keep proposals with the number of votes in the top quar-
tile for each DAO to focus on most impactful governance activities. Finally, we ended up with 2,988
proposals in 216 DAOs on Snapshot during 2020-2024. Information on proposals includes a DAO’s
name, proposal title, body, and timeline (i.e., created date, start and end date of voting), voting strategy,
number of votes cast, and scores for each option.
Next, we retrieve information on voting records from Snapshot using its API, which contains the ad-
dresses of voters, each voter’s voting power, and selected choice. Moreover, we gather delegation data on
the sample DAOs from Snapshot’s delegation panels. Each delegate listed on the delegation panel pro-
vides information such as their wallet address, a statement regarding their role or intentions, the number
of delegations they have received, and their total voting power. However, Snapshot’s panels only display
delegations facilitated through their platform. A subsample of DAOs adopts a hybrid voting scheme
that combines both off-chain and on-chain voting. T o account for delegations facilitated through smart
contracts on the blockchain, we supplement this data with information from T ally, a popular on-chain
governance platform.
T o study the behavior of governance participants around proposal events, we complement the DAO
voting data with on-chain transactions from BigQuery, a publicly available parsed Ethereum dataset. The
dataset compiles transaction-level data covering token address, sender address, recipient address, transac-
tion time, number of tokens transferred, and transaction hash (transaction identifier) for each on-chain
transaction. W e aggregate transaction volume at the daily level for each native token in our sample. W e
focus on on-chain volume because on-chain volume is recorded and validated on the blockchain through
consensus mechanisms, ensuring high security and immutability. In contrast, off-chain volume occurs
outside the blockchain and is susceptible to manipulation (Amiram et al., 2020; Cong et al., 2023). Fi-
nally, we collect price information on DAOs’ native tokens from CoinMarketCap, a leading platform
for tracking the market data of crypto assets. CoinMarketCap aggregates trading information from over
200 crypto exchanges, offering daily data on opening, closing, high and low prices, volume, and market
capitalization (in dollars) for over 10,000 crypto assets. CoinMarketCap includes active and defunct cryp-
14

---

## Page 16

tocurrencies, which helps mitigate survivorship bias (Liu and T syvinski, 2021). W e merge DAO voting
data with on-chain transactions and token price data using the token address.
4 Governance Concentration
4.1 Governance Proposals
T able 1 presents summary statistics on the characteristics of DAOs and governance proposals in our
sample. On average, a typical DAO has 13.83 significant proposals listed on Snapshot. Approximately
46% of DAOs maintain an open discussion forum. Proposal initiation is concentrated, with an average
of only four members submitting all proposals within a DAO. Although most investors are eligible to
propose governance actions, a large share of proposals are submitted by a small subset of investors, high-
lighting centralization in proposal creation. Regarding proposal characteristics, the average voting period
is 5.3 days, and proposals contain a combined title and body length of roughly 374.8 words. On average,
2,369 voters cast votes on each proposal, with most proposals passing by a high support ratio of 84.4%.
Proposals typically employ three voting strategies to calculate the voting power of token holders. Among
these, 38.8% of proposals adopt a delegation strategy, while 1.2% use quadratic voting.
W e classify proposals into five categories based on their content, following the framework developed
by Appel and Grennan (2023b): Finance, Governance, Management, T okenomics, and Viability. Pro-
posals can belong to multiple categories. T okenomics emerges as the most frequent category, with ap-
proximately 44% of proposals addressing infrastructure, parameter adjustments, or token supply design.
Viability is also prominent, comprising 40.7% of proposals related to upgrades, maintenance, security,
and similar topics, followed by Governance (32.9%) and Management (20.6%). Finance, which pertains
to the allocation of treasury funds, is the least common category, represented in 16.7% of proposals.
The average participation rate—defined as the proportion of votes cast relative to the total eligible
votes—is approximately 6.3% per proposal in our sample. 12 Casting an informed vote in DAO governance
often requires significant time and effort, as participants must understand the complex technological and
economic mechanisms underlying the organization. The resulting high cognitive and participation costs
12Eligible votes are estimated using the number of circulating tokens on the proposal creation date (or the closest prior
date if unavailable). This estimate may be imperfect, as some proposals allow voting with multiple token types beyond the
governance token or apply a conversion rate other than one-to-one between governance tokens and votes. Proposals with
participation rates exceeding 100% are excluded.
15

---

## Page 17

discourage many token holders from voting. Moreover, while voters incur these costs, the benefits of effec-
tive governance are shared by all token holders, creating a classic free-rider problem well-documented in
corporate governance research (Grossman and Hart, 1980). Additionally, unlike traditional firms where
institutional investors typically have fiduciary duties to vote their shares, institutions holding DAO to-
kens are not subject to such regulatory obligations, contributing further to low voter turnout.
4.2 V oting Power
T o evaluate the degree of centralization in DAO governance, we calculate two metrics that measure
the inequality in the distribution of voting power: the Gini coefficient for votes cast on a proposal and the
fraction of votes controlled by top decile voters in a proposal. As a significant portion of delegated votes
are unexercised, we base our calculations on votes cast on proposals to capture the distribution of voting
powers that are exercised. On average, the Gini coefficient for voting power distribution in a proposal
is about 0.8. The top decile voters control 76.2% of a proposal’s voting power, with the largest voter
alone holding 37.5%. Blockvoters—voters with votes exceeding 5% of a proposal’s total votes—collectively
account for 75.7% of the voting power. Despite their decentralized architecture, DAOs exhibit a high level
of centralization: voting process is dominated by a few large token holders.
By analyzing the Ethereum Name Service (ENS) names linked to the wallet addresses of the top vot-
ers or reviewing their statement in the delegation page, we identify four primary categories to which
they belong: core team members, institutional investors, third-party service providers, and Key Opinion
Leaders (KOLs), which may be either individuals or groups. Let’s use Compound, a lending protocol,
as an example to understand blockvoter’s composition in DAO governance. The voter with the largest
voting power in Compound is a16z, a venture capital fund specializing in crypto and W eb-3 startups.
The second-largest voter is Geoffrey Hayes, the CTO of Compound, followed by an active community
member operating under the pseudonym T ennisBowling. Another prominent voter is Gauntlet, a firm
employed by Compound to offer risk management services.
The left panel of Figure 3 illustrates the evolution of voting power among the top five voters in Com-
pound. A16z consistently holds more than twice the voting power of the second-largest voter throughout
the observed period. The voting power of the second-largest voter increases over time, while the power
held by other voters remains relatively stable. The composition of blockvoters varies significantly across
16

---

## Page 18

DAOs. While some DAOs are dominated by core team members and institutional investors, others fea-
ture a substantial proportion of blockvoters who are KOLs with specialized expertise in the crypto sec-
tor. Moreover, the evolution of voting power demonstrates considerable differences across DAOs. For
instance, the right panel of Figure 3 illustrates the voting power dynamics in Arbitrum, a layer-2 scaling
solution built on Ethereum. Unlike Compound, where voting power remains relatively stable among
top voters, Arbitrum exhibits more dynamic and upward trends in voting power among its leading par-
ticipants. This highlights the diversity in voting power trajectories across different DAOs.
[Figure 3]
Figure 4 illustrates the evolution of voting power concentration over time, where the x-axis represents
the chronological order of proposals within a DAO (e.g., “1” denotes the first proposal, “2” the second,
and so forth). The figure shows the average Gini coefficient and the share of voting power held by the top
decile voters for the first 30 proposals. Both metrics begin at high levels and exhibit a clear upward trend
as DAOs grow over time, indicating an increasing concentration of voting power.
[Figure 4]
The initial concentration of voting power can be attributed to the concentrated token allocation
schemes in DAOs. According to Pantera Capital, early-stage investors and core team members receive
disproportionately large allocations—approximately 28.8% and 20.6%, respectively—of the tokens dis-
tributed among eligible voters. When analyzing active voters, these groups of investors hold an even
greater share due to their heightened engagement in DAO governance, which grants them substantial
influence over voting outcomes.
As DAOs evolve, voting power becomes increasingly concentrated, as active token holders purchase
tokens from less-engaged investors to strengthen their influence over proposal outcomes. This concentra-
tion can help mitigate the free-rider problem (Shleifer and Vishny, 1986) and reduce the costs associated
with collective decision-making (Hansmann, 2000), echoing findings from the corporate governance lit-
erature. However, the absence of stringent regulatory oversight on pre-proposal token trading, combined
with minimal disclosure requirements for significant ownership stakes, facilitates token accumulation by
blockvoters and may exacerbate agency conflicts.
17

---

## Page 19

4.3 Cross-sectional Variation in DAO Governance
W e next investigate the cross-sectional variation in DAO governance by examining how participation
rates and the concentration of voting power differ across DAOs and proposals. T o do so, we regress par-
ticipation rates and concentration measures on a set of DAO- and proposal-level characteristics. Figure
5 presents the estimated coefficients with 95% confidence intervals. The analysis reveals that Yield and
Lending protocols tend to have significantly lower participation rates compared to other types of proto-
cols. Moreover, DAO size—measured by the logarithm of market capitalization—is negatively correlated
with participation, suggesting that larger DAOs experience lower voter engagement. Regarding proposal-
level characteristics, we find that Finance-related proposals attract significantly higher participation than
other categories. Other proposal features, including proposal complexity—proxied by the logarithm of
the total word count in the title and body—and proposal contentiousness—defined as a support ratio
between 30% and 70%—do not exhibit a significant relationship with participation rates.
[Figure 5]
Turning to the concentration of voting power, both the Gini coefficient and the share of voting power
held by the top decile of voters display consistent patterns: voting power tends to be more concentrated
in larger DAOs. Among protocol types, DEXs exhibit the highest levels of concentration, while Yield
protocols show the lowest. Across proposal categories, the ranking of concentration levels from highest to
lowest is Finance, Governance, Management, Viability, and T okenomics. W e also find that more complex
proposals are associated with higher levels of voting power concentration. Finally, contentious proposals
are linked to lower concentration, and this negative relationship is statistically significant at the 10% level
when measured by the share of voting power held by the top decile of voters.
5 Token Trading by Governance Participants
Next, we examine the relationship between investors’ voting and trading behavior by plotting the
trading activities around the proposal creation of two groups of governance participants on Snapshot—
proposal managers and voters. On a DAO’s Snapshot settings page, there is a list of accounts (wallet
18

---

## Page 20

addresses) that are granted permissions to manage the space and its proposals. 13 These roles range from
Admin, who can edit space settings and archive proposals, to Moderators, who can manage proposals
within the space and create new ones. These proposal managers are responsible for reviewing submitted
proposals and facilitating the governance process, and are likely core team members engaged in the DAO’s
internal operations. In addition to these addresses, we also consider voters to capture token holders with
an interest in a proposal.
[Figure 6]
Figure 6 plots the average abnormal trading volume and the abnormal number of transactions by
proposal managers and voters in the [-30,30] window around the creation date of a proposal. Abnor-
mal trading volume (abnormal number of transactions) is the ratio of daily trading volume (number of
transactions) to the average daily trading volume (number of transactions) from 90 days to 30 days before
the creation date minus one. W e observe an abnormal increase in the investors’ trading of native tokens
before the creation of DAO proposals. V olume increases ahead of the proposal creation by about 34%
above the level in the estimation period, jumps by another 45% on the proposal creation date, and then
declines to the previous level 30 days after the proposal is created. The number of transactions exhibits a
similar pattern: it increases by 33% 30 days before the proposal creation and then reverts to the previous
level 30 days after. This pattern indicates that proposal managers and voters start to trade native tokens
more intensively approximately one month before the proposal creation.
T o more rigorously compare the trading behavior of different investors surrounding proposal events,
we estimate the following regression model:
Abvoli,p,t,d = β0 + β1Day[−30, −1]i,p,t,d + β2VotingPeriod i,p,t,d + β3Day[+1, +30]i,p,t,d
+θ′Controls i,d + λd + σi + ϵi,p,t,d
(1)
where Abvoli,p,t,d represents abnormal trading volume, calculated as the percentage increase in trading
volume on the trading dayd relative to the average trading volume during the estimation window, which
is the period from 90 to 60 days before the creation of proposal p by DAO i at time t. For each pro-
posal, we include a time window starting 60 days before the proposal creation and extending to 30 days
13Space is an organization’s account on Snapshot. It serves as a hub for all proposals related to the organization and a source
of information for the users.
19

---

## Page 21

after the voting ends. W e introduce several indicator variables to capture the effect of proposal events on
trading volume. Day[−30, −1]i,p,t,d equals one for the 30 days leading up to the proposal creation and
zero otherwise. VotingPeriod i,p,t,d equals one for days during the voting period, typically 7 days, and zero
otherwise. Day[+1, +30]i,p,t,d equals one for the 30 days following the conclusion of voting and zero oth-
erwise. These indicator variables capture the incremental changes in abnormal trading volume relative to
the control period in the [-60, -31] window. Additionally, we control for a set of variables that may influ-
ence investor trading volume, including the logarithm of market capitalization on the trading day (Size),
return volatility (Return V olatility), and abnormal return (AbReturn) over the [-7,-1] window before the
trading day. DAO fixed effects and year-quarter fixed effects are included to account for DAO-specific
characteristics and time trends.
W e first estimate the regression for the total trading volume. The results are reported in column (1)
of T able 2. The findings show that total trading volume increases by 16.8% in the month preceding pro-
posal creation, remains elevated during the voting period, and increases by 22.4% in the month following
the conclusion of voting. T o identify the investors contributing to this volume increase, we categorize
investors into passive and active investors. Active investors refer to those who play a role in advancing the
proposal, including proposal managers and voters. All other investors are classified as passive. Columns
(2) and (3) display the results for active and passive investors, respectively. The analysis shows active in-
vestors exhibit a more pronounced increase in trading volume around proposal events than passive in-
vestors. Specifically, active investors’ trading volume increases by 48.2% before proposal creation and by
76.2% during the voting period, whereas passive investors’ trading volume increases by only 19.2% and
20.1% over the same periods. The difference between these groups is statistically significant, as indicated
in Column (4). Furthermore, unlike passive investors, whose trading volume peaks after the voting con-
cludes, active investors exhibit the most significant increases in trading volume before and during the
voting period, indicating their tendency to accumulate votes and influence proposal outcomes.
[T able 2]
T able 3 decomposes active investors into proposal managers and voters, and investigates their trading
behavior separately. Columns (2) and (3) show that proposal managers and voters significantly increase
their trading activities by 59.2% and 52.7%, respectively, in the month leading up to the creation of a pro-
posal. This heightened trading activity intensifies during the voting period, with increases of 93.8% for
20

---

## Page 22

proposal managers and 82.5% for voters. Following the voting period, voters display an abnormal trading
volume of 37.9%. In contrast, the trading volume for proposal managers returns to a statistically indis-
tinguishable level from the control period. Column (4) compares the estimates on the time indicators
for voters and proposal managers and finds no significant differences between the two groups, suggesting
that both engage in token trading around proposal events.
[T able 3]
Among voters, those with greater voting power are hypothesized to engage more in token trading
before the proposal creation. In T able 4, we divide voters into deciles based on their voting power on a
proposal and examine their abnormal trading volumes separately. The analysis reveals a significant dis-
parity between the two groups: top voters exhibit abnormal trading volume increases of 52.5% before the
voting period and 80.2% during the voting period, whereas bottom voters show corresponding increases
of 17.9% and 33.9%, respectively. These findings are consistent with our expectations.
[T able 4]
T o summarize our findings, we observe a notable increase in abnormal trading volume before pro-
posal events, primarily driven by proposal managers and top voters who actively participate in the gov-
ernance process and possess significant voting power. This unbalanced trading behavior supports the
hypothesis that blockvoters accumulate voting power before proposal creation, leading to the skewed
distribution of voting power in DAOs.
6 Insider Trading
Proposal managers and top voters are the most active participants in DAO governance, who fre-
quently initiate and cast votes on proposals. Their substantial token holdings through trading before
proposals grant them considerable influence over the organization’s trajectory. Compared to other stake-
holders, these investors often possess superior information about operational developments and the or-
ganization’s future direction. W e refer to them as DAO insiders hereinafter.
As documented in the corporate finance literature, officers, directors, and significant shareholders
who possess material nonpublic information about a listed firm have the incentive to exploit such infor-
mation advantage by buying or selling the company’s securities before the information is made public
21

---

## Page 23

(Cohen et al., 2012; Dechow et al., 2016; Blackburne et al., 2021; Jagolinzer et al., 2020). Insider trading
is prohibited in financial markets under insider trading laws. There are several reasons why insider trad-
ing may exist in the context of DAOs. First, DAOs lack a standard legal structure that subjects them to
a well-defined regulatory framework (Makarov and Schoar, 2020). DAOs whose tokens are classified as
securities are required to comply with SEC regulations, but the classification of DAO tokens remains
contentious and open to interpretation, leaving the legal status of DAOs ambiguous. As a result, insider
trading regulations typically do not apply to DAOs, leading to limited regulatory oversight in this area.
Moreover, the anonymity inherent in blockchain technology complicates the identification of wallets be-
longing to project insiders. The inability to establish users’ legal identities makes holding stakeholders ac-
countable for their actions difficult. The absence of a regulatory framework, combined with blockchain’s
anonymity, exacerbates the challenge of monitoring insider transactions and reduces the legal risks asso-
ciated with such activities. On the other hand, DAOs’ decentralized structure disperses decision-making
rights among token holders, allowing the broader community to participate directly in governance and
influence the organization’s direction. This dispersion of power limits the effective control insiders can
exert over DAO decisions and increases their uncertainty about voting outcomes and associated market
reactions, which likely mitigates their incentives to front-run. In addition, the transparency offered by
blockchain technology ensures that all transactions are recorded and publicly accessible in near real-time,
which diminishes the potential profitability of insider trades and harms insiders’ ex-ante incentive. Based
on these arguments, whether insider trading occurs in DAOs remains an open question.
6.1 Buy-Sell Imbalance Around Proposal Creation
W e start examining governance participants’ insider trading by analyzing their token trading behavior
around the time of proposal creation. W e have shown that these investors exhibit abnormal trading ac-
tivities before proposal creation. These trading behaviors can be driven by either the incentive to acquire
votes or insider information. The two motives yield distinct predictions regarding trading directions be-
fore proposal events. V oting power accumulation suggests increased purchases prior to proposal creation,
irrespective of the proposal’s expected value impact. In contrast, insider trading is associated with strategic
trading behaviors: more purchases before proposals with positive CARs and more sales before proposals
with negative CARs. The asymmetric trading patterns between value-enhancing and value-destroying
proposals provide a framework for distinguishing between vote accumulation and insider trading. T o
22

---

## Page 24

investigate this, we first estimate market-adjusted cumulative abnormal returns (CARs) within a [-3,3]
window around the proposal creation date, and categorize proposals based on whether their CARs are
positive or negative. The average (median) CAR for the sample proposals is 0.040 (0.018), indicating
that, on average, proposals are perceived as value-enhancing.
[T able 5]
W e then examine the buy-sell imbalance of proposal managers and top voters to understand their trad-
ing directions around proposal events. Buy-sell imbalance is calculated as insiders’ net purchase volume
(purchase volume minus sales volume) scaled by their total trading volume on a given day. The analysis
includes trading days in the [-30, 30] window around the creation dates of proposals, where we regress
insiders’ buy-sell imbalance on the Day[−30, −1] indicator along with other control variables specified
in Eq. (1), conditional on whether the proposal generates positive or negative returns. The results are
presented in T able 5. For proposals with positive CARs, proposal managers exhibit a 3.9% higher buy-
sell imbalance in the period before proposal creation compared to the period following it. However, for
proposals with negative CARs, there is no significant difference in buy-sell imbalance before and after
proposal creation. This pattern indicates that proposal managers may have mixed motives when trading
tokens before proposal creation. For proposals with negative CARs, the positive effects of vote accu-
mulation are partially offset by the negative impact of insider trading, resulting in an insignificant net
effect on overall trading behavior. In contrast, top voters consistently make more purchases before pro-
posal creation regardless of whether the proposal has positive or negative CARs, indicating their strategic
accumulation of voting power to influence voting outcomes.
6.2 Profitability of Insider Trades
Short-term profitability provides another way to differentiate insider trading from vote accumula-
tion. While insiders trade before proposal creation to capitalize on short-term gains, trades driven by vote
accumulation are typically motivated by the pursuit of long-term value appreciation and may not yield
significant immediate profits. Thus, we compare the short-term profitability of insider trades made in the
[-30,-1] window around proposal creation to those made over the [0,30] window using the specification:
T radePro f iti, j,t,d = β0 + β1Day[−30, −1]i,t,d + θ′Controls i,d + λi, j,d + ϵi, j,t,d (2)
23

---

## Page 25

where T radePro f iti, j,t,d is measured as BHAR15, the 15-day market-adjusted abnormal buy-and-hold
returns (multiplied by -1 for sales) of a transaction made by investor j on trading day d, around a proposal
created at time t for DAO i. Day[−30, −1]i,t,d is an indicator that takes the value of one if the trade
occurs during the [-30,-1] window before the creation of a proposal, and zero if it occurs during the [0,
+30] window following it. Besides the control variables in Eq. (1), we additionally control forT radeS ize,
which is the number of tokens traded as a percentage of the token circulating supply on a trading day.
Investor × DAO × YearQuarter fixed effects are included to facilitate the comparison of trades made
by the same investor within the same DAO during the same year-quarter.
W e estimate Eq. (2) for the trades made by proposal managers and top voters separately, with the
results reported in T able 6. The coefficients on Day[−30, −1] are positive and significant for proposal
managers, as shown in columns (1) and (2). Specifically, proposal managers earn 9.5% higher market-
adjusted returns when trading tokens before proposal creation. In contrast, top voters do not achieve
significant short-term abnormal profits from their trades before proposal events. This finding, together
with the results in T able 5, further suggests that top voters and proposal managers likely have different
trading motives. The fact that top voters make more purchases before proposal creation irrespective of
a proposal’s price impact, and earn no significant short-term gains, supports the notion that top voters
purchase tokens before proposal creation to accumulate voting power, intending to achieve voting out-
comes that increase platform value and lead to token appreciation in the long run. In subsequent tests,
we only include proposal managers’ trades to study the factors that affect insider trading profitability.
[T able 6]
6.3 DAO Characteristics and Profitability of Insider Trades
W e further explore cross-sectional variations in insider trading profitability. W e expect insider trades
to be more profitable in small DAOs with worse information environments, where the information asym-
metry between insiders and outsiders is likely higher. W e use a DAO’s market capitalization as a proxy for
its size and the presence of an open discussion forum for the quality of the DAO’s information environ-
ment. T ypically, a DAO’s governance process requires a proposer to post a thread on the community’s
discussion forum to gather members’ feedback before creating a formal proposal on Snapshot. An open
discussion process is crucial as it facilitates communication among community members and reduces
24

---

## Page 26

information asymmetry between insiders and outsiders.
W e divide the DAOs into two groups based on whether they have an open discussion forum, and
whether their size, proxied by market capitalization, is in the top or bottom quartile of the sample DAOs.
W e re-estimate Eq. (2) for each subgroup of DAOs. The results are reported in column (1)-(4) of T able
7. Our results show that proposal managers in DAOs without a discussion forum and DAOs whose
size is in the bottom quartile earn 66.3% and 94.7% higher abnormal returns than the sample average. 14
Furthermore, the number of insider trades around proposal events is larger in smaller DAOs and in DAOs
without a discussion forum, consistent with a better information environment deterring insider trading.
[T able 7]
Furthermore, we expect insider trades to be more profitable in DAOs with concentrated voting power.
The significant influence exercised by large investors reduces the uncertainty of voting outcomes, poten-
tially translating into increased profitability of insider trades. T o test this hypothesis, in columns (5) to
(8) of T able 7, we divide DAOs into two groups based on whether their average Gini coefficient of voting
power distributions in proposals or the average fraction of voting power held by top decile voters, falls
into the top or bottom quartile of the sample. W e find more insider trades and greater abnormal returns
on these trades in DAOs where voting power is more concentrated.
6.4 Effects of V oting Strategies
The challenges associated with decentralized governance have garnered significant attention, prompt-
ing various mechanisms aimed at addressing issues such as low participation rates and concentrated voting
power. One such mechanism is the delegation strategy, which allows community members to delegate
their voting power to a representative who votes on their behalf. Delegates are held accountable to the
members who have entrusted their votes, and members can revoke or reassign their delegation if they are
dissatisfied with the delegate’s performance. This strategy enables members who may lack the time or
expertise to participate in every decision to still have their interests represented, thereby enhancing over-
all participation and engagement in the DAO’s governance. Fan et al. (2024) evaluates the effectiveness
of vote delegation mechanisms in DAOs and provides evidence that token holders actively monitor del-
egates and align their incentives through delegation. Therefore, delegation is anticipated to reduce the
14The calculation is as follows: (0.158 − 0.095)/0.095 = 0.663 and (0.185 − 0.095)/0.095 = 0.947.
25

---

## Page 27

insiders’ ability to exploit private information. Additionally, quadratic voting is designed to overcome
the limitations of traditional one-token-one-vote systems by scaling the voting power to the square root
of the voter’s token holdings. For example, investors with 100 tokens are granted 10 votes. By making vot-
ing power a concave function of token holdings, quadratic voting helps to protect minorities and reduce
the influence of blockvoters on voting outcomes, therefore mitigating insider trading.
T o evaluate the effectiveness of the two strategies, we identify proposals that utilize either the delega-
tion or quadratic voting strategy and estimate Eq. (2) for trades made by proposal managers surrounding
these proposals, compared to those associated with proposals that do not employ these strategies. As re-
ported in T able 8, both strategies effectively reduce the profitability of insider trading. After employing
the delegation (quadratic voting) strategy, abnormal returns decline from 9.7% (9.5%) to levels statisti-
cally indistinguishable from zero. These findings suggest that insider trading in decentralized governance
systems can be mitigated by adopting well-designed voting mechanisms that either enhance community
oversight or limit the voting power of large stakeholders.
[T able 8]
6.5 Insider Trading of External Tokens
T o further separate insider trading from vote accumulation, we leverage the unique setting of a lend-
ing protocol, Compound, where the value of its interest-bearing tokens (cT okens) is influenced by pro-
posals but do not confer any voting rights. Compound is a decentralized, Ethereum-based lending pro-
tocol that enables users to lend and borrow cryptocurrency assets. When lenders supply cryptocurrency
assets to the platform’s liquidity pools, they receive cT okens in return for the assets they deposit, repre-
senting their share of the liquidity pool. These cT okens accrue interest through an exchange rate mecha-
nism: over time, each cT oken can be redeemed for an increasing amount of the underlying asset. Lenders
earn interest by redeeming cT okens for more underlying assets based on the exchange rate at the time of
redemption. This exchange rate, automatically adjusted by the protocol, depends on the supply and de-
mand of the underlying asset within the pool and can be altered through the governance process. While
the value of cT okens is affected by governance proposals, cT okens do not grant voting power, annlowing
us to differentiate informed trades from those motivated by voting power accumulation.
[Figure 7]
26

---

## Page 28

T aking advantage of this setting, we investigate whether voters in Compound trade cT okens whose
value is influenced by a proposal before the proposal is posted. Compound has an open discussion forum
where a proposer must post a thread before creating a formal proposal for on-chain voting. As illustrated
in Figure 7, the number of cT oken transactions by voters rises by about 6.5 times approximately six days
before the forum thread is created, followed by a decline back to previous levels within six days after the
discussion date, providing evidence of informed trading.15
7 Consequences of Conflicts of Interest
Thus far, we have shown that proposal managers and top voters engage in abnormal trading activities
before proposal creation, driven both by the intention to accumulate voting power and by insider trading
motives. If a DAO consistently exhibits high levels of abnormal trading before proposal events, it may
indicate that its members are more aggressively engaging in insider trading or competing for voting power.
Such behavior reflects conflicts of interest within the DAO. These conflicts of interest are likely to result
in detrimental real consequences for the DAO’s overall performance.
7.1 Identification Strategy
T o assess the impact of conflicts of interest on DAO performance, we use a popular metric in the
crypto sector—T otal V alue Locked (TVL), which refers to the total value of digital assets locked or staked
in a decentralized finance (DeFi) protocol. W e examine how conflicts of interest influence a DAO’s TVL,
mainly when governance quality is prominent. Specifically, we investigate how the TVL of DAOs with
varying levels of conflicts of interest changes during two market-wide adverse shocks: the T erra-Luna
crash and the FTX collapse.
Luna is the native token of the T erra blockchain. In May 2022, T erraUSD (UST), an algorithmic
stablecoin that was designed to maintain a $1 peg to the US dollar through a mint-and-burn mechanism
involving Luna, lost its peg and caused a massive sell-off, leading to Luna’s hyperinflation and a crash in
price. The Luna network collapse, the largest crypto crash ever, entails an estimated $60 billion wipeout.
15Although cT okens can be transferred and traded like other ERC-20 tokens, price data for cT okens is not available on
CoinMarketCap. Therefore, we cannot directly test the profitability of these cT oken trades. A viable alternative for assessing
the economic benefits of insider trading with cT okens is to gather data on deposit and borrowing interest rates from transac-
tion logs in blockchain records. This remains a future task on our research agenda.
27

---

## Page 29

FTX was a major cryptocurrency exchange founded by Sam Bankman-Fried. In November 2022, it
was revealed that its sister company, Alameda Research, had heavily used FTX customer funds to cover
its risky investments, causing a liquidity crisis. The exchange filed for bankruptcy after failing to meet
customer withdrawal demands, leading to widespread losses and triggering broader concerns across the
crypto industry regarding governance and financial management. The crypto market reacted sharply to
the Luna crash and the FTX collapse, causing a substantial drop in prices and trading volumes for a wide
range of crypto assets.
W e hypothesize that DAOs with higher levels of conflicts of interest are more adversely affected, as
investors may perceive these DAOs as having greater exposure to governance risk.
7.2 Analysis and Results
T o evaluate this, we categorize DAOs into two groups based on whether their average abnormal trad-
ing volume in the month preceding proposal creation dates is above or below the sample median. Figure 8
illustrates the average daily TVL (logarithmic scale) for the two groups of DAOs over a [-60,60] window
surrounding the Luna crash and FTX collapse. Overall, DAOs with higher levels of conflicts of interest
exhibit lower TVL. Following these shocks, both groups experience a significant decline in TVL, with
the reduction being more substantial for DAOs with greater levels of conflicts of interest.
[Figure 8]
T o quantify the difference between the two groups, we estimate the following DID model:
ln(T V Li, j,t) = β0 + β1T reatmenti, j × Postt + β2T reatmenti, j + β3Postt
+θ′Controls i, j,t + λ j + ϵi, j,t
(3)
where ln(T V Li, j,t) represents the natural logarithm of the T otal V alue Locked (TVL) for DAO i in cat-
egory j on day t. The variable T reatmenti, j is an indicator that equals one if DAO i’s average abnormal
trading volume before proposal creation is above the median of the sample, and zero if it is below the
median. Postt is an indicator that equals one if day t is within the [0,60] window following either the
Luna crash on May 9, 2022, or the FTX collapse on November 8, 2022, and zero if it is in the [-60,-1]
pre-event window. W e also control for several variables that may influence a DAO’s TVL, including the
28

---

## Page 30

number of blockchains on which a DAO operates (Numo f Chains), the logarithm of market capitaliza-
tion (S ize), and the daily return ( Return). W e include category fixed effects to control for differences
across DAO types, which include decentralized exchanges (DEX), Lending, Yield, Staking, Derivatives,
Indexes, Services, and Others.
[T able 9] [Figure 9]
Based on the estimates presented in T able 9, DAOs with higher conflicts of interest experience sig-
nificantly larger decreases in TVL following the two market shocks. Specifically, these DAOs suffered
an 18.9% (44.6%) greater decline in TVL after the Luna crash (FTX collapse) compared to DAOs with
lower levels of conflicts of interest. Although Figure 8 shows that DAOs with higher levels of conflicts of
interest generally have lower TVLs, the positive coefficients on theT reatment suggest that after control-
ling for market capitalization and other variables, these DAOs initially have higher TVLs. The negative
coefficients on Post in both columns show that these market shocks negatively impacted the TVL of all
DAOs. T o explore how the effect unfolds over time, we disaggregate thePost variable into weekly indi-
cators from four weeks before the shocks up to seven weeks after. The coefficients on the interactions
between the time indicators and the T reatment dummy are plotted in Figure 9, revealing no significant
pre-shock trends consistent with the parallel trend assumption. The adverse effects begin immediately af-
ter the Luna crash and four weeks after the FTX collapse, persisting throughout the sample period. This
analysis suggests that DAOs with elevated levels of conflicts of interest are more vulnerable to negative
market shocks than their counterparts with lower levels of conflicts of interest.
8 Robustness Checks
This section presents a series of robustness checks to evaluate the reliability and validity of our main
findings. First, rather than using the proposal creation date on Snapshot as the event date, we use the date
the proposal was first posted in the community discussion forum when available.16 While this earlier date
carries some uncertainty — since not all proposals ultimately reach the voting stage — it marks the first
point at which the information is disclosed. W e regress the abnormal trading volume on a series of time
dummies and control variables, and replicate the tests in T able 2 – 4. The results are reported in T able
16Discussion dates are available for 574 out of 2,988 proposals, accounting for roughly one-fifth of the sample.
29

---

## Page 31

A1 and A2. 17 The findings closely mirror those in our main tables. T otal trading volume increases by
approximately 15.3% in the month prior to the proposal’s posting in the discussion forum. This increase
is more pronounced among active investors relative to passive investors (49.3% vs. 17.5%). Among active
participants, proposal managers and top voters are the main drivers of the spike, whose trading volume
rises by 62.2% and 58.2%, respectively. In contrast, voters in the bottom quartile show only a modest
increase of 17%.
Next, we use the abnormal number of transactions as an alternative measure of investor trading be-
havior, which captures the frequency of trades rather than their size. The results, reported in T ables
A3 and A4, continue to show elevated trading activity prior to proposal creation: the total number of
transactions increases by approximately 13.3% in the month leading up to the proposal creation. Active
investors show a more pronounced increase than passive investors (24.2% vs. 15%). However, when we
further decompose active investors into proposal managers, top voters, and bottom voters, the patterns
becomes a little different. T op voters exhibit the largest increase in transaction frequency, followed by bot-
tom voters. In contrast, proposal managers, despite showing a substantial rise in overall trading volume,
only increase their number of transactions moderately (by 18.5%). This suggests that proposal managers
tend to increase the size of trades rather than trading more frequently. T aken together, these findings
offer deeper insights into the trading behaviors of different investor groups around the time of proposal
creation.
In T able A6, we examine the economic consequences of conflicts of interest in DAOs using the alter-
native proxy — the average abnormal number of transactions in the month preceding proposal creation.
DAOs are classified into two groups based on whether their values fall above or below the sample median.
The results are consistent with those in T able 9. In particular, the interaction terms remain significantly
negative for both the Luna crash and the FTX collapse. Coefficients on the control variables also closely
resemble those reported in T able 9, reinforcing the robustness of our findings to alternative measures of
trading activity.
W e also employ an alternative measure of short-term profits in Eq. 2. W e replace BHAR15 with
BHAR30, which extends the buy-and-hold period to 30 days. The results, shown in T able A5, are broadly
consistent with those in T able 6: proposal managers continue to earn significant abnormal returns, while
top voters do not generate abnormal profits. This contrast underscores potential differences in the trad-
17T o save space, we remove the duplicate columns in T able 2 – 4, and consolidate the results into two tables.
30

---

## Page 32

ing motives of the two groups of investors. Notably, proposal managers earn higher returns over the
longer holding period — achieving a 14.6% market-adjusted abnormal return from trades made prior to
proposal creation, compared to those made after. T aken together, these robustness checks support the
validity of our main findings and demonstrate that they are not driven by specific methodological choices.
9 Conclusion
Our findings reveal that, contrary to the promise implied by the “D” in DAOs, governance in these or-
ganizations is often centralized, characterized by low participation rates and highly concentrated voting
power. Corporate governance theory helps explain this centralization, suggesting it can arise naturally
from free-rider problems and coordination costs. Our analysis shows that governance participants, in-
cluding proposal managers and top voters, engage in abnormal trading activity before proposal creation.
A particularly concerning implication of this centralized power structure is the prevalence of insider
trading, whereby influential stakeholders exploit informational advantages to extract wealth from less-
informed token holders. The profitability of insider trading is especially pronounced in smaller DAOs
with poorer information environments and more concentrated voting power, where insiders possess
greater informational advantages and influence over outcomes.
The broader implications of our findings highlight the potential for conflicts of interest to undermine
DAO stability, particularly during periods of market-wide stress. DAOs with higher levels of conflicts
of interest experience significantly larger declines in T otal V alue Locked (TVL) following major market
shocks. Recent market innovations aimed at limiting voting power accumulation—such as quadratic
voting and delegation mechanisms—appear to offer promising avenues for mitigating conflicts of in-
terest. Overall, our study highlights the critical importance of addressing conflicts of interest in DAO
governance and emphasizes the need for effective mechanisms that promote community oversight and
participation.
31

---

## Page 33

References
Aggarwal, R., P. A. Saffi, and J. Sturgess (2015). The role of institutional investors in voting: Evidence
from the securities lending market. The Journal of Finance 70(5), 2309–2346.
Alldredge, D. M. and D. C. Cicero (2015). Attentive insider trading.Journal of Financial Economics 115(1),
84–101.
Amiram, D., B. N. Jørgensen, and D. Rabetti (2022). Coins for bombs: The predictability of on-chain
transfers for terrorist attacks. Journal of Accounting Research 60(2), 427–466.
Amiram, D., E. Lyandres, and D. Rabetti (2020). T rading volume manipulation and competition
among centralized crypto exchanges. Forthcoming. Management Science (Available at https://
pubsonline.informs.org/doi/10.1287/mnsc.2021.02903).
Appel, I. and J. Grennan (2023a). Control of decentralized autonomous organizations. AEA Papers and
Proceedings 113, 182–185.
Appel, I. and J. Grennan (2023b). Decentralized governance and digital asset prices. (Available athttps:
//ssrn.com/abstract=4367209).
Arif, S., J. D. Kepler, J. Schroeder, and D. T aylor (2022). Audit process, private information, and insider
trading. Review of Accounting Studies 27(3), 1125–1156.
Bakos, Y. and H. Halaburda (2022). Will blockchains disintermediate platforms? the problem of cred-
ible decentralization in daos. (Available at https://papers.ssrn.com/sol3/papers.cfm?
abstract_id=4221512).
Bellavitis, C. and P. P. Momtaz (2024). V oting governance and value creation in decentralized au-
tonomous organizations (DAOs). Available at ResearchGate DOI:10.13140/RG.2.2.29565.88805.
Bena, J. and S. Zhang (2023). T oken-based decentralized governance, data economy and platform business
model. Available at SSRN 4248492.
Berg, C., S. Davidson, and J. Potts (2019). Understanding the blockchain economy: An introduction to
institutional cryptoeconomics. Edward Elgar Publishing.
Bethel, J. E., G. Hu, and Q. W ang (2009). The market for shareholder voting rights around mergers and
acquisitions: Evidence from institutional daily trading and voting. Journal of Corporate Finance 15(1),
129–145.
Birchall, J. (2011). People-centred businesses. In People-Centred Businesses: Co-operatives, Mutuals and
the Idea of Membership, pp. 1–19. Springer.
Blackburne, T., J. D. Kepler, P. J. Quinn, and D. T aylor (2021). Undisclosed SEC investigations. Man-
agement Science 67(6), 3403–3418.
Cardillo, G., E. Bendinelli, and G. T orluccio (2023). COVID-19, ESG investing, and the resilience of
more sustainable stocks: Evidence from european firms. Business Strategy and the Environment 32(1),
602–623.
32

---

## Page 34

Christoffersen, S. E., C. C. Geczy, D. K. Musto, and A. V . Reed (2007). V ote trading and information
aggregation. The Journal of Finance 62(6), 2897–2929.
Cohen, L., C. Malloy, and L. Pomorski (2012). Decoding inside information.The Journal of Finance 67(3),
1009–1043.
Cong, L., C. R. Harvey, D. Rabetti, and Z.-Y. Wu (2024). An anatomy of crypto-enabled cybercrimes.
(Forthcoming). Management Science (Available athttps://www.nber.org/papers/w30834).
Cong, L. and Z. He (2019). Blockchain disruption and smart contracts.Review of Financial Studies 32(5),
1754–1797.
Cong, L. W ., K. Grauer, D. Rabetti, and H. Updegrave (2023). Blockchain forensics and crypto-related
cybercrimes. Book chapters. (Available at http://dx.doi.org/10.2139/ssrn.4358561).
Cong, L. W ., W . R. Landsman, E. L. Maydew, and D. Rabetti (2023). T ax-loss harvesting with cryptocur-
rencies. Journal of Accounting and Economics 76(2–3), 101607.
Cong, L. W ., E. Prasad, and D. Rabetti (2023). Financial and informational integration through decen-
tralized oracle networks. (Available at https://dx.doi.org/10.2139/ssrn.4495514).
Cornelli, F. and D. D. Li (2002). Risk arbitrage in takeovers. The Review of Financial Studies 15 (3),
837–868.
Das, N. C., S. Mishra, and K. Sokolov (2023a). Does vote trading improve voting outcome? (Available
at https://ssrn.com/abstract=4592674).
Das, N. C., S. P. Mishra, and K. Sokolov (2023b). Does vote trading improve voting outcome?Available
at https://ssrn.com/abstract=4592674 .
Davidson, S. (2025). The nature of the decentralised autonomous organisation. Journal of Institutional
Economics 21, e5.
Davidson, S., P. De Filippi, and J. Potts (2016). Economics of blockchain. Available at SSRN 2744751.
Davydiuk, T., D. Gupta, and S. Rosen (2023). De-crypto-ing signals in initial coin offerings: Evidence of
rational token retention. Management Science 69(11), 6584–6624.
De Filippi, P. and A. Wright (2018). Blockchain and the law: The rule of code. Harvard University Press.
Dechow, P. M., A. Lawrence, and J. P. Ryans (2016). SEC comment letters and insider sales. The Ac-
counting Review 91(2), 401–439.
DeSimone, L., P. Jin, and D. Rabetti (2025). T ax planning, illiquidity, and credit risks: Evidence from
DeFi lending. (Available at http://dx.doi.org/10.13140/RG.2.2.32320.85760).
Deuskar, P., A. Khatri, and J. Sunder (2024). Insider trading restrictions and informed trading in peer
stocks. Management Science.
Fama, E. F. and M. C. Jensen (1983). Separation of ownership and control. Journal of Law and Eco-
nomics 26(2), 301–325.
33

---

## Page 35

Fan, C., T. Shu, and F. Xie (2024). Is there wisdom among the dao crowd? evidence from vote delegation.
Evidence from V ote Delegation (December 01, 2024).
Félez-Viñas, E., L. Johnson, and T. J. Putnin, š (2022). Insider trading in cryptocurrency markets. (Avail-
able at https://ssrn.com/abstract=4184367).
Ferreira, D. and J. Li (2024). Governance and management of autonomous organizations. Available at
SSRN 4746904.
Fos, V . and C. G. Holderness (2023). The distribution of voting rights to shareholders.Journal of Finan-
cial and Quantitative Analysis 58(5), 1878–1910.
Fracassi, C., M. Khoja, and F. Schär (2024). Decentralized crypto governance? transparency and concen-
tration in ethereum decision-making. Transparency and Concentration in Ethereum Decision-Making
(January 10, 2024).
Fritsch, R., M. Müller, and R. W attenhofer (2024). Analyzing voting power in decentralized governance:
Who controls DAOs? Blockchain: Research and Applications, 100208.
Gefen, O., D. Rabetti, Y. Sun, and C. Zhang (2024). Code-washing: Evidence from open-source
blockchain startups. (Available at https://ssrn.com/abstract=5068292).
Grossman, S. J. and O. D. Hart (1980). T akeover bids, the free-rider problem, and the theory of the
corporation. The Bell Journal of Economics, 42–64.
Han, J., J. Lee, and T. Li (2025). A review of dao governance: Recent literature and emerging trends.
Journal of Corporate Finance, 102734.
Hansmann, H. (2000). The ownership of enterprise. Harvard University Press.
Harvey, C. R. and D. Rabetti (2024). International business and decentralized finance. Journal of Inter-
national Business Studies 55, 840–863.
Haselmann, R., C. Leuz, and S. Schreiber (2021). Know your customer: Relationship lending and bank
trading. (Available at https://ssrn.com/abstract=3903968).
Holmstrom, B. (1999). Future of cooperatives: A corporate perspective. Liiketaloudellinen
aikakauskirja, 404–417.
Howell, S. T., M. Niessner, and D. Y ermack (2020). Initial coin offerings: Financing growth with cryp-
tocurrency token sales. The Review of Financial Studies 33(9), 3925–3974.
Hsieh, Y.-Y., J.-P. V ergne, P. Anderson, K. Lakhani, and M. Reitzig (2018). Bitcoin and the rise of decen-
tralized autonomous organizations. Journal of Organization Design 7(1), 1–16.
Hu, H. T. and B. Black (2007). Hedge funds, insiders, and the decoupling of economic and voting
ownership: Empty voting and hidden (morphable) ownership. Journal of Corporate Finance 13(2-3),
343–367.
34

---

## Page 36

Jagolinzer, A. D., D. F. Larcker, G. Ormazabal, and D. J. T aylor (2020). Political connections and the
informativeness of insider trades. The Journal of Finance 75(4), 1833–1876.
Jensen, M. C. and W . H. Meckling (1976). Theory of the firm: Managerial behavior, agency costs and
ownership structure. Journal of Financial Economics 3(4), 305–360.
Jensen, M. C. and W . H. Meckling (1992). Specific and general knowledge, and organizational structure.
In L. W erin and H. Wijkander (Eds.),Contract Economics, pp. 251–274. Oxford: Blackwell.
Jiang, W . and T. Li (2024). Corporate governance meets data and technology. (Available at https:
//ssrn.com/abstract=4746141).
Kim, S. and S. Oh (2023). Outside directors’ insider trading around board meetings.Review of Accounting
Studies, 1–33.
Landsman, W . R., E. Lyandres, E. L. Maydew, and D. Rabetti (2025, March). Auditing smart con-
tracts. Available at SSRN: https://ssrn.com/abstract=5198563 or http://dx.doi.org/
10.2139/ssrn.5198563. HKU Jockey Club Enterprise Sustainability Global Research Institute -
Archive.
Larcker, D. and B. T ayan (2020).Corporate governance matters. FT Press.
Laturnus, V . (2023). The economics of decentralized autonomous organizations. (Available at https:
//ssrn.com/abstract=4320196).
Lee, S. W ., J. Pinto, D. Rabetti, and G. Sadka (2024). Blockchain-induced supply chain transparency and
firm performance: The role of capacity utilization. (Available at https://ssrn.com/abstract=
4921795).
Levit, D., N. Malenko, and E. Maug (2024). T rading and shareholder democracy. The Journal of Fi-
nance 79(1), 257–304.
Li, T., D. Shin, and B. W ang (2021). Cryptocurrency pump-and-dump schemes. (Available at https:
//ssrn.com/abstract=3267041).
Li, T.-T., K. W ang, T. Sueyoshi, and D. D. W ang (2021). ESG: Research progress and future prospects.
Sustainability 13(21), 11663.
Liu, Y. and A. T syvinski (2021). Risks and returns of cryptocurrency. The Review of Financial Stud-
ies 34(6), 2689–2727.
Luo, M., D. Rabetti, and S. Yu (2024). Blockchain adoption and audit quality. (Avaliable at https:
//ssrn.com/abstract=5074602).
Lyandres, E., B. Palazzo, and D. Rabetti (2022). Initial coin offering (ICO) success and post-ICO perfor-
mance. Management Science 68(12), 8658–8679.
Lyandres, E. and D. Rabetti (2024). Initial coin offerings. In D. Cumming and B. Hammer (Eds.), The
Palgrave Encyclopedia of Private Equity. Cham: Palgrave Macmillan.
35

---

## Page 37

Makarov, I. and A. Schoar (2020). T rading and arbitrage in cryptocurrency markets.Journal of Financial
Economics 135(2), 293–319.
Makarov, I. and A. Schoar (2022). Blockchain analysis of the Bitcoin market. (Available at https:
//www.nber.org/papers/w29396).
Mehta, M. N., D. M. Reeb, and W . Zhao (2021). Shadow trading.The Accounting Review 96(4), 367–404.
Ostrom, E. (1990). Governing the commons: The evolution of institutions for collective action. Cambridge
university press.
Rabetti, D. (2023). Auditing decentralized finance (defi) protocols. (Available at http://dx.doi.
org/10.2139/ssrn.4458298).
Reijers, W ., F. O’Brolcháin, and P. Haynes (2016). Governance in blockchain technologies & social con-
tract theories. Ledger 1, 134–151.
Shleifer, A. and R. W . Vishny (1986). Large shareholders and corporate control. Journal of political
economy 94(3, Part 1), 461–488.
Sockin, M. and W . Xiong (2023). Decentralization through tokenization. The Journal of Finance 78(1),
247–299.
Sokolov, K. (2021). Ransomware activity and blockchain congestion. Journal of Financial Eco-
nomics 141(2), 771–782.
Y ermack, D. (2010). Shareholder voting and corporate governance. Annual Review of Financial Eco-
nomics 2(1), 103–125.
Zachariadis, K. E., D. Cvijanovic, and M. Groen-Xu (2020). Free-riders and underdogs: Participation in
corporate voting. European Corporate Governance Institute–Finance W orking Paper(649).
36

---

## Page 38

Figures
Figure 1. DAOs’ Total Treasury.
The figure depicts the monthly total assets owned (in billions) and managed by DAOs listed on DeepDAO from January 2021
to March 2025.
Figure 2. Timeline of DAOs’ Governance Process.
The figure illustrates the typical timeline of DAOs’ governance process and the intervals between each phase.
37

---

## Page 39

Figure 3. Evolution of V oting Power by Top Delegates.
The figure is a snapshot from T ally, which illustrates the monthly evolution of voting power held by the top five delegates
in Compound and Arbitrum, respectively, from their listing on T ally (March 1, 2022, for Compound and March 1, 2023, for
Arbitrum) through December 1, 2024.
Figure 4. Evolution of V oting Power Concentration.
The figure shows the average Gini coefficient and the share of voting power held by the top decile voters for the first 30 proposals
in sample DAOs. The x-axis represents the chronological order of proposals within a DAO (e.g., 1 denotes the first proposal,
2 the second, and so forth).
38

---

## Page 40

(a) Participation Rate
 (b) V oting Power Concentration
Figure 5. Governance across DAOs/Proposals
The figure plots the standardized coefficients with 95% confidence intervals from regressions of participation rates (Panel (a))
and concentration measures (Panel (b)) on DAO- and proposal-level characteristics.
Figure 6. Abnormal Trading V olume and Number of Transactions around Proposal Creation Date.
The figure plots the average abnormal trading volume and abnormal number of transactions of proposal managers and voters
on days around the creation date of proposals with votes in the top quartile in a sample DAO. Abnormal trading volume
(abnormal number of transactions) is the ratio of daily trading volume (number of transactions) to the average daily trading
volume (number of transactions) from 90 days to 30 days before the proposal creation minus one.
39

---

## Page 41

Figure 7. V oters’ Number of Transactions around Compound Proposal Creation.
The figure plots Compound voters’ average number of transactions of cT okens around the discussion date of proposals.
Figure 8. TVL around Luna/FTX Crash.
The figure plots the average daily TVL of two groups of DAOs – DAOs with average abnormal trading volume in the one
month before proposal creation dates above or below the sample median – in the [-60d, 60d] window around the Luna crash
or FTX collapse.
40

---

## Page 42

Figure 9. Parallel Trend and Dynamic Effect of Luna/FTX Crash.
The figure plots the estimated coefficients on the interaction terms of T reatment and week dummies from a Difference-in-
Difference (DID) model in which the dependent variable is DAOs’ daily TVL. The sample consists of days in the [-60, 56]
window around two negative market shocks – Luna crash and FTX collapse – for all the DAOs with TVL data on Defillama.
DAOs are divided into quartiles based on their average abnormal trading volume in the two weeks before proposal creation
dates. T reatment is an indicator that equals one if a DAO is in the top quartile, and zero if a DAO is in the bottom quartile.
W eek dummies take the value of one for days in the week, and zero otherwise.
41

---

## Page 43

Tables
Table 1. Summary Statistics.
The table reports the summary statistics of the variables in the sample. All the variables are defined in Appendix A.
Obs. Mean SD Min Median Max
DAO Characteristics:
Number of Proposals per DAO 216 13.833 33.313 1.000 5.000 392.000
Num of Creators per DAO 216 3.870 5.317 1.000 2.000 40.000
Has Forum 216 0.458 0.499 0.000 0.000 1.000
Proposal Characteristics:
Duration 2,988 5.306 3.226 0.000 5.000 16.000
Num of W ords 2,988 374.831 404.595 2.000 237.000 2,771.000
Num of V oters 2,988 2,369.180 27,217.686 2.000 86.000 510,523.000
Support Ratio of Winning Option 2,988 0.844 0.243 0.027 0.991 1.000
Num of V oting Strategies 2,988 3.013 2.331 1.000 2.000 8.000
Delegation 2,988 0.388 0.487 0.000 0.000 1.000
Quadratic V oting 2,988 0.012 0.108 0.000 0.000 1.000
Finance 2,988 0.167 0.373 0.000 0.000 1.000
Governance 2,988 0.329 0.470 0.000 0.000 1.000
Management 2,988 0.206 0.405 0.000 0.000 1.000
T okenomics 2,988 0.440 0.496 0.000 0.000 1.000
Viability 2,988 0.407 0.491 0.000 0.000 1.000
Participation Rate 2,554 0.063 0.115 0.000 0.022 0.994
Gini 2,900 0.801 0.202 0.000 0.863 0.999
T op Decile V oters (%) 2,569 0.762 0.230 0.029 0.828 1.000
Blockvoters (%) 2,900 0.762 0.240 0.000 0.839 1.000
Largest V oter (%) 2,900 0.375 0.242 0.002 0.312 1.000
Daily Market Metrics:
Abvol 252,331 0.305 2.604 –1.000 –0.394 24.402
Size 252,331 17.844 3.794 0.000 18.457 23.641
AbReturn 252,331 0.001 0.191 –1.037 –0.023 6.099
Return V olatility 252,331 0.093 1.471 0.000 0.049 80.394
T rade Size 244,334 0.046 0.151 0.000 0.012 8.590
TVL 117,846 355.222 1,175.815 0.000 18.542 8,724.258
Insider Trades:
BHAR15 374,326 –0.024 0.484 –5.994 –0.016 5.975
42

---

## Page 44

Table 2. Abnormal Trading around Proposal Creation.
The table reports the estimates from OLS regressions of abnormal trading volume of DAOs’ native tokens for different groups
of investors. The sample consists of trading days from 60 days before the creation date of a proposal to 30 days after the voting
end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent variable is Abvol,
which is the ratio of daily trading volume to the average daily trading volume from 90 days to 60 days before the proposal
creation minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window before the
proposal creation, and zero otherwise. V oting Periodis an indicator that takes the value of one for trading days in the voting
window, and zero otherwise. Day[+1,+30] is an indicator that takes the value of one for trading days in the [+1,+30] window
after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control period. All the
control variables are defined in Appendix A. Column (1) presents the estimates for all investors’ abnormal trading volume.
Column (2) presents the estimates for the abnormal trading volume of active investors involved in advancing the proposal,
including proposal managers listed in the administrator section on the DAO’s Snapshot page and individuals who cast votes
on the proposal. Column (3) presents the estimates for the abnormal trading volume of all other investors, classified as passive
investors. Differences between the coefficients in column (2) and (3) are displayed in column (4). The regressions control for
year-month fixed effects and DAO fixed effects. The standard errors are clustered by DAO. P-values are reported in parentheses.
The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels, respectively.
(1) (2) (3) (4)
All Active Passive
Investors Investors Investors Diff.(2)-(3)
Variables of interest:
Day[–30,–1] 0.168** 0.482*** 0.192** 0.290***
(0.033) (0.000) (0.049) (0.001)
V oting Period 0.176** 0.762*** 0.201* 0.561***
(0.047) (0.000) (0.067) (0.000)
Day[+1,+30] 0.224** 0.422*** 0.263** 0.159*
(0.026) (0.001) (0.039) (0.075)
Controls:
Size –0.022 –0.052 –0.020
(0.487) (0.281) (0.539)
Return V olatility 0.019** 0.014* 0.019**
(0.014) (0.057) (0.022)
AbReturn 0.870*** 0.720** 0.992***
(0.000) (0.039) (0.001)
Y ear-Month FE Y es Y es Y es
DAO FE Y es Y es Y es
Adj. R2 0.101 0.030 0.099
Obs. 252,331 245,075 252,156
43

---

## Page 45

Table 3. Active Investors’ Abnormal Trading around Proposal Creation.
The table reports the estimates from OLS regressions of abnormal trading volume of DAOs’ native tokens for different groups
of active investors. The sample consists of trading days from 60 days before the creation date of a proposal to 30 days after
the voting end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent variable
is Abvol, which is the ratio of daily trading volume to the average daily trading volume from 90 days to 60 days before the
proposal creation minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window
before the proposal creation, and zero otherwise. V oting Periodis an indicator which takes the value of one for trading days
in the voting window, and zero otherwise. Day[+1,+30] is an indicator which takes the value of one for trading days in the
[+1,+30] window after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control
period. All the control variables are defined in Appendix A. Column (1) presents the estimates for the abnormal trading
volume of active investors involved in advancing the proposal, including proposal managers listed in the administrator section
on the DAO’s Snapshot page and individuals who cast votes. Columns (2) and (3) present the estimates for proposal managers’
and voters’ abnormal trading volume, respectively. Differences between the coefficients in column (2) and (3) are displayed in
column (4). The regressions control for year-month fixed effects and DAO fixed effects. The standard errors are clustered
by DAO. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels,
respectively.
(1) (2) (3) (4)
Active Proposal
Investors Managers V oters Diff.(2)-(3)
Variables of interest:
Day[–30,–1] 0.482*** 0.592* 0.527*** 0.065
(0.000) (0.087) (0.000) (0.860)
V oting Period 0.762*** 0.938** 0.825*** 0.113
(0.000) (0.028) (0.000) (0.794)
Day[+1,+30] 0.422*** 0.773 0.379*** 0.394
(0.001) (0.182) (0.000) (0.504)
Controls:
Size –0.052 –0.579** –0.026
(0.281) (0.019) (0.546)
Return V olatility 0.014* 0.141*** 0.009
(0.057) (0.000) (0.159)
AbReturn 0.720** 2.088** 0.567*
(0.039) (0.044) (0.071)
Y ear-Month FE Y es Y es Y es
DAO FE Y es Y es Y es
Adj. R2 0.030 0.041 0.029
Obs. 245,075 136,886 234,366
44

---

## Page 46

Table 4. V oters’ Abnormal Trading around Proposal Creation.
The table reports the estimates from OLS regressions of abnormal trading volume of DAOs’ native tokens for different groups
of voters. The sample consists of trading days from 60 days before the creation date of a proposal to 30 days after the voting end
date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent variable isAbvol, which
is the ratio of daily trading volume to the average daily trading volume from 90 days to 60 days before the proposal creation
minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window before the proposal
creation, and zero otherwise. V oting Periodis an indicator which takes the value of one for trading days in the voting window,
and zero otherwise. Day[+1,+30] is an indicator which takes the value of one for trading days in the [+1,+30] window after
the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control period. All the control
variables are defined in Appendix A. Column (1) presents the estimates for the abnormal trading volume of all voters who cast
votes on the proposal. Column (2) presents the estimates for the abnormal trading volume of voters whose voting powers are
in the top decile among all voters. Column (3) presents the estimates for the abnormal trading volume of voters whose voting
powers are in the bottom decile among all voters. Differences between the coefficients in columns (2) and (3) are displayed
in column (4). The regressions control for year-month fixed effects and DAO fixed effects. The standard errors are clustered
by DAO. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels,
respectively.
(1) (2) (3) (4)
T op Bottom
V oters V oters V oters Diff.(2)-(3)
Variables of interest:
Day[–30,–1] 0.527*** 0.525*** 0.179*** 0.346**
(0.000) (0.001) (0.002) (0.033)
V oting Period 0.825*** 0.802*** 0.339*** 0.463***
(0.000) (0.000) (0.002) (0.005)
Day[+1,+30] 0.379*** 0.290*** –0.071 0.361**
(0.000) (0.009) (0.355) (0.010)
Controls:
Size –0.026 –0.103 –0.040
(0.546) (0.126) (0.330)
Return V olatility 0.009 0.024*** 0.038***
(0.159) (0.000) (0.000)
AbReturn 0.567* 0.930*** 0.549*
(0.071) (0.000) (0.090)
Y ear-Month FE Y es Y es Y es
DAO FE Y es Y es Y es
Adj. R2 0.029 0.027 0.025
Obs. 234,366 196,613 110,325
45

---

## Page 47

Table 5. Insiders’ Trading Strategy.
The table reports the estimates from OLS regressions of insiders’ buy-sell imbalance. The sample consists of trading days in
the [-30, 30] window around the creation dates of proposals with votes in the top quartile in a sample DAO. The dependent
variable isBSI, which is insiders’ purchase volume minus sales volume divided by insiders’ total trading volume on a trading day.
Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window before the proposal creation, and
zero otherwise. All the control variables are defined in Appendix A. Proposals are classified into two groups based on whether
their market-adjusted cumulative abnormal returns (CARs) within a [-3,3] window around the creation date is positive or
negative. Columns (1) and (2) present the estimates for proposal managers’ buy-sell imbalance around the creation date of
proposals with negative CARs and positive CARs, respectively. Columns (3) and (4) present the estimates for top voters’ buy-
sell imbalance around the creation date of proposals with negative CARs and positive CARs, respectively. The regressions
control for year-month fixed effects and DAO fixed effects. The standard errors are clustered by DAO. P-values are reported
in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels, respectively.
Proposal Managers T op V oters
(1) (2) (3) (4)
Neg. CAR Pos. CAR Neg. CAR Pos. CAR
Variables of interest:
Day[–30,–1] –0.009 0.039** 0.125*** 0.144***
(0.544) (0.040) (0.003) (0.000)
Controls:
Size –0.001 –0.023 –0.016*** –0.017***
(0.924) (0.220) (0.000) (0.000)
Return V olatility –0.001 0.156 –0.009*** 0.004
(0.957) (0.119) (0.000) (0.845)
AbReturn –0.078 –0.109 –0.095* –0.161***
(0.144) (0.172) (0.097) (0.007)
Y ear-Month FE Y es Y es Y es Y es
DAO FE Y es Y es Y es Y es
Adj. R2 0.253 0.256 0.049 0.052
Obs. 6,706 8,897 25,649 31,666
46

---

## Page 48

Table 6. Profitability of Insider Trades.
The table reports the estimates from OLS regressions of the profitability of insiders’ trades around DAO voting. The sample
consists of purchases and sales made by insiders in sample DAOs between 30 days before the proposal creation and 30 days after
the end of voting. The dependent variable isBHAR15, the 15-day market-adjusted abnormal buy-and-hold returns (multiplied
by -1 for sales) to insider trades. Day[-30,-1] is an indicator that takes the value of one if the insider trade occurs during the [-
30,-1] window before the proposal creation and zero otherwise. All the control variables are defined in Appendix A. Columns
(1) and (2) present the estimates for trades made by proposal managers. Columns (3) and (4) present the estimates for trades
made by top voters. The regressions control for investor-DAO-year-quarter fixed effects. The standard errors are clustered by
the proposal manager. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and
1% levels, respectively.
Proposal Managers T op V oters
(1) (2) (3) (4)
Variable of interest:
Day[–30,–1] 0.131** 0.095** –0.058 0.001
(0.035) (0.044) (0.194) (0.910)
Controls:
Size –0.080*** 0.059***
(0.000) (0.000)
Return V olatility –0.018* –0.000
(0.064) (0.880)
AbReturn –0.560*** 0.242
(0.000) (0.143)
T rade Size 0.092*** 0.022***
(0.000) (0.000)
Investor × DAO
× Y earQuarter FE Y es Y es Y es Y es
Adj. R2 0.079 0.488 0.032 0.194
Obs. 79,131 73,487 283,527 253,024
47

---

## Page 49

Table 7. DAO Characteristics and Insider Trading Profitability.
The table reports the estimates from OLS regressions of the profitability of insiders’ trades in different groups of DAOs. The sample consists of purchases and sales made by
proposal managers in sample DAOs between 30 days before the proposal creation and 30 days after the end of voting. The dependent variable isBHAR15, the 15-day market-
adjusted abnormal buy-and-hold returns (multiplied by -1 for sales) to insider trades. Day[-30,-1] is an indicator that takes the value of one if the insider trade occurs during
the [30,0) window before the proposal creation and zero otherwise. All the control variables are defined in Appendix A. Columns (1) and (2) present the estimates for trades
made by proposal managers in DAOs without a discussion forum versus those with a discussion forum, respectively. Columns (3) and (4) present the estimates for trades
made by proposal managers in DAOs whose market capitalization is in the bottom quartile among the sample DAOs versus those whose market capitalization is in the top
quartile, respectively. Columns (5) and (6) present the estimates for trades made by proposal managers in DAOs whose average Gini coefficient of voting power distributions
in proposals is in the bottom quartile among the sample DAOs versus those whose average Gini coefficient is in the top quartile, respectively. Columns (7) and (8) present the
estimates for trades made by proposal managers in DAOs whose average fraction of voting power held by top decile voters is in the bottom quartile among the sample DAOs
versus those whose average fraction is in the top quartile, respectively. The regressions control for admin-DAO-year-quarter fixed effects. The standard errors are clustered by
the administrator. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels, respectively.
Has Forum DAO Size Gini T op V oters%
(1) (2) (3) (4) (5) (6) (7) (8)
No Y es Low High Low High Low High
Variable of interest:
Day[–30,–1] 0.158*** 0.036*** 0.185*** 0.002 –0.005 0.159*** –0.004 0.171***
(0.000) (0.000) (0.000) (0.832) (0.713) (0.000) (0.765) (0.000)
Controls:
Size –0.080*** –0.050 –0.085*** 0.003 –0.002 –0.079*** –0.002 –0.083***
(0.000) (0.271) (0.000) (0.415) (0.902) (0.000) (0.919) (0.000)
Return V olatility –0.096 –0.006 –0.204*** –0.725 –0.006 –0.013** 0.001 –0.169
(0.516) (0.131) (0.000) (0.185) (0.958) (0.013) (0.994) (0.118)
AbReturn –0.627*** –0.077*** –0.661*** –0.035 –0.009 –0.659*** –0.014 –0.648***
(0.000) (0.000) (0.000) (0.363) (0.705) (0.000) (0.392) (0.000)
T rade Size 0.026 0.089*** 0.159*** –0.025 0.033* 0.072 –0.076 0.104
(0.802) (0.000) (0.000) (0.593) (0.084) (0.166) (0.187) (0.170)
Investor × DAO
× Y earQuarter FE Y es Y es Y es Y es Y es Y es Y es Y es
Adj. R2 0.531 0.338 0.554 0.111 0.138 0.540 0.138 0.541
Obs. 44,009 29,242 41,849 4,330 5,318 44,069 4,050 44,104
48

---

## Page 50

Table 8. V oting Strategies and Insider Trading Profitability.
The table reports the estimates from OLS regressions of insiders’ trades’ profitability in different proposal groups. The sample
consists of purchases and sales made by proposal managers in sample DAOs between 30 days before the proposal creation and
30 days after the end of voting. The dependent variable isBHAR15, the 15-day market-adjusted abnormal buy-and-hold returns
(multiplied by -1 for sales) to insider trades. Day[-30,-1] is an indicator that takes the value of one if the insider trade occurs
during the [30,0) window before the proposal creation and zero otherwise. All the control variables are defined in Appendix
A. Columns (1) and (2) present the estimates for trades made by proposal managers around proposals that do not employ
delegation strategy versus those that employ delegation strategy, respectively. Columns (3) and (4) present the estimates for
trades made by proposal managers around proposals that do not employ quadratic voting strategy versus those that employ
quadratic voting strategy, respectively. The regressions control for admin-DAO-year-quarter fixed effects. The standard errors
are clustered by the administrator. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the
10%, 5%, and 1% levels, respectively.
Delegation Quadratic V oting
(1) (2) (3) (4)
No Y es No Y es
Variable of interest:
Day[–30,–1] 0.097** –0.012 0.095** 0.005
(0.042) (0.166) (0.045) (0.949)
Controls:
Size –0.080*** 0.003 –0.080*** 0.003
(0.000) (0.762) (0.000) (0.777)
Return V olatility –0.016* –0.072*** –0.015* –0.071***
(0.051) (0.000) (0.051) (0.000)
AbReturn –0.563*** –0.176*** –0.562*** –0.179***
(0.000) (0.000) (0.000) (0.000)
T rade Size 0.093*** 0.136*** 0.092*** 0.137***
(0.000) (0.000) (0.000) (0.000)
Investor × DAO
× Y earQuarter FE Y es Y es Y es Y es
Adj. R2 0.492 0.587 0.491 0.589
Obs. 70,547 29,536 73,180 26,905
49

---

## Page 51

Table 9. Effect of Negative Shocks on DAOs’ TVL.
The table reports the estimates from a Difference-in-Difference (DID) model in which the dependent variable is DAOs’ daily
TVL. The sample consists of days in the [-60, 60] window around two negative market shocks – Luna crash and FTX collapse
– for all the DAOs with TVL data on Defillama. DAOs are divided into quartiles based on their average abnormal trading
volume one month before proposal creation dates. Treatment is an indicator that equals one if a DAO is above the sample
median and zero if a DAO is below the sample median.Post is an indicator that equals one after the Luna crash on 9 May 2022
in column (1), or after the FTX collapse on 8 Nov 2022 in column (2), and zero otherwise. All the control variables are defined
in Appendix A. The regressions control for industry-fixed effects. P-values are reported in parentheses. The symbols *, **, and
*** denote significance at the 10%, 5%, and 1% levels, respectively.
(1) (2)
Luna FTX
Variables of interest:
T reatment× Post –0.189** –0.446***
(0.025) (0.000)
T reatment 0.628*** 0.255***
(0.000) (0.002)
Post –0.701*** 0.065
(0.000) (0.376)
Controls:
Num of Chains 0.242*** 0.167***
(0.000) (0.000)
Size 0.177*** 0.095***
(0.000) (0.000)
Return –0.459* –0.303
(0.082) (0.489)
Industry FE Y es Y es
Adj. R2 0.496 0.213
Obs. 8,984 11,088
50

---

## Page 52

Appendix
Variable Definitions.
V ariable Definition Source
Abvol Ratio of daily trading volume to the average daily trading vol-
ume from 90 days to 60 days before the proposal creation mi-
nus one.
BigQuery
Buy-sell Imbalance (BSI)Insiders’ purchase volume minus sales volume divided by insid-
ers’ total trading volume on a trading day.
BigQuery
BHAR15 15-day market-adjusted abnormal buy-and-hold returns (multi-
plied by -1 for sales).
CoinMarketCap
Day[-30,-1] An indicator that takes the value of one for trading days in the [-
30,-1] window before the proposal creation, and zero otherwise.
Snapshot
V oting Period An indicator that takes the value of one for trading days in the
voting window and zero otherwise.
Snapshot
Day[+1,+30] An indicator that takes the value of one for trading days in the
[+1,+30] window after the voting end date, and zero otherwise.
Snapshot
Size Logarithm of a DAO’s market capitalization plus one. CoinMarketCap
Return V olatility Standard deviation of daily token returns during the [-7,-1] win-
dow prior to a trading day.
CoinMarketCap
AbReturn Market-adjusted buy-and-hold abnormal return over the [-7,-1]
window prior to a trading day.
CoinMarketCap
Trade Size Number of tokens traded as a percentage of the token circulat-
ing supply on a trading day
BigQuery, CoinMarketCap
Total V alue Locked
(TVL)
T otal value of digital assets locked or staked in a DAO’s smart
contracts.
Defillama
Treatment An indicator that equals one if a DAO’s average abnormal trad-
ing volume in the one month prior to proposal creation dates
is in the top quartile among the sample DAOs, and zero if a
DAO’s average abnormal trading volume is in the bottom quar-
tile.
BigQuery, Snapshot
Post An indicator that equals one after the Luna crash on 9 May 2022
or after the FTX collapse on 8 Nov 2022, and zero otherwise.
CoinDesk
Num of Chains Number of blockchains on which a DAO operates. Defillama
Number of Proposals per
DAO
Number of proposals with votes in the top quartile for a given
DAO.
Snapshot
Num of Creators per
DAO
Number of unique members who initiate the sample proposals
in a given DAO.
Snapshot
Have Forum An indicator that equals one if the DAO has an open discussion
forum, and zero otherwise.
Snapshot
Duration Length of a proposal’s voting window (in days). Snapshot
Num of W ords T otal word count in a proposal’s title and body. Snapshot
Num of V oting StrategiesNumber of voting strategies adopted in a proposal. Snapshot
Delegation An indicator that equals one if a proposal employs delegation
strategy, and zero otherwise.
Snapshot
Quadratic V oting An indicator that equals one if a proposal employs quadratic
voting strategy, and zero otherwise.
Snapshot
Num of V oters Number of voters that cast votes on a proposal. Snapshot
Support Ratio of Win-
ning Option
Proportion of votes received by the winning option relative to
the total votes cast on a proposal.
Snapshot
Gini Gini coefficient of the voting power distribution among partic-
ipants within a proposal.
Snapshot
Top V oters% Ratio of total voting power held by voters in the top decile to
the total voting power cast on a proposal.
Snapshot
51

---

## Page 53

Table A1. Abnormal Trading around Proposal Discussion.
The table reports the estimates from OLS regressions of abnormal trading volume of DAOs’ native tokens for different groups
of investors. The sample consists of trading days from 60 days before the date a proposal was posted in the discussion forum
to 30 days after the voting end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The
dependent variable is Abvol, which is the ratio of daily trading volume to the average daily trading volume from 90 days to 60
days before the discussion date minus one.Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1]
window before the discussion date, and zero otherwise. V oting Periodis an indicator that takes the value of one for trading
days in the voting window, and zero otherwise. Day[+1,+30] is an indicator that takes the value of one for trading days in the
[+1,+30] window after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control
period. All the control variables are defined in Appendix A. Column (1) presents the estimates for all investors’ abnormal
trading volume. Column (2) presents the estimates for the abnormal trading volume of active investors involved in advancing
the proposal, including proposal managers listed in the administrator section on the DAO’s Snapshot page and individuals
who cast votes on the proposal. Column (3) presents the estimates for the abnormal trading volume of all other investors,
classified as passive investors. The regressions control for year-month fixed effects and DAO fixed effects. The standard errors
are clustered by DAO. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and
1% levels, respectively.
(1) (2) (3)
All Investors Active Investors Passive Investors
Variables of interest:
Day[–30,–1] 0.153** 0.493*** 0.175*
(0.046) (0.000) (0.067)
V oting Period 0.191** 0.783*** 0.213*
(0.036) (0.000) (0.058)
Day[+1,+30] 0.220** 0.470*** 0.257**
(0.031) (0.000) (0.048)
Controls:
Size –0.018 –0.033 –0.019
(0.536) (0.452) (0.561)
Return V olatility 0.019*** 0.012 0.020**
(0.007) (0.107) (0.011)
AbReturn 0.875*** 0.669** 0.999***
(0.000) (0.050) (0.000)
Y ear-Month FE Y es Y es Y es
DAO FE Y es Y es Y es
Adj. R2 0.103 0.031 0.100
Obs 259,360 251,748 259,185
52

---

## Page 54

Table A2. Abnormal Trading around Proposal Discussion by Investor Type.
The table reports the estimates from OLS regressions of abnormal trading volume of DAOs’ native tokens for different groups
of voters. The sample consists of trading days from 60 days before the date a proposal was posted in the discussion forum to 30
days after the voting end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent
variable is Abvol, which is the ratio of daily trading volume to the average daily trading volume from 90 days to 60 days before
the discussion date minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window
before the discussion date, and zero otherwise.V oting Periodis an indicator which takes the value of one for trading days in the
voting window, and zero otherwise. Day[+1,+30] is an indicator which takes the value of one for trading days in the [+1,+30]
window after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control period.
All the control variables are defined in Appendix A. Column (1) presents the estimates for the abnormal trading volume of
proposal managers. Column (2) presents the estimates for the abnormal trading volume of all voters who cast votes on the
proposal. Column (3) and (4) presents the estimates for the abnormal trading volume of voters whose voting powers are in
the top decile and bottom decile among all voters, respectively. The regressions control for year-month fixed effects and DAO
fixed effects. The standard errors are clustered by DAO. P-values are reported in parentheses. The symbols *, **, and *** denote
significance at the 10%, 5%, and 1% levels, respectively.
(1) (2) (3) (4)
Proposal Managers V oters T op V oters Bottom V oters
Variables of interest:
Day[–30,–1] 0.622* 0.539*** 0.582*** 0.170***
(0.084) (0.000) (0.000) (0.003)
V oting Period 0.742* 0.864*** 0.803*** 0.387***
(0.059) (0.000) (0.000) (0.000)
Day[+1,+30] 0.857 0.423*** 0.355*** –0.075
(0.158) (0.000) (0.002) (0.371)
Controls:
Size –0.582** –0.011 –0.078 –0.042
(0.021) (0.768) (0.163) (0.330)
Return V olatility 0.121*** 0.008 0.021*** 0.038***
(0.000) (0.241) (0.000) (0.000)
AbReturn 2.252** 0.517* 0.819*** 0.573*
(0.032) (0.089) (0.000) (0.079)
Y ear-Month FE Y es Y es Y es Y es
DAO FE Y es Y es Y es Y es
Adj. R2 0.040 0.031 0.028 0.025
Obs 140,269 240,381 201,735 113,138
53

---

## Page 55

Table A3. Abnormal Transactions around Proposal Creation.
The table reports the estimates from OLS regressions of abnormal number of transactions of DAOs’ native tokens for different
groups of investors. The sample consists of trading days from 60 days before the creation date of a proposal to 30 days after
the voting end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent variable
is Abtxn, which is the ratio of daily number of transactions to the average daily transactions from 90 days to 60 days before
the proposal creation minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window
before the proposal creation, and zero otherwise. V oting Periodis an indicator that takes the value of one for trading days in
the voting window, and zero otherwise.Day[+1,+30] is an indicator that takes the value of one for trading days in the [+1,+30]
window after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control period.
All the control variables are defined in Appendix A. Column (1) presents the estimates for all investors’ abnormal number of
transactions. Column (2) presents the estimates for the abnormal transactions of active investors involved in advancing the
proposal, including proposal managers listed in the administrator section on the DAO’s Snapshot page and individuals who
cast votes on the proposal. Column (3) presents the estimates for the abnormal transactions of all other investors, classified as
passive investors. The regressions control for year-month fixed effects and DAO fixed effects. The standard errors are clustered
by DAO. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels,
respectively.
(1) (2) (3)
All Investors Active Investors Passive Investors
Variables of interest:
Day[–30,–1] 0.133*** 0.242*** 0.150***
(0.000) (0.000) (0.000)
V oting Period 0.135** 0.286*** 0.152***
(0.010) (0.000) (0.007)
Day[+1,+30] 0.116** 0.006 0.136**
(0.023) (0.917) (0.014)
Controls:
Size –0.016 –0.017 –0.019
(0.560) (0.247) (0.554)
Return volatility 0.023*** 0.009** 0.026***
(0.000) (0.015) (0.001)
AbReturn 1.326*** 0.690*** 1.539***
(0.000) (0.000) (0.000)
Y ear-Month FE Y es Y es Y es
DAO FE Y es Y es Y es
Adj. R2 0.282 0.073 0.278
Obs 252,331 245,075 252,297
54

---

## Page 56

Table A4. Abnormal Transactions around Proposal Creation by Investor Type.
The table reports the estimates from OLS regressions of abnormal number of transactions of DAOs’ native tokens for different
groups of voters. The sample consists of trading days from 60 days before the creation date of a proposal to 30 days after the
voting end date of the proposal for all proposals with votes in the top quartile in a sample DAO. The dependent variable is
Abtxn, which is the ratio of daily number of transactions to the average daily transactions from 90 days to 60 days before the
proposal creation minus one. Day[-30,-1] is an indicator that takes the value of one for trading days in the [-30,-1] window
before the proposal creation, and zero otherwise. V oting Periodis an indicator which takes the value of one for trading days
in the voting window, and zero otherwise. Day[+1,+30] is an indicator which takes the value of one for trading days in the
[+1,+30] window after the voting end date, and zero otherwise. T rading days in the [-60,-31] window are used as the control
period. All the control variables are defined in Appendix A. Column (1) presents the estimates for the abnormal number of
transactions of proposal managers. Column (2) presents the estimates for the abnormal transactions of all voters who cast
votes on the proposal. Column (3) and (4) presents the estimates for the abnormal number of transactions of voters whose
voting powers are in the top decile and bottom decile among all voters, respectively. The regressions control for year-month
fixed effects and DAO fixed effects. The standard errors are clustered by DAO. P-values are reported in parentheses. The
symbols *, **, and *** denote significance at the 10%, 5%, and 1% levels, respectively.
(1) (2) (3) (4)
Proposal Managers V oters T op V oters Bottom V oters
Variables of interest:
Day[–30,–1] 0.185** 0.262*** 0.263*** 0.226***
(0.011) (0.000) (0.001) (0.000)
V oting Period 0.270*** 0.297*** 0.370*** 0.144*
(0.005) (0.000) (0.000) (0.062)
Day[+1,+30] 0.213** 0.001 0.092 –0.176***
(0.034) (0.989) (0.291) (0.003)
Controls:
Size –0.010 –0.013 –0.028* 0.005
(0.721) (0.389) (0.075) (0.841)
Return V olatility 0.048*** 0.008** 0.013*** 0.025***
(0.000) (0.020) (0.005) (0.000)
AbReturn 0.368* 0.694*** 0.630*** 0.540**
(0.065) (0.000) (0.000) (0.014)
Y ear-Month FE Y es Y es Y es Y es
DAO FE Y es Y es Y es Y es
Adj. R2 0.029 0.080 0.062 0.050
Obs 136,982 234,366 196,711 110,325
55

---

## Page 57

Table A5. Profitability of Insider Trades.
The table reports the estimates from OLS regressions of the profitability of insiders’ trades around DAO voting. The sample
consists of purchases and sales made by insiders in sample DAOs between 30 days before the proposal creation and 30 days after
the end of voting. The dependent variable isBHAR30, the 30-day market-adjusted abnormal buy-and-hold returns (multiplied
by -1 for sales) to insider trades. Day[-30,-1] is an indicator that takes the value of one if the insider trade occurs during the [-
30,-1] window before the proposal creation and zero otherwise. All the control variables are defined in Appendix A. Columns
(1) and (2) present the estimates for trades made by proposal managers. Columns (3) and (4) present the estimates for trades
made by top voters. The regressions control for investor-DAO-year-quarter fixed effects. The standard errors are clustered by
the proposal manager. P-values are reported in parentheses. The symbols *, **, and *** denote significance at the 10%, 5%, and
1% levels, respectively.
Proposal Managers T op V oters
(1) (2) (3) (4)
Variable of interest:
Day[–30,–1] 0.120** 0.146*** –0.031 0.007
(0.045) (0.000) (0.108) (0.274)
Controls:
Size –0.043*** 0.035***
(0.000) (0.001)
Return V olatility –0.021 –0.000
(0.233) (0.933)
AbReturn –0.457*** 0.164
(0.000) (0.176)
T rade Size 0.006 0.015*
(0.889) (0.096)
Investor × DAO
× Y earQuarter FE Y es Y es Y es Y es
Adj. R2 0.241 0.426 0.086 0.200
Obs. 79,126 73,482 283,519 253,021
56

---

## Page 58

Table A6. Effect of Negative Shocks on DAOs’ TVL.
The table reports the estimates from a Difference-in-Difference (DID) model in which the dependent variable is DAOs’ daily
TVL. The sample consists of days in the [-60, 60] window around two negative market shocks – Luna crash and FTX collapse
– for all the DAOs with TVL data on Defillama. DAOs are divided into quartiles based on their average abnormal number of
transactions one month before proposal creation dates.Treatment is an indicator that equals one if a DAO is above the sample
median and zero if a DAO is below the sample median.Post is an indicator that equals one after the Luna crash on 9 May 2022
in column (1), or after the FTX collapse on 8 Nov 2022 in column (2), and zero otherwise. All the control variables are defined
in Appendix A. The regressions control for industry-fixed effects. P-values are reported in parentheses. The symbols *, **, and
*** denote significance at the 10%, 5%, and 1% levels, respectively.
(1) (2)
Luna FTX
Variables of interest:
T reatment× Post –0.156* –0.232**
(0.067) (0.037)
T reatment 0.216*** 0.606***
(0.001) (0.000)
Post –0.724*** –0.021
(0.000) (0.777)
Controls:
Num of Chains 0.235*** 0.169***
(0.000) (0.000)
Size 0.169*** 0.100***
(0.000) (0.000)
Return –0.434 –0.306
(0.102) (0.484)
Industry FE Y es Y es
Adj. R2 0.489 0.217
Obs. 8,984 11,088
57

---
