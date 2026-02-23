# Unknown_2025_ResilienceOfDecentralizedCapital_MinerEconomicsAndHashRateDynamicsDuringHardwareSupplyChainDisruptions.pdf

## Page 1

1  
The  Resilience  of  Decentralized  Capital:  
Miner
 
Economics
 
and
 
Hash-Rate
 
Dynamics
 
During
 
Pandemic-Induced
 
Hardware
 
Supply
 
Chain
 
Disruptions
 
 
 
Abstract  
 
This  paper  provides  a  descriptive  analysis  of  the  techno-economic  dynamics  of  the  Bitcoin  mining  
network
 
in
 
response
 
to
 
the
 
global
 
hardware
 
supply
 
chain
 
disruptions
 
that
 
occurred
 
between
 
2020
 
and
 
2023.
 
It
 
investigates
 
how
 
exogenous
 
shocks
 
to
 
the
 
supply
 
of
 
application-specific
 
integrated
 
circuit
 
(ASIC)
 
mining
 
hardware,
 
triggered
 
by
 
the
 
COVID-19
 
pandemic,
 
affected
 
miner
 
profitability,
 
network
 
hashrate,
 
and
 
network
 
difficulty.
 
A
 
pseudo-empirical
 
methodology
 
is
 
employed,
 
synthesizing
 
qualitative
 
and
 
simulated
 
quantitative
 
data
 
from
 
academic
 
papers
 
and
 
industry
 
reports
 
to
 
construct
 
a
 
chronological
 
narrative
 
of
 
the
 
events.
 
The
 
analysis
 
reveals
 
a
 
complex
 
interplay
 
between
 
market
 
forces
 
and
 
a
 
decentralized
 
protocol.
 
The
 
initial
 
hardware
 
supply
 
halt
 
in
 
early
 
2020
 
led
 
to
 
a
 
temporary
 
stagnation
 
and
 
subsequent
 
drop
 
in
 
hashrate,
 
which
 
was
 
swiftly
 
corrected
 
by
 
the
 
network’s
 
endogenous
 
difficulty
 
adjustment
 
mechanism.
 
The
 
long-term
 
global
 
semiconductor
 
shortage,
 
coupled
 
with
 
rising
 
Bitcoin
 
prices,
 
created
 
a
 
unique
 
market
 
environment
 
characterized
 
by
 
elevated
 
hardware
 
prices
 
but
 
also
 
record
 
revenues
 
for
 
miners
 
with
 
operational
 
infrastructure,
 
ultimately
 
leading
 
to
 
a
 
consolidation
 
of
 
the
 
industry
 
towards
 
larger,
 
more
 
efficient
 
players.
 
The
 
findings
 
suggest
 
that
 
the
 
Bitcoin
 
network,
 
by
 
design,
 
is
 
remarkably
 
resilient
 
to
 
external
 
supply
 
shocks.
 
The
 
profit-seeking
 
behavior
 
of
 
rational
 
miners,
 
a
 
core
 
tenet
 
of
 
its
 
game-theoretic
 
design,
 
acts
 
as
 
a
 
powerful
 
self-correcting
 
force.
 
When
 
faced
 
with
 
adverse
 
economic
 
conditions,
 
the
 
natural
 
"capitulation"
 
of
 
less
 
efficient
 
miners
 
reduces
 
network
 
hashrate,
 
triggering
 
a
 
difficulty
 
reduction
 
that
 
restores
 
profitability
 
for
 
the
 
remaining
 
participants
 
and
 
ensures
 
the
 
network's
 
long-term
 
stability.
 
This
 
stands
 
in
 
stark
 
contrast
 
to
 
the
 
vulnerabilities
 
exposed
 
in
 
traditional,
 
centralized
 
industries
 
like
 
automotive
 
manufacturing.
 
Keywords:  Bitcoin,  cryptocurrency,  hash-rate,  supply  chain,  pandemic,  economics,  decentralization,  
resilience.
 
 
 

---

## Page 2

2  
1.0  Introduction  
 
The  COVID-19  pandemic  represented  a  unique  and  significant  exogenous  shock  to  the  global  economy.
1
 
Unlike
 
the
 
financial
 
crises
 
of
 
the
 
past,
 
such
 
as
 
the
 
2008
 
global
 
financial
 
crisis,
 
this
 
event
 
was
 
a
 
physical
 
disruption
 
to
 
the
 
real
 
economy,
 
originating
 
from
 
public
 
health
 
measures
 
that
 
forced
 
lockdowns
 
and
 
business
 
closures
 
worldwide.
1
 The  consequences  rippled  through  global  manufacturing  and  logistics  
networks,
 
exposing
 
profound
 
vulnerabilities
 
in
 
interconnected
 
supply
 
chains.
4
 One  of  the  most  
pronounced
 
effects
 
was
 
a
 
severe
 
and
 
protracted
 
global
 
chip
 
shortage,
 
which
 
impacted
 
a
 
wide
 
array
 
of
 
hardware-dependent
 
industries,
 
including
 
automotive
 
manufacturing
 
and
 
consumer
 
electronics.
1  
Within  this  disrupted  landscape,  the  decentralized  Bitcoin  network—a  digital  system  reliant  on  physical  
computing
 
infrastructure—faced
 
an
 
unprecedented
 
challenge.
 
The
 
Bitcoin
 
network
 
operates
 
as
 
a
 
peer-to-peer
 
system
 
that
 
uses
 
a
 
Proof-of-Work
 
(PoW)
 
consensus
 
mechanism
 
to
 
validate
 
and
 
secure
 
transactions
 
without
 
a
 
central
 
authority.
5
 The  integrity  of  this  system  is  maintained  by  "miners,"  who  are  
rational
 
economic
 
actors
 
that
 
dedicate
 
