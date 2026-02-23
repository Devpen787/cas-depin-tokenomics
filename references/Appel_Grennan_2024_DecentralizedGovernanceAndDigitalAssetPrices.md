# Appel_Grennan_2024_DecentralizedGovernanceAndDigitalAssetPrices.pdf

## Page 1

Decentralized Governance and Digital Asset Prices *
IAN APPEL
University of Virginia
JILLIAN GRENNAN
Emory University
ABSTRACT
For digital assets, is traditional corporate governance still ideal? We explore the governance
of hundreds of prominent Decentralized Autonomous Organizations (DAOs), classifying 28
distinct characteristics related to aspects of governance such as token holder’s privileges
to bring improvement proposals, the voting process, consensus mechanisms, and security
features. Our findings reveal that governance practices fostering inclusive participation or
heightened security are linked with positive abnormal returns, while barriers to proposal
adoption correspond to negative returns. This outperformance is also evident in non-financial
metrics like higher DEX volume and lack of security breaches. Evidence from a regression
discontinuity design using close-call votes on proposals suggests these novel governance fea-
tures, distinctive to DAOs, significantly change value. Overall, our research suggests that
governance responds to the production process. For digital assets, the process differs enough
that solely concentrating on traditional corporate concerns, such as reducing agency costs,
is inadequate.
JEL classification: G32, G24, G28
Keywords: DAOs, cryptocurrency, blockchain, tokens, digital assets, decentralization, digital
governance, Web3, FinTech, decentralized finance, DeFi, protocols, voting rights, cybersecurity,
compliance, board of directors, delegates, cooperatives
* Authors: Appel, University of Virginia (e-mail: appeli@darden.virginia.edu), Grennan, Emory University (e-mail: jil-
lian.grennan@emory.edu). We thank Vivianna Fang He (discussant), Jonathan Karpoff, Frank Partnoy, Jason Sandvik (dis-
cussant), Donghwa Shin (discussant), Keer Yang (discussant), David Yermack (discussant), and seminar participants at UC-
Berkeley, UC-Santa Barbara, University of Mannheim, U.S. Treasury Office of Financial Research, the American Economic
Association, SFS Calvalcade Conference, the American Law and Economics Association, the Conference on Empirical Legal
Studies (U. Chicago), GSU-RFS FinTech Conference, Society for Institutional and Organizational Economics Conference, the
University Blockchain Research Initiative Conference, Drexel University’s Corporate Governance Conference, SCU Crypto Con-
ference, Owners as Strategist Conference (U. Bocconi), Science of Blockchain Conference DAO Workshop (Cornell Tech), Swiss
National Bank Conference on Cryptoassets and Financial Innovation, RnDAO, and the International Corporate Governance
Forum for helpful comments on an earlier draft of this study. We gratefully acknowledge financial support from Ripple’s Uni-
versity Blockchain Research Initiative. We thank Erkin Asci, Nick Dahlborg, Allison Hart, George Iyalomhe, Oliver Lee, Rayan
Malik, Dominic Parante, Brendan Phillips, Ryan Schmitzer, and Gabriel Silva for helping to collect DAO proposal data.

---

## Page 2

A prominent theory of the firm views it as a nexus of explicit and implicit contracts between
owners, managers, and other stakeholders (Coase, 1937; Jensen and Meckling, 1976). Agency con-
flicts emerge, in part, because contracts are incomplete and costly to enforce. Recently, blockchain
technology has facilitated the creation of “smart contracts” that may mitigate these frictions. Smart
contracts are programs that run on a blockchain (e.g., Ethereum) that automatically execute trans-
actions or operations when pre-determined conditions are satisfied. Not only do smart contracts
potentially expand the contracting space of organizations, but their self-executing nature renders
the issue of enforcement moot.
An important byproduct of the advent of smart contracts is the emergence of a new orga-
nizational form: the Decentralized Autonomous Organization (DAO). DAOs are internet-based
communities that raise funds via the sale of tokens. In contrast to corporations and other types
of business organizations, they typically do not have managers or a board of directors. Rather,
decision-making authority rests solely with the token holders, who submit and vote on proposals
that dictate the DAO’s operations. The governance structures of a DAO are defined by a smart
contract that encodes features of the proposal and voting processes (e.g., support needed for a pro-
posal to be implemented). Smart contracts can automatically implement proposals, thus negating,
at least in part, the need for centralized management.
DAOs can have virtually any objective. Commonly, they are used to govern decentralized
finance (DeFi) protocols that seek to provide traditional financial services without centralized
intermediaries (Harvey et al., 2021; Makarov and Schoar, 2022). MakerDAO, which governs the
protocol for the Dai stablecoin, provides an instructive example. Dai is a cryptocurrency that seeks
to maintain a $ 1 value. Users make an overcollateralized loan of an approved cryptocurrency to
borrow Dai and agree to an interest rate. If the value of the collateral falls below the loan amount,
the loan is automatically liquidated via a smart contract. MakerDAO controls Dai’s protocol. For
example, the DAO decides which assets to lend against and sets corresponding collateralization
rates. The governance token associated with MakerDAO, MKR, is traded on secondary markets
such as Coinbase. Interest charged on DAI loans are, in part, used for repurchases. As of April
2024, MKR’s market capitalization reached approximately $ 3.8 billion, nearing its all-time high of
1

---

## Page 3

over $ 5 billion in November 2021.
The growth of DAOs in recent years has been rapid. The first DAO, an investment collective
called “The DAO,” was created in 2016. As of the middle of 2022, there are over four thousand
(Cointelegraph, 2022). Despite this growth, relatively little is known about the governance of
DAOs. We aim to fill this gap in the literature. Specifically, we have three primary goals. First, we
shed light on the economic activities of a sample of prominent DAOs by classifying their primary
functions. Second, we highlight common governance mechanisms used by our sample of DAOs,
specifically focusing on voting mechanisms/processes, organizational design, and security features.
Third, we analyze the value implications of DAOs’ governance structures, particularly focusing on
features that promote or impede broad involvement in the proposal and voting process.
We collect data on the activities and governance structures of 200 prominent DAOs using both
commercial databases and hand-collecting information from public sources (e.g., white papers).
We classify each DAO into one of three broad categories (DeFi, Web3, and Infrastructure) and
further refine their activities into 21 specific functionalities. We classify the governance structures
for each DAO, focusing on 28 dimensions related to voting mechanisms/processes, organizational
design, security features, and governance models. Finally, we assemble a comprehensive database
of 17,485 proposals voted on between 2020Q1 and 2024Q2 with corresponding token prices. We
analyze abnormal token returns, adjusted for three crypto factors (Liu et al., 2022), associated with
these proposals to study the relationship between decentralized governance and digital asset prices.
First, we describe the economic activities of DAOs in our sample. In other words, what do
DAOs do? Consistent with anecdotal evidence, the majority (60%) of DAOs in our sample pri-
marily engage in DeFi. Common functionalities for DeFi DAOs include staking cryptocurrencies,
borrowing/lending, decentralized exchanges, and stablecoins. Web3 DAOs, which create decen-
tralized internet services and platforms, constitute 32% of the sample. The specific activities
undertaken by these DAOs relate to virtual reality, talent/gig work, public goods, and asset man-
agement/crowdfunding. Finally, infrastructure DAOs, which primarily build tools for the crypto
ecosystem (e.g., bridges to facilitate communication and asset transfers between blockchains) con-
stitute 7% of our sample.
2

---

## Page 4

Next, we characterize the DAOs’ governance structures. We focus on four dimensions: voting
mechanisms, voting processes, organizational design features, and security. For voting mechanisms,
the bulk (70%) of DAOs in our sample use relative quorum voting, under which a proposal passes if
a majority of voters approve it. The main alternative to a quorum system is weighted voting (19%
of DAOs), in which votes have more/less influence based on a metric (e.g., time tokens have been
owned). DAOs also use mechanisms that functionally encourage or discourage wide participation
in the voting/proposal process. Examples of mechanisms that discourage participation include
requirements (e.g., minimum token ownership) to create a formal proposal (63%) or to submit
executable code along with a proposal (8%). Factors encouraging participation include holding votes
“off-chain” so participants do not need to pay transaction (“gas”) fees associated with “on-chain”
votes. Organizational design features also potentially play an important role in the governance of
DAOs. Some DAOs adopt corporate-like governance mechanisms, including the appointment of
representatives/councils and the use of vesting schedules for key members. Over a quarter of DAOs
in our sample delegate responsibility via the formation of subDAOs.
Security plays a unique role in the governance of DAOs. In contrast to shareholders of a
corporation, token holders do not owe a fiduciary duty to each other, thus subjecting DAOs to
“governance attacks” in which majority token holders expropriate the minority. A common attack
involves using short-term “flash” loans to obtain control of a DAO, allowing an attacker to imple-
ment any proposal, including transferring a DAO’s treasury assets. 1 DAOs implement governance
mechanisms to mitigate the risk of such an attack. For example, 44% of DAOs in our sample require
a “multi-sig” (i.e., signatures from multiple authorized parties) for proposals to be implemented.
Other common mechanisms include allowing the core or developer team to override proposals or
requiring a delay before implementation.
Then, we characterize the returns associated with improvement proposals in DAOs. We ex-
1For example, Beanstalk, a DeFi protocol, was subject to a governance attack in April of 2022. The
attacker obtained a flash loan for approximately $ 1 billion, allowing it to bypass a supermajority voting
requirement to make instant changes to the protocol via an improvement proposal. The attacker then created
and approved a proposal to transmit funds from the protocol to itself. For additional details, see https:
//medium.com/coinmonks/beanstalk-exploit-a-simplified-post-mortem-analysis-92e6cdb17ace .
3

---

## Page 5

amine returns during two critical periods: from the initial public discussion of the idea, typically
occurring in DAO forums or group chat platforms until voting opens, and from the opening of
voting to its conclusion. While returns across these periods exhibit a positive correlation, the rela-
tionship is weak (0.08) and varies with the winning percentage, suggesting persistent uncertainty
until voting concludes. Further, we find substantial heterogeneity in returns which are correlated
with proposal characteristics, content, and broader market conditions. Any proposal outcome cor-
responds to a 1.1 to 3.6 percentage point higher abnormal return during crypto market upcycles.
Notably, contributor-initiated proposals yield higher returns compared to those from core team
members, indicating the potential benefits of inclusive governance structures. Our findings reveal
that forum discussion sentiment impacts voter turnout but not returns, while proposal importance
and treasury-funded expenses negatively correlate with returns. The complexity of proposals, mea-
sured through various metrics, is linked to voter turnout, though its relationship with returns is
inconsistent. Content analysis demonstrates that proposals focused on viability or marketing ex-
hibit lower returns, whereas those related to tokenomics tend to generate higher returns. These
descriptive results showcase that DAO proposals are meaningful and have implications for digital
asset prices.
Having provided an overview of DAOs, their governance features, and proposal returns, we turn
to evaluating the relation between decentralized governance and digital asset prices. We consider
three fundamental aspects of DAO governance: broad participation in decision-making (inclusive
governance features), barriers to adopting improvement proposals (restrictive governance features),
and provisions that mitigate malicious behavior (security governance features). We classify the
dimensions of governance discussed above into these three categories. For example, inclusive gov-
ernance features include provisions such as permitting off-chain voting and providing voting in-
centives. Restrictive governance features include quorum and supermajority voting requirements.
Security features include requiring feasibility studies for proposals or multisig before implementa-
tion. Our analysis indicates that inclusive and security governance features are positively associated
with abnormal returns around adopting improvement proposals, which is consistent with the idea
that they improve DAO decision-making. However, provisions that impede the improvement pro-
4

---

## Page 6

posal process are associated with lower abnormal returns.
We also rule out alternative stories through additional tests. For instance, there is the possibility
that digital asset returns may be inefficient because of whales manipulating prices, segmented
markets, or irrational exuberance leading to deviations from underlying fundamentals (Griffin and
Shams, 2020). Therefore, we extend our analysis to examine the relation between governance
features and real effects. First, we focus on the DeFi DAOs as their business model is more readily
understandable in that having greater trading volume is associated with higher profitability and
performance. Our decentralized governance index is positively related to DEX trading volume.
Next, we focus on the two subcomponents unique to decentralized governance – security features
and inclusivity provisions. Having more secure governance features negatively correlates with DAO-
specific crypto news about scams or hacks. We also find that having more inclusive governance
features is positively associated with user growth, which we proxy for with social media followers.
Finally, while our index results are primarily descriptive correlations, we also pursue a regression
discontinuity design (RDD) approach for identification that exploits the discontinuous probability
of enhancing DAO governance as a function of close-call votes on DAO improvement proposals.
This approach follows the popular econometric approach in nonexperimental settings of examining
discontinuous changes at known cutoffs (Lee and Lemieux, 2010; Cunat et al., 2012). As long
as there is some arbitrariness in the cutoff (e.g., vote passes with 50.1% or fails with 49.9% of
the vote), DAOs just below the cutoff are good comparisons to those just above the cutoff or “as
close as random.” While RDD is known to have high internal validity due to the relatively mild
assumptions required for identification (i.e., continuity near the threshold), the inferences made on
those estimates may not generalize due to low coverage within the optimal bandwidth. Indeed, the
sample of close-call proposals that we have is only 5% of the full sample of proposals. Nevertheless,
with this small sample, we still find that stronger decentralized governance is associated with
positive crypto-adjusted returns for the digital assets in the week and month after the passing
vote. This suggests that expected improvements in DAO governance through the approval of an
improvement proposal are associated with positive abnormal returns of 3.1% and are consistent
with the broader correlations we document.
5

---

## Page 7

