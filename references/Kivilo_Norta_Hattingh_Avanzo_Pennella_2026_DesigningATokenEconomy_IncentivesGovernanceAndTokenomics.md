# Kivilo_Norta_Hattingh_Avanzo_Pennella_2026_DesigningATokenEconomy_IncentivesGovernanceAndTokenomics.pdf

## Page 1

Blockchain:Research and Applications 00 (2026) 1–27
Blockchain:
R and A
Designing a Token Economy: Incentives, Governance, and
Tokenomics
Samela Kiviloa, Alex Nortab,d,1,∗, Marie Hattinghc, Sowelu Avanzoe, Luca Pennellaf
aTallinn University of Technology, Estonia; samela.kivilo@gmail.com
bTallinn University, Estonia; alex.norta.phd@ieee.org
cUniversity of Pretoria, South Africa; marie.hattingh@up.ac.za
dDymaxion OÜ, Tallinn, Estonia
eUniversity of Torino, Italy; soweluelios.avanzo@unito.it
fUniversity of Trieste, Italy; luca.pennella@phd.units.it
Abstract
In recent years, tokenomic systems, decentralized systems that use cryptographic tokens to represent value and rights, have evolved
considerably. Growing complexity in incentive structures has expanded the applicability of blockchain beyond purely transactional
use. Existing research predominantly examines token economies within specific use cases, proposes conceptual frameworks, or
studies isolated aspects such as governance, incentive design, and tokenomics. However, the literature offers limited empirically
grounded, end-to-end guidance that integrates these dimensions into a coherent, step-by-step design approach informed by concrete
token-economy development efforts. To address this gap, this paper presents the Token Economy Design Method (TEDM), a
design-science artifact that synthesizes stepwise design propositions for token-economy design across incentives, governance, and
tokenomics. TEDM is derived through an iterative qualitative synthesis of prior contributions and refined through a co-designed
case. The artifact is formatively evaluated via the Currynomics case study and additional expert interviews. Currynomics is an
ecosystem that maintains the Redcurry stablecoin, using real estate as the underlying asset. TEDM is positioned as reusable
design guidance that facilitates the analysis of foundational requirements of tokenized ecosystems. The specificity of the proposed
approach lies in the focus on the socio-technical context of the system and early stages of its design.
©2026 Published by Elsevier Ltd.
Keywords:token economy, token economy incentives, token economy design, token economy governance, tokenomics
1. Introduction
Blockchain technology has become increasingly popular in recent years due to its ability to provide decentral-
ization, security, and transparency. Still, even with significant advances in blockchain technology over time, its true
potential has not yet been fully realized. Although simple cryptocurrency transfers are straightforward to execute and
comprehend, it remains challenging to link such transactions to real-world objects or activities. The latter makes it
difficult to expand the range of beneficial use cases for blockchains [1]. As a solution, cryptographic tokens have
emerged that can be used to represent various assets or services within a network [2].
∗Corresponding author
1ORCID: 0000-0003-0593-8244
1
arXiv:2602.09608v1  [cs.CE]  10 Feb 2026

---

## Page 2

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–272
Before blockchain technology, tokens were commonly associated with vouchers that indicate tangible values such
as casino chips or beverages at festivals [3]. In the blockchain context, tokens act as a claim on both physical and
immaterial assets, e.g., gold ingots, real estate, and the accompanying rental contracts. Establishing a connection be-
tween real-life technology and blockchain paves the way for the development of advanced and innovative applications.
Thus, tokens play an important role in offering competition to hyperscaler web2 platforms that have reached a near-
monopoly status during the last decade [4]. These dominant platforms, for example, Facebook, Instagram, Airbnb
and Google, own user data in a centralized way, allowing the former to use them to increase proprietary profits [5].
Such centralization threatens the privacy of user data and increases the general vulnerability of the ecosystem against
hackers [6]. On the other hand, tokens enable translating various functionalities of such platforms, from social net-
works to search engines and file storage, into a decentralized form, where user data cannot be maliciously converted
into profits for intermediary platforms.
In terms of blockchain startups, tokens are an innovative channel of financing and can function as an “internal
currency” of ecosystems [7]. Additionally, tokens enable novel organizational forms often referred to as decentralized
autonomous organizations (DAOs). In practice, DAOs differ substantially in their degree of automation and decentral-
ization: some rely primarily on on-chain smart contracts and token-based governance, while others combine on-chain
execution with off-chain coordination, social processes, and informal norms. In this context, tokens frequently pro-
vide the basis for membership and governance mechanisms, and token-based voting is adopted in a large share of
governance protocols [8, 9, 10]. This interlinks decision making in DAOs with key functions such as conditional
value storage and transfer, which are essential for DAO operations [11], and underscores the importance of designing
sound token economies for DAOs.
The literature review in Section 2.2 suggests three recurring design dimensions in token economies: incentives,
governance, and tokenomics. Incentives concern rewards and penalties that shape participant behavior toward system
goals. Governance refers to how decision-making rights are allocated and exercised. Tokenomics defines the rules for
token issuance, distribution, allocation, and burning [12]. In this work, we focus on these dimensions as a pragmatic
structuring lens for design, while acknowledging that additional technical choices may condition feasible solutions.
Several studies highlighted the relevance of token economy design for blockchain ecosystems and their gover-
nance [13, 14]. Tokens in this context can align the interests of various stakeholder groups in a blockchain ecosystem,
since the value of the token is related to the inherent value added to the ecosystem itself [6]. Yet, the wide range
of token functionalities raises the need for careful tokenomic design. Developers often do not fully understand the
incentive structures they create for users of blockchain systems, as well as how incentivization can backfire in the
emergence of unexpected market events [15]. For example, ill-reasoned use of combined token functionalities, asset
and payment tokens, can hinder the growth of token ecosystems [16]. Furthermore, excessive token liquidity decreases
the market capitalization of a token economy with respect to future profits, setting a financing limit [17]. Sockin &
Xiong [18] warn against a token price collapse, a situation where there is no equilibrium price that would match the
token supply with the demand, commonly caused by speculation.
One of the largest empirical examples of poor tokenomic design is the collapse of Luna and TerraUSD tokens
in 2022, causing thousands of stakeholders to lose their investments [19]. Blockchain collapses were caused by the
excessive accumulation of risk within the cryptocurrency ecosystem [15]. That is, inadequate risk management often
coincided with poor product design, so tokens were created in a way that left them vulnerable to significant losses
when unexpected events occurred. In 2022, many digital asset initiatives and token releases continued to cause damage
to the people who used them and those who bought the tokens [20]. These individuals often ended up with nothing
more than worthless tokens after an initial period of success.
Prior work proposes several conceptual frameworks for token economies (e.g., [21, 22, 12, 6]) and a growing
body of domain-specific design discussions (e.g., industrial, automotive, Web3 gaming) [23, 24, 25, 26]. However,
end-to-end guidance that (i) integrates incentives, governance, and tokenomics in a single coherent structure, (ii)
provides stepwise design propositions with explicit decision points and trade-offs, and (iii) is grounded in empirical
evidence from concrete token-economy development efforts remains limited. Moreover, several studies address one
of the three dimensions in isolation, such as governance [27] or tokenomics in ICO settings [28], while incentive-
mechanism modeling is often treated separately [29].
In the domain of DAOs, research emphasizes the importance of token economy design for system utility, with
references to architecture models that incorporate incentive mechanisms [30, 31]. Furthermore, the need for a com-
prehensive software engineering method for token economy design in DAOs is highlighted in [32], along with the
2

---

## Page 3

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–273
support tool to validate DAO incentive mechanisms, which are proposed in [33]. However, a complete software
engineering method for this scope is not yet developed.
Taking these challenges into account, the objective of this study is to propose a Token Economy Design Method
(TEDM) as a design-science artifact consisting of structured design propositions grounded in an empirical token-
economy development case. We follow a Design Science Research (DSR) approach in which iterative design cycles
address the following research questions [34]:
•Main Research Question:How can a token economy be designed in a structured way by explicitly integrating
incentives, governance, and tokenomics?
•Subresearch Question 1 (RQ1):What design considerations and decision points support incentive-mechanism
design in token economies?
•Subresearch Question 2 (RQ2):What design considerations and decision points support governance design
in token economies?
•Subresearch Question 3 (RQ3):What design considerations and decision points support tokenomics design
in token economies?
To this end, Section 2.1 describes the proposed DSR approach. The existing literature is examined in Section 2.2
to identify the theoretical frameworks overlapping for token economy design and to introduce the three pillars of the
proposed design artifact. In Section 2.3 the Currynomics token system use case is introduced that helps the search
process for effective design principles. The Token Economy Design Method (TEDM) is introduced in Section 3.
Each of the components of the design artifact is expanded upon in Sections 3.1, 3.2, 3.3, respectively, to present the
results of each sub-research question. Section 4 presents a discussion of how the artifact was evaluated, first, through
a case study that evaluates the real-life practicality of the proposed design guidelines when used by the Currynomics
ecosystem and, second, additional expert interviews. Finally, Section 5 concludes the study with recommendations
for future research.
2. Preliminaries
This section provides the background information necessary to understand the main contributions of the article.
Firstly, in Section 2.1, the methodology adopted for the study and the data collection and analysis methods are de-
scribed. Subsequently, Section 2.2 presents the related work, and Section 2.3 describes the use case.
2.1. Methodology and Data
The methodology chosen for this study is Design Science Research (DSR), as it is well suited for sociotechnical
systems such as token economies [34]. The purpose of the study is to develop and evaluate a Token Economy De-
sign Method (TEDM) that supports the early-stage structuring of token-economy design decisions across incentives,
governance, and tokenomics. The DSR artifact consists of a practical guide that represents the core structure of the
method and is informed by concepts derived from extant literature (Section 2.2) and refined through an empirical
design case.
In line with DSR, the knowledge base of the study includes (i) foundational theories and frameworks relevant to
token economies (Section 2.2.1) and (ii) established research methodologies and design-oriented approaches used for
adjacent problems in the literature (Sections 2.2.3, 2.2.4, and 2.2.5). Based on this knowledge base, we identify three
key design pillars that organize the method: incentive structures, governance, and tokenomics. Importantly, TEDM
is not intended as a predictive model of economic performance. Rather, it operationalizes empirically grounded
design propositions that make decision points, trade-offs, and risks explicit, thereby supporting analytical reasoning
and communication during token-economy development. Figure 1 illustrates the DSR research approach followed
in this study. DSR aims to ensure the relevance of developed artifacts by targeting concrete business needs. The
environmental component of the DSR study captures key needs, shortcomings, and objectives of the focal organization
and identifies resource constraints. Consistent with DSR, the contribution of this work lies in articulating a reusable
design artifact grounded in empirical evidence. The evaluation is formative and supports analytical transferability (i.e.,
3

---

## Page 4

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–274
People
*Users
*Investors 
*Community members 
Organizations 
*Partners
*Currynomics Labs OÜ
*Currynomics DAO
Technology 
* Application protocols to
accommodate the RedCurry token
and the DAO token 
 
Frameworks
*Special-purpose token economy
design frameworks 
*Token classification and taxonomy
frameworks 
* Token economy incentives',
governance and tokenomics
frameworks
Methodology
* Artefact evaluation criteria
* Semi-structured interviews
* Thematic analysis 
 
Environment IS Research Knowledge BaseRigor Relevance 
Business
 needs Applicable
 knowledge
Application in the
Appropriate Environment
Contribution to the
 Knowledge Base
Evaluate
*Currynomics use case
*Case study
*Expert interviews
*Curve Finance and
Uniswap use case
Develop
*Artefact
Refine
Evaluate
Figure 1. Design Science Research (DSR) framework adopted in this study [34].
applicability-by-reasoning across contexts), rather than statistical generalization or causal proof of superior economic
outcomes. Our case study is focused on the Currynomics ecosystem, whose environment includes stakeholders (users,
investors, and community members), organizations (partners, Currynomics Labs OÜ, and Currynomics DAO), and
the technology utilized in the form of application protocols to accommodate the Redcurry token and the DAO token.
Each of these elements is described in detail in Section 2.3.
2.1.1. Artifact derivation and traceability
The TEDM was derived through an iterative and qualitative process consistent with Design Science Research
(DSR) for sociotechnical systems [34]. First, we conducted a scoped synthesis of extant research on token econ-
omy design, focusing on recurring constructs, decision points, and trade-offs reported across incentives, governance,
and tokenomics (Section 2.2). Second, we performed concept extraction and clustering to consolidate overlapping
constructs into a coherent set of design propositions. This synthesis resulted in three macro-dimensions that repeat-
edly co-occur in prior work and in practice: incentive structures, governance, and tokenomics. Third, the resulting
propositions were iteratively refined through design cycles with the Currynomics case, where each step was checked
for (i) goal clarity, (ii) operational interpretability, and (iii) traceable grounding in either literature, case evidence, or
both. Accordingly, the TEDM should be interpreted as empirically grounded, reusable design guidance with explicit
boundary conditions, rather than a statistically generalizable predictive model of token-economy outcomes.
2.1.2. Data Collection and Analysis
In DSR artifact evaluation, expert interviews can be an effective method for eliciting informed judgments on the
artifact’s utility and interpretability [35]. Semi-structured interviews are a valuable means of collecting data by getting
insights from experts about their practices, beliefs, experiences, and points of view [36]. Each TEDM component
(Sections 3.1, 3.2, and 3.3) underwent four iterative cycles of development, evaluation, and refinement. In the first
cycle, concepts derived from extant literature were consolidated into initial design propositions and arranged into
a stepwise method. The artifact was then evaluated through a use-casedemonstration, i.e., a simplified evaluation
that shows how an artifact can be used to address a specific problem instance [37]. This step involved applying
the prescribed TEDM steps to the Currynomics case. A purposive sample of two Currynomics representatives were
first introduced to the visual method steps and subsequently instantiated the goal model shown in Figure 4 based
on project requirements. The artifact utility was then evaluated through semi-structured interviews with the two
Currynomics representatives (IN1, IN2). Additional feedback was collected from a distinct purposive sample of
4

