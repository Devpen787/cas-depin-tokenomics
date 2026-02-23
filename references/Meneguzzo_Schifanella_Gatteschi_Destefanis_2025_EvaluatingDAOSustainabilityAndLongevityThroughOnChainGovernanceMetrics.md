# Meneguzzo_Schifanella_Gatteschi_Destefanis_2025_EvaluatingDAOSustainabilityAndLongevityThroughOnChainGovernanceMetrics.pdf

## Page 1

1
Evaluating DAO Sustainability and Longevity
Through On-Chain Governance Metrics
Silvio Meneguzzo, Claudio Schifanella, Valentina Gatteschi, Giuseppe Destefanis
Abstract—Decentralised Autonomous Organisations (DAOs)
automate governance and resource allocation through smart
contracts, aiming to shift decision-making to distributed token
holders. However, many DAOs face sustainability challenges linked
to limited user participation, concentrated voting power, and
technical design constraints. This paper addresses these issues by
identifying research gaps in DAO evaluation and introducing a
framework of Key Performance Indicators (KPIs) that capture
governance efficiency, financial robustness, decentralisation, and
community engagement. We apply the framework to a custom-
built dataset of real-world DAOs constructed from on-chain data
and analysed using non-parametric methods. The results reveal
recurring governance patterns, including low participation rates
and high proposer concentration, which may undermine long-term
viability. The proposed KPIs offer a replicable, data-driven method
for assessing DAO governance structures and identifying potential
areas for improvement. These findings support a multidimensional
approach to evaluating decentralised systems and provide practical
tools for researchers and practitioners working to improve the
resilience and effectiveness of DAO-based governance models.
Index Terms—Decentralized Autonomous Organizations, DAO,
Blockchain, Voting Mechanisms, Decentralization, Governance,
Sustainability, Longevity, Key Performance Indicators, User
Participation.
I. I NTRODUCTION
D
ECENTRALISED Autonomous Organisations (DAOs)
introduce a governance model that replaces centralised
decision-making with blockchain-based smart contracts and
voting mechanisms [1]. DAOs enable collective decision-
making by users without the need for central authorities or
intermediaries [2]. This structure is based on decentralisation,
transparency, and automated decision-making, making DAOs
applicable to various collaborative systems. Despite these
characteristics, unresolved challenges remain [3], particularly
low user participation in governance [4]. When participants do
not vote or engage in the decision-making process, a DAO’s
ability to function effectively and maintain its decentralised
structure is weakened [5]. Addressing participation issues is
necessary to ensure that DAOs operate as intended and support
long-term sustainability.
Manuscript created March, 2025; This work was developed by Silvio
Meneguzzo (Corresponding author) is with the Department of Computer
Science, University of Turin, Italy (e-mail: silvio.meneguzzo@unito.it).
Claudio Schifanella is with the Department of Informatics, University of
Turin, Italy (e-mail: claudio.schifanella@unito.it).
Valentina Gatteschi is with the Department of Automation and Computer
Science, Politecnico di Torino, Italy (e-mail: valentina.gatteschi@polito.it).
Giuseppe Destefanis is with the Department of Computer
Science, Brunel University of London, United Kingdom (e-mail:
giuseppe.destefanis@brunel.ac.uk).
In this paper, we examine how DAOs compare to tra-
ditional organisational models and analyse the blockchain-
based mechanisms that influence participation and governance.
By evaluating real-world DAOs through Key Performance
Indicators (KPIs), we identify critical governance challenges
related to user engagement and decision-making.
To address these issues, we define the following research
questions:
RQ1: Which challenges most significantly affect DAO sustain-
ability and longevity, particularly regarding user participation?
Rationale: DAOs face multiple obstacles, but inadequate
engagement is consistently identified as a primary factor
influencing decentralisation and effectiveness.
RQ2: Which Key Performance Indicators (KPIs) can be used
to evaluate DAO sustainability, including financial stability,
governance processes, decentralisation, and community engage-
ment?
Rationale: Establishing measurable indicators allows for com-
parability and helps identify organisational and technical
weaknesses in DAOs.
RQ3: How does applying these KPIs to real-world DAOs
reveal governance issues and inform strategies for improving
sustainability and longevity?
Rationale: Beyond theoretical measures, the study aims to
demonstrate how KPI-based analysis provides structured rec-
ommendations for improving DAO governance.
We make three principal contributions. First (I), we identify
persistent open challenges in DAO governance, focusing
specifically on the lack of consistent user engagement as a
limiting factor for sustainability and effective decentralization.
Second (II), we develop a set of empirically grounded KPIs
spanning social, economic, and procedural dimensions of DAO
governance. These KPIs offer a replicable and structured means
of assessing DAOs across multiple dimensions, including voting
activity, treasury management, automation, and distribution
of power. Third (III), we apply these KPIs to a curated
dataset based on on-chain data, comprising 50 active DAOs
and demonstrate how the ensuing analysis reveals critical
governance asymmetries, especially low voter turnout and
concentration of proposer authority, and highlights paths
for structural improvements. By establishing this integrated
KPI framework, we aim to support both researchers and
practitioners in diagnosing governance shortfalls and designing
more resilient, community-driven DAO ecosystems.
By applying the proposed KPI framework to real-world cases,
we show how inclusive governance structures, more equitable
resource allocation, and user-friendly voting mechanisms can
significantly boost engagement and decentralisation. In this
arXiv:2504.11341v2  [cs.CY]  24 Apr 2025

---

## Page 2