By combining a large set of decentralized governance provisions into an index that proxies for
traditional aspects of governance (strength of tokenholders rights through restrictive governance
features) as well as novel aspects of digital governance (empowering tokenholder wisdom through
inclusive governance features and eliminating hacking vulnerability through security features), and
then studying the empirical relationship between this index and digital asset performance, we
demonstrate that both traditional and novel aspects of digital governance matter for returns. Our
analyses do not use random assignment, so we cannot make claims about causality. However, we
explore the implications in various contexts and assess the supportive evidence for our hypotheses
about decentralized governance. For example, we show that our results are robust to looking at
unadjusted returns, suggesting it is not something about our adjustment process. We also show
that the patterns hold when looking at weekly and monthly returns, suggesting that it is not some
private information being revealed solely through the voting process.
Our paper joins the growing literature on the economics of decentralization, which advances in
blockchain and AI catalyzed. Yermack (2017) explores the implications of the transparency afforded
by smart contracts (and blockchains, more generally) on various dimensions of firm behavior. Many
of the DAOs we study provide DeFi services, a prominent use of smart contracts (Harvey et al.,
2021; Makarov and Schoar, 2022; John et al., 2023). A growing theoretical literature models how
commitment enabled by smart contracts can mitigate underinvestment (Cong et al., 2022), limit
conflicts between platforms and users (Sockin and Xiong, 2022), and alter incentives to compete
(Cong and He, 2019; Goldstein et al., 2022). A related strand of literature studies the use of
digital tokens to finance entrepreneurial ventures via initial coin offerings (ICOs) (e.g., Howell
et al., 2020; Li and Mann, 2021). Papers also study specific protocols that DAOs control, such
as decentralized exchanges (DEXs) (Augustin et al., 2022; Lehar and Parlour, 2023). Thus, by
studying the governance framework and processes that direct and control these novel FinTech
applications, we provide insights into how to balance stakeholder interests best to promote both
traditional goals of for-profit organizations, like long-term value creation, and novel goals of DAOs,
like the sustainability of the protocol.
The application of smart contracts to DAOs is being explored in a series of contemporaneous
6

---

## Page 8

papers. Appel and Grennan (2023) and Laturnus (2023) study the concentration of voting on DAO
proposals, while Han et al. (2023) focus on conflicts of interest between major investors (“whales”)
and retail participants. Retail investors beliefs when investing in digital assets differ from institu-
tions (Kogan et al., 2023; Oh et al., 2022; White and Wilkoff, 2023). The focus on ownership of
digital assets heralds back to prominent theories of ownership in organizational economics (Hans-
mann, 2000; Baker et al., 2002) and the role of commons. The theoretical literature, thus far, has
focused more on the platform nature of decentralized organizations. For instance, Bena and Zhang
(2023) model the optimal design of decentralized governance when the platform leverages user data
as input. Mei and Sockin (2023) explore the extent to which speculation in native tokens on DAOs
prohibit the adoption of the platform’s services because the because the risk-adjusted benefit of
adoption is lower than that from speculation. More recently, Atta-Darkua (2023) focuses on cash
management at DAOs.
Our research also complements recent work that offers DAO design insights based on engineering
principles (Hassan and Filippi, 2021; Kiayias and Lazos, 2022; Sharma et al., 2023; Tan et al., 2023;
Austgen et al., 2023). Specifically, our work builds on and extends the insights from Wang et al.
(2022), one of the first papers in engineering that analyzed many DAO proposals by webscraping
Snapshot, a popular off-chain voting platform, and identified challenges in DAOs. A key challenge
was voter apathy in horizontal vs. vertical organizations, and the authors called for more robust,
inclusive, and accessible governance mechanisms to encourage broader participation and ensure a
sustainable future for DAOs. By evaluating inclusive governance features and showing that they
add token value, our work helps extend our understanding of the best practices for DAOs.
Finally, we contribute to the literature on crowd wisdom and the voice of investors (Admati
and Pfleiderer, 2009; Broccardo et al., 2022). Financial economists are interested in the extent to
which technology can empower crowd wisdom and generate more efficient outcomes for shareholders
(Dugast and Foucault, 2018; Cookson and Niessner, 2019; Da and Huang, 2020; Grennan and
Michaely, 2020). While the evidence in the corporate context suggests that crowd wisdom improves
market efficiency, the verdict is still out about crowd wisdom in the shareholder proposal context.
In July 2022, the U.S. Securities and Exchange Commission (SEC) proposed amending Rule 14a-8,
7

---

## Page 9

which governs shareholders right to make proposals to the management team for consideration, to
allow more shareholder ideas to be considered. To the extent that a setting like the DAO setting
resembles the expanded shareholder proposals, our evidence, which shows more inclusive governance
processes are associated with positive returns in digital asset markets, points to the power of crowd
wisdom (Grennan and Michaely, 2022; Dessaint et al., 2022).
Importantly, we expand the rich literature examining corporate governance, voting rights, and
equity returns (Zingales, 1995; Gompers et al., 2003; Bebchuk et al., 2009; Cunat et al., 2012; Kalay
et al., 2014). By showing a correlation between our decentralized governance index and digital asset
returns, we further establish that democracy matters beyond equity markets and that digital asset
markets are not orthogonal to equity markets. This comparison between decentralized frameworks
and their centralized counterparts builds on important work doing exactly this, focusing on the
role of exchanges, broker-dealers, and even fiat currencies (e.g., Gorton and Zhang (2023)). By
showing though that there are novel governance features, like inclusivity and security, that matter
for DAOs, we find results consistent with an earlier literature exploring co-ops and alternative
governance structures that found governance processes adapt to production processes (Karpoff and
Rice, 1989; Hart, 1996).
Finally, a key contribution of our study is to make the DAO governance data publicly available,
so that other scholars can build for DAOs what is missing in the corporate governance literature.
As Frankenreiter et al. (2021) demonstrate, corporate governance data availability matters and
unfortunately, most corporate governance data is behind a paywall and difficult to collect, organize,
and analyze because of jurisdiction-level differences (e.g., Delaware makes it very expensive to get
corporate charters) which has led to significant error rates, often exceeding eighty percent, even
in the G-Index. We hope that researchers use this rich setting to better understand fundamental
questions like the need for active involvement in organizations such as through the extensive and
costly monitoring (Appel et al., 2016; Lewellen and Lewellen, 2021).
8

---

## Page 10

1 Institutional Background
1.1 What is a DAO?
DAOs are collectively-owned, internet-based organizations that are governed by token holders.
The creation of this organizational form is credited to Dan Larimer who, in 2013, coined the term
decentralized autonomous corporation (DAC). The following year, Vitalik Buterin, the inventor of
Ethereum, expanded on this idea. In Ethereum’s white paper, Buterin argued that the idea of
a DAC could be applied to a broader set of (non-capitalist) organizations, and he discussed the
implementation of such structures on the Ethereum blockchain.2 The first DAO, a collective venture
capital fund called “The DAO,” was formed in 2016. While The DAO failed following a hack of
its treasury, resulting in a “fork” (i.e., invalidation of transactions) of the Ethereum blockchain, its
basic structure has been employed by subsequent organizations (Huberman et al., 2019).
The defining feature of DAOs is the lack of centralized leadership (e.g., a CEO). Instead,
decision-making authority lies with the token holders of the DAO via a voting system. The decen-
tralization of decision making is made possible by a smart contract, which formalize the rules of
the DAO and automates on-chain transactions (e.g., making payments) when a proposal passes.
Decentralization is further promoted by the use of a public blockchain (e.g., Ethereum) to deploy
smart contracts, so a DAO’s treasury and transactions are transparent and difficult to censor by
third parties. Proponents of DAOs argue that decentralization confers important benefits, including
improved decisionmaking, censorship resistance, and fairness. 3
There is considerable uncertainty regarding the legal status of DAOs. Commentators often
argue that, by default, DAOs are general partnerships. As such, the members of the DAO may be
subject to joint and several liability for any claims against the DAO. 4. However, some jurisdictions
have formalized the legal status of DAOs. For example, Wyoming and Tennessee are the only states
2See https://ethereum.org/669c9e2e2027310b6b3cdce6e1c52962/Ethereum_Whitepaper_-_
Buterin_2014.pdf
3See Vitalik Buterin, “DAOs are not corporations: where decentralization in autonomous organizations
matters” available at https://vitalik.ca/general/2022/09/20/daos.html.
4See, for example, “DAOs: A game changer in need of new rules” available at https://www.reuters.
com/legal/legalindustry/daos-game-changer-need-new-rules-2022-10-07/
9

---

## Page 11

that explicitly recognize DAOs as legal entities, allowing them to register as LLCs. See Appendix
A for additional discussion of the legal status of DAOs.
There is significant heterogeneity in the purpose of DAOs. A prominent class of DAOs control
open source protocols. Such DAOs are often associated with DeFi protocols that provide traditional
financial services in a disintermediated manner. For example, Uniswap is a decentralized exchange
(DEX) that allows users to trade digital assets. Uniswap is open source, but changes to the protocol
are determined by UNI token holders. However, many DAOs are not protocols and instead serve a
community function. Examples include investment DAOs (e.g., Pleasr DAO, Constitution DAO),
social groups and members’ clubs DAOs (e.g., Friends With Benefits, ApeCoin), public goods DAOs
(e.g., BitDAO, Gitcoin), advocacy-oriented DAOs (e.g., Bankless, Lobby3).
While DAOs have a wide range of purposes, they share a number of common features. Given
their goal of decentralization, DAOs act through collective action that is primarily implemented by
code rather than through intermediaries and other formal systems. DAO voting can occur on chain
or off chain. With on-chain voting, individual votes are submitted as transactions and recorded
directly on the blockchain. Submitting votes on chain requires users to pay gas fees for each vote,
but the outcome of the vote can be automatically implemented via smart contracts. In contrast,
with off-chain voting, individual votes are not submitted as blockchain transactions and no gas fees
are necessary. Instead, users are typically prompted to sign messages with their cypto wallets to
vote, and the resulting data is stored via an oracle or some type of decentralized file storage system.
Given that DAOs are a new organizational form, there has been significant experimentation
with aspects of their governance. In the next section, we provide a case study of Compound in
order to motivate our discussion of governance.
1.2 Case Study: Compound
Compound is a lending platform built on the Ethereum blockchain that enables users to per-
missionlessly borrow or lend from a pool of pre-selected digital assets. Intermediaries do not set
the interest rates after a detailed review process involving loan officers; instead, interest rates are
10

---

## Page 12

determined algorithmically based on the proportion of assets lent out. In this sense, Compound is
a typical DeFi application and its purpose is as a “protocol” rather than as a social community.
Compound launched on Ethereum in September 2018 via a tokenless protocol. While the
protocol is non-custodial, initially, developers retained some centralized, administrative privileges.
For the developers to remove themselves from this centralized position, and thereby, fulfill their
purpose of creating a sustainable, decentralized protocol, the developers introduced a token called
COMP meant to govern the protocol. Between April and June 2020, the administrators of the
Compound protocol replaced themselves with a community governance system, which meant that
all changes or proposals had to come from community members. Specifically, the administrators
demonstrate the proposal system to implement improvements when they held all of the tokens, and
then they distributed tokens to all users of the platform.
Through the COMP token, the community of COMP users or those who bought the governance
token on token platforms like Coinbase, are the ones responsible for making changes to the protocol
by proposing improvements and voting on their adoption. Given the importance of U.S. securities
law considerations, the documentation for the COMP token states there is no expectation of profit
from COMP, which gives it a stronger case for passing the Howey Test used to determine if an asset
is a security.5 While there is no expectation of profit in the short run, there is a contingent of token
holders who believe that they could propose, approve, and implement a mechanism to capture and
claim some of the cash flows of the protocol in the future.
COMP tokenholders’ belief that they could claim some of value from lending process and
distribute that value to COMP holders is very similar to what traditional equity investors are doing
when they invest in a non-dividend paying firms yet expect to receive payout at some future date.
The key difference is that COMP holders can vote to receive payout. In contrast, for corporations,
the board of directors, who have fiduciary duties to the shareholders who elect them, decide on
whether and when cash distribution to shareholders occurs (i.e., dividends or repurchases).
While there are not examples of token holders electing to pay themselves dividends yet, there
5For a more detailed description of the legal risks and regulation surrounding cryptocurrencies, see Gren-
nan (2022).
11

---

## Page 13

are example governance attacks that have done something very similar. For example, a hacker
slowly bought enough stake (33%) to control True Seigniorage Dollar’s DAO voting process, and
then, the hacker proposed a new implementation in the code and using his own stake, passed the
changes and when implementing it, and inserted a malicious code to mint himself coins that wiped
out the value of the treasury. Because the possibility of bad actors is always present, protocols
strive to develop and implement protections against such security risks. Two common approaches,
which we detail below, are the requirement of multiple signatures and inability to access certain
functions like minting.
In general, for a protocol like Compound, the majority of the proposals involve some type of
business judgment. To date, the COMP community has introduced more than 100 proposals. Most
proposals are technical and involve some type of process innovation (i.e., change a risk parameter
changes, adjust the rewards, allow for different digital assets). Some proposals are business-oriented
(e.g., hire an auditor, make changes to the developer team, develop a partnership) and some are
about the soundness of the decentralization process (e.g., multisig considerations, voting thresh-
olds).
Given that most of the proposals involve some type of business judgment, a key design decision
then involves the threshold of voter participation required or the ability of voters to delegate their
shares to experts. As of writing, Compound is governed entirely on-chain by COMP holders where
one token equals one vote. COMP token holders can vote directly or delegate their voting rights
to another party they deem more capable of making decisions. All governance activity occurs
through Governor Alpha, which Compound developed itself, and then upgraded to Governor Bravo
to include additional meta data features such as voter history. Governance Alpha and Governor
Bravo are open-source, and as such, several other DAOs have adopted it.
At its core, the Governor system is code that has six main functions: proposal initiation, vote
casting, vote delegation, proposal canceling, proposal queuing, and proposal execution. Any smart
contract with a token balance can vote, and they do so in proportion to their token balance. In the
case of COMP, the threshold is set such that anyone with 1% of tokens held or delegated to them
is eligible to submit a proposal. The proposal must include executable code that can be directly
12

---

## Page 14