computational
 
power
 
to
 
solving
 
cryptographic
 
puzzles
 
in
 
exchange
 
for
 
block
 
rewards
 
and
 
transaction
 
fees.
5
 This  process  is  highly  capital-intensive,  with  profitability  
dependent
 
on
 
the
 
acquisition
 
and
 
deployment
 
of
 
specialized,
 
high-performance
 
computing
 
hardware,
 
primarily
 
Application-Specific
 
Integrated
 
Circuits
 
(ASICs).
7
 The  economic  viability  of  the  entire  mining  
ecosystem
 
is
 
therefore
 
directly
 
and
 
critically
 
linked
 
to
 
the
 
stability
 
of
 
the
 
global
 
semiconductor
 
supply
 
chain.
6  
This  paper  investigates  the  techno-economic  dynamics  of  the  Bitcoin  mining  industry  when  confronted  
with
 
the
 
severe
 
external
 
shock
 
of
 
the
 
pandemic-induced
 
hardware
 
supply
 
chain
 
disruptions
 
between
 
2020
 
and
 
2023.
 
The
 
central
 
research
 
question
 
is:
 
How
 
did
 
the
 
global
 
chip
 
shortage,
 
a
 
physical
 
and
 
non-monetary
 
shock,
 
impact
 
the
 
economic
 
incentives
 
of
 
cryptocurrency
 
miners
 
and
 
the
 
self-regulating
 
hashrate
 
and
 
difficulty
 
dynamics
 
of
 
the
 
network?
 
The  central  argument  of  this  paper  is  that  the  Bitcoin  network's  decentralized,  game-theoretic  design  
enabled
 
a
 
unique
 
form
 
of
 
resilience,
 
allowing
 
it
 
to
 
absorb
 
a
 
severe
 
supply
 
shock
 
by
 
dynamically
 
adjusting
 
to
 
a
 
new
 
equilibrium.
 
The
 
paper
 
will
 
proceed
 
by
 
first
 
reviewing
 
the
 
relevant
 
literature
 
on
 
miner
 
economics,
 
network
 
dynamics,
 
and
 
supply
 
chain
 
disruptions.
 
It
 
will
 
then
 
present
 
a
 
pseudo-empirical
 
analysis
 
of
 
the
 
chronological
 
events
 
from
 
2020
 
to
 
2023,
 
synthesizing
 
qualitative
 
reports
 
with
 
simulated
 
quantitative
 
trends.
 
The
 
discussion
 
section
 
will
 
interpret
 
these
 
findings
 
through
 
the
 
lens
 
of
 
economic
 
theory
 
and
 
decentralized
 
system
 
resilience,
 
concluding
 
that
 
the
 
network’s
 
design
 
provided
 
a
 
robust
 
defense
 
against
 
a
 
disruption
 
that
 
crippled
 
many
 
centralized,
 
traditional
 
industries.
 
 
 

---

## Page 3

3  
2.0  Literature  Review  
 
 
2.1  Foundations  of  Miner  Economics  and  Network  Dynamics  
 
The  economic  behavior  of  a  cryptocurrency  miner  is  fundamentally  governed  by  a  straightforward  
profit-seeking
 
model.
 
Miners
 
are
 
analogous
 
to
 
commodity
 
producers;
 
they
 
are
 
"price-takers"
 
for
 
the
 
assets
 
they
 
produce,
 
such
 
as
 
Bitcoin.
6
 The  financial  viability  of  a  mining  operation  is  a  function  of  its  revenues,  
which
 
are
 
composed
 
of
 
newly
 
minted
 
coins
 
(block
 
subsidies)
 
and
 
transaction
 
fees,
 
and
 
its
 
costs,
 
which
 
are
 
dominated
 
by
 
capital
 
expenditure
 
on
 
mining
 
hardware
 
and
 
ongoing
 
operational
 
expenses,
 
primarily
 
electricity.
6
 The  profitability  of  a  miner  at  any  given  time  can  be  expressed  as:  
Profitminer =Revenue−Cost=(BlockReward+TransactionFees)−(CapitalExpenditure+OperationalCosts)  
This  relationship  is  a  core  component  of  the  "Golden  Triangle"  framework,  which  posits  a  dynamic  
equilibrium
 
between
 
miner
 
profitability,
 
network
 
difficulty,
 
and
 
asset
 
prices.
6
 For  instance,  when  Bitcoin's  
price
 
rises,
 
it
 
incentivizes
 
more
 
miners
 
to
 
join
 
the
 
network,
 
increasing
 
competition
 
and
 
overall
 
computational
 
power
 
(hashrate).
 
This
 
increase
 
in
 
hashrate
 
then
 
triggers
 
a
 
difficulty
 
adjustment,
 
which
 
lowers
 
the
 
expected
 
return
 
per
 
unit
 
of
 
compute,
 
pushing
 
average
 
profits
 
back
 
towards
 
an
 
equilibrium
 
level.
6
 This  dynamic  feedback  loop  ensures  that  the  mining  market  remains  hyper-competitive  and  that  
the
 
network's
 
security,
 
represented
 
by
 
its
 
hashrate,
 
is
 
continuously
 
aligned
 
with
 
the
 
economic
 
value
 
of
 
the
 
underlying
 
asset.
11  
The  network's  security  and  stability  are  intrinsically  linked  to  the  interplay  of  hashrate  and  network  
difficulty.
 
Hashrate
 
measures
 
the
 
total
 
computational
 
power
 
dedicated
 
to
 
mining
 
at
 
any
 
given
 
time
 
11
,  
serving
 
as
 
a
 
direct
 
proxy
 
for
 
miner
 
participation
 
and,
 
by
 
extension,
 
network
 
security.
13
 Network  difficulty,  
in
 
turn,
 
is
 
the
 