2
sense, our findings suggest that structured, data-driven indica-
tors enable DAOs to develop more participatory and automated
governance models, ultimately strengthening their sustainability.
The rest of this paper is structured as follows: Section II reviews
related work on DAOs, governance mechanisms, and ongoing
challenges. Section III describes the research methodology,
including KPIs development and the creation of a Multi-chain
on-chain retrieval pipeline. Section IV presents the results
based on the analysis of existing DAOs. Section V discusses
the implications of these findings, followed by threats to validity
in Section VI. Finally, Section VII provides conclusions and
directions for future research.
We provide a replication package including all the nalysis
scripts and results at this link 1 to support reproducibility and
verification.
II. B ACKGROUND
A. DAOs: Definition and Evolution
Decentralised Autonomous Organisations represent a gov-
ernance model that uses blockchain technology and smart
contracts to automate decision-making processes [2]. Unlike
traditional organisations, which rely on centralised authorities,
DAOs distribute decision-making power among members
through token-based voting systems [6].
The concept of DAOs emerged with Buterin’s [1], [7] intro-
duction of Ethereum, the first blockchain platform supporting
smart contracts capable of encoding organisational rules. In
2016, “The DAO” was launched as the first large-scale
implementation, raising over $150 million before a vulnerability
in its smart contract led to a major security breach [8]. This
event demonstrated how flaws in smart contract code could
result in governance failures [9]. Interest in DAOs was later
revived when MakerDAO introduced an on-chain governance
system in 2018, followed by the adoption of similar approaches
across various DeFi (Decentralized Finance) protocols [10].
B. DAO Characteristics and Challenges
DAOs are built on three core principles: decentralisation
(distributed network-based management), automation (code-
based governance), and organisation (transparent operating
rules via smart contracts) [11]. Additional attributes include
transparency, immutability, resistance to manipulation, interop-
erability, incentives for participation, and operational efficiency
[2], [12].
Despite these characteristics, DAOs encounter significant
challenges. Security vulnerabilities in smart contracts can have
severe consequences due to blockchain immutability, as seen
in “The DAO” hack [6]. Privacy concerns arise from the full
transparency of all transactions [9]. Legal uncertainties persist
in many jurisdictions, raising questions about liability [12],
despite the fact that some jurisdictions have begun formalizing
DAO-friendly statutes, including Vermont [13], Wyoming
[14], the Marshall Islands [15], and Utah [16]. Technical
constraints include the gap between legal frameworks and
1The replication package is hosted on Figshare: https://figshare.com/s/
2cf646c67f23ea917ac1
smart contract code [6]. Governance-related difficulties also
remain, particularly the concentration of voting power and
low participation rates [4] and related security issues in the
governance process [17]. Early analyses stressed that DAOs
must balance on-chain rules with off-chain social coordination
[18], but this approach is in contradiction with a full transparent
and decentralized desired behaviour.
C. DAO Governance Mechanisms
Governance is a central aspect of DAOs, with voting
mechanisms forming a key part of their structure alongside
blockchain and smart contracts. Fan et al. [19] examined several
voting mechanisms used in DAOs, including Approved Relative
Majority, Token-Based Quorum, Quadratic V oting, Liquid
Democracy, Weighted V oting, Rage Quitting, and Holographic
Consensus. Ding et al. [20] also described Conviction V oting,
which adjusts vote weight based on preference and time. Dimitri
[21] highlights how different voting schemes, such as approval
voting or rank-based voting, impact outcome legitimacy in DAO
governance. Beck et al. [22] propose a blockchain governance
model highlighting the tension between decentralization and
the need for effective coordination.
Despite the range of governance models, Feichtinger et al.
[4] found that voting power remains concentrated in most
DAOs. In their study of 21 governance systems, 17 were
controlled by fewer than 10 participants. Common measures
of voting power distribution include the Gini Coefficient and
Nakamoto Coefficient [23], which assess inequality and control
concentration, respectively. While these mechanisms represent a
diverse range of voting protocols, prior empirical studies often
overlook the interplay between on-chain user participation,
treasury management, and the degree of proposal automation.
As a result, comprehensive frameworks for capturing overall
DAO sustainability remain underdeveloped. This gap underpins
the need for an integrated KPI-based approach, as we discuss
in Section III.
D. Evaluation Approaches for DAOs
Existing research on DAO evaluation often focuses on
individual aspects rather than complete frameworks. Park et al.
[24] introduced dimensions for assessing decentralisation, while
Faqir-Rhazoui et al. [25] conducted a comparative study of
DAO platforms on Ethereum. Although these studies provide
useful insights, they do not offer an integrated method for
assessing sustainability. Wang et al. [6] and Qin et al. [26]
proposed architectural models to examine DAO structures,
covering technological, execution, coordination, organisational,
and application layers. These models provide a conceptual
understanding of governance structures but do not translate
into practical evaluation metrics.
E. Research Gap
Despite the growing body of literature on DAOs, there
remains no widely accepted framework for comprehensively
assessing their sustainability and longevity. Many studies
rely on off-chain or aggregator data that fail to capture on-
chain details and some of the existing works tend to focus

---

## Page 3

3
narrowly on specific issues such as security vulnerabilities [8],
governance limitations [4], or technical implementations [6],
while neglecting broader social and economic dimensions. For
example, Park et al. [24] propose decentralisation indicators
focused on organisational structure, and Faqir-Rhazoui et
al. [25] compare DAO platforms (Aragon, DAOstack, and
DAOhaus) primarily in terms of feature sets. Although such
studies contribute valuable insights into decentralisation ratios,
treasury sizes, or code security, they rarely address procedural
and community-oriented factors such as user participation,
voting fairness, and long-term engagement within a unified
evaluative model.
Furthermore, the lack of a complete dataset incorporating
detailed on-chain governance events further hampers progress.
Many existing datasets offer incomplete views of token
distribution and voting activities. A recent empirical study based
on off-chain data from the Snapshot platform [27] analysed 581
DAO projects over more than three years, providing valuable
insights into DAO performance at scale. However, while such
approaches capture broad activity metrics, they do not include
the fine-grained, verifiable on-chain details, such as precise
token transfers and smart contract event logs, needed for an
integrated assessment of governance performance. In response,
our work introduces a dataset, constructed directly from raw
blockchain data, which enables a more accurate and integrated
evaluation of DAO performance.
Many DAOs suffer from persistently low voting turnout,
centralised token ownership, or ambiguous legal standing [9],
[12], but a thorough, empirical framework that captures these
varied challenges is still lacking. In particular, while indicators
like the Gini Coefficient [23] or token-based voting measures
[19] help quantify power concentration, they do not account
for social incentives, governance processes, or community
resilience; factors that are equally critical to a DAO’s viability
over time.
To address these gaps, this paper introduces a KPI framework to
evaluate DAOs across four dimensions—participation, financial
stability, voting efficiency, and decentralisation—linking social,
economic, and procedural factors to identify governance issues
and support long-term sustainability.
III. M ETHODOLOGY
We used a data-based approach to develop and apply Key
Performance Indicators for evaluating the sustainability and
longevity of DAOs. Our methodology combined quantitative
data analysis with qualitative reasoning to ensure that our
KPIs were both empirically grounded and conceptually sound.
Existing studies often focus on isolated aspects of DAO
performance (e.g., decentralisation ratios, treasury sizes, or
code security) and rely on incomplete aggregator-based datasets,
which limits analyses of voting power distribution and user
engagement [4], [6], [8], [11], [28].
To address these limitations, we extracted raw data from multi-
ple sources, including Smart Contracts’ ABI from blockchain
explorers (e.g., Etherscan) and direct queries to blockchain
networks via providers like Infura and Alchemy. This process
provided detailed numerical and categorical information on var-
ious aspects of DAOs, allowing reliable quantitative assessment
of their structures and activities.
We interpreted our quantitative findings within the context
of existing research on DAO governance models, established
theoretical frameworks, and current organisational patterns
[29], [30]. This combination ensured our KPIs captured
both measurable indicators and broader aspects of DAO
sustainability.
A. Key Performance Indicators
To assess the sustainability and longevity of DAOs, we
defined four Key Performance Indicators covering core aspects
such as community participation, financial capacity, governance
processes, and decentralisation. These KPIs were shaped by
existing literature [4], [19], [24], [25], [31] and insights from
our curated dataset. Together, they offer a structured way to
evaluate organisational resilience over time.
1) KPI 1: Network Participation: This KPI reflects the
extent of member engagement within the DAO. Participation
in voting and proposal creation is essential to decentralised
governance and helps ensure representative decision-making,
adaptability and helps mitigate oligarchic tendencies [4], [31].
We define the Participation Rate as:
Participation Rate =
Active Members
Total Members

