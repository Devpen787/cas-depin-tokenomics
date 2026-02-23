# Meneguzzo_Schifanella_Gatteschi_Destefanis_2026_OperationalisingDAOSustainabilityKPIs_AMultiChainDashboardForGovernanceAnalytics.pdf

## Page 1

Operationalising DAO Sustainability KPIs: A Multi-Chain
Dashboard for Governance Analytics
Silvio Meneguzzo
University of Turin
Turin, Italy
silvio.meneguzzo@unito.it
Claudio Schifanella
University of Turin
Turin, Italy
claudio.schifanella@unito.it
Valentina Gatteschi
Politecnico di Torino
Turin, Italy
valentina.gatteschi@polito.it
Giuseppe Destefanis
University College London
London, UK
g.destefanis@ucl.ac.uk
Abstract
We present DAO Portal, a production-grade analytics pipeline and
interactive dashboard for assessing the sustainability of Decen-
tralised Autonomous Organisations (DAOs) through Key Perfor-
mance Indicators (KPIs) derived from on-chain governance and
token events. Building on our previous work, which defined and
validated a multidimensional KPI framework for DAO sustainabil-
ity, this paper moves from theory to practice by operationalising
that framework in software infrastructure designed for finance and
FinTech contexts. The system ingests governance and treasury data
from major EVM networks, harmonises the outputs, and computes
sustainability scores across four dimensions: participation, accu-
mulated funds, voting efficiency, and decentralisation. A composite
0 to 12 score is then derived using transparent thresholds that are
applied client-side in the browser.
Using a curated snapshot of more than 50 active DAOs covering
6,930 proposals and 317,317 unique voting addresses, we show how
the platform surfaces recurring patterns such as persistently low
participation and concentration of proposal activity. These results
demonstrate how DAO Portal supports the diagnosis of governance
risks and the comparison of design choices across DAOs. To pro-
mote reproducibility and adoption, we release source code, data
schema, and dashboard implementation. By turning governance
traces into measurable and explainable KPIs, DAO Portal provides
auditable evidence of DAO sustainability and contributes software
engineering infrastructure for financial applications where trea-
suries and decision-making rights involve significant assets.
CCS Concepts
•Software and its engineering → Software architectures;•
Information systems → Decision support systems;Data ana-
lytics; Electronic commerce;•Security and privacy → Distributed
systems security.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
FinanSE ’26, Rio De Janeiro, Brazil
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Keywords
DAOs, Blockchain Analytics, Governance, Sustainability, KPI, Re-
producibility, Software Engineering for Finance
ACM Reference Format:
Silvio Meneguzzo, Claudio Schifanella, Valentina Gatteschi, and Giuseppe
Destefanis. 2026. Operationalising DAO Sustainability KPIs: A Multi-Chain
Dashboard for Governance Analytics. InFinanSE ’26: AI for SE in Financial
Firms Workshop, April 2026, Rio De Janeiro, Brazil.ACM, New York, NY,
USA, 8 pages.
1 Introduction
Decentralised Autonomous Organisations (DAOs) govern protocol
changes and manage sizeable treasuries within DeFi and related
financial ecosystems. As these organisations mature, regulators,
investors, and protocol stewards require transparent, auditable, and
reproducible evidence about governance health and operational
sustainability. Prior studies documented participation patterns, pro-
poser dynamics, and concentration of voting power, and highlighted
measurement challenges across chains and tooling [ 1, 2, 8, 11].
In our previous study, we derived a set of sustainability key per-
formance indicators (KPIs) from theory and validated them on a
curated on chain dataset [ 7]. This paper moves from theory to
practice by engineering DAO Portal1 , a production-oriented an-
alytics pipeline and dashboard that computes those KPIs at scale
across heterogeneous blockchains and exposes them through an
explainable and reproducible interface.
Existing analytics focus on market and token activity, with lim-
ited coverage of governance specific signals such as voter participa-
tion dynamics, proposer concentration, and holder dispersion [1, 2].
Method auditability is also weak, which hampers regulator and
operator use [8, 11]. In financial contexts, where treasury control
and voting outcomes condition the movement and safety of assets,
operational teams face software engineering challenges that mirror
those in traditional financial firms: the need for repeatable data in-
gestion pipelines, traceable calculations with clear provenance, and
comparative views that support risk assessment, audit readiness,
and regulatory review. These requirements align with established
practices in financial software engineering, where reproducibility
and independent verification are prerequisites for compliance.
1Live demo (test deployment): http://daoportal.space/ (mirror: http://130.192.84.45:
8080/). The demo serves the 50 DAO snapshot used in this paper; endpoints are
read only and may be rate limited.
arXiv:2601.14927v1  [cs.CE]  21 Jan 2026

---

## Page 2