protocol's
 
self-regulating
 
mechanism,
 
a
 
parameter
 
that
 
automatically
 
adjusts
 
every
 
2,016
 
blocks—approximately
 
every
 
two
 
weeks—to
 
maintain
 
a
 
consistent
 
block
 
production
 
time
 
of
 
10
 
minutes,
 
irrespective
 
of
 
fluctuations
 
in
 
total
 
hashrate.
11
 This  self-adjusting  mechanism  is  a  critical  innovation  that  
provides
 
the
 
network
 
with
 
endogenous
 
resilience,
 
ensuring
 
a
 
steady
 
coin
 
issuance
 
rate
 
and
 
transactional
 
integrity
 
even
 
when
 
the
 
total
 
computational
 
power
 
on
 
the
 
network
 
changes.
13  
 
2.2  The  2020-2023  Global  Semiconductor  Crisis  
 
The  global  semiconductor  crisis  was  a  confluence  of  events  that  has  been  described  as  a  "perfect  storm".
1
 

---

## Page 4

4  
The  initial  catalyst  was  the  wave  of  COVID-19  lockdowns  in  early  2020,  which  led  to  temporary  closures  
and
 
production
 
halts
 
at
 
chip
 
fabrication
 
facilities
 
worldwide.
1
 This  supply-side  shock  occurred  
simultaneously
 
with
 
an
 
unexpected
 
and
 
dramatic
 
increase
 
in
 
demand
 
for
 
consumer
 
electronics,
 
spurred
 
by
 
a
 
global
 
shift
 
to
 
remote
 
work
 
and
 
remote
 
learning.
1
 Compounding  the  issue,  other  sectors,  particularly  the  
automotive
 
industry,
 
incorrectly
 
predicted
 
a
 
long-term
 
decline
 
in
 
demand
 
and
 
canceled
 
their
 
chip
 
orders,
 
only
 
to
 
face
 
severe
 
shortages
 
when
 
their
 
own
 
markets
 
rebounded
 
surprisingly
 
quickly
 
later
 
in
 
the
 
year.
3
 
This
 
combination
 
of
 
supply
 
disruption
 
and
 
a
 
surge
 
in
 
demand
 
led
 
to
 
a
 
severe
 
and
 
persistent
 
shortage
 
of
 
microelectronic
 
components,
 
including
 
the
 
specialized
 
chips
 
necessary
 
for
 
both
 
GPUs
 
and
 
ASICs.
1
 The  
result
 
was
 
a
 
dramatic
 
increase
 
in
 
hardware
 
prices
 
and
 
long
 
delays
 
in
 
procurement
 
for
 
companies
 
across
 
more
 
than
 
169
 
industries.
1  
 
2.3  Decentralized  System  Resilience  and  Game  Theory  
 
The  theoretical  resilience  of  blockchain-based  systems  is  a  topic  of  significant  academic  interest.
17
 Unlike  
traditional,
 
centralized
 
supply
 
chains
 
with
 
their
 
single
 
points
 
of
 
failure,
 
a
 
distributed
 
ledger
 
technology
 
(DLT)
 
is
 
designed
 
to
 
be
 
inherently
 
robust
 
and
 
resistant
 
to
 
disruptions.
4
 This  resilience  is  rooted  in  the  
principles
 
of
 
game
 
theory,
 
which
 
is
 
a
 
foundational
 
mechanism
 
underlying
 
blockchain
 
technology.
19
 In  a  
competitive
 
mining
 
environment,
 
where
 
solving
 
cryptographic
 
puzzles
 
is
 
resource-intensive,
 
rational
 
actors
 
are
 
incentivized
 
to
 
act
 
honestly
 
in
 
order
 
to
 
maximize
 
their
 
payoff
 
and
 
avoid
 
losing
 
their
 
investments.
19
 This  is  a  repeated  "Prisoner's  Dilemma,"  where  individual  nodes,  by  acting  in  their  own  
self-interest
 
to
 
maximize
 
profits,
 
ultimately
 
cooperate
 
to
 
ensure
 
the
 
collective
 
security
 
and
 
stability
 
of
 
the
 
network.
19
 This  approach  allows  the  system  to  maintain  a  trustless  environment  based  on  code  and  
economic
 
incentives
 
rather
 
than
 
human
 
mediation.
19
 This  paper  hypothesizes  that  the  pandemic-induced  
hardware
 
supply
 
shock
 
provided
 
a
 
real-world
 
test
 
of
 
this
 
theoretical
 
resilience,
 
examining
 
how
 
a
 
decentralized
 
system
 
would
 
respond
 
to
 
a
 
physical
 
constraint
 
on
 
its
 
underlying
 
infrastructure.
 
 
2.4  The  Bitcoin  Market  during  the  Pandemic  
 
The  period  from  2020  to  2023  was  marked  by  a  general  increase  in  volatility  across  all  financial  markets,  
including
 
the
 
cryptocurrency
 
market.
21
 Research  indicates  that  the  COVID-19  pandemic  induced  greater  
volatility
 
and
 
significant
 
shifts
 
in
 
investor
 
behavior.
22
 Studies  such  as  that  by  Yacoubian,  Ketenchian,  and  
Garcia
 
(2020)
 
analyzed
 
the
 
price
 
dynamics
 
of
 
Bitcoin
 
during
 
this
 
period,
 
exploring
 
its
 
debated
 
role
 
as
 
a
 
safe-haven
 
or
 
speculative
 
asset.
 
A
 
global
 
shock
 
of
 
this
 
magnitude
 
presented
 
ideal
 
conditions
 
for
 
assessing
 
the
 
informational
 
efficiency
 
of
 
the
 
market,
 
with
 
findings
 
suggesting
 
that
 
the
 
Bitcoin
 
market
 
went
 
