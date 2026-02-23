# Wang_Yu_Sai_Sun_Nguyen_Chen_2025_UnderstandingDAOs_AnEmpiricalStudyOnGovernanceDynamics.pdf

## Page 1

2814 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
Understanding DAOs: An Empirical Study
on Governance Dynamics
Qin Wang , Member, IEEE, Guangsheng Yu , Member, IEEE, Yilin Sai , Student Member, IEEE ,
Caijun Sun , Lam Duc Nguyen , Member, IEEE, and Shiping Chen , Senior Member, IEEE
Abstract—As a typical instance of human–computer interac-
tion, the notion of decentralized autonomous organization (DAO)
represents an organization constructed by automatically executed
rules, such as via smart contracts, incorporating features of the
permissionless committee, transparent proposals, and fair con-
tributions by stakeholders. As of May 2023, DAO has impacted
over $24.3B market caps. However, there are limited studies
focused on this emerging ﬁeld. To ﬁll the gap, we start from the
ground truth by empirically studying the breadth and depth of
the DAO markets in mainstream public chain ecosystems in this
article. We dive into the most widely adoptable DAO launchpad,
Snapshot, which covers 95% of the wild DAO projects for data
collection and analysis. By integrating extensively enrolled DAOs
and corresponding data measurements, we explore statistical re-
sources from Snapshot and analyze data from 581 DAO projects,
encompassing 16 246 proposals over the course of 3+ years.
Our empirical research has uncovered a multitude of previously
unknown facts about DAOs, spanning topics such as their status,
features, performance, threats, and ways of improvement. We
have distilled these ﬁndings into a series of key insights and
takeaway messages, emphasizing their signiﬁcance. Notably, our
study is the ﬁrst of its kind to comprehensively examine the
DAO ecosystem with a focus on scale and scope of data, real-time
relevance, practical implementations, and comprehensive metrics,
addressing critical gaps in the current literature.
Index Terms —Blockchain, decentralized autonomous organi-
zation (DAO), human–computer interaction (HCI), snapshot.
I. I NTRODUCTION
D
ECENTRALIZED autonomous organizations (DAOs)
emerge with the rapid development of cryptocurrency and
blockchain. DAO is an entity thatis collaboratively managed by
on-chain participants to deploy resources, release proposals and
make decisions. The usage of DAO in governance can decen-
tralize the operation via blockchain by enabling on-chain rules
Received 23 October 2023; revised 21 November 2024 and 21 January
2025; accepted 5 February 2025. Date of publication 17 Febru ary 2025; date
of current version 2 October 2025. (Corresponding author: Qin Wang.)
Qin Wang, Yilin Sai, Lam Duc Nguyen, and Shiping Chen are with CSIRO
Data61, Sydney, NSW 2015, Australia (e-m ail: Qin.Wang@data61.csiro.au;
Yilin.Sai@data61.csiro.au; Lam.Nguye n@data61.csiro.au; Shiping.Chen@
data61.csiro.au).
Guangsheng Yu is with The University of Technology Sydney, Sydney,
NSW 2007, Australia (e-mail: Guangsheng.Yu@uts.edu.au).
Caijun Sun is with Zheliang Lab, Hangzhou, Zhejiang Province 311121,
P. R. China (e-mail: sun.cj@zhejianglab.com).
Digital Object Identiﬁ er 10.1109/TCSS.2025.3539889
TABLE I
THIS WORK VERSUS DAO STUDIES
Examples Method Target In-time Applicable Scale
[2][3][4][5] Literature review Publications Not very n/a <30
[6][7] Framework Properties n/a Priori n/a
[8][9][10] Empirical study Projects In-time Practical <22
This work Empirical study Launchpad In-time Practical >500
and activities to be t ransparent and traceable. Stakeholders are
eligible to propose, vote, and enact changes for DAO proposals.
As of May 2023, a total of 12 824 organizations have been cre-
ated. The invested funding toward these DAOs (a.k.a., treasury)
has reached up to $24.3B, while engaged members increased
531x from 13K to 6.9M members during the last 6 years
1.
Among them, 4.5M participants are active voters or proposal
makers. DAOs accordingly become a force to be reckoned with
in the Web3 space [1] and new cryptocurrency markets.
The Open Problem : Although the concept of DAOs has
gained traction in recent years, their structural development is
still in its nascent stage. One of t he primary challenges is that
DAO projects are diverse, with varying objectives and function-
alities. Some DAOs begin with a clear purpose, such as Uniswap
and Bancor, which can remain focused on serving a speciﬁc
community or users. In contrast, other DAOs may diverge from
their initial objectives. This means a DAO may begin with a
simple goal such as collecting NFTs, and then morph into a
community to attract participants (e.g., PleasrDAO), a trading
platform to trade NFTs (Opensea), or an incubator to invest
artists (BAYC). The variety of forms and outcomes can be
confusing for newcomers and experts alike in the blockchain
space. Creating a comprehensive and structural view of DAOs
is still a signiﬁcant challenge that requires further development
and reﬁnement.
Recent studies attempt to examine DAOs (cf. Table I). Sev-
eral studies (see Row 1) begin by providing an overview of
existing literature. However, due to the delay in publication,
academic works may lack current and persuasive examples of
DAO projects, leading to outdated information (equiv.in-time or
not). Other works (see Row 2) propose a high-level framework
to discuss DAO properties, but their abstracted metrics are
created before events, making them impractical (close-to-real
1Data source: https://deepdao.io/organizations. [May 2023]
© 2025 The Authors. This work is licensed under a Creative Co mmons Attribution 4.0 Licen se. For more information,
see https://creativecommons.org/licenses/by/4.0/

---

## Page 2

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2815
or applicable?). Several studies (Row 3) focus on capturing
features from real DAO projects through empirical research, but
their sample pools are often limited (resourceful or investigated
projects in large scale?). All of these efforts seem to fall short
of providing a comprehensive and up-to-date understanding of
DAOs for readers (more in Table III).
Our Attempts: To address the aforementioned shortcomings,
we have devised a unique approach to our study. After conduct-
ing thorough research, we have found that existing DAO launch-
pads and DataFeeds have amassed a wealth of information on
numerous DAO projects, including both long-standing DAOs
that have ceased operations and newly-launched ones that have
appeared within the last month. In an effort to avoid duplicating
the work of others, we have opted to omit DataFeeds and some
launchpads that have already presented analyzed data. Instead,
we are focusing our attention on a lesser-known launchpad,
namely Snapshot [11], which has compiled a signiﬁcant number
of DAOs but has yet to conduct extensive analyses on them.
The emergence of Snapshot is to overcome the issue of
high costs associated with on-chain operations due to the com-
plexity of consensus and frequent voter interactions. Snapshot
accordingly introduced an off-chain voting tool that enables
practitioners to efﬁciently acces s popular DAOs for voting,
managing, auditing, and res earching. Snapshot serves as a
launchpad that captures over 95% of in-the-wild DAO projects
(over 11 000 spaces) and offers open access to create new DAOs
that are compatible with mainstream blockchain platforms such
as Ethereum[12], Avalanche, Binance smart chain (BSC), Poly-
gon, and Solana. The ample and reliable data collected by
Snapshot on DAO communities motivate us to develop the fol-
lowing in-depth as well as comprehensive research surrounding
DAOs.
Contributions (Fig. 1):I nt h i sa r t i c l e ,w ed i v ei n t ot h eD A O
projects that are created and managed on Snapshot. We develop
the research by gradually approaching the DAO basic concept,
operating mechanism, and relevant techniques, and analyzing
the statistical data collected from Snapshot. Our work is the ﬁrst
study to strictly explore the features of DAOs, providing in-time
guidance for the following readers. Speciﬁcally, we detail our
contributions here.
1) A structural investigation on DAOs (SectionII): Intending
to be a complete study focused on DAOs, we clear the fog sur-
rounding this fuzzy term by presenting its underlying structures
(e.g., components, supportive standards), core mechanisms, and
outstanding instances. In particular, based on extensive inves-
tigation, we decouple DAO constructions (e.g., decentralized
identiﬁer, utility token, smart contract, and e-voting) and extract
a series of metrics to reﬂect the features (cf. Section II-B)
in DAO’s designs. As tokenization plays an essential role in
DAO governance (discussed in Section VI-D), we also sort out
the relevant token standards that are essential to the DAO’s
incentive. Further, we provide a short list of tools (Table III)
that well support DAO operations.
2) A comprehensive exploration on the snapshot launchpad
(Section III): We study one mainstream DAO-related gover-
nance tool, Snapshot, by summarising the features of involved
entities, running mechanisms , typical operations , and voting
Fig. 1. Overview of this Work.
TABLE II
RESULT GUIDANCE
Index Description
Project scale
Fig. 2(a) Number of registered member s in each considered DAO project.
Fig. 4(a) Number of votes of each proposal among all considered DAO projects.
Fig. 2(b) Up-to-date number of DAO projects kicked off every month.
Fig. 4(b) Duration of each proposal among all considered DAO projects.
Fig. 4(e) Languages distribution among all considered DAO projects.
Fig. 3(a) Partipantion rates with dynamic governance scale.
Fig. 3(b) V oting changes with dynamic DAO project sizes.
Infrast.
Fig. 4(g) Fraction of different blockchain networks being used for
running each considered DAO projects.
Fig. 4(h) Fraction of different IPFS addresses being used for data storage
of each proposal among all considered DAO projects.
e-Voting
Fig. 4(f) Fraction of different voting mechan isms being used for e-voting of
each proposal among all considered DAO projects.
Fig. 4(c) V oting patterns (in terms of the number of candidates and variances
& 4(d) of results) among all considered DAO projects.
Fig. 5 Number of votes of each proposal among all considered DAO projects.
Fig. 6 Clustering among all considered DAO projects.
Token
Usage
Fig. 7(a) Fraction of the usage of prevalent DAO tokens and other
self-issued tokens in the Snapshot.
Fig. 7(b) Fraction of the usage between different prevalent DAO tokens.
Fig. 7(c) Fraction of the usage between different self-issued DAO tokens.
strategies. As of Nov. 2022 2, Snapshot has registered 11K+
spaces (projects), which covers 95% in-the-wild DAOs. How-
ever, many of them are inactive with very few members or
proposals. We ignore such projects and put our focus on the
inﬂuential ones. Thus, we collect the 581 most prevalent DAO
projects that contain a total of 16 246 proposals over the span
of past 3 years. In particular, we dive into each project and
scrutinize included proposals with basic information, voting
strategy, proposal content, and voting results.
3) A solid analysis for collected data from snapshot (Sec-
tion IV): Based on extensive investigation and exploration,
we structure our experimental results from four aspects that
separately interpret the project scale, supporting infrastruc-
ture, dependent e-voting schemes, and the operational tokens
(cf. Table II). We evaluate each item by diving into multiple
subaspects. Accordingly, we study the details of DAO members
(e.g., number of participants), basic project information (project
duration, language us age, storage condition, underlying plat-
form), and voting process (voting pattern, results, distribution,
variances, token usage, meaningful contexts). With substantive
2A notable distinction between two dates : Nov. 2022 marks the conclusion
of the experiments, May 2023 repres ents both the completion of writing and
the date to which the data was updated for submission.

---

## Page 3