---

## Page 5

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–275
three industry experts external to the case (IN3, IN4, IN5). A final evaluation step consisted of applying the TEDM
categories to compare two existing token economies as a comparative demonstration, aiming to assess whether the
method’s constructs and decision points remain interpretable beyond the focal case. This step does not test economic
performance outcomes, but supports analytical transferability of the method’s structuring logic across contexts.
The objective of the interviews is to evaluate the artifact’scompleteness,simplicity,understandability,operational
feasibility, and perceivedaccuracy, evaluation criteria commonly adopted in IS/DSR artifact evaluation [37]. The
selection of these criteria is inspired by van Pelt et al. [38], who developed and evaluated a blockchain governance
framework with a narrower scope than the present study. Interviews were transcribed using the Transkriptor software2.
The collected data were analyzed via thematic analysis following the six steps outlined by Braun and Clarke [39],
using the coding functionality of MAXQDA 3. At the beginning of each interview, participants were informed about
the purpose of the study and the interview structure, and consent to record the interview was requested. In the first
part, participants were introduced to TEDM and invited to comment on any design topic they considered salient. In
the second part, the following questions were asked:
1. How do you perceive the completeness of the method?
2. How would you comment on the simplicity of the method?
3. How do you perceive the understandability of the method?
4. What are your thoughts on the operational feasibility of the method?
5. What are your thoughts on the perceived accuracy of the method?
In Table 1, we present the notation adopted in the use case examples to illustrate the method. The notation, which is
part of Agent-Oriented Modeling (AOM), was chosen due to its simplicity and explainability, as well as its suitability
for sociotechnical systems such as token economies [40]. In AOM, goal models are used to represent and analyze
system requirements. The goals that agents pursue correspond to the functional requirements of the system, while
the quality goals correspond to the quality attributes associated with the given functions. Goals are hierarchically
decomposed into sub-goals. The following section presents a review of the literature that contextualizes the foundation
of the method.
2.2. Literature Review
This literature review organizes prior work into four complementary streams. First, we discuss scholarly frame-
works and taxonomies that conceptualize token economies at a theoretical level (Section 2.2.1). Second, we review
special-purpose token-economy design approaches proposed for specific domains (Section 2.2.2). Third, we examine
literature addressing one of the three recurring token-economy design dimensions in isolation: governance (Sec-
tion 2.2.3), incentives (Section 2.2.4), and tokenomics (Section 2.2.5). Finally, we synthesize the resulting gaps and
motivate the need for a stepwise, empirically grounded design method that integrates these dimensions.
2.2.1. Theoretical Frameworks and Taxonomies of Token Economies
The academic literature reports several theoretical frameworks that address token-economy design from different
perspectives. Benedetti et al. [12] examine typical tokenomic designs, explore regulatory approaches, and review
applications of utility tokens in domains such as decentralized finance and virtual reality platforms. Lage et al. [21]
analyze fundamental characteristics of blockchain-based decentralized platform models. Khamisa [6] proposes a
conceptual structure for token-economy design that includes the definition of economic goals, token design choices,
and governance considerations.
Barrera and Hurder [22] introduce theHouse Framework(Figure 2), which decomposes the economic design of
blockchain-based ecosystems into five layers: (1) value proposition, (2) financing, (3) incentives, (4) token design,
and (5) governance. While the framework is useful for conceptual decomposition, it remains high-level and provides
limited guidance on how to navigate among concrete design options within and across layers.
In addition to conceptual frameworks, several works focus on token classification and taxonomy. Freni et al. [41]
map channels through which tokens can add value (technology, behavior, coordination) and highlight the relevance of
2https://app.transkriptor.com/uploader
3https://www.maxqda.com/
5

---

## Page 6

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–276
Elements Description Notation
Goal A particular situation or state of things in
the world that the stakeholders wish to at-
tain.
Quality Goal A set of precise standards or criteria that
must be met to achieve a broader goal.
Decomposition Relationship to illustrate the connection
between two distinct goals, namely a
higher level or parent goal and a lower
level or sub-goal.
Association Relationship used to connect a goal with
other related elements that aid in defining
or describing the goal.
Example A concrete instantiation used to illustrate
a goal in the case study
Table 1. Goal Model Notation adopted in the use case.
token characteristics, monetary policy, and incentive mechanisms. Oliveira et al. [2] propose a guide to token design
based on literature review and expert interviews. Tapscott [42] discusses token standards and a taxonomy-oriented
perspective on tokens as digital assets. Overall, these contributions provide valuable constructs and categories, but
they typically do not translate the constructs into an end-to-end, stepwise design method that integrates incentives,
governance, and tokenomics while making decision points and trade-offs explicit.
Positioning relative to practitioner token-engineering and quantitative design frameworks.In industry and adjacent
research communities, token-engineering approaches often emphasize quantitative refinement, simulation, or state-
space exploration. Examples include the simulation tooling and methodology developed by BlockScience4 and related
4https://block.science/
Value proposition 
Financing 
Contract design Market design Information systems
Tokenization
Governance
Participants Proposal processDecision process
Property rights Platform subsidies Monetary policy 
Cost of development Investor rights Equity / token sale
Use cases Target customers Strategy
Incentive layer
Token layer 
Contract terms 
Dispute resolutionEscrow
Matching mechanisms
PricingTerm negotiations
Reputation systems
IdentityEducation
Figure 2. The House Framework [22].
6

---

## Page 7

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–277
work (e.g., [33, 43]), as well as state-space modeling frameworks for engineering crypto-economic systems (e.g., [44,
45]). These approaches are particularly valuable for stress testing, parameter tuning, and exploring system dynamics
once a candidate design is specified. However, they typically presuppose that the designer has already articulated
(i) system goals, (ii) stakeholder roles, (iii) governance decision rights, and (iv) token issuance/allocation policies in
a sufficiently structured way to be operationalized in models or simulations. Against this background, the TEDM is
positioned as a complementary, design-science artifact that supports thequalitative and structured derivationof token-
economy requirements and design propositions across incentives, governance, and tokenomics, thereby producing
inputs that can subsequently be refined and validated quantitatively.
2.2.2. Special Purpose Token Economy Design
A large part of token-design research focuses on special-purpose cases and domain-specific constraints, which
limits transferability across domains. For instance, Wang et al. [23] and Dasaklis et al. [46] focus on supply-chain
contexts, while Hofmann et al. [24] address collaborative manufacturing. Hasan et al. [47] and Zhang et al. [25]
propose domain-specific designs for the automotive sector. Direr et al. [26] develop an economic design for a Web3
game. Hou et al. [48] propose a mechanism for a voluntary public carbon market using a dual-token design. Kim
et al. [49] propose a token-economic design for the Insolar business network. While these contributions are valuable
within their domains, they typically do not provide a broadly applicable, stepwise method that integrates governance,
incentives, and tokenomics for token economies with heterogeneous stakeholders and objectives.
2.2.3. Governance
Several studies highlight the interconnection between token economies and DAOs, since token-based governance
both relies on tokens (e.g., voting power and membership) and directly affects token supply, distribution, and incen-
tive alignment. Avanzo et al. [32] emphasize the complexity of token-economy design in DAO settings and argue
for modeling languages and methods that support governance grounded in sound token-economy design. Empirical
studies examine governance in prominent DAOs, such as voting-power concentration and participation (e.g., Com-
pound, Uniswap, ENS) [50], and the impact of governance decisions on token economies (e.g., MakerDAO) [51, 52].
Venugopalan et al. [53] consider the interconnection among governance, tokenomics, and incentives in DAOs, but the
resulting method and tooling primarily target governance-related tensions and do not constitute an integrated, stepwise
design method across all three pillars.
Additional work proposes governance models, evaluation perspectives, and analytical tools for blockchain gov-
ernance. Bena and Zhang [27] study decentralized governance under heterogeneous contributor costs. Kiayas and
Lazos [54] discuss evaluation of governance procedures. Liu et al. [4] propose a governance framework including
factors such as decentralization, authority, incentives, and accountability. Fernandez et al. [55] simulate voting-right
concentration after token launches. Mohan et al. [56] discuss challenges such as Sybil resistance and plutocracy.
Wang et al. [13] propose an ontology of blockchain governance that includes incentive-related concepts. Overall, this
stream provides important constructs and empirical insights, but practical stepwise guidance that also incorporates
tokenomics decisions (issuance schedules, allocation strategies, price-management mechanisms) remains limited.
2.2.4. Incentive Structures
A substantial body of work addresses incentives in blockchain systems, including surveys of incentive mecha-
nisms [57, 58, 59, 29]. However, many contributions focus primarily on mining and base-layer protocol incentives
rather than application-level token economies. Complementary work examines how token design shapes partici-
pant incentives in ledger-based ecosystems, sometimes in domain-specific contexts (e.g., supply chains or data mar-
kets) [60]. Others propose incentive models aimed at improving business-market profitability [61] or analyze token
incentives in competitive platform settings (e.g., decentralized exchanges) [62]. DAO-oriented models frequently in-
corporate incentives as a core component [30, 31] but typically provide limited stepwise design guidance and often
do not integrate tokenomics decisions such as issuance, allocation, and price-management policies.
2.2.5. Tokenomics
Tokenomics is frequently studied under the lenses of token monetary policy, supply strategies, and distribution
mechanisms. Prior work examines airdrops and strategic behaviors (including Sybil participation) [63, 64], relates
7

---