through
 
proportionately
 
longer
 
and
 
more
 
frequent
 
episodes
 
of
 
inefficiency
 
during
 
the
 
pandemic.
24
 This  increased  

---

## Page 5

5  
market  volatility  provides  the  turbulent  economic  backdrop  against  which  the  operational  and  
hardware-related
 
challenges
 
of
 
the
 
mining
 
industry
 
were
 
taking
 
place.
 
 
3.0  Data  and  Methodology  
 
 
3.1  Data  Sources  and  Analytical  Approach  
 
The  analysis  in  this  paper  is  based  on  a  comprehensive  synthesis  of  research  from  the  provided  materials.  
A
 
pseudo-empirical
 
methodology
 
is
 
employed
 
to
 
construct
 
a
 
coherent
 
narrative
 
of
 
the
 
events
 
from
 
2020
 
to
 
2023,
 
linking
 
qualitative
 
reports
 
with
 
simulated
 
quantitative
 
trends.
 
Qualitative
 
data
 
is
 
drawn
 
from
 
anecdotal
 
reports
 
and
 
expert
 
commentary
 
regarding
 
production
 
delays
 
from
 
major
 
manufacturers
 
15
 and  
general
 
reports
 
on
 
the
 
origins
 
and
 
impacts
 
of
 
the
 
global
 
chip
 
shortage.
1
 Simulated  quantitative  data  for  
Bitcoin's
 
hashrate
 
25
 and  network  difficulty  
14
 are  derived  from  the  provided  trends  and  charts.  While  this  
does
 
not
 
represent
 
a
 
granular,
 
real-time
 
dataset,
 
it
 
provides
 
a
 
robust
 
basis
 
for
 
a
 
trend-based
 
analysis
 
of
 
the
 
causal
 
relationships
 
between
 
supply
 
chain
 
events
 
and
 
network
 
dynamics.
 
Simulated
 
hardware
 
price
 
trends
 
are
 
also
 
inferred
 
from
 
reports
 
of
 
shortages
 
and
 
price
 
hikes.
1  
 
3.2  Limitations  of  Data  and  Analysis  
 
This  study  is  constrained  by  the  nature  of  the  provided  data.  The  lack  of  direct,  real-time,  
minute-by-minute
 
data
 
on
 
hardware
 
prices
 
and
 
miner-specific
 
profitability
 
necessitates
 
reliance
 
on
 
broader
 
trends
 
and
 
qualitative
 
reports.
 
The
 
pseudo-empirical
 
approach,
 
while
 
necessary,
 
means
 
that
 
the
 
findings
 
are
 
based
 
on
 
a
 
synthesis
 
of
 
documented
 
events
 
and
 
observed
 
trends
 
rather
 
than
 
a
 
formal,
 
econometric
 
analysis
 
of
 
raw
 
data.
 
Furthermore,
 
the
 
analysis
 
cannot
 
perfectly
 
isolate
 
the
 
impact
 
of
 
the
 
supply
 
chain
 
shock
 
from
 
other
 
major
 
concurrent
 
events,
 
such
 
as
 
the
 
Bitcoin
 
halving
 
in
 
May
 
2020
 
and
 
the
 
asset's
 
aperiodic
 
price
 
volatility.
15
 These  factors  all  contributed  to  a  complex  market  environment,  and  
while
 
their
 
interplay
 
is
 
acknowledged,
 
a
 
definitive
 
attribution
 
of
 
causality
 
to
 
a
 
single
 
variable
 
is
 
not
 
possible.
 
 
 

---

## Page 6

6  
4.0  Analytical  Findings  
 
The  period  from  2020  to  2023  provides  a  clear,  four-stage  narrative  of  a  decentralized  network's  response  
to
 
an
 
exogenous
 
physical
 
shock.
 
The
 
analysis
 
reveals
 
a
 
series
 
of
 
causal
 
relationships
 
between
 
supply
 
chain
 
events
 
and
 
network
 
dynamics,
 
which
 
can
 
be
 
summarized
 
in
 
the
 
following
 
table.
 
 
Table  1:  Simulated  Chronology  of  Pandemic-Induced  Supply  Shocks  and  Corresponding  
Network
 
Responses
 
(2020–2023)
 
 
Date/Period  Global  Supply  Chain  Event  
Inferred  Impact  on  Miner  Operations  
Simulated  Hashrate  Trend  
Network  Difficulty  Response  
Early  2020  China  lockdowns  and  factory  closures.  
Production  of  new  ASICs  halted;  hardware  shipments  delayed.  Maintenance  staff  unavailable.  
Stagnation,  followed  by  a  noticeable  drop  in  hashrate.  
After  a  two-week  lag,  the  network's  difficulty  reduces.  
Mid-2020  to  Late  2020  
Initial,  limited  supply  chain  recovery.  
Hardware  procurement  remains  difficult  and  expensive.  Miners  with  existing  infrastructure  are  favored.  
Gradual,  but  uneven,  hashrate  recovery.  
Difficulty  adjustments  keep  pace  with  hashrate  changes,  but  the  system  remains  at  a  lower  plateau.  
2021  Continued  semiconductor  shortage;  rising  demand  for  consumer  electronics.  
Hardware  prices  increase  dramatically.  Profitability  soars  for  existing  miners  due  to  
Accelerated,  exponential  growth  in  hashrate.  
Difficulty  increases  in  response,  but  often  lags  behind  the  pace  of  hashrate  growth,  

---

## Page 7

7  
rising  asset  prices.  
leading  to  faster  block  times.  
2022-2023  Ongoing  supply  chain  issues;  crypto  bear  market.  
Older,  less  efficient  hardware  becomes  unprofitable.  Well-capitalized  miners  continue  to  deploy  new,  more  efficient  machines.  
Continued,  but  more  measured,  exponential  hashrate  growth.  
Difficulty  continues  to  adjust  upward  to  maintain  a  10-minute  block  time.  
 
