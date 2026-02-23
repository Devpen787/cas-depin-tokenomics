# Cheng_Dai_Wang_Sun_Wen_Sun_2026_ControlTheoreticApproachToDecentralizedAIEconomyStabilizationViaDynamicBuybackAndBurnMechanisms.pdf

## Page 1

A Control Theoretic Approach to Decentralized AI
Economy Stabilization via Dynamic
Buyback-and-Burn Mechanisms
Zehua Cheng 1,2, Wei Dai 2, Zhipeng Wang 2,3, Rui Sun 2,4, Nick Wen 2, and Jiahao Sun 2
1FLock.io
2University of Oxford
3University of Manchester
4Newcastle University
hello@flock.io
Abstract—The democratization of artificial intelligence
through decentralized networks represents a paradigm shift in
computational provisioning, yet the long-term viability of these
ecosystems is critically endangered by the extreme volatility
of their native economic layers. Current tokenomic models,
which predominantly rely on static or threshold-based buyback
heuristics, are ill-equipped to handle complex system dynamics
and often function pro-cyclically, exacerbating instability
during market downturns. To bridge this gap, we propose the
Dynamic-Control Buyback Mechanism (DCBM), a formalized
control-theoretic framework that utilizes a Proportional-Integral-
Derivative (PID) controller with strict solvency constraints to
regulate the token economy as a dynamical system. Extensive
agent-based simulations utilizing Jump-Diffusion processes
demonstrate that DCBM fundamentally outperforms static
baselines, reducing token price volatility by approximately
66% and lowering operator churn from 19.5% to 8.1% in
high-volatility regimes. These findings establish that converting
tokenomics from static rules into continuous, structurally
constrained control loops is a necessary condition for secure
and sustainable decentralized intelligence networks.
Index Terms—decentralized AI, tokenomics, control theory,
buyback-and-burn, stability
I. INTRODUCTION
The democratization of artificial intelligence through de-
centralized networks represents a paradigm shift in how
computational resources and machine learning models are
provisioned [1]. By leveraging blockchain technology, these
platforms aim to create permissionless marketplaces that align
the incentives of model creators, compute providers, and end-
users. However, the long-term viability of these ecosystems
is critically dependent on their economic stability. Unlike
traditional SaaS platforms with fixed fiat pricing, decentralized
networks rely on native tokens whose value fluctuates with
market sentiment [2]. However, this volatility also represents
a systemic risk where without a consistent source of revenue
for the GPU operators and a fixed cost of inference for the
consumer, the underlying computational service itself, even
if it represents a technological advantage, will not be widely
adopted.
One of the most important tasks in this regard is creating a
reliable and self-managing economic system that always favors
the real inference and training economy. The token price in an
operating decentralized AI market could theoretically be based
on the utility value of the network (inference demand) rather
than just operating in the realm of speculation. The decoupling
of token prices from utility values during bear markets and
during hype cycles will create problems in the OpEx and
CapEx planning phases for compute and model providers [3].
Consequently, maintaining a price equilibrium that supports
sustainable growth while mitigating extreme volatility is not
merely a financial desideratum, but an operational necessity
for network survival.
Despite this need for stability, current tokenomic models
predominantly rely onstatic or simplistic heuristic mech-
anismsthat are ill-equipped to handle complex system dy-
namics. The standard buyback-and-burn model operates inde-
pendently of the network’s state, applying the same pressure
regardless of whether the token is overheating or collapsing
[4]. Even simple rules based on a certain threshold level (for
example, buying as the price drops byX) demonstrate “bang-
bang” control features and therefore induce oscillations. The
system will be brittle because it doesn’t adapt and doesn’t have
continuous control; this will create feedback circuits between
prices and activity in the network that can easily get out
of control because the parameters don’t adapt to exogenous
shocks.
To bridge this gap, we propose a shift from static policies
tocontrol-theoretic stabilization mechanisms. By modeling
the token economy as a dynamical system [5], we can apply
established principles from control engineering to regulate it.
We introduce theDynamic-Control Buyback Mechanism
(DCBM), which utilizes aProportional-Integral-Derivative
(PID) controllerto continuously adjust the buyback rate in
response to real-time on-chain metrics [6]. Just as a thermostat
regulates temperature by adjusting heating output based on
the deviation from a setpoint, our mechanism adjusts buyback
pressure to minimize the deviation of the token price from its
long-term growth trend. Uniquely, theintegral termallows
arXiv:2601.09961v1  [cs.GT]  15 Jan 2026

---

## Page 2

Fig. 1. Closed-loop control architecture of the Dynamic-Control Buyback Mechanism (DCBM). The schematic illustrates the feedback loop designed to
stabilize the decentralized AI economy. a, The Error Interface computes the logarithmic deviation (e k) between the target Time-Weighted Average Price
(TW AP) and the real-time Spot Price. b, The PID Controller processes this error, applying proportional, integral (clamped), and derivative gains to calculate
a raw intervention intensity (u k). c, The Solvency Actuator functions as a critical safety valve, strictly bounding the physical buyback expenditure (J k) by
the current Treasury Balance (T k) and the circuit breaker parameter (γ), ensuring asymptotic solvency regardless of market conditions. d, The AMM Plant
represents the market environment where the buy-and-burn action is executed, altering the token price state for the subsequent control epoch (k+ 1).
the system to correct for persistent errors (steady-state drift)
that static and threshold models ignore, enabling the network
to act counter-cyclically—building reserves during booms and
deploying them effectively to stabilize the economy during
busts.
Our contributions in the area of token engineering and
decentralized AI are the following. First, we provide a formal
control-theoretic modeling of the decentralized AI economy by
formally specifying the state space, the agent dynamics, and
the stability criteria taking into account solvency conditions for
the treasury. Second, we propose the DCBM algorithm based
on a PID controller designed to work in the blockchain envi-
ronment while taking into account the causality constraints and
the saturation constraints in discrete-time blockchain systems.
Finally, we validate our approach through extensive agent-
based simulations utilizing Jump-Diffusion processes [7] to
model fat-tail market shocks and specific adversarial attack
vectors. These experiments demonstrate that DCBM yields
superior price stability and lower operator churn compared to
static baselines, while exhibiting enhanced resilience against
MEV exploitation and market manipulation.
II. RELATEDWORK
Buyback-and-burn (BnB) is one of the most widely adopted
value-accrual primitives in contemporary token economies.
Analogous to equity repurchases in traditional finance, BnB
uses protocol revenue (or treasury assets) to purchase the na-
tive token in the open market and permanently remove it from
circulation (typically via an irrecoverable burn address). What
is noteworthy here is that the unique properties blockchain
technology, including immutability and transparency, enable
such BnB mechanisms to be carried out in a way that ensures
accountability and predictability [8].
Existing literature points to two effects of BnB. First, by
reducing the circulating supply of tokens permanently and
thus creating deflationary pressure, such strategy may maintain
stability or increase the price of a token [9], [10]. Second,
a way for projects to signal to the market that they are a
legitimate network business, especially in the presence of
non-zero information costs [4]. BnB mechanisms are not
uncommon across industry protocols like MakerDAO [11],
STEPN [12] and PancakeSwap [13]. This can be exceptionally
useful for protocols at its inception phase. For instance, when
DOT first launched, a liquidity pool mechanism was chosen
which combined token burning with token recycling, allows
DOT to operate as a central bank [14]. It was aimed to stabilize
velocity and incentivize participation at the project’s early
stage [8].
It is noteworthy that buyback may go alone without burning
in some cases. This may potentially shift governance distri-
butions or even pushing a project towards centralization [4].
Reversely, some may choose to burn without buy-back. This
is particularly prevalent in protocols which relying on slashing
mechanism to punish malicious behaviors.
Further, BnB is rarely an isolated mechanism; instead it
appears as one option in a broader “earnings allocation”
design space. For instance, Carvalho frames BnB as the token-
native counterpart to stock buybacks, situating it alongside
reserve accumulation, direct distributions, and reinvestment,
and emphasizes its role as a value-accrual path for gover-
nance and utility tokens [9]. In parallel, applied investor and
infrastructure-oriented literature highlights token design as a