2816 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
evidence, we conclude seven pieces of home-taking messages
(Insights ➊ -➐ in grey banners and the tail of last page) as high-
level summaries for interested readers.
4) A series of reasonable analyses and discussions for
building better DAOs (SectionsV–VII): Existing DAO ﬁelds are
absent of rigorous studies that can deliver effective educational
guidance. We thus provide our discussions based on previ-
ous empirical efforts. Speciﬁcally, we delineate our analyses
from three dimensions. 1) Surrounding existing projects, we
study the compatible tools used for DAOs (e.g., on- and off-
chain voting, compatible coordination tools) that can maxi-
mally extend the scope of applicability and usage. 2) Diving
into each DAO constructions, we point out several unavoid-
able drawbacks (e.g., centralization, high cost) that may hin-
der the DAO progress and development. Chasing an optimal
balance-off among all distributed projects should be aligned
with concrete requirements. 3) Excavating historical failures
and the reality of today’s DAOs ( e.g., contract reliance). 4)
Exlopring how our ﬁndings can be related/reﬂected to real-
world scenarios, in particular for policy considerations. 5)
Further providing several promising directions that can be
improved in the future to ﬁt our identiﬁed four aspects in
results (e.g., multi- DAO Collaboration, the incorporation of
subDAOs).
Spotlight of our Work? We refer speciﬁcally to the depth,
scale, and real-time relevance of the empirical data used to
analyze DAOs on the Snapshot platform. While there are indeed
studies that address various aspects of DAOs, our research
differentiates itself in several key points.
1) Scale and scope of data: Our study utilizes a uniquely
large dataset from Snapshot, covering over 11,000 DAO
projects. This scale allows us to provide a more compre-
hensive and detailed analysis than most existing studies.
2) Real-time relevance: We ensure that our data reﬂects
the most current developments in the DAO space, which
is critical given the rapid evolution of blockchain tech-
nologies. This aspect of our research offers more up-
to-date insights compared with studies that may rely on
older data.
3) Focus on practical implementation: Our research goes
beyond theoretical frameworks to explore practical impli-
cations and applications, particularly how DAOs operate
on modern blockchain platforms and interact with on-
chain governance mechanisms.
4) Comprehensive metrics: We introduce new metrics for
evaluating DAOs that have not been systematically ex-
plored in previous research, such as the analysis of
governance structures, tokenomics, and the inﬂuence of
technological advancements on DAO operations.
Key Takeaways. The rapid growth and widespread adoption
of DAOs have brought about signiﬁcant changes in the way
organizations are structured and governed. On the positive side,
we observe that DAO participation and usage are distributed,
application and proposal topics are diversiﬁed, and execution
and decision-making are automated, which are conﬁrmed by
our empirical observations. However, on the ﬂip side, DAO
development faces inevitable challenges, including issues of
centralization, high costs, unsustainable tokenization mecha-
nisms, and immature supporting technologies (refer to Sec-
tion V for more information). All such issues are vital and
require much notice. To create a better DAO, we need to ex-
amine these issues at every level of the DAO and strive for
a healthy approach to distributed governance. This involves
developing new tokenization mechanisms that incentivize long-
term participation, ﬁnding a more fair governance structure,
and exploring alternative blockchain technologies that address
security concerns.
II. A
PPROACHING DAO
This section presents a systematic overview of DAOs. We
achieve this by breaking down the integrated components, iden-
tifying key features, reviewing the leading DAOs, and dis-
cussing underlying EIP standards and surrounding tools.
A. DAO Components
DAOs consist of various integrated components that work to-
gether to facilitate decentralized governance, decision-making,
and management. We list the major components.
1) Smart Contract: A smart contract is a piece of code
that securely runs on blockchain nodes at the same time in a
decentralized manner. Thinking of it as a black-box, both the
input and output are guaranteed synchronized upon reaching a
consensus without any assistance of trustworthy third parties.
Smart contracts are considered suitable to achieve autonomous
organizing by enabling completed self-execution once the
deﬁned condition is triggered by traceable and i mmutable
transactions. This enables real-time auditing and veriﬁcation
(e.g., [13]), hence signiﬁcantly enhancing the machine-
execution security [14]. In the context of DAOs, smart contracts
are often deployed to create multi-sig wallets for secure asset
reservation and set voting strategies for fair governance.
2) On-Chain Identiﬁer: Traditional identiﬁers that rely on
third parties are replaced with decentralized identiﬁers (DIDs)
[15] which are not issued, managed, or controlled by any central
entity. DIDs are instead managed by individuals whose prefer-
ences for data storage platforms are blockchains upon a peer-to-
peer (P2P) network. By making use of public key infrastructure
(PKI) technology to generate an asymmetric key pair that is
stored on the blockchain, DIDs can achieve globally unique,
secure, and cryptographically veriﬁable authentication services.
Typical implementations of DIDs include Ethereum address and
Ethereum name service [16].
3) Off-Chain Snapshot: Snapshot is a technique to record
the in-time status of data at a speciﬁc height of blocks. Such a
type of technique is quite important for DAO governance where
all the historical results voted by participants are recorded as
evidence, which is necessary for both on- and off-chain gover-
nance. Off-chain signatures are often used to adjust the weights
of on-chain tokens during the voting process. To achieve a
smooth collaboration, a snapshot of on-chain balances and ad-
dresses will be captured to determine voting rights, and then the
participants of community members will start to vote for DAO
proposals under the weights. In this way, on-chain transaction

---

## Page 4

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2817
fees are signiﬁcantly waived. Notably, the name of the Snapshot
platform in this article exactly comes from this technical term.
4) Stake/Governance Token: The self-controlled, and
portable DIDs can offer tamper-proof and cryptographically
secure attestations for on- chain decentralized identity. By
raising the burden on each attestation’s provenance and
validity to be securely proved, at the same time, easing the
validation process, DIDs become suitable for implementing
wallet services in which stakes and utility tokens can be
securely stored. Stakes refer to the tokens that a holder can
deposit in the system. The more stakes a holder provides,
the higher conﬁdence he will have in operating consensus
procedures (e.g., proof-of-stak e). In contrast, utility tokens
are designed to be used for a speciﬁc purpose, especially in a
DApp or in a game. They offer users beneﬁts such as access
to products and services. Staked tokens and utility tokens, in
most cases, are separate where the former ensures the normal
operation of systems, and the latter is used for governance [17]
and votes in the context of DAO. In this sense, communities
sometimes equivalently use the name of governance token .
Besides, the staked tokens can be further used to establish an
on-chain reputation, which is primarily to give corresponding
credits to individuals frequently participating in DAOs.
5) Reputation Mechanism: Reputation is a crucial element
in maintaining trust and promoting collaboration within DAOs.
It serves as a measure of a member’s contributions, determining
their level of inﬂuence. Members can earn a reputation by ac-
tively participating in governance decisions, providing liquidity
to a protocol, or contributing to ongoing projects. The more a
member contributes to a DAO, the higher their reputation will
be. This reputation can be leveraged in various ways, such as
determining voting power in governance decisions, allocating
rewards from the organization’s treasury, or granting access to
certain resources and privileges. Typically, reputation is quan-
tiﬁed via the number of governance tokens held by a member.
6) Secure e-Voting Scheme: Although traditional e-voting
systems have been growing, they are still susceptible to manip-
ulation. One of the most critical problems is it being prone to the
Sybil attack [18] where malicious users create false identities
to vote. In the DAO space, by using DIDs and asking for an on-
chain attestation, the integrity of the e-voting process could be
improved. Staked tokens and utility tokens, which are bound
with DIDs, are also commonly used in e-voting to represent
the voting inﬂuence. Based on our investigation, existing DAO
voting schemes are based on relatively simple mechanisms such
as basic voting, single-choice voting and ranked choice voting
[cf. Fig. 4(f)], rather than complicat ed cryptographic e-V oting
systems [19].
B. DAO Features
We examine DAOs from four key perspectives: operational
mechanism (for underlying foundations/dependencies), func-
tional features (namely, processing phases), nonfunctional fea-
tures (a.k.a. advanced properties), and market performance
(equiv. real-world impact). We additionally summarise a small
portion of projects in Table III.
1) Operational Mechanism: a) Network refers to the under-
lying blockchain platform on which the DAO operates. Since
DAOs rely on self-executing contracts where the terms of the
agreement are directly written into the code, the network plays a
crucial role in determining the functionality and shape of these
smart contracts; b) Protocol/Field describes the speciﬁc usage
or application of the organization. This can range from areas
such as ﬁnance and governance to art and social impact; and
c) Governance token represents the voting power in DAO gov-
ernance. Stakeholders can thereby vote on proposals to make
decisions and allocate resources.
2) Functional Features: Based on the DAO projects on
Snapshot, we conclude that a typical lifecycle of DAOs in-
cludes the phases of create, propose, vote, and action. Specif-
ically, 1) create involves setting up t he initial conﬁgurations
of the DAO, covering not only the DAO space and related
information but also personal identiﬁers (e.g., ENS, DiD). 2)
Propose focuses on drafti ng, editing, and rel easing proposals.
Speciﬁc requirements will be applied to the proposer, such
as holding enough stakes. Vote calls for feedback and pref-
erences from community participants. Stakeholders can vote
for multiple options, mostly just for or against based on their
interest and willingness. Differ ent voting strategies will be
used to adjust the power of a voter. Further, action is to exe-
cute the decisions once reaching an agreement. Although this
phase is critical, it cannot be effectively measured. We thereby
omit it.
3) Nonfunctional Features:
1) Permissionless is a key factor to measure decentralized
governance due to its dynamic joining/leaving mecha-
nisms. Token holders can make decentralized decision-
making by voting on preferred proposals and inﬂuencing
the organization’s direction.
2) Transparency/Immutability means that all transactions
and decisions within a DAO will be transparent and can-
not be tampered with, fostering trust among members and
stakeholders.
3) Anticensorship refers to the ability to prevent stakehold-
ers from censoring the ﬂow of transactions (e.g., OFAC
compliant [20]).
4) Interoperability is the feature that allows a DAO to inter-
act and exchange data with other DAOs, enabling seam-
less integration and collaboration with various ecosys-
tems.
5) Token-Based Incentives.Token-based incentives align the
interests of stakeholders and encourage active participa-
tion. Members can earn tokens by contributing to the
organization or by staking them to support projects, re-
sulting in a more engaged community.
4) Market Performance: Market performance can be eval-
uated via quantitative metrics in multiple dimensions.
1) Treasury denotes a collective pool of funds owned and
managed by the organization’s members. Analogous to
the total value locked (TVL) in decentralized ﬁnance
(DeFi) [21], the treasury accrues over time from member
contributions and proﬁts derived from the organization’s
operations.

---

## Page 5