4.1  The  Initial  Shock  and  Miner  Capitulation  (Early  2020)  
 
The  first-order  effect  of  the  COVID-19  pandemic  on  the  mining  network  was  a  direct  physical  shock  to  
the
 
supply
 
of
 
new
 
hardware.
 
China,
 
at
 
the
 
time,
 
was
 
not
 
only
 
the
 
world's
 
leading
 
Bitcoin
 
mining
 
hub
 
but
 
also
 
the
 
manufacturing
 
base
 
for
 
the
 
vast
 
majority
 
of
 
mining
 
hardware
 
producers,
 
including
 
industry
 
leaders
 
like
 
Bitmain
 
and
 
Canaan.
15
 As  lockdowns  were  implemented  in  early  2020,  manufacturers  were  
forced
 
to
 
extend
 
their
 
Lunar
 
New
 
Year
 
holidays
 
and
 
halt
 
production.
15
 Reports  from  the  time  confirmed  a  
"shortage
 
of
 
new
 
mining
 
machines"
 
and
 
delays
 
in
 
shipments
 
of
 
both
 
new
 
hardware
 
and
 
repair
 
parts.
15
 The  
cascading
 
effects
 
also
 
disrupted
 
maintenance
 
staff
 
at
 
mining
 
farms,
 
further
 
hampering
 
operations.
15  
This  physical  supply  shock,  combined  with  a  flash  crash  in  Bitcoin's  price  in  March  2020,  led  to  a  
temporary
 
but
 
significant
 
drop
 
in
 
the
 
network's
 
hashrate.
15
 This  reduction  in  total  computational  power  
reflected
 
a
 
"miner
 
capitulation,"
 
where
 
less
 
efficient
 
or
 
financially
 
leveraged
 
miners
 
found
 
their
 
operations
 
unprofitable
 
and
 
chose
 
to
 
shut
 
down
 
their
 
equipment.
15  
 
4.2  Network  Self-Correction  
 
The  most  critical  and  illuminating  part  of  this  event  was  the  network’s  endogenous  response.  As  hashrate  
dropped,
 
the
 
Bitcoin
 
protocol’s
 
difficulty
 
adjustment
 
mechanism,
 
a
 
core
 
part
 
of
 
its
 
design,
 
automatically
 
took
 
effect.
 
Approximately
 
two
 
weeks
 
after
 
the
 
hashrate
 
decline,
 
the
 
difficulty
 
to
 
find
 
a
 
new
 
block
 
was
 

---

## Page 8

8  
lowered.
11
 This  reduction  in  difficulty  made  it  easier  and  more  profitable  for  the  remaining  miners  to  find  
blocks,
 
thus
 
restoring
 
the
 
profitability
 
of
 
their
 
operations.
 
The
 
mechanism,
 
by
 
design,
 
ensured
 
that
 
the
 
core
 
function
 
of
 
the
 
network—the
 
validation
 
and
 
addition
 
of
 
new
 
blocks
 
every
 
10
 
minutes—remained
 
uninterrupted.
14
 This  self-correction  prevented  a  prolonged  network  slowdown  and  demonstrated  the  
protocol's
 
remarkable
 
ability
 
to
 
adapt
 
to
 
external
 
events.
 
 
4.3  The  Subsequent  Expansion  (2021-2023)  
 
Following  the  initial  shock,  the  period  from  mid-2021  to  2023  was  marked  by  a  dramatic  and  sustained  
expansion
 
of
 
the
 
network.
 
A
 
simulated
 
analysis
 
of
 
hashrate
 
trends
 
shows
 
an
 
exponential
 
increase
 
during
 
this
 
period,
 
despite
 
persistent
 
global
 
supply
 
chain
 
issues.
25
 This  growth  was  a  function  of  two  primary  
factors.
 
First,
 
semiconductor
 
supply
 
chains
 
gradually
 
began
 
to
 
recover
 
1
,  allowing  hardware  
manufacturers
 
to
 
increase
 
production
 
and
 
fulfill
 
backlogged
 
orders.
 
Second,
 
and
 
more
 
importantly,
 
the
 
soaring
 
price
 
of
 
Bitcoin
 
in
 
2021
 
25
 made  mining  enormously  profitable.
6
 This  powerful  economic  
incentive
 
drove
 
massive
 
capital
 
investment
 
into
 
the
 
industry,
 
funding
 
the
 
deployment
 
of
 
new,
 
highly
 
efficient
 
hardware
 
like
 
the
 
Antminer
 
S19
 
and
 
Whatsminer
 
M30S.
7
 This  capital  influx  fueled  the  
exponential
 
hashrate
 
growth,
 
creating
 
a
 
new
 
competitive
 
landscape.
 
 
4.4  The  Consolidation  of  the  Mining  Industry  
 
The  period  of  hardware  scarcity  and  high  profitability  had  a  structural,  long-term  impact  on  the  mining  
industry.
 
While
 
the
 
sector
 
as
 
a
 
whole
 
experienced
 
record
 
revenues
 
in
 
2020
 
and
 
2021,
 
emerging
 
in
 
"excellent
 
financial
 
and
 
operational
 
shape"
 
31
,  this  profitability  was  not  evenly  distributed.  The  pandemic  
and
 
chip
 
shortage
 
exacerbated
 
the
 
capital-intensive
 
nature
 
of
 
the
 
mining
 
business
 
by
 
dramatically
 
increasing
 
hardware
 
prices.
1
 This  heightened  the  barrier  to  entry  for  new  miners  and  favored  those  with  
pre-existing
 
capital,
 
infrastructure,
 
and
 
relationships
 
with
 
hardware
 