(1)
An Active Member is any address that has cast a vote or
created a proposal. Total Members are token holders with
on-chain voting rights. Drawing on literature reporting low
participation levels, we adopt the following classification:
• Low: <10%
• Medium: 10–40%
• High: >40%
These categories reflect empirical observations of voter turnout
in prominent DAOs [4] and distinguish between minimal,
moderate, and widespread participation. Prior analyses indicate
that below 10% turnout, governance tends to be dominated by
a handful of token holders, undermining true decentralization
of partecipation.
2) KPI 2: Accumulated Funds: This KPI captures a DAO’s
financial capacity. We consider two aspects:
Treasury Size denotes the total assets held in smart contracts
under DAO control. Larger treasuries allow for sustained
contributor rewards, protocol development, and other activities.
Circulating Token Percentage measures the proportion of
governance tokens in circulation:
Circulating Token Percentage =
Circulating Supply
Total Supply

(2)
Tokens held by the treasury or locked in vesting contracts are
excluded from circulation. High circulation suggests broader
economic participation, while low circulation may indicate
concentration. We combine both aspects to categorise financial
status:
• Low: Treasury <$100M
• Medium-Low: $100M–$1B, circulation ≤ 50%

---

## Page 4

4
• Medium-High: $100M–$1B, circulation > 50%
• High: Treasury >$1B
Treasury size thresholds at $100 million and $1 billion
reflect typical boundaries observed in leading DeFi DAOs
like MakerDAO, Compound, and Uniswap, where financial
resources can significantly influence governance dynamics and
system resilience.
3) KPI 3: Voting Mechanism Efficiency: This KPI considers
governance effectiveness based on proposal approval rate and
voting duration:
Approval Rate =
Approved Proposals
Total Proposals

(3)
Average V oting Duration=
Pn
i=1 V oting Durationi
n (4)
Short durations may indicate rushed decision-making, while
longer voting windows can hinder timely execution. Based on
empirical observations [19], we define:
• Low: Approval <30% and/or duration <3 days
• Medium: Approval 30–70%, duration 3–14 days
• High: Approval >70%, duration 3–14 days
These levels help distinguish between inefficient governance,
functional deliberation, and overly streamlined approvals.
4) KPI 4: Decentralisation: This KPI addresses the concen-
tration of resources and the degree of autonomy in operations. It
combines token distribution, member activity, and automation.
Inspired by work on DAO structures [24], [32], we assess
decentralisation based on the largest token holder’s share,
whether there is sufficient participation, and whether decisions
are executed automatically. We label a DAO’s decisions as
“fully automated” when successful on-chain proposals directly
trigger contract execution without requiring off-chain signatures
or multi-sig confirmations.
• Low: Largest holder >66%
• Medium-Low: 33–66%
• Medium: 10–33%, with at least medium participation, no
automation
• Medium-High: 10–33%, with medium/high participation,
full automation
• High: <10%
Our on-chain dataset allows precise measurement of token
distributions and automation status. These categories differen-
tiate between DAOs with strong individual control and those
exhibiting distributed ownership and autonomous operations.
5) Scoring System: Each KPI level is mapped to a numeric
score from 0 to 3, with all four KPIs equally weighted.
The total score ranges from 0 to 12. This uniform scheme
avoids arbitrary prioritisation and reflects our assumption
that DAO sustainability results from balanced performance
across community, financial, procedural, and structural domains.
Table I summarises the scoring.
This scoring method reflected our assumption that DAO
sustainability depends on a balanced combination of social
(participation), financial (funds), procedural (voting efficiency),
and organisational (decentralisation) factors. We used equal
TABLE I: KPIs and Their Level Divisions with Assigned
Scores
KPI Level Description Score
Network ParticipationLow Participation rate<10% 1Medium Participation rate 11%–40% 2High Participation rate>40% 3
Accumulated Funds
Low Treasury<$100 million USD 0.75
Medium-LowTreasury$100 million–$1 billion USD, circulating tokens≤50% 1.5
Medium-HighTreasury$100 million–$1 billion USD, circulating tokens>50% 2.25
High Treasury>$1 billion USD 3
V oting Mechanism EfficiencyLow Approval rate<30% and/or voting duration<3 days 1Medium Approval rate 30%–70%, voting duration 3–14 days2High Approval rate>70%, voting duration 3–14 days3
Decentralisation
Low Largest holder≥66% of resources 0.6Medium-LowLargest holder 33%–66% of resources 1.2
Medium Largest holder 10%–33%, medium participation, not fullyautomated decisions 1.8
Medium-HighLargest holder 10%–33%, medium/high participation, fullyautomated decisions 2.4
High Largest holder<10% of resources 3
weights to avoid introducing arbitrary prioritisation, though
future work may adjust this based on further analysis.
By combining these four KPIs, each based on our harmonised
on-chain dataset, we developed a multidimensional view of
DAO sustainability and enabled comparative analysis across
different governance structures.
B. Dataset Construction
Our initial data collection included 5,999 DAOs from
aggregator sources, most notably, the DAO Analyzer dataset
from Kaggle. However, after applying strict criteria for on-
chain voting and recent governance activity, most entries
failed to meet our thresholds for meaningful participation 2.In
particular, only a negligible number of DAOs (2 DAOs) from
the Kaggle dataset exhibited the required level of governance
activity; hence, we opted to exclude this dataset from our final
analysis. To address this, we developed the custom pipeline
described in Section III-C, creating a harmonized on-chain
dataset comprising 50 DAOs that demonstrated:
• Robust on-chain governance mechanisms
• Transparent participation profiles
• Key activity metrics (e.g., average voting duration, pro-
posal frequency, treasury size)
We classified DAOs into four activity categories:
1) Highly Active: DAOs with at least 5 governance-related
transactions in the last 30 days, showing consistent
involvement from multiple members.
2) Moderately Active : DAOs with at least 1 transac-
tion/proposal in the last 90 days, maintaining regular
community activity.
3) Minimally Active : DAOs with transactions/proposals
older than 90 days and low recent activity.
4) Potential Test or Dormant : DAOs with fewer than 2
transactions since creation, possibly representing experi-
mental deployments or abandoned projects.
These thresholds follow conventions in blockchain governance
literature, which often uses monthly and quarterly assessments
to track participation trends [25].
Before calculating KPIs, we performed several validation
checks:
• Removal of duplicates
2https://github.com/smeneguz/data-analyzer-dao-ecosystem.git