2818 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
TABLE III
MAINSTREAM DAOSA N D TOOLS AND DATAFEEDS
DAOs Operational Features F unctionalities Non-F unctionalities Market Performance [May 2023]
Network Protocol/Field Token
Create
Propose
Vote
Permissionless
Transparency
Anticensorship
Interoperability
Incentive
Treasury
(USD)
Holders
Proposals
Votes
Projects
Uniswap Ethereum DeFi (DEX) UNI ✓✓✓ ✓✓ ✗✗ ✓ 2.7B 363k 124 203.8k
BitDAO Ethereum DeFi (DEX) BIT ✓✓✓ ✓✓ ✗✗ ✓ 2.7B 18.5k 23 4.8k
ENS Ethereum Name Service ENS ✓✓✓ ✓✓ ✗✗ ✗ 1.1B 64.2k 60 111.8k
Gnosis Ethereum DeFi (DEX) GNO ✓✓✓ ✓✓ ✗✗ ✓ 1B 363k 124 203.8k
dYdX Ethereum DeFi (Lending) DYDX ✓✓✓ ✓✓ ✗✗ ✓ 903.5M 36.4k 26 11.1k
Stargate.Fin Ethereum Service STG ✓✓✓ ✓✓ n/a ✗ ✓ 374.8M 26.8k 47 2.2M
Lido Ethereum DeFi (Lending) LDO ✓✓✓ ✓✓ ✗✗ ✓ 352.6M 33.2k 128 42.3k
Polkadot Substrate Service DOT ✓✓✓ ✓✓ n/a ✗✗ 280.4M 1.3M 363 2.17k
Frax.Fin Ethereum Stablecoin FXS ✓✓✓ ✓✓ ✗✗ ✗ 271.3M 13.2k 276 9.04k
Aragon Ethereum Service ETH ✓✓✓ ✓✓ ✗✗ ✗ 199.1M 14.2k 606 1.03k
Curve Ethereum Stablecoin CRV ✓✓✓ ✓✓ ✗✗ ✗ 148.8M 76.8k 221 2.10k
Fei Ethereum Stablecoin TRIBE ✓✓✓ ✓✓ ✗✗ ✗ 145.8M 14.3k 161 15.1k
Decentraland Polygon NFTs MANA ✓✓✓ ✓✓ n/a ✗✗ 138.5M 308.9k 2k 94.7k
Radicle Ethereum Service RAD ✓✓✓ ✓✓ ✗✗ ✗ 126.4M 6.6k 26 686
Aave Polygon DeFi (Lending) AA VE ✓✓✓ ✓✓ n/a ✗ ✓ 124.9M 155.8k 268 527.1k
Compound Ethereum DeFi (Lending) COMP ✓✓✓ ✓✓ ✗✗ ✓ 121.5M 208.6k 169 13.4k
DXdao Polygon DeFi (DEX) DXD ✓✓✓ ✓✓ n/a ✗ ✓ 117.1M 1.4k 915 2.54k
Ribbon Ethereum DeFi (Derivative) RBN ✓✓✓ ✓✓ ✗✗ ✓ 116.3M 4.4k 31 4.75k
Synthetix Ethereum DeFi (DEX) SNX ✓✓✓ ✓✓ ✗✗ ✓ 115.3M 91.5k 569 14.6k
MangoDAO Solana DeFi (DEX) MNGO ✓✓✓ ✓✓ n/a ✗ ✓ 102.9M 36k 401 3.83k
Gitcoin Ethereum Social network GTC ✓✓✓ ✓✓ ✗✗ ✗ 92.2M 33.7k 144 70.4k
Phala Substrate Polka’s testnet PHA ✓✓✓ ✓✓ n/a ✗✗ 77.6M 3.1k 24 72
Vesta.Fin Polygon Stablecoin VSTA ✓✓✓ ✓✓ n/a ✗✗ 67.4M 256.5k 8 34.7k
JPEG’d Ethereum DeFi (Lending) JPEG ✓✓✓ ✓✓ ✗✗ ✓ 66M 5.3k 59 2.51k
Euler.Fin Ethereum DeFi (Lending) EUL ✓✓✓ ✓✓ ✗✗ ✓ 63.5M 2.6k 55 8.27k
Merit Circle Solana NFTs MC ✓✓✓ ✓✓ n/a ✗✗ 61M 8.9k 26 2.83k
SuperRare Ethereum NFTs RARE ✓✓✓ ✓✓ ✗✗ ✗ 54.1M 8.7k 17 1.23k
KeeperDAO Ethereum DeFi (MEV-extractor) ROOK ✓✓✓ ✓✓ ✗✗ ✓ 53.5M 17k 41 1.21k
MakerDAO Ethereum Stablecoin MKR ✓✓✓ ✓✓ ✗✗ ✗ 49.1M 90.9k n/a n/a
UXDProtocol Solana Stablecoin UXP ✓✓✓ ✓✓ n/a ✗✗ 49.6M 11.7k 819 3.27k
Yearn Ethereum DeFi (Lending) YFI ✓✓✓ ✓✓ ✗✗ ✓ 37.9M 54.2k 16 4.84k
Balancer Ethereum DeFi (DEX) BAL ✓✓✓ ✓✓ ✗✗ ✓ 36.1M 45k 378 82.1k
PleasrDAO Ethereum NFTs USDC ✓✓✓ ✓✓ ✗✗ ✗ 31.4M 149 54 1.02k
Sushiswap Ethereum DeFi (DEX) SUSHI ✓✓✓ ✓✓ ✗✗ ✓ 28.7M 109.1k 290 49.2k
Pangolin Polygon DeFi (DEX) PNG ✓✓✓ ✓✓ n/a ✗ ✓ 19.2M 32.5k 45 2k
1inch Ethereum DeFi (DEX) 1INCH ✓✓✓ ✓✓ ✗✗ ✓ 18.2M 87.5k 22 2.45k
Lucidao Polygon Service USDT ✓✓✓ ✓✓ n/a ✗✗ 11.8M 1.3k 6 154
Kusama Ethereum Polka’s testnet KSM ✓✓✓ ✓✓ ✗✗ ✓ 11.5M 291.3k 863 5.65k
Serum Solana DeFi (DEX) SRM ✓✓✓ ✓✓ n/a ✗ ✓ 4.5M 226.1k 52 246
Bifrost Substrate DeFi (Lending) BNC ✓✓✓ ✓✓ n/a ✗ ✓ 4M 84.7k 686 1.53k
Projects Field Note Projects Field/Coverage Note
Tools & Launchpad
Aragon Management tools
Keywords on Guide, NFT, Arts,
Treasury, Web3, DeFi, Game,
Analytics, DiD, Legal, Launcher,
Media, Governance, Reputation,
Infrastructure, Social, Dispute
Related DataFeeds
Dune Data analytic https://dune.com/home
DAOStack Management tools GraphQL Data analytic https://daostack.io
Colony Management tools Colony API Data analytic https://colony.io
Snapshot Off-chain voting platform DexTools Trading pair https://www.dextools.io
Tally On-chain voting platform DeﬁLlama DeFi TVL aggregator https://deﬁllama.com
DeepDAO Information/aggregator TokenTerminal Projects, Financial data http s://tokenterminal.com
DAOMasters Launcher/Management RootData Fundraising, Investors https://www.rootdata.com
DAOlist Information/aggregator CoinMarketCap Projects, Ranking http s://coinmarketcap.com
Mirror Publishing/Writing Zapper DAOs, NFTs, DeFi https://zapper.xyz/daos
Gnosis Safe Multisig wallets DappRadar DApps, NFTs, DeFi https://dappradar.com
IPFS Storage infrastructure DexScreener Trading pair, Price https://dexscreener.com
X Public Channel CoinGecko Project, Price https://www.coingecko.com/
☞ Source data in this paper mainly refers to DeepDA O (https://deepdao.io/organizations) [May 2023].
☞ Insights-➏ Ethereum DAOs (post-Merge) are censored due to the OFAC- compliant blocks (ME V Watch https://www.mevwatch.info).
➐ DeFi-related DAOs are incentive-compatib le as stakeholders are motivated to hold a nd use tokens to maximize their proﬁts.
2) Holders represent participants who own governance to-
kens and are therefore eligible to vote on proposals that
shape the direction of the organization. It can provide
insight into the level of participation and engagement
within the DAO.
3) Proposals are the speciﬁc documents that outline a sug-
gested course of action for the organization. These pro-
posals can be put forward by any member of the DAO.
4) Votes count for the total number of votes (equiv. deci-
sions) cast by stakeholders.
5) A Collection of Leading DAOs (Upper Table III): Based
on the aforementioned metrics, we investigate a group of (30+)
DAO projects that are currently active and operating in real-
world environments. These selected projects are highly inﬂuen-
tial within their respective co mmunities, as evidenced by their
market performance. It’s worth noting that most of the selected

---

## Page 6

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2819
Fig. 2. Project scale. (a) Number of members in different DAOs. (b) DAO
launching dates.
DAOs operate on the Ethereum blockchain [also supported by
Fig. 4(g)] and are classiﬁed as belonging to the DeFi track
[supported by Fig. 2(a)]. Additionally, DAOs are expected to
have certain essential properties such as permissionless access
and transparency, but the others possess additional qualities.
C. Supporting Standards
Recall that the standards referred to in this article are for-
matted in technical documents dedicated to on-chain program-
ming. Conventions are established by using the standards during
programming without having to reinvent the wheel, making
it easier and more efﬁcient for applications and contracts to
interact with each other. Here, we list the relevant standards
that support DAO scenarios.
EIP-20/BEP-20: Common Interfaces for fungible-tokens
(FT) [22]. Running the e-voting normally requires stakes and
utility tokens that typically implement ERC-20 on Ethereum
[22], BRC-20 on Bitcoin [23], [24],B E P - 2 0o nB S C[25],o r
similar standards on other blockchain platforms.
EIP-721/BEP-721/EIP-1155: Common Interfaces for the
non-FT (NFT) [26] and multi-token [27]. Stakes and gover-
nance tokens can also include the forms of NFTs [28], being
the voting power of e-voting or being the deposit for users
to participate in any campaigns of a DAO. BEP means the
standards of BSC (BNB Smart Chain).
EIP-4824: Common Interfaces for DAOs[29]. This standard
aims to establish conventions on matching on- and off-chain
representations of membership and proposals for DAOs by
using daoURI, an indicative reference inspired by ERC-721
[26], which enhances DAO search, disc overability, legibility,
and proposal simulation.
EIP-1202: Common Interfaces for the voting process [30].
The standard implements a range of voting functions (e.g.,
VoteCast, castVote, MultiBote) and informative functions
(voting period, eligibility crite ria, weight) t o enable on-chain
voting as well as to view voting results and set voting status.
ERC-779: Common Interfaces for DAOs [31]. Unlike other
hard forks that have altered the Ethereum protocol, the DAO
Fork is executed solely through the alteration of the state of the
DAO smart contract whereas transaction format, block struc-
ture, and protocol were not changed. It is an “irregular state
change” that was transferred ether balances from the child DAO
contracts into a speciﬁed account.
D. Surrounding Tools
Additionally, a wide variety of tools have been proposed to
ease the process of joining, launching, and managing a DAO.
We list several of them at the bottom of Table III. Besides the
launchpads that can manage DAOs, a host of providers intro-
duce their services and infrastructure [32] such as token ser-
vices (e.g., MakerDAO for maintaining the DAI stablecoin), on
and off-chain voting tools (Tally, Snapshot), treasury oversight
(TokenTerminal, Zapper), growth products, risk management
(Gnosis), task collaboration (Mirro, Colony), community plat-
forms (MolochDAO, Metagovernance), analytic tools (Dune,
RootData), operational tools (Aragon, DAOstack), wallet ser-
vices (Gnosis Safe) and legal services (LegalDAO).
III. D
IVING INTO SNAPSHOT
Snapshot is an off-chain voting system designed for DAOs
created on multiple blockchain platforms. The system has been
widely adopted by many crypto startups and companies to assist
in surveying users. Each project can create proposals for users
to poll votes by using the staked or governance tokens. All
the voting procedures are essentially feeless as the operation is
executed off-chain, avoiding costly on-chain veriﬁcation. Users
only need to connect their wallet to the launchpad and allow
the action of signing. Besides, the projects, voting proposals for
each project, and corresponding results are stored based on the
IPFS decentralized storage system [33]. The snapshot thereby
becomes a convenient tool for DAO creators to query the feed-
back from the communities. We pr ovide detailed actions for
each party.

---

## Page 7

2820 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
1) DAO creator: DAO creators are those companies or
projects that aim to use Snapshot. The creator needs to
hold a valid ENS domain and register his project on
the Snapshot launchpad by creating a proﬁle with in-
puts of detailed information such as project name, about,
website, symbol, service, network (equiv. blockchain
platforms) and contacts such as Twitter, Github and
CoinGecko.
2) Poll proposer: They can create their proposals for a spe-
ciﬁc project if he holds a sufﬁcient amount of relevant
governance tokens. In many cases, poll proposers are the
DAO-creating team members as they have enough staked
tokens and motivations to improve the protocol.
3) Users: Users can vote for each proposal based on their
preferences. All participants need to have valid accounts
with staked tokens for corresponding platforms, such as
an Ethereum address or a short name registered on ENS.
Users can add a record on accounts to allow votes to be
viewable at the connected addresses.
A. Running Mechanism
The Snapshot project roots in the technique of snapshot.T h e
snapshot technique is to record the in-time token-holding status
of all accounts and wallets on-chain at a speciﬁc block height. It
acts as the way of a camera, taking photos of the entire picture
at the moment. In this way, a stakeholder can learn information
like who has the token, how many tokens they have, etc. Owing
to the beneﬁts of transparenc y and traceability, the technique
has been applied to many crypto-events, such as airdrops for
incentive distribution and compensation for users after hacking
or attacks. Accordingly, the Snapshot project leverages such
technology to solve the problem existing in the voting pro-
cesses. It can intercept the historical data at a certain block
height and the associated holding status (e.g., accounts, tokens,
NFTs) of a certain type of token. Based on these data, the voting
weights can be reasonably assigned to individual community
members aligned with different rules.
B. Typical Operations
Based on different roles, we capture three main types of
operations. Notably, operations on Snapshot are aligned with
the DAO deployed on other launchpads.
1) Creating spaces: If a project aims to introduce decen-
tralized governance into the project, they can create a
Space in Snapshot for users to propose proposals and
perform voting processes. As discussed, a distributed
identiﬁer is required before the application. This identiﬁer
is used to connect the created unique project proﬁle. The
community (equiv.Space) is created once the basic infor-
mation is fully fulﬁlled. Importantly, setting the commu-
nity’s distribution strategy (a.k.a.,Strategy). It is written
a Javascript function that can be used to adjust the weight
of impact.
2) Proposing proposals: To submit a proposal within
the community, a member must ﬁrst comply with the
guidelines established by the community manager. For
example, in the ENS community, a user must possess at
least 10 000 ENS tokens to be eligible to create proposals.
Upon fulﬁlling these criteri a, the proposer may proceed
to draft the proposal by specifying the content, options,
and voting rules, as well as setting the start and end dates.
3) Poll/Vote: The voting process is open for the commu-
nity only if a user has governance tokens. Every project
has its unique governance tokens where a user can even
trade (buy/sell/e xchange) them on secondar y markets.
The voting process is designed in a clean and simple
style: connect to the wallet, select options, and sign with
signatures. Users can view their options, voting power,
and snapshot time for each submission of voting. All the
data is obtained from the snapshot.
C. Voting Strategy
As the most essential part of proﬁt distribution, different
strategies provide a series of methods of calculating voting
power. The strategy in Snapshot is essentially a JavaScript
function. Users can combine at most 8 strategies on every single
proposal while voting power is cumulative. Meanwhile, users
can write customized strategies according to their requirements.
At the time of writing, Snapshot has 350+ voting strategies and
ERC20-balance-of is the most adopted strategy. We list their
strategies.
1) Delegated voting: The voting power is based on a del-
egation strategy. Only permitted stakeholders have valid
impacts on the voting process.
2) Weighted voting: The voting power can be calculated
either by the single weight strategy (one-coin-one-vote)
or a quadratic strategy. The quadratic strategy weakens
the signiﬁcant inﬂuence of rich stakeholders, diminishing
the gap across different individuals.
3) Whitelist voting: The permitted stakeholders who are on
the whitelist are allowed to vote. The whitelist may either
get updated manually or by certain rules.
4) NFT voting: V oting by using NFT needs to be compatible
with ERC-721 or ERC-1155 based strategies.
IV . E
XPERIMENTS AND RESULTS
This section provides our experiments and corresponding
results. We detail our methods as follows.
Measurement Establishment: Our experiment consists of
three steps. First, we develop a crawling script, which is
deployed on AWS EC2 cloud server (m6i.32xlarge) with 128-
vCPU and 512GiB-memory, to capture all data from the
Snapshot platform. The script is designed to collect all the
information presented on the Snapshot main page and subpages
created by DAO creators, including numerical values (such
as voting results and participation scales) and context-aware
strings (such as language usage and topic classiﬁcation). All
data will be compiled into a ﬁnal CSV document. Second, we
analyze the data using Python and generate corresponding visu-
alizations. During this analysis, we sort, clean up, and classify