FinanSE ’26, April 2026, Rio De Janeiro, Brazil Meneguzzo et al.
We address this gap with a service architecture in which a back-
end serves harmonised governance and token metrics from pre-built
JSON snapshots, and a frontend computes the sustainability KPIs.
The system provides single DAO drill downs covering participa-
tion, token distribution, treasury, and proposal statistics, together
with a multi DAO table offering client side sorting and banding.
Using a snapshot of 50 active DAOs across major EVM networks
(Ethereum, Optimism, BNB Smart Chain (BSC), Arbitrum, Poly-
gon (Matic) Mainnet), covering 6,930 proposals and 317,317 unique
voting addresses (as in [ 7]), DAO Portal surfaces recurring pat-
terns, including persistently low turnout and concentration among
proposers [8, 11]. In this way the platform acts as software engi-
neering infrastructure for finance, turning governance traces into
measurable KPI for sustainability, reproducibility, and regulatory
inspection.
This paper offers four contributions:
(1) an operational system that implements the sustainability
KPIs at scale with end to end provenance from ingestion to
dashboard;
(2) a multi chain data collector for EVM governance and token
events with harmonised schemas suitable for longitudinal
and cross DAO analysis;
(3) a composite sustainability score (0 to 12) with transparent
definitions and thresholds exposed via the API to enable
consistent comparisons;
(4) reproducible artefacts, including code, schema, and example
datasets, intended to support evaluation and adoption in
finance and FinTech settings.
The remainder of the paper details the system architecture (Sec-
tion 3), the data pipeline and KPI computation (Section 4), the
dashboard and APIs (Section 4.6), the empirical evaluation (Sec-
tion 5), and a discussion of implications and limitations (Section 6
and Section 7).
2 Background and Related Work
Decentralised Autonomous Organisations (DAOs) are crypto-native
organisations whose rules and assets are administered by smart
contracts, with governance typically mediated by token-weighted
voting. In practice, governance spans on-chain mechanisms, where
proposals are encoded, voted, and executed by contracts, and off-
chain signalling, where deliberation and preference aggregation
occur on forums or polling systems before being bridged to on-
chain execution. Common EVM patterns comprise a lifecycle of
proposal creation, discussion, voting, and execution, with timelocks
and access-control policies determining when and how approved
actions take effect. Delegation is widely employed to concentrate
voting rights in active representatives while preserving underlying
ownership. Governor-style contracts exemplify on-chain voting and
execution, whereas Snapshot is an instance of off-chain signalling
whose outcomes may be enacted via multisignatures or timelocked
controllers, depending on the DAO’s operational model [1, 11].
A typical vote specifies a snapshot of voting power, a quorum
or threshold criterion, a fixed voting window, and result aggre-
gation overfor,against, andabstainoptions, before an execution
step triggers one or more contract calls. Variants differ in whether
abstentions count toward quorum, how proposer eligibility is de-
termined, and whether execution is fully automated or requires
human intervention.
2.1 Sustainability considerations for governance
Sustainability in DAO governance involves organisational partici-
pation and legitimacy, financial capacity, and operational reliabil-
ity. Persistent low turnout, proposer and delegate concentration,
and underlying holder concentration create risks of plutocracy.
Game-theoretic analyses of DAO voting behaviour suggest that
rational self-interest can amplify these dynamics when incentive
structures are misaligned [6]. Voting-window design and quorum
calibration can reinforce these dynamics. Execution pathways (au-
tonomous timelock versus multisig mediation), upgradeability, and
cross-chain fragmentation further introduce operational fragility.
On-chain traces provide useful but partial proxies for these proper-
ties, since off-chain deliberation, identity ambiguity, and heteroge-
neous contract semantics limit comparability without normalisation
and audit trails [8, 11].
Building on our prior work, we adopt a bounded and inter-
pretable KPI framework for DAO sustainability, defined over four
dimensions with explicit thresholds and aggregation rules [7]. The
composite sustainability score is calculated by summing the four
dimensions (Network Participation, Accumulated Funds, Voting
Mechanism Efficiency, and Decentralization) with equal weight to
yield a value of 0–12. Thresholds and measurement policies are
defined in prior work. This paper operationalises those definitions
in production software via DAO Portal, computing the constituent
KPIs and the composite across multiple chains.
2.2 Related work
(i) Blockchain and DeFi analytics platforms provide market- and
protocol-oriented dashboards that are useful for exploratory anal-
ysis but offer limited governance-specific observability. General-
purpose tools such as DeepDAO aggregate treasury valuations and
membership counts across DAOs, while Boardroom and Tally focus
on vote aggregation and delegation tracking for on-chain gover-
nance. These platforms support discovery and participation but
do not expose auditable KPI calculations, lack cross-chain schema
harmonisation, and do not provide the threshold-based scoring
required for reproducible sustainability assessment [ 1, 2]. DAO-
Analyzer offers visualisation of participation and temporal evolu-
tion but does not compute composite sustainability indicators or
support multi-chain comparisons with explicit provenance.
(ii) Empirical DAO governance studies document participation
patterns, proposer dynamics, concentration of voting power, and
lifecycle timings across selected DAOs and protocols. These studies
improve construct understanding but often rely on single-chain
scopes, manual stitching of off-chain artefacts, or ad hoc denomi-
nators, which constrains cross-DAO comparability and auditability
[8–10]. Broader ecosystem censuses confirm oligarchic tendencies
and low participation, but rarely provide the governance-aware
schemas required for KPI computation at scale [9].
(iii) Software engineering work on blockchain monitoring ad-
dresses ingestion, normalisation, provenance, and explainability,
including archive-node pipelines and schema harmonisation. These