---

## Page 5

5
Fig. 1: Multi-chain on-chain retrieval pipeline
• Consistency checks across sources
• Standardisation of timestamps
• Verification of event logs by comparing proposal creation
and execution events
Any inconsistencies prompted targeted queries to blockchain
nodes or re-examination of aggregator data, helping ensure a
reliable dataset.
C. Data Collection Pipeline
Understanding DAO dynamics required thorough data ex-
traction and analysis from multiple sources. Our multi-chain
on-chain retrieval pipeline, illustrated in Figure 1, consisted of
the following steps:
DAO and Token Address Enumeration (Step 1 in Figure 1):
We identified candidate DAOs on Ethereum and other EVM-
compatible networks (e.g., Polygon, Arbitrum, BNB Chain) by
scanning known governance contracts and verifying that they
supported on-chain voting transactions.
As shown in the leftmost panels of Figure 1, we processed
governance contracts and token contracts separately, organizing
their addresses and interfaces into config files for subsequent
processing.
Setup for Multi-chain Access (Step 2 in Figure 1): We con-
figured connections to multiple blockchain networks through
node providers and explorers. As shown in the second panel of
Figure 1, this involved setting up environment configurations
(.ENV files) to access Ethereum, Polygon, Arbitrum, BNB
Chain, and Optimism networks, ensuring broad coverage of
DAO activity.
Smart Contract Event Retrieval (Step 3 in Figure 1): For
each DAO’s governance contract(s) and associated token(s), we
queried block explorers and node providers to fetch all event
logs from the deployment block until April 2025. In parallel,
we retrieved transactions from the associated governance token
smart contracts to capture token transfers and other economic
events. As shown in the third panel of Figure 1, this process
created separate datasets for smart contract events and token
transactions, which were stored in dedicated databases for later
analysis.
Event Decoding and Data Normalisation (Step 4 in Figure 1):
We decoded each raw log using the contract’s ABI to map event
signatures into human-readable records. We then converted
timestamps to UTC, normalized token amounts, and filtered
out repeated or malformed entries. The fourth panel of
Figure 1 illustrates how we transformed raw blockchain data
into structured event files (events decoded, eventName.json,
eventName2.json), making them suitable for analysis.
Cross-linking Governance and Token Data (Step 5 in Fig-
ure 1): To assess how voting power correlated with participation,
we supplemented event data with historical token transfers
retrieved via RPC nodes, enabling us to track token holder
distribution over time and identify concentrated voting power.
As shown in the fifth panel of Figure 1, we processed token
information into standardized JSON formats that captured
ownership patterns and voting activity.
DAO Data Extraction and Analysis (Step 6 in Figure 1):
We integrated governance events with token distribution data
to create a consistent view of each DAO’s activity. The sixth
panel of Figure 1 shows how we combined these datasets into a
unified format that enabled consistent analysis across different
DAOs and governance models.
Harmonised Dataset Output and Visualization (Step 7
in Figure 1): Finally, we generated standardized files for
each DAO, including key fields such as total proposals,
voter addresses, top holders, and execution outcomes. This
structured output, represented in the rightmost panel of Figure 1,
formed the basis for KPI calculation, statistical analysis, and
visualization through customised dashboards.
IV. R ESULTS
Our sample consists of 50 DAOs spread across Ethereum,
Polygon, and Arbitrum. Together, they account for 6930
proposals, 317317 unique voting addresses and 4524205 total
members, providing a robust basis for evaluating governance
patterns. We applied the Shapiro–Wilk test for normality and
Levene’s test for variance homogeneity to assess the suitability
of parametric methods. Based on the results of these tests, we
used one-way ANOV A for normally distributed groups with
homogeneous variances, and the Kruskal–Wallis test for cases
where these assumptions were violated. To complement the
statistical analysis, we generated box plots, violin plots, scatter
plots with regression lines and radar charts. These visualisations
illustrate the relationships among the KPI metrics and facilitate
the empirical evaluation of the proposed framework using our
newly compiled dataset of 50 DAOs.

---

## Page 6

6
A. Statistical Approach
We structured the data analysis as a sequence of standard
tests to verify statistical assumptions and ensure that group
comparisons were conducted appropriately.
1) Shapiro–Wilk Test for Normality: For each KPI category
(e.g. Low, Medium, High), we first evaluated whether the data
followed a normal distribution. The Shapiro–Wilk test [33]
was used, with the test statistic W computed as:
W =
Pn
i=1 ai x(i)
2
Pn
i=1(xi − ¯x)2 ,
where x(i) denotes the i-th order statistic (i.e., the sample
sorted in ascending order), ¯x is the sample mean, and ai
are constants derived from the covariance matrix of a normal
distribution. A p-value below a commonly used threshold (0.05)
led to rejection of the null hypothesis of normality. Given the
Shapiro–Wilk test’s sensitivity to small sample sizes, we report
its results only for categories with n ≥ 3.
2) Levene’s Test for Variance Homogeneity: We used Lev-
ene’s test [34] to assess whether variances were homogeneous
across groups. For k groups, let Xij denote the j-th observation
in the i-th group, with i = 1 , . . . , k. The test statistic is
computed as:
WLevene = (N − k)Pk
i=1 ni
 