---

## Page 3

primary determinant of ecosystem viability, as the token’s
rules (utility, governance, and monetary policy) directly shape
platform incentives and long-term adoption [15], [16].
However despite its prevalence in industry, BnB designs
lack comprehensive, empirical evidence to denote its strengths
and weaknesses. Further, existing BnB designs are typically
specified asstatic policies: a fixed fraction of revenue is
allocated to buybacks, or buybacks occur on a pre-announced
schedule, largely independent of the system’s evolving state.
Recent work on disclosure and market integrity argues that
credibility depends on transparent, rule-based execution with
public verification, because discretionary interventions can
concentrate informational advantage and invite allegations of
manipulation. However, even when fully transparent, static
BnB policies can behave procyclically: buybacks may natu-
rally expand when protocol revenue is high (often during bull
regimes) and shrink during downturns, precisely when price
support and operator revenue stability are most needed [10].
Moreover, deflationary pressure alone is insufficient to guar-
antee price stability under weak demand or large exogenous
supply shocks (e.g., unlocks and emissions), and aggressive fee
redirection into buybacks can undermine contingency funding
for operations and security.
Feedback control of prices has been extensively modeled
in the literature of macroeconomics and monetary theory for
quite some time now. The Taylor rule is one such monetary
policy rule where the policy reaction is proportional to the
inflation or the output gap, which has been extensively an-
alyzed in the literature regarding stability issues [17]. Sub-
sequent work shows that fixed or poorly tuned rules can
induce instability when agents adapt expectations over time,
motivating the need for state-dependent feedback mechanisms
[18], [19]. More recently, Hawkins et al. [20] explicitly
interpret monetary policy through the lens of proportional-
integral derivative (PID) control, demonstrating how integral
action eliminates steady-state drift while derivative terms damp
oscillatory dynamics. Collectively, this literature establishes
feedback control as a principled approach for stabilizing
complex economic systems under uncertainty.
Such findings trigger a rethink of the design of buyback-
and-burn schemes with a focus on control theory, particularly
in the context of a decentralized environment, in which the
issues of execution, transparency, and solvency conditions
remain paramount. Although the literature in economics and
money theory has shown that feedback control represents a
sound basis for price stabilization, these models generally
focus on policy formulation and equilibrium analysis, abstract-
ing from execution issues altogether. In contrast, the current
design of buyback-and-burn schemes in token economies
remains largely static and threshold-dependent, with no sta-
bility goal in sight, and with a lack of formal guarantees in
the face of stochastic demand and supply disturbances. Our
proposal remedies this shortcoming in that it operationalizes
the stabilization aspect of control theory in an on-chain,
executable manner. Indeed, we propose the design of buyback
actions as a feedback control actuator with the objective of
tracking a time-varying reference trajectory (time-weighted
average price trend), along with the hard enforcement of
solvency and saturation constraints, as naturally present in
the on-chain treasury system. This approach allows for: (i)
flexibility in the face of regime changes and disturbances,
using proportional, integral, and derivative actions; (ii) drift
compensation in the steady-state, using integral action; and
(iii) hard safety guarantees, using a solvency-aware actuator
and a circuit breaker mechanism. In practice, our DCBM
makes the buyback policy state-dependent, stability-objective-
driven, and safety-constraint-aware, features not present in the
current static and threshold-dependent designs of buyback-
and-burn schemes.
III. METHODOLOGY
A. Formal Problem Formulation
We model the decentralized AI economy as a discrete-time
dynamical system. To align with the computational constraints
of the Ethereum Virtual Machine (EVM)—specifically to mit-
igate the prohibitive gas costs of performing complex control
logic on every block—we discretize time into Control Epochs
indexed byk∈Z +. Each epoch spans a fixed duration∆t
(e.g.,Nblocks).
The system state at epochkis defined asS k =
[Pk, ¯Pk, Tk]⊤, where:P k is the Time-Weighted Average Price
(TW AP) of the native token over epochk. ¯Pk is the Target
Reference Price (Exponential Moving Average).T k refers to
Network Treasury Balance (denominated in Stablecoin, e.g.,
USDC).
Unlike previous models that incorrectly couple buybacks
to instantaneous revenue, we decouple accumulation from
stabilization. The Treasury acts as a reservoir that buffers
system shocks.
The Treasury evolves according to the conservation equa-
tion:
Tk+1 =T k +R acc(k)| {z }
Inflow
−J k|{z}
Outflow
(1)
WhereR acc(k)is the accumulated protocol revenue (fees) dur-
ing epochk, andJ k is the stabilization expenditure (buyback
amount) determined by the controller.
The system satisfies the strict solvency conditionT k+1 ≥0.
This impliesJ k ≤T k +R acc(k).
We assume the token trades on a Constant Product Market
Maker (CPMM) satisfying the invariantx·y=K, wherex
is the token reserve andyis the stablecoin reserve. When the
controller executes a buyback of magnitudeJ k (stablecoins),
the reserves update as follows:
ynew =y old +J k
xnew = K
ynew
The purchased tokens∆x=x old −x new are burned, perma-
nently reducing supply. This mechanical price impact provides
the actuation force for our control system.

---

## Page 4