incorporated into the protocol after passing. Once the proposal is submitted, there is a voting
period. In the case of COMP token holders, the voting period is 3 days and either COMP holders
or their delegates can cast their votes. There is a minimum threshold for the number of votes cast,
and a passing threshold. For COMP, at least 400,000 votes must be cast and 50% is the passing
threshold. The votes are made on-chain, so that the governance smart contract can total up the
votes and determine what proposals pass. On-chain voting cost gas. Once passed, the proposed
code becomes part of the queue to be executed after a delay period. The COMP delay period is
two days and serves as an additional security measure.
1.3 DAO Governance
Modifiable voting parameters is a key feature of DAO governance. In fact, many of the other
DAOs adopting Compound’s Governor Alpha and Bravo systems tweak the modifiable voting pa-
rameters. For example, Uniswap follows the Compound Governor system, but they have a week
long voting period and a lower threshold for bringing forward a proposal. This flexibility in voting
features is consistent with design choices in business law whereby some corporations have strong
governance practices and some weaker governance practices. For example, supermajority vote
thresholds are considered weak governance (Gompers et al., 2003), and DAOs may select this fea-
ture as a default. Similarly, the rule that one must own a certain number of shares or tokens to
make a proposal is also consistent with corporate law, in which a shareholder must own a certain
amount of shares and have held them for a certain amount of time before being able to bring
forward a shareholder proposal.
The main drawback of the Compound voting mechanism is that it is costly. The gas fees
associated with voting on-chain do not incentivize voter participation. A few alternatives are
available to avoid the costly gas fees associated with exercising the right to vote. First, vote
signaling that occurs off-chain is common. Typically, discussions of improvement proposals occur
among community members or users of the DAO protocol on a forum or Discord chat. Then,
interested users vote on a preliminary proposal off-chain. For example, a preliminary vote may
13

---

## Page 15

occur on Snapshot, which is an off-chain, open-source, gasless multi-governance client with easy
to verify and hard to contest results. Snapshot also allows for flexible voting strategies (vote with
tokens or NFTs) and systems (approval votes, quadratic voting, ranked choices, etc.).
Depending on the DAO’s specific rules, there are a few options available when the preliminary
proposal passes. First, administrators with mutlisig power can implement the proposal on-chain
through a vote, and only the admins need to pay the gas fee. 6 Obviously, this is not as decentral-
ized as the admins could presumably choose not to implement a proposal that received approval.
Second, only a few community members vote on-chain for a formal proposal that is the same as
the preliminary proposal, thereby avoiding all the fees. Third, some DAOs require the person sub-
mitting the proposal to have reserve funds available to refund the gas fees. Fourth, some oracles
exist that could be used to execute proposals associated with off-chain votes on-chain.
From a voter participation perspective, the gas fee challenges are even more problematic, be-
cause most theories of voting acknowledge most voters are not the marginal voter, and thereby have
no incentives to vote. In the corporate setting, regulators recognized the challenges associated with
shareholder passivity, and through a series of reforms in beginning in the late 1980s, regulators set
out to ensure that institutional investors like private pension plans diligently exercised their proxy
voting duties as part of their fiduciary duties to their clients (Grennan and Michaely, 2019). In
practice, this means that fiduciary responsibilities lead to high voter turnout and active governance
even for passive investors (Appel et al., 2016). To meet their fiduciary duties, many asset managers
began contracting out to third-party advisers like GlassLewis and ISS to get recommendations
on how to vote. Presumably, especially for some complex DAOs, where users may not have the
expertise to vote on a given topic, they could delegate their vote to someone who did have the
authority.
In equity markets, collective action challenges are overcome by fiduciary duties that require
institutional investors to actively vote shares on behalf of their clients. In contrast, DAOs face old
6Multisig refers to systems that require multiple signatures to execute. For security reasons, developers
distribute multiple administrative keys. This mitigates risk, because any hacker trying to access the digital
assets of the DAO are going to need several keys to do so. Similarly, no single bad actor in a community or
a DAO is going to be able to withdraw funds without the consent or administrative access of others.
14

---

## Page 16

governance challenges such as voter participation and new governance challenges that are intricately
linked to the technology such as scale and resilience. For example, anecdotes suggest that voter
engagement is typically low, so one-token-one-vote systems tend toward plutocracies, in which the
whole is governed by those with the most voting rights, often the wealthiest.
Vote delegation lets token holders transfer their voting power to another user, without giving
up control of the underlying asset. Vote delegation can be withdrawn at any time, which helps
ensure that protocol advocates remain aligned with their supporters. Vote delegation lowers the
cost of participating in governance. By delegating to another user, token holders can avoid the time
involved in reviewing each individual proposal as well as the transaction fee required to submit their
vote on chain. Delegation also allows smaller token holders to aggregate their stakes to gain a bigger
voice in governance discussions. As an example, many protocols have minimum vote requirements
to submit and pass proposals; vote delegation gives ordinary users the opportunity to meet these
thresholds despite limited personal resources.
2 Data
2.1 DAO characteristics
Our sample of DAOs includes all DAOs for which we could obtain both the text of the individual
improvement proposals and the individual voting choices. In total, this gives us data on 150 DAOs
and spans voting actions from 2020Q1 through 2022Q3. To better understand what the purpose
and origin of each DAO is, we read each DAO’s documents (i.e., white papers and FAQs) and any
related writing such as Medium or Notion posts. We classify the DAOs into three mutually exclusive
categories, which include DeFi, infrastructure, and Web3, based on their primary operational area.
We recognize that young organizations often pivot as they learn what market niches they can fulfill.
For this reason, we also create non-mutually exclusive subcategories for each DAO that recognizes
the various functionalities that they encompass. The full list of DAOs, a Web2 site, and digital
asset ticker are available in Appendix C.
15

---

## Page 17

2.2 DAO governance and voting
Unlike corporations, which have their corporate charter and bylaws and a uniform process
through which shareholders can submit proposals for a potential vote at the annual shareholder
meeting, there is no uniformity in the governance structure and voting process for DAOs. Thereby,
we spend meaningful time going through each DAO’s documents (i.e., white paper and FAQs)
to understand and classify the governance structure and voting process. For example, we create
variables characterizing the voting mechanism, the voting process, specific organizational design
features, and security features that the DAOs put in place. Appendix B defines the dimensions of
governance that we use in this study.
2.3 DAO improvement proposals
We gather over 10,141 improvement proposals from across four sources – Boardroom, Tally,
Snapshot, and Messari. In Figure 1, we provide an example improvement proposal and voting
outcomes from 1Inch, a decentralized exchange (DEX), that was started by the community member
“Radar” on the 1inch Forum on July 21, 2021. It subsequently went to an off-chain vote on August
8, 2021. The proposal’s aim was to implement a robust deflationary mechanism to 1INCH token
that removes single-asset-staking and farming completely. We examine abnormal returns around
proposal votes to measure DAO performance.
We also introduce a novel classification for the improvement proposals to estimate the scope
of decisions being made. We access and examine each DAO’s Forum, Discord, and voting page to
understand the content of the proposal. In Figure 2, we showcase the wide range of issues requiring
votes. For example, governance issues such as how treasury funds should be spent to evaluating
the quality of code-upgrade proposals, to soliciting user feedback on service experience, aggregating
product quality ratings, combating fake news, and many others. The five main categories of DAO
improvement proposals include finance, governance, management, tokenomics, and viability. Below
each main category are subcategories representative of different kinds of proposals.
16

---

## Page 18

2.4 Digital asset prices
We gather information on governance token prices as well as prices for the crypto market
more generally. To do so, we compile data on individual digital assets from either Coingecko,
Coinmarketcap, DeFi Lama, or Messari. While digital assets trade continuously, we use daily close
prices based on UTC time to construct returns. To generate a crypto market factor, we follow a
process similar to Liu et al. (2022). Our market factor is based on the overall market capitalization
of five dominant digital assets (Bitcoin, Ethereum, Ripple, Cardano, and Solano). We then adjust
daily governance token returns based on this dominant-five market factor.
In most of our specifications, we use proposal-specific returns. For these proposals, we calculate
the returns from the date the voting window opens to when it ends. Some DAOs have voting
windows of three days and others a week. In each case, we use the window that is unique to the
DAOs specific voting process. The process at some DAOs may involve introducing and discussing
potential proposals in Forums or on Discord ahead of time, but not all DAOs do this. For consis-
tency, we use open as the beginning date. This open date represents when the proposal is formally
submitted either on-chain or off-chain (e.g., to Snapshot) for a vote. In the Appendix, we consider
a subsample for which we have the date of first discussion.
2.5 Real outcomes
We gather information on real outcomes for the DAOs in our study by focusing on trading
volumes on decentralized exchanges (DEXs), occurrences of fraud or security breaches, and social
media engagement metrics. Given that DeFi protocols and DEXs have the most well-established
business model and make up the majority of our sample, we start by collecting data on the daily
trading volumes of DEXs and DeFi protocols, normalizing the data in terms of Bitcoin equivalence
for consistent cross-platform comparability. Next, we address the aspect of security within the DeFi
space. Here, we utilize an advanced NLP algorithm to sift through Messari’s crypto newsfeed,
identifying and marking dates of known security breaches. The algorithm is designed to detect
specific security-related keywords in articles from leading crypto news outlets. Additionally, we
17

---

## Page 19

integrate data from Molly White’s “Web3 is Going Just Great” archive, which provides a unique
perspective on the challenges and exploits faced in the Web3 domain. Lastly, we turn our attention
to the social media to proxy for user growth and engagement with DAOs. For this, we normalize
and log-transform the number of daily social media users recorded on various platforms, including
X (formerly known as Twitter), Reddit, and Telegram. In sum, our data on real outcomes spans
DEX trading volume, security incidents, and user engagement, providing a rich dataset to analyze
the real effects and decentralized governance.
3 Characterizing DAOs
3.1 Types and functions
Table 1 characterizes the DAOs in our sample. Panel A classifies DAOs into three broad cate-
gories: DeFi, Infrastructure, and Web3. DeFi DAOs have a primary function related to providing
financial services in a decentralized manner (e.g., borrowing/lending). Infrastructure DAOs build
tools to facilitate the development of crypto ecosystems (e.g., bridges to facilitate communication
or asset transfers between blockchains). Web3 DAOs conduct a variety of activities related to new
internet services and platforms facilitated by blockchains (e.g., gaming and media, social clubs). 7
We also include DAOs that promote such activities (e.g., via accelerators, crowdfunding, or the
production of public goods) in the Web3 category. Overall, 61% (91 out of 150) of DAOs in our
sample have a primary function related to DeFi, followed by Web3 (32%), and Infrastructure (7%).
The third column of Panel A reports the number of proposals in our sample corresponding to each
type. The average number of proposals per DAO is 71.6 for DeFi, 22.4 for infrastructure, and 83.4
for Web3.
Panel B of Table 1 sheds further light on the functions of DAO. For each of the three broad
categories (DeFi, Infrastructure, and Web3), we provide a granular breakdown of the DAO functions
that are common in our sample. Functions are not mutually exclusive and can cut across the
7While there is not a consensus definition of “Web3,” decentralization as well ownership by users and
creators are often regarded as important aspects. See, for example, Roose (2022)
18

---

## Page 20

three broad categories. For example, BitDAO, which has close to $ 2 billion in Treasury assets,
invests in crypto projects and produces public goods by building tools for DAO governance/treasury
management as well as providing grants to researchers.8 The average DAO in our sample has more
than three functions under our classification, highlighting the diverse nature of activities that they
undertake. The most common DeFI functions include liquidity staking/yield farming (58 DAOs),
decentralized exchanges (44), borrowing and lending (24), and stablecoins (20). The functions
of infrastructure DAOs are data and identity (14), multichain (11), and tooling (37). The most
common Web3 functions are virtual reality (55), talent/gig work (28), public goods (28), and asset
management/crowdfunding (25).
3.2 Governance structures
Table 2 provides an overview of the governance structures used by DAOs. We focus on five di-
mensions of governance: voting mechanism, voting process, organizational design, security features,
and governance system model. We discuss each dimension in turn.
First, we consider voting mechanics, arguably the cornerstone of DAO governance. The majority
of DAOs in our sample (70%) use relative quorum voting. The use of this voting mechanism is
similar for the two main categories, DeFi and Web3 (columns 3 and 4 of Panel B). A relatively
small number of DAOs use variations on this idea. For example, 2% use relative quorum voting
with a differential. Under this system, if token turnout is low for a vote, a greater differential in
favor (e.g., 10 percentage points rather than a single vote) is required for a proposal to pass. Only
5% use a simple quorum which requires approval from a majority of tokens, not just voters. In
general, most DAOs using quorum voting abide by the majority, but 11% have a supermajority
requirement. The most common alternative to quorum systems is weighted voting (19%), which
places different weights on token holders’ votes. Common weighting criteria include reputation
(e.g., how active has the token holder been in the DAO) or the amount of time tokens have been
held. Other voting systems (e.g., quadratic or plural voting) are relatively rare, though 15% of
8See https://medium.com/bitdao/introducing-bitdao-464ebf80eb56
19

---

## Page 21