---

## Page 3

Practical KPI-Based DAO Sustainability Analytics FinanSE ’26, April 2026, Rio De Janeiro, Brazil
contributions underpin auditability, yet few incorporate governance-
aware state machines (for example, proposal–vote–execution link-
age and cross-chain message tracking) that are required to explain
KPI movements and support accountability [3, 4].
Taken together, the literature indicates a gap: prior work does
not operationalise a theory-grounded sustainability KPI framework
into a multi-chain, auditable, reproducible, and explainable system
and dashboard as delivered by DAO Portal. This motivates the de-
sign choices in Section 3 and the multi-chain pipeline in Section 4.
By encoding governance-aware semantics and provenance, DAO
Portal enables comparative, audit-ready analyses. As DAOs increas-
ingly manage significant treasuries and decision-making rights, this
type of software engineering infrastructure contributes directly to
financial applications where transparency, reproducibility, and reg-
ulatory inspection are required.
3 System Overview
DAO Portal provides an auditable, reproducible, and explainable
pipeline that delivers DAO sustainability KPIs and a 0–12 composite
score to analysts and practitioners, operationalising the framework
in [7] within a production-ready web application.
3.1 Architecture
DAO Portal consists of a FastAPI backend and a Next.js 14 fron-
tend. The reference implementation is database-backed: a Celery
worker can import harmonised JSON files from a mounted directory
(/data), create a MetricRun, and persist one MetricSnapshot per
metric block in Postgres. The backend exposes read-only endpoints;
no server-side scoring is performed. For lightweight demonstra-
tions, the frontend can operate in a file-backed mode by reading
a bundled JSON snapshot (web/public/dao_data.json) without
contacting the backend. This dual mode allows operators to choose
between (i) database-backed deployments with historical runs and
queueable imports, and (ii) read-only snapshot mode for quick eval-
uation. A schematic of the serving path is presented in Figure 1.
3.2 Component responsibilities
Backend (FastAPI).Exposes read-only endpoints that serve har-
monised JSON blocks per DAO.
Frontend (Next.js 14).Renders single-DAO drill-downs and a
multi-DAO comparison table. It applies fixed, documented thresh-
olds to compute the four KPIs (each up to 3 points) and their 0–12
sum in the browser.
Optional operations (private deployments).Operators may attach
a database and import jobs to persist multiple runs over time. These
features are not used in the public test deployment described here.
3.3 Data and control flow
(1) Ingestion (optional, worker).A Celery job reads har-
monised JSON files under /data, records a MetricRun, and
persists namedMetricSnapshotblocks
(e.g.,network_participation,accumulated_funds,
voting_efficiency, decentralisation, health_metrics).
(2) Serving (backend).FastAPI exposes read-only endpoints
that return the latest or run-scoped blocks for one or more
DAOs.
(3) Scoring and visualisation (frontend).The browser fetches
the blocks, computes KPI scores and the 0–12 composite with
fixed thresholds, and renders single- and multi-DAO views.
In demo mode, the frontend consumes
web/public/dao_data.json.
3.4 API surface (v1)
The system exposes a minimal, stable API surface used by the UI:
•GET /api/v1/daos: paginated list of DAOs with metadata.
•GET /api/v1/daos/{id}/enhanced_metrics : the five canon-
ical metric blocks for one DAO.
•GET /api/v1/daos/metrics/multi?dao_ids=... : metric
blocks for multiple DAOs, optimised for the comparison
table.
Additional endpoints support run-scoped retrieval, historical queries,
and import triggering; full API documentation is provided in the
source repository.
3.5 Data model and deployment
Each import creates a MetricRun (with timestamp and source file
path) and one MetricSnapshot per metric block, supporting run-
scoped retrieval and historical queries. The public test deployment
runs FastAPI and the Next.js frontend in containers, following
deployment patterns validated in other production blockchain sys-
tems [5]. Operators can optionally add a database for longitudinal
tracking in private installations.
4 Data Pipeline and KPI Computation
4.1 Scope and division of labour
DAO Portal separatesextractionfromserving and analytics. The
external ETL (from our prior work [7]) connects to archive nodes
across EVM chains, decodes governance and token events via ABIs,
resolves proposal lifecycles, and harmonises outputs into JSON
snapshots. DAO Portal ingests these snapshots and serves them,
while the dashboard computes the sustainability KPIs and the com-
posite score client-side and exposes them through widgets.
This separation keeps the web stack lightweight and auditable.
The repository does not include Web3 providers or ABIs, as crawl-
ing and decoding are handled upstream. The backend focuses on
deterministically transforming harmonised inputs into versioned
and explainable KPI outputs.
4.2 Snapshot contract and directory layout
The importer accepts harmonised JSON with canonical KPI blocks
either at the root or under a nestedmetrics object. In this paper, we
use five blocks:network_participation,accumulated_funds,
voting_efficiency, decentralisation, and health_metrics,
which are persisted as MetricSnapshot rows. The frontend can
also consume the same structure directly from a bundled file
(web/public/dao_data.json) in demo mode2.
{
"dao_name": "Uniswap",
2The listing shows the primary fields used for KPI computation. Additional fields
(e.g., token_distribution, health_metrics) and legacy keys are documented in the
repository. Our evaluation uses the five canonical blocks

---

## Page 4

FinanSE ’26, April 2026, Rio De Janeiro, Brazil Meneguzzo et al.
Figure 1: Serving path used in this paper: harmonised JSON snapshots → FastAPI (read-only) → Next.js (client-side KPI and
composite computation)→dashboard visualisation.
"chain_id": 1,
"timestamp": "2025-04-06T17:38:34.119947",
"network_participation": {
"num_distinct_voters": 21527,
"total_members": 393314,
"participation_rate": 5.4732,
"unique_proposers": 34
},
"accumulated_funds": {
"treasury_value_usd": 2.087864e9,
"circulating_supply": 6.28494e8,
"total_supply": 1.0e9,
"circulating_token_percentage": 62.8494
},
"voting_efficiency": {
"total_proposals": 83,
"approved_proposals": 57,
"approval_rate": 68.67,
"avg_voting_duration_days": 6.07
},
"decentralisation": {
"largest_holder_percent": 37.15,
"on_chain_automation": "Yes",
"proposer_concentration": 40.96
}
}
Mapping to API payload.The backend serves harmonised JSON
snapshots directly to the UI. The browser renders tiles and charts
from the five canonical blocks and computes per-KPI scores locally.
Table 1 summarises the mapping between snapshot fields, the API
payload consumed by the UI, and the corresponding UI components.
4.3 Ingestion and validation (file-backed,
read-only)
The backend serves a curated set of harmonised JSON snapshots
(one per DAO) produced by the upstream extractor described in
our prior work. In the public test deployment, snapshots are stored
under a mounted data directory and are loaded or cached by the API
handlers. The service isstatelesswith respect to per-run provenance;
no per-run SQL tables are required.
Validation.On read, the service checks the presence and types of
the canonical blocks:network_participation, accumulated_funds,
voting_efficiency,decentralisation, and optionally
health_metrics. Missing blocks are surfaced to the UI as empty
objects, and booleans or enums such as on_chain_automation are
normalised to true/false or "Yes"/"No" for consistent rendering.
Idempotence.Snapshots are immutable within a given deploy-
ment. Replacing a snapshot file atomically updates what the end-
points serve, ensuring deterministic behaviour for the figures pre-
sented in this paper.
4.4 Enhanced-Metrics API and Client-Side
Scoring
For interactive exploration, the UI uses two patterns: (i) a multi-
DAO endpoint for comparisons and (ii) a single-DAO endpoint for
detail.
Comparison (multi-DAO).The multi-DAO endpoint returns the
five metric blocks for each requested DAO. The
SustainabilityDashboard consumes this payload, computes four
KPI scores client-side, and renders the 0–12 composite.
Detail (single-DAO).The single-DAO endpoint returns the five
metric blocks for one DAO. Run-scoped and historical payloads are
also available (see Section 3.4).
Client-side scoring.The browser applies fixed thresholds to com-
pute the four KPIs and their 0–12 sum. The thresholds (Table 2) are
derived from our prior empirical work [7]; the scoring functions
are part of the open-source UI.