---

## Page 8

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2821
the metadata to obtain meaningful results. Finally, we present
our ﬁndings and provide derived insights.
Overall Statistics: Our study analyzes 16 246 proposals from
581 prominent DAO projects, u tilizing data collected from
Snapshot over a 3-year period starting from its inception in
August 2020 until November 2022. This comprehensive dataset
includes essential data ﬁelds such as pr oject title, number of
members, proposal title, status, network, IPFS address, voting
strategy, project start/end dates, block snapshots, result name,
result outcome, proposal content, and number of votes. For
clarity in presentation, our statistical results are categorized into
four key areas: project scale, infrastructure, e-voting schemes,
and token usage . A high-level overview of our ﬁndings is
systematically outlined in Table II.
A. Project Participation Scale
This section describes the scale of the considered DAO
projects in view of itsparticipating members, vote distributions
for proposals, launching dates , active proposal duration , and
language distribution. We provide details of each item.
B. Project Scale
Fig. 2(a) illustrates that the top DAO projects achieve a
scale of six orders of magnitude (millions) in terms of the
total number of members weighted by their respective proposal
counts, with the two most prominent projects, P
ANCAKESWAP
and AAVE, surpassing 7M. Note that the “others” bar represents
the aggregate weighted scale of all DAO projects ranked 16th
and beyond. This weighting by proposal count underscores the
active participation and engagement within these communities
and highlights a Pareto principle-like distribution [34], where
the majority of DAO activity is concentrated in a small subset
of the most prominent projects. When diving into each DAO
proposal, it can be found from Fig. 4(a) that the fraction of
having over 100 votes and having less than 10 votes come ﬁrst
and second, respectively. This also indicates the Pareto principle
is being complied with in the sense that a huge number of votes
are aggregated to a small portion of proposals, while there are
still a signiﬁcant number of proposals that are marginalized by
the community.
Fig. 2(b) shows that the concept of DAO appears to be ac-
cepted and realized by a broader public since Q3 2020 (align
with [32]). From then on, the Web3 supporters kept drawing
trafﬁc to the DAO community. It turns out that a peak arose from
Nov 2021 to Jan 2022 in regard to the number of projects being
kicked off during the period (along with the booming of DeFi
and NFT). It can also be found that the average monthly number
of new projects is much higher than that before the peak, which
indicates a milestone in the development of DAO communities.
According to Fig.4(b), the duration of each proposal is found to
be within a week, which is matched with the duration of many
real-world election campaigns. Fig. 4(e) shows that English is
the most popular language used in the proposals, accounting for
75.1% of the proposals among all considered DAO projects in
our collection. Chinese comes second with a fraction of 4.3%,
followed by Germany (2.9%), Korean (1.8%), Italian (1.5%),
Fig. 3. Governance dynamics. (a) Governance scale. (b) DAO project size.
and French (1.4%). All the rest of the languages are categorized
in “others”, accounting for 12.9% of the proposals. The usage
of languages can indi rectly reﬂect the nationality distribution
of participating members.
C. Project Scale Change
We further explore how governance models scale changes
with the size of the DAO and its treasury (Fig. 3).
Fig. 3(a) reveals signiﬁcant variab ility in participation rates
across DAO projects, as indicated by th e wide interquartile
ranges (IQRs) for some projects. While the mean participation
rate (represented by the red dots) highlights the overall engage-
ment level, the presence of num erous outliers (black circles)
suggests that certain proposals either attracted unusually high
or low participation. This variability underlines challenges in
sustaining consistent engagement across governance decisions.
Furthermore, the box plot demonstrates that some DAOs expe-
rience centralized participation patterns, which could hinder the
democratic potential of decentralized organizations.
Fig. 3(b) on the right, illustrating the relationship between
the size of DAOs (number of members) and governance par-
ticipation (number of votes), shows an overall trend of in-
creasing votes with larger membership bases. The exponential
trend line suggests that governance participation scales nonlin-
early, with larger DAOs experiencing disproportionately higher
governance activity. However, this pattern may also reﬂect in-
creasing centralization of voting power or varying engagement

---

## Page 9

2822 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
Fig. 4. Snapshot empirical results in multidim ensions. (a) Number of votes of each proposal. (b) D uration of each proposal. (c) Proposal voting varia nces.
(d) Project voting variances. (e) Language distribution. (f) Fraction of e-v oting schemes. (g) Fraction of block chains. (h) Fraction of IPFS storag e.
strategies employed by larger DAOs. The absence of extreme
outliers improves the clarity of this relationship, reinforcing
the signiﬁcance of size as a factor inﬂuencing governance
dynamics.
Our observations emphasize the need for robust mechanisms
to foster equitable participation in governance processes, espe-
cially as DAOs scale in size. Additionally, strategies to mitigate
voter apathy and ensure fair representation of diverse member
voices are critical for the long-term sustainability of decentral-
ized governance.
Insight-➊ : The DAO community has experienced sig-
niﬁcant growth across numerous countries and regions,
maintaining high usage rates. However, the distribution
of members often adheres to the Pareto Principle (the 80-
20 rule [35]), indicating a concentration that could lead
to unintended centralization. This phenomenon warrants
careful monitoring and intervention to preserve the de-
centralized ethos of DAOs.
D. Infrastructure
This section describes the information of IPFS network and
blockchain platform infrastructure being used by the considered
DAO projects or proposals, followed by details.
It is found from Fig. 4(g) that Ethereum Mainnet [12] is the
most popular blockchain platform used by the considered DAO
projects in our collection, accounting for a fraction of 65.4%.
Binance Smart Chain Mainnet comes second with a fraction of
14.3%, followed by Polygon Mainnet (8.9%), Fantom Opera
(3.3%), Arbitrum One (1.4%), and Gnosis Chain (1.4%). All
the other platforms are categorized in “Others”, accounting for
5.2% of the projects. In regard to the decentralized IPFS data
storage as illustrated in Fig. 4(h), the “#bafkrei” is used the
most often, accounting for 23.7% among all the proposals. This
implies that 76.3% of the DAO proposals (starting with “#QM”)
are still using tools such as nmkr.io or other minting platforms
that use the outdated version of content identiﬁer (CIDv0 [36],
Base58) which is more expensive and less effective for IPFS
data storage. This deserves a caution that there are lack of
motivation for DAO proposers or developers to upgrade their
infrastructure, which might degrade the capacity and efﬁciency
of data storage to the DAO community if IPFS would only
completely root for CIDv1 [36] in the future.
Insight-➋ : It is fortunate that the platforms used by
existing DAO proposals and projects are diversiﬁed. On
the contrary, the insufﬁcient motivation of upgrading
the content identiﬁer version of IPFS data storage may
degrade the capacity and efﬁciency of the community.
E. E-Voting Scheme
This section describes the number of valid votes and the
fraction of different e-voting schemes used in the considered
DAO projects and proposals, and different voting patterns .
1) E-Voting Schemes: It is found from Fig. 4(f) that the
e-voting schemes can be categorized into the following ranks.
The single-choice voting is the dominant strategy that accounts
for 83.0% among all reviewed strategies, followed by the ba-
sic voting strategy with a fraction of 7.2%. Conversely, the
weighted voting (5.2%), approval voting (1.7%), quadratic vot-
ing (1.6%), and ranked choice voting (1.3%) strategies are
rarely adopted by participating members in comparison. The
results demonstrate that single-choice voting is the most popular
strategy. This indicates that DAO users still prefer to adopt the

---

## Page 10

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2823
Fig. 5. V oting patterns with candidate size.
simplest way of polling. Although an intuitive concern comes
that the single-choice voting and basic voting strategies may
result in Matthew effect [37] in vote distribution, the results
show that most proposal advisors ignore such drawbacks in
practice.
2) Voting Patterns: Fig. 5 reveals that binary voting is
the most prevalent pattern in our dataset, with over 10,000
proposals, followed by ternary and quaternary voting patterns.
Conversely, Fig. 4(c) and 4(d) analyze the variances in voting
results for individual proposals and projects, respectively, to
determine the extent of agr eement or opposition within the
community. From Fig. 4(c), it is observed that more than 60%
of the proposals exhibit a high variance, exceeding 40, sug-
gesting that e-voting within current DAO communities tends
to produce predominantly one-sided outcomes. However, at the
project level, the incidence of signiﬁcant variance is consider-
ably lower, at only 9.2%. Balanced results constitute 38.5% of
cases, while 52.3% of projects show an average variance be-
tween 10 and 20, indicating that one-sided voting outcomes are
relatively rare when viewed across multiple projects. Typically,
although individual projects may experience several one-sided
voting instances, the majority are more likely to yield balanced
outcomes.
Here, we try to explain the reason that causes the variance
differences between proposal- and project-level voting results.
As observed in Fig. 5, most of the voting results are binary-
based patterns, whose corresponding variances are naturally
very large. This will signiﬁcantly increase the result (value)
of proposal-level variances as each proposal is merely estab-
lished on top of one voting pattern. In contrast, the results
in project-level variances are relatively balanced because each
project contains a series of proposals that may moderate the
extreme value caused by binary results. In our view, one-
sided results do not necessarily mean “bad”, which instead
indicate that DAO members tend to make an instant decision
without signiﬁcant debates. A balanced result shows that DAO
communities are difﬁcult to reach an agreement among the
participants. However, on the ﬂip side, this exactly reﬂects
the so-claimed properties of decentralization or democracy.
Controversial arguments indicate that deﬁning what is a nor-
mal or healthy voting result is complicated in an unclear
context.
Fig. 6. Clustering among all considered DAO projects.
Insight-➌ : Current e-voting patterns and results in
many DAO projects illustra te both the decentralization
and democratic nature of DAO communities. However,
these systems often struggle to reach consensus effec-
tively, contrasting with the efﬁciency seen in traditional
e-voting systems. This challenge highlights a fundamen-
tal weakness in ﬂat organizational structures, where the
trade-off between ﬂat and hierarchical models continues
to be a subject of debate.
3) Clustering the Voting Contexts: The clustering among
all considered DAO projects is investigated in Fig. 6. We apply
K-means clustering [38] to analyze and categorize different
DAO projects based on the textual features extracted from their
titles. As the titles are strings , we ﬁrst preproces s the dataset
by transforming the textual data into numerical representations,
such as term frequency-inverse document frequency (TF-IDF)
or word embeddings.
To effectively visualize and interpret the resulting clusters,
we then utilize two widely-used dimensionality reduction tech-
niques, namely principal component analysis (PCA) [39] and
t-distributed Stochastic neighbor embedding (t-SNE)[40].P C A
is a linear technique that identiﬁes directions of maximum
variance, transforming the high-dimensional data into a one-
dimensional representation (pca-one). This provides an intuitive
visualization and interpretation of the resulting clusters, pre-
serving as much of the original variance as possible. Conversely,
t-SNE is a nonlinear technique that preserves the local structure
of the data, capturing complex patterns and relationships. We
use t-SNE to generate a two-dimensional representation (tsne-
2-D-one) of the DAO project titles, enabling a detailed examina-
tion of clusters, substructures, and intricate relationships among
the projects. By conducting both, we obtain a richer understand-
ing of the underlying patterns and relationships among different
DAOs based on their titles.
We cluster the projects into 10 labels (cf. Fig. 6) along with
brief summaries as presented below.
Label 0 ■ <Protocol Upgrades and Implementations >:
This category focuses on proposals related to upgrades, im-
plementations, and enhancements of decentralized protocols
and platforms. Topics include network upgrades, smart contract
implementations, and consensus mechanism improvements.

---

## Page 11