B. Dynamical System Modeling and State Space
The economic stabilization of a decentralized network con-
stitutes a stochastic control problem constrained by the rigid
discrete-time execution of the underlying blockchain. Unlike
continuous-time financial models, a decentralized autonomous
organization (DAO) operates as a discrete dynamical sys-
tem where state transitions occur atomically at block height
k∈Z +. To rigorously define the control environment, we
establish a state spaceS k = [Pk, ¯Pk, Tk]⊤. Here,P k denotes
the Time-Weighted Average Price (TW AP) of the native token,
¯Pk represents the reference target price calculated via an
Exponential Moving Average (EMA), andT k represents the
Treasury Balance denominated in a stable numeraire. We
specifically utilize TW AP rather than instantaneous spot price
for the state definition to act as an intrinsic low-pass filter,
rendering the controller mathematically blind to single-block
flash loan attacks that rely on high-frequency price manipula-
tion.
A fundamental correction to prior tokenomic literature is the
incorporation of mandatory operational expenditures into the
treasury evolution equation. Previous models often assumed
monotonic treasury growth whenever revenue was positive,
leading to the “Treasury Paradox” where protocols appeared
solvent despite failing to cover basic costs. We define the
treasury dynamics using a strict conservation law that accounts
for fixed infrastructure overhead,C ops (e.g., oracle gas costs,
node subsidies). The state transition is given byT k+1 =
max(0, Tk+Racc(k)−J k −Cops). This formulation allows for
realistic simulation of liquidity crises; if accumulated revenue
Racc(k)is less thanC ops, the treasury naturally contracts,
imposing a time-to-ruin constraint that the controller must
actively manage.
The market plant is modeled as a Constant Product Market
Maker (CPMM) satisfying the invariantx·y=K. The
interaction between the stabilization expenditureJ k and the
market reserves creates a nonlinear feedback loop. For the
purpose of control design, we linearize the plant dynamics
around the operating point. In the logarithmic domain, the
price update approximates a discrete integrator with a variable
gainα k = 2/y k. This reveals that the system’s sensitivity
to buybacks is inversely proportional to liquidity depth, ne-
cessitating a controller that can operate stably across varying
regimes of market capitalization without inducing oscillatory
ringing.
C. Dynamic-Control Buyback Mechanism
To regulate this system, we introduce the Dynamic-Control
Buyback Mechanism (DCBM), a PID-based architecture
specifically optimized for the Ethereum Virtual Machine
(EVM). Standard control implementations are ill-suited for
this environment due to the prohibitive gas costs of floating-
point arithmetic and the risk of derivative kick during setpoint
changes. We employ a Derivative-on-Measurement strategy
combined with a Spectral Noise Filter. Instead of differentiat-
ing the error signal—which would amplify sudden price drops
into a ”panic buyback” signal—we calculate the rate of change
of the filtered TW AP. This ensures that the derivative term
functions correctly as a damper for organic volatility trends
while rejecting the high-velocity, high-amplitude signatures
characteristic of adversarial manipulation.
To address the “Gas Cost Impossibility” of calculating
transcendental functions on-chain, we implement the control
logic using high-precision fixed-point arithmetic (W AD math)
and Piecewise Linear Approximations. Functions such as
natural logarithm and hyperbolic tangent are approximated via
optimized lookup tables and Taylor series expansions bounded
to the expected domain of price deviations. This reduces the
computational footprint of the controller from a theoretical
infinite gas cost (for perfect precision) to a target execution
cost of approximately150,000gas, rendering the mechanism
economically viable for high-frequency deployment.
Under this definition,e k >0implies the asset is under-
valued (price below target), necessitating support. The DCBM
utilizes a discrete-time Proportional-Integral-Derivative (PID)
control law.
To prevent Integral Windup—a destabilizing phenomenon
where the integrator accumulates massive error during periods
when the treasury is empty (saturated)—we implement a
Clamped Integration scheme. The raw, dimensionless control
intensityu k ∈Ris computed as:
uk =K pek +K i
X
j= 0 kˆej∆t+Kd
ek −ek−1
∆t (2)
Here,ˆej represents the conditional error, defined asˆe j =e j
if the actuator is unsaturated (T j >0) and0otherwise.
This ensures the controller possesses a ”short-term memory”
of recent instability without being burdened by unresolvable
historical debts that occurred when it lacked the agency to act.
The final stage of the methodology maps the abstract control
intensityu k to a physical expenditureJ k in a manner that sat-
isfies Assumption 1 by construction. We introduce a Sigmoid
Actuator bounded by a ”Liquidity Circuit Breaker” parameter
γ∈(0,1]. The physical buyback amount is determined by the
mapping functionΦ :R×R ≥0 →R ≥0:
Jk = Φ(uk, Tk) =T k ·γ·tanh(max(0, u k))(3)
Themax(0, u k)operator ensures that negative signals (over-
valuation) result in zero spending. The termγdefines the
maximum fraction of the treasury that can be deployed in
a single epoch. This multiplicative formulation provides a
critical theoretical guarantee regarding the system’s survival.
Proposition III.1(Asymptotic Solvency).Given an initial
treasuryT 0 >0and parameterγ∈(0,1), the treasury
balanceT k remains strictly positive for all finitek, regardless
of the magnitude or duration of revenue collapse (R k = 0).
Proof: Substituting Equation 3 into Equation 1 under the
worst-case conditionR k = 0yields the geometric recur-
sionT k+1 =T k(1−λ k), whereλ k =γtanh(u k). Since
tanh(·)<1andγ <1, the decay factor(1−λ k)is strictly
positive. Thus, the treasury follows a Zeno-like trajectory,
asymptotically approaching zero but never reaching it. This

---

## Page 5

ensures the protocol never defaults, maintaining a non-zero
dust reserve to fund recovery once market conditions stabilize.
D. Game-Theoretic Robustness
In a permissionless blockchain environment, the controller
must be robust not only to stochastic noise but also to strategic
exploitation by Maximal Extractable Value (MEV) agents. We
model the adversarial interaction as a ”Fishing Attack,” where
an adversaryAartificially depressesP k to trigger a subsidized
buyback. We assume the adversary solves the following profit
maximization problem at each epochk:
max
δ
E[Π A] =E[P exit(Jk(δ))−P entry −C risk(τ)](4)
whereδis the induced price deviation andC risk(τ)is the cost
of holding the deviation for durationτ.
The DCBM defends against this manipulation via the spec-
tral filtering properties of the Derivative term (K d) in Eq.
2. By reacting to the rate of change 1 ∆ek
∆t , the controller
identifies the high-velocity signature of a flash-loan attack
as noise rather than a trend shift.2 This effectively acts as
a high-pass filter that suppresses the actuation signalu k in the
presence of discontinuities, forcing the adversary to sustain
the manipulation over multiple epochs (τ > N∆t) to trigger
the Integral term. This requirement linearly increases the
adversary’s exposure to market riskCrisk, rendering the attack
strictly dominated (negative expected value) for sufficiently
tuned gains.
IV. THEORETICALANALYSIS
We analyze the DCBM as a closed-loop feedback control
system. Unlike classical control problems where the actuator
has infinite energy (e.g., a motor connected to the grid),
our system is energy-constrained: the control authority is
strictly limited by the finite Treasury levelT k. We analyze the
system’s behavior across two dimensions: Dynamical Stability
(convergence) and Structural Solvency (non-bankruptcy).
A. Plant Model Derivation (AMM Dynamics)
To analyze stability, we must mathematically define how
the control action (buybackJ k) affects the system state (price
Pk). We assume a Constant Product Market Maker (CPMM)
satisfying the invariantx k ·y k =K, where priceP k = yk
xk
.A
buyback of magnitudeJ k (stablecoins) shifts the reserves:
yk+1 =y k +J k
The new priceP k+1 follows the quadratic AMM curve:
Pk+1 = (yk +J k)2
K =P k

1 + Jk
yk
2
(5)
Taking the natural logarithm to align with our log-error
controller (e k = ln ¯Pk −lnP k):
ln(Pk+1) = ln(Pk) + 2 ln

1 + Jk
yk

+ξ k
whereξ k represents exogenous market noise.
Linearization: For the operating region where buybacks are
small relative to liquidity depth (J k ≪y k), we use the Taylor
approximationln(1 +x)≈x. We define the Price Impact
Coefficientα k = 2
yk
. The linearized plant model is:
pk+1 =p k +α kJk +ξ k (6)
wherep k = ln(Pk). This establishes the market as a Discrete
Integrator Plant: the price state accumulates the history of
control actions, implying that without control, errors persist
indefinitely (Type 1 System).
B. Closed-Loop Stability Analysis
We examine the feedback loop formed by the Plant and
the PID Controller. Let the target ¯Pbe constant for stability
analysis (¯pk+1 = ¯pk). The error dynamics aree k+1 =e k −
αkJk.
Substituting the PID control law in the Z-domain, the open-
loop transfer functionL(z)is the product of the Controller
C(z)and PlantP(z):
P(z) = α
z−1
C(z) =K p +K i
z
z−1 +K d
z−1
z
The closed-loop characteristic equation is1 +C(z)P(z) =
0. Substituting and organizing terms yields the characteristic
polynomial inz:
z2(1 +αKp +αK i +αK d)−z(2 +αK p + 2αKd) + (1 +αKd) = 0
(7)
Stability Criteria:Applying the Jury Stability Test for a second-
order discrete system, the roots of this polynomial lie strictly
inside the unit circle (|z|<1) if and only if the gains satisfy
the following inequalities: Positivity:K p +K i >0; Damping
Limit:K d < 2−αKp
α ; Integral Limit:K i < 4−2αKp
α .
Implication(The “Whale in a Puddle” Risk): The stability
region scales inversely withα= 2
yk
.
Theorem IV .1(Gain Sensitivity).As liquidity decreases
(yk →0), the plant gainα→ ∞. To maintain sta-
bility, the controller gains (K p, Ki, Kd) must be reduced
proportionally.This proves that static-parameter baselines in-
evitably enter oscillatory instability (”ringing”) during liq-
uidity crunches, whereas the DCBM’s solvency constraint
(derived below) naturally throttles the effective gain (T kγ) to
satisfy these bounds.
C. Proof of Asymptotic Solvency
A critical requirement for an autonomous economic agent is
that it must never default. We formally prove that the DCBM
TreasuryT k remains strictly positive for all finite timek.
Theorem IV .2(Non-Depletion).Given an initial treasury
T0 >0, the treasury balanceT k >0for allk∈Z +,
regardless of market conditions.
Proof: Recall the Treasury evolution from Equaiton 1. Sub-
stituting the actuator mapping functionJ k =T k ·γ·tanh(u k):
Tk+1 =T k[1−γ·tanh(u k)] +R acc(k)