DAOs have voting requirements that vary by the nature of the proposal.
Second, we turn attention to the voting process. For the majority of DAOs (73%), the voting
process originates with informal discussion among token holders on a message board (e.g., Discord),
allowing the community to discuss the merits of the proposal and offer refinements. Creating a
formal proposal requires the use of a uniform template for 54% of DAOs, and 8%, primarily in the
DeFi category, require proposals to include executable code. More than half of the DAOs in our
sample impose other requirements to create a formal proposal (e.g., minimum token holdings). The
majority of DAOs conduct votes “off chain,” meaning that they use platforms that allow for token
holders to vote on proposals without incurring transaction (“gas”) fees associated with transactions
on a blockchain. Finally, 45% of DAOs permit votes to be delegated to other parties.
Third, we examine the organizational design of DAOs. Some DAOs implement corporate-like
structures to delegate decision-making. For example, 33% of DAOs in our sample have representa-
tives or board-like councils, while 27% have “sub DAOs” that specialize in a particular aspect of the
DAO’s mission. Similar to executive compensation in corporations, 18% of DAOs have multi-year
token-vesting schedules for key members. Finally, some DAOs reward participation by members
via incentives to vote (8%) or proof of attendance badges (5%). Such incentives highlight the idea
that token holders not only provide capital to the DAO but also the labor.
Fourth, we examine security features that mitigate the risk of malicious governance. To this
end, some DAOs employ ex post mechanisms. For example, 44% of DAOs in our sample require
multiple signatures (“multisig”) to execute a proposal, a third (42% in the DeFi category) allow the
core or developer team to override a proposal, and a quarter have a delay before implementation.
Some DAOs also use ex ante mechanism, including requiring a feasibility study prior to a proposal
vote (17%).
Finally, some DAOs are modeled after specific governance systems. Governor Bravo, Com-
pound’s governance system, is the model for 11% of DAOs in our sample. The governance of 6%
of DAOs is based on a framework developed by Aragon, which offers a suite of tools to set up a
DAO. Five percent of DAOs in our sample use some other governance model.
20

---

## Page 22

3.3 DAO Governance Index
Having characterized the DAO governance and voting process, we next seek to construct an
index of decentralized governance. For every DAO, we add one point for every feature that enhances
inclusivity and security and we deduct a point for features that serve to restrict the flexibility of
DAOs and make them more corporate-like. Such a simple index may not accurately reflect the
relative impact of different features, but we believe this simple design as a first attempt provides
advantages in terms of transparency and reproducability.
4 Governance and Performance
We next seek to shed light on the relationship between DAO governance and performance.
We consider three fundamental aspects of governance. First, to what extent do governance struc-
tures intended to promote broad participation in decision-making help DAOs achieve their goals?
Such structures help to incorporate a of a variety of viewpoints in DAO decision-making, thus
harnessing the wisdom of crowds. It is not clear, however, that inclusive decision-making is nec-
essarily desirable. Token holders, similar to shareholders of a corporation, have incentives to free
ride (Grossman and Hart, 1980; Shleifer and Vishny, 1986). If free rider incentives are sufficiently
strong, encouraging broad participation in decision-making may be counterproductive. Second,
do restrictions that impede DAO decision-making improve performance? Such restrictions help to
ensure proposals have broad community support but also present a barrier to reforms. Finally, does
security enhance a DAO’s ability to achieve its objectives? On the one hand, mitigating the risk of
malicious governance is obviously consistent with DAOs’ objectives. On the other hand, security
features may centralize decision-making and impede the flexibility inherent to this organizational
form (e.g., by impeding how quickly proposals can be passed).
Addressing these questions requires a measure of DAO performance. In the corporate context,
objectives are generally framed in terms of shareholder value maximization (e.g., Gompers et al.,
2003; Bebchuk et al., 2009). DAOs, however, rarely focus on explicit goals related to token value.
21

---

## Page 23

Rather, they often pursue non-financial objectives (e.g., long-term viability of the protocol, com-
munity growth). Our analysis assumes that the extent to which a DAO’s objectives are achieved is
reflected by the token price. For example, if a DAO’s primary goal is the long-term viability of its
protocol, we assume its token price will increase in response to actions that increase the likelihood
of the survival of the protocol.
We classify individual governance provisions into three categories: Inclusive, restrictive, and
security governance features. Inclusive governance features include provisions that encourage broad
participation in DAO decision-making (e.g., providing uniform templates for proposals, off-chain
voting, providing incentives to vote). Restrictive governance features limit members’ abilities to
implement proposals (e.g., quorum or supermajority requirements). Finally, security features reduce
the risk of governance attacks (e.g., requiring feasibility studies for proposals or multisig before
implementation). Figure 3 provides a heat map of the provisions within each category. In the
following analysis, we consider the relationship between individual governance provisions and token
returns associated with improvement proposals. We also conduct analysis on indexes of governance
features, which we construct by summing the indicators for each type of provision.
Table 3 analyzes the relationship between individual DAO governance structures and proposal
returns. The dependent variable is market-adjusted returns associated with proposals, measured
from the introduction of a proposal to the end of voting. All specifications include year, geographic
location, and DAO-type fixed effects. Column 1 reports coefficients for inclusive governance fea-
tures. Estimated coefficients are positive for 3 of the 5 variables (off-chain voting, ability to delegate
votes, and proof of attendance badges). The coefficient for providing uniform proposal templates is
negative, and the coefficient for vote incentives is statistically indistinguishable from zero. Column
2 reports coefficients for restrictive governance features. Coefficients are negative for 4 of 8 gover-
nance features (executable code requirements, voting requirements varying by content, the use of
board-like councils, and the inclusion of subDAOs), 2 out of 8 provisions have positive coefficients
(formal proposal requirements and supermajority voting), and the coefficient for a quorum require-
ment is indistinguishable from zero. Column 3 reports coefficients for security features. Coefficients
for multisig requirements, feasibility studies, and the use of Safesnap are positive, while those for
22

---

## Page 24

delays before implementation and ability of the core/developer team to override proposals are in-
distinguishable from zero. Finally, columns 4 and 5 report specifications including all three types
of provisions. Patterns observed in columns 1–3 are even more apparent in these specifications.
Specifically, 4 out of 5 coefficients are positive for inclusive governance features, 6 out of 8 are
negative for restrictive governance features, and 4 out of 5 are positive for security features.
In Table 4 we aggregate provisions into indexes of inclusive, restrictive, and security governance
features by summing indicators for the provisions within each group. This test is similar to the
analysis of corporate governance provisions by Gompers et al. (2003) and Bebchuk et al. (2009).
Echoing the findings in Table 3, we find that the inclusive voting and security indexes are positively
related to abnormal returns, while the restrictive voting index is negatively related. Our inferences
are similar when considering indexes individually (columns 1-3) or in joint specifications (columns
4-5).
If decentralized governance matters for digital asset returns, then the price should quickly
incorporate any changes brought about. In Table 5, we aggregate into a single index of decentralized
governance and analyze the relationship between the index and proposal returns. It shows a strong,
positive correlation between the index and the proposal returns both with and without controls.
Further, when we analyze the relation between a low score on the index, a middle score on the index,
and a high score on the index, we see a consistent pattern that higher decentralized governance
scores are associated with higher proposal returns whereas lower decentralized governance index
scores are associated with lower proposal returns.
We recognize that these are interesting conditional correlations and not causal. Given that DAO
token returns are analyzed following a vote on a new improvement proposal, our study faces the
difficulty that new provisions may be driven by contemporaneous conditions at the DAO (i.e., the
adoption of provision may be related to the governance structure and provide a signal of whoever
suggested the proposal’s private information). One way to avoid these difficulties is to take a
calendar-horizon approach and view the relationship over time. In Table 6, this is exactly what we
do. We use the aggregated single index of decentralized governance and analyze the relationship
between the index and weekly crypto-adjusted returns. It shows a strong, positive correlation
23

---

## Page 25

between the decentralized governance index and weekly crypto-market adjusted returns. Further,
when we analyze the relation between a low score on the index, a middle score on the index, and
a high score on the index, we see a consistent pattern that higher decentralized governance scores
are associated with higher weekly returns whereas lower decentralized governance index scores are
associated with lower weekly returns.
Overall, our findings highlight the relation between governance and performance in DAOs. Di-
mensions of governance that promote broad participation by token holders or reduce the likelihood
of malicious behavior are associated with improved performance. However, governance provisions
that impede improvement proposals are negatively related to performance.
4.1 Alternative Return Specifications
In Appendix D, we consider several alternative return specifications as robustness checks. First,
we examine the non-crypto market adjusted returns and document, in almost all cases even stronger
statisical results. This suggests this is not something driven by our adjustment process. Next, for
a subsample of proposals, we have the date the discussion started online. We re-run our analysis
based on the longer window and find similar results. Third, we examine monthly returns rather
than weekly returns. Again, we find similar patterns even when we focus on monthly returns.
4.2 Testing Real Outcomes
Next, we examine the efficacy of the digital asset return findings by evaluating real outcomes.
We do so because there are many factors other than decentralized governance that potentially
influence digital asset pricing dynamics. Among these factors are the potential roles of major
investors (often termed “whales”) play, which can lead to price manipulation, the existence of
segmented markets, and the phenomenon of irrational exuberance, which might lead to deviations
from underlying economic fundamentals. To address these concerns and to rule out these alternate
narratives, our analysis is extended to explore the connection between our decentralized governance
index and components and real outcomes associated with performance and success.
24

---

## Page 26

First, we look within the DeFi space as these DAOs often offer a more straightforward business
model to interpret. In this context, a higher trading volume typically correlates with improved
profitability and overall performance. As demonstrated in Table 7, we estimate a positive relation-
ship between the decentralized governance index and the trading volume on DEXs. This suggests
that effective decentralized governance, as proxied by our index, contributes more broadly to the
organization and helps to attract additional trading activity within these platforms.
Second, we delve deeper into the components of the decentralized governance index by con-
centrating on two distinctive features of decentralized governance relative to traditional corporate
governance: security features and inclusivity provisions. As shown in Columns 3 and 4 of Table 7,
our analysis uncovers a negative correlation between adopting security features and the frequency
of DAO-specific crypto news pertaining to scams or hacks. This indicates that stronger security
measures in decentralized settings may contribute to reducing the incidence of such adverse events.
Finally, as shown in Columns 5 and 6 of Table 7, we find a positive association between the in-
clusivity components of our governance index and user growth. Here, we use the number of social
media followers as a proxy for user growth. This suggests that governance systems that are more
open and inclusive may be more effective in attracting and engaging users.
In summary, our additional tests exploring real outcomes are consistent with the tests that we
have highlighting crypto-market adjusted returns associated with the voting window for improve-
ment proposals. This suggests that the significance of security and inclusivity in the decentralized
governance index are not just mere speculation or the influence of whales but rather, on average,
reflect a respective real link to trading volumes, hacks or scams, and user engagement.
4.3 Estimates from a Regression Discontinuity Design
One important question that arises when trying to infer the value of decentralized governance
is exactly what to look at when considering returns. While we have examined returns surrounding
proposals as well as real outcomes, for identification purposes, we would want to identify the impact
of decentralized governance changes with an “as if random” counterfactual. Close-call governance
25

---

## Page 27

proposals offer one such option. However, we note that given that the vast majority of proposals
pass or fail by more than 80%, this meaningfully limits our sample size. Nevertheless, we have 624
governance proposals that are close-call, and that would directly impact the construction of our
index. For instance, 1inch had a proposal to reduce the quorum threshold, which would make the
voting process less restrictive in our index. In determining our restricted sample, we focus only on
observations within an optimally derived threshold bandwidth. Specifically, we follow the econo-
metric procedure developed by Imbens and Kalyanaraman (2011) and further refined in Calonico
et al. (2015) and Calonico et al. (2019). The procedure allows for different bandwidth selections
on either side of the threshold and distinguishes between mean-square error (MSE) optimal band-
widths and coverage error ratio (CER)-optimal choices. Different estimators will have different bias
and variance terms depending on the outcome of interest and the assumptions on heteroskedasticity
and clustering. We consider a variety of optimal bandwidth selectors and report them in Appendix
D. We observe little difference between the various MSE-optimal bandwidth selectors and the var-
ious CER-optimal selectors, and so choose the median bandwidth for each type as it may have
better rate properties. However, we see more meaningful differences between the MSE-optimal and
CER-optimal choices, something we explore more when we turn to the evidence for changes in DAO
performance.
We start by exploring the visual evidence for increases in DAO performance following the
passing of a governance improvement proposal. Figure 4 presents visual evidence for a discontinuity
in changes in crypto-adjusted returns during the week after the close-call vote as a function of the
vote share crossing the win threshold. This discontinuity is critical for estimating the effect of an
increase in the governance index on DAO performance. The figure illustrates the discontinuity
by plotting the average change in performance as a function of the proximity to the winning
threshold. If the proposal passes as is indicated by being above the win threshold, then the average
DAO changes by 0.03 to 0.05 standard deviations depending on the line of best fit. This establishes
visual evidence for a discontinuity.
Next, Table 8 shows the regression evidence for the discontinuity. Columns (1) to (4) examine
the MSE-optimal bandwidth, columns (5) to (8) examine the CER-optimal bandwidth, and columns
26

---

## Page 28

(9)-(12) use the full sample but allow for flexible polynomial form on either side of the threshold.
Panel A examines short-term returns (one week). In all 12 regressions, we find a statistically
significant increase in digital asset returns in relation to a close-call improvement proposal passing.
Across the various specifications, the point estimates are similar and suggest anywhere from 0.048
to 0.057 standard deviation increase. Panel B examines the returns in the longer-term as proxied
by one month returns. Here, again, we see variation across the bandwidths. While each estimate
is positive, only the MSE-optimal and polynomial bandwidths are statistically significant. This
evidence is consistent with prior results suggesting that decentralized governance matters for digital
asset returns.
5 Conclusion
The DAO organizational form has gained prominence in recent years. In contrast to corpora-
tions, decision-making authority lies with members of the DAO rather than managers. This study
provides some of the first evidence on DAO governance structures and their implications for digital
asset prices. We document rich heterogeneity in both the purposes of DAOs and the governance
mechanisms they employ. Consistent with anecdotal evidence, most DAOs have primary functions
related to DeFi, though a sizable portion engage in other activities related to Web3. DAOs em-
ploy a variety of governance structures related to voting mechanisms and processes, organizational
design such as the creation of board-like structures and subDAOs, and security.
To make headway in understanding best practices for DAOs, we categorize DAO governance
features, classifying them into inclusive, restrictive, and security-oriented provisions. We find that
dimensions of governance that promote inclusive decision-making and security are positively associ-
ated with DAO performance. Restrictive structures that impede reaching consensus are associated
with worse performance on average. These results help to extend our understanding of governance
beyond traditional corporate structures. Consistent with traditional structures, democratic pro-
cesses are valuable (Gompers et al., 2003; Frankenreiter et al., 2021) in DAOs too. However, broad
engagement and empowerment of non-core contributors are especially valuable in decentralized
27