---

## Page 5

Practical KPI-Based DAO Sustainability Analytics FinanSE ’26, April 2026, Rio De Janeiro, Brazil
Table 1: Snapshot → API payload (as served by /api/v1/daos/{id}/enhanced_metrics and /api/v1/daos/metrics/multi) and
UI consumers.
Snapshot field API JSON path Used by UI
dao_name dao_name(top-level) Titles, table rows
chain_id chain_id(top-level) Table filters/labels
timestamp timestamp(top-level) Display/ordering (optional)
network_participationblocknetwork_participation(top-level) KPI card & bar chart; scoring
accumulated_fundsblockaccumulated_funds(top-level) KPI card & pie chart; scoring
voting_efficiencyblockvoting_efficiency(top-level) KPI card & pie chart; scoring
decentralisationblockdecentralisation(top-level) TokenDistribution chart; scoring
health_metricsblockhealth_metrics(top-level) Health tile (optional)
4.5 Derived Indicators
From the JSON blocks returned by the API, the UI derives a set of
indicators directly in the browser, following the logic implemented
in the open-source components:
• Turnout (%): turnout= 100 · num_distinct_voters
total_members if both fields
> 0; otherwise the participation KPI defaults to the lowest
score.3
• Approval (%): If approval_rate> 1, it is treated as a per-
centage; otherwise it is multiplied by100.
• Circulating token share (%): If bothcirculating_supply
and total_supply> 0, the UI computes100·circulating_supply
total_supply ;
otherwise it falls back to circulating_token_percentage.
•Relative treasury (% of circulating market cap):
If circulating_supply> 0and token_price_usd> 0, the
UI computes:
100 · treasury_value_usd
circulating_supply·token_price_usd; otherwise it defaults to
0and relies on absolute bins.
4.6 KPI Scoring Thresholds (UI Policy)
The browser maps these indicators to four KPI scores (each up to
3 points) using fixed thresholds implemented in the React code.
These thresholds were derived from empirical analysis in our prior
work [7], where we examined the distribution of governance met-
rics across active DAOs to identify natural breakpoints. The current
bins are calibrated for general-purpose comparison; domain-specific
deployments may require adjusted thresholds (see Section 7). Base-
lines are non-zero to avoid degenerate cases for sparse or nascent
DAOs. Table 2 summarises the rules; Listing 1 shows the abridged
implementation.
Listing 1: Abridged client scoring (matching the UI source).
constcalculateNetworkParticipation = (dao) => {
constm = dao.network_participation?.total_members ?? 0;
constv = dao.network_participation?.num_distinct_voters
?? 0;
if(m === 0 || v === 0)return1;
constrate = (v / m) * 100;
if(rate > 100)return1;
if(rate > 40)return3;
3If the computed value exceeds100%, the UI treats it as anomalous and assigns the
lowest participation score (see §4.6).
if(rate >= 10)return2;
return1;
};
constcalculateAccumulatedFunds = (dao) => {
constt = dao.accumulated_funds?.treasury_value_usd ?? 0;
constcirc = dao.accumulated_funds?.circulating_supply ??
0;
consttotal = dao.accumulated_funds?.total_supply ?? 0;
constprice = dao.accumulated_funds?.token_price_usd ?? 0;
constcircPct = total > 0 && circ > 0 ? (circ/total)*100
:
dao.accumulated_funds?.circulating_token_percentage ??
100;
constrel = circ > 0 && price > 0 ? (t / (circ*price)) *
100 : 0;
if(t >= 1e9)return3;
if(t >= 1e8)returncircPct > 50 ? 2.25 : 1.5;
if(t >= 1e7 && rel >= 10)return1.5;
if(t >= 1e6 && rel >= 5)return1.25;
return0.75;
};
Composite and sustainability levels.Scores are summed with
equal maxima to yield 𝐶=𝑆 part +𝑆 funds +𝑆 vote +𝑆 decent ∈ [ 0, 12].
Because baselines are non-zero (Table 2), the practical range of
𝐶 is [3.35, 12].4 The UI classifies sustainability asLowfor 𝐶< 6,
Mediumfor6≤𝐶<9, andHighfor𝐶≥9.
Scope of scoring (client-only).In this release, KPI and composite
scores are computed entirely in the browser from the raw snapshot
blocks. The backend does not add policy tags or versioned scoring
metadata. Any such extensions would be future work and would
be clearly flagged in API responses when introduced.
4.7 Edge Cases and Guards
• Sparse governance activity.If total_proposals<3, the
voting-efficiency KPI defaults to 1 point.
• Anomalous participation.If turnout> 100%, the partici-
pation KPI defaults to 1 (the lowest score). This conservative
4Baselines:1+0.75+1+0.6=3.35.