---

## Page 6

Letλ k =γtanh(u k). By design, the Liquidity Circuit Breaker
γ∈(0,1)andtanh(·)∈[0,1), so0≤λ k <1.Consider the
doomsday scenario where RevenueR acc = 0indefinitely. The
treasury evolves as a geometric sequence:
Tk+1 =T k(1−λ k)
Tn =T 0
n−1Y
k=0
(1−λ k)
Since(1−λ k)is strictly positive, the product is strictly
positive.Conclusion: The Treasury asymptotically approaches
zero but never reaches it. The system exhibits Structural
Solvency, ensuring that a dust reserve always remains to fund
recovery, making the bankruptcy scenarios observed in Fixed-
Rate baselines mathematically impossible.
D. Robustness to Impulse Attacks
Finally, we address the system’s resilience against game-
theoretic exploitation, specifically “Fishing” attacks where
Maximal Extractable Value (MEV) actors introduce artificial
volatility to trigger profitable buybacks. We model these at-
tacks as a discrete impulse function:δ attack(k) = ∆spike ·δ(k)
injected into the price signal. A naive proportional controller
would immediately react to this signal, effectively transferring
treasury funds to the attacker. The DCBM, however, employs
a spectral filtering approach to reject these high-frequency
anomalies. The use of Time-Weighted Average Price (TW AP)
inputs acts as a low-pass filter, attenuating the magnitude of
any single-block manipulation by a factor of 1
N , whereN
is the epoch length. Further, the derivative part of the PID
controller acts as a high-pass filter in the control system.
The Z-transform of the derivative part of the control system
translates a zero at the origin, making it prone to changes
in the error signal. For an attacking agent trying to cause a
flash crash in price, the derivative part of the control system
reacts to the mathematically improbable rate of price drop by
generating a compensatory control signal that dampens the
system’s control. Thus, it becomes costly for the attacking
agent because a significant amount of capital is needed to
maintain a price deviation against market participants over
a period of multiple epochs, which is typically above the
maximum value that can be extracted from the treasury.
V. EXPERIMENTS
The experiments are designed to rigorously evaluate the pro-
posed Dynamic-Control Buyback Mechanism (DCBM) against
baseline models using a sophisticated agent-based simulation.
A. Dataset Preparation
We will use a dual-data approach to ensure the simulation is
both theoretically sound and grounded in real-world dynamics,
a methodology validated by [21].
1)Synthetic Data Generation:
•Inference Demand (D t):We will model the arrival
of inference demand as a stochastic process using
aJump-Diffusion Model[7] (extending GBM).
This incorporates a standard drift (µD) and volatility
(σD) component, plus a Poisson process to simulate
sudden, discontinuous “jumps” (shocks) in demand.
This ensures the simulation captures fat tail events
and does not underestimate the frequency of black
swan scenarios, a critical improvement over stan-
dard GBM.
•External Market Shocks (ξ t):Broader crypto mar-
ket movements affecting the native token’s price will
also be modeled as a Jump-Diffusion process, with
drift (µP ) and volatility (σ P ) parameters, correlated
with the inference demand process.
2)Real-World Data Integration:
•Model Usage Data:We will source anonymized
historical data on the usage of popular open-source
AI models from platforms like Hugging Face to
create realistic demand patterns for inference. This
includes metrics like daily downloads and API calls.
•Token Price Data:We will use historical price data
from existing decentralized AI or DePIN (Decen-
tralized Physical Infrastructure Networks) project
tokens (e.g., Bittensor, Render) to simulate realistic
price volatility and correlation with the broader
market (e.g., BTC/ETH).
B. Baseline Implementation
To establish a benchmark for performance, we will im-
plement and simulatefivebaseline tokenomic models. These
models will run within the same agent-based framework as
our proposed method. The Figure 2 presents the details of the
baselines.
C. Proposed Method Implementation
The DCBM will be implemented as a modular component
within the agent-based simulation, written in Python using
libraries such as Mesa (for agent-based modeling) and NumPy.
•Agent Implementation:We will define four agent
classes:ModelOwner,Operator,User, and
Speculator. Each agent will have a state (e.g.,
token balance, active models) and astep()method
that executes their decision logic based on their utility
function and perception of the market state.
•Controller Implementation:The PID controller will
be implemented as a class that maintains the state of
the integral and derivative terms. At each simulation
step (representing a block), it will read the network
metrics, calculate the new buyback rateu t, and execute
the buyback against a simulated AMM.
•Development Phases:
1)Phase 1:Implement the agent logic and market
environment.
2)Phase 2:Integrate the baseline models.
3)Phase 3:Implement and integrate the DCBM con-
troller.

---

## Page 7

Fig. 2. Schematic representation of baseline stabilization mechanisms. The diagram illustrates the five control strategies evaluated against the proposed DCBM:
(1) No Buyback, where fees are fully distributed to operators without burning; (2) Fixed-Rate Buyback, which applies a static percentage burn (e.g., 50%)
regardless of market state; (3) Threshold Buyback, a heuristic approach triggering buybacks only when spot priceP t falls below the moving averageP M A,t;
(4) Model Predictive Control (MPC), which minimizes predicted error over a finite horizon; and (5) Reinforcement Learning (PPO), utilizing a neural policy
to maximize a reward function based on stability and control effort.
4)Phase 4:Calibrate agent parameters and controller
gains (K p, Ki, Kd) using a smaller set of synthetic
data before running full-scale experiments.
D. Main Experiments & Evaluation
The main experiments will involve running the simulation
for each model (2 baselines, 1 proposed) under various data-
driven scenarios. We will use Monte Carlo methods, running
each scenario 1,000 times to gather statistical distributions of
our evaluation metrics. Each simulation run will span a period
equivalent to 1 year of real-world time, with discrete time steps
(∆t) corresponding to blockchain block times (e.g., 12-second
intervals).
Evaluation Metrics:
•Token Price Volatility:Standard deviation of log returns
of the token price, and the average percentage deviation
from the moving average ( 1
T
PT
t=1 | Perr,t
PM A,t
|).
•Gini Coefficient of Token Holdings:To measure wealth
concentration and decentralization within the network.
•Operator Churn Rate:Percentage of operators leaving
the network per simulation period, normalized by total
operators.
•Model Innovation Rate:Number of new high-quality
models introduced per period, normalized by total de-
ployed models.
•Network Treasury Health:The average rate of change
of the treasury’s value over time, and its stability (stan-
dard deviation).
•Control Effort:The average buyback rateu t and its
variance, indicating the aggressiveness and stability of
the controller.
Hyperparameters and Tuning:
•PID Gains (K p, Ki, Kd):These will be tuned using a
grid search or optimization algorithms (e.g., Bayesian
optimization) on a validation set of synthetic data to
minimize a composite loss function that includes price
volatility and treasury health.
•AMM Liquidity:The initial liquidity in the simulated
AMM pool will be varied to observe the impact of market
depth on price stability.
•Agent Parameters:Risk aversion (λ M O, λOP ), cost
parameters, and utility function weights will be set based
on economic intuition and sensitivity analysis.
•Moving Average Window:The window size forP M A,t
will be explored (e.g., 30-day, 60-day) to assess its impact
on the target signal.
E. Attack and Game Robustness Experiments
The deployment of deterministic control loops in adversarial
blockchain environments introduces specific game-theoretic
vulnerabilities that differ from standard stochastic market
noise. While the DCBM is designed to dampen volatility,
its reliance on observable on-chain metrics, specifically the
deviation between spot price and moving average which cre-
ates a potential attack surface for Maximal Extractable Value
(MEV) bots and strategic large holders. To rigorously evaluate
the mechanism’s resilience against these adversarial behaviors,
we introduce a specific set of attack simulations targeting the
controller’s logic.
We model two primary adversarial strategies:Signal Ma-
nipulation (“Fishing”)andFront-running/Sandwiching. For
example, in the Front-running attack, the MEV bot spots a