---

## Page 29

contexts. The positive relationship between inclusive governance and DAO performance supports
the notion that crowd wisdom can enhance decision-making. It also supports the notion that gover-
nance processes adjust to the production function, indicating decentralized and centralized finance
require different structures.
Our analysis also highlights the unique challenges and opportunities presented by blockchain-
based governance. Implementing security features to mitigate governance attacks represents a novel
aspect of governance, reflecting the distinct risks inherent in decentralized systems. While our study
provides valuable insights, it also opens avenues for future research. The long-term sustainability
of DAOs, the optimal balance between decentralization and efficiency, and the potential for DAOs
to integrate and serve as a viable alternative to traditional organizational structures are all fertile
areas for further investigation. As the DAO ecosystem continues to evolve, our findings suggest
that governance design will play a crucial role in determining these novel organizational forms’
success and value creation. By making our DAO governance data publicly available, we aim to
facilitate further research in this rapidly developing field, potentially leading to more robust and
effective decentralized governance models in the future.
28

---

## Page 30

References
Admati, A. R., Pfleiderer, P., 2009. The wall street walk and shareholder activism: Exit as a form
of voice. Review of Financial Studies 22, 2645–2685.
Appel, I., Gormley, T., Keim, D., 2016. Passive investors, not passive owners. Journal of Financial
Economics 121, 111–141.
Appel, I., Grennan, J., 2023. Control of decentralized autonomous organizations. AEA Papers and
Proceedings 113, 182–185.
Atta-Darkua, V., 2023. Decoding decentralized liquidity: A study of dao cash reserves. Working
Paper .
Augustin, P., Chen-Zhang, R., Shin, D., 2022. Yield farming. working paper .
Austgen, J., Fabrega, A., Allen, S., Babel, K., Kelkar, M., Juels, A., 2023. Dao decentralization:
Voting-bloc entropy, bribery, and dark daos. arXiv:2311.03530v1 .
Baker, G., Gibbons, R., Murphy, K. J., 2002. Relational contracts and the theory of the firm.
Quarterly Journal of Economics 117, 39–84.
Bebchuk, L., Cohen, A., Ferrell, A., 2009. What matters in corporate governance? The Review of
financial studies 22, 783–827.
Bena, J., Zhang, S., 2023. Token-based decentralized governance, data economy and platform
business model. UBC Working Paper .
Broccardo, E., Hart, O., Zingales, L., 2022. Exit versus voice. Journal of Political Economy 130,
3101–3145.
Calonico, S., Cattaneo, M. D., Farrell, M. H., 2019. Optimal bandwidth choice for robust bias-
corrected inference in regression discontinuity designs. The Econometrics Journal 23, 192–210.
Calonico, S., Cattaneo, M. D., Titiunik, R., 2015. Optimal data-driven regression discontinuity
plots. Journal of the American Statistical Association 110, 1753–1769.
Coase, R. H., 1937. The nature of the firm. Economica 4, 386–405.
Cointelegraph, 2022. Dao: The evolution of organization. White Paper .
Cong, L. W., He, Z., 2019. Blockchain disruption and smart contracts. The Review of Financial
Studies 32, 1754–1797.
Cong, L. W., Li, Y., Wang, N., 2022. Token-based platform finance. Journal of Financial Economics
144, 972–991.
29

---

## Page 31

Cookson, A. J., Niessner, M., 2019. Why don’t we agree? Evidence from a social network of
investors. Journal of Finance forthcoming.
Cunat, V., Gine, M., Guadalupe, M., 2012. The vote is cast: The effect of corporate governance on
shareholder value. Journal of Finance 67, 1943–1977.
Da, Z., Huang, X., 2020. Harnessing the wisdom of crowds. Management Science forthcoming.
Dessaint, O., Foucault, T., Fresard, L., 2022. Does alternative data improve financial forecasting?
the horizon effect. Journal of Finance .
Dugast, J., Foucault, T., 2018. Data abundance and asset price informativeness. Journal of Finan-
cial Economics 130, 367–391.
Frankenreiter, J., Hwang, C., Nili, Y., EricTalley, 2021. Cleaning corporate governance. University
of Pennsylvania Law Review 170, 1–70.
Goldstein, I., Gupta, D., Sverchkow, R., 2022. Utility tokens as a commitment to competition.
Working Paper .
Gompers, P., Ishii, J., Metrick, A., 2003. Corporate governance and equity prices. The quarterly
journal of economics 118, 107–156.
Gorton, G., Zhang, J. Y., 2023. Taming wildcat stablecoins. University of Chicago Law Review 90,
909.
Grennan, J., 2022. Fintech regulation in the United States: Past, present, and future. working
paper .
Grennan, J., Michaely, R., 2019. The deleveraging of U.S. firms and institutional investors’ role.
Working Paper .
Grennan, J., Michaely, R., 2020. FinTechs and the market for financial analysis. Journal of Financial
and Quantitative Analysis 56, 1877–1907.
Grennan, J., Michaely, R., 2022. Artificial intelligence and high-skilled work: Evidence from ana-
lysts. working paper .
Griffin, J., Shams, A., 2020. Is bitcoin really untethered? The Journal of Finance 75, 1913–1964.
Grossman, S. J., Hart, O. D., 1980. Takeover bids, the free-rider problem, and the theory of the
corporation. The Bell Journal of Economics pp. 42–64.
Han, J., Lee, J., Li, T., 2023. Dao governance. Working paper .
Hansmann, H., 2000. The Ownership of Enterprise. Harvard University Press.
Hart, O., 1996. The governance of exchanges: members’ cooperatives versus outside ownership.
Oxford Review of Economic Policy 12, 53–69.
Harvey, C., Ramachandran, A., Santoro, J., 2021. DeFi and the Future of Finance. Wiley.
30

---

## Page 32

Hassan, S., Filippi, P. D., 2021. Decentralized autonomous organization. Internet Policy Review
10, 1–10.
Howell, S. T., Niessner, M., Yermack, D., 2020. Initial coin offerings; financing groth with cryp-
tocurreny token sales. Review of Financial Studies 33, 3925–3974.
Huberman, G., Leshno, J. D., Moallemi, C., 2019. An economist’s perspective on the bitcoin
payment system. AEA Papers and Proceedings 109, 93–96.
Imbens, G., Kalyanaraman, K., 2011. Optimal bandwidth choice for the regression discontinuity
estimator. The Review of Economic Studies 79, 933–959.
Jensen, M. C., Meckling, W. H., 1976. Theory of the firm: Managerial behavior, agency costs and
ownership structure. Journal of Financial Economics 3, 305–360.
John, K., Kogan, L., Saleh, F., 2023. Smart contracts and decentralized finance. Annual Review of
Financial Economics 15.
Kalay, A., Karak¸ s, O., Pant, S., 2014. The market value of corporate votes: Theory and evidence
from option prices. The Journal of Finance 69, 1235–1271.
Karpoff, J. M., Rice, E. M., 1989. Organizational form, share transferability, and firm performance.
Journal of Financial Economics 24, 69–105.
Kiayias, A., Lazos, P., 2022. Sok: Blockchain governance.
Kogan, S., Niessner, M., Makarov, I., Schoar, A., 2023. Are cryptos different? evidence from retail
trading. Working paper .
Laturnus, V., 2023. The economics of decentralized autonomous organizations. Working paper .
Lee, D. S., Lemieux, T., 2010. Regression discontinuity designs in economics. Journal of Economic
Literature 48, 281–355.
Lehar, A., Parlour, C., 2023. Decentralized exchange: The uniswap automated market maker.
Journal of Finance .
Lewellen, J., Lewellen, K., 2021. Institutional investors and corporate governance: The incentive
to be engaged. Journal of Finance 77, 213–264.
Li, J., Mann, W., 2021. Digital tokens and platform building. Working Paper .
Liu, Y., Tsyvinski, A., Wu, X., 2022. Common risk factors in cryptocurrency. Journal of Finance
77, 1133–1177.
Makarov, I., Schoar, A., 2022. Cryptocurrencies and decentralized finance (defi). Working Paper .
Mei, K., Sockin, M., 2023. A theory of speculation in community assets. Working Paper .
Oh, S., Rosen, S., Zhang, A. L., 2022. Investor experience matters: Evidence from generative art
collections on the blockchain. Working paper .
31

---

## Page 33

Roose, K., 2022. What is web3? New York Times p. March 18.
Sharma, T., Kwon, Y., Pongmala, K., Wang, H., Miller, A., DawnSong, Wang, Y., 2023. Tanusree
sharma, yujin kwon, kornrapat pongmala, henry wang, andrew miller, dawnsong, and yang wang.
unpacking how decentralized autonomous organizations (daos)work in practice. arXiv:2304.09822
.
Shleifer, A., Vishny, R. W., 1986. Large shareholders and corporate control. Journal of Political
Economy 94, 461–488.
Sockin, M., Xiong, W., 2022. Decentralization through tokenization. Journal of Finance .
Tan, J., Merk, T., Hubbard, S., Oak, E. R., Rong, H., Pirovich, J., Rennie, E., Hoefer, R., Zargham,
M., Potts, J., Berg, C., Youngblom, R., De Filippi, P., Frey, S., Strnad, J., Mannan, M., Nabben,
K., Elrifai, S. N., Hartnell, J., Hill, B. M., South, T., Thomas, R. L., Dotan, J., Spring, A.,
Maddox, A., Lim, W., Owocki, K., Juels, A., Boneh, D., 2023. Open problems in daos.
Wang, Q., Yu, G., Sai, Y., Sun, C., Nguyen, L. D., Xu, S., Chen, S., 2022. An empirical study on
snapshot daos.
White, J., Wilkoff, S., 2023. The effect of celebrity endorsements on crypto: Evidence from initial
coin offerings (icos). Working paper .
Yermack, D., 2017. Corporate Governance and Blockchains. Review of Finance 21, 7–31.
Zingales, L., 1995. What determines the value of corporate votes? The Quarterly Journal of
Economics 110, 1047–1073.
32

---

## Page 34

Figure 1. Voters on 1Inch proposal. The figure depicts the voters and outcomes on a
1inch proposal.
33

---

## Page 35

Figure 2. DAO improvement proposal categories. The figure depicts the five main
categories of DAO improvement proposals: finance, governance, management, tokenomics,
and viability. Below each main category are subcategories representative of different kinds
of proposals.
34

---

## Page 36

Figure 3. DAO governance heatmap. The DAO governance index includes 17 components
which are categorized into three main groups: inclusive, restrictive, and secure. This figure
displays a heatmap of the correlations between the DAO governance index, which is displayed
on the bottom row, and all of its individual components. Red reflects a negative correlation
and blue a positive correlation.
35

---

## Page 37

-0.05
0.00
0.05
0.10
Change in digital asset returns (one week)
-0.30 -0.20 -0.10 0.00 0.10 0.20 0.30
Percent above or below winning threshold
Figure 4. The figure displays the average change in digital asset value following a close-call
vote involving a governance improvement proposal. If the improvement proposal wins as is
indicated by being above the passing threshold based on the DAOs’ rules, then the digital
asset is significantly more likely to increase in value. Each dot is the average change in digital
asset value within the optimally derived bin width as derived by Calonico et al. (2019) and
contains multiple underlying observations. The lines associated with the dots represent the
upper and lower 90% confidence intervals. Solid lines are estimated using linear regressions
on either side of the threshold and represent a monomial fit.
36

---

## Page 38

Table 1.
Characterizing DAOs
This table presents the percentage of DAOs with each governance provision. The data are collected from
DAO white papers, Forum rules, and Snapshot pages. See Appendix A for detailed information on each of
these provisions. The sample consists of 150 DAOs for which we have proposal text, voting outcomes, and
digital asset returns.
Number of DAOs Number of Proposals
Panel A. Main DAO types (1) (2)
DeFi 91 6513
Infrastructure 11 246
Web3 48 4005
Total 150 10764
Panel B. Detailed DAO functionalities
DeFi
Borrowing/lending 26 1266
Decentralized exchanges and automated market makers 44 3911
Derivatives, leverage, and margin trading 17 925
Insurance and risk management 10 346
Liquidity staking and yield farming 58 3248
Payments 12 642
Stablecoin 20 1714
Infrastructure
Data and Identity 14 595
Multichain 11 262
Tooling 37 2049
Web3
Asset management/crowdfunded investments 25 1715
Entrepreneurial accelerators 5 193
Gaming 14 1931
Media and content curation 18 2274
NFTs 6 178
Porting assets between Web3 and real world 10 537
Public goods 28 1186
Single-purpose 10 499
Social clubs 21 1169
Talent and gig work 28 1137
Virtual and augmented reality 55 4248

---

## Page 39

Table 2.
DAO Governance Provisions
This table presents the percentage of DAOs with each governance provision. The data are collected from
DAO white papers, Forum rules, and Snapshot pages. See Appendix A for detailed information on each of
these provisions. The sample consists of 150 DAOs for which we have proposal text, voting outcomes, and
digital asset returns.
All DAOs DeFi DAOs Web3 DAOs
(1) (2) (3)
DAO voting mechanism
Simple quorum voting 5% 2% 10%**
Relative quorum voting 70% 70% 71%
Relative quorum voting with differential 2% 2% 2%
Supermajority voting 11% 12% 8%
Weighted voting 19% 21% 13%
Quadratic voting 3% 2% 2%
Conviction voting 1% 0% 2%
Lazy consensus 7% 8% 4%
Voting requirements vary by content 15% 15% 10%
DAO voting process
Ideas start via informal discussion (e.g., on Discord) 73% 78% 67%
Requirements to create a formal proposal (e.g., hold X tokens) 63% 67% 56%
Uniform, transparent templates for proposals 54% 54% 50%
Requires executable code in proposal (i.e., no developer help) 8% 11% 2%*
Off-chain gasless vote for signaling (e.g., Snapshot) 88% 85% 94%
Quorum requirement (e.g., 5% of token supply) 56% 66% 33%***
Votes can be delegated to individuals or DAOs 45% 49% 38%
DAO organizational design features
Includes subDAOs 27% 26% 31%
Includes appointed representatives or board-like councils 33% 29% 35%
Includes multi-year, token-vesting schedule for key members 18% 23% 6%**
Provides incentives to vote (e.g., increased rewards) 8% 10% 4%
Provides proof of attendance badges 5% 2% 10%**
Security features
Delay or timelock before implementation 25% 25% 25%
Multisig before implementation 44% 47% 38%
Core or developer team can override 33% 42% 21%***
Feasibility study (e.g., technical, financial, security) 17% 16% 17%
Safesnap 7% 11% 0%**
Governance systems modeled after
Aragon 6% 7% 4%
Governor Bravo 11% 14% 8%
Other 5% 7% 0%*