---

## Page 6

FinanSE ’26, April 2026, Rio De Janeiro, Brazil Meneguzzo et al.
Table 2: Client-side KPI scoring thresholds used inSustainabilityDashboard.
KPI Points Rule (key indicators)
Network Participation 3turnout>40%
210%≤turnout≤40%
1turnout< 10%or invalid (e.g., turnout> 100%or
missing denominators)
Accumulated Funds 3treasury_value_usd≥$1B
2.25 $100M–$1B andcirc_pct>50%
1.5 $100M–$1B andcirc_pct≤50%
1.5 (fallback) $10M–$1B andrel_treasury≥10%
1.25 (fallback) $1M–$1B andrel_treasury≥5%
0.75 otherwise
Voting Efficiency 3approval> 70%and3 ≤
avg_voting_duration_days≤14
230%≤approval≤70%and same duration window
1< 30%approval or duration < 3or > 14days; or
total_proposals<3
Decentralisation 3largest_holder_percent<10%
2.4 10–33%largest holder and medium/high participation
and on-chain automation=Yes
1.810–33%largest holder, otherwise
1.233–66%largest holder
0.6>66%largest holder
approach ensures that data quality issues or potential ma-
nipulation (e.g., vote-buying, Sybil activity) do not inflate
the sustainability assessment score. Our future design would
flag such anomalies explicitly for manual review; we discuss
this in Section 7.
•Automation flag.on_chain_automationmay be boolean
or the strings "Yes"/"No". The UI treats true and "Yes" as
equivalent.
• Funds fallback.If token_price_usd is missing, the rela-
tive treasury is ignored and only absolute bins and circulating-
share bins apply.
4.8 From Scores to Visuals
The SustainabilityDashboard computes KPI scores per DAO,
sums 𝐶, maps the result toHigh/Medium/Low, and renders: (i)
colour-coded KPI columns, (ii) summary tiles (counts per level
and average 𝐶), and (iii) sorting controls (by any KPI or overall).
The MetricsDashboard renders single-DAO tiles and charts from
the same raw blocks (participation, treasury, governance outcomes,
token distribution).
5 Evaluation
We evaluate DAO Portal as a software artefact along three axes
aligned with its intended use: (i)correctnessof the values shown in
the dashboard with respect to the ingested snapshots; (ii)respon-
sivenessof the read-heavy UI and API path; and (iii)practitioner
utilityfor routine governance analytics. This evaluation focuses
on functional correctness and traceability rather than synthetic
load testing or formal security analysis; we discuss these scope
limitations in Section 7. Our goal is to validate that the platform
faithfully implements the KPI framework from our prior study [7]
and supports the practitioner tasks it was designed for.
5.1 Setup
Unless stated otherwise, we use the curated snapshot of 50 active
DAOs (Section 4) served as read-only JSON blocks. The stack mir-
rors Section 3: a FastAPI backend serving harmonised snapshots and
a Next.js 14 frontend (TypeScript, shadcn/ui, Tailwind, Recharts).
The comparison view loads multi-DAO payloads; the single-DAO
view fetches metrics for one DAO. In demo mode, both views can
fall back to a bundled snapshot file shipped with the UI.
5.2 Correctness: snapshot→UI
We verify that the UI presents values that are deterministically
derived from the harmonised blocks delivered by the API.
Method.We instrumented a lightweight checker that, for a ran-
dom subset of DAOs, (a) reads the JSON snapshot used at import
time, (b) fetches the corresponding API payload forenhanced_metrics,
and (c) re-executes the exact client scoring functions used by
SustainabilityDashboard to compute per-KPI points and the
overall sum (code in Listing 1). We also verify per widget mappings
used byMetricsDashboard:
•Participation cards and charts:num_distinct_voters,
total_members,participation_rate.
•Treasury card and pie:treasury_value_usd,
circulating_supply,total_supply,
derivedcirculating_token_percentage.