Zi· − Z··
2
(k − 1)Pk
i=1
Pni
j=1(Zij − Zi·)2
,
where Zij = |Xij − ¯Xi| (or, alternatively, the median may
be used in place of the mean), Zi· is the mean of group i
after transformation, and Z·· is the overall mean of all Zij. N
denotes the total number of observations, and ni is the size
of group i. A significant p-value (typically < 0.05) indicates
heterogeneity of variances across groups.
3) Parametric vs. Non-parametric Group Comparisons:
(1) One-Way ANOV A: If all groups satisfied the normality
assumption (Shapiro–Wilk) and exhibited homogeneous vari-
ances (Levene’s), we applied one-way Analysis of Variance
(ANOV A) to test for differences in group means. The ANOV A
F -statistic was evaluated against the null hypothesis that all
group means are equal [35].
(2) Kruskal–Wallis Test: When either normality or homo-
geneity of variances was not satisfied, we used the Kruskal–
Wallis test [36]:
H = 12
N(N + 1)
kX
i=1
ni R2
i − 3 (N + 1),
where N is the total sample size across k groups, ni is the
sample size of group i, and Ri is the average rank within group
i. The null hypothesis states that all groups follow the same
distribution. A significant p-value indicates that at least one
group differs. Post-hoc pairwise comparisons were conducted
using Dunn’s test with Bonferroni correction to identify specific
group differences.
4) Interpretation of Test Outcomes: To guide the application
of statistical tests, we established a decision process based on
the outcomes of normality and variance homogeneity checks.
Table II summarises the interpretation criteria for the Shapiro–
Wilk, Levene’s, ANOV A, and Kruskal–Wallis tests, along with
the corresponding implications for group comparison methods.
TABLE II: Interpretation of statistical test outcomes and
corresponding analysis decisions.
Condition Interpretation
Shapiro–Wilkp-value<0.05 Data deviate from normality; ANOV A not used.
Levene’s Testp-value<0.05 Variances differ; ANOV A not used.
ANOV Ap-value<0.05 At least one group mean differs significantly.
Kruskal–Wallisp-value<0.05 At least one group distribution differs; post-hoc tests applied.
This procedure ensures that each KPI category is analysed
using appropriate statistical methods, reducing the risk of
misinterpretation due to violations of parametric assumptions.
The following sections present the results for each KPI,
including the applied thresholds and visualisations.
B. Network Participation
Definition. As introduced in Section III, Network Participation
measures the proportion of active members, those who cast
at least one on-chain vote or submitted a proposal, relative to
total membership. We classified DAOs into three categories:
Low (< 10%), Medium (10–40%), and High (> 40%).
Findings. Figure 2 presents the relationship between total
membership (log-scaled x-axis) and participation rate ( y-axis).
The visualisation highlights an inverse pattern: smaller DAOs
tend to show higher participation, with thresholds at 10%
and 40% marking the category boundaries. Summary statistics
indicate a low median participation rate (4.16%) and high
variability, with a few outlier values capped at 100%
Figure 3 shows notched box plots across the three participation
categories. The notches represent 95% confidence intervals
for the medians. The Shapiro–Wilk test returned p-values
below 0.05 for the Low and High categories, and Levene’s
test indicated unequal variances. Based on these results, we
applied the Kruskal–Wallis test, which identified significant
group differences ( H = 30.45, p < 0.01). Post-hoc analysis
using Dunn’s test with Bonferroni correction confirmed that
the High group had a significantly higher median participation
rate (median = 98.29%) than the Low group (median = 2.47%),
confirming a substantial gap in user engagement across the
DAO ecosystem.
C. Accumulated Funds
Definition. Accumulated Funds reflect the DAO’s financial
capacity, incorporating both treasury size and the proportion
of circulating tokens. As defined in Section III, DAOs were
classified into four categories: Low, Medium-Low, Medium-
High, and High, based on combined thresholds for these two
dimensions.
Findings. Figure 4 visualises the distribution of DAOs by
plotting treasury value (in log scale to handle wide differences
from $1 million to billions) against circulating token percentage.

---

## Page 7

7
Fig. 2: Scatter plot showing the relationship between total
members (x) and participation rate (y)
Fig. 3: ”Notched“ box plot for Network Participation.
Threshold lines at $100 million, $1 billion, and 50% token
circulation delineate category boundaries.
Figure 5 shows notched box plots of treasury sizes grouped by
circulating token status. DAOs in the Low category (treasury
< $100 million) exhibited high variance, possibly reflecting
early-stage operations or inconsistent funding cycles. Normality
tests (Shapiro–Wilk) returned p-values below 0.05 for all
four categories, and Levene’s test indicated heterogeneity of
variances. These results support the use of non-parametric
methods for group comparisons.
Visualisation Support. We observed a weak and statistically
non-significant correlation between treasury size and circulating
token percentage (Pearson’s r ≈ −0.13, p ≈ 0.37).
D. Voting Mechanism Efficiency
Definition. V oting Mechanism Efficiency captures the balance
between approval rates and average voting duration, grouping
DAOs into Low, Medium, or High efficiency categories. This
KPI reflects the trade-off between swift decision-making and
thorough deliberation.
Findings. Figure 6 presents notched box plots of approval
rates across the three efficiency categories. The Shapiro–Wilk
Fig. 4: Scatter plot of treasury value (log scale) vs. circulating
token percentage.
Fig. 5: Notched box plot of treasury sizes, grouped by
circulating token status.
test indicated non-normality in the Low (p = 0.0373) group,
while the Medium (p = 0.4003) and High (p = 0.0804) groups
satisfied the normality assumption. Levene’s test confirmed
variance heterogeneity ( p = 0.0043). Accordingly, we applied
the Kruskal–Wallis test, which returned H = 9.4687 and p =
0.0088. Although the High group showed the highest median
approval rate (88.24%), the differences were not statistically
significant at the 5% level.
Visualisation Support. Figure 7 displays approval rate against
average voting duration, offering a joint view of the two
dimensions that define this KPI. While no direct statistical
inference is drawn, the pattern suggests that extremely short
or excessively long voting windows may undermine effective
governance. These empirical observations are consistent with
prior findings [19] recommending moderate voting periods in
DAO settings.
E. Decentralisation
Definition. Decentralisation encompasses economic distribu-
tion, participatory engagement, and the degree of on-chain
automation [24]. We classified DAOs into five categories: Low,
Medium-Low, Medium, Medium-High, and High, based on the

---

## Page 8