---

## Page 40

Table 3.
Return Regression on Improvement Proposals by Individual Governance Features
This table estimates the relation between governance features and crypto-market adjusted returns from the
opening date of the proposal to the voting end. The governance features are grouped into the subindex
components: inclusive, restrictive, and secure. Year, geographic location, and DAO type fixed effects are
included. Controls include DAO age, an indicator for an early proposal, vote duration, and the detailed
industry characterization. Robust standard error are reported in parantheses and significance at the 10
percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5)
Inclusive governance features
Uniform, transparent templates for proposals -0.312** 0.018 -0.004
(0.136) (0.136) (0.161)
Off-chain gasless vote for signaling 0.300** 0.510*** 0.761***
(0.145) (0.162) (0.223)
Votes can be delegated to individuals or DAOs 0.176* 0.737*** 0.757***
(0.096) (0.153) (0.186)
Provides incentives to vote 0.590* 1.000*** 2.383***
(0.354) (0.357) (0.535)
Provides proof of attendance badges 0.240 2.104*** 2.775***
(0.420) (0.602) (0.694)
Restrictive governance features
Requirements to create a formal proposal 0.621*** 0.455*** 0.715***
(0.135) (0.124) (0.224)
Requires executable code in proposal -0.238 -0.512** -0.969***
(0.170) (0.219) (0.285)
Quorum requirement -0.417** -0.682*** -0.806***
(0.163) (0.168) (0.284)
Relative quorum voting with differential -0.064 -2.191*** -3.320***
(0.141) (0.461) (0.681)
Supermajority voting 0.213 -0.409** -1.095***
(0.156) (0.206) (0.253)
Voting requirements vary by content -0.621*** -0.726*** -0.502**
(0.203) (0.189) (0.238)
Includes appointed representatives of board-like council -0.480*** -0.658*** -0.919***
(0.125) (0.149) (0.220)
Includes subDAOs -0.691*** -1.043*** -0.813***
(0.101) (0.164) (0.165)
Secure governance features
Delay or timelock before implementation 0.126 0.287* 0.474**
(0.135) (0.161) (0.236)
Multisig before implementation 0.188* 0.359*** 0.935***
(0.097) (0.118) (0.213)
Core or developer team can override -0.107 0.106 0.372
(0.100) (0.144) (0.237)
Feasibility study 0.518*** 1.467*** 1.998***
(0.197) (0.294) (0.387)
Safesnap 0.748** 1.114*** 0.432
(0.337) (0.355) (0.385)
Fixed effects Yes Yes Yes Yes Yes
Controls No No No No Yes
Observations 8,534 8,534 8,534 8,534 8,534
R-squared 0.019 0.029 0.020 0.061 0.084

---

## Page 41

Table 4.
Return Regression on Improvement Proposals by Governance Indices
This table estimates the relation between governance features and crypto-market adjusted returns from the
opening date of the proposal to the voting end. The governance features are grouped into the subindex
components: inclusive, restrictive, and secure. Year, geographic location, and DAO type fixed effects are
included. Controls include DAO age, an indicator for an early proposal, vote duration, and the detailed
industry characterization. Robust standard error are reported in parantheses and significance at the 10
percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5)
Inclusive voting features 0.056 0.318*** 0.199**
(0.042) (0.062) (0.086)
Restrictive voting features -0.288*** -0.489*** -0.484***
(0.041) (0.063) (0.076)
Secure voting features 0.178*** 0.399*** 0.419***
(0.051) (0.072) (0.104)
Fixed effects Yes Yes Yes Yes Yes
Controls No No No No Yes
Observations 8,534 8,534 8,534 8,534 8,534
R-squared 0.014 0.019 0.016 0.030 0.053

---

## Page 42

Table 5.
Return Regression on Improvement Proposals by Decentralized Governance Index
This table estimates the relation between decentralized governance index and crypto-market adjusted returns
from the opening date of the proposal to the voting end. The governance features are grouped into a single
index defined as inclusive less restrictive plus secure features. Year, geographic location, and DAO type fixed
effects are included. Controls include DAO age, an indicator for an early proposal, vote duration, and the
detailed industry characterization. Robust standard error are reported in parantheses and significance at
the 10 percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5) (6) (7) (8)
Decentralized governance index 0.362*** 0.324***
(0.049) (0.059)
Low index -0.489*** 0.034
(0.087) (0.122)
Mid-range index 0.366*** 0.089
(0.103) (0.133)
High index 1.219*** 1.014***
(0.243) (0.276)
Fixed effects Yes Yes Yes Yes Yes Yes Yes Yes
Controls No Yes No Yes No Yes No Yes
Observations 8,534 8,534 8,534 8,534 8,534 8,534 8,534 8,534
R-squared 0.029 0.052 0.015 0.043 0.016 0.043 0.023 0.048

---

## Page 43

Table 6.
Weekly Regressions by Decentralized Governance Index
This table estimates the relation between decentralized governance index and crypto-market adjusted returns
using weekly returns. The governance features are grouped into a single index defined as inclusive less
restrictive plus secure features. Robust standard error are reported in parantheses and significance at the
10 percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted weekly returns
(1) (2) (3) (4) (5) (6) (7) (8)
Decentralized governance index 0.513*** 0.526**
(0.195) (0.219)
Low index -2.367*** -1.763**
(0.771) (0.778)
Mid-range index -0.416 -1.060*
(0.600) (0.643)
High index 2.196** 2.454**
(0.918) (0.961)
Observations 11,330 11,330 11,330 11,330 11,330 11,330 11,330 11,330
R-squared 0.015 0.025 0.015 0.025 0.015 0.025 0.015 0.025

---

## Page 44

Table 7.
Real Outcomes and Decentralized Governance
This table estimates the relation between the decentralized governance index and real outcomes. The key
dependent variables are average DEX trading volume, an indicator variable for a hack or scam, and user
growth. Observations are at the DAO-month level. Year, geographic location, and DAO type fixed effects are
included. Controls include DAO age and detailed industry characterization. The decentralized governance
index represents when the governance features are grouped into a single index defined as inclusive less
restrictive plus secure features. Robust standard error are reported in parantheses and significance at the
10 percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Real outcomes
DEX volume Hack or scam User Growth
(1) (2) (3) (4) (5) (6)
Decentralized governance index 0.433** 0.418**
(0.211) (0.199)
Secure voting features -0.491* -0.426*
(0.281) (0.237)
Inclusive voting features 0.846** 0.232*
(0.385) (0.123)
Fixed effects Yes Yes Yes Yes Yes Yes
Controls No Yes No Yes No Yes
Observations 1,589 1,589 2,610 2,610 2,610 2,610
R-squared 0.033 0.041 0.034 0.035 0.033 0.041

---

## Page 45

Table 8.
Digital Asset Performance after Close-call Governance Improvement Proposal Vote
This table presents regressions of the change in digital asset performance on whether or not an improvement proposal won in a close-call vote.
Panel A examines digital asset performance in the short-term (one week), and Panel B examines digital asset performance in the long-term
(one month). Estimates in columns (1) to (4) use the optimal mean square error (MSE) bandwidth; columns (5) to (8) use the optimal coverage
error rate (CER) bandwidth, and columns (9) to (12) introduce a polynomial on each side of the threshold and uses the full sample. Pre-vote
DAO controls include whale ownership, functionality, and governance. Robust standard errors are reported below the coefficient estimates.
***, ** and * indicate p-values of 1%, 5%, and 10%, respectively.
Dep. var. = Crypto-adjusted returns (one week post vote)
MSE-optimal bandwidth CER-optimal bandwidth Polynomial
Panel A. (1) (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12)
Governance improvement proposal wins 0.048*** 0.049*** 0.048*** 0.048*** 0.049** 0.050** 0.050** 0.049** 0.057*** 0.048** 0.057*** 0.055**
(0.017) (0.017) (0.017) (0.017) (0.025) (0.024) (0.025) (0.024) (0.021) (0.021) (0.022) (0.021)
Size of bandwidth [0.250, 0.285] [0.143, 0.163] Full sample
Pre-vote DAO controls No Yes No Yes No Yes No Yes No Yes No Yes
Time fixed effets No No Yes Yes No No Yes Yes No No Yes Yes
Dep. var. = Crypto-adjusted returns (one month post vote)
MSE-optimal bandwidth CER-optimal bandwidth Polynomial
Panel B. (1) (2) (3) (4) (5) (6) (7) (8) (9) (10) (11) (12)
Governance improvement proposal wins 0.031** 0.031** 0.030** 0.029** 0.026 0.026 0.026 0.027 0.036** 0.037** 0.030* 0.030*
(0.013) (0.013) (0.013) (0.013) (0.019) (0.019) (0.019) (0.019) (0.016) (0.016) (0.016) (0.016)
Size of bandwidth [0.250, 0.285] [0.143, 0.163] Full sample
Pre-vote DAO controls No Yes No Yes No Yes No Yes No Yes No Yes
Time fixed effets No No Yes Yes No No Yes Yes No No Yes Yes
44

---

## Page 46

Internet Appendix

---

## Page 47

A Legal Analysis of DAOs
Regulators reduced regulatory uncertainty surrounding DAOs by commenting on the sale of
the original DAO tokens. As described in Grennan (2022), the SEC maintained that the extent to
which an instrument has the signs or indications of an investment contract, then it should be offered
and sold in compliance with the securities laws. Another key regulatory decision came in December
2017, when the SEC took its first enforcement action relating to the sale of digital assets, ultimately
issuing a cease-and-desist letter to halt the sale of Munchee tokens after concluding that the sale
was in fact an unregistered securities offering. A key lesson of the Munchee enforcement action
was that a developer’s decentralized design was not enough to bypass the securities distinction and
instead, expectation of profit is what mattered. Specifically, since Munchee offered the digital assets
to prospective investors under an investment intent, it constituted a securities offering subject to
the U.S. federal securities laws.
As the regulator stance helped to clarify an organization can classify itslef as a DAO, but if
the organization is aiming to make a profit of some sort, then it is likely an implied partnership
without any partnership agreement to define rights and obligations of members. This means lack
of limitation of liability, fiduciary duties, and rights that members have against other members.
States recognized the need for a legal framework for DAOs. In 2018, Vermont enacted a law that
enables Blockchain-Based Limited Liability Company (BBLLCs). Then, in 2019, the first legally
established Decentralized Autonomous Organization (DAO) under United States law was formed
in Vermont. The protocol, known as dOrg, deployed its DAO on the Ethereum blockchain, and also
formed a BBLLC, known as dOrg LLC. By linking the DAO to the BBLLC, the DAO obtained
official legal status, allowing it to enter contractual agreements and offer participants liability
protections. Other states have created similar legislation. As of July 1, 2021, Wyoming put into
place legislation pertaining to DAOs that made it possible to register DAOs and to convert existing
LLCs into DAOs without requiring residence in the state. In contrast, Delaware, the most common
jurisdication for corporations to incorporate, still does not recognize DAOs but does recognizes
organizations that do not classify themselves as implied partnerships.
1

---

## Page 48

Unlike corporations, which typically can obtain default charters from the state that they are
incorporating in, there is no default DAO structure. Instead, a set of service providers are helping
DAOs with their legal structure. For example, in 2017 Tribute Labs was launched to support
and create DAO communities through open-source frameworks built on Ethereum. The founders’
vision was to help crypto projects create, execute, and store legal agreements in one place. Its main
function today is to provide software and support services to help form and run DAOs, with the
crucial feature of handling legal matters. The team was able to successfully wrap traditional DAOs
as legal entities. In July 2021, Tribute Labs launched the Tribute DAO framework, which enables
building and managing DAOs through a modular architecture offering.
Other open source technologies are also helping to facilitate the creation of DAOs. Specifically,
there are many DAO tooling companies that serve to help DAOs set up legally, to outsource aspects
of the governance process, especially off-chain voting and social dynamics, and to facilitate some
functions commonly associated with personnel economics like human resources.
2

---

## Page 49

B Variable Definitions
Main categories of DAOs
 DeFi DAOs or “decentralized finance” DAOs provide financial products and services with-
out relying on centralized intermediaries by using smart contracts on a blockchain.
 Infrastructure DAOs provide products and services (i.e., tools) that DAOs use to operate.
These tools may include software for governance or treasury management, data to execute
smart contracts, smart contract templates, cross-chain services, etc.
 Web3 DAO help non-financial consumers connect to the benefits of blockchain by allowing
both users and developers to orchestrate actions with tokens in a decentralized manner.
DAO DeFi functionalities
 Borrowing and lending indicates that the DAO is involved in making loans that are
denominated in cryptocurrencies. These loans may involve collateral that is a traditional
asset or digital asset and the loans may be made to individual for real-world purposes.
 Decentralized exchanges and automated market makers indicates that the DAO is
involved in a DEX or AMM. A DEX is a digital currency exchange that allows users to buy
crypto through direct, peer-to-peer cryptocurrency transactions, all over an online platform
without an intermediary. An AMM is a type of DEX protocol that automates the process of
pricing and matching orders on the exchange, typically using an algorithm to determine the
prices at which buyers and sellers can trade assets. This means that users can purchase and
sell crypto assets in a trustless, peer-to-peer fashion without needing to rely on a custodian
or other third party.
 Derivatives, leverage, and margin trading indicates that the DAO is involved in some