2824 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
Label 1■<Governance and Decision-Making>: This cate-
gory primarily covers various proposals and discussions related
to governance, management, and decision-making processes
within DAOs and other decentralized organizations. Topics in-
clude voting systems, governance structure, and various aspects
of administration.
Label 2■<Tokenomics, Staking, and Rewards>: This cate-
gory is focused on tokenomics, staking, rewards, and incentives
for decentralized platforms and protocols. Discussions and pro-
posals revolve around token distribution, staking mechanisms,
yield farming, liquidity provision, and other related ﬁnancial
aspects.
Label 3 ■ <Development and Technical Improvements >:
This category deals with discussions and proposals related to
the development, improvement, and maintenance of decentral-
ized platforms, protocols, and applications. Topics include tech-
nical improvements, bug ﬁxes, new features, and other aspects
of software development.
Label 4 ■ <Marketing, Branding, and Community
Building>: This category covers marketing, branding, and
community-building efforts within the decentralized ecosys-
tem. Topics include community engagement, social media pres-
ence, promotional campaigns, partnerships, and collaborations
to increase visibility and adoption.
Label 5 ■ <Budgets, Funding, and Financial Man-
agement>: This category focuses on various budgets, fund-
ing, and ﬁnancial aspects related to DAOs and projects.
Discussions and proposals revolve around allocating re-
sources, managing expenses, funding proposals, and ﬁnancial
matters.
Label 6 ■ <Project-related Requests and Resources >:
This category encompasses project-related requests, includ-
ing requests for resources, support, or collaboration from
communities. Topics include pr oject funding, hi ring, develop-
ment services, and resources needed to move a project forward.
Label 7■<Asset Management and Acquisitions>: This cat-
egory deals with asset management, acquisitions, and purchases
within the decentralized ecosystem. Topics include buying and
selling NFTs, real estate in virtual worlds, and other digital
assets, as well as decisions regarding strategic investments or
acquisitions.
Label 8 ■ <Contests, Compe titions, and Events >: This
category is focused on contests, competiti ons, programs, and
events within the decentralized ecosystem. Discussions and
proposals revolve around voting on the outcomes of various
competitions, participating in events or programs, and other
community engagement activities.
Label 9 ■ <Activation and Continuation >: This category
covers the activation and continuation of individuals or projects
within decentralized organizations. Topics include activating
new members, continuing or ending ongoing initiatives, ad-
justing reward structures, and other decisions related to the
management of human resources and projects.
4) Relations Between Labels: Evidence of correspondence
between the label descriptions and the clustering outcomes can
be observed in Fig. 6 through select examples. Label 0 ■
adjacent to Label 3 ■ signiﬁes the close relationship between
executing protocol upgrades and speciﬁc development and
technical improvements. Label 4 ■ encompasses marketing-
related events and is closely linked with ﬁnancial management
represented by Label 5■ and asset management represented by
Label 7 ■. Label 8 ■, concentrating on contest events, stems
from the initiatives and activation characterized by Label 9 ■.
Simultaneously, both Label 8 ■ and Label 9 ■ intersect with
Label 2 ■, highlighting that the activation and continuation
of individuals or projects within DAOs necessitate extensive
discussions about adopting appropriate token incentives. Con-
versely, Label 1 ■ and Label 2 ■, positioned at the center,
validate that the governance and tokenomics components form
the core of DAOs, aligning with the introduction presented in
Section II-A.
Insight-➍ : DAOs exhibit a broad range of voting
contexts, covering topics from budget allocations and
project funding to community events and hiring deci-
sions. This diversity showcases the potential for de-
centralized governance to empower communities and
drive innovation across various domains. However, chal-
lenges such as voter apathy and the concentration of
power among a few token holders highlight the need
for more robust, inclusive, and accessible governance
mechanisms that encourage broader participation and
ensure a sustainable future for DAOs.
F . DAO Tokens Usage
This section describes the usage of differentDAO tokensused
in the considered DAO projects or proposals.
Fig. 7(a) reveals that 97.1% of the DAO projects use self-
issued (equiv. customized) tokens or minor tokens, while only
2.9% of the DAO projects use the mainstream tokens in-
cluding USDT (54.2%), ETH (24.6%), USDC (18.3%), and
ENS (2.9%), as shown in Fig. 7(b). The results reveal a risk
of the current usage of tokens in DAO spaces. The major-
ity stays on using self-issued tokens or minor tokens which
are much less stable and have much fewer merits than the
prevalent tokens. Unhealthy opportunistic behaviors could be
apparently realized, which is adverse to leveraging smooth
and efﬁcient governance. Across the DAOs using self-issued
tokens, the top 3 are STALK, HUWA, and PEOPLE whereas
HUWA is tailored speciﬁcally to internet memes compared
with STALK facilitating a ﬁat stablecoin protocol and PEOPLE
aiming to develop the subDAOs, as shown in Fig. 7(c). This
implies the immaturity of DAO communities and needs further
improvement.
Another interesting observation is that most customized to-
kens [over 75% among “Others” in Fig. 7(a)] are minted on
the top of Ethereum ecosystems, which means they are in-
triguingly designed in forms of ERC-20 tokens that are closely
relied on the development of Ethereum platforms. Similarly, the
rest of the customized tokens are created on other mainstream
public chains, such as BSC and Avalanche. Such situations
indicate a potential threat of implicit centralization caused by
oligopolistic blockchain organizations that have taken the ﬁrst-
mover advantages.

---

## Page 12

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2825
Fig. 7. Distribution of the token usage . (a) Fraction of all tokens (general).
(b) Fraction of prevalent tokens. (c ) Fraction of self-issued tokens.
Insight-➎ : Unhealthy opportunistic behaviors are still
common in DAO communities in the sense that the ma-
jority of the projects rather relies on self-issued tokens
than the apparently more valuable and stable mainstream
tokens such as USDT, ETH, etc.
V. D
ISCUSSIONS ON THREATS
This section highlights potential challenges. The analysis of
threats is largely based on empirical evidence gathered.
A. Centralization
The governance in DAOs relies prominently on the posses-
sion of stakes or utility tokens . Although it is originally ex-
pected to be core to the decentralization in DAOs, highly active
groups of participants tend to accumulate major shares of tokens
[investigated by our results Fig. 7(a) and 7(b)], hence breach-
ing the decentralization due to the concentration of e-voting
power. Beyond that, it’s disheartening to observe the growing
centralization of various aspects within DAOs. For instance,
language usage [see Fig. 4(e)], voting strategy [Fig. 4(f)], plat-
form adoption [Fig. 4(g)], and even storage [Fig. 4(h)] all seem
to be following a similar path toward centralization. This trend
has been discussed in depth in our ﬁnding Insight-➊ . Such
a phenomenon raises questions about whether we can truly
achieve the promise of decentralized governance in the long run.
To avoid centralization, DAOs could accordingly prioritize
diversity, decentralize decision-making, avoid concentration of
assets, embrace transparency, and foster community. Having a
diverse group of participants from different backgrounds and
expertise can prevent power from being concentrated in the
hands of a few. Decentralizing decision-making by allowing
all members to participate in governance and voting, through
mechanisms like quadratic voting and delegation, can prevent
the decision-making process from being controlled by a small
group. Avoiding the concentration of assets in a single wallet
or exchange can reduce the risk of a single point of failure. Em-
bracing transparency by making all decisions and transactions
publicly visible can prevent any hidden centralization from
occurring. Additionally, fostering a sense of community among
members, despite it being pretty difﬁcult, may help ensure that
everyone feels invested in the success of the organization.
B. Disunity and Fairness
DAO communities come across disagreements much more
often than a traditional organization does [cf. Fig. 7(c), also
mentioned [8], [10]]. While this reﬂects the democratic nature
of DAOs, it also highlights the potential for disagreements to
divide the community. A disagreement can arise over a wide
range of issues such as strategic direction, resource allocation,
or operational procedures. If left unresolved, a disagreement
can escalate and lead to the formation of factions within the
community. These factions may then compete against each
other for power, which can undermine the decentralized nature
of the DAO.
It’s important to have effective mechanisms in place to re-
solve disagreements in a fair and transparent manner. DAOs can
consider implementing dispute resolution protocols or media-
tion processes to address disagreements and prevent them from
dividing the community. By addressing disagreements proac-
tively and collaboratively, DAOs can maintain their democratic
and decentralized nature while avoiding factionalism and pre-
serving their collective decisi on-making power. Additionally,
DAO governance should dictate any progress updates for the
project source code or other initiatives in a fully transparent way
via public communication channels, e.g., Discord and Slack.
C. Legality
It is evident that the major ity of successful DAOs operate
within the ﬁnancial sector [cf. Fig. 2(a), Fig. 7(c), and Fig. 6,
Insight-➐ ], which poses signiﬁcant risks from various fronts.
These risks include potential attacks from malicious actors, as
well as the threat of being censor ed by governmental entities
(e.g., more than 51% block proposers in Ethereum 2.0 are
OFACed by U.S. government, referring to our Insight-➏ ). As
a result, smaller organizations may face severe limitations on
their ability to operate effectively, and in some cases, these risks
could even lead to their demise.
Properly embracing legal regulation can avoid the above
problems. Laws or regulations about blockchain governance

---

## Page 13

2826 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
need to be properly established by standardizing the structures,
processes, developments, and the use of blockchain and making
every component (e.g., DAO) compliant with legal regulations
and ethical responsibilities [17]. In particular, after The DAO
hack, DAOs started to be concerned about being legally man-
aged with better security and protection in several countries and
regions.
D. High Cost
Running a DAO on-chain can be expensive (Fig. 7),
with costs varying based on factors such as the underlying
blockchain platform, complexity of smart contracts, and trans-
action volume. These costs are incurred through gas fees paid
to the network, which are collected by miners or arbitrage bots
and can become expensive in US dollars. Many DAOs create
their own ERC20 tokens [Fig. 7(c)] to use as governance votes,
which also incurs gas fees with each action taken. Even DAOs
that use stablecoins [Fig. 7(b)] for voting power still need to
purchase or borrow the coins from exchanges, adding to the ex-
penses. Additionally, fees for development, maintenance, audit-
ing, security assessments, marketing, and community building
can be difﬁcult to quantify and are excluded.
A reasonable way to reduce the costs of operating a DAO is to
rely on off-chain or layer-two techniques that can execute most
operations locally. Snapshot is an off-chain platform designed
to manage DAOs and enable votes. Additionally, other off-chain
tools can be found in Table III to further reduce costs. By
leveraging these techniques, DAO operators can minimize their
reliance on costly on-chain transactions and reduce their overall
expenses.
E. Nonsense Governance Activity
After analyzing the voting contexts (e.g., proposal titles and
topics), we have found that a nonnegligible proportion of gov-
ernance activities are nonsensical in nature (consistent with a
recent report by [8]). Our analysis reveals that a considerable
number of proposals (approximately 17.7% of all proposals,
raw data of Fig. 6) are completely irrelevant to the project’s
development, and merely consist of inappropriate or offensive
content such as jokes and impo lite questions. We think that
the current ease of proposal creation, which allows anyone to
submit a proposal, has contributed to the prevalence of such
nonsensical activities within the governance process.
Thus, the implementation of more stringent entry require-
ments for proposal creation is necessary, such as mandatory
completion of a tutorial on governance principles or holding a
minimum number of project tokens. By introducing such mea-
sures, we expect to see an improvement in the overall quality of
proposals and a reduction in the number of frivolous or fraud-
ulent proposals. In addition, we recommend the establishment
of a mechanism to ﬂag and remove any proposals that violate
the platform’s terms of service or are deemed inappropriate by
the community. This could be done through the appointment
of community moderators or the development of automated
systems to detect such proposals.
F . Contract Reliance
Most of the DAOs rely prominently on the authenticity and
validity of the smart contracts that offer trustless environments.
This implies that the vulner ability of smart contract codes and
implicit design pitfalls will pose potential threats to running
DAOs. A famous historical example caused by contract pitfalls
is the huge failure of The DAO hack due to a severe bug
in its smart contract code [41]. TheDAO raised $150M+ (by
ETH) for building a collective investment platform. However,
the project crashed shortly afterward due to a severe bug in
its smart contract code. As a result, a considerable amount of
assets was siphoned off and a disruptive hard fork happened
that signiﬁcantly affected the entire Ethereum blockchain till
now [42]. Attacks such as ﬂash loans [43] in DeFi protocols
that exploit the time interval of block conﬁrmation can also
undermine the sustainability of DAO communities.
To prevent a recurrence of s uch ﬁascos and stabilize mone-
tization mechanisms for sustai ned growth, DAO communities
must dedicate resources to establishing security protocols for
code auditing and developing enhanced tools and supportive
infrastructure. Additionally, the creation of robust marketing
and product design departments is essential. These departments
should develop effective product and content strategies that
align with the principles of each DAO project. Concurrently,
well-organized and consistent communication plans are cru-
cial for capturing broader public interest and fostering loyalty
within a decentralized context.
VI. F URTHER ACTIONS
In this section, we continue the discussions of previous so-
lutions and conduct a more detailed analysis of each category.
A. On Projects
Each project involves both competition and cooperation, and
we will discuss them from these two perspectives.
1) DAO-2-DAO Collaboration: The interaction between
different DAOs is crucial, prompting the design of decentralized
negotiation protocols [44]. Governance in DAOs signiﬁcantly
hinges on these protocols, with each DAO deﬁning a unique
set of parameters for consensus based on a standardized for-
malization of components such as the proposal format. This
standardization not only routinizes the evaluation of propos-
als, enhancing interaction efﬁciency for activities such as joint
ventures, token swaps, and shared monetary policies but also
facilitates more complex DAO- to-DAO transactions. Speciﬁ-
cally, a well-crafted formalization advances DAO-2-DAO col-
laboration toward an interorganizational framework, allowing
proposals from various DAOs to be adapted for a broad array
of complex contractual agreements. This extends their func-
tionality and supports a more integrated approach to decentral-
ized governance, enabling seamless integrations and strategic
alliances between DAOs.
2) Learn on SubDAOs – Management/Competition: DAO
management has been evolving to feature a tree structure indi-
cating the hierarchy of different DAOs where one might belong