## Page 8

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–278
tokenomics to concepts in finance (e.g., shares, profits, dividends) [65], and proposes valuation perspectives for
DAOs [66]. Other studies focus on ICO design and issuance caps [28], as well as token launch practices and val-
uation methods for digital assets [20]. Additional work analyzes wealth concentration [67, 68, 69] and mechanisms
such as burns and buybacks through a corporate-finance lens [70].
Among the closest stepwise contributions, Kim and Chung [71] analyze the tokenized social network Steemit and
propose an eight-step design flow for a successful ICO. While valuable, this flow is tailored to an ICO setting and
does not address governance-property specification and incentive-structure design in an integrated manner.
Synthesis and gap.Across the reviewed streams, prior work provides (i) conceptual frameworks and taxonomies
that define relevant constructs, (ii) domain-specific token designs that incorporate local constraints, and (iii) pillar-
specific insights on governance, incentives, or tokenomics. Nevertheless, empirically grounded, stepwise guidance
that integrates the three pillars into a coherent design method, while making decision points, trade-offs, and bound-
ary conditions explicit, remains limited. This motivates the development of the Token Economy Design Method
(TEDM) as a DSR artifact that consolidates and operationalizes design propositions across incentives, governance,
and tokenomics, and evaluates them formatively through an empirical design case and expert feedback.
2.3. Use Case - Currynomics Ecosystem
In this study, the TEDM is formatively evaluated using the Currynomics ecosystem as an empirical design case.
The case is suitable because it entails an integrated token-economy design problem in which incentives, governance,
and tokenomics must be specified jointly under real-world constraints (e.g., asset backing, organizational roles, and
stakeholder trust). At the same time, we explicitly treat Currynomics as a bounded problem instance: it does not
represent all classes of token economies (e.g., governance-minimal protocols or purely algorithmic stablecoins), and
the case is used to ground and refine the method rather than to claim statistical generalization.
Currynomics is a decentralized blockchain ecosystem that links the value of its stablecoin (the Redcurry token) to
the net asset value (NA V) of a commercial real estate (CRE) portfolio [72]. The design of Redcurry is motivated by
a common challenge among stablecoins: token holders often cannot fully verify or trust the validity and availability
of the underlying collateral, which increases perceived shortfall risk and threatens the peg [73]. In Currynomics,
Redcurry represents the value of the CRE portfolio and is designed to maintain the peg through an asset-backed
mechanism [72].
By functioning as a means of payment and a store of value, Redcurry resembles established stablecoins such as
USDT, but differs in that its supply is not fixed [72]. Moreover, Redcurry is not a pure asset token: holders do not
obtain direct legal rights to specific underlying properties. Instead, the ecosystem reinvests financial gains from the
portfolio back into the system. In this sense, the design aims to “commodify” real estate by creating a bridge through
which capital can move from the traditional economy to the crypto economy while maintaining an asset-backed value
anchor.
The Currynomics ecosystem is summarized in Figure 3. The core bodies of the ecosystem are marked in red:
Redcurry Holding mints Redcurry tokens, acquires real estate in the CRE portfolio, and distributes tokens to partners.
Marked in orange are the developers and maintainers of the ecosystem: Currynomics Labs OÜ provides development,
marketing, and management services, while Currynomics DAO is the governing body of the token economy and uses
DAO tokens in its decision-making operations. Currynomics DAO operates as a decentralized organization that is
distinct from the other legal entities in the ecosystem.
The token economy supporting Redcurry faces multiple challenges originating from the surrounding business en-
vironment. A key challenge is to identify the levers that build trust for users (Redcurry holders) to purchase and
retain the token in the long term, given the availability of competing investment alternatives outside the crypto econ-
omy (e.g., low-risk real-estate funds). Trust is tightly connected to governance design, raising questions about whether
(and how) community participation can be sustained without exposing the system to governance capture or misaligned
incentives. Finally, the introduction of a governance token (DAO token) requires careful tokenomics decisions con-
cerning issuance timing, allocation, and distribution mechanisms, as these choices shape both governance power and
long-term incentive alignment.
8

---

## Page 9

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–279
CRE Portfolio
Currynomics Labs
OÜ
owner Currynomics
Foundation
governance
contributes to the
development pool of 
Currynomics DAO
receive
tokens
RedCurry Token
(digital currency)
invests rent
income into
development &
management &
marketing services
mints new tokens
 at NAV
transaction
fees into
DAO treasury
RedCurry Holding
tokens sold
to users 
purchase the
tokens from
Partners
(licenced financial
service providers)
Users 
Figure 3. Stakeholder map of the Currynomics ecosystem.
3. Token Economy Design Method
The token-economy design aspects introduced in Sections 2.2.3, 2.2.4, and 2.2.5 are consolidated into the Token
Economy Design Method (TEDM), which we describe in this section.
TEDM does not follow a predominantly quantitative approach (e.g., optimization or simulation-based search), as
commonly emphasized in parts of the practitioner token-engineering literature. Instead, TEDM emerged through an
iterative synthesis of relevant scholarly literature and formative evaluation through an empirical design case. This ap-
proach deliberately prioritizes actionable relevance and interpretability over formal completeness; accordingly, TEDM
should be understood as a set of empirically grounded design propositions that make decision points, trade-offs, and
risks explicit, rather than as a predictive model of token-economy outcomes.
TEDM is applied to the Currynomics case introduced in Section 2.3. The results are evaluated through a case-
based demonstration and expert interviews (Section 4). Figure 4 summarizes the three sequential method components
and their stepwise structure.
TEDM consists of three components: incentive structures, governance, and tokenomics. Each component is
detailed in the subsections that follow.
3.1. Incentives
Well-designed incentive structures are necessary to align stakeholder behavior with the token economy’s goals.
As discussed by Yoo et al., it is crucial to understand which user groups participate in the token economy and what
benefits they receive from reward and penalty mechanisms [74]. According to [6], key principles for incentive design
are to encourage actions that advance the primary objectives of the token economy, discourage destructive behavior,
and account for heterogeneous stakeholder needs. Incentives are also relevant because they act as remuneration
mechanisms that can support the long-term viability of the ecosystem [75].
This subsection responds to RQ1 (Section 1) by providing stepwise guidance for establishing incentive mecha-
nisms. In TEDM, each step is formulated as a design proposition: it clarifies the design goal addressed, the rationale
for the step, and the expected output artifact thereby making trade-offs and risks explicit rather than providing a purely
procedural checklist.
Steps 1 and 2 define the token economy value proposition in terms of (i) actors and (ii) functions the system
is expected to perform. After the value proposition is established, Step 3 identifies desirable behaviors that support
9

---

## Page 10

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2710
Governance
Defined level of 
decentralisation
Defined
governance
areas 
Core voting mechanism
Defined 
stakeholders 
General updates 
to the protocol
Community matters
Marketing and
branding matters 
Distribution of funds
Defined need for on-chain
/ off-chain mechanisms
Regulation &
compliance
Efficiency & speed
Security & control
Centralisation
Transparency
Autonomy & resilience
Greater innovation
Decentralisation
Transparency,
accountability, inclusivity
Subject to security risks;
computational-resource heavy
On-chain
Greater flexibility for 
complex decision-making
Prone to centralisation
Off-chain 
Property
Keep governance as simple
as possible
Explanation
Desired voting
mechanism properties 
Participants need to have 'skin in
 the game' - via token staking or reputation
Protection against plutocracy; smaller 
stakeholders have an equal standing
Voters can have a larger influence over 
decisions they are particularly interested in
The capability to decide on time-sensitive 
governance areas  
Support mechanisms 
for voting
Inaction from decision fatigue
Inaction from rational ignorance
Sybil attacks 
Pros
Cons
Issue Support mechanism
Prediction markets, algorithmic screening
Delegated voting, better education
Proof of Personhood (PoP) systems
Protection against Sybil attacks
simplicity
accountability
inclusivity
time efficiency
preference
intensity
security
STEP
2STEP
1
STEP
3
STEP
4
STEP
5
STEP
6
STEP
7
1T1V
Quadratic Voting
Time-Weighted
 
Reputation-Weighted
Tokenomics
Token release
schedule
incentivises token
usage adaptive
sustainable
Token price 
stability
Amount 
Timing
Distribution
mechanisms
Token
inherent 
value
Price
management 
mechanisms
Shorter timeline; 
greater control over investors
Use caseDistribution
mechanism
Private sale
Public sale For building a larger 
community; increasing demand
Secures critical 
mass of 
early interested users
Timing strategy
Pre-listing
Post-listing
More accurate pricing; 
enables fair token 
launches
Hard to price 
the token 
 Harder to
 generate 
user interest
Distribution
mechanism
Inflationary
Deflationary To induce scarcity; 
for long-term store of value
To encourage spending; 
flexibility to adjust to 
market conditions
Use case
Governance rights 
Value from network
Claim to earnings
Representation
of an asset
Mechanisms
Reducing token
 supply
Mechanism type
Promotes token
holding
Token burns;
token buybacks
Token staking; 
token vesting
maintains token
price stability 
STEP
1
STEP
2
STEP
3
STEP
4
STEP
5
Governance
matches stakeholder 
expectations with token 
economy functions 
Incentive 
mechanisms
Defined token 
value proposition 
Defined token economy
stakeholders Defined token
economy functions
Defined desirable
 behaviours 
contribute to token
economy goals
Using the product
Investing
Contributing to development
Participation in governance
File storage network
Investment vehicle
Wealth protection
Trading platformDigital currency
Investors
Miners
Developers
Exchanges
Users
Community 
Defined need for (non-)
monetary incentive mechanisms
incentive-
aligning
promote user
acquisition
Social network
Token rewards 
Revenue share 
Dividends
Token price
appreciation
Monetary 
Access to product
Participation in
governance
Reputational gains
Network effects
Gamification
Non-monetary
Tied to monetary outcome 
Costly 
Effective in short-term
Monetary 
Community-oriented outcome
Effective in long-term
Less expensive to distribute
Non-monetary
STEP
2
STEP
1
STEP
3
STEP
4
STEP
5
IncentivismTokenomics
Advantages Disadvantages
Figure 4. Token Economy Design Method (TEDM).
10

---

## Page 11

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2711
Incentive Design Goals TEDM Incentive design
Defining the token economy value proposition 1) Identify the token economy stakeholders
2) Define the token economy functions
Identifying behaviors that contribute to system utility 3) Determine desirable behaviors
Selecting incentive mechanisms to promote desirable behaviors 4) Define the type of incentive mechanism.
5) Specify incentive mechanisms
Table 2. Incentive design goals and corresponding TEDM steps.
system utility. Steps 4 and 5 then determine the type of incentives required and specify concrete incentive mechanisms.
Each step is defined below, followed by its application to the Currynomics case.
3.1.1. Step 1 - Identify the stakeholders
Identifying stakeholder categories and their motivations is a key prerequisite for incentive design [6]. Prior work
proposes different stakeholder taxonomies. Davidson [76] distinguishes maintainers, contributors, and users. Allen
and Berg [77] include token holders, developers, founding teams, miners/validators, and indirect stakeholders such as
government and venture capital. V oshmgir [78] highlights nodes, developers, miners, and market actors (e.g., market
makers). Liu et al. [4] distinguish project teams, node operators, users, application providers, and regulators. A single
individual may belong to multiple stakeholder groups simultaneously.
In the Currynomics case, we identify:
•Users: Redcurry token holders who purchase and hold the token primarily for financial purposes.
•Partners: licensed financial institutions that purchase tokens from Redcurry Holding and distribute them to end
users for a transaction fee.
•Developers: Currynomics Labs OÜ, providing development, marketing, and management services for the
ecosystem.
•Community members: holders of the Currynomics governance token (DAO token) participating in governance
processes.
•Investors: actors providing capital either by purchasing/holding governance tokens or by investing in Curry-
nomics Labs OÜ to support ecosystem development.
3.1.2. Step 2 - Identify the functions of the token economy.
Blockchain ecosystems connect stakeholders to create value based on shared resources [22]. Value creation can
include the transfer of goods, means of payment, monitoring of asset status, enabling access to a service/product, or
voting [3]. Sockin and Xiong [18] argue that value may stem from (i) enabling transactions among a large set of
users or (ii) providing an investment vehicle. From a financial perspective, systems may also aim at price stability (as
common in stablecoins) or wealth protection against inflation [79].
The core objectives of the Currynomics ecosystem are predominantly financial. The Redcurry token, minted
against real-estate acquisition, is intended to support:
•wealth protection and liquidity parking for savings;
•an investment vehicle linked to CRE portfolio value appreciation;
•a means of payment;
•collateral utility in credit settings enabled by price stability.
11

---