type of more advanced financial product or service such as derivatives trading in which digital
asset like a perpetual derives its value from some other digital assets.
 Insurance and risk management indicates that the DAO is involved in the insurance or
risk management business. This functionality can vary widely from DAO members deciding
which insurance claims are valid to risk modeling platforms for quants controlled by a DAO.
3

---

## Page 50

 Liquidity staking and yield farming indicates that the DAO offers liquidity staking
and/or yield farming. Liquidity staking is the process of staking tokens in pools to earn
rewards in return. Yield farming is a method of earning rewards (i.e., interest) by depositing
your cryptocurrency into a pool with other users. In most cases, the pooled funds are used to
carry out other decentralized finance services via smart contracts actions such as borrowing
or lending.
 Payments indicates that the DAO is involved in transactions associated with various pay-
ment means and card schemes such as providing solutions to interconnect with traditional
banks or payment service providers.
 Stablecoin indicates that the DAO has its own stablecoin, which is a cryptocurrency de-
signed to trade at par with a reference asset (e.g., the US dollar).
DAO infrastructure functionalities
 Data and identity indicates that the DAO is involved in a decentralized market to publish,
discover, and use data or is involved in confirming identity or transactions.
 Mutlichain indicates that the DAO is involved in building some type of infrastructure for
blockchain users that enables cross-chain activity (e.g., transfers or communication)
 Tooling indicates that the DAO is involved in providing some type of tooling for DAOs
whether this be tools to automate traditional organizational activities like risk management
and expense management or tools for DAO-specific services like decentralized voting and
crowdfunding.
DAO web3 functionalities
 Asset management/crowdfunded investments indicates that the DAO is a blockchain
alligned group of investors that team up to buy goods whether they be culturally significant
investments like NFTs or more traditional business investments.
 Entrepreneurial accelerators indicates that the DAO is involved in funding early stage
blockchain and Web3 ventures.
4

---

## Page 51

 Gaming indicates that the DAO is involved in development, marketing, and monetization
of video games with a Web3 component.
 Media and content curationindicates that the DAO is involved in the media or publishing
business and/or provides some type of curation and storytelling to convey certain information
or value to Web3 users.
 NFTs indicates that the DAO has some NFT aspect to it.
 Porting assets between Web3 and real world indicates that the DAO is involved in
porting assets or providing provenance for real-world assets in the Web3 space with the most
common applications so far being art and real estate.
 Public goods indicates that the DAO is involved in the efficient distribution of donations
to fund a project or service that will benefit the well-being of all members of a society (e.g.,
Web3 education).
 Single-purpose DAOs indicates that the DAO has a single purpose (e.g., buying the Con-
stitution).
 Social clubs indicates that the DAO has a social aspect and that part of tokenholders
benefits are the entertainment, social interaction, and positive vibes.
 Talent and gig work indicates that the DAO is involved in providing either technical or
non-technical talent and advisory services for either real-world or Web3 organizations.
 Virtual and augmented reality indicates that the DAO is involved in some type of experi-
ence in which users can participate in or create their own shared virtual- or augmented-reality
world.
DAO voting mechanisms
 Simple quorum is the most basic mechanism used for decision-making in DAOs, and it
requires that the majority of tokens vote in favor of a proposal for it to pass. One token is
equivalent to one vote and the overall quorum is defined by the total token supply.
 Relative quorum is similar to a simple quorum in that it requires the majority of tokens
vote in favor of a proposal for it to pass and that one token is equivalent to one vote. But
5

---

## Page 52

the overall quorum is defined relative to the total number of tokens that actually vote. Even
if only one token holder votes, this is still a quorum.
 Relative quorum voting with differential is a relative quorum with the additional re-
quirement that the differences between the yes votes and the no votes have a certain percent-
age differential. For example, if 20% of the tokens vote, and the required differential is 15%,
and 6% of the total tokens votes “no” then, the proposal would fail, because the differential
would require that the threshold to define the quorum is raised to 21%, because 6% no plus
at least 15% more yes = 21% quorum.
 Supermajority voting stipulates a higher percentage, usually between 67% and 90% for a
proposal to pass. This higher threshold requirement means it is often very difficult to pass a
proposal.
 Weighted voting or other reputation-based voting takes into account the contributions
a voter made rather than the capital the voter provided. Common considerations include
how long the tokens have been held for or give a higher weight to certain member tokens
based on their history of participation in the DAO. Reverse escrow voting also falls into this
category. Reverse escrow voting is a process whereby holders of vesting tokens are allowed
to participate in governance, but with their voting weight reduced using a multiplier applied
to their token balances.
 Quadratic voting allows would-be voters to buy tokens and acquire greater voting power.
The voting power increases by the square of the number of tokens a voter has. So, while
the representative impact of a single vote is one, it increases to four for two votes and nine
for three votes. This system comes with its pros and cons: It discourages people without a
vested interest from voting on an issue and gives a minority a more prominent voice on issues
they are passionate about.
 Conviction voting leads to the approval of proposals based on the aggregated preference
of community members, expressed continuously. This means token holders are continuously
asserting their preference for which proposals they would like to see approved, rather than
casting votes one time. A member can change their preference at any time, but the longer
6

---

## Page 53

they keep their preference for the same proposal, the stronger their conviction gets. This
added conviction gives long-standing community members with consistent preferences more
influence than short-term participants potentially trying to influence a single vote.
 Lazy consensus assumes that all improvement proposals are legitimate unless proven other-
wise. Each proposal once formalized is put in a queue and schedule for an on-chain transaction
that will execute by default at a pre-specified date, unless it is specifically challenges by a
member. In practice, this means that uncontroversial decisions can be made quickly and
without costs or voter exhaustion, but more divisive proposals can be challenged in when
necessary.
 Voting requirements vary by content This indicates that the DAO stipulates different
voting requirements based on the content of the proposal. For example, supermajority to
remove a member of the DAO council or conviction voting for the DAO budget.
DAO voting process
 Ideas start via informal discussion (e.g., on Discord) Before bringing a proposal
forward, members are encouraged to post their proposal idea for discussion either in a Forum
chat or on Telegram or Discord for members to review and comment on.
 Requirements to create a formal proposal (e.g., hold X tokens) Requirements to
make a formal proposal vary. A common requirement is to hold a certain number of tokens.
Typically, the number is so large that the individual putting forward the formal proposal has
an outsized interest (e.g., a founder or an early investor) rather than an ordinary community
member. Other common requirements include a minimum number of comments during the
idea stage or receiving support from the majority in a temperature check vote at the idea
stage. In some DAOs, this is a point at which the proposal must be reviewed by a governance
subDAO or elected representatives to ensure it meets some requirement.
 Uniform, transparent templates for proposals This indicates that the DAO has pro-
posal templates that members should adopt as a standard. While there has yet to be any
uniform templates across all DAOs, some DAOs provide their own templates to promote
7

---

## Page 54

transparency and ensure token holders have sufficient information to make an informed de-
cision.
 Requires executable code in proposal (i.e., no developer help) indicates that the
DAO requires the community member proposing the change to write the code themselves
that implements the change on-chain.
 Off-chain gasless vote for signaling (e.g., Snapshot) indicates that the DAO uses off-
chain gasless voting for signaling purposes. Snapshot and Tally are two popular DAO tooling
companies, but some DAOs have created their own bespoke gasless voting systems.
 Quorum requirement (e.g., 5% of token supply) means that the DAO has a minimum
acceptable number of tokens that need to vote to make the proceedings of the vote valid.
This requirement is typically meant to ensure there is sufficient representation before any
changes are made
 Votes can be delegated to individuals or DAOs indicates that users can allow another
entity to vote tokens on their behalf.
DAO organizational design features
 Includes subDAOs indicates that the DAO has subDAOs which can either be like sub-
sidiaries in a corporation or like business lines in a corporation. Typically, the subDAOs
operate with autonomy while remaining strategically and monetarily aligned with the main
DAO.
 Includes appointed representatives or board-like councils indicates that the DAO has
a structure that follows some type of hierarchical management model, in which representatives
are either appointed or elected.
 Includes multi-year, token-vesting schedule for key members
 Provides incentives to vote (e.g., increased rewards) provides some type of monetary
incentive to vote such as an increased yield or issuance of additional governance tokens.
 Provides proof of attendance badges POAP, meaning Proof of Attendance Protocol,
refers to an NFT (non-fungible token) that is given to participants in an event, course, or
8

---

## Page 55

activity. Essentially, it is a badge of honor or recognition for having been present or having
participated in an online or in-real-life event.
DAO security features
 Delay or timelock before implementation indicates that the DAO has a delay period
(e.g., 48 hours) before the change is implemented on-chain.
 Multisig before implementation indicates that the DAO requires a certain number of
authorized multiple signers to sign-off on the implementation of a proposal before it can go
into effect.
 Core or developer team can override indicates that the core or developer team can veto
or override a proposal even if it passes all other hurdles.
 Feasibility study (e.g., technical, financial, security) indicates that the community
requires a feasibility study for any variety of reasons. For example, have the code audited
before implementation for security reasons. Or estimate the expected financial returns from
implementing a proposal.
 Safesnap allows trustless, on-chain execution based on the outcome of off-chain votes, via a
Gnosis Safe module connected to Reality.eth (an escalation-game-based oracle). This means
teams can continue to secure their assets in a Gnosis Safe, avoid needing gas for on-chain
voting, and ease into decentralization.
Governance systems modeled after
 Aragon is a tooling company for DAOs that provides modular systems for DAO developers
to use when composing their organization. Aragon created a system that divides governing
power into three branches: legislative, executive, and judicial. Aragon Govern is a smart
contract that acts as a DAO’s executive branch, responsible for enacting the will of the
community as expressed by the legislature. The legislative role is performed by Aragon
Voice, where token holders may make proposals and vote on them. If there is a disagreement
between the executive and legislative branch, then the digital dispute is resolved in Aragon
9

---

## Page 56

Court. In “digital court,” subjective disputes are handled just as in a traditional court system
with human judgement, except here jurors scroll in their dashboard and vote, thus completing
actions to earn special tokens. Aragon is often used to implement Lazy Consensus voting
within DAOs.
 Governor Bravo indicates that the DAO uses a system based on Compound’s Governor
Alpha or Governor Bravo (the upgraded version) for its governance. This means that the
governance runs on-chain, so that there is no way for an admin to change smart contract
parameters without an on-chain vote. The main features are that anyone with enough votes
can propose a change to the protocol. Any token holder can cast a token-weighted vote on
a proposal. Any tokenholder can assign their vote to anyone including themselves. Anyone
can cancel a proposal if the proposer stops having enough votes. Once a proposal passes,
anyone can queue the proposal in the timelock and after the timelock expires the proposal is
executed on-chain.
Real outcomes
 DEX volume is daily trading volume on a $ BTC-equivalent basis for comparability across
decnetralized exchanges and protocols. Data is pulled from Coingecko for all decentralized
exchanges or DeFi protocols with swap functionality. We then match by name those that are
governed by a DAO.
 Hack or scam is an indicator variable equal to one marking the date of a known security
breaches. To identify security breaches, we use an natural language processing (NLP) algo-
rithm to identify articles likely to have information about security breaches from Messari’s
crypto newsfeed, which mostly covers prominent crypto outlets like Blockworks, CoinDesk,
Cointelegraph, Crypto News, the Daily HODL, Decrypt, etc. . . This initial screen is based on
a dictionary that includes security breach keywords such as “attack,” “breach,” “butchering,”
”cyberattack,” “hacker,” “malicious,” “scam,” “security,” “spoofing,” etc . . . as well as dic-
tionary for litigious words in finance developed by ?. We supplement this crypt-news-based
data with Molly White’s “Web3 is Going Just Great” archive which is a weekly Substack
10

---

## Page 57

chronicling exploits in Web3.
 Social metrics is the log of a normalized number of daily social media users/followers for
a DAO. The social media outlets, we pull data from include X (formerly known as Twitter),
Reddit, and Telegram. For each social media outlet, we first normalize the quantity of users
to account for differences in popularity across platforms. If more than one series is available
for a particular DAO, we take the maximum across the multiple series. We pull this from
a variety of sources that puport to track it (e.g., X, Messari, and Coingecko). If days are
missing between observations, we interpolate between days.
11

---

## Page 58

C List of DAOs
12

---

## Page 59

Table C.1.
DAOs in Sample
This table lists the DAOs in our sample as well as the digital asset ticker and website.
DAO name Ticker DAO website
(1) (2) (3)
earthfund 1EARTH https://www.earthfund.io/
1inch dao 1INCH https://1inch.exchange/
aave AAVE https://aave.com/
abachi ABI https://www.abachi.io/
akropolis AKRO https://www.akropolis.io/
alchemix dao ALCX https://app.alchemix.fi/
aladdin dao ALD https://aladdin.club/
alpaca finance dao ALPACA https://www.alpacafinance.org/
alpha dao ALPHA https://alpha-dao.com/
amp dao AMP https://amptoken.org/
angle labs ANGLE https://app.angle.money/
angle protocol ANGLE https://www.angle.money/
yuga labs APE https://www.yugalabs.io/
ap wine dao APW https://www.apwine.fi/
armorfi/ease ARMOR https://ease.org/
airswap AST https://www.airswap.io/
baconcoin BACON https://www.baconcoin.com/
badger dao BADGER https://app.badger.finance/
balancer dao BAL https://balancer.finance/
bankless dao BANK https://www.bankless.community/
beanstalkfarmseth BEAN https://bean.money/
beethoven X BEETS https://beets.fi/
bifi BIFI https://bifi.finance/
bit dao BIT https://www.bitdao.io/
bancor dao BNT https://home.bancor.network/
barnbridge BOND https://barnbridge.com/
boring dao BOR https://www.boringdao.com/
b.protocol dao BPRO https://www.bprotocol.org/
basis dollar BSD https://www.basis.io/
biswap BSW https://biswap.org/
redactedcarteleth BTRFLY https://redacted.finance/
braintrust BTRST https://www.usebraintrust.com/
pancakeswap CAKE https://pancakeswap.finance/
celer network CELR https://www.celer.network/
city dao CITY https://www.citydao.io/
credmark CMK https://www.credmark.com/
candle CNDL https://candlelabs.org/
developer dao CODE https://www.developerdao.com/
compoud dao COMP https://compound.finance/
13