8
Fig. 6: Notched box plot of approval rates among the three
efficiency categories
Fig. 7: Scatter plot of approval rate versus average voting
duration
largest holder’s token share and the presence of automated
governance processes.
Findings. Figure 8 shows notched box plots of proposer concen-
tration across the five decentralisation categories. The Shapiro–
Wilk test indicated that the Medium group ( p = 0 .0018)
deviated from normality, while other groups did not violate
normality assumptions. Levene’s test showed no significant
variance heterogeneity ( p = 0 .2338). We therefore applied
the Kruskal–Wallis test, which returned H = 15 .10 and
p = 0.0045, indicating statistically significant differences in
proposer concentration among the decentralisation categories.
The Low decentralisation group (largest holder > 66%)
exhibited the highest mean proposer concentration (45.41),
while the Medium group (10–33% ownership, no automation)
had the lowest mean (9.51). These results suggest that high
token concentration does not necessarily limit proposal activity,
whereas intermediate ownership levels may correspond to
reduced proposer diversity in this dataset.
Visualisation Support. Figure 9 maps the largest holder’s
percentage against participation rate. The Pearson correlation
coefficient was weak and non-significant ( r = 0 .09, p =
0.5449), indicating no linear relationship. However, Spearman’s
rank correlation showed a moderate monotonic trend ( ρ = 0.27,
p = 0 .0644), suggesting a mild association between lower
concentration and higher engagement. Threshold lines at 10%,
Fig. 8: Notched box plot of proposer concentration across five
decentralisation categories
Fig. 9: Scatter plot of largest holder percentage versus
participation rate
33%, and 66% (economic decentralisation) and at 10% and
40% (participation) provide reference boundaries. While a slight
rank-based trend is observable, the visual evidence does not
indicate a strong predictive relationship between largest-holder
share and participation rate.
F . Composite Metrics and Overall Patterns
To summarise DAO performance across dimensions, we
constructed composite scores based on the four KPIs: Net-
work Participation, Accumulated Funds , Voting Mechanism
Efficiency, and Decentralisation.
Figure 10 presents radar plots for a subset of DAOs, illustrating
the trade-offs and balance across the four governance dimen-
sions. DAOs with more balanced profiles, showing consistent
scores across all KPIs, tend to achieve higher composite scores,
suggesting more resilient governance structures. In contrast,
DAOs that perform strongly in one or two KPIs but poorly
in others often display structural imbalances that may affect
long-term sustainability.
For example, Uniswap and Lido DAO demonstrate high finan-
cial capacity but score lower in decentralisation. By contrast,
DAOs such as Public Nouns, Lil Nouns, and Union achieve
high composite scores through more distributed governance
structures and consistent performance across participation and
voting dimensions. DAOs with lower composite scores, such

---

## Page 9

9
Fig. 10: radar composite plot - 10 daos
as HAI, Open Dollar, and Unlock, often reflect a combination
of centralised ownership and limited user engagement.
These aggregated comparisons reinforce the core premise
of the study: assessing DAO sustainability requires a multi-
dimensional perspective. Strong performance in one area does
not necessarily compensate for weaknesses in others. A com-
bined evaluation of participation, financial health, procedural
efficiency, and decentralisation provides a more complete
understanding of organisational robustness.
V. D ISCUSSION
A. Interpretation of KPI Findings
The four KPIs, Network Participation, Accumulated Funds,
V oting Mechanism Efficiency, and Decentralisation, yielded
statistically significant group differences in most cases, based
primarily on non-parametric testing. DAOs classified as High
in Network Participation and Accumulated Funds exhibited
more consistent engagement and greater financial capacity,
respectively. Those with Medium-High to High decentralisation
levels showed broader proposer distributions and lower voting
concentration. In contrast, correlations such as that between
largest-holder percentage and participation were weaker or
marginal, indicating that concentrated token ownership does
not necessarily reduce member activity.
DAOs scoring highly across multiple KPIs demonstrated
structural features associated with more sustainable governance.
These findings support the broader view that sustained commu-
nity involvement, procedural efficiency, and equitable resource
distribution jointly contribute to the resilience of decentralised
organisations.
B. Degree of Decentralisation
The results show that many DAOs exhibit partial decentralisa-
tion, with voting activity or proposal initiation often concen-
trated among a small number of addresses. However, several
cases of high decentralisation were observed, particularly where
moderate to large treasuries were combined with automated
on-chain governance mechanisms. These patterns suggest that
decentralisation is shaped not only by token distribution but also
by social and procedural dynamics such as proposer diversity,
governance automation, and participation incentives.
Notably, variations in the largest-holder percentage did not
consistently suppress network participation. This finding com-
plicates assumptions about centralisation effects, suggesting that
concentrated capital, when coupled with effective delegation
or automation, may coexist with active governance.
C. Voting Mechanism Efficiency
While DAOs classified as High in voting efficiency generally
exhibited shorter but adequate voting durations and higher
approval rates, not all observed differences across groups were
statistically significant (Section IV-D). This outcome points to
the influence of contextual factors, such as proposal complexity
or urgency, on governance behaviour. Shorter decision cycles
do not inherently imply more effective outcomes.
Scatter plots of approval rate versus average voting duration
suggested that overly short windows may hinder deliberation,
while excessively long ones can reduce engagement. A more
dynamic approach, calibrating voting duration based on prior
proposal complexity or participation history, could improve
legitimacy without sacrificing efficiency. These observations
suggest that future refinements to the boundaries for KPI 3
may strengthen its interpretive value.
D. Implications for DAO Governance
The KPI framework enables a structured diagnosis of DAO
governance strengths and weaknesses. DAOs with limited
participation but substantial financial reserves may benefit
from changes to voting accessibility or community engagement
strategies. Conversely, DAOs with strong participation but
weaker financial capacity may need to diversify treasury
structures or enhance economic sustainability mechanisms.
Governance reforms targeting concentration risk, such as token
lockups, quadratic voting, or partial delegation, may help reduce
disproportionate influence without discouraging large token
holders from participating. Effective design in this area can
facilitate broad-based input while preserving capital efficiency
[37].
More broadly, aligning governance practices with DAO-specific
operational profiles (e.g. adjusting voting durations based on
proposal type) may help ensure decision quality and continuity
over time. Our findings confirm that persistent low participation
remains a core vulnerability. This aligns with prior studies
indicating that under 10% voter turnout can lead to oligarchic
outcomes [4]. In particular, large token holders often propose
and pass initiatives with minimal community input. We showed
that DAOs with more equitable token distribution and moderate
voting windows (3–14 days) achieve higher median approval
rates and more balanced proposer activity. Hence, introducing
tiered quorums or partial delegation (as in Liquid Democracy)
could further diversify proposer authority.

---

## Page 10