---

## Page 7

Practical KPI-Based DAO Sustainability Analytics FinanSE ’26, April 2026, Rio De Janeiro, Brazil
• Governance pie: approved_proposals, total_proposals
(andapproval_rate).
• Token distribution:decentralisation.token_distribution,
largest_holder_percent,on_chain_automation.
Observations.Across DAOs in the snapshot, (i) API payloads
matched the stored JSON block structure (field names and numeric
types) and (ii) recomputing scores with the client functions repro-
duced the numbers rendered in the table (including fractional bins
forAccumulated FundsandDecentralisation). The guard rails in the
client (for example, low participation if the computed rate > 100%,
conservative scoring when total_proposals<3) produced stable
and predictable behaviour on edge cases.
5.3 Responsiveness
Client-side scoring.Sorting, filtering, and banding are executed
entirely in the browser (useMemo over a single list response), which
keeps interactions fluid and minimises server load for exploratory
analysis. The API read path returns compact JSON blocks with min-
imal server-side shaping. When the list is paginated, server load
scales with page size; the dashboard avoids N+1 patterns by comput-
ing all KPI bins client-side. This architecture prioritises auditability
and client-side verifiability over server-side optimisation.
5.4 Practitioner Utility
To assess whether DAO Portal supports routine governance analyt-
ics, we exercised the dashboard with representative tasks identified
from practitioner workflows. A formal usability study with external
participants is left to future work. Some of the dashboard’s typical
tasks for analysts could include:
T1: Screen DAOs by sustainability.TheSustainabilityDashboard
table sorts by overall score or a single KPI, with colour-coded bins
and an inline “Research Methodology” panel that restates thresh-
olds.
T2: Diagnose score drivers.Selecting a DAO, theMetricsDashboard
reveals the raw indicators (for example, approved versus total pro-
posals, average voting window, largest holder share). Because the
client computes scores from these values, the rationale for a high,
medium, or low band is visible without leaving the page.
T3: Compare and export.Single DAO views provide pie and bar
charts (Recharts) and summary tiles; these can be exported (SVG
or PNG) from the browser for reporting.5
5.5 Evaluation Scope
This is a system evaluation: we do not claim new empirical findings
about DAOs here, and we avoid synthetic throughput numbers that
would depend on deployment choices (container resources, net-
work conditions, database tuning). We also do not include a formal
security audit, as the system is designed for read-only analytics
over public blockchain data rather than for handling private creden-
tials or executing transactions. Instead, we show that (i) values on
screen are traceable to stored blocks, (ii) UI interactivity is achieved
by shifting scoring logic to the client, and (iii) the ingestion-and-
serving split keeps the web stack simple and auditable. Section 7
discusses additional limitations.
5CSV or Parquet export is left to API consumers; see Future Work.
6 Discussion
DAO Portal operationalises a compact KPI framework for DAO
sustainability into a web application. Two design choices are central.
Transparent and explainable scoring.The dashboard renders raw
governance indicators (e.g., participation rate, approval rate, largest
holder share) and applies fixed, documented thresholds to compute
per-KPI scores and an overall 0–12 composite. This makes the
system explainable: analysts can see why a DAO falls into a given
band and verify the mapping directly, without bespoke scripts.
For regulators and compliance teams assessing DAOs as financial
entities, such transparency is a prerequisite for accepting automated
governance analytics.
Separation of concerns.Crawling, ABI decoding, and cross-chain
harmonisation remain upstream in a dedicated extractor, while
DAO Portal focuses on ingestion, validation, storage, and presenta-
tion. This separation supports auditability and reproducibility: the
server exposes exactly what was ingested, and the client computes
exactly what it displays. The design mirrors established financial
software engineering practice, where clear boundaries between
extraction, storage, and presentation layers are essential for opera-
tional reliability.
Implications and trade-offs for practice.For protocol teams and
investors, the platform supports rapid triage (High, Medium, Low
by composite score), targeted diagnosis of weak governance di-
mensions, and evidence-based discussion of design choices such
as quorum thresholds or voting windows. For risk and compliance
teams, storing harmonised snapshots with timestamps enables re-
peatable reviews and independent recomputation. These benefits
come with trade-offs: equal weighting across KPIs simplifies inter-
pretation but may not suit all contexts, client-side scoring requires
careful policy documentation to avoid drift, and the focus on on-
chain data limits coverage of off-chain deliberation. These trade-offs
point to future research on configurable scoring policies, integra-
tion of heterogeneous governance artefacts, and validation against
financial risk models.
Interpretation scope.The composite score is intended for initial
screening rather than definitive assessment. Aggregation can mask
important trade-offs, for example when strong financial reserves
coexist with weak decentralisation. Practitioners should therefore
use the composite for triage and rely on per-KPI breakdowns and
raw indicators for interpretation. The relationship between sustain-
ability scores and concrete outcomes such as governance failures
or treasury losses remains unvalidated and is an open research
question (see Section 7).
Relevance to financial software engineering.DAO treasuries and
governance outcomes involve substantial financial resources. By ap-
plying established software engineering practices including schema
harmonisation, provenance tracking, deterministic computation,
and verifiable client-side scoring, DAO Portal demonstrates how
governance traces can be transformed into reproducible indicators
suitable for risk assessment, regulatory review, and investment
analysis. This positions the system within blockchain governance
research while illustrating how financial applications can benefit
from auditable and reproducible analytics infrastructure.