---

## Page 60

Table C.2.
DAOs in Sample (Cont.)
This table continues the DAOs in our sample as well as the digital asset ticker and website.
DAO name Ticker DAO website
(1) (2) (3)
cryptocorgis CORGI https://cryptocorgis.co/
cream dao CREAM https://cream.finance/
curvefi CRV https://curve.fi/
cryptex/c2x CTX https://c2x.world/
primedao D2D https://www.prime.xyz/
streamreth DATA https://streamr.network/
decentral games DG https://decentral.games/
dhedge DHT https://www.dhedge.org/
dodo dao DODO https://dodoex.io/
doodles dao DOODLE https://doodles.app/
piedao DOUGH https://www.piedao.org/
drc DRC https://drcglobal.org/
dsd DSD https://dynamicsetdollar.medium.com/
dydx DYDX https://dydx.exchange/
armorfi/ease EASE https://ease.org/
elyfi ELFI https://www.elyfi.world/en
ens ENS https://ens.domains/
empty set dao ESD https://www.emptyset.finance/
euler EUL https://www.euler.finance/
harvestfinance FARM https://harvest.finance/
fei FEI https://fei.money/
forefront FF https://forefront.market/
ampleforth dao FORTH https://www.ampleforth.org/
shapeshift fox token FOX https://shapeshift.com/
frax FRAX https://frax.finance/
friends with benefits FWB https://fwb.help/
gasdao GAS https://www.gasdao.org/
gcr GCR https://globalcoinresearch.com/
gearbox GEAR https://gearbox.fi/
gelato GEL https://www.gelato.network/
goldfinch dao GFI https://goldfinch.finance/
aavegotchi GHST https://www.aavegotchi.com/
gmx GMX https://gmx.io/
gnosis dao/safe GNOSIS https://gnosis-safe.io/
gro dao token GRO https://www.gro.xyz/
the graph GRT https://thegraph.com/
gitcoin dao GTC https://gitcoin.co/
hbotprpeth HBOT https://hummingbot.org
hop protocol HOP https://hop.exchange/
idle IDLE https://idle.finance/
ilveth ILV https://illuvium.io/
indexcoop dao INDEX https://app.indexcoop.com/
14

---

## Page 61

Table C.3.
DAOs in Sample (Cont.)
This table continues the DAOs in our sample as well as the digital asset ticker and website.
DAO name Ticker DAO website
(1) (2) (3)
instadapp INST https://instadapp.io/
inverse INV https://www.inverse.finance/
juicebox dao JBX http://juicebox.fun/
klima dao KLIMA https://www.klimadao.finance/
krausehouse KRAUSE https://www.krausehouse.club/
thelanddaopropeth LAND devour.landdao.io
thelao LAO https://www.thelao.io/
lido LDO https://lido.fi/
linear DAO LINA https://linear.finance/
links dao LINKS https://linksdao.io/
tokenlon LON https://tokenlon.im/
treasure dao MAGIC https://treasure.lol/
decentraland MANA https://decentraland.org/
mask MASK https://mask.io/
merit circle MC https://www.meritcircle.io/
mclub MCLB http://app.charmverse.io
magic internet money MIM https://abracadabra.money/
alchemist dao MIST https://alchemist.farm/
makerDAO MKR https://makerdao.com/en/
moondao MOONEY https://www.moondao.com/
mstable dao MTA https://mstable.org/
indexed NDX https://indexed.finance/
nftx NFTX https://nftx.io/
nounsdao NOUNS https://nouns.wtf/
nexus mutual NXM https://nexusmutual.io/
official ocean dao OCEAN https://oceanprotocol.com/dao
origin protocol OGN https://www.originprotocol.com/
origin dollar governance OGV https://www.ousd.com/
olympus dao OHM https://www.olympusdao.finance/
mantra dao OM https://mantradao.com/
ooki OOKI https://hello.ooki.com/
optimism collective OP https://optimism.io/
opium OPIUM https://opium.network/
paladin PAL https://paladin.vote/
dopewars dao PAPER https://dopewars.gg/
pleasrdao PEEPS https://pleasr.org/
peopledaoeth PEOPLE https://www.constitutiondao.com/
perpetual protocol PERP https://perp.fi/
phonon PHONON https://phonon.network/
pickle PICKLE https://pickledao.io/
unipiloteth PILOT https://unipilot.io/
pocket network POKT https://www.pokt.network/
pooltogether POOL https://pooltogether.com/
premia PREMIA https://premia.finance/15

---

## Page 62

Table C.4.
DAOs in Sample (Cont.)
This table continues the DAOs in our sample as well as the digital asset ticker and website.
DAO name Ticker DAO website
(1) (2) (3)
paraswap dao PSP https://paraswap.io/
epns dao PUSH https://epns.io/
quickswap QUICK https://quickswap.exchange/
radicle RAD https://radicle.xyz/
reflexer RAI https://reflexer.finance/
superrare RARE https://superrare.co/
rarible dao RARI https://rarible.com/
ribbon finance RBN https://ribbon.finance
ren REN https://renproject.io/
rari RGT https://www.rari.capital/
daosquare RICE https://www.daosquare.io/
rally RLY https://rally.io/
metafactory ROBOT https://twitter.com/TheMetaFactory
rome ROME https://romedao.finance/
keeper dao ROOK https://keeperdao.com/
rocket pool RPL https://rocketpool.net/
rss3 RSS3 https://rss3.io/
saddle finance SDL https://saddle.finance/
sdt SDT https://stakedao.org/
saffron SFI https://saffron.finance/
sharkdaoeth SHARK https://sharks.wtf/
silo SILO https://www.silo.finance/
synthetix dao SNX https://synthetix.io/
opendao SOS https://www.theopendao.com/
xdai chain/gnosis chain STAKE https://docs.gnosischain.com/
stargate finance STG https://stargate.finance/
sushiswap dao SUSHI https://www.sushi.com/
stakewise SWISE https://stakewise.io/
synapse dao SYN https://synapseprotocol.com/landing
threshold T https://threshold.network/
token engineering commons TEC https://tecommons.org/
tornado cash TORN https://tornadocash.eth.link/
truefi dao TRU https://www.trusttoken.com/
trust wallet dao TWT https://community.trustwallet.com/
proof of humanity UBI https://www.proofofhumanity.id/
unlock UDT https://unlock-protocol.com/
uniswap UNI https://app.uniswap.org/
union UNN https://unn.finance/
vsp VSP https://vesper.finance/
blockzerolabs XIO https://blockzerolabs.io/
yam YAM https://yam.finance/
yfbeta YFBETA http://yfbeta.finance/
yearn finance YFI https://yearn.finance/
yup YUP https://yup.io/
0xgov ZRX https://0x.org/
16

---

## Page 63

D Additional Tables
17

---

## Page 64

Table D.1.
Robustness Check: Unadjusted Return Regressions by Individual Governance Features
This table estimates the relation between governance features and unadjusted returns from the opening date
of the proposal to the voting end. The governance features are grouped into the subindex components: in-
clusive, restrictive, and secure. Year, geographic location, and DAO type fixed effects are included. Controls
include DAO age, an indicator for an early proposal, vote duration, and the detailed industry characteriza-
tion. Robust standard error are reported in parantheses and significance at the 10 percent, 5 percent and 1
percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Unadjusted returns on proposal votes
(1) (2) (3) (4) (5)
Inclusive governance features
Uniform, transparent templates for proposals -0.323*** -0.055 -0.060
(0.120) (0.106) (0.125)
Off-chain gasless vote for signaling 0.316*** 0.412*** 0.599***
(0.119) (0.120) (0.167)
Votes can be delegated to individuals or DAOs 0.163** 0.606*** 0.643***
(0.077) (0.122) (0.153)
Provides incentives to vote 0.297 0.665*** 1.769***
(0.248) (0.249) (0.388)
Provides proof of attendance badges 0.241 1.566*** 2.057***
(0.295) (0.425) (0.503)
Restrictive governance features
Requirements to create a formal proposal 0.536*** 0.356*** 0.561***
(0.111) (0.093) (0.183)
Requires executable code in proposal -0.273** -0.418** -0.797***
(0.131) (0.165) (0.218)
Quorum requirement -0.273** -0.506*** -0.616***
(0.122) (0.129) (0.238)
Relative quorum voting with differential 0.032 -1.536*** -2.570***
(0.113) (0.335) (0.543)
Supermajority voting 0.259* -0.243 -0.782***
(0.145) (0.187) (0.214)
Voting requirements vary by content -0.630*** -0.658*** -0.408**
(0.173) (0.151) (0.185)
Includes appointed representatives of board-like council -0.360*** -0.548*** -0.775***
(0.097) (0.116) (0.178)
Includes subDAOs -0.537*** -0.849*** -0.640***
(0.080) (0.134) (0.128)
Secure governance features
Delay or timelock before implementation 0.105 0.218* 0.388*
(0.114) (0.132) (0.202)
Multisig before implementation 0.208*** 0.317*** 0.793***
(0.079) (0.100) (0.174)
Core or developer team can override -0.056 0.121 0.405**
(0.082) (0.120) (0.198)
Feasibility study 0.446*** 1.214*** 1.596***
(0.167) (0.252) (0.323)
Safesnap 0.787** 1.048*** 0.564*
(0.313) (0.318) (0.315)
Fixed effects Yes Yes Yes Yes Yes
Controls No No No No Yes
Observations 8,534 8,534 8,534 8,534 8,534
R-squared 0.017 0.027 0.020 0.059 0.082

---

## Page 65

Table D.2.
Robustness Check: Unadjusted Return Regressions by Governance Indices
This table estimates the relation between governance features and unadjusted returns from the opening date
of the proposal to the voting end. The governance features are grouped into the subindex components: in-
clusive, restrictive, and secure. Year, geographic location, and DAO type fixed effects are included. Controls
include DAO age, an indicator for an early proposal, vote duration, and the detailed industry characteriza-
tion. Robust standard error are reported in parantheses and significance at the 10 percent, 5 percent and 1
percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5)
Inclusive voting features 0.033 0.260*** 0.147**
(0.032) (0.051) (0.072)
Restrictive voting features -0.220*** -0.395*** -0.381***
(0.031) (0.051) (0.061)
Secure voting features 0.180*** 0.360*** 0.395***
(0.044) (0.063) (0.090)
Fixed effects Yes Yes Yes Yes Yes
Controls No No No No Yes
Observations 8,534 8,534 8,534 8,534 8,534
R-squared 0.011 0.016 0.016 0.029 0.053

---

## Page 66

Table D.3.
Robustness Check: Unadjusted Return Regressions by Decentralized Governance Index
This table estimates the relation between decentralized governance index and unadjusted returns from the
opening date of the proposal to the voting end. The governance features are grouped into a single index
defined as inclusive less restrictive plus secure features. Year, geographic location, and DAO type fixed
effects are included. Controls include DAO age, an indicator for an early proposal, vote duration, and the
detailed industry characterization. Robust standard error are reported in parantheses and significance at
the 10 percent, 5 percent and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5) (6) (7) (8)
Decentralized governance index 0.300*** 0.257***
(0.042) (0.048)
Low index -0.386*** 0.036
(0.070) (0.093)
Mid-range index 0.330*** 0.083
(0.088) (0.114)
High index 0.957*** 0.759***
(0.205) (0.230)
Fixed effects Yes Yes Yes Yes Yes Yes Yes
Controls No Yes No Yes No Yes
Observations 8,534 8,534 8,534 8,534 8,534 8,534 8,534 8,534
R-squared 0.028 0.050 0.013 0.042 0.014 0.042 0.020 0.046

---

## Page 67

Table D.4.
Robustness Check: Monthly Returns Rather than Weekly or Proposal Returns
This table estimates the relation between decentralized governance index and unadjusted monthly returns.
The governance features are grouped into a single index defined as inclusive less restrictive plus secure
features. Robust standard error are reported in parantheses and significance at the 10 percent, 5 percent
and 1 percent levels is indicated by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted returns on proposal votes
(1) (2) (3) (4) (5) (6) (7) (8)
Decentralized governance index 0.106 0.115
(0.066) (0.075)
Low index -0.747*** -0.378
(0.278) (0.274)
Mid-range index -0.480** -0.636***
(0.199) (0.213)
High index 0.692** 0.922***
(0.315) (0.324)
Observations 2,791 2,791 2,791 2,791 2,791 2,791 2,791 2,791
R-squared 0.023 0.048 0.024 0.047 0.024 0.050 0.024 0.050

---

## Page 68

Table D.5.
Robustness Check: Return Window from Discussion Boards Rather than Vote Start
This table estimates the relation between decentralized governance index and crypto-market adjusted returns
for a subsample of proposals for which we have the start date in the discussion forums, Discord, Telegram,
etc.. The governance features are grouped into a single index defined as inclusive less restrictive plus secure
features. Year, geographic location, and DAO type fixed effects are included. Controls include DAO age, an
indicator for an early proposal, vote duration, and the detailed industry characterization. Robust standard
error are reported in parantheses and significance at the 10 percent, 5 percent and 1 percent levels is indicated
by *, **, and ***, respectively.
Dep. var. = Crypto-adjusted
discussion board returns on proposal votes
(1) (2)
Decentralized governance index 0.788*** 0.716***
(0.174) (0.175)
Fixed effects Yes Yes
Controls No Yes
Observations 1,803 1,803
R-squared 0.018 0.029

---