## Page 12

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2712
3.1.3. Step 3 - Define the desirable behaviors
In an effective token economy, participants’ actions should support system utility rather than only individual
short-term gains [6, 80]. Khamisa [6] refers to this astoken–network fit. Yoo [74] argues that desirable behaviors are
determined by whether actions add long-term economic value to the ecosystem. Long-term participation and retention
are frequently highlighted as particularly valuable behaviors [74, 81].
In Currynomics, the following behaviors were identified:
•Users: hold Redcurry as a long-term store of value and use it without persistently selling below its reference
value/market price anchor.
•Community members: participate in discussion and decision-making via the DAO token.
•Investors: provide development liquidity (e.g., by purchasing/holding the DAO token or investing in the devel-
opment entity).
While Redcurry can support multiple financial functions, its primary intended use in the early phases is long-
term holding to build stability and trust. Trading can be neutral in later phases provided it does not systematically
undermine the price anchor during low-liquidity periods.
3.1.4. Step 4 - Select incentive-mechanism types
Incentives can be monetary or non-monetary. Monetary incentives includetoken rewardsfor actions [4],stak-
ingmechanisms that lock tokens to support ecosystem operations [41, 66],liquidity miningby providing liquidity
to DEX/DeFi protocols [62], andgrowth expectationsconcerning platform success that motivate participation with-
out direct token earnings [41, 16]. Non-monetary incentives discussed in the literature include access to services,
reputation mechanisms, and governance participation [41], as well as network effects and gamification [71].
Incentive Mechanism Type Mechanism Description
Monetary
Token Rewards (User actions) [4]
Staking (Token lock-up for support) [41, 66]
Liquidity Mining (Earning via DEX/DeFi) [62]
Growth Expectations (platform success) [41, 16]
Non-Monetary
Access to services [41]
Reputation mechanisms (enhanced reputation) [41]
Governance Participation (decision-making) [41]
Network Effects [71]
Gamification [71]
Table 3. Monetary and non-monetary incentive-mechanism types.
3.1.5. Step 5 - Specify incentive mechanisms
Concrete incentive mechanisms should (i) contribute to token-economy goals, (ii) motivate behavior that supports
system utility, and (iii) attract and retain participants. These can be treated as quality goals, i.e., criteria that incentive
mechanisms should satisfy.
In Currynomics, Redcurry Users are primarily motivated by monetary incentives, in particular gains associated
with Redcurry value appreciation and stability. By contrast, the DAO token primarily aims to incentivize governance
participation and coordinated decision-making. Accordingly, non-monetary incentives such as reputational gains and
the intrinsic value of governance participation are particularly relevant for community members, while the potential
appreciation of the DAO token can serve as an additional monetary incentive for investors.
3.2. Governance of a Token Economy
Figure 4 summarizes seven governance-design steps in TEDM. The goal is to structure governance decisions
according to project requirements while making explicit the main trade-offs and risks (e.g., plutocracy/governance
capture, Sybil attacks, low participation, and decision fatigue) [82].
12

---

## Page 13

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2713
3.2.1. Step 1 - Define governance areas
Governance areas depend on the system goals and the scope of what the community is allowed (and able) to
decide. Governance decisions can include protocol upgrades and parameter changes, ecosystem service/product de-
velopment, recruitment and management, treasury and token-asset management, and changes to governance rules
themselves [6]. Governance may also include emergency actions (e.g., triggering shutdown modes) and infrastructure
funding decisions [83], as well as compensation and resource-allocation policies [22].
In Currynomics, we identify four broad governance areas:
•Treasury management: allocation and management of the DAO treasury funds.
•Governance and process: governance structure, voting procedures, community goals, and community senti-
ment toward proposals.
•Protocol upgrades: implementation of upgrades, adjustment of global and treasury-specific parameters, and
replacement of modular smart contracts.
•Tokenomics: decisions related to the issuance, allocation, and distribution of governance tokens and other
token-policy parameters.
3.2.2. Step 2 - Define governance stakeholders and roles
For each governance area, the relevant stakeholders and their roles should be identified (e.g., who proposes, who
deliberates, who votes, who executes, and who is accountable). In Currynomics, the stakeholder groups are defined in
Section 3.1.1; here, TEDM uses these categories to assign decision rights and responsibilities across the governance
areas.
3.2.3. Step 3 - Define the target level of decentralization
At this stage, the desired degree of decentralization should be determined. Liu et al. [4] distinguish (i)private and
centralizedecosystems (e.g., enterprise blockchains), (ii)public but centralizedtoken economies where governance
is formally open but effectively controlled by privileged actors, and (iii)public and decentralizedsystems without
privileged stakeholders, enabling broad participation.
To operationalize decentralization targets, public token economies are commonly assessed using distribution-
based indicators such as theGini coefficientand theNakamoto coefficient[84, 69]. The Gini coefficient quantifies
inequality in a resource distribution (e.g., voting power), ranging from 0 (perfect equality) to 1 (maximal concentra-
tion):
G=
Pn
i=1
Pn
j=1 |xi −x j|
2n2 ¯x .(1)
A higher Gini value indicates stronger concentration and, therefore, greater centralization.
The Nakamoto coefficient captures how many independent entities are required to control more than 50% of a
resource (e.g., voting power):
N=min
k

kX
i=1
S i > 1
2
nX
j=1
S j
 .(2)
Lower Nakamoto values indicate that few entities can form a controlling coalition (more centralization), while
higher values indicate broader dispersion of control.
These indicators can support (i) setting decentralization targets at design time and (ii) monitoring whether the
implemented governance remains aligned with those targets once the system is operational. In practice, decentraliza-
tion is multi-dimensional (it may differ across token ownership, voting participation, proposer power, and execution
privileges), so these metrics should be interpreted as informative signals rather than exhaustive measures.
In Currynomics, some governance decisions remain necessarily centralized due to legal and operational con-
straints. For instance, Redcurry issuance is governed by code, while the reserve-asset composition is managed by
an investment board. The composition of the Currynomics Foundation board, which oversees ecosystem integrity, is
13

---

## Page 14

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2714
also not subject to community votes. However, multiple governance areas remain open to decentralized participation,
allowing community members to influence decisions while maintaining essential oversight.
3.2.4. Step 4 - Define the need for on-chain and off-chain mechanisms
On-chain governance refers to processes where proposals and voting are executed through the protocol (e.g., via
smart contracts), potentially enabling automated enactment of accepted changes [85]. Off-chain governance refers to
deliberation and decision-making processes that occur outside the protocol (e.g., forums, social channels), often used
for discussion, signaling, and agenda setting [70].
Currynomics aims to keep governance as transparent and inclusive as possible; therefore, most governance areas
are decided via on-chain voting mechanisms. However, some stages are intentionally off-chain, such as proposal
filtering and early deliberation (“temperature checks”) in a community forum. If a proposal passes the temperature
check, it can be escalated to a formal vote. This hybrid structure balances transparency and inclusivity with practical
deliberation needs that are difficult to accommodate purely on-chain.
3.2.5. Step 5 - Define desired voting-mechanism properties
No single voting mechanism is universally optimal across criteria; selection involves trade-offs [54]. In TEDM,
candidate mechanisms (Step 6) are assessed against the following desired properties:
•Simplicity: procedures should be understandable and implementable without unnecessary complexity.
•Accountability: participants should have “skin in the game” (e.g., committed tokens, time, or reputation) to
promote responsible decisions [54].
•Inclusivity: mechanisms should avoid systematically marginalizing small stakeholders purely due to limited
financial means [56].
•Time efficiency: urgent decisions should be feasible within time constraints [54].
•Intensity of preferences: mechanisms should allow expressing how strongly voters care about an issue [56].
•Security: mechanisms should mitigate voter fraud (e.g., Sybil attacks) [56] and reduce centralization/capture
risks associated with concentrated voting power [86].
3.2.6. Step 6 - Core voting mechanisms
We distinguish four core voting-mechanism families discussed in the literature:
•1-token-1-vote (1t1v)assigns voting power proportional to token holdings [56]. It is simple and time-efficient,
but can enable vote buying and plutocracy, reducing inclusivity and increasing capture risk [86].
•Time-weighted votingintroduces a time commitment to increase accountability and mitigate short-term capture
dynamics [56]. Time-weighting can improve accountability/security compared to pure 1t1v, but often reduces
time efficiency and increases complexity. Common variants include:
– Conviction voting: sustained support increases “conviction” for a proposal over time [87].
– Vote-escrow (ve-token): users lock tokens for a period to receive increased voting power [56].
– Bond voting: voting power increases with staked resources via bond-like commitments [56].
•Reputation-weighted votingweights votes by reputation rather than token wealth [88]. This can improve
inclusivity, but requires additional mechanisms to quantify and update reputation and can introduce new attack
surfaces and governance overhead. It is used, for example, in Colony [56].
•Quadratic votingallocates voice credits such that the marginal cost of additional votes increases quadratically,
aiming to reflect intensity of preferences [89, 90, 91]. It can improve inclusivity relative to 1t1v, but its real-
world robustness and resistance to strategic behavior remain debated [90].
14

---

## Page 15

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2715
Table 4. V oting-mechanism families mapped to desired properties, with scores derived from the referenced literature.
The mechanisms are mapped to the desired properties in Table 4. In the table, a full node indicates strong fulfill-
ment, a half-filled node indicates partial fulfillment, and an empty node indicates weak fulfillment based on the cited
literature.
Achieving both Sybil resistance and plutocracy resistance simultaneously is challenging when voting power de-
pends predominantly on a single factor (e.g., staked tokens) [56]. Including time or reputation can mitigate certain
risks, but does not eliminate Sybil behavior or capture incentives entirely; therefore, no mechanism achieves a perfect
score in thesecuritydimension.
In Currynomics, the DAO prioritizesaccountabilityandsecuritydue to the system’s financial focus. The selection
process rules out 1t1v because of its vulnerability to plutocracy and capture dynamics. Among remaining options,
Currynomics considered implementation and communication complexity as a key constraint. Reputation-weighted
voting was deemed unsuitable because it requires additional reputation-assessment infrastructure. Quadratic voting
was considered not worth the added complexity for the anticipated governance needs. Consequently, Currynomics
selectedtime-weighted voting, and within that family,conviction votingas a comparatively simple option. This choice
is case-dependent: TEDM provides a structured rationale for selecting a mechanism under given constraints rather
than claiming that a single mechanism generalizes to all token economies.
3.2.7. Step 7 - Support mechanisms for Voting
As token economies mature, governance can face issues that core voting mechanisms do not directly address.
TEDM therefore includes optional support mechanisms that can be introduced when specific needs arise:
•Decision fatigue/proposal overload: too many proposals can reduce participation and decision quality. Miti-
gations include agenda-setting, proposal pre-screening, prediction markets, or algorithmic filtering [92, 22].
•Rational ignorance: participants may avoid information gathering when its costs exceed perceived benefits [54].
Mitigations include delegated voting, improved information design, and structured deliberation [93].
•Sybil attacks: identity splitting can occur even when voters commit tokens, time, or reputation. Mitigations
include identity systems such as Proof of Personhood (PoP), acknowledging potential trade-offs in privacy and
accessibility [56].
The Currynomics team plans to adopt a simple mechanism initially to support early community engagement, and
to introduce more advanced support mechanisms only as governance complexity and participation needs increase.
15

---