10
E. Comparisons with Existing Literature
The observed patterns of partial decentralisation are consistent
with prior research on governance concentration in DAOs
[4], [6]. While many DAOs aim to implement community-led
models, token distribution and proposer activity often remain
uneven. This study builds on previous work by quantifying how
treasury size, participation rates, and voting structure relate to
sustainability indicators.
The moderate association between treasury size and participa-
tion mirrors earlier findings by [25], where financial capacity
alone did not guarantee user engagement. These findings
reinforce the view that sustainable governance depends on
multiple interacting factors, not isolated metrics.
F . Limitations and Opportunities for Future Research
Few limitations should be noted. First, the dataset includes only
DAOs meeting certain on-chain activity thresholds, excluding
organisations with limited or off-chain governance. Second, the
analysis provides a snapshot as of April 2025; DAO structures
and participation trends may evolve over time.
Future work could incorporate longitudinal analysis to observe
governance changes over time, introduce weighting schemes
based on governance outcomes, or expand coverage to off-chain
processes through community forums and governance platforms.
Analysing the gap between the realities of DAO governance
and its ideals [38] represents another avenue for future work.
Extending the pipeline to non-EVM-compatible chains, or
integrating data across bridging protocols, would improve
generalisability across DAO ecosystems. Finally, refining score
thresholds and incorporating adaptive metrics could make the
framework more responsive to DAO-specific use cases, such
as fast-moving DeFi projects or socially-driven communities.
VI. T HREATS TO VALIDITY
A. Construct Validity
Definition of KPIs. The four KPIs provide a structured view of
DAO governance but are proxies for broader qualities. Off-chain
deliberation, community sentiment, and informal leadership
are not captured in on-chain data. As such, participation and
voting metrics may underestimate engagement in DAOs that
rely on off-chain activity.
Boundaries of KPI Thresholds. Thresholds (e.g. 10% and
40% for participation; $100 million and $1 billion for treasury
size) are based on empirical patterns and conceptual rationale.
However, small differences (e.g. 9% vs. 10%) can shift category
placement. Token-based decentralisation thresholds may also
not apply uniformly across DAO types, introducing subjectivity
into classification.
B. Internal Validity
Data Completeness. The dataset includes DAOs with active
on-chain governance, excluding those led off-chain. This
reduces reliance on aggregator dashboards but may bias the
sample toward more formal or transparent governance models,
influencing KPI trends.
Measurement Accuracy. Node queries and event de-
coding can be affected by parsing errors, outdated
ABIs, or contract anomalies. Despite validation (e.g.
ProposalCreated/Executed checks), some modules de-
viate from expected schemas. We addressed this via schema-
based normalization and curated data, reaching 99.8% coverage.
C. External Validity
Generalisability of Findings. Our analysis focuses on
Ethereum and EVM-compatible networks, which follow
ERC-20/721 governance models. Governance in Tendermint-,
Cosmos-, or Substrate-based DAOs may differ, so findings may
not generalise beyond EVM contexts.
Temporal Context. The dataset captures DAO governance as of
April 2025. Given evolving rules, tokenomics, and participation,
KPI scores may change. A longitudinal approach would better
reflect governance stability and change over time.
D. Reliability
Reproducibility of the Pipeline. The analysis relies on third-
party services (e.g. Infura, Alchemy, Etherscan), which may
face downtime or updates. Script or API changes can affect
future runs. While version control and pinned contracts were
used, replication may still be impacted by ABI or ecosystem
changes.
Thresholding and Scoring Variations. An equal-weighted
scoring scheme was used to reduce bias, but alternative weights
or finer scoring could shift results. Open-source code and clear
definitions support replication and comparison across models.
While the study ensures robustness through direct data collec-
tion and defined KPIs, some limitations remain: threshold trade-
offs, exclusion of off-chain activity, and limited generalisability
to EVM-based DAOs. Still, the data supports strong links
between governance sustainability and participation, decentral-
isation, financial robustness, and procedural efficiency. Future
work integrating off-chain and multi-chain data can expand
coverage and address these gaps.
VII. C ONCLUSION
This study introduced a data-driven framework for evaluating
DAO governance, combining four empirically grounded KPIs:
Network Participation, Accumulated Funds, V oting Mechanism
Efficiency, and Decentralisation, into a unified analytical model.
Analysis of on-chain data across a diverse set of 50 DAOs
revealed that higher sustainability scores tend to be associated
with broader participation, decentralised control, and balanced
financial and procedural structures. These findings reinforce
the view that sustainability is shaped by the interaction of
social, economic, and procedural factors, rather than any
single attribute. The framework offers a replicable basis for
comparative analysis and may support both academic research
and practitioner decision-making in decentralised governance.
Evaluating DAOs as complex socio-technical systems, rather
than through isolated metrics, provides a more accurate account
of their governance dynamics. Future work can refine this model
through longitudinal evaluation, off-chain data integration, and
cross-chain extensions.

---

## Page 11