---

## Page 8

TABLE I
COMPARATIVEANALYSIS OFECONOMICSTABILITY ANDNETWORKHEALTHMETRICS. VALUES INDICATEMEAN±95% CI. BEST RESULTS
(EXCLUDING THEORACLE)ARE BOLDED.↓IMPLIES LOWER IS BETTER;↑IMPLIES HIGHER IS BETTER. GAS ESTIMATES ARE APPROXIMATE FOR
EVM-EQUIVALENT CHAINS.
Scenario Model σP ↓ ϵMA ↓ Churn↓ Gini↓ Growth↑ Compute Cost↓
Bull Market
No Buyback 0.42±0.03 12.4%±1.2 5.2±0.5 0.88 15.2±1.1 –
Fixed-Rate 0.39±0.02 8.1%±0.9 4.8±0.4 0.85 8.1±0.8 ≈21k
Threshold 0.31±0.04 6.5%±1.5 4.1±0.8 0.82 9.4±1.2 ≈5k
RL (PPO) 0.26±0.05 3.5%±0.8 4.0±0.6 0.80 10.8±1.4 ≈720k
MPC (Oracle) 0.19±0.01 2.0%±0.2 3.5±0.2 0.78 12.5±0.6 >40M
DCBM (Ours) 0.21±0.01 2.3%±0.3 3.8±0.2 0.79 11.2±0.5 ≈8k
Bear Market
No Buyback 0.65±0.05 28.7%±2.1 42.1±3.5 0.92 2.1±0.9 –
Fixed-Rate 0.59±0.04 22.4%±1.8 35.5±2.8 0.89 -12.4±1.5 ≈21k
Threshold 0.48±0.06 15.2%±2.4 28.4±4.1 0.86 -5.1±1.8 ≈24k
RL (PPO) 0.41±0.08 8.2%±1.2 15.8±2.1 0.83 -3.5±1.1 ≈720k
MPC (Oracle) 0.28±0.02 5.0%±0.5 10.5±0.8 0.80 -1.2±0.3 >40M
DCBM (Ours) 0.32±0.02 5.8%±0.6 12.6±1.1 0.81 -1.8±0.4 ≈32k
High V olatility
No Buyback 0.89±0.07 35.6%±3.2 28.4±2.9 0.91 5.4±1.2 –
Fixed-Rate 0.75±0.05 28.5%±2.2 24.2±2.5 0.88 -4.2±1.4 ≈21k
Threshold 0.55±0.08 18.4%±2.5 19.5±3.1 0.85 -2.5±1.6 ≈15k
RL (PPO) 0.45±0.12 6.5%±1.1 11.5±1.5 0.81 -0.5±0.8 ≈720k
MPC (Oracle) 0.26±0.02 3.8%±0.4 7.2±0.6 0.77 2.1±0.4 >40M
DCBM (Ours) 0.30±0.02 4.2%±0.5 8.1±0.8 0.78 1.5±0.3 ≈28k
Demand Shock (+)
No Buyback 0.55±0.04 18.5%±1.5 4.5±0.3 0.89 22.4±1.8 –
Fixed-Rate 0.45±0.04 14.2%±1.3 4.2±0.4 0.86 12.5±1.0 ≈21k
Threshold 0.38±0.05 9.2%±1.1 4.1±0.4 0.83 14.2±1.1 ≈5k
RL (PPO) 0.32±0.06 5.1%±0.9 3.9±0.5 0.81 16.8±1.5 ≈720k
MPC (Oracle) 0.22±0.01 2.5%±0.3 3.2±0.2 0.78 19.5±0.8 >40M
DCBM (Ours) 0.25±0.02 3.1%±0.4 3.6±0.3 0.79 18.1±0.6 ≈8k
Demand Shock (-)
No Buyback 0.78±0.06 42.1%±3.8 55.2±4.5 0.94 1.5±0.5 –
Fixed-Rate 0.70±0.06 31.5%±2.8 45.2±3.8 0.91 -6.5±1.2 ≈21k
Threshold 0.62±0.07 21.5%±2.2 32.4±3.8 0.88 -8.5±1.2 ≈24k
RL (PPO) 0.51±0.09 12.4%±1.6 18.5±2.2 0.84 -4.2±0.9 ≈720k
MPC (Oracle) 0.35±0.02 6.8%±0.5 11.2±1.1 0.81 -1.5±0.4 >40M
DCBM (Ours) 0.39±0.03 7.5%±0.8 14.1±1.5 0.82 -2.4±0.6 ≈32k
Liquidity Crisis
No Buyback 1.12±0.15 58.4%±6.2 48.5±5.1 0.95 3.2±1.1 –
Fixed-Rate 0.98±0.10 45.2%±5.1 42.1±4.5 0.93 -4.2±1.5 ≈21k
Threshold 0.85±0.12 35.2%±4.5 35.2±4.2 0.91 -9.2±2.5 ≈20k
RL (PPO) 0.68±0.14 15.4%±2.8 22.1±3.5 0.88 -5.5±1.8 ≈720k
MPC (Oracle) 0.42±0.04 8.5%±0.9 14.5±1.5 0.84 0.5±0.8 >40M
DCBM (Ours) 0.48±0.05 10.2%±1.2 18.4±2.1 0.86 -0.8±1.2 ≈30k
pending buyback in the mempool and submits a buy order
just before it happens, followed by a sell order to reap a risk-
free profit. In the Signal Manipulation attack, a big holder
unwinds a part of their holding to drive down the price below
the moving average, triggering a forceful buyback signal from
the PID controller. They then sell the rest of their holding in
the PID controller at a reduced price. These attacks test if the
system serves as a predictable source of exit liquidity instead
of a stabilizer.
To quantify robustness, we measureAttacker Profitability,
Treasury Efficiency Loss, andStability Degradation. We
hypothesize that while simple threshold-based mechanisms are
highly susceptible to “fishing” due to their binary response, the
DCBM’s derivative term (Kd) and integral memory (K i) will
provide a degree of resistance. The derivative term dampens
the controller’s reaction to sudden, sharp price drops typical
of manipulation attempts, while the integral term requires
sustained deviation to ramp up buyback pressure, making
instantaneous “pump-and-dump” attacks capital-inefficient for
the attacker. We expect these experiments to demonstrate that
DCBM incurs a lower “manipulation tax” on the treasury
compared to static baselines.
VI. RESULTS
We present the empirical results of our extensive agent-
based simulations, evaluating the efficacy of the Dynamic-
Control Buyback Mechanism (DCBM) against standard in-
dustry baselines. The experiments were conducted using the
simulation framework described in this section, running on a
high-performance compute cluster to facilitate 1,000 Monte
Carlo runs per scenario. Our analysis focuses on three core
dimensions: (1) macro-economic stability and network health
under varying market conditions, (2) the specific contribution
of control-theoretic components via ablation studies, and (3)
system resilience against adversarial game-theoretic attacks.