## Page 16

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2716
3.3. Tokenomics
This subsection responds to RQ3 by providing stepwise guidance for tokenomics design in TEDM. In the method,
tokenomics is treated as (i) arelease and distribution policy(Steps 1–3) and (ii) avalue and price-management policy
(Steps 4–5). Each step is formulated as a design proposition that clarifies the design goal, typical options discussed in
the literature, and the expected output artifact (e.g., a supply policy, a timing plan, or a price-management toolbox).
Figure 4 summarizes these five steps.
3.3.1. Step 1 - Define the token supply policy
A first tokenomics decision concerns whether supply is capped or uncapped, and how minting and burning affect
circulating supply over time. Prior work often distinguishesuncapped(inflationary) models, where supply can expand
over time, fromcapped(deflationary or fixed-supply) models, where an upper bound exists [94, 95, 96]. A simple
accounting identity for token supply over discrete time steps is:
S t =min (S max,S t−1 +M t −B t)
whereS t is circulating supply at timet,M t newly minted tokens, andB t burned tokens. For capped designs, an
additional constraintS t ≤S max is imposed.
Furthermore, the constraints imposed below are specific to inflationary or deflationary issuance models.
•Inflationary Model:
–S max is undefined (no cap).
–M t >B t (net supply increases over time).
•Deflationary Model:
–S max is fixed (supply cannot exceed cap).
Design implication and trade-off.Capped supplies can support scarcity narratives and long-term holding, but may
reduce spending willingness for governance or utility purposes if the token is primarily treated as a store of value.
Uncapped supplies can support flexibility and responsiveness to demand but may increase concerns about dilution and
long-run credibility if minting rules are not transparent and constrained.
Currynomics.Redcurry issuance is demand-driven and asset-backed: new Redcurry tokens are minted as the
underlying CRE portfolio expands. This resembles an uncapped mechanism in operational terms, but the minting
rule is constrained by the collateral base rather than discretionary emission. By contrast, the Currynomics DAO
token follows a capped supply policy. The team acknowledges the trade-offthat strong scarcity incentives can reduce
willingness to deploy DAO tokens for governance-related participation; the governance design (e.g., token locking for
voting) can partially mitigate this by decoupling participation incentives from pure “spend vs. hold” dynamics.
3.3.2. Step 2 - Define the timing strategy (pre-launch vs. post-launch)
Token releases can occurpre-launch(before product/protocol launch) orpost-launch(after launch) [50]. Pre-
launch issuance can fund development and bootstrap early stakeholders (often via escrow/vesting structures) [94].
Post-launch issuance can follow a schedule or be demand-driven; demand-driven issuance can help align supply
expansion with adoption, which may reduce certain volatility pressures compared to large upfront releases [94].
Design implication and trade-off.Pre-launch issuance improves early financing and coordination but increases risks of
misalignment (e.g., early concentration, opportunistic selling) if vesting and lockups are weak. Post-launch issuance
can better reflect realized demand but may slow early ecosystem growth if participation incentives require upfront
distribution.
Currynomics.Redcurry cannot be meaningfully issued pre-launch because issuance requires acquisition and man-
agement of the underlying real-estate portfolio; hence, it is effectively post-launch and collateral-driven. The DAO
token can be issued partly pre-launch to secure early contributors and bootstrap governance capacity, with controls
(e.g., vesting) to limit early sell pressure.
16

---

## Page 17

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2717
3.3.3. Step 3 - Define the distribution mechanism (public vs. private channels)
Token distribution can occur through different channels, including:
•Private sale: selling tokens to a limited set of investors (often discounted) [97].
•Public sale: selling tokens broadly (e.g., ICO/IEO or other public offerings) [28, 41, 98].
•Airdrops: distributing tokens to users for free to promote adoption [63, 64, 99].
Design implication and trade-off.Private sales can accelerate funding and attract strategic partners but may in-
crease concentration and perceived unfairness. Public sales can broaden participation and signal demand but face
regulatory and market-manipulation risks. Airdrops can bootstrap adoption but may allocate voting power to recipi-
ents with low governance competence or low willingness to participate, potentially harming governance quality [76].
Currynomics.Redcurry distribution is structured as a public channel via licensed financial institutions (partners),
consistent with its asset-backed nature and compliance constraints. The DAO token is distributed partly through a
pre-launch private sale (to founders, early contributors, advisors, and early-stage investors) and partly through post-
launch public mechanisms. The remaining pool is reserved for liquidity provision and ecosystem incentives (e.g., bug
bounties, community management, marketing), with an additional reserve for future ecosystem needs.
3.3.4. Step 4 - Define value-capture mechanisms (“inherent value”)
Token price sustainability depends on credible value-capture mechanisms and on how token demand relates to
system utility. While some authors argue that tokens lack intrinsic value in a strict sense [70, 94], the literature
discusses recurring channels through which tokens can capture value:
•Governance rights: participation in decision-making [65, 66].
•Claims linked to assets: representation tied to real-world or on-chain assets (e.g., collateral-backed struc-
tures) [41, 94].
•Network value: value influenced by adoption, trust, and utility of the ecosystem [41, 94].
•Claims on earnings: structures where token holders benefit from fee flows or economic surplus (directly or
indirectly) [41, 96].
3.3.5. Step 5 - Define price-management mechanisms (stability toolbox)
Designers often introduce mechanisms to mitigate excessive volatility, preserve trust, and manage adverse scenar-
ios (e.g., speculative pressure, liquidity shocks, or rapid sell-offs). Prior work highlights that speculation can crowd
out utility users under high volatility, undermining long-run adoption [100, 101]. Common mechanisms discussed in
the literature include:
•Token burns: reducing circulating supply by permanently removing tokens [70].
•Staking/locking: reducing circulating supply and aligning incentives through lock-up commitments [66].
•Buybacks: purchasing tokens from the market using treasury or revenue, reducing circulating supply and
signaling resources [65, 70].
•Vesting: releasing tokens gradually to avoid sudden supply shocks from early stakeholders [74, 100].
Design implication and trade-off.Supply-reduction mechanisms can support price stabilization but can also am-
plify future volatility if large unlock events occur or if staking yields attract primarily speculative participants. Accord-
ingly, TEDM treats price management as a toolbox whose suitability depends on the token’s value-capture channel
and anticipated adverse scenarios.
Currynomics.Redcurry’s primary value anchor is its link to real assets and the associated trust dynamics. A
complementary channel is network value: broader adoption can reinforce perceived credibility for new users. For
17

---

## Page 18

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2718
the DAO token, key value channels are governance rights and (prospectively) claims on earnings, insofar as trans-
action fees may indirectly support token value over time. Regarding price management, Redcurry incorporates a
redemption/buyback-style control logic tied to demand changes; in addition, users can stake Redcurry and receive
DAO tokens as a reward, which reduces circulating supply and can dampen short-run sell pressure. For the DAO to-
ken, vesting is applied to mitigate early-contributor sell-offs, and the chosen voting mechanism provides an additional
lock-up channel that can reduce circulating supply during governance participation. The team is considering whether
additional price-management mechanisms will be necessary as the ecosystem matures and as liquidity conditions
evolve.
4. Evaluation
This section presents the evaluation of the Token Economy Design Method (TEDM) following the iterative DSR
cycles described in Section 2.1. The evaluation isformative: it assesses TEDM’s interpretability, completeness,
simplicity, understandability, operational feasibility, and perceived accuracy, rather than providing statistical gener-
alization or causal proof of superior economic outcomes. Since the Currynomics ecosystem had not yet launched
at the time of writing, outcome-oriented validation (e.g., long-run sustainability, robustness under market stress) is
outside the scope of the empirical evidence available in this version of the study. To partially address external validity
and failure-mode concerns, we complement the focal-case demonstration with (i) external expert interviews and (ii) a
structured, desk-based stress discussion that links TEDM decision points to common adverse scenarios.
First, we report the use-casedemonstrationin Section 4.1. Second, we present the case-based evaluation through
interviews with Currynomics participants in Section 4.2. Case-based evaluation is widely adopted in DSR stud-
ies [102]; however, the maturity of the focal system constrains what can be validated empirically at the time of
writing. Therefore, a further evaluation cycle is conducted through semi-structured interviews with industry experts
not related to the Currynomics case (Section 4.3). Finally, Section 4.4 provides an overview of the thematic-analysis
coding results.
Code Role Background
IN1 Co-founder of the Redcurry Foundation Business development, MBA
IN2 Co-founder of the Redcurry Foundation Engineer, BSc in Information Technology
IN3 External Industry Expert Electrical engineer, researcher in token engineering.
IN4 External Industry Expert Web3 project consultant and advisor.
IN5 External Industry Expert MSc in Computer Science, software developer, and Web3
infrastructure founder.
Table 5. Interviewee roles and backgrounds.
Experts were purposively sampled based on the criterion of having at least three years of substantial experience in
token-economy design, either through industry practice or academic work. The mix of participants supports triangu-
lation between case-specific constraints and broader practitioner and research perspectives.
4.1. Use Case Demonstration
The demonstration illustrates how TEDM supports moving from environmental problem statements to structured
design propositions across incentives, governance, and tokenomics.
Incentives (Section 3.1).TEDM supported the elicitation of (i) stakeholder categories, (ii) system functions, and
(iii) desirable behaviors to be incentivized. Given these outputs, the Currynomics team concluded that incentives
linked to Redcurry should primarily be monetary (reflecting a financial value proposition), while participation in
governance around the DAO token should rely more on non-monetary mechanisms (e.g., governance participation
and reputational signals), with monetary appreciation as a secondary incentive.
Governance (Section 3.2).TEDM supported mapping governance areas to stakeholders and clarifying which
decisions remain centralized due to legal/operational constraints. Based on decentralization targets and the desired
voting properties, the method guided the selection of a time-weighted voting family and, given simplicity constraints,
18

---

## Page 19

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2719
the adoption of conviction voting as an initial mechanism. The team further concluded that support mechanisms
should be introduced only as governance complexity increases.
Tokenomics (Section 3.3).TEDM supported structuring token supply policy, release timing, and distribution
mechanisms. For Redcurry, the method confirmed a demand-driven, collateral-constrained issuance consistent with
its asset-backed design. For the DAO token, the method clarified trade-offs of capped supply (e.g., reinforcing holding
incentives) and motivated the use of vesting and token-locking to mitigate early sell pressure and reduce short-run
volatility. The method also made explicit how value-capture channels (asset-linked, governance rights, prospective
earnings) inform price-management choices and failure-mode risks.
4.2. Case Study-Based Evaluation
As described in Section 2.1, TEDM was evaluated using five criteria: completeness, simplicity, understandability,
operational feasibility, and perceived accuracy. Due to space constraints, Figure 4 reports the refined version of TEDM
after incorporating feedback.
Completeness.From the perspective of the Currynomics case, IN2 perceived TEDM as covering the major gover-
nance, incentive, and tokenomics choices relevant at the current stage, and highlighted that the next practical step
would be quantitative refinement (e.g., simulations) for selected mechanisms. IN1 suggested that token distribution
guidance (pre- and post-launch) and best practices around initial price formation could be expanded in future exten-
sions of the method.
Simplicity.Both IN1 and IN2 considered the method adequately simple given the inherent complexity of token-
economy design, emphasizing that the visual structure helps reduce cognitive overload without omitting essential
topics
Understandability.Both participants noted that the method benefits from explicit reading guidance and ordering
across the three pillars and their sub-steps. This feedback motivated the inclusion of progressive step indices and
clearer navigation cues in Figure 4. They also emphasized that governance concepts introduce social-science termi-
nology that may be unfamiliar to technically oriented practitioners, reinforcing the need for concise definitions and
rationale statements per step.
Operational F easibility.Participants perceived TEDM as practically useful for early-stage structuring and for ruling
out unsuitable mechanisms under case constraints. They noted that guidance on selecting a DAO technology stack
would increase operational value, while acknowledging that such implementation-level choices are beyond the current
scope. A key observation was that TEDM helps focus effort by clarifying what doesnotfit the case constraints, thereby
narrowing the design space.
Perceived Accuracy.IN1 cautioned that potential downsides of uncapped supply should be more prominently bal-
anced against benefits, pointing to dilution dynamics and cascade sell-offrisk. This concern aligns with prior dis-
cussions on valuation uncertainty and instability risks under unrestricted contributions [20]. The feedback motivates
more explicit boundary-condition statements in TEDM (e.g., when uncapped/demand-driven issuance is appropriate
and what safeguards are required).
4.3. Expert Interviews
This subsection reports feedback from external experts after a presentation of TEDM and the case instantiation
(Figure 4).
Completeness.IN3 emphasized that token-economy design is tightly coupled with legal and regulatory constraints
and suggested adding an optional legal-awareness module, while acknowledging that a full legal framework is be-
yond the scope of this version. IN3 also stressed the need to consider incentive design through a game-theoretic lens,
highlighting how poorly aligned payoffstructures can trigger adverse dynamics (e.g., rapid sell-offs). IN4 was com-
fortable with TEDM’s current scope but suggested that future work could provide modular extensions for different
DAO archetypes. IN5 proposed enriching governance with staged decision-making (e.g., proposal intake, delibera-
tion, voting, execution) and tool support by stage, consistent with views that governance evolves over time [103].
19

---