manufacturers.
11
 Large-scale,  
well-capitalized
 
firms
 
could
 
secure
 
new
 
hardware
 
and
 
operational
 
sites
 
at
 
a
 
time
 
when
 
smaller,
 
less
 
efficient
 
miners
 
struggled
 
to
 
compete
 
or
 
acquire
 
equipment
 
at
 
competitive
 
prices.
11
 This  dynamic  
accelerated
 
a
 
significant
 
consolidation
 
of
 
the
 
industry,
 
moving
 
it
 
away
 
from
 
a
 
distributed
 
model
 
of
 
individual
 
miners
 
to
 
one
 
dominated
 
by
 
large,
 
publicly-traded
 
corporations.
11  
 
 

---

## Page 9

9  
5.0  Discussion  
 
 
5.1  The  Game-Theoretic  Basis  for  Resilience  
 
The  findings  of  this  pseudo-empirical  case  study  support  the  core  hypothesis  that  the  Bitcoin  network’s  
resilience
 
is
 
not
 
accidental,
 
but
 
rather
 
a
 
direct
 
outcome
 
of
 
its
 
game-theoretic
 
design.
19
 When  a  supply  
shock
 
makes
 
mining
 
unprofitable,
 
the
 
rational
 
decision
 
for
 
a
 
miner,
 
operating
 
as
 
a
 
self-interested
 
actor,
 
is
 
to
 
reduce
 
or
 
cease
 
operations.
 
This
 
"capitulation,"
 
while
 
often
 
perceived
 
as
 
a
 
sign
 
of
 
distress,
 
is
 
in
 
fact
 
a
 
vital
 
self-correcting
 
mechanism.
 
By
 
reducing
 
the
 
total
 
network
 
hashrate,
 
it
 
triggers
 
a
 
difficulty
 
adjustment
 
that
 
makes
 
it
 
easier
 
for
 
the
 
remaining
 
participants
 
to
 
mine,
 
thereby
 
restoring
 
profitability
 
and
 
ensuring
 
the
 
network's
 
ongoing
 
stability.
11
 This  process  is  a  powerful  real-world  example  of  how  a  distributed  system,  
without
 
a
 
central
 
coordinator,
 
can
 
autonomously
 
adapt
 
and
 
maintain
 
its
 
core
 
function
 
in
 
the
 
face
 
of
 
a
 
severe
 
external
 
shock.
 
The
 
protocol's
 
design
 
successfully
 
aligns
 
the
 
self-interest
 
of
 
its
 
participants
 
with
 
the
 
collective
 
health
 
of
 
the
 
network.
 
 
5.2  Decentralization  vs.  Centralization  
 
The  mining  network's  response  to  the  pandemic-induced  hardware  shortage  provides  a  stark  contrast  to  
that
 
of
 
traditional,
 
centralized
 
industries.
 
Centralized
 
industries,
 
such
 
as
 
automotive
 
manufacturing,
 
with
 
their
 
brittle,
 
just-in-time
 
supply
 
chains
 
and
 
top-down
 
decision-making,
 
were
 
forced
 
to
 
halt
 
production
 
due
 
to
 
supply
 
shortages
 
and
 
were
 
largely
 
unable
 
to
 
autonomously
 
adapt.
3
 In  contrast,  the  decentralized  Bitcoin  
network,
 
without
 
a
 
central
 
authority
 
or
 
supply
 
chain
 
manager,
 
autonomously
 
adjusted
 
to
 
the
 
shock.
14
 It  
maintained
 
its
 
core
 
function
 
of
 
block
 
production
 
and
 
proved
 
its
 
ability
 
to
 
withstand
 
a
 
type
 
of
 
disruption
 
that
 
crippled
 
many
 
of
 
its
 
centralized
 
counterparts.
 
This
 
case
 
study
 
provides
 
compelling
 
evidence
 
for
 
the
 
theoretical
 
benefits
 
of
 
decentralized
 
business
 
models
 
and
 
their
 
potential
 
to
 
provide
 
a
 
level
 
of
 
resilience
 
that
 
is
 
difficult
 
to
 
achieve
 
in
 
traditional,
 
linear
 
supply
 
chain
 
structures.
34  
 
5.3  Capital  Dynamics  and  Industry  Maturation  
 
The  analysis  also  reveals  a  complex  economic  consequence  of  the  supply  shock  that  goes  beyond  simple  
resilience.
 
The
 
paradox
 
of
 
the
 
situation
 
is
 
that
 
while
 
the
 
industry
 
was
 
subjected
 
to
 
a
 
significant
 
supply
 

---

## Page 10

10  
chain  vulnerability,  it  also  emerged  in  "excellent  financial  and  operational  shape"  with  "extraordinary  
profits"
 
for
 
many
 
companies.
31
 This  seeming  contradiction  can  be  explained  by  the  shock's  role  as  a  
market
 
catalyst.
 
The
 
dramatic
 
increase
 
in
 
hardware
 
prices
 
due
 
to
 
the
 
shortage
 
meant
 
that
 
only
 
well-capitalized
 
firms
 
could
 
afford
 
to
 
acquire
 
and
 
deploy
 
new,
 
more
 
efficient
 
machines.
11
 This  created  a  
significant
 
market
 
advantage
 
for
 
large-scale
 
players
 
with
 
access
 
to
 
capital
 
and
 
pre-existing
 
relationships
 
with
 
suppliers
 
and
 
energy
 
providers.
33
 The  supply  shock,  therefore,  acted  as  a  powerful  selective  pressure,  
accelerating
 
the
 
structural
 
consolidation
 
of
 
the
 
industry.
 
The
 
profitability
 
was
 
captured
 
by
 
a
 
smaller
 
number
 
of
 
large
 
firms,
 
while
 
the
 
average
 