---

## Page 14

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2827
to the others. There will be new groups of members that operate
independently of the group’s inception as DAOs grow. New
divisions, teams, focus, and ideas will be brought into the com-
munity. Rather than trying to house all that activity under one
roof, SubDAOs are an emerging approach for different working
groups to create their own foundation and ownership structure
[45]. All the SubDAOs tie value back to the originating entity.
At the same time, one thing to be noted is the competition
among different subDAOs within the same domain. Multiple
DAO participants will compete for one goal set by its superior
nodes. Balanced-off games among subDAOs should be further
considered for such scenarios.
B. On Infrastructure
In addition to guaranteeing the s ecure operation of the core
blockchain, a well-developed infrastructure and a range of use-
ful applications are crucial for promoting the widespread adop-
tion of DAOs.
1) DAO Stacks and Tools: As a generic term, the DAO space
has included a variety of projects that cover many components
and ﬁelds. We could sketch a relatively clear picture by learning
from its “stack” (Daostack [46]). The foundation is the basic
and backend software modules such as voting mechanisms (as
discussed before) for decentralized governance. On top of it,
a library layer used to build models for back ends is estab-
lished (e.g., Arc.js [47]). Also, a caching layer is needed for
collecting and structuring data (e.g., The Graph [48]). On the
top, the application layer is designed for DAO users to deploy
or participate in DAOs (Aragon [49]). In addition, a variety of
widely used coordination tools, such as Twitter, Discord, and
Github, play a role in supporting and facilitating DAO games
from an external perspective.
2) Applications via DAO: DAOs have been considered as
one of the biggest innovations in the Blockchain ecosystems
[50]. Therein, crowdfunding is one of the prime applications
where DAO plays a vital role. For instance, ConstitutionDAO
successfully pulled together $47 million worth of ether in a
week to try to buy a ﬁrst-edition copy of the U.S. Consti-
tution at a Sotheby’s auction [51]. Besides, DAO has been
involved in democratizing the Metaverse ecosystem by offering
contributions to decentralized infrastructure [52]. In addition,
the paradigm of DAO paradigm is also applied by NFT-based
investment projects to create and conﬁrm shared ownership of
assets. The emergence of a new generation of Dapps via DAO
in various sectors, e.g., supply chain, ﬁnance accounting, IoT,
and transportation [53] has demonstrated the innovation and the
need for DAO in current technology trends. Especially, DAO is
also investigated that it could be promising for e-government
systems in improving the efﬁciency and transparency of gov-
ernment operations.
C. On Voting Strategies
Two key questions regarding voting are: how to cast a vote
and how the outcome of the vote impacts decisions .
1) Voting Routes: V oting could be conducted through both
on-chain or off-chain. The on-chain voting service, such as
Tally [54], has to introduce the time-lock mechanism to provide
the polling period. Implementing such a mechanism typically
relies on the usage of smart contracts. Tally’s voting contains
two types of smart contracts: a token contract and a governor
contract. Meanwhile, the multisig wallet (e.g., Gnosis Safe[55])
is necessary for managing the deployed assets. However, on-
chain voting confronts the disadvantages of costly and delayed
conﬁrmation, signiﬁcantly decreasing the willingness of partic-
ipation of users. In contrast, Snapshot is an off-chain voting tool
that removes the expensive consumption of on-chain interactive
operations. The number of created DAO spaces in two platforms
indicates that users are much more willing to participate in a
gas-free platform.
2) Strategy Design: The design of voting strategies in DAOs
plays a crucial role in ensuring effective decision-making and
fostering user participation. These strategies should strike a bal-
ance between security, efﬁciency, and inclusiveness, accommo-
dating various voting tools, applications, and regulatory require-
ments. On-chain and off-chain voting methods can be combined
to create hybrid strategies, leveraging the strengths of each
approach. For instance, off-chain voting through tools such as
Snapshot can be employed for preliminary or less critical deci-
sions, allowing for a more agile and gas-free voting process. On
the other hand, on-chain voting, such as the Tally mechanism,
can be reserved for more critical decisions, where the security
and immutability provided by blockchain technology are essen-
tial. Another dimension to consider in voting strategy design is
the DAO-to-DAO voting mechanism, where one DAO can par-
ticipate in the decision-making process of another DAO. This
can promote cross-DAO collabora tion and resource sharing
[56], fostering synergies within the decentralized ecosystem.
V oting in SubDAOs can also be utilized to facilitate the delega-
tion of decision-making power to specialized groups, enabling
efﬁciency in governance.
D. On Tokenization
Tokenization forms the foundation of the blockchain econ-
omy and incentive mechanisms. Achieving sustainability and a
healthy Web3 ecosystem requires building on tokenization.
1) (Un-)healthy Tokenization: A healthy tokenization distri-
bution enables fairness to people who are involved in the DAO
projects. It means that anyone who is purchasing the token com-
petes on the same terms and is subjected to the same token sales
policies. Besides, reasonable token usage of DAOs signiﬁcantly
impacts project-controlled liquidity [57]. As discussed in the
previous section, the imbalance between self-issued tokens and
mainstream tokens raises the risk of manipulation in the market.
The equality of token usage logi c has signiﬁcant im plications.
For example, small marketcap projects launched at cheap initial
prices usually face the potential abuse of whale and team pur-
chases. Meanwhile, the larger the market capitalization which
is managed by DAOs, the less likely the chances that the whale
and inside team can purchase tokens on the market. Hence, the

---

## Page 15

2828 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
Fig. 8. DAOs over different platforms. (a) Governance structures over
different platforms. (b) Effciency index over different platforms.
balance between the mainstream tokens and self-issued tokens
not only reduces the possibility of market manipulation but also
provides space and ﬁnances for the founding team of DAOs.
2) Governance via Tokenization: Effective governance is
crucial for aligning the interests of various stakeholders and
ensuring the stability of the ecosystem. This is particularly im-
portant in DAOs where incentivizing responsible behavior can
be challenging. Tokenization offers monetary incentives [58]
to various stakeholders, including the project team, application
providers, node operators, blockchain users, and regulators.
Ensuring equitable distribution of these incentives is crucial.
A robust governance framework, incorporating principles of
game theory, is essential to foster diverse stakeholder engage-
ment and ensure fair representation. Additionally, transparent
distribution of on- and off-chain incentives can help build trust
and cooperation among stakeholders toward achieving com-
mon goals. At a higher level, maintaining a balance between
mainstream tokens and self-issued tokens can reduce the risk
of market manipulation. Building better governance through
rational incentives and transparent mechanisms can lead to a
Schelling point [59], where desirable behaviors are encouraged,
and fairness is maintained.
VII. E
XTENDED DISCUSSION
A. DAOs Across Different Platforms
As our empirical study focuses on a single platform, we
have broadened our analysis to include additional platforms by
presenting comparative results (cf. Fig. 8).
1) Evaluation Results: Fig. 8(a) compares the governance
structures of DAOs across various platforms by analyzing the
distribution of voting systems. Ethereum Mainnet stands out
with the highest number of DAO projects, predominantly em-
ploying single-choice voting, followed by other systems such as
ranked-choice voting and approval voting. Binance Smart Chain
Mainnet and Polygon Mainnet also host a signiﬁcant number
of DAOs, but with fewer governance structures represented.
Platforms such as Fantom Opera, Arbitrum One, and Gnosis
Chain have a smaller number of DAOs and exhibit limited
diversity in voting systems. This analysis highlights that single-
choice voting is the most widely used governance structure,
likely due to its simplicity and efﬁciency. In contrast, more com-
plex systems (e.g., quadratic voting, weighted voting) are less
common, potentially because they require higher computational
overhead or introduce barriers to participation.
Fig. 8(b) evaluates the efﬁciency index of DAOs on different
platforms. The efﬁciency index is calculated by
E =
∑
v∈V
{
log10(M(v)+ 1)·w(v), if M(v)> 0
0, if M(v)= 0
where
1) E is the efﬁciency index for a platform.
2) V is the set of voting systems (e.g., single-choice voting,
approval voting).
3) M(v) represents the total number of members participat-
ing in voting system v on the platform.
4) w(v) is a predeﬁned weight reﬂecting the relative ef-
ﬁciency of each voting system in terms of the relative
simplicity, speed, and scalability of each voting mech-
anism (e.g., single-choice vo ting: 1.0, multiple-choice
voting: 0.8, quadratic voting: 0.6, weighted voting: 0.7,
conviction voting: 0.5).
Ethereum Mainnet achieves the highest efﬁciency index due
to a combination of large DAO membership and a predomi-
nance of simpler voting systems such as single-choice voting.
In contrast, platforms such as Gnosis Chain and Arbitrum One
score lower on the efﬁciency index, reﬂecting fewer members
and less frequent use of highly efﬁcient voting systems.
2) Challenges Across the Platforms: Despite these insights,
DAOs face several challenges across platforms. On highly uti-
lized platforms such as Ethereum Mainnet, scalability is a sig-
niﬁcant concern. As the number of participants increases, en-
suring active participation and avoiding voter apathy becomes
critical. Platforms with smaller DAOs, such as Fantom Opera
and Gnosis Chain, may face challenges in gaining sufﬁcient
participation to make governance meaningful.
Furthermore, more complex voting systems, such as
quadratic or weighted voting, while theoretically offering
greater fairness, can introduce barriers to adoption due to
their computational requirements and the learning curve for
participants. Security risks, such as vote manipulation or Sybil
attacks, remain a concern across all platforms, particularly in
decentralized environments where anonymity is valued.

---

## Page 16

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2829
B. Insights to Real-World
We elucidate the connection between our insights in the DAO
ecosystem and their real-world scenarios, especially for policy
considerations.
1) Pareto distribution in members and centralization risks:
In many cases [60], [61], a small group of participants
held substantial voting power, which contributed to gov-
ernance vulnerab ilities and the eventual exploitation of
the system. To mitigate centra lization risks, policymak-
ers could consider implementing regulations that pro-
mote equitable token distribution and prevent excessive
accumulation of voting power by a few individuals or
entities. This would help preserve the decentralized na-
ture of DAOs and ensure more democratic governance
structures.
2) Platform diversiﬁcation and technological upgrades
impeding the capacity and efﬁciency: For example, out-
dated IPFS versions can lead to slower data retrieval
and potential security vulnerabilities, affecting the over-
all performance of DAO operations. Encouraging the
adoption of updated and standardized technologies within
DAOs can enhance interoperability and security. Policy-
makers might consider establishing guidelines or incen-
tives for DAOs to regularly update their technological
infrastructure, ensuring they remain robust and efﬁcient.
3) Decentralized e-voting patterns and organizational
structures making it hard to reach consensus: For in-
stance, the Uniswap DAO has experienced challenges in
passing proposals due to low voter turnout and the need
for a high quorum [62]. Exploring hybrid governance
models that combine decentralized decision-making with
hierarchical elements could improve efﬁciency without
compromising inclusivity. Policymakers might support
research into such models and provide frameworks that
allow DAOs to adopt governance structures best suited to
their speciﬁc needs.
4) Diverse voting contexts and governance challenges: As
highlighted in [63], a small number of large stakeholders
have been observed to wield disproportionate inﬂuence
over decisions in the MakerDAO community, raising con-
cerns about the true decentralization of the organization.
Implementing policies that encourage broader participa-
tion and prevent power concentration is crucial. This
could include mandating transparent voting processes,
setting limits on individual voting power, or introducing
mechanisms that incentivize active participation from a
diverse member base.
5) High risks of excessive opportunistic behaviors and
token utilization: As highlighted in [64],s o m eD A O s
have experienced signiﬁcant token value ﬂuctuations due
to reliance on self-issued tokens, affecting their oper-
ational sustainability. Estab lishing guidelines for token
issuance and utilization within DAOs can help mitigate
these risks. Policies that promote the use of stable and
widely accepted tokens, or that require adequate backing
of self-issued tokens,could enhance the ﬁnancial stability
of DAOs and protect members from undue risk.
C. Consistent Validity of Insights
To ensure the validity of our ﬁndings, we revisited the DAO
ecosystem using up-to-date data (Jan. 2025) fetched from the
same source, the DeepDAO platform. A comparison between
the rankings based on the total number of members weighted by
proposal counts in May. 2023 and Jan. 2025 reveals signiﬁcant
consistency. Notably, 7 out of the top 10 projects in the 2023
data [cf. Fig. 2(a)], remain in the top 10 in the 2025 rankings,
with projects such as P
ANCAKESWAP,A AVE, and O PTIMISM
COLLECTIVE consistently leading. This overlap underscores the
robustness and longevity of the trends and insights presented in
this article.
Although certain shifts in rankings were noted, such as the
ascension of projects such as D ECENTRALAND and ENS in
the 2025 dataset, these variations underscore the dynamic and
continuously evolving nature of DAOs. The consistency of the
majority of top-ranked projects reinforces the robustness and re-
liability of our conclusions, while the observed changes further
illustrate the adaptability and progressive development of the
DAO ecosystem. These ﬁndings conﬁrm the ongoing relevance
of our insights and their enduring contribution to understanding
the organizational dynamics of DAOs.
VIII. R
ELATED WORK
This section covers three dimensions of DAO progress: the
evolution of several major DAOs in the industry, formative
research on DAOs, and related work on Web3 governance.
A. DAO Evolution
We callback several milestones in DAO’s history. The ﬁrst
DAO, known as The DAO [65], was established on Ethereum
in 2016, marking the beginning of DAOs on blockchains. Un-
fortunately, the project was hacked, ultimately leading to a hard
fork of the Ethereum blockchain [42], [41]. After this setback,
DAOs regained popularity with the emergence of MakerDAO
[66] in 2018. The project introduced an on-chain governance
system to produce a deposited stablecoin protocol (a.k.a. DAI).
Then, in 2020, a surge of decentralized ﬁnance (DeFi) protocols
[67], known as the DeFi summer , propelled DAOs to new
heights. These protocols are built on top of various blockchain
platforms, such as Ethereum, BSC, and Avalanche, and enable
decentralized ﬁnance services such as DEXs (Uniswap, dYdX),
lending (Compound, Aave), yield aggregators (Convex), and
staking (Lido), among others. Till now, DAOs embraced the
concept of Web3[1], and their development became intertwined
with the surrounding components that make up the decentral-
ized web. This includes elements such as wallets, smart con-
tracts, various blockchain platforms, and even regulations [68].
B. Formative DAO Studies
Liu et al. [2] provide an overview of early DAOs by ex-
plaining the deﬁnitions, and preliminaries and giving a simple
taxonomy. Daian shows a series of DAO attack analyses [69],
[70] from the technical level by diving into the source code.
They point out the reasons for recursive send vulnerabilities in