---

## Page 9

A. Macro-Economic Stability and Network Health
Our primary evaluation compares the DCBM against three
baselines: theLaissez-Faire(No Buyback) model, theStatic
(Fixed-Rate) model, and theHeuristic(Threshold) model. We
examined these across three distinct market regimes modeled
by Jump-Diffusion processes [7]: aBull Market(positive drift
µD >0), aBear Market(negative driftµ D <0), and a
High Volatilityregime (highσ D, σP ). Table 1 summarizes the
aggregate performance metrics.
1) Analysis of Main Results:The results in Table 1 demon-
strate a statistically significant improvement in stability metrics
for the DCBM across all scenarios. In theHigh Volatility
regime, which represents the greatest threat to network viabil-
ity, the DCBM reduced price volatility (σ P ) by approximately
66% compared to the No Buyback baseline and 46% compared
to the Heuristic Threshold model. This suppression of volatil-
ity directly correlated with a reduction inOperator Churn,
which dropped from 19.5% (Threshold) to 8.1% (DCBM).
Qualitative inspection of agent logs reveals that operators
in the DCBM simulations maintained profitability for longer
durations due to the predictable “price floor” effect created
by the controller’s integral term, which aggressively corrected
persistent negative deviations.
Notably, theTreasury Growthmetric highlights the capital
efficiency of our approach. While the Fixed-Rate model indis-
criminately burned capital during the Bear Market, resulting
in a 12.4% treasury contraction, the DCBM limited this loss
to 1.8%. Conversely, in the Bull Market, the DCBM allowed
the treasury to accumulate reserves (11.2% growth) rather
than over-spending, effectively “saving for a rainy day.” This
counter-cyclical behavior validates the theoretical solvency
constraints embedded in the control law.
B. Ablation Study: Component Contribution
TABLE II
ABLATIONSTUDY OFCONTROLLERCONFIGURATIONS(HIGH
VOLATILITYSCENARIO)
Controller MSE Settling
Time
Max
Overshoot
Steady-
State Err.
Control
Var.
P-Only0.045 142 18.5% 4.2% 0.12
PI-Only0.012 210 25.4%0.1%0.18
PD-Only0.03885 5.2%3.8% 0.09
Full PID 0.008115 8.4% 0.3%0.11
To isolate the impact of the Proportional (K p), Integral
(Ki), and Derivative (K d) terms, we conducted an ablation
study under the High V olatility scenario. We evaluated four
controller configurations: P-Only, PI-Only, PD-Only, and the
full PID controller. Table 2 presents the control performance
metrics.
1) Analysis of Control Dynamics:The ablation results con-
firm the theoretical roles of each term. TheP-Onlycontroller
exhibited a persistent steady-state error (4.2%), failing to fully
return the price to the moving average during sustained selling
pressure. The addition of the Integral term in thePI-Only
configuration successfully eliminated this error (e ss ≈0.1%)
but introduced significant instability, evidenced by a high
Maximum Overshoot (25.4%) and longer settling times. This
aligns with control theory, as the integral term adds phase lag.
ThePD-Onlycontroller provided the fastest response (Set-
tling Time: 85 blocks) and lowest overshoot, demonstrating
the Derivative term’s ability to dampen volatility. However, it
failed to correct the long-term drift. TheFull PIDconfigu-
ration achieved the optimal trade-off, leveraging the Integral
term for error elimination and the Derivative term for damping,
resulting in the lowest Mean Squared Error (0.008).
C. Adversarial Robustness and Control System Security
To align our evaluation with standards in robust machine
learning and control theory, we treat the DCBM controller as
a differentiable policyπ θ(St)and subject it to gradient-based
adversarial attacks. We map standard adversarial attack vectors
to economic manipulation strategies:
•FGSM (Fast Gradient Signal Manipulation):Analo-
gous to the Fast Gradient Sign Method, this represents
a single-step, high-intensity “Flash Crash” attack where
the adversary calculates the gradient of the buyback rate
∇Sut and perturbs the priceP t by−ϵ·sign(∇ Sut)to
maximize system over-reaction.
•PGD (Projected Gradient Descent Manipulation):
A multi-step, iterative “Sustained Manipulation” attack
where the adversary optimizes a sequence of trades over
kblocks to drain the treasury, constrained by a capital
budgetϵ.
•C&W (Cost-Optimized Arbitrage):A Carlini &
Wagner-style attack that finds the minimum perturbation
δrequired to force the controller into a saturated state
(ut = 1.0), minimizing attacker cost while maximizing
disruption.
We evaluate four defense configurations:
1)Baseline (Threshold):The heuristic rule described in
Section 3.2.
2)PID-Standard:The DCBM with parameters tuned via
standard grid search.
3)PID-AdvTrain (Adversarial Training):The DCBM
with parametersθoptimized via a min-max game ob-
jective:min θ maxδ∈∆ L(πθ(St +δ)).
4)PID-Cert (Certified Robustness):The DCBM with
analytical bounds on the integral term accumulation
(clipping) and Lipschitz continuity constraints on the
derivative term.
1) Analysis of Adversarial Dynamics:Table III reveals a
strict hierarchy in defense capability. TheBaseline (Thresh-
old)model, akin to a standard non-robust classifier, collapses
almost entirely under even moderate perturbation budgets
(ϵ= 1.0%), exhibiting an Attack Success Rate (ASR) nearing
100%. This confirms that static, binary rules are easily game-
able by adversaries who can calculate the precise sell volume
required to trigger the threshold.
ThePID-Standardoffers a baseline level of improvement,
reducing treasury drain significantly, but remains vulnerable

---

## Page 10