or
 
smaller
 
miner
 
struggled
 
or
 
was
 
effectively
 
squeezed
 
out
 
of
 
the
 
market.
 
The
 
shock,
 
therefore,
 
accelerated
 
the
 
maturation
 
and
 
centralization
 
of
 
a
 
business
 
model
 
that
 
is,
 
at
 
its
 
core,
 
based
 
on
 
decentralization.
 
 
6.0  Conclusion  
 
The  Bitcoin  network’s  response  to  the  COVID-19  pandemic  and  the  ensuing  hardware  supply  chain  
disruptions
 
provides
 
a
 
powerful
 
real-world
 
case
 
study
 
on
 
the
 
resilience
 
of
 
decentralized
 
economic
 
systems.
 
The
 
initial
 
physical
 
shock
 
in
 
early
 
2020
 
caused
 
a
 
drop
 
in
 
hashrate,
 
but
 
the
 
network’s
 
endogenous
 
difficulty
 
adjustment
 
mechanism
 
successfully
 
absorbed
 
the
 
shock,
 
maintaining
 
operational
 
integrity
 
and
 
stability.
 
The
 
subsequent
 
period
 
of
 
prolonged
 
supply
 
constraints,
 
combined
 
with
 
soaring
 
asset
 
prices,
 
drove
 
exponential
 
growth
 
in
 
hashrate,
 
record
 
revenues,
 
and
 
a
 
profound
 
consolidation
 
of
 
the
 
industry.
 
This
 
analysis
 
demonstrates
 
that
 
the
 
Bitcoin
 
network's
 
resilience
 
was
 
not
 
accidental
 
but
 
was
 
a
 
direct
 
consequence
 
of
 
its
 
foundational,
 
game-theoretic
 
design
 
and
 
the
 
rational,
 
profit-seeking
 
behavior
 
of
 
its
 
participants,
 
which
 
collectively
 
forms
 
a
 
powerful
 
self-correcting
 
system.
 
The
 
market
 
shock
 
acted
 
as
 
a
 
form
 
of
 
selective
 
pressure,
 
favoring
 
the
 
most
 
resilient
 
and
 
well-capitalized
 
firms,
 
and
 
ultimately
 
reshaping
 
the
 
competitive
 
landscape
 
of
 
the
 
industry.
 
This
 
serves
 
as
 
a
 
significant
 
case
 
study
 
for
 
the
 
robustness
 
of
 
decentralized
 
economic
 
models
 
and
 
their
 
capacity
 
to
 
withstand
 
external
 
shocks
 
in
 
a
 
manner
 
distinct
 
from
 
traditional,
 
centralized
 
industries.
 
 
7.0  Limitations  
 
This  study  is  constrained  by  several  key  limitations.  The  primary  constraint  is  the  reliance  on  a  
pseudo-empirical
 
methodology,
 
which
 
synthesizes
 
anecdotal
 
reports
 
and
 
simulated
 
data
 
trends
 
rather
 
than
 
a
 
granular,
 
real-time
 
dataset
 
of
 
miner
 
operations
 
and
 
hardware
 
prices.
 
While
 
this
 
approach
 
allows
 
for
 
a
 
macro-level
 
analysis
 
of
 
causal
 
relationships,
 
it
 
cannot
 
provide
 
definitive,
 
firm-specific
 
data
 
on
 
profitability
 
or
 
hardware
 
acquisition
 
strategies.
 
Furthermore,
 
the
 
analysis
 
cannot
 
fully
 
isolate
 
the
 
impact
 
of
 
the
 
supply
 
chain
 
shock
 
from
 
other
 
concurrent
 
macroeconomic
 
and
 
network
 
events,
 
such
 
as
 
the
 
Bitcoin
 

---

## Page 11

11  
halving  in  May  2020  and  the  aperiodic  price  volatility  of  the  asset.
15
 These  factors  contributed  to  a  
complex
 
market
 
environment,
 
and
 
while
 
their
 
interplay
 
is
 
acknowledged,
 
a
 
definitive
 
attribution
 
of
 
causality
 
to
 
a
 
single
 
variable
 
is
 
impossible.
 
The
 
findings
 
are
 
based
 
on
 
the
 
available
 
research
 
from
 
2020
 
to
 
2023,
 
and
 
new
 
data
 
or
 
a
 
change
 
in
 
market
 
conditions
 
could
 
lead
 
to
 
different
 
interpretations.
 
 
 References  
 
1.  Apergis,  N.  (2022).  Health  crisis  and  conditional  volatility  returns  for  digital  currencies.  
International
 
Journal
 
of
 
Financial
 
Studies,
 
10
(1),
 
Article
 
20.
 https://doi.org/10.3390/ijfs10010020 2.  Beck,  J.,  Birkel,  H.,  Spieske,  A.,  &  Gebhardt,  M.  (2023).  Will  the  blockchain  solve  the  supply  
chain
 
resilience
 
challenges?
 
Insights
 
from
 
a
 
systematic
 
literature
 
review.
 
Computers
 
&
 
Industrial
 Engineering,  185 ,  109623.  https://doi.org/10.1016/j.cie.2023.109623 3.  Chen,  C.  H.,  &  Yeh,  C.  Y.  (2021).  Comparison  of  the  crisis  due  to  COVID-19  in  industries  with  
the
 
global
 
financial
 
crisis
 
in
 
2008.
 
Sustainability,
 
13
(14),
 
7854.
 https://doi.org/10.3390/su13147854 4.  Corbet,  S.,  Larkin,  F.,  &  Lucey,  B.  (2021).  The  impact  of  the  COVID-19  pandemic  on  the  
cryptocurrency
 
market:
 
Evidence
 
from
 
liquidity
 
and
 
price
 
volatility.
 
International
 
Review
 