---

## Page 8

FinanSE ’26, April 2026, Rio De Janeiro, Brazil Meneguzzo et al.
7 Threats to Validity and Limitations
Extractor maturity and data quality.The external extractor is
under active development. Partial coverage, ABI mismatches, and
evolving normalisation rules can introduce inconsistencies in pro-
posal counts, voting windows, or token supply figures, which prop-
agate to KPI calculations. To limit inflated scores, the client applies
conservative guards (e.g., defaultingVoting Efficiencyto 1 point
when total_proposals<3).Mitigation:We plan to expose data-
quality flags in the API so that known extraction gaps are explicitly
surfaced in the UI.
On-chain scope and identity assumptions.DAO Portal derives
KPIs exclusively from on-chain evidence. Off-chain deliberation,
identity, and social context are not captured, and delegation struc-
tures are only partially represented. As a result, participation and
decentralisation may be under- or over-estimated, for example
when low direct turnout coexists with active delegation, or when
proposer concentration reflects delegate responsibility rather than
oligarchy. Metrics also rely on address-level uniqueness and do
not include Sybil detection, making them vulnerable to address
splitting.Mitigation:Future work may integrate delegation graphs,
identity attestations, or anomaly detection to improve robustness.
Snapshot-based evaluation.Results are computed on a time-bounded
snapshot. Although the platform supports multiple runs, longitudi-
nal dynamics such as token unlocks or governance reforms are not
analysed here, and the UI prioritises current values for clarity.
Fixed scoring policy.KPI thresholds are fixed in the client and
derived from prior empirical analysis [7]. While interpretable, they
are not universal, and alternative weights or bins may be preferable
in domain-specific settings. The current API does not expose scoring
policy versions.Mitigation:Planned extensions include configurable
thresholds and weighting schemes.
Governance heterogeneity.DAOs differ substantially in gover-
nance design, including execution models, quorum rules, and au-
tomation mechanisms. Applying uniform KPIs across heteroge-
neous designs may misrepresent context-specific controls, for ex-
ample when multisig-based execution scores lower on automation.
Mitigation:DAO-type classification and type-specific scoring ad-
justments are potential extensions.
Platform scope and performance.The system is tailored to Ethereum
and major EVM networks; non-EVM ecosystems would require new
extractors and possibly revised KPIs. Performance characteristics
depend on deployment choices, and we do not report quantitative
throughput or latency benchmarks.
Interpretation limits.Anomaly guards prevent UI failures but do
not correct erroneous upstream data, resulting in conservative yet
potentially inaccurate scores. Moreover, the relationship between
sustainability scores and real governance failures or financial losses
is not empirically validated. Establishing such links requires longi-
tudinal outcome studies beyond the scope of this work.
8 Conclusion and Future Work
We presented DAO Portal, a platform that transforms harmonised,
governance-aware on-chain data into transparent sustainability
KPIs and an interpretable 0–12 composite score. The system sepa-
rates extraction from serving, stores audit-ready JSON snapshots,
and renders explainable single- and multi-DAO views. By applying
fixed and visible thresholds, DAO Portal enables analysts and prac-
titioners to triage DAOs and diagnose governance drivers without
bespoke analytics pipelines. Future work will focus on extending
chain coverage, integrating off-chain governance and lightweight
identity signals, supporting configurable scoring policies, enriching
longitudinal analysis, and improving robustness through anomaly
detection, Sybil-resistance signals, and DAO-type classifications.
Longitudinal studies are also needed to assess whether sustainabil-
ity scores correlate with governance failures or treasury losses. All
source code, data schemas, and the dashboard implementation are
publicly available to support reproducibility and adoption.6 More
broadly, the work demonstrates how established software engineer-
ing practices such as schema harmonisation, provenance tracking,
and deterministic scoring can turn DAO governance traces into
reproducible indicators suitable for risk assessment, compliance
review, and investment analysis in financial and FinTech contexts.
References
[1] Javier Arroyo, David Davó, Elena Martínez-Vicente, Youssef Faqir-Rhazoui, and
Samer Hassan. 2022. DAO-Analyzer: Exploring Activity and Participation in
Blockchain Organizations, In Companion Publication of the 2022 Conference on
Computer Supported Cooperative Work and Social Computing (Virtual Event,
Taiwan).Companion Publication of the 2022 Conference on Computer Supported
Cooperative Work and Social Computing, 193–196. doi:10.1145/3500868.3559707
[2] Youssef El Faqir, J. Arroyo, and Samer Hassan. 2020. An overview of decentralized
autonomous organizations on the blockchain. doi:10.1145/3412569.3412579
[3] Rainer Feichtinger, Robin Fritsch, Y. Vonlanthen, and R. Wattenhofer. 2023. The
Hidden Shortcomings of (D)AOs - An Empirical Study of On-Chain Governance.
ArXivabs/2302.12125 (2023). doi:10.48550/arXiv.2302.12125
[4] Junjie Ma, Muhui Jiang, Jinan Jiang, Xiapu Luo, Yufeng Hu, Yajin Zhou, Qi Wang,
and Fengwei Zhang. 2024. Demystifying the DAO Governance Process.ArXiv
abs/2403.11758 (2024). doi:10.48550/arXiv.2403.11758
[5] Silvio Meneguzzo, Alfredo Favenza, Claudio Schifanella, Alessandro Mozzato,
and Stefano Leto. 2025. Design and Evaluation of a Sub-8 Second Decentralised
Marketplace for Energy Data. In2025 IEEE 49th Annual Computers, Software, and
Applications Conference (COMPSAC). 1722–1727. doi:10.1109/COMPSAC65507.
2025.00233
[6] Silvio Meneguzzo and Rachele Pierri. 2025. A Game-Theoretic Incentive Model for
DAO Governance. In2025 IEEE 49th Annual Computers, Software, and Applications
Conference (COMPSAC). 1714–1721. doi:10.1109/COMPSAC65507.2025.00232
[7] Silvio Meneguzzo, Claudio Schifanella, Valentina Gatteschi, and Giuseppe Deste-
fanis. 2025. Evaluating DAO Sustainability and Longevity Through On-Chain
Governance Metrics.ArXivabs/2504.11341 (2025). doi:10.48550/arXiv.2504.11341
[8] Johnnatan Messias, Vabuk Pahari, B. Chandrasekaran, K. Gummadi, and P.
Loiseau. 2023. Understanding Blockchain Governance: Analyzing Decentral-
ized Voting to Amend DeFi Smart Contracts.ArXivabs/2305.17655 (2023).
doi:10.48550/arXiv.2305.17655
[9] Andrea Peña-Calvin, Javier Arroyo, Andrew Schwartz, and Samer Hassan. 2024.
Concentration of Power and Participation in Online Governance: the Ecosystem
of Decentralized Autonomous Organizations.Companion Proceedings of the ACM
Web Conference 2024. doi:10.1145/3589335.3651481
[10] Tanusree Sharma, Yujin Kwon, Kornrapat Pongmala, Henry Wang, Andrew Miller,
D. Song, and Yang Wang. 2023. Unpacking How Decentralized Autonomous
Organizations (DAOs) Work in Practice.2024 IEEE International Conference on
Blockchain and Cryptocurrency (ICBC)(2023), 416–424. doi:10.1109/ICBC59979.
2024.10634404
[11] Joshua Z. Tan, Tara Merk, Sarah Hubbard, Eliza R. Oak, Joni Pirovich, Ellie
Rennie, Rolf Hoefer, Michael Zargham, Jason Potts, Chris Berg, R. Youngblom,
Primavera De Filippi, Seth Frey, Jeff Strnad, M. Mannan, Kelsie Nabben, S. Elrifai,
Jake Hartnell, Benjamin Mako Hill, Alexia Maddox, Woojin Lim, Tobin South,
Ari Juels, and D. Boneh. 2023. Open Problems in DAOs.ArXivabs/2310.19201
(2023). doi:10.48550/arXiv.2310.19201
6Repository: https://github.com/smeneguz/dao-portal

---