## Page 20

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2720
Simplicity and feasibility.IN3 and IN5 considered the scope appropriate and did not identify clearly redundant
components. IN5 appreciated the separation between core voting mechanisms and support mechanisms as a pragmatic
“add-on” approach for later ecosystem maturity. IN4 noted that the method is practical for newcomers but requires
additional reading to master details, which is expected for this domain.
Perceived accuracy and boundary conditions.Experts emphasized that full decentralization is rare in practice and
can reduce flexibility, consistent with empirical challenges observed in DAO governance [50]. They also argued for
hybrid on-chain/off-chain designs as many effective decision-making tools remain off-chain and less costly, supporting
the hybrid governance positioning in TEDM [104]. Regarding Sybil resistance, IN3 cautioned that identity-based
mechanisms can introduce new attack vectors (e.g., vote buying), suggesting that the method should present such
mechanisms together with trade-offs and limitations rather than as universal solutions.
Adversarial stress discussion (diagnostic use).Although outcome-oriented testing is outside the available empiri-
cal scope, expert feedback and the literature motivate using TEDM diagnostically against common failure modes.
We therefore relate key method decision points to adverse scenarios as follows: (i)governance capture/plutocracy
is addressed by decentralization targets (Step 3) and voting-property selection (Step 5), complemented by support
mechanisms (Step 7); (ii)liquidity shocks and sell-offcascadesmotivate conservative release/distribution policies
(Tokenomics Steps 1–3) and price-management tool choices (Step 5); (iii)speculative dominance and incentive back-
firemotivate explicitly linking desirable behaviors (Incentives Step 3) to incentive types and safeguards (Steps 4–5),
and clarifying boundary conditions under which monetary incentives should be used sparingly. This discussion does
not constitute empirical proof of robustness; rather, it clarifies how TEDM can be used to surface risks and design
trade-offs early.
4.4. Thematic Analysis Overview
Table 6 summarizes the thematic-analysis coding results across the five interview transcripts with regard to the
evaluation criteria. Counts reflect the number of coded comment segments (codes) associated with each criterion and
stance. These descriptive counts support transparency about what themes were most frequently raised; they are not
intended as statistical evidence.
Evaluation Criterion Supporting Neutral Opposing
Completeness 3 4 2
Simplicity 7 2 -
Understandability - 2 3
Operational feasibility 6 8 -
Perceived Accuracy 4 11 3
Table 6. Summary of coded interview comments by evaluation criterion
Overall, TEDM received a positive formative assessment. Simplicity and operational feasibility were strongly
supported, reinforcing practical usefulness for early-stage structuring. Completeness and perceived accuracy received
mixed feedback, with recurring suggestions to (i) make legal/regulatory boundary conditions more explicit and (ii)
strengthen the link between qualitative design propositions and subsequent quantitative validation. Understandability
emerged as the main area of concern, motivating the refinement of navigation cues and step ordering in Figure 4.
4.5. Comparative Analysis of Curve Finance and Uniswap Token Economies
We apply the TEDM classification introduced in Sections 3–5 as an analytic coding scheme to compare two op-
erating token economies: Curve Finance 5 and Uniswap6. Both are well-established decentralized exchanges (DEXs)
based on automated market makers (AMMs) [105]. This comparative instantiation complements the prior evaluation
5https://resources.curve.fi/
6https://app.uniswap.org/
20

---

## Page 21

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2721
steps by illustrating how TEDM categories can be applied beyond the focal Currynomics case. While both cases
belong to the same application class, they differ substantially in incentive and governance design, thereby providing a
non-trivial test of the portability of the TEDM classification within a shared domain.
Both protocols facilitate permissionless token swaps through liquidity pools rather than order books [105]. Uniswap
employs a constant-product AMM design (commonly formalized via the invariantx·y=k), enabling swaps across a
broad range of ERC-20 token pairs. Governance is handled via a DAO, where UNI token holders vote on upgrades and
protocol parameters. Curve Finance specializes in stable-value asset swaps, optimizing for low slippage and reduced
impermanent loss through a bonding-curve design tailored for correlated assets (e.g., stablecoins and wrapped as-
sets) [105]. Curve governance is also DAO-based, but relies heavily on token locking (veCRV) that links governance
influence to long-term commitment and reward boosting.
In the following, we summarize the main design features of the two token economies using the TEDM pillars:
incentives, governance, and tokenomics.
4.6. Incentives
TEDM Step Uniswap Curve Finance
Value Proposi-
tion •Liquidity Providers (LPs): Earn trad-
ing fees by supplying liquidity to pools.
•Traders: swap tokens without interme-
diaries at automated market prices.
•UNI Holders: participate in gover-
nance (e.g., upgrades and parameter de-
cisions).
•Liquidity Providers (LPs): earn trad-
ing fees and CRV incentives for provid-
ing liquidity.
•Traders: exchange stable-value assets
with minimal slippage.
•veCRV holders: lock CRV to gain gov-
ernance power and reward boosts.
•External DeFi stakeholders: compete
to attract liquidity by influencing emis-
sions toward specific pools.
Desirable Be-
haviors
liquidity provision; participation in gover-
nance.
Long-term commitment; active governance;
directing incentives toward strategically rele-
vant pools.
Incentive Mech-
anisms
Trading fees for LPs (monetary); governance
rights for UNI holders (non-monetary).
Trading fees for LPs (monetary); CRV
emissions to liquidity providers (monetary);
veCRV-based boosted yields (monetary); gov-
ernance influence via veCRV locking (non-
monetary).
Table 7. TEDM-based comparison of incentive structures in Uniswap and Curve Finance.
Applying TEDM to incentives highlights how both protocols align liquidity provision and governance participa-
tion, but with different mechanism complexity (Table 7). In Uniswap, the stakeholder set is relatively compact: LPs are
rewarded via fee distribution, while UNI holders gain governance rights. Desirable behaviors are continuous liquid-
ity provision and governance participation, supported primarily by fee-based monetary incentives and non-monetary
governance rights.
Curve Finance introduces additional incentive channels and roles. Beyond fees, CRV emissions reward liquidity
provision, while locking CRV as veCRV increases both governance power and reward boosts. In addition, external
DeFi projects may seek to influence veCRV votes to direct CRV emissions toward their pools (often discussed as
“bribing” dynamics) [106, 107]. This creates a stronger coupling between incentives and governance: governance
participation is not only non-monetary (decision rights) but also tightly linked to monetary outcomes via boosted
yields and emissions allocation.
21

---

## Page 22

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2722
4.7. Governance
TEDM Step Uniswap Curve Finance
Governance Areas Protocol upgrades, fee-related decisions, and
treasury management.
Liquidity incentives/emissions allocation, pro-
tocol upgrades, and treasury allocation.
Stakeholder Roles UNI holders propose (via governance pro-
cesses) and vote on changes.
veCRV holders vote on liquidity incentives
and other governance decisions; LPs can influ-
ence outcomes indirectly via locking decisions
and emissions-focused participation.
Level of Decentralization Permissionless but highly concentrated voting
power (reported as highly centralized).
Permissionless; more distributed voting power
than Uniswap, but still meaningfully concen-
trated.
Voting Mechanism 1-Token-1-V ote based on UNI. Time-weighted vote-escrow governance (ve-
CRV: longer lock⇒higher vote weight).
Table 8. TEDM-based comparison of governance models in Uniswap and Curve Finance.
Table 8 summarizes governance properties under TEDM. Uniswap relies on a standard 1-token-1-vote model,
which is simple but vulnerable to plutocratic concentration. Prior work reports a Gini coefficient of 0.996 and a
Nakamoto-style threshold of 11 for Uniswap governance power, indicating extreme concentration [50]. This supports
low inclusivity and elevated capture risk for the governance process.
Curve Finance uses a vote-escrow model (veCRV), where voting power depends on both the amount of CRV
locked and the lock duration. Our analysis reports a Gini coefficient of 0.8402 and a Nakamoto coefficient of 23,
suggesting broader distribution of voting power relative to Uniswap, though still centralized in absolute terms. These
metrics should be interpreted as distribution-based signals of governance concentration; they do not fully capture
turnout effects, delegation patterns, or off-chain influence channels. The full methodology and dataset for the Curve
concentration analysis are available in the associated GitHub repository7.
4.8. Tokenomics
TEDM Step Uniswap Curve Finance
Token Supply
Model
Inflationary policy (e.g., 2% annual inflation re-
ported in the literature [108]).
Capped supply (reported cap≈3.03B CRV).
Token Distribution Post-launch distribution via airdrop and (time-
bounded) liquidity mining; allocations for trea-
sury, team, and investors.
Post-launch emissions via liquidity mining; vested
allocations for team and early stakeholders.
Value-Capture
Channels •UNI: governance rights; network value.
•LP token:claims on pool assets and fee
revenue; network value.
•CRV/veCRV:governance rights; boosted
rewards via locking; earnings-linked value
via directing liquidity incentives.
•LP token:claim for asset, claim for rev-
enues, value of the network
Price-Management
Mechanisms
No explicit price-stabilization mechanism; price
dynamics largely market-driven (aside from vest-
ing/lockups in allocations).
veCRV locking reduces circulating supply and
links governance power to long-term commit-
ment.
Table 9. TEDM-based tokenomics comparison of Uniswap and Curve Finance.
Table 9 highlights distinct tokenomics choices. Uniswap’s UNI supply is reported as inflationary (e.g., 2% an-
nual inflation) without a hard cap, with an initial post-launch distribution through airdrops and liquidity mining and
7https:github.comSoweluAvanzoCurve_Finance_data_analysis
22

---

## Page 23

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2723
additional allocations to treasury, team, and investors [109]. Curve Finance is reported as capped (approximately
3.03B CRV), with emissions primarily routed through liquidity mining and complemented by vested allocations [110].
Unlike Uniswap’s immediate airdrop to early adopters, CRV distribution emphasizes ongoing participation through
emissions and vesting.
For both protocols, LP tokens capture value through claims on pooled assets and fee revenue, and the growth of
network activity amplifies fee generation. UNI and CRV/veCRV provide governance rights; however, Curve further
links governance to reward allocation and long-term locking, which can affect both incentive alignment and circulating
supply dynamics. Under TEDM, these differences illustrate how value-capture channels and distribution policies
interact with governance design and incentive mechanisms, supporting the use of the TEDM classification as a cross-
case analytic lens (within the DEX AMM domain).
Future work should extend the comparative instantiation to structurally distinct token economies (e.g., governance-
minimal protocols, stablecoins, or failed algorithmic designs) to further probe boundary conditions.
5. Conclusion and Future Work
This study proposed the Token Economy Design Method (TEDM), a stepwise, DSR-inspired method that sup-
ports early-stage token-economy design across three core pillars: incentives, governance, and tokenomics. TEDM
is intended as a qualitative requirements, derivation and structuring method for practitioners, especially those new to
Web3, who must navigate a large design space and make trade-offs explicit before proceeding to implementation and
quantitative refinement.
The development of the method followed a Design Science Research approach in which prior academic knowl-
edge was synthesized into design propositions and iteratively refined through application to a concrete case. TEDM
was instantiated in the Currynomics ecosystem, which is developing an inflation-resistant, CRE-backed stablecoin
(Redcurry), and evaluated formatively through semi-structured interviews with two case participants and three ex-
ternal experts using the criteria of completeness, simplicity, understandability, operational feasibility, and perceived
accuracy. Feedback primarily motivated improvements to the method’s navigation cues and ordering, which were
incorporated into the final version of the artifact.
To complement the focal case, we further instantiated the TEDM classification in a comparative analysis of two
operational DeFi token economies (Uniswap and Curve Finance) [105]. While both belong to the DEX AMM domain,
they exhibit markedly different incentive–governance couplings (fee-driven governance vs. vote-escrow locking and
emissions direction). This demonstrates how TEDM can be applied as a reusable analytic lens to structure and
compare token economy design choices beyond the focal case, within a shared application class.
Overall, TEDM contributes a method-level artifact that helps: (i) make stakeholder objectives and desired behav-
iors explicit; (ii) structure governance choices via decentralization targets, voting properties, and mechanism selec-
tion; and (iii) organize tokenomics decisions as a coherent policy space covering release/distribution and value/price-
management mechanisms. The method is not positioned as a guarantee of economic success; rather, it supports
disciplined reasoning about design trade-offs and boundary conditions, and prepares the ground for subsequent quan-
titative testing and refinement.
Limitations and Future Work.This paragraph clarifies how the current evidence should be interpreted and outlines
directions for future work. First, the evaluation is qualitative and formative. The interview-based assessment focuses
on perceived usefulness and interpretability (e.g., completeness, simplicity, understandability, operational feasibility,
and perceived accuracy), and should not be interpreted as causal evidence that applying TEDM leads to superior
economic outcomes (e.g., sustainability, robustness, or incentive alignment) under real market conditions.
Second, the empirical basis is narrow. The in-depth evaluation relies on a small purposive sample and on a single
co-designed case, which enables rich insight into design trade-offs but limits statistical generalization. The results are
therefore intended to be analytically transferable rather than statistically generalizable. The comparative instantiation
with Uniswap and Curve Finance supports portability of the TEDM classification beyond the focal case, but it remains
within one application class (DEX AMMs) and thus does not establish cross-context validity on its own.
Third, the development of TEDM prioritizes relevance to design practice over strict reproducibility. The method
was developed through an iterative synthesis of selected literature and refinement based on evaluation feedback, rather
than through a fully formal and reproducible derivation pipeline. As a result, the current version provides structured
23