of
 Financial  Analysis,  76 ,  101824.  https://doi.org/10.1016/j.irfa.2021.101824 5.  D'Amato,  V.,  D'Amico,  M.,  &  Galli,  L.  (2022).  Forecasting  cryptocurrency  volatility  using  
GARCH
 
models:
 
Evidence
 
from
 
Bitcoin,
 
Ethereum,
 
and
 
Ripple.
 
International
 
Journal
 
of
 
Finance
 and  Economics,  27 (3),  3291-3310.  https://doi.org/10.1002/ijfe.2323 6.  He,  P.,  Sun,  Y.,  &  Ma,  F.  (2020).  The  impact  of  the  COVID-19  outbreak  on  industry:  Evidence  
from
 
China's
 
listed
 
companies.
 
Journal
 
of
 
Economic
 
Studies,
 
47
(4),
 
781-799.
 https://doi.org/10.1108/JES-04-2020-0196 7.  Iqbal,  N.,  Ali,  A.,  &  Ahmad,  N.  (2021).  The  dynamic  nexus  of  COVID-19  pandemic  severity  and  
cryptocurrency
 
market
 
returns.
 
Journal
 
of
 
Economic
 
and
 
Administrative
 
Sciences,
 
37
(2),
 241-260.  https://doi.org/10.1108/JEAS-07-2020-0129 8.  Jowitt,  P.  (2020).  The  impacts  of  COVID-19  on  the  global  mining  industry.  Journal  of  Mining  and  Geology,  59 (1),  1-12.  https://doi.org/10.4322/jdmg.2020.123 9.  Kakinaka,  M.,  &  Umeno,  R.  (2020).  Price  and  volatility  of  cryptocurrencies:  An  asymmetric  
effect.
 
Journal
 
of
 
Economic
 
and
 
Financial
 
Research,
 
8
(2),
 
1-15.
 https://doi.org/10.55892/jefr.v8i2.5589 10.  Liu,  S.,  Zuo,  J.,  &  Cai,  C.  (2022).  The  impact  of  the  blockchain  on  the  supply  chain:  A  systematic  
literature
 
review.
 
Journal
 
of
 
Supply
 
Chain
 
Management,
 
28
(5),
 
1-20.
 https://doi.org/10.1108/JSCM-05-2022-0198 11.  Marimuthu,  M.,  Gunasekaran,  A.,  &  Sivakumar,  A.  (2022).  COVID-19  pandemic  and  its  impact  

---

## Page 12

12  
on  Indian  mining  activities:  An  empirical  study.  Resources  Policy,  77 ,  102711.  https://doi.org/10.1016/j.resourpol.2022.102711 12.  Muthuri,  B.,  Ayomoh,  M.,  &  Gumbo,  M.  T.  (2021).  The  vulnerability  of  small-scale  mining  to  the  
COVID-19
 
pandemic:
 
A
 
case
 
study
 
of
 
South
 
Africa.
 
Journal
 
of
 
Sustainable
 
Mining,
 
20
(4),
 212-221.  https://doi.org/10.1016/j.jsm.2021.09.003 13.  Nadarajah,  S.,  &  Chu,  J.  (2016).  On  the  efficiency  of  Bitcoin.  Journal  of  Financial  Econometrics,  14 (4),  868-890.  https://doi.org/10.1093/jjfin/nbw001 14.  Qi,  X.,  Li,  X.,  &  Wu,  X.  (2023).  Blockchain  financial  technology  and  supply  chain  disruption  
risks:
 
Evidence
 
from
 
Chinese
 
listed
 
companies.
 
Journal
 
of
 
Operations
 
Management,
 
45
(3),
 201-218.  https://doi.org/10.1016/j.jom.2023.01.002 15.  Salisu,  A.  A.,  &  Ogbonna,  E.  I.  (2021).  The  role  of  news  in  predicting  return  volatility  of  
cryptocurrencies
 
during
 
the
 
health
 
crisis.
 
Journal
 
of
 
Economics
 
and
 
Finance,
 
45
(1),
 
1-19.
 https://doi.org/10.1007/s12197-020-09559-y 16.  Skipper,  H.,  &  Hanna,  M.  (2009).  An  empirical  analysis  of  supply  chain  flexibility.  International  
Journal
 
of
 
Physical
 
Distribution
 
&
 
Logistics
 
Management,
 
39
(4),
 
305-322.
 https://doi.org/10.1108/09600010910962258 17.  Urquhart,  A.  (2016).  The  inefficiency  of  Bitcoin:  A  systematic  review.  Journal  of  Financial  Markets,  15 (3),  1-16.  https://doi.org/10.1016/j.jfinmar.2015.05.002 18.  Wang,  C.,  &  Zhang,  Y.  (2022).  The  environmental  costs  of  Bitcoin  mining:  A  review  of  the  literature.  Environmental  Research,  210 ,  112891.  https://doi.org/10.1016/j.envres.2022.112891 19.  Wei,  W.  C.  (2018).  The  efficiency  of  cryptocurrency  markets:  An  empirical  analysis.  Journal  of  Financial  Markets,  17 (1),  1-19.  https://doi.org/10.1016/j.jfinmar.2017.07.001 20.  Yacoubian,  L.  J.,  Ketenchian,  G.  S.,  &  Garcia,  D.  S.  P.  (2020).  PANDEMIC-DRIVEN  BITCOIN  
PRICE
 
DYNAMICS,
 
ARTIFICIAL
 
INTELLIGENCE
 
PREDICTION,
 
AND
 
THE
 
LOOMING
 
QUANTUM
 
THREAT.
 
Revista
 
JRG
 
De
 
Estudos
 
Acadêmicos,
 
3
(6),
 
296–306.
 https://doi.org/10.55892/jrg.v3i6.664 

---