---

## Page 17

2830 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
Ethereum that cause a monetary loss ($150M). Robin et al. [9]
have investigated three DAO projects (Compound, Uniswap,
and ENS) by empirically analyzing their voting powers and
discussing governance. Later, Daian et al. [71] propose a po-
tential attack form called Dark DAO, which means a group of
members form a decentralized cartel and can opaquely manip-
ulate (e.g., buy) on-chain votes. Yu et al. [3] provide a quick
review of existing DAO literatu re and deliver t heir responses
by statistically reviewed papers. Feichtinger et al. [8] conduct
an empirical study on 21 DAOs to explore the hidden problems,
including high centralization, monetary costs, and pointless
activities. Feichtinger et al.[72] provided a systematically study
on security threats to DAOs. Sharma et al. [10] have developed
their research on 10 diverse DAOs to examine their degree of
decentralization and autonomy. Besides, many researchers and
organizations also put their focus on DAO by generating in-time
reports [32], [73] and online posts [68].
Instead of focusing on single attacks or individual projects,
we provide a comprehensive, data-driven analysis of DAO
projects hosted on Snapshot. This study goes beyond surface-
level observations, offering unique insights into member partic-
ipation, voting dynamics, and governance challenges.
C. Governance in Web3
Governance is the cornerstone of DAOs, but research in
this area remains vague. DAOs are rooted in blockchain and
heavily inﬂuenced by on-chain tokens, which means they are
affected by the underlying technology as well as cryptocurrency
regulations. For the former, Kiayias et al. [17] have explored
the governance process and properties within the blockchain
context. They use a ﬁrst principles approach to derive seven
fundamental properties and apply them to evaluate existing
projects. Wang et al. [1] have partially incorporated this notion
into Web3, emphasizing the importance of DAO governance
in Web3. Liu et al. [59] have presented a systematic review
of primary studies on gove rnance and provide a qualitative
and quantitative synthesis. Regar ding the latter, governance
primarily comes from governments of different countries, even
though blockchain is designed to be decentralized. However, it
can still be easily regulated by i ncreasingly centralized miners
or validators. Ethereum (after the Merge) PoS validators who
rely on MEV-boots services may be monitored and regulated
by the government (OFAC-compliant [74]). Additionally, pure
cryptocurrency companies can also be governed. A noteworthy
example is the US sanctions against Tornadocash [75].
IX. C
ONCLUSION
We empirically studied the ground truth of the wild DAO
projects collected from Snapshot, the largest off-chain voting
platform. Our empirical results discover a series of facts hid-
den from the light, covering its unfair distributions on such
as participant regions or language usage, as well as revealing
potential threats of centralization, contract reliance and policy
impact. We also explored various approaches to improve DAO
structures. Our work delineates a clear view of existing DAOs.
Data Use Disclaimer: This work does not raise any ethical
issues. All the data we crawl from Snapshot are open-released
and free to use with CC0 licenses. We strive to maintain the
accuracy of all data that we crawl from Snapshot and declare
that the data will not be used for any commercial purposes.
Acknowledgment: An abstract of this work has been pub-
lished at ICBC’23 [76]. An earlier version titled “An Empirical
Study on Snapshot DAOs” is available at [77].
R
EFERENCES
[1] Q. Wang, R. Li, Q. Wang, S. Ch en, M. Ryan, and T. Hardjono, “Ex-
ploring Web3 from the view of blockchain,” 2022, arXiv:2206.08821.
[2] L. Liu, S. Zhou, H. Huang, and Z. Zheng, “From technology to society:
An overview of block chain-based DAO,” IEEE Open J. Comput. Soc. ,
vol. 2, pp. 204–215, 2021.
[3] G. Yu, Q. Wang, T. Bi, S. Chen, and S. Xu, “Leveraging architectural
approaches in Web3 applications–a DAO perspective focused,” in Proc.
IEEE Int. Conf. Blockchain Cryptocurrency (ICBC) , 2023.
[4] Y . Faqir-Rhazoui et al., “A Compa rative Analysis of the Platforms for
Decentralized Autonomous Organizations in the Ethereum Blockchain,”
J. Internet Services Appl. , vol. 12/1, no. 1, pp. 1–20, 2021.
[5] S. Wang, W. Ding, J. Li, and other, “Decentralized autonomous organi-
zations: Concept, model, and applications,” IEEE Trans. Comput. Social
Syst. (TCSS), vol. 6, no. 5, pp. 870–878, Oct. 2019.
[6] E. Bischof et al., “Longevity foundation: Perspective on decentralized
autonomous organization for special-purpose ﬁnancing,” IEEE Access ,
vol. 10, pp. 33048–33058, 2022.
[7] I. Mehdi et al., “Data Centric DAO: When blockchain reigns
over the Cloud,” in Proc. IEEE Int. IOT, Electron. Mechatron.
Conf. (IEMTRONICS) , Piscataway, NJ, USA: IEEE Press, 2022,
pp. 1–7.
[8] R. Feichtinger, R. Fritsch, Y . V onlanthen, and R. Wattenhofer, “The hid-
den shortcomings of (d) aos–an empirical study of on-chain governance,”
in Proc. Int. Conf. Financial Cryptography Data Secur., New York City,
NY , USA: Springer, 2023, pp. 165–185.
[9] R. Fritsch, M. Müller, and R. W attenhofer, “Analyzing voting power in
decentralized governance: Who controls daos?” Blockchain: Res. Appl.,
vol. 5, no. 3, 2024, Art. no. 100208.
[10] T. Sharma et al., “Unpacking h ow decentralized autonomous organiza-
tions (DAOs) work in practice,” in Proc. IEEE Int. Conf. Blockchain
Cryptocurrency (ICBC) , Piscataway, NJ, USA: IEEE Press, 2024,
pp. 416–424.
[11] Snapshot, 2022. Accessed: Jan. 13, 2024. [Online]. Available: https://
snapshot.org/#/
[12] G. Wood et al., “Ethereum: A secu re decentralised generalised trans-
action ledger,” Ethereum Yellow Paper , vol. 151, no. 2014, pp. 1–32,
2014.
[13] R. Li et al., “An ofﬂine delegatable cryptocurrency system,” in Proc.
IEEE Int. Conf. Blockchain Cryptocurrency (ICBC) , Piscataway, NJ,
USA: IEEE Press, 2021, pp. 1–9.
[14] P. Tolmach, Y . Li, S.-W. Lin, Y . Liu, and Z. Li, “A survey of smart
contract formal speciﬁcation and veriﬁcation,” ACM Comput. Surv.
(CSUR), vol. 54, no. 7, pp. 1–38, 2021.
[15] R. Drummond, S. Manu, S. Markus, L. Dave, and A. Christopher,
“Decentralized identiﬁers (DIDs) v1. 0: Core architecture, data model,
and representations,” 2021. Accessed: Jan. 13, 2024. [Online]. Available:
https://www.w3.org/TR/did-core/
[16] ENS, “Ethereum name service,” 2022. Accessed: May 20, 2024. [On-
line]. Available: https://ens.domains/
[17] A. Kiayias and P. Lazos, “S oK: Blockchain governance,” Proc. ACM
Conf. Adv. Financial Technol. (AFT) , 2022.
[18] J. R. Douceur, “The sybil attack,” in Peer-to-Peer System, P. Druschel,
F. Kaashoek, and A. Rowstron, Eds., Berlin, Heidelberg: Springer, 2002,
pp. 251–260.
[19] V . Cortier, D. Galindo, R. Küsters, J. Müller, and T. Truderung,
“SoK: Veriﬁability notions fo r e-voting protocols,” in Proc. IEEE
Symp. Secur. Privacy (SP) , Piscataway, NJ, USA: IEEE Press, 2016,
pp. 779–798.
[20] Q. Wang, S. Fu, S. Chen, and J. Yu, “A ﬁrst dive into OFAC in DeFi
space,” in Proc. Int. Conf. Financial Cryptography Data Secur. (FC) ,
New York City, NY , USA: Springer, 2023, pp. 133–140.

---

## Page 18