---

## Page 24

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2724
guidance for qualitative requirements derivation and early design scoping, but it does not prescribe quantitative pa-
rameter choices (e.g., optimal issuance amounts) and does not provide a formal guarantee of completeness.
Fourth, TEDM’s applicability depends on context. It is most useful for token economies where incentives, gover-
nance, and token-supply policies are first-order design decisions and where stakeholder behaviors can be meaningfully
shaped through such mechanisms. It may be less informative for governance-minimal systems or purely speculative
token launches where design intent is not tied to sustained utility or institutional constraints. In addition, the present
version abstracts from several technology-layer decisions (e.g., base-layer blockchain choices, middleware/DAO stack
selection, and execution-layer constraints) that can materially affect feasible governance and tokenomics designs.
These points motivate several directions for future work. A natural extension is broader cross-context evaluation
across structurally distinct token economies (e.g., lending protocols, stablecoins with different collateralization strate-
gies, governance-minimal systems, and failed designs) to better formalize boundary conditions. Another direction
is integrating simulation and state-space exploration approaches from token engineering to complement TEDM with
quantitative refinement and stress testing, enabling outcome-oriented validation under adverse scenarios [44, 43, 45].
Further work can also strengthen reproducibility by adopting a more explicit derivation protocol (e.g., systematic
mapping with transparent inclusion criteria and traceability from literature constructs to method steps). Future work
will complement TEDM with on-chain behavioral metrics (e.g., token velocity and holding-time distributions) [111].
This will help evaluate whether TEDM-informed choices align with observed usage and governance dynamics in
operational token economies. Finally, TEDM can be extended with optional modules addressing legal/regulatory
awareness, base-layer and middleware choices, and DAO archetypes, including, for instance, protocol, investment,
and social DAOs [112], as well as additional tokenomics options such as dynamic-supply mechanisms (e.g., bonding-
curve-based policies) when appropriate [45].
Acknowledgement
This project is also partially funded by the Estonian ”Personal research funding: Team Grant (PRG)" project
PRG1641.
Declaration of Competing Interests
Authors have no competing interests to declare.
References
[1] D. R. D. Santos, M. A. Sanfins, A. Nascimento, P. L. D. S. Nacif, The token economy: Assets for the blockchain era, Global Media Journal
19 (37) (2021) 226.
[2] L. Oliviera, L. Zavolokina, I. Bauer, G. Schwabe, To token or not to token: Tools for understanding blockchain tokens, in: 39th International
Conference on Information Systems, San Francisco, 2018.
[3] N. Schubert, D. Obermeier, F. Kohlbrenner, P. Sander, Development of a token design framework, in: IEEE International Conference on
Decentralized Applications and Infrastructures (DAPPS), 2021.
[4] Z. Liu, Y . Li, Q. Min, M. Chang, User incentive mechanism in blockchain- based online community: An empirical study of steemit,
Information & Management 59 (7).
[5] V . Aistov, B. Kirpes, M. Roon, A blockchain token economy model for financing a decentralized electric vehicle charging platform, in:
IEEE 44th Annual Computers, Software, and Applications Conference (COMPSAC), Madrid, 2020.
[6] A. Khamisa, Token economies, in: The Emerald Handbook of Blockchain for Business, 2021, pp. 121–140.
[7] L. Pietrewicz, Token-based blockchain financing and governance: A transaction cost economics approach, Studia i Materiały Wydziału
Zarz˛ adzania UW 2 (28) (2018) 126–139.
[8] W. Kurniawan, S. Jansen, J. M. van der Werf, V oting mechanism selection for decentralized autonomous organizations, Tech. rep.,
SecureSECO (2022).
URLhttps://secureseco.org/wp-content/uploads/2022/08/Voting_Mechanism_Selection_for_Decentralized_
Autonomous_Organizations-3-1.pdf
[9] E. Baninemeh, S. Farshidi, S. Jansen, A decision model for decentralized autonomous organization platform selection: Three industry case
studies, Blockchain: Research and Applications 4 (2) (2023) 100127.
[10] C. Ziegler, I. M. Welpe, A taxonomy of decentralized autonomous organizations, in: ICIS 2022 proceedings, 2022.
[11] O. Rikken, M. Janssen, Z. Kwee, The ins and outs of decentralized autonomous organizations (daos) unraveling the definitions, characteris-
tics, and emerging developments of daos, Blockchain: Research and Applications (2023) 100143.
24

---

## Page 25

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2725
[12] H. Benedetti, C. Caceres, L. A. Abarzúa, Utility tokens, in: The Emerald Handbook on Cryptoassets: Investment Opportunities and Chal-
lenges, 2023, pp. 79–92.
[13] Y . Wang, F. Kaya, J. Gordijn, Blockchain governance design a computer science perspective, in: International Conference on Advanced
Information Systems Engineering, Springer, 2023, pp. 178–185.
[14] R. Han, Z. Yan, X. Liang, L. T. Yang, How can incentive mechanisms and blockchain benefit with each other? a survey, ACM Computing
Surveys 55 (7) (2022) 1–38.
[15] C. Biancotti, What’s next for crypto?, Occasional Paper 711, Bank of Italy (September 21 2022). doi:10.2139/ssrn.4462817.
URLhttps://ssrn.com/abstract=4462817
[16] B. J. Drasch, G. Fridgen, T. Manner-Romberg, F. M. Nolting, S. Radszuwill, The token’s secret: The two-faced financial incentive of the
token economy, Electronic Markets 30 (3) (2020) 557–567.
[17] J. Chod, N. Trichakis, S. Yang, Platform tokenization: Financing, governance, and moral hazard, Management Science 68 (9) (2021)
6411–6433.
[18] M. Sockin, Q. Xiong, A model of cryptocurrencies, [Online]. Available:
https://www.nber.org/papers/w26816. [Accessed 23 March 2023] (2020).
[19] Z. Faux, M. Shen, A $ 60 billion crypto collapse reveals a new kind of bank run, [Online]. Available:
https://www.bloomberg.com/news/articles/2022-05-19/luna-terra-collapse-reveal-crypto-price-volatility. [Accessed 29 October 2022]
(2022).
[20] W. A. Kaal, Fair token launch, Tech. Rep. 22-19, University of St. Thomas (Minnesota) Legal Studies (2022).
[21] O. Lage, M. Saiz-Santos, J. M. Zarzuelo, Decentralized platform economy: Emerging blockchain-based decentralized platform business
models, Electronic Markets 32 (3) (2022) 1707–1723.
[22] C. Barrera, S. Hurder, Cryptoeconomics: Designing effective incentives and governance models for blockchain networks using insights from
economics, Tech. rep., Blockchain Research Institute (2020).
[23] Y . Wang, C. H. Chen, A. Zghari-Sales, Designing a blockchain enabled supply chain, International Journal of Production Research 59 (5)
(2020) 1450–1475.
[24] A. Hofmann, C. Freichel, A. Winkelmann, A decentralized marketplace for collaborative manufacturing, in: 29th European Conference on
Information Systems (ECIS), Marrakech, 2021.
[25] J. Zhang, H. Zhao, Y . Yang, J. Yan, Towards transparency and trustworthy: A used-car deposit platform based on blockchain, in: IEEE 19th
International Conference on Software Quality, Reliability and Security Companion (QRS-C), Sofia, 2019.
[26] A. Direr, R. Doursat, B. Laurent, D. Biton, A data-driven and principled approach to designing the tokenomics of a new blockchain-based
game, SSRN Electronic Journal.
[27] J. Bena, S. Zhang, Token-based decentralized governance, SSRN Electronic Journal.
[28] J. Gan, G. Tsoukalas, S. Netessine, Financing platforms with cryptocurrency: Token retention, sales commission, and ico caps, ResearchGate
(2022).
[29] R. Han, Z. Yan, X. Liang, L. T. Yang, How can incentive mechanisms and blockchain benefit with each other? a survey, ACM Computing
Surveys 55 (7) (2022) 1–38.
[30] R. Qin, W. Ding, J. Li, S. Guan, G. Wang, Y . Ren, Z. Qu, Web3-based decentralized autonomous organizations and operations: Architectures,
models, and mechanisms, IEEE Transactions on Systems, Man, and Cybernetics: Systems 53 (4) (2022) 2073–2082.
[31] S. Wang, W. Ding, J. Li, Y . Yuan, L. Ouyang, F.-Y . Wang, Decentralized autonomous organizations: Concept, model, and applications,
IEEE Transactions on Computational Social Systems 6 (5) (2019) 870–878.
[32] S. Avanzo, A. Norta, C. Schifanella, A modelling approach for a high utility decentralized autonomous organization development, in:
International Congress on Blockchain and Applications, Springer, 2023, pp. 542–547.
[33] X. Liang, W. Ding, R. Qin, J. Hou, Y . Yuan, X. Wang, F.-Y . Wang, From cadcad to cascad2: A mechanism validation and verification system
for decentralized autonomous organizations based on parallel intelligence, IEEE Transactions on Computational Social Systems.
[34] A. R. Hevner, S. T. March, J. Park, S. Ram, Design science in information systems research, MIS quarterly (2004) 75–105.
[35] R. Wieringa, Empirical research methods for technology validation: Scaling up to practice, Journal of Systems and Software 95 (2014)
19–31.
[36] M. Harrell, M. Bradley, Data collection methods: Semi-structured interviews and focus groups, Tech. Rep. ADA512853, RAND National
Defense Research Institute (2009).
[37] N. Prat, I. Comyn-Wattiau, J. Akoka, A taxonomy of evaluation methods for information systems artifacts, Journal of Management Infor-
mation Systems 32 (3) (2015) 229–267.
[38] R. van Pelt, S. Jansen, D. Baars, S. Overbeek, Defining blockchain governance: A framework for analysis and comparison, Information
Systems Management 38 (1) (2021) 21–41.
[39] V . Braun, V . Clarke, Thematic analysis, in: Qualitative research in clinical and health psychology, Palgrave Macmillan, Hampshire, 2014,
pp. 95–114.
[40] L. Sterling, K. Taveter, The art of agent-oriented modeling, MIT press, 2009.
[41] P. Freni, E. Ferro, R. Moncada, Tokenomics and blockchain tokens: A design-oriented morphological framework, Blockchain: Research
and Applications 3 (1).
[42] S. Tapscott, Token taxonomy: The need for open-source standards around digital assets, Tech. rep., Blockchain Research Institute (2020).
[43] C. Rice, M. Zargham, On the practice of token engineering, part iii: Something is missing, blockScience Blog (Apr. 2019).
URLhttps://blog.block.science/on-the-practice-of-token-engineering-part-iii-something-is-missing/
[44] M. Zargham, Z. Zhang, V . Preciado, A state-space modeling framework for engineering blockchain-enabled economic systems, arXiv
preprint (2018). arXiv:1807.00955, doi:10.48550/arXiv.1807.00955.
URLhttps://arxiv.org/abs/1807.00955
[45] M. Zargham, J. Shorish, K. Paruch, From curved bonding to configuration spaces, in: 2020 IEEE International Conference on Blockchain
and Cryptocurrency (ICBC), 2020.
25

---