TABLE III
COMPREHENSIVEADVERSARIALROBUSTNESSANALYSIS
Defense Type Attack Type Budget (ϵ) Success Rate
(↓)
Robustness
Score↑ Treasury Drain Defense Efficacy Robustness Gain
BaselineFGSM-Flash 1.0% 88.4% 0.116 22.1% - -
Baseline FGSM-Flash 2.5% 96.2% 0.038 34.5% - -
Baseline FGSM-Flash 5.0% 100.0% 0.000 58.2% - -
Baseline PGD-Sustained 1.0% 92.1% 0.079 28.4% - -
Baseline PGD-Sustained 2.5% 98.5% 0.015 45.1% - -
Baseline PGD-Sustained 5.0% 100.0% 0.000 72.3% - -
Baseline C&W-Arb - 91.5% 0.085 18.2% - -
PID-StandardFGSM-Flash 1.0% 42.1% 0.579 8.5% +12.4% +46.3%
PID-Standard FGSM-Flash 2.5% 68.3% 0.317 14.2% +8.1% +27.9%
PID-Standard FGSM-Flash 5.0% 85.2% 0.148 25.1% +4.2% +14.8%
PID-Standard PGD-Sustained 1.0% 55.4% 0.446 12.8% +9.5% +36.7%
PID-Standard PGD-Sustained 2.5% 81.2% 0.188 29.4% +3.1% +17.3%
PID-Standard PGD-Sustained 5.0% 94.1% 0.059 48.2% +1.2% +5.9%
PID-Standard C&W-Arb - 62.4% 0.376 11.5% +10.2% +29.1%
PID-AdvTrainFGSM-Flash 1.0% 12.5% 0.875 3.2% +28.5% +75.9%
PID-AdvTrain FGSM-Flash 2.5% 24.1% 0.759 5.8% +22.1% +72.1%
PID-AdvTrain FGSM-Flash 5.0% 45.3% 0.547 11.2% +16.4% +54.7%
PID-AdvTrain PGD-Sustained 1.0% 18.2% 0.818 4.5% +25.2% +73.7%
PID-AdvTrain PGD-Sustained 2.5% 35.6% 0.644 9.1% +18.7% +62.9%
PID-AdvTrain PGD-Sustained 5.0% 62.1% 0.379 18.5% +11.2% +37.9%
PID-AdvTrain C&W-Arb - 28.4% 0.716 6.2% +24.8% +63.1%
PID-CertFGSM-Flash 1.0%4.2% 0.958 1.2% +32.1% +84.2%
PID-Cert FGSM-Flash 2.5%9.1% 0.909 2.4% +29.4% +87.1%
PID-Cert FGSM-Flash 5.0%18.5% 0.815 4.8% +24.8% +81.5%
PID-Cert PGD-Sustained 1.0% 8.4% 0.916 1.8% +30.2% +83.4%
PID-Cert PGD-Sustained 2.5% 15.2% 0.848 3.9% +26.5% +83.3%
PID-Cert PGD-Sustained 5.0% 32.1% 0.679 8.5% +19.1% +67.9%
PID-Cert C&W-Arb - 12.6% 0.874 2.9% +28.2% +78.9%
Input-SmoothFGSM-Flash 5.0% 55.2% 0.448 14.5% +12.4% +44.8%
Input-Smooth PGD-Sustained 5.0% 78.4% 0.216 32.1% +5.1% +21.6%
to high-budget iterative attacks (PGD), where the adversary
“steers” the controller into an unstable region over time.
The deployment of deterministic control loops in blockchain
environments inevitably introduces game-theoretic vulnerabil-
ities where adversaries attempt to reverse-engineer the inter-
vention logic to extract risk-free value. This analysis evalu-
ates the resilience of the proposed DCBM against such so-
phisticated threats, specifically contrasting heuristic baselines
against advanced control-theoretic defenses. The results from
the “Fishing” and “Flash Crash” vector simulations reveal that
defense mechanisms relying on static rules or unconstrained
feedback loops eventually become predictable exit liquidity
for well-capitalized adversaries.
The brittleness of static heuristic models is immediately
apparent when subjected to optimization-based attacks, con-
firming the hypothesis that binary intervention rules are fun-
damentally insecure. Theoretical vulnerability transforms into
catastrophic failure in the Baseline (Threshold) model, which
lacks the capacity to modulate its response based on the
severity or persistence of a shock. Under the FGSM-Flash
attack with a mereϵ= 1.0%budget, the baseline already
concedes an 88.4% Attack Success Rate (ASR)3. The failure
becomes absolute under the PGD-Sustained attack (ϵ= 5.0%),
where the baseline fails 100.0% of the time, resulting in
a massive 72.3% treasury drain, effectively rendering the
protocol insolvent.
Standard feedback control mechanisms offer a statistically
significant improvement over static baselines by introducing
soft response curves that are harder to game instantaneously,
though they remain susceptible to sustained manipulation. The
PID-Standard configuration dampens the efficacy of instanta-
neous shocks, reducing the success rate of the 1.0% FGSM-
Flash attack from 88.4% to 42.1% and limiting treasury drain
to 8.5%. However, this unhardened controller struggles against
iterative optimization attacks that steer the system over time;
under the high-budget PGD-Sustained attack (ϵ= 5.0%),
the PID-Standard still succumbs to a 94.1% success rate
and a 48.2% treasury drain, indicating that without specific
constraints, the integrator term can still be weaponized by an
attacker to saturate the controller.
Adversarial training properly reinforces the controller
against known attack gradients, making the defense pro-
active rather than reactive and improving robustness. The PID-
AdvTrain model, which is optimized for a min-max objective

---

## Page 11

against PGD attack models, shows a dramatic decrease in
exploitability for all vectors. When attacked by FGSM-Flash
(1.0%), success rate drops to 12.5%, and treasury drain is
restricted to a negligible 3.2%. Even for the very powerful
C&W-Arb attack, robustness is maintained at 0.716, which is
a far higher value than that of the standard PID at 0.376.
In the end, the application of structural constraints via
Certified Robustness appears to be the most effective defense
mechanism, performing better than even the adversarially
learned model parameters of adversarial training. On one hand,
through mathematical constraints of control authority using
Lipschitz continuity and saturation thresholds, the PID-Cert
setup prevents the system from falling prey to overreaction,
regardless of the input disturbance scale. On the other hand,
this is proved through its efficacy in the most adversarial test
environment, namely the PGD-Sustained attack with a 5.0%
budget, where the system keeps the attack success rate at
32.1% and the treasury depletion at a manageable 8.5%, a
factor of nearly a ten-fold difference over the 72.3% loss of
the baseline system.
VII. DISCUSSIONS
First, the operational viability of Decentralized AI Networks
largely depends on the economic stability of their respective
tokens because high volatility makes it difficult to plan for
Compute Providers (CapEx) and Model Users (OpEx) in AI
applications. The experiment shows that the Dynamic-Control
Buyback Mechanism (DCBM) successfully separates network
utility from speculative market cycles, reducing price volatility
by 66% compared to laissez-faire approaches. The DCBM
gives AI network operators a stable floor of revenue because it
changes the economy of tokens from a chaotic to a sentiment-
driven market to a dynamical system, thus reducing churn rates
from 19.5% to 8.1%. This makes it an economic imperative
for DePIN to compete with SaaS applications that use fixed
fiat prices.
Whereas the goal is stabilization, the resilience of the
stabilization mechanism itself, from a game-theoretic point
of view, is the key that decides the long-term viability of a
given permissionless network. The catastrophic failure of the
heuristic “Threshold” approach within the adversarial tests,
with failure rates close to 100% for the heuristic approach,
illustrates the high risk involved with the use of static rules
within the adversarial context. In the dark forest scenario,
where the overall balance is dominated by the actions of the
Maximal Extractable Value (MEV) bots, the clear and static
intervention levels offer a predictable and exploitable signal
for the well-informed agents, which would then derive risk-
free gains from the project’s treasury. The results suggest that
the “Certified Robustness” setting for the DCBM overturns
the situation, forcing the attackers to assume market risk that
is proportional to the length of the manipulation, making the
pump and dump approach mathematically unprofitable.
To distinguish between “saving” and “stabilizing”, consider
the following behaviors that can be observed in treasuries:
Fixed Rate baselines and DCBM have different dynamics. Tra-
ditional buyback strategies that burn a constant fraction of the
revenue are pro-cyclic, reducing the reserves during periods
when the network needs them most to protect value. On the
other hand, the integral component of DCBM imposes natural
counter-cyclic constraints, ensuring that the profit during a bull
market is 11.2% while keeping the draw-down at 1.8% during
a bear market. Such a phenomenon verifies the mathematical
proofs related to asymptotic solvency, ensuring that a control-
theoretic actuator can theoretically guarantee that a protocol
will not default regardless of the collapse of the revenue.
Finally, this research proposes a paradigm shift for token en-
gineering based on the transition from discretionary monetary
policies to control systems. The state-of-the-art approaches
based on “bang-bang” threshold policies or DAO votes have
a reaction time and mathematical certainty that is insufficient
for handling high-frequency processes on the markets. The
research closes the gap between macroeconomic theories and
smart contract implementation by implementing the Taylor
rule and PID control on the blockchain. The outperformance of
the PID-Cert model suggests that future research on DePIN to-
kenomics should focus on structural constraints like Lipschitz
continuity and saturation levels instead of complex models that
could turn out to be sensitive to distributional changes.
VIII. LIMITATIONS
The underlying assumption of the mechanism from a the-
oretical standpoint is based on simplifying market dynamics
to linear models, thereby limiting its application in light of
extreme non-linear scenarios. The authors linearize plant dy-
namics around a selected operating point to make control sys-
tem design tractable, implying a linear assumption of buybacks
in relation to overall liquidity levels. Such a simplification is
inherently bound to system stability based on the mechanics
of a Constant Product Market Maker (CPMM), in a manner
consistent with the conditionx·y=K. Consequently, the
system is exposed to a ”Whale in a Puddle” risk where stability
regions scale inversely with liquidity; as liquidity decreases,
the plant gain approaches infinity, inevitably causing static-
parameter controllers to enter oscillatory instability or “ring-
ing” without manual intervention.
The integration of deterministic control loops into per-
missionless blockchain systems brings about specific game-
theoretic risks that are inadequately mitigated by traditional
control system designs. Because of the transparent nature of
the control logic, Maximal Extractable Value (MEV) actors
are able to reverse-engineer the control system’s thresholds and
manipulate the system with “Fishing” or “Flash Crash” attacks.
While countermeasures are provided by the authors, they
themselves recognize that without specific hardening against
Certified Robustness requirements such as Lipschitz values
and saturation levels, a standard unhardened Proportional-
Integral-Derivative (PID) control system is still at risk of
optimization attacks with a failure rate of 94.1% for PGD-
Sustained attacks.