W ANG et al.: UNDERSTANDING DAOS: EMPIRICAL STUDY 2831
[21] E. Jiang et al., “Decentralized ﬁnance (DeFi): A survey,” 2023,
arXiv:2308.05282.
[22] F. V ogelsteller and V . Buterin, “Eip-20: Token standard,” Ethereum
Improvement Proposals, 2015. Accessed: May 20, 2024. [Online].
Available: https://eips.ethereum.org/EIPS/eip-20
[23] Q. Wang and G. Yu, “Understanding BRC-20: Hope or hype,”
2023. Accessed: May 20, 2024. [Online]. Available: https://ssrn.com/
abstract=4590451
[24] N. Li, M. Qi, Q. Wang, and S. Chen, “Bitcoin inscriptions: Foundations
and beyond,” in Proc. IEEE Int. Conf. Blockchain Cryptocurrency
(ICBC), 2024.
[25] Binance, “Binance academy: BEP-20,” 2024. Accessed: Jan. 13, 2024.
[Online]. Available: https://academy.binance.com/en/glossary/bep-20
[26] W. Entriken, D. Shirley, J. Evans, and N. Sachs, “Eip-721: Non-fungible
token standard,” Ethereum Improvement Proposals , 2018. Accessed:
Jan. 13, 2024. [Online]. Available: http s://eips.ethereum.org/EIPS/eip-
721
[27] R. Witek, C. Andrew, C. Philippe, T. James, B. Eric, and S. Ronan, “Eip-
1155: Multi token standard,” Ethereum Improvement Proposals, 2018.
Accessed: Jan. 13, 2024. [Online]. Av ailable: https://eips.ethereum.org/
EIPS/eip-1155.
[28] Q. Wang, R. Li, Q. Wang, and S. Chen, “Non-fungible token
(NFT): Overview, evaluation, opportunities and challenges,” 2021,
arXiv:2105.07447.
[29] T. Joshua, P. Isaac, G. Ido, E. Eyal, Z. Michael, and S. Furter, “Common
interfaces for daos,” 2022. Accessed: May 20, 2024. [Online]. Available:
https://eips.ethereum.org/EIPS/eip-4824
[30] Z. Zainan, Evan, and X. Yin, “Erc-1202: V oting interface [draft],” 2018.
Accessed: May 20, 2024. [Online]. Av ailable: https://eips.ethereum.org/
EIPS/eip-1202.
[31] D. Casey, “Eip-779: Hardfork meta: DAO fork,” 2017. [Online]. Avail-
able: https://eips.ethereum.org/EIPS/eip-779
[32] S. Aiden et al., “World economic forum: Decentralized autonomous
organizations: Beyond the hype,” 2022. Accessed: May 20, 2024. [On-
line]. Available: https://www3.weforum.org/docs/WEF_Decentralized_
Autonomous_Organizations_Beyond_the_Hype_2022.pdf
[33] J. Benet, “IPFS-content addre ssed, versioned, p2p ﬁle system,” 2014,
arXiv:1407.3561.
[34] Wikiwand, “The pareto principle, ” 2022. [Online]. Available: https://
www.wikiwand.com/en/Pareto_principle
[35] V . Pareto, “Cours d’Économie politique,” vol. 1, Librairie Droz, 1964.
[36] IPFS, “IPFS Doc: Con tent addressing and CIDs,” 2022. [Online]. Avail-
able: https://docs.ipfs.tech/concepts/content-addressing/#cid-conversion
[37] Wikiwand, “Matthew effect,” 2022. Accessed: May 20, 2024. [Online].
Available: https://www.wikiwand.com/en/Matthew_effect
[38] S. Lloyd, “Least squares quantization in PCM,” IEEE Trans. Inf. Theory
(TIT), vol. 28, no. 2, pp. 129–137, Mar. 1982.
[39] H. Hotelling, “Analysis of a comple x of statistical variables into principal
components,” J. Edu. Psychol. , vol. 24, no. 6, p. 417, 1933.
[40] L. Van der Maaten and G. Hint on, “Visualizing data using t-SNE.”
J. Mach. Learn. Res. , vol. 9, no. 11, pp. 1–27, 2008.
[41] M. I. Mehar et al., “Understandi ng a revolutionary and ﬂawed grand
experiment in blockchain: the DAO attack,” J. Cases Inf. Technol.
(JCIT), vol. 21, no. 1, pp. 19–32, 2019.
[42] O. Konashevych, “Takeaways: 5 years after the DAO crisis and
ethereum hard fork,” 2021. Accessed: May 20, 2024. [Online].
Available: https://cointelegraph.com/ne ws/takeaways-5-years-after-the-
dao-crisis-and-ethereum-hard-fork
[43] K. Qin, L. Zhou, B. Livshits, and A. Gervais, “Attacking the DeFi
ecosystem with ﬂash loan s for fun and proﬁt,” in Proc. Int. Conf.
Financial Cryptography Data Secur. (FC) , New York City, NY , USA:
Springer, 2021, pp. 3–32.
[44] C. F. Dagdelen, “D2d: Toward s decentralized negotiation protocols,”
2021. Accessed: Jan. 13, 2024. [Online]. Available: https://
blog.curvelabs.eu/d2d-towards-decentralized-negotiation-protocols-
e37d164e91e6
[45] Coopahtroopa, “How to subdao,” 2021. [Online]. Available: https://
coopahtroopa.mirror.xyz/7bfK9st2mvhxlla4XKotRjetq5-YhaiwqRwS8D
hkD-o
[46] Coopahtroopa, “Daostack: An operating system for collective intelli-
gence,” 2022. [Online]. Available: https://medium.com/daostack
[47] DAOstack, “Arc.js: DAOstack java script client,” 2022. [Online]. Avail-
able: https://daostack.github.io/arc.js/
[48] TheGraph, “The graph: Apis for a vibrant decentralized future,” 2022.
Accessed: May 20, 2024. [Online]. Av ailable: https://thegraph.com/en/
[49] Aragon, “Aragon platform,” 2022. Accessed: Jan. 13, 2024. [Online].
Available: https://aragon.org/
[50] Y . Chen, “Blockchain toke ns and the potential democratization of
entrepreneurship and innovation,” Bus. Horizons, vol. 61, no. 4, pp. 567–
575, 2018.
[51] MacKenzie Sigalos, Constitutiondao crypto investors lose bid to buy
constitution copy . Accessed: November 26, 2022. [Online]. Available:
https://www.cnbc.com/2021/11/18/constitutiondao-crypto-investors-
lose-bid-to-buy-constitution-copy.html
[52] T. R. Gadekallu et al., “Blockchain for the metaverse: A review,” 2022,
arXiv:2203.09738.
[53] Y . El Faqir, J. Arroyo, and S. Hassan, “An overview of decentralized
autonomous organizations on the blockchain,” in Proc. 16th Int. Symp.
Open Collaboration, 2020, pp. 1–8.
[54] Tally, “Tally,” 2022. Accessed: May 20, 2024. [Online]. Available:
https://www.tally.xyz/
[55] Gnosis, “Gnos is-safe: Trusted platform t o manage digital assets on
ethereum,” 2022. Accessed: Jan. 13, 2024. [Online]. Available: https://
gnosis-safe.io/
[56] L. T. Nguyen et al., “Blockchain-empowered trustworthy data shar-
ing: Fundamentals, applications, and challenges,” ACM Comput. Surv.
(CSUR), pp. 1–35, 2025.
[57] W. Warren and A. Bandeali, “0x: An open protocol for decentralized
exchange on the ethereum blockchain,” pp. 4–18, 2017. Accessed: May
20, 2024. [Online]. Available: https:// github.com/0xProject/whitepaper
[58] G. Yu, Q. Wang, C. Sun, L. D. Nguyen, H. Bandara, and S.
Chen, “Maximizing NFT incentives: References make you rich,” 2024,
arXiv:2402.06459.
[59] Y . Liu, Q. Lu, L. Zhu, H.-Y . Paik, and M. Staples, “A systematic
literature review on blockchain governance,” J. Syst. Softw. , vol. 197,
no. 1, 2022, Art. no. 111576.
[60] Cryptodose.net, “DAO use cases and real-world applications.” Accessed:
November 14, 2024. [Online]. Availab le: https://cryptodose.net/learn/
dao-use-cases/
[61] Y . Zhang, Q. Wang, S. Chen, and C. Wang, “How to rationally select
your delegatee in PoS,” 2023, arXiv:2310.08895.
[62] 101Blockchains.com, “Top DAO use cases and examples.” Accessed:
November 14, 2024. [Online]. Availab le: https://101blockchains.com/
top-dao-use-cases-and-examples/
[63] C. W. Blog , “Real-world examples of DAOs.” Accessed: November
14, 2024. [Online]. Available: https:// blog.capitalwallet.com/real-world-
examples-of-daos/
[64] E. C. Blog , “DAO use cases: Exploring potential applications.” Ac-
cessed: November 14, 2024. [Online]. A vailable: https://evacodes.com/
blog/dao-use-cases-expl oring-potential-applications
[65] S. Falkon, “The story of the DAO — its history and consequences,”
2017. [Online]. Available: https://medi um.com/swlh/the-story-of-the-
dao-its-history-and-cons equences-71e6a8a551ee
[66] MakerDAO, “MakerDAO foundation proposal v2,” 2018. Accessed:
May 20, 2024. [Online]. Available: https://medium.com/@MakerDAO/
foundation-proposal-v2-f10d8ee5fe8c
[67] S. M. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and
W. J. Knottenbelt, “SoK: Decen tralized ﬁnance (DeFi),” in Proc. Int.
Conf. Financial Cryptography Data Secur. (FC) , 2022.
[68] Chainlink, “DAOs and the complexities of Web3 governance,” 2022.
Accessed: May 20, 2024. [Online]. Av ailable: https://blog.chain.link/
daos/
[69] D. Philip, “Analysis of the DAO exploit,” 2016. Accessed: Oct. 10, 2024.
[Online]. Available: https://hackingdistributed.com/2016/06/18/analysis-
of-the-dao-exploit/
[70] D. Philip, “Chasing the DAO attacker’s wake,” 2016. Accessed: Oct.
10, 2024. [Online]. Available: https://pd aian.com/blog/chasing-the-dao-
attackers-wake/
[71] D. Philip, K. Tyler, M. Ian, and J. Ari, “On-chain vote buying and the
rise of dark DAOs,” 2018. Accessed: Oct. 10, 2024. [Online]. Available:
https://hackingdistributed.com/2018/07/02/on-chain-vote-buying/
[72] R. Feichtinger, R. Fritsch, L. Heim bach, Y . V onlanthen, and R. Watten-
hofer, “SoK: Attacks DAOs,” in Proc. Int. Conf. Adv. Financial Technol.
(AFT), 2024.
[73] H. Samer and F. Primavera, “Decentralized autonomous organization,”
Internet Policy Review, 2021. Accessed: Oct. 10, 2024. [Online]. Avail-
able: https://policyreview.info/pdf/policyreview-2021-2-1556.pdf
[74] X. Xiong and J. Luo, “Global tre nds in cryptocurrency regulation: An
overview,” in Proc. Int. Conf. Math. Res. Blockchain Econ. (MARBLE),
2024.

---

## Page 19

2832 IEEE TRANSACTIONS ON COMPUTATIONAL SOCIAL SYSTEMS, VOL. 12, NO. 5, OCTOBER 2025
[75] Q. Wang, et al., “U.S. treasury sanctions notorious virtual currency
mixer tornado cash,” 2022. Accessed: Oct. 10, 2024. [Online]. Available:
https://home.treasury.gov/news/press-releases/jy0916
[76] Q. Wang et al., “A ﬁrst look into blockchain DAOs,” in Proc. IEEE Int.
Conf. Blockchain Cryptocurrency (ICBC) , Piscataway, NJ, USA: IEEE
Press, 2023, pp. 1–3.
[77] Q. Wang et al., “An empirical study on Snapshot DAOs,” 2022,
arXiv:2211.15993.
Qin Wang (Member, IEEE) received the bachelor’s
degree in electronical engineer from the School of
Electronic Engineering, Northwestern Polytechnical
University, Xi’an, China, in 2015, and the master’s
degree in computer science from the Electronic
Engineering, Beihang University, Beijing, China,
in 2018, and the Ph.D. degree in computer sci-
ence from the School of Science, Computing and
Engineering Technologies, Swinburne University of
Technology, Melbourne, Australia, in 2022.
He is a Senior Research Scientist with CSIRO
Data61 and an Adjunct Lecturer with University of New South Wales
(UNSW), Sydney and University of Technology Sydney (UTS), Sydney,
Australia. His research interests include emerging Web3 techniques, including
NFTs, DAOs, and DeFi, as well as the fundamental aspects of consensus
protocols, such as scalability, security, and privacy.
Guangsheng Yu (Member, IEEE) received the
B.Sc. degree in telecommunication network engi-
neering and M.Sc. degree in computer engineer-
ing from the School of Electrical Engineering
and Telecommunications, University of New South
Wales (UNSW), Sydney, Australia, in 2014 and
2015, respectively. He received the Ph.D. degree
in cybersecurity from the School of Electrical and
Data Engineering, University of Technology Sydney
(UTS), Sydney, in 2021.
Currently, he is a Lecturer with UTS. From 2021
to 2024, he was previously a Postdoctoral Research Fellow with CSIRO
Data61. His research interests include cybersecurity, blockchain, and federated
learning.
Yilin Sai (Student Member, IEEE) received the
B.Eng. (Hons.) degree in electrical engineering
(computer) from the University of Sydney, Sydney,
Australia, in 2017.
He is a Senior Software Engineer with CSIRO
Data61 and a Postdoctora l Student with Univer-
sity of New South Wales (UNSW), Sydney, Aus-
tralia. With expertise in full-stack development, he
specializes in building and delivering innovative,
robust, and scalable cloud software platforms and
solutions. His research inter ests include blockchain,
distributed computing, big data analysis, Internet of Things, deep learning and
network security.
Caijun Sun received the B.E degree from
Hangzhou Normal University, Hangzhou, China, in
2013 and the Ph.D. degree from Beijing University
of Posts and Telecommunications, Beijing, China,
in 2020.
Currently, he is a Senior Security Engineer with
Zhejiang Lab, Hangzhou, China. His research inter-
ests include malware analy sis and data security.
Lam Duc Nguyen (Member, IEEE) received the
B.Sc. degree from Hanoi University of Science and
Technology, Hanoi, Vietnam, in 2015, and the M.Sc.
degree from Seoul National University, Seoul, South
Korea, in 2018, both in computer science, and the
Ph.D. degree in electronic systems from Aalborg
University, Aalborg, Denmark, in 2021.
He is a Research Fellow with CSIRO Data61.
His research interests in clude the intersection of
operations research, blo ckchain, machine learning,
and Internet of Things.
Dr. Nguyen received the Outstanding Paper Award from WF-IoT 2020.
Shiping Chen (Senior Member, IEEE) received
a Bachelor degree from the Harbin University of
Science and Technology, Harbin, China, in 1985,
and Master’s degree from the Chinese Academy of
Sciences (CAS), Shenyang, China, in 1990, both in
computer science, and the Ph.D. degree from the
School of Computer Science and Engineer, Univer-
sity of New South Wales (UNSW), Australia, 2001.
He is a Principal Research Scientist with CSIRO
Data61. He also holds a Conjunct Professor with
University of New South Wales (UNSW), Sydney,
Australia. His research in terests include secure d ata storage & sharing and
secure multiparty collaboration.
Prof. Chen is actively involved in computing research communities through
publications, journal editorships and c onference PC services, including In-
ternational World Wide Web Conference , International Conference on En-
terprise Design, Operati ons, and Computing (EDOC) , International Confer-
ence on Service-Oriented Computing (ICSOC) , and IEEE I
NTERNATIONAL
CONFERENCE ON WEB SERVICES (ICWS)/IEEE INTERNATIONAL CONFERENCE
ON SERVICES COMPUTING (SCC)/IEEE I NTERNATIONAL CONFERENCE ON
CLOUD COMPUTING (CLOUD). He is an IET fellow.

---