## Page 26

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2726
[46] T. Dasaklis, F. Casino, C. Patsakis, C. Douligeris, A framework for supply chain traceability based on blockchain tokens, in: 17th Interna-
tional Conference on Business Process Management, Vienna, 2019.
[47] H. R. Hasan, K. Salah, Blockchain-based proof of delivery of physical assets with single and multiple transporters, IEEE Access 6 (2018)
46781–46793.
[48] D. Hou, Y . Hao, Y . Du, Design of public voluntary carbon market mechanism based on crosschain and token economics, in: Proceedings of
the Fourth ACM International Symposium on Blockchain and Secure Critical Infrastructure, Nagasaki, 2022.
[49] H. Kim, M. Laskowski, M. Zargham, H. Turesson, M. Barlin, D. Kabanov, Token economics in real life: Cryptocurrency and incentives
design for insolar’s blockchain network, Computer 54 (1) (2021) 70–80.
[50] R. Fritsch, R. Wattenhofer, M. Müller, Analyzing voting power in decentralized governance: Who controls daos?, arXiv.
[51] X. Sun, C. Stasinakis, Decentralization illusion in defi: Evidence from makerdao, Available at SSRN 3971791.
[52] X. Zhao, P. Ai, F. Lai, X. Luo, J. Benitez, Task management in decentralized autonomous organization, Journal of Operations Management
68 (6-7) (2022) 649–674.
[53] S. Venugopalan, H. Aydt, Dance of the daos: Building data assets as a use case, arXiv preprint arXiv:2301.05945.
[54] A. Kiayas, P. Lazos, Sok: Blockchain governance, [Online]. Available:
https://arxiv.org/pdf/2201.07188.pdf. [Accessed 14 March 2023] (2023).
[55] J. D. Fernandez, T. Barbereau, O. Papageorgiou, Agent-based model of initial token allocations: Evaluating wealth concentration in fair
launches, [Online]. Available: https://arxiv.org/pdf/2208.10271.pdf. [Accessed 20 February 2023] (2022).
[56] V . Mohan, P. Khezr, C. Berg, V oting with time commitment for decentralized governance: Bond voting as a sybil-resistant mechanism,
SSRN Electronic Journal.
[57] W. Wang, D. T. Hoang, P. Hu, Z. Xiong, D. Niyato, P. Wang, Y . Wen, D. I. Kim, A survey on consensus mechanisms and mining strategy
management in blockchain networks, Ieee Access 7 (2019) 22328–22370.
[58] Z. Yu, X. Liu, G. Wang, A survey of consensus and incentive mechanism in blockchain derived from p2p, in: 2018 IEEE 24th international
conference on parallel and distributed systems (ICPADS), IEEE, 2018, pp. 1010–1015.
[59] J. Huang, K. Lei, M. Du, H. Zhao, H. Liu, J. Liu, Z. Qi, Survey on blockchain incentive mechanism, in: Data Science: 5th International Con-
ference of Pioneering Computer Scientists, Engineers and Educators, ICPCSEE 2019, Guilin, China, September 20–23, 2019, Proceedings,
Part I 5, Springer, 2019, pp. 386–395.
[60] J. Jürjens, S. Scheider, F. Yildirim, M. Henke, Tokenomics: Decentralized incentivization in the context of data spaces, in: Designing Data
Spaces, 2021, pp. 91–108.
[61] C. Guo, P. Zhang, B. Lin, J. Song, A dual incentive value-based paradigm for improving the business market profitability in blockchain
token economy, Mathematics 10 (3).
[62] X. Liu, W. Chen, K. Zhu, Token incentives and platform competition: A tale of two swaps, SSRN Electronic Journal.
[63] K. Lommers, C. Makridis, L. Verboven, Designing airdrops, SSRN Electronic Journal.
[64] Z. Liu, H. Zhu, Fighting sybils in airdrops, [Online]. Available:
https://arxiv.org/pdf/2209.04603.pdf. [Accessed 15 March 2023] (2022).
[65] A. Carvalho, Tokenomics and their parallels in traditional finance, SSRN Electronic Journal.
[66] K. Lommers, J. Xu, T. A. Xu, A framework for dao token valuation, SSRN Electronic Journal.
[67] B. Kusmierz, R. Overko, How centralized is decentralized? comparison of wealth distribution in coins and tokens, in: 2022 IEEE Interna-
tional Conference on Omni-Layer Intelligent Systems (COINS), 2022.
[68] A. Peña Calvin, J. Arroyo, A. Schwartz, S. Hassan, Concentration of power and participation in online governance: the ecosystem of
decentralized autonomous organizations, in: Companion Proceedings of the ACM Web Conference 2024, WWW ’24, Association for
Computing Machinery, New York, NY , USA, 2024, p. 927–930. doi:10.1145/3589335.3651481.
URLhttps://doi.org/10.1145/3589335.3651481
[69] T. Eisermann, C. Campajola, C. J. Tessone, A. S. Teixeira, Concentration in governance control across decentralised finance protocols, EPJ
Data Science 14 (1) (2025) 85.
[70] D. W. E. Allen, C. Berg, S. Davidson, Buyback and burn mechanisms: Price manipulation or value signalling?, SSRN Electronic Journal.
[71] M. Kim, J. Chung, Sustainable growth and token economy design: The case of steemit, Sustainability 11 (1).
[72] RedCurry, Redcurry, [Online]. Available: https://docs.redcurry.co/. [Accessed 16 April 2023] (2023).
[73] M. Hafner, M. H. Pereira, H. Dietl, J. Beccuti, The four types of stablecoins: A comparative analysis, Ledger 9.
[74] S. Yoo, How to design cryptocurrency value and how to secure its sustainability in the market, Journal of Risk and Financial Management.
[75] J. Y . Lee, A decentralized token economy: How blockchain and cryptocurrency can revolutionize business, Business Horizons 62 (6) (2019)
773–784.
[76] S. Davidson, From corporate governance to crypto-governance, SSRN Electronic Journal.
[77] D. W. E. Allen, C. Berg, Blockchain governance: What we can learn from the economics of corporate governance, SSRN Electronic Journal.
[78] S. V oshmgir, Token economy: How the web3 reinvents the internet (2020).
[79] S. Kampakis, Auditing tokenomics: A case study and lessons from auditing a stablecoin project, The Journal of The British Blockchain
Association 5 (2) (2022) 1–7.
[80] A. Pazaitis, P. D. Filippi, V . Kostakis, Blockchain and value systems in the sharing economy: The illustrative case of backfeed, Technological
Forecasting and Social Change.
[81] S. Kang, K. Cho, K. Park, On the effectiveness of multi-token economies, in: 2019 IEEE International Conference on Blockchain and
Cryptocurrency (ICBC), 2019.
[82] J. Ma, M. Jiang, J. Jiang, X. Luo, Y . Hu, Y . Zhou, Q. Wang, F. Zhang, Understanding security issues in the dao governance process, IEEE
Transactions on Software Engineering.
[83] K. Bersani, Separating governance tokens from securities: How the utility token may fall short of the investment contract, Cardozo Law
Review.
[84] R. Feichtinger, R. Fritsch, Y . V onlanthen, R. Wattenhofer, The hidden shortcomings of (d) aos–an empirical study of on-chain governance,
26

---

## Page 27

Kivilo, S.; Norta, A.; Hattingh, M.; Avanzo, S.; Pennella, L/Blockchain:Research and Applications 00 (2026) 1–2727
in: International Conference on Financial Cryptography and Data Security, Springer, 2023, pp. 165–185.
[85] W. Reijers, I. Wuisman, M. Mannan, P. De Filippi, Now the code runs itself: On-chain and off-chain governance of blockchain technologies,
SSRN Electronic Journal.
[86] V . Buterin, Moving beyond coin voting governance, [Accessed 29 March 2023] (August 2021).
URLhttps://vitalik.ca/general/2021/08/16/voting3.html
[87] Y . Faqir-Rhazoui, J. Arroyo, S. Hassan, A comparative analysis of the platforms for decentralized autonomous organizations in the ethereum
blockchain, Journal of Internet Services and Applications 12 (1).
[88] M. C. Valiente Blazquez, S. Hassan, J. Pavon Mestras, Evaluating the software frameworks for developing decentralized autonomous
organizations, in: VI Jornadas de Ciencia e Ingeniería de Servicios (JCIS), 2021.
[89] D. Wright Jr, Quadratic voting and blockchain governance, UMKC Law Review 88 (1).
[90] N. Dimitri, Quadratic voting in blockchain governance, Information 13 (6).
[91] A. Benhaim, B. H. Falk, G. Tsoukalas, Balancing power in decentralized governance: Quadratic voting and information aggregation,
Management Science.
[92] W. W. Ding, X. L. Liang, J. C. Hou, G. Wang, Y . Yuan, J. Li, F. Y . Wang, Parallel governance for decentralized autonomous organizations
enabled by blockchain and smart contracts, in: IEEE 1st International Conference on Digital Twins and Parallel Intelligence (DTPI), 2021.
[93] L. Weidener, F. Laredo, K. Kumar, K. Compton, Delegated voting in decentralized autonomous organizations: a scoping review, Frontiers
in Blockchain 8 (2025) 1598283.
[94] W. A. Kaal, Crypto economics - the top 100 token models compared, SSRN Electronic Journal.
[95] J. Gan, G. Tsoukalas, S. Netessine, Initial coin offerings, speculation, and asset tokenization, Management Science 67 (2) (2020) 914–931.
[96] W. A. Kaal, S. Evans, H. Howe, Digital asset valuation, SSRN Electronic Journal.
[97] S. T. Howell, M. Niessner, D. Yermack, Initial coin offerings: financing growth with cryptocurrency token sales, The Review of Financial
Studies 33 (9) (2020) 3925–3974.
[98] E. Lyandres, B. Palazzo, D. Rabetti, Initial coin offering (ico) success and post-ico performance, Management Science 68 (12) (2022)
8658–8679.
[99] D. W. Allen, Crypto airdrops: An evolutionary approach, Journal of Evolutionary Economics 34 (4) (2024) 849–872.
[100] J. Li, W. Mann, Digital tokens and platform building, SSRN Electronic Journal.
[101] S. Mayer, Token-based platforms and speculators, SSRN Electronic Journal.
[102] K. Peffers, M. Rothenberger, T. Tuunanen, R. Vaezi, Design science research evaluation, in: Lecture Notes in Computer Science, 2012, p.
398–410.
[103] G. Laatikainen, M. Li, P. Abrahamsson, A system-based view of blockchain governance, Information and Software Technology 157 (2023)
107149.
[104] L. Mosley, H. Pham, Y . Bansal, Towards a systematic understanding of blockchain governance in proposal voting: A dash case study,
Blockchain: Research and Applications 3 (3) (2022) 100085.
[105] M. Ottina, P. J. Steffensen, J. Kristensen, Automated market makers: A practical guide to decentralized exchanges and cryptocurrency
trading, Springer, 2023.
[106] T. Lloyd, D. O’Broin, M. Harrigan, Emergent outcomes of the vetoken model, in: 2023 IEEE international conference on omni-layer
intelligent systems (COINS), IEEE, 2023, pp. 1–6.
[107] D. W. Allen, C. Berg, A. M. Lane, T. MacDonald, J. Potts, The exchange theory of web3 governance, Kyklos 76 (4) (2023) 659–675.
[108] Uniswap, Introducing UNI: Uniswap’s governance token, Uniswap Blog (2020).
[109] J. Howell, A comprehensive guide to uniswap (uni) tokenomics, 101 BlockchainsAccessed: 2024-02-10.
URLhttps://101blockchains.com/uniswap-tokenomics-explained/
[110] Curve Finance, Crv token supply and distribution, accessed: 2024-02-10 (2020).
URLhttps://resources.curve.fi/crv-token/supply-distribution/
[111] B. Kraner, L. Pennella, N. Vallarano, C. J. Tessone, Money in motion: Micro-velocity and usage of ethereum’s liquid staking tokens, in: 7th
Conference on Advances in Financial Technologies (AFT 2025), Schloss Dagstuhl–Leibniz-Zentrum für Informatik, 2025, pp. 9–1.
[112] S. Bonnet, F. Teuteberg, Decentralized autonomous organizations: A systematic literature review and research agenda, International Journal
of Innovation and Technology Management (2024) 2450026.
27

---