11
REFERENCES
[1] V . Buterin, “DAOs, DACs, DAs and more: An incomplete terminology
guide,” Ethereum Blog, 2014.
[2] S. Hassan and P. De Filippi, “Decentralized autonomous organization,”
Internet Policy Review, vol. 10, no. 2, pp. 1–10, 2021, https://doi.org/10.
14763/2021.2.1556.
[3] J. Tan, T. Merk, S. Hubbard, E. R. Oak, H. Rong, J. Pirovich, E. Rennie,
R. Hoefer, M. Zargham, J. Potts, C. Berg, R. Youngblom, P. De Filippi,
S. Frey, J. Strnad, M. Mannan, K. Nabben, S. N. Elrifai, J. Hartnell, B. M.
Hill, T. South, R. L. Thomas, J. Dotan, A. Spring, A. Maddox, W. Lim,
K. Owocki, A. Juels, and D. Boneh, “Open problems in daos,” arXiv
cs.CY, vol. 2310.19201, June 17 2024, https://arxiv.org/abs/2310.19201.
[4] R. Feichtinger, R. Fritsch, Y . V onlanthen, and R. Wattenhofer, “The
hidden shortcomings of (d)aos – an empirical study of on-chain
governance,” in International Conference on Financial Cryptography
and Data Security . Springer-Verlag, 2023, pp. 165–185, https://doi.org/
10.1007/978-3-031-48806-1 11.
[5] J. Han, J. Lee, and T. Li, “A review of dao governance:
Recent literature and emerging trends,” Journal of Corporate
Finance, vol. 91, p. 102734, 2025. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0929119925000021
[6] S. Wang, W. Ding, J. Li, Y . Yuan, L. Ouyang, and F.-Y . Wang, “Decen-
tralized autonomous organizations: Concept, model, and applications,”
IEEE Transactions on Computational Social Systems , vol. 6, no. 5, pp.
870–878, 2019.
[7] V . Buterin, “Ethereum white paper: A next-generation smart contract
and decentralized application platform,” Ethereum, 2014.
[8] Q. DuPont, “Experiments in algorithmic governance: A history and
ethnography of “the dao”, a failed decentralized autonomous organization,”
in Bitcoin and Beyond . Routledge, 2017, pp. 157–177.
[9] L. Liu, S. Zhou, H. Huang, and Z. Zheng, “From technology to society:
An overview of blockchain-based dao,” IEEE Open Journal of the
Computer Society, vol. 2, pp. 204–215, 2021.
[10] H. Altaleb and R. Zolt ´an, “Decentralized autonomous organizations
review, importance, and applications,” in 2022 IEEE 26th International
Conference on Intelligent Engineering Systems (INES), 2022, pp. 000 121–
000 126.
[11] Q. Wang, G. Yu, Y . Sai, C. Sun, L. D. Nguyen, X. Xu, and S. Chen,
“A first look into blockchain daos,” in ICBC, 2023, pp. 1–3. [Online].
Available: https://doi.org/10.1109/ICBC56567.2023.10174961
[12] A. Wright, “The Rise of Decentralized Autonomous Organizations:
Opportunities and Challenges,” Stanford Journal of Blockchain Law
& Policy, jun 30 2021, https://stanford-jblp.pubpub.org/pub/rise-of-daos.
[13] T. V . S. Online, “Subchapter 012: Blockchain-based limited liability
companies,” 2018, https://legislature.vermont.gov/statutes/section/11/025/
04173?ref=internetnative.org.
[14] I. N. Organization, “Wyoming dao jurisdictions,” 2023, https://
internetnative.org/wyoming-dao/.
[15] N. I. Organization, “Marshall island dao jurisdictions,” 2023, https:
//internetnative.org/marshall-islands-dao/.
[16] R. B. Lamb, “Utah passes innovative dao legislation,” 2023, https://
natlawreview.com/article/utah-passes-innovative-dao-legislation.
[17] J. Ma, M. Jiang, J. Jiang, X. Luo, Y . Hu, Y . Zhou, Q. Wang, and F. Zhang,
“Understanding security issues in the dao governance process,” IEEE
Transactions on Software Engineering , pp. 1–16, 2025.
[18] Y . Liu, Z. Gao, Y . Xia, and Z. Zhang, “From technology to society:
An overview of blockchain-based DAO,” in 2019 IEEE 1st Interna-
tional Conference on Civil Aviation Safety and Information Technology
(ICCASIT). IEEE, 2019, pp. 518–522.
[19] Y . Fan, L. Zhang, R. Wang, and M. A. Imran, “Insight into voting in
daos: Conceptual analysis and a proposal for evaluation framework,”
Netwrk. Mag. of Global Internetwkg. , vol. 38, no. 3, p. 92–99, Jun.
2023. [Online]. Available: https://doi.org/10.1109/MNET.137.2200561
[20] Q. Ding, W. Xu, Z. Wang, and D. K. C. Lee, “V oting schemes
in dao governance,” p. 2350004, 2023. [Online]. Available: https:
//doi.org/10.1142/S2811004823500045
[21] N. Dimitri, “V oting in DAOs,”ACM SIGecom Exchanges , vol. 21, no. 2,
pp. 39–48, 2023.
[22] R. Beck, C. M ¨uller-Bloch, and J. L. King, “Governance in the blockchain
economy: A framework and research agenda,” Journal of the Association
for Information Systems , vol. 19, no. 10, 2018, https://aisel.aisnet.org/
jais/vol19/iss10/1, DOI: 10.17705/1jais.00518.
[23] R. Fritsch, M. M ¨uller, and R. Wattenhofer, “Analyzing voting power in
decentralized governance: Who controls daos?” Blockchain: Research
and Applications , vol. 5, no. 3, p. 100208, 2024. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S2096720924000216
[24] H. Park, I. Ureta, and B. Kim, “Developing dimensions and indicators
to measure decentralization in decentralized autonomous organizations,”
Administrative Sciences , vol. 13, no. 11, 2023. [Online]. Available:
https://www.mdpi.com/2076-3387/13/11/241
[25] Y . Faqir-Rhazoui, J. Arroyo, and S. Hassan, “A comparative
analysis of the platforms for decentralized autonomous organizations
in the ethereum blockchain,” Journal of Internet Services and
Applications, vol. 12, pp. 1–20, 2021. [Online]. Available: https:
//doi.org/10.1186/s13174-021-00139-6
[26] R. Qin, W. Ding, J. Li, S. Guan, G. Wang, Y . Ren, and Z. Qu,
“Web3-based decentralized autonomous organizations and operations:
Architectures, models, and mechanisms,” IEEE Transactions on Systems,
Man, and Cybernetics: Systems , pp. 2073–2082, 2022.
[27] Q. Wang, G. Yu, Y . Sai, C. Sun, L. D. Nguyen, and S. Chen,
“Understanding daos: An empirical study on governance dynamics,” IEEE
Transactions on Computational Social Systems , pp. 1–19, 2025.
[28] C.-C. Tsai, C.-C. Lin, and S.-W. Liao, “Unveiling vulnerabilities in dao:
A comprehensive security analysis and protective framework,” in 2023
IEEE International Conference on Blockchain (Blockchain) , 2023, pp.
151–158.
[29] O. Rikken, M. Janssen, and Z. K. and, “Governance impacts of
blockchain-based decentralized autonomous organizations: an empirical
analysis,” Policy Design and Practice , vol. 6, no. 4, pp. 465–487, 2023.
[Online]. Available: https://doi.org/10.1080/25741292.2023.2270220
[30] A. Pe˜na-Calvin, J. Saldivar, J. Arroyo, and S. Hassan, “A categorization of
decentralized autonomous organizations: The case of the aragon platform,”
IEEE Transactions on Computational Social Systems , vol. 11, no. 6, pp.
8143–8155, 2024.
[31] G. Liu, “The illusion of democracy— why voting in decentralized
autonomous organizations is doomed to fail,” NYU Law and
Economics Research Paper , pp. 24–13, 2024. [Online]. Available:
http://dx.doi.org/10.2139/ssrn.4441178
[32] V . Lo Monaco, P. Momtaz, and S. Vismara, “Distributed governance
and value creation in decentralized autonomous organizations:
Evidence from a regression discontinuity design,” Economics
Letters, vol. 248, p. 112233, 2025. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0165176525000709
[33] S. S. Shapiro and M. B. Wilk, “An analysis of variance test for normality
(complete samples),” Biometrika, vol. 52, no. 3/4, pp. 591–611, 1965.
[Online]. Available: http://www.jstor.org/stable/2333709
[34] H. Levene, “Robust tests for equality of variances,” in Contributions
to Probability and Statistics: Essays in Honor of Harold Hotelling .
Stanford University Press, Palo Alto, 1960, pp. 278–292. [Online].
Available: https://api.semanticscholar.org/CorpusID:117424234
[35] L. Sthle and S. Wold, “Analysis of variance (anova),” Chemometrics
and Intelligent Laboratory Systems , vol. 6, no. 4, pp. 259–272, 1989.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
0169743989800954
[36] W. H. Kruskal and W. A. Wallis, “Use of ranks in one-
criterion variance analysis,” Journal of the American Statistical
Association, vol. 47, no. 260, pp. 583–621, 1952. [Online]. Available:
http://www.jstor.org/stable/2280779
[37] D. Rozas, A. Tenorio-Forn ´es, S. D ´ıaz-Molina, and S. Hassan, “When
ostrom meets blockchain: Exploring the potentials of blockchain for
commons governance,” SAGE Open, 11(1). , 2021.
[38] A. Alawadi, N. Kakabadse, A. Kakabadse, and S. Zuckerbraun, “Decen-
tralized autonomous organizations (daos): Stewardship talks but agency
walks,” Journal of Business Research , vol. 178, p. 114672, 05 2024.

---