---

## Page 12

Implementing sophisticated control theory on the Ethereum
Virtual Machine (EVM) imposes severe computational con-
straints that force trade-offs between precision and cost. The
authors face a “Gas Cost Impossibility” regarding floating-
point arithmetic and transcendental functions, which are pro-
hibitively expensive to calculate directly on-chain. To make the
mechanism economically viable, the design must rely on fixed-
point arithmetic, lookup tables, and Taylor series expansions
to approximate necessary calculations like natural logarithms
. Even with these optimizations, the controller targets an
execution cost of approximately150,000gas, representing a
non-trivial overhead for high-frequency deployment.
However, the validation of the mechanism is still limited to
simulations on a theoretical level rather than implementation
on a mainnet. The findings are obtained from agent-based
modeling with the use of synthetic jump diffusion processes
and historical data to simulate market shocks and demands.
While these simulations have shown improvements over the
current baselines, it has been clearly shown in the study
that the current implementation does not have the capability
for adaptive gain scheduling for the verification of control
parameters on-chain. As such, the system could potentially
have issues with self-correcting its parameters based on market
changes.
IX. CONCLUSIONS
The economic infrastructure that the democratization of AI
is based on is as solid as the cryptographic infrastructure that
supports it. In the context of the current study, the Dynamic-
Control Buyback Mechanism (DCBM) is proposed, which is
a new control theory-based approach that aims to regulate the
economic system of AI and control the token emission based
on the dynamics of the market, and therefore, address the
fundamental problem of distinguishing organic growth from
speculation without the need for intermediation.
Results from comprehensive agent-level simulations show
that a stabilized economic layer is necessary for robust
physical infrastructure. The DCBM delivers statistically sig-
nificant price volatility and churn improvement compared
with industry-standard baselines, thus ensuring a predictable
environment for computational service providers. In addition
to this, it delivers improved capital efficiency by effectively
building up reserves during periods of peak demand to safe-
guard against periods of low economic activity. The DCBM
thus displays a counter-cyclical trait that fixed rate models
lack.
However, apart from the issue of macro-stability, it is clear
that the importance of adversarial robustness in permissionless
financial networks has been underlined. On a comparison of
defensive strategies, it has been found that while learning
algorithms provide certain gains, only structural constraints
such as Certified Robustness provide the necessary mathe-
matical assurance for resistance to game-theoretical attacks.
Future work will build upon this by looking into adaptive gain
scheduling for verification of control values on-chain.
REFERENCES
[1] J. Zarrinet al., “Toward decentralized intelligence: A systematic litera-
ture review of blockchain-enabled ai systems,”AI, vol. 5, no. 2, p. 23,
2024.
[2] L. W. Cong, Y . Li, and N. Wang, “Tokenomics: Dynamic adoption and
valuation,” Tech. Rep. 27222, National Bureau of Economic Research,
2020.
[3] Reflexivity Research, “The state of depin,” 2024. Accessed: 22 Decem-
ber 2025.
[4] D. W. E. Allen, C. Berg, and S. Davidson, “Buyback and burn
mechanisms: Price manipulation or value signalling?,”SSRN Electronic
Journal, 2022.
[5] R. Sams, “A note on cryptocurrency stabilisation: Seigniorage shares,”
2015.
[6] S. O. Yese, S. Berri, and A. Chorti, “Novel slice admission control
scheme with overbooking and dynamic buyback process,” in2023 IEEE
Conference on Network Function Virtualization and Software Defined
Networks (NFV-SDN), pp. 1–7, 2023.
[7] S. Kou, “A jump diffusion model for option pricing,”American Finance
Association Meetings (AFA), 2001.
[8] S. Kampakis, “Three case studies in tokenomics,”The Journal of The
British Blockchain Association, vol. 1, no. 2, 2018.
[9] R. Carvalho, “Tokenomics designs and their parallels in traditional
finance,”Journal of International Financial Markets, 2022. Preprint
available online.
[10] E. Waisanen and E. Wood, “Hydro finance: Evolving the amm model
past pre-money speculation with sustainable incentives and independent
liquidity,” tech. rep., Hydro Finance, Apr. 2022. accessed Dec 2025.
[11] monet-supply, “stkmkr: Maker staking and tokenomics revision,” 2022.
MakerDAO Forum. Accessed Jan 2026.
[12] STEPN Official, “Stepn announces q2 profits & initiates quarterly gmt
buyback & burn,” 2022. Medium. Accessed Jan 2026.
[13] PancakeSwap, “Cake tokenomics,” 2023. PancakeSwap Documentation.
Accessed Jan 2026.
[14] Polkadot Wiki, “Treasury,” 2023. Polkadot Documentation. Accessed
Jan 2026.
[15] P. Garvey, “Token design and use case,” inBlockchain Fundamental
Analysis for Digital Asset Investors: A Guide to Minimizing Risk and
Maximizing Returns, pp. 327–357, Springer, 2025.
[16] S. Sharma, “Exploring the future of ai agents in crypto,”Outlook, vol. 1,
p. 1, 2024.
[17] M. Woodford, “The taylor rule and optimal monetary policy,”American
Economic Review, vol. 91, no. 2, pp. 232–237, 2001.
[18] J. Bullard and K. Mitra, “Learning about monetary policy rules,”Journal
of monetary economics, vol. 49, no. 6, pp. 1105–1129, 2002.
[19] K. Aoki, K. Nikolov, F. Canova, and V . Chari, “Rule-based monetary
policy under central bank learning [with comments],” inNBER Inter-
national Seminar on Macroeconomics, vol. 2004, pp. 145–195, The
University of Chicago Press Chicago, IL, 2004.
[20] R. J. Hawkins, J. K. Speakes, and D. E. Hamilton, “Monetary policy
and pid control,”Journal of Economic Interaction and Coordination,
vol. 10, no. 1, pp. 183–197, 2015.
[21] I. Lebedeva, D. Umnov, Y . Yanovich, I. Melnikov, and G. Ovchin-
nikov, “Dynamic fee for reducing impermanent loss in decentralized
exchanges,”arXiv preprint arXiv:2506.03001, 2025.

---
