# Gow_2021_UncertaintyQuantificationAndPropagationThroughComplexChainsOfComputationalModels.pdf

## Page 1

UNIVERSITY OF SOUTHAMPTON
Faculty of Engineering and Physical Sciences
EPSRC Centre for Doctoral Training in Next Generation Computational
Modelling
Uncertainty quantiﬁcation and
propagation through complex
chains of computational models
by
Stephen Gow
Thesis submitted for the degree of Doctor of Philosophy
January 2021

---

## Page 3

UNIVERSITY OF SOUTHAMPTON
ABSTRACT
FACULTY OF ENGINEERING AND PHYSICAL SCIENCES
EPSRC Centre for Doctoral Training in Next Generation Computational Modelling
Doctor of Philosophy
Uncertainty quantiﬁcation and propagation through complex chains of computational
models
by Stephen Gow
There are many ﬁelds in which it is of interest to make predictions from a chain of
computational models or simulators, in which the output of one simulator in the chain
forms one of the inputs to the next simulator. In order to make reliable predictions from
the chain, it is necessary to understand how uncertainty in the individual models will
propagate through the chain. Each simulator will often be computationally intensive,
and for computational feasibility must be approximated; we use a Gaussian process
emulator to do this. This thesis focuses on a “linked” emulator, in which each model is
emulated separately and the emulators are linked to make predictions from the chain
as a whole.
We present two methods to make predictions from a chain of linked emulators. Both
have precedent in previous research, but are fully formalised and extended in our work.
One method uses simulation and Monte Carlo integration to make empirical predictions
from the chain; this is extremely ﬂexible and can be applied to a wide class of emulators,
but can be computationally intensive and is open to Monte Carlo error. The second
method uses theoretical results for the mean and variance of the linked emulator under
certain restrictive conditions on the emulators of the individual models in the chain;
this is fast and provides exact or near-exact results, but is possible only for a very
limited set of emulators.
Related problems include experimental design and sensitivity analysis for chains of
models. We present an algorithm for single-stage design, and discuss approaches to
sequential design strategies. We also propose methods for sensitivity analysis on the
ﬁnal model of a chain, and develop techniques towards sensitivity analysis for the chain
as a whole.
The above methodology is demonstrated on a chain to assess the impact of a chemical,
biological or radiological release which combines a model for atmospheric dispersion
with a model for the probability of casualty.

---

## Page 5

Contents
Declaration of Authorship ix
Acknowledgements xi
Glossary of symbols xiii
1 Introduction 1
2 Emulation 7
2.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Gaussian Process emulation . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Unknown parameters of the Gaussian process emulator . . . . . . . . . . 17
2.3.1 Plug-in approach . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.3.2 Markov chain Monte Carlo . . . . . . . . . . . . . . . . . . . . . 20
2.4 Extensions of the GP emulator . . . . . . . . . . . . . . . . . . . . . . . 24
2.5 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3 Emulation for chains of multiple models 29
3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.2 Approximating the linked emulator output by Monte Carlo integration . 33
3.3 The mean and variance of the linked emulator . . . . . . . . . . . . . . . 35
3.4 Extending the simulation-based linked emulator to longer chains . . . . 42
3.5 Extending the theoretical linked emulator to longer chains . . . . . . . . 43
3.6 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
4 Experimental design for chains of multiple models 49
4.1 Review of existing methods for experimental design . . . . . . . . . . . . 49
4.2 Single-stage design for chains of emulators . . . . . . . . . . . . . . . . . 53
4.3 Sequential design for chains of emulators . . . . . . . . . . . . . . . . . . 58
4.4 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
5 Sensitivity analysis 63
5.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
5.2 Probabilistic sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . 64
5.3 Sensitivity analysis using emulation . . . . . . . . . . . . . . . . . . . . . 68
iii

---

## Page 6

5.4 Practical issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
5.5 Example: CBR modelling . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.6 Sensitivity analysis for multiple models . . . . . . . . . . . . . . . . . . . 86
5.6.1 Sensitivity analysis for the ﬁnal model in a chain with respect to
the model’s inputs . . . . . . . . . . . . . . . . . . . . . . . . . . 86
5.6.2 Sensitivity analysis for the ﬁnal output of a chain with respect to
the controllable inputs . . . . . . . . . . . . . . . . . . . . . . . . 89
5.7 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
6 Software implementation 95
6.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
6.2 Details of usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
6.2.1 Prediction from a linked emulator using simulation . . . . . . . . 96
6.2.2 Prediction from a linked emulator using the theoretical method . 97
6.2.3 Sensitivity analysis for the ﬁnal model in a chain . . . . . . . . . 98
6.2.4 Sensitivity analysis for the output of a chain in terms of the
directly controllable inputs . . . . . . . . . . . . . . . . . . . . . 100
6.3 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7 Application: casualty prediction from a CBR release 109
7.1 Dispersion model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
7.2 Casualty model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7.3 Prediction from the chain . . . . . . . . . . . . . . . . . . . . . . . . . . 114
7.3.1 Direct simulation on the dose-response model . . . . . . . . . . . 115
7.3.2 Composite emulator . . . . . . . . . . . . . . . . . . . . . . . . . 116
7.3.3 Theoretical linked emulator . . . . . . . . . . . . . . . . . . . . . 118
7.3.4 Simulation-based linked emulator . . . . . . . . . . . . . . . . . . 120
7.4 Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
7.5 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
8 Simulation study 127
8.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
8.2 Simulation setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
8.3 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
9 Conclusions and future work 135
9.1 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
9.2 Future work: experimental design . . . . . . . . . . . . . . . . . . . . . . 136
9.3 Future work: sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . 137
9.4 Future work: other areas . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
Bibliography 150
iv

---

## Page 7

List of Figures
1.1 Chain of models for casualty prediction for a CBR release . . . . . . . . 3
2.1 GP emulator in one dimension . . . . . . . . . . . . . . . . . . . . . . . 16
3.1 Diagram of a chain of two models . . . . . . . . . . . . . . . . . . . . . . 30
3.2 Prediction from the ﬁrst two-model example chain . . . . . . . . . . . . 34
3.3 Prediction from the second two-model example chain - theoretical method 42
3.4 Prediction from the second two-model example chain - simulation method 43
3.5 Prediction from the three-model example chain - simulation method . . 44
3.6 Prediction from the three-model example chain - theoretical method . . 47
4.1 Example maximin Latin hypercube design . . . . . . . . . . . . . . . . . 50
4.2 Experimental design eﬀect on prediction in a three-model chain . . . . . 55
4.3 A two-model chain with space-ﬁlling design on model 1 but not on model 2 56
4.4 Prediction from the new three-model chain with space-ﬁlling designs at
each stage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.5 Variance of the linked emulator for y2 given x1,1 and x2,1 under the ﬁrst
initial design. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.6 Variance of the linked emulator for y2 given x1,1 and x2,1 under the
second initial design. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
5.1 Posterior expectation of Y given each xi in the test example . . . . . . . 74
5.2 Posterior expectation of Y given each xi in the full CBR model . . . . . 76
5.3 ±2 s.d. bounds on E(Y |x6) in the full CBR model . . . . . . . . . . . . 77
5.4 Contour plot of E(Y ) against x1 and x6 in the full CBR model . . . . . 78
5.5 E(Y |xi) for each xi in the full CBR model with new input distributions 79
5.6 Contour plot of E(Y ) against x1 and x6 with new input distributions . . 80
5.7 E(Y |xi) for each xi in the CBR model with ﬁxed radius . . . . . . . . . 81
5.8 ±2 s.d. bounds on E(Y |x1) iwith ﬁxed radius . . . . . . . . . . . . . . . 82
5.9 ±2 s.d. bounds on E(Y |x3) with ﬁxed radius . . . . . . . . . . . . . . . 82
5.10 Contour plot of E(Y ) against x1 and x3 with ﬁxed radius . . . . . . . . 83
5.11 E(Y |xi) for each xi with ﬁxed radius and new input distributions . . . . 84
5.12 Contour plot of E(Y ) against x1 and x3 with ﬁxed radius and new input
distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
v

---

## Page 8

5.13 Contour plot of E(Y ) against x1 and x2 with ﬁxed radius and new input
distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.14 Contour plot of E(Y ) against x2 and x3 with ﬁxed radius and new input
distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
5.15 E(y3|y2) and E(y3|x3,1) in a simple three-model chain . . . . . . . . . . 87
5.16 E(y2|x1,1) and E(y2|x2,1) in a two-model chain . . . . . . . . . . . . . . 91
7.1 HYSPLIT output at the 20 design points against release rate . . . . . . 110
7.2 HYSPLIT output at the 20 design points against release duration . . . . 111
7.3 HYSPLIT output at the 20 design points against release time . . . . . . 111
7.4 Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release rate . . . . . . . . . . . . . . . . . . . . . . . . . . 112
7.5 Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release duration . . . . . . . . . . . . . . . . . . . . . . . 112
7.6 Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release time . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7.7 Mean prediction of probability of casualty at the prediction points against
release rate, duration, time and D50 - direct simulation model . . . . . . 116
7.8 Prediction variance of probability of casualty at the prediction points
against release rate, duration, time and D50 - direct simulation model . 117
7.9 Mean prediction of probability of casualty at the prediction points against
release rate, duration, time and D50 - composite emulator . . . . . . . . 118
7.10 Prediction variance of probability of casualty against D50 - composite
emulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
7.11 Mean prediction of probability of casualty at the prediction points against
release rate, duration, time and D50 - linked emulator, theoretical method120
7.12 Mean prediction of probability of casualty at the prediction points against
release rate, duration, time and D50 - linked emulator, theoretical method121
7.13 Prediction variance of probability of casualty against D50 for both linked
emulators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
7.14 Posterior expectation of probability of casualty given the two inputs to
the dose-response model. . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
7.15 Posterior expectation of probability of casualty given each input to the
linked emulator. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
vi

---

## Page 9

List of Tables
4.1 Initial experimental design for the three-model example. . . . . . . . . . 54
4.2 Experimental design for the three-model example using Algorithm 2. . . 58
5.1 Assumed ranges and units for the inputs to the CBR model . . . . . . . 75
5.2 Estimates of ˆSi for each input in the full CBR model . . . . . . . . . . . 76
5.3 Estimates of ˆSi,j for each pair of inputs in the full CBR model . . . . . 77
5.4 Estimates of each ˆSi with new input distributions . . . . . . . . . . . . . 79
5.5 Estimates of each ˆSi,j with new input distributions . . . . . . . . . . . . 79
5.6 Estimates of ˆSi for each input in the CBR model with ﬁxed radius . . . 80
5.7 Estimates of each ˆSi,j with ﬁxed radius . . . . . . . . . . . . . . . . . . 81
5.8 Estimates of each ˆSi with ﬁxed radius and new input distributions . . . 83
5.9 Estimates of each ˆSi,j with ﬁxed radius and new input distributions . . 83
7.1 Ranges and units for the inputs of interest to the HYSPLIT model . . . 110
8.1 Experimental design for the complete chain of models for the composite
emulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
8.2 Experimental design for the ﬁrst model in the chain for the linked emulator130
8.3 RMSE and coverage for the simulation (S) and theoretical (T) linked
emulators, for the composite emulator (C), and for the linear regression
model (L). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
vii

---

## Page 10

viii

---

## Page 11

Declaration of Authorship
I, Stephen Gow, declare that the thesis entitled “Uncertainty quantiﬁcation and prop-
agation through complex chains of computational models” and the work presented in
the thesis are both my own, and have been generated by me as the result of my own
original research. I conﬁrm that:
• this work was done wholly or mainly while in candidature for a research degree
at this University;
• where any part of this thesis has previously been submitted for a degree or any
other qualiﬁcation at this University or any other institution, this has been clearly
stated;
• where I have consulted the published work of others, this is always clearly at-
tributed;
• where I have quoted from the work of others, the source is always given. With
the exception of such quotations, this thesis is entirely my own work;
• I have acknowledged all main sources of help;
• where the thesis is based on work done by myself jointly with others, I have made
clear exactly what was done by others and what I have contributed myself;
• none of this work has been published before submission.
Signed:
Date:
ix

---

## Page 12

x

---

## Page 13

Acknowledgements
First and most importantly, I wish to thank my main supervisor, Professor David
Woods, for his advice and guidance during the course of this PhD. Completing this
thesis would not have been possible without the time and eﬀort he provided to point
me in the right direction, which must have required an extraordinary amount of patience
at times. Thank you also to my secondary supervisor Jon Forster for his support, and
to all those in the Mathematics department and in particular Southampton’s design
group who provided much-needed help.
I am also grateful to the team behind the Centre for Doctoral Training in Next Gen-
eration Computational Modelling (NGCM) - in particular Hans Fangohr, Ian Hawke
and Susanne Ufermann - whose help during the taught year of the PhD and beyond
made the coding side of my research much less daunting.
I must also acknowledge the Engineering and Physical Science Research Council
(EPSRC) and the Defence Science and Technology Laboratory (Dstl) for the funding
contributions that made this project possible. Special thanks to Veronica Bowman and
Paul Westoby of Dstl, who provided valuable advice and assistance with the real-life
applications of our work.
Finally, I would like to thank my family and friends for their support over the years.
xi

---

## Page 14

xii

---

## Page 15

Glossary of symbols
Symbol Meaning
y Output of a single-output computational model
q Number of inputs to a computational model
xq Input q to a computational model
x = (x1, x2, ..., xq)T Vector of inputs to computational model
η(x) Model function (simulator) for computational model
Rq q-dimensional real number space
X Space on which the model inputs are deﬁned (subset of Rq)
n Number of design points for a computer experiment
ξ = (x1, ...,xn)T Experimental design with n design points
y1, ..., yn Outputs of a computer experiment with n design points
Z(x) Gaussian process
k Dimension of any subset of X in GP deﬁnition
µz(x) Mean function of a Gaussian process
Cz(x1, x2) Covariance function of a Gaussian process
h = x1 − x2 Vector of distance between two points
C(h) Stationary covariance function of a GP
σ2
z (Constant) process variance of a GP
R(h) = C(h)/σ2
z Correlation function of a GP
bj Scale parameter of power-exponential correlation function in
dimension j
α Shape parameter of power-exponential correlation function
θj Scale parameter of Mat´ ern correlation function in dimensionj
ω Smoothness parameter of Mat´ ern correlation function
p Number of regression terms in GP emulator
f(x) = [f1(x), ..., fp(x)] Vector of regression functions for GP emulator
β = (β1, ..., βp)T Vector of regression coeﬃcients for GP emulator
µ Mean of ordinary GP emulator
xn+1 New input vector at which we wish to predict from GP emu-
lator
Yn+1 Unknown simulator output at new input vector
Yn Vector of results of a computer experiment
xiii

---

## Page 16

F Matrix of regression functions for the elements of ξ
fn+1 Vector of regression functions for xn+1
C Matrix of correlations among the elements of ξ
cn+1 Vector of correlations between xn+1 and ξ
θ = (θ1, ..., θq)T Vector of correlation parameters
b0 Mean of normal prior on β|σ2
z or β
V0 Variance matrix of normal prior on β|σ2
z or β
ν0 Degrees of freedom of scaled-inverse-chi-squared prior on σ2
z
c0 Parameter used in deﬁnition of scaled-inverse-chi-squared prior
on σ2
z
T1 Univariate non-standardised t-distribution
ν Degrees of freedom of non-standardised t-distribution
µ Location parameter of multivariate non-standardised t-
distribution
Σ2 Scale parameter matrix of multivariate non-standardised t-
distribution
ν∗ Scale parameter of non-standardised t-distribution for predic-
tion from GP emulator
µ∗ Location parameter of normal or non-standardised t-
distribution for prediction from GP emulator
σ∗2 Scale parameter of normal or non-standardised t-distribution
for prediction from GP emulator
ˆβ Posterior estimate for an unknown β
τ 2 Parameter used in deﬁnition of Normal prior on β
δ Nugget of a GP emulator
I Identity matrix
ˆσ2
z Maximum likelihood estimator for σ2
z
S State space of a Markov chain
A Subset of S
θ(j) Value of θ in a Markov chain after j timesteps have elapsed
ψ State of a Markov chain
φ State of a Markov chain not equal to ψ
π Stationary distribution of a Markov chain
M Monte Carlo sample size
t(θ) Function of θ we wish to approximate using Markov chain
Monte Carlo sample
t′
M Approximation to t(θ) of size M
D(θ) Target distribution of a Markov chain Monte Carlo simulation
q(ψ) Transition kernel in a Markov chain Monte Carlo simulation
wj Movement term in a random walk transition kernel
fw Probability density function of wj
xiv

---

## Page 17

fD(θ) Function proportional to target density D(θ)
Θ Sample matrix from D(θ) obtained using Markov chain Monte
Carlo
λi ith eigenvalue of a matrix Λ
yk Output of model k in a chain of models
qk Number of inputs to model k in a chain, excluding those which
depend on a previous model
˜ xk = (xk,1, ..., xk,qk)T Vector of inputs to model k in a chain, excluding inputs which
depend on a previous model
ηk(˜ xk, yk−1) Model function (simulator) for model k in a chain
βk Vector of regression coeﬃcients for GP emulator of model k in
a chain
σ2
z,k Process variance of GP emulator of model k in a chain
θk Vector of correlation parameters for GP emulator of model k
in a chain
Fk Matrix of regression functions at the design points for model k
in a chain
Ck Matrix of correlations among the design points for model k in
a chain
Yn,k Vector of results of a computer experiment for model k in a
chain
˜ xk,n+1 Vector of directly controllable inputs to model k at an untested
input conﬁguration
xk,n+1 Vector of inputs to model k in a chain at an untested input
conﬁguration
fn+1,k Vector of regression functions for xk,n+1
cn+1,k Vector of correlations between xk,n+1 and the design points for
model k
f∗(y2) Product of conditional densities for y1 and y2 in a two-model
linked emulator
d(xi, xj) Distance between the points xi and xj in χ
φMm(ξ) Maximin distance design criterion
φmM(ξ) Minimax distance design criterion
Ck,l(ξ) Coverage design criterion for parameters k and l
S Set of candidate points in χ
nk Number of design points in computer experiment for model k
in a chain
ξk Experimental design for model k in a chain
Lk Matrix of limits for controllable inputs to model k in a chain
Ly,k Vector of length 2 containing limits foryk−1 based on simulator
runs at points in ξk−1
xv

---

## Page 18

ynew
1 Value of y1 at a newly added design point in ˜ x1 in sequential
experimental design
κ Set of indices in q
xκ Subvector of x containing the elements with indices in κ
x−κ Subvector of x containing elements with indices not in κ
G(x) Probability distribution for x
E(Y |xκ) Expectation of model output when the inputs in the subvector
xκ are ﬁxed
zi(xi) Main eﬀect of input xi
zi,j(xi,j) Second-order interaction between the inputs xi and xj
Vκ Expected reduction in the variance of Y when xκ is ﬁxed
Sκ Sobol’ index for subset of inputs xκ
VTκ Expected uncertainty when all inputs other than xκ are ﬁxed
STκ Total eﬀect index for subset of inputs xκ
Gκ(xκ) Marginal distribution of xκ
G−κ|κ(x−κ|xκ) Conditional distribution of x−κ given xκ
EEi Elementary eﬀect of input xi
ρ Number of levels in the discretisation of the input space for
elementary eﬀect analysis
∆ Value in the set
[
1
ρ−1 , 2
ρ−1 , ...,1 − 1
ρ−1
]
used in elementary ef-
fects analysis
µ∗
i Measure of the sensitivity of Y to the input xi using elementary
eﬀect analysis
χκ Design space of the inputs xκ
χ−κ Design space of the inputs x−κ
Rκ(xκ) Integral of fn+1 with respect to G−κ|κ(x−κ) across χ−κ
Tκ(xκ) Integral of cn+1 with respect to G−κ|κ(x−κ) across χ−κ
R Special case of Rκ(xκ) where κ is the empty set
T Special case of Tκ(xκ) where κ is the empty set
R∗(x, x′) Posterior correlation between x and x′
υ Set of indices in q which are not identical to κ
Uκ,υ(xκ, x′υ) Integral of R∗(x, x′) with respect to the conditional distribu-
tions of two distinct sets of unknown inputs
E Triple integral of the product µ∗(x)µ∗(x∗) with respect to the
marginal distribution Gκ(xκ) and the conditional distributions
G−κ|κ(x−κ|xκ), G−κ|κ(x′−κ|x′κ)
M Monte Carlo sample size
Sκ(xκ) Distribution used in importance sampling for Gκ(xκ)
S−κ|κ(x−κ|xκ) Distribution used in importance sampling for G−κ|κ(x−κ|xκ)
Cov∗(Y2, Y′
2) Covariance between two independent realisations of a two-
model linked emulator given the directly controllable inputs
xvi

---

## Page 19

c∗(Y2, Y′
2) Covariance between two independent realisations of a two-
model linked emulator given all inputs
xvii

---

## Page 20

xviii

---

## Page 21

Chapter 1
Introduction
A computational models is a complex mathematical model implemented via a com-
puter program to simulate a real-life process. Computational models are commonplace,
being used in “almost all ﬁelds of science and technology” according to O’Hagan (2006).
The method of constructing a mathematical model for a real process predates comput-
ers, and allows the modeller to gain insight into the behaviour of the process without
the need for potentially diﬃcult or expensive real-world testing. Implementing the
model as a computer program allows more complex models to be considered than could
be done by hand. In this thesis, we consider computational models which return a
single output value, which we call y. A single-output model may nonetheless depend
on multiple inputs, say q, which we group into a vector x = (x1, x2, ..., xq)T . We work
with models of the form
y = η(x) ,
where η(x) is a deterministic function. The model function η(x) is the core of the
computational model itself. Following the terminology of O’Hagan (2006), we call the
model a simulator. This form of model does not include a random term; the output
y is entirely determined by the inputs x and the function η(x), so the same output is
obtained any time the model is run with the same inputs. Uncertainty in the simulator
output thus arises only from uncertainty in its input variables.
These restrictions on the type of model we work with are somewhat limiting, as
a deterministic model with a single output will not always be an appropriate choice.
For some real-life applications, computational models with multiple outputs are more
useful than single-output models. These will be not be dealt with here. Additionally,
it is highly unlikely that a computational model is exactly equivalent to the real-life
process it is designed to replicate, so a deterministic model is not necessarily the best
approximation. A model which attempts to quantify the uncertainty in its own out-
put via a probability distribution may provide a better reﬂection of the real process
being modelled. Despite this, deterministic models are widely used across many appli-
cation areas, and form the basis of a large body of statistical literature on the topic of
1

---

## Page 22

computational models.
When the behaviour of a process across the entire space of its inputs is of interest,
the simulator must be run many times for diﬀerent input conﬁgurations. This can be
computationally infeasible if the simulator is expensive to run. Computer experimen-
tation provides a solution to this: the simulator is run for a few input conﬁgurations,
called training or design points, and the outputs are treated as data from an exper-
iment, which is then used to construct a statistical approximation to the simulator.
The approximation is called an emulator, and the technique - which was ﬁrst applied
to computational models by Sacks et al. (1989) - is called emulation. Predictions at
other inputs can then be made quickly from the emulator. This approach does however
introduce uncertainty into the predictions made; to quantify this, the emulator returns
a probability distribution instead of a single value. Analysis of uncertainty in the com-
putational model must thus take account of not only the uncertainty arising from the
inputs, but also the uncertainty in the emulator at input conﬁgurations where the sim-
ulator has not been run directly. The most common emulator uses a combination of
a regression model and a stationary Gaussian process to approximate the simulator.
Emulation for a single model is discussed in Chapter 2.
The overall aim of this thesis is to explore how predictions can be made and assessed
through chains of computational models, in which the output of one model in the chain
is then used as an input (potentially one of several) to the next model until a ﬁnal model
is reached. The models may be extremely complex and computationally intensive, so
emulation will be required. Each link in the chain is thus subject to two sources of
uncertainty: uncertainty arising from the inputs to the model, and uncertainty arising
from the emulator. These individual sources of uncertainty will propagate and combine
through the model chain, aﬀecting our ability to understand and quantify the reliability
and accuracy of overall predictions from the full chain.
Motivation for the project comes from the multi-modal chains of computational mod-
els used by our research partners, the Defence Science and Technology Laboratory
(Dstl), for hazard prediction and management. For example, consider the prediction
of casualties from a chemical, biological or radiological (CBR) release. An illustration
of this process can be seen in Figure 1.1. One output of interest is the probability of ca-
sualty for an aﬀected individual. This output depends on several linked processes which
would each need to be approximated by separate models which would then be linked
together. The probability of casualty is a function of the properties of the released con-
taminant and the dosage received by the individual; this would constitute ﬁnal model in
the chain. The dosage received is itself a function of several other variables determining
how the contaminant reaches the individual following its release. These variables could
include the location of the release, the release mass and duration, and the wind speed
and direction both at and after the time of release. At least one further model would
be needed to capture this variation, and potentially another to account for changes
2

---

## Page 23

in meteorological conditions across time. For a fuller picture of the eﬀects of such a
release on the population as a whole, the probability of casualty at each location in
the potentially aﬀected area would itself be an input into a ﬁnal model for the number
of casualties due to the release. This model could also include other variables such as
the population density at each location, placement of sensors to detect the release and
factors relating to the strategy chosen to mitigate the eﬀects of the release, allowing
the eﬀects of diﬀerent mitigation strategies to be modelled.
Figure 1.1: Diagram of the steps in a chain of models to predict the casualties from a
CBR release. (Source: Dstl)
There are two alternative methods by which emulation for chains of models can be
conducted. The ﬁrst is to approximate the entire chain via a single emulator, referred
to in previous work on the topic as the composite emulator. This has the advantage of
in eﬀect reducing the problem to one which has already been solved, as the theory for
single-model emulation is extremely well-developed. However, if the input space of the
chain of models is large, this approach may be computationally expensive; knowledge of
the chain of models eﬀectively deﬁnes a form of dimension reduction on the full chain.
Additionally, information can be lost by performing only one emulation, both in terms
of understanding the behaviour of subsets of the models in the chain and - as in an
example in the work of Kyzyurova et al. (2018) - in terms of the performance of the
composite emulator.
The second approach, which is taken during our work, is to emulate each model
independently and link the results together to produce a ﬁnal approximation called the
linked emulator. This introduces additional challenges, since one of the inputs to the
later models in the chain is not known exactly but only up to a probability distribution.
Approaches exist to deal with this uncertainty for a chain of two models using either
Monte Carlo methods (Kyzyurova et al., 2018) or theoretical results concerning inputs
to a Gaussian process emulator which follow a normal distribution (Candela et al.,
2003; Kyzyurova et al., 2018). Chapter 3 reviews the existing methods and extends
them to chains of more than two models.
3

---

## Page 24

There is a relationship between this approach and the ﬁeld of deep Gaussian pro-
cesses. A deep Gaussian process is a form of neural network based on a Gaussian
process prior distribution, with its origins in the work of Neal (1996), Chapter 2, which
focuses on priors for Bayesian neural network. More recently, Damianou and Lawrence
(2013) developed a framework for deep learning in which the observed data is treated as
the output of a multivariate Gaussian process, and the inputs to this Gaussian process
are themselves controlled by another Gaussian process. This can be thought of a form
of latent variable modelling in which the Gaussian process controlling the inputs to the
second Gaussian process adds an additional layer of understanding to the behaviour
of the system as a whole. Damianou and Lawrence (2013) go on to use variational
marginalisation to remove all of the intermediate layers from the system, with some
level of approximation required to do this.
The structure of this hierarchy can be viewed as similar to that of a chain of models.
There are however some noteworthy diﬀerences between the deep Gaussian process
setup and the chain of models as deﬁned in this thesis. Firstly, each model in a chain
takes only one input as an output from a previous model, instead of an entire layer at a
time being deﬁned through latent variables. More importantly, every input and output
to any model in the chain corresponds directly to a quantity of interest, and their
deﬁnition comes directly from the real-world process being modelled. The number
of intermediate inputs is ﬁxed by the nature of the problem. In a deep Gaussian
process, the latent variables are typically artiﬁcial, and the number of intermediate
inputs can be chosen for the purposes of improving predictive performance. Our work
is nonetheless similar in spirit to the method of Damianou and Lawrence (2013), but
diﬀers signiﬁcantly in its approach.
A further problem of interest is that of how the design points for the chain of computer
experiments required to build each emulator should be chosen. There is a large body
of theory for how this can be done for a single model. One popular approach is space-
ﬁlling design, in which the points are chosen to ﬁll the input space based on either a
Latin hypercube principle (McKay et al., 1979), or to satisfy an optimality criterion
based on the distances between the points (Johnson et al., 1990). A second method
is sequential design, in which the model is run for a reduced set of design points and
the remaining points are allocated using information gained from the runs which have
already been made (Sacks et al., 1989; Gramacy and Lee, 2009). Extending either
of these methods to models in a chain faces challenges not seen in the single-model
case. Both the existing methods and our proposals for experimental design for chains
of models are discussed in Chapter 4.
The quantiﬁcation and understanding of uncertainty in statistical models forms the
basis of the ﬁeld of sensitivity analysis. When applied to a deterministic model, sensi-
tivity analysis is based upon apportioning the uncertainty in the simulator output to its
inputs (Saltelli et al., 2008). Several techniques exist to do this; the approaches we are
4

---

## Page 25

most interested in are based on decomposing the model into a sum of the main eﬀects
of each input and the interactions between them, and on quantifying the eﬀect of each
input (or set of inputs) in terms of the proportion of the total output variance explained
by the input(s). However, traditional sensitivity analysis relies on an extremely large
number of model runs at diﬀerent input conﬁgurations, so it is often necessary to use
emulation to build an approximation to the simulator for sensitivity analysis to proceed
(Oakley and O’Hagan, 2004). Sensitivity analysis for a chain of emulators is thus of
interest. Chapter 5 focuses on both existing methods for sensitivity analysis for a single
model, including an example from Dstl based on CBR modelling, and their potential
extensions to the case of a chain.
The methods developed in the early chapters of the report are implemented in the
R programming language, with some use of C++ for reasons of execution speed. Our
code includes functions for prediction from linked emulators using both the theoretical
and the Monte Carlo method, methods for sensitivity analysis for the ﬁnal model of a
chain given its own inputs, and some limited sensitivity analysis for the output of the
chain with respect to the directly controllable inputs. This software implementation is
introduced in Chapter 6.
The techniques we present for prediction and analysis of chains of computational
models are demonstrated on a real-life example from Dstl in Chapter 7. The study
concerns a chain of two models for dispersion and casualty estimation from a CBR
release. We construct a linked emulator for the chain using both the Monte Carlo and
the theoretical method and review the performance of both, together with that of a
composite emulator. Sensitivity analysis for the CBR chain is also considered.
It is of interest to make comparisons between the diﬀerent methods considered in
this thesis. In Chapter 8, a simulation study is conducted to investigate the diﬀerences
in behaviour between the two forms of linked emulator and the simpler methods of a
composite emulator and linear regression, and to determine which settings the diﬀerent
approaches are best suited to. Finally, the main conclusions of our work and ideas for
relevant future research directions are presented in Chapter 9.
5

---

## Page 26

6

---

## Page 27

Chapter 2
Emulation
2.1 Overview
Emulation is a technique which attempts to reduce the time and cost associated with
prediction from a computationally expensive simulator. In theory, the output of the
simulator can be determined for any choice of inputs we wish to make; if, as we assume
to be the case throughout, the model is deterministic, this output does not change
should we run the simulator multiple times with the same inputs. In practice, for many
real-world problems the simulator is computationally expensive or time-consuming to
run, and it is therefore infeasible to perform a large number of runs of the simulator.
But there are several situations in which a large number of simulator runs would be
required. It may be necessary, for example, to make predictions at a large number of
input conﬁgurations relating to diﬀerent real-world conditions. Additionally, sensitivity
analysis for a computational model can require many thousands or even millions of
model runs; this shall be discussed further in Chapter 5.
When using the simulator directly is infeasible, the most practical alternative is to
construct an approximation to the simulator using a computer experiment. Let X ⊂ Rq
be the space on which the q inputs to the simulator are deﬁned; in the context of a
computer experiment, X is called the design space. The simulator is run at a relatively
small number of input settings, ξ = (x1, ...,xn)T , x1, ...,xn ∈ X , called design points or
training points. The (scalar) outputs, y1, ..., yn, are treated as data from an experiment.
This data is then used to build a statistical approximation to the simulator, called an
emulator, which can then be used to make predictions of the simulator output for
untested input values. The key advantage of this method is to substantially reduce the
computational cost associated with prediction from the original model.
The simulator itself is a function of its inputsx which returns a single value,y = η(x).
For a suﬃciently good approximate function ˆ η of η, it would be possible to take the
point approximation ˆy = ˆη(x) as a surrogate for y and perform any desired analysis
on this approximation. This approach is sometimes taken in previous literature: a
recent example is the work of Joseph et al., 2019 on model-based optimal experimental
7

---

## Page 28

design, where it is used due to its computational simplicity. However, this approach
does not reﬂect the fact that we cannot be sure of the accuracy of a point approximation
where the true simulator output is unknown. It is therefore preferable to quantify the
uncertainty in the estimate. For this reason, the most common emulators return a
probability distribution for the true output y given the inputs x instead of a single
value. Bayesian methodology can be used to construct an emulator from the training
data.
There are two properties which a good emulator typically obeys. At the design points,
where the true output is known, we would expect the emulator to return the known
output with probability one. Elsewhere, the probability distribution returned by the
emulator should have a mean which is a plausible estimate for the true output, and
should provide a reasonable expression of the uncertainty associated with this estimate.
The ﬁrst property can be easily checked, but the second is somewhat more diﬃcult; one
common approach, as discussed by Bastos and O’Hagan (2009), is to run the model at
some previously-untested inputs and compare the true output at these points to the
emulator output.
The most common form of emulator in use is the Gaussian process emulator, which
we discuss in Section 2.2; it is based upon a stochastic process called the Gaussian
process. This can be interpreted within a Bayesian framework: the simulator is treated
as an unknown function, with a prior distribution given by a Gaussian process. When
combined with the data obtained from the simulator runs, this leads to a posterior
distribution for the simulator output at any point. The resulting posterior distribution
is also Gaussian, with a mean and covariance which depend on both the data and the
parameters of the prior distribution.
The choice of the points at which the true model is run, called the experimental
design, is important: a well-chosen set of design points allow much more information
to be gained from the simulator runs than a poorly-chosen set. Several methods exist
to choose the points well for a single model. These are reviewed in Section 4.1 in the
context of extending the process to multiple linked models.
2.2 Gaussian Process emulation
Using the notation followed by Santner et al. (2003), let Z(x), x ∈ X , be a stochastic
process. Z(x) is a Gaussian process if Z(x1), ..., Z(xk) follows a k-dimensional multi-
variate normal distribution for any subset ( x1, ...,xk) of X . The alternative nomen-
clature Gaussian random function or Gaussian random ﬁeld is used in some literature,
but we will use the more common term Gaussian process (GP). A GP is deﬁned by its
mean function,
µz(x) = E[Z(x)] ,
8

---

## Page 29

for x ∈ X , and by its covariance function ,
Cz(x1, x2) = Cov[Z(x1), Z(x2)] ,
for x1, x2 ∈ X . Both µz and Cz may be parametric functions with an additional
dependences on unknown parameters. A covariance function is deﬁned as stationary
if, where x1 − x2 is the distance between x1 and x2, the covariance is given by
Cov[Z(x1), Z(x2)] = C(x1 − x2) ,
for some function C. For ease of notation, we write h = x1 − x2, with hj being the jth
element of the vector h. A stationary covariance function C(h) thus depends on h and
any other parameters of the function. GPs with stationary covariance functions have
many useful properties regarding inference based on data from a single sample path;
details are given by Adler (1981).
The process variance of a GP is deﬁned as
σ2
z(x) = V ar[Z(x)]
= Cov[Z(x), Z(x)] .
An additional assumption which is usually made is that the process variance is a
constant value σ2
z. This variance must be greater than zero for the GP to be non-
degenerate. For a stationary GP, the process variance can be written as
σ2
z = C(0) .
It is often more convenient, and substantially more common in the literature, to work
with the correlation function of a stationary GP instead of the covariance function. This
is deﬁned as:
R(h) = C(h)/σ2
z .
For the GP to be non-degenerate, the correlation function must satisfy R(0) = 1;
for stationarity, we additionally require that R(h) = R(−h), and that R is positive
semi-deﬁnite. It is useful to note that the product of several correlation functions with
these properties is itself a valid correlation function with the same properties. This is
referred to as separability, and means that it is possible to create multi-dimensional
correlation functions by taking the product of several independent one-dimensional
correlation functions meeting the required conditions. This is useful, as for the purposes
of building a GP emulator, the correlation function must be of dimension q, where q is
the number of inputs to the computational model.
9

---

## Page 30

Santner et al. (2003), Chapter 2, presents several families of multi-dimensional cor-
relation functions which meet the conditions required for non-degeneracy and station-
arity, of which two are of particular interest to us. The power-exponential family of
correlation functions in q dimensions has the form
R(h) = exp
(
−
q∑
j=1
bj|hj|α
)
. (2.1)
This is a parametric function: each bj > 0 is a scale parameter for the jth dimension,
while α is a shape parameter which is consistent across dimensions, and must satisfy
0 < α ≤ 2. The most commonly used value for this parameter is α = 2, the Gaussian
correlation function,
R(h) = exp
(
−
q∑
j=1
bjh2
j
)
, (2.2)
or equivalently
R(h) =
q∏
j=1
exp(−bjh2
j) .
This has been used in prior work on emulation and sensitivity analysis, notably
by Oakley and O’Hagan (2004), and is the basis of previous work on linking Gaussian
process emulators in a chain by Girard et al. (2002) and Kyzyurova et al. (2018). A
Gaussian process with this correlation function is inﬁnitely diﬀerentiable, and tends to
produce extremely smooth sample realisations (Stein, 1999).
Another common choice is the Mat´ ern correlation function, introduced in the PhD
thesis of Matern (1960), which has the form
R(h) =
q∏
j=1
1
Γ(ω)2ω−1
(2√ω|hj|
θj
)ω
Kω
(2√ω|hj|
θj)
)
, (2.3)
in q dimensions. Each θj > 0 is the jth-dimensional scale parameter. ω > 0 is a
smoothness parameter; the smoothness parameters could also be dimension-speciﬁc,
but authors such as Santner et al. (2003) use a common smoothness parameter in their
deﬁnitions. Kω is the modiﬁed Bessel function of the second kind of order ω. If ω is
an integer multiple of 1 /2, the Bessel function reduces to a much simpler form. The
most common choices for the smoothness parameter are ω = 5/2 and ω = 3/2. The
alternative ω = 1/2, which in one dimension leads to a GP which is equivalent to the
Ornstein-Uhlenbeck process, is generally too rough for computer experiments; ω ≥ 7/2
gives very smooth realisations similar to that of the squared exponential, which is
itself a limiting case of the Mat´ ern correlation function asω → ∞ per Rasmussen and
Williams (2006), Chapter 4.
For the purposes of emulation, we could use a Gaussian process to approximate a
simulator. However, more ﬂexibility is often required than can be provided by a GP
10

---

## Page 31

in isolation. This can be achieved by considering the output of the simulator as a
realisation of a stochastic process, and ﬁtting a regression model to this stochastic
process; instead of modelling the error term as a series of independent and identically
distributed random variables, it is modelled as a zero-mean stationary Gaussian process.
This leads to the model
Y (x) =
p∑
i=1
fi(x)β(i) + Z(x)
= fT (x)β + Z(x) ,
where p is the the number of regression terms in the model, f(x) = [ f1(x), ..., fp(x)]T
is a vector of regression functions, β = (β1, ..., βp)T is a vector of regression coeﬃcients
and Z(x) is a stationary Gaussian process with zero mean. Since Z has mean 0,
its behaviour is determined entirely by the choice of the process variance and the
correlation function. We shall refer to this technique as Gaussian process emulation; it
is also called Kriging by authors including Fang et al. (2006), after a similar and longer-
established technique from mining and geostatics. It was ﬁrst applied to computer
experiments by Sacks et al. (1989).
The choice of regression component of the Gaussian process emulator is an important
one. Intuitively, it is tempting to choose a model with several terms, as a well-ﬁtted
regression model can explain much of the variation in the simulator output. In practice,
however, it is rare to perform regression using an order higher than linear; this is
justiﬁed by O’Hagan (2006), who states that practical experience suggests that the
additional complexity of a higher-order model does not lead to a substantial enough
improvement in the ﬁt to be worthwhile. In the literature, the most common model
consists of a constant regression term (the mean) plus the stationary Gaussian process,
Y (x) = µ + Z(x) .
This is equivalent to setting the number of regression terms p = 1, and is referred
to by some authors, including Fang et al. (2006), as the ordinary Kriging model; the
sample mean is used as a point estimate for µ. A common alternative is p = 2, a linear
regression component, used for example by O’Hagan (2006).
To predict the simulator output, Yn+1 = η(xn+1), for an untested input vector, xn+1,
given the known vector Yn = [η(x1), ..., η(xn)]T of the simulator output at the training
points, we must use the posterior predictive distribution for Yn+1. This is identical to
the conditional distribution of the unknown simulator output given the training data,
so we must derive the density f(Yn+1|Yn).
As before, let n be the number of design points for the emulator and p be the
number of regression terms. We deﬁne F as an n × p matrix of regression functions for
11

---

## Page 32

the elements of the experimental design ξ, fn+1 = f(xn+1) as a p×1 vector of regression
functions for xn+1, C = R(xi − xj) as an n × n matrix of correlations amongst the
elements of ξ, and cn+1 = R(xi −xn+1) as an n ×1 vector of correlations between xn+1
and the elements of ξ.
The parameters β and σ2
z, which are deﬁned above, and the q × 1 vector of corre-
lation parameters θ = ( θ1, ..., θq)T are unknown. We ﬁrst obtain a joint conditional
distribution for Yn+1 and Yn given these unknown parameters:
f
(
Yn+1
Yn
) ⏐⏐⏐⏐ (β, σ2
z , θ) ∼ Nn+1
[ (
fT
n+1
F
)
β, σ2
z
(
1 cT
n+1
cn+1 C
) ]
.
If all three of β, σ2
z and θ are unknown, the posterior predictive distribution cannot
be determined analytically. If, however, the correlation parameters θ are treated as
being known, the predictive distribution can be derived. This is done by ﬁnding the
conditional density,
f(Yn+1|σ2
z , β, Yn) ,
and integrating out the two unknown variables. To obtain this we need a conjugate
prior distributions for β|σ2
z: a multivariate normal with known mean b0 and variance-
covariance matrix σ2
zV0. A conjugate prior is also required for σ2
z: this is a scaled-
inverse-chi-squared distribution with parameters ( ν0, c0/ν0), where ν0 is the degrees of
freedom and c0 is a constant. This can equivalently be viewed as an inverse-gamma
(ν0/2, c0/2) distribution, with density given by
f(σ2
z) = (c0/2)(ν0/2)
Γ(ν0/2) (σ2
z)−(ν0/2)−1 exp
{
− c0
2σ2z
}
.
The details of the derivation of the posterior predictive distribution are given in
Chapter 5 of Santner et al. (2003), with the result that the posterior predictive dis-
tribution is a non-standardised t-distribution. In one dimension, this is a function of
three parameters: the degrees of freedom ν, location parameter µ, and scale parameter
σ2. It is denoted as T1(ν, µ, σ2) and has the density function
f(w) = Γ[(ν + 1)/2]
Γ(ν/2)π(1/2)
√
νσ 2
(
1 + (w − µ)T (σ2)−1(w − µ)
ν
)(ν+1)/2
.
The posterior predictive distribution for Yn+1 has the form
f(Yn+1|Yn) ∼ T1(ν∗, µ∗, σ∗2) , (2.4)
where ν∗ = ν0 + n,
µ∗ = fT
n+1 ˆβ + cT
n+1C−1(yn − Fˆβ) , (2.5)
12

---

## Page 33

and
σ∗2 = Q1
ν∗
{
1 − (fT
n+1, cT
n+1)
[
−V−1
0 FT
F C
] (
fn+1
cn+1
) }
.
In the above equations, we have
ˆβ = (V−1
0 + FTC−1F)−1(V−1
0 b0 + FTC−1yn) , (2.6)
a Bayesian form of the generalised least squares regression estimator for the unknown
regression coeﬃcients β. We also have
Q1 = c0 + yT
n
[
C−1 − C−1F(FTC−1F)−1FTC−1
]
yn + H1 ,
where
H1 = (b0 − ˆβ)T (V0 + [FTC−1F]−1)−1(b0 − ˆβ) .
The conjugate prior distributions require several parameters to be estimated, and
choosing any speciﬁc value for them can be thought of as an informative decision. The
information required to make sensible informative choices for the prior distributions
is rarely available in advance. A more practical alternative is to use non-informative
or weak priors instead. For the regression coeﬃcients β, a non-informative conjugate
prior is the constant
f(β|σ2
z) = 1 .
The weak prior for the process variance σ2
z is the Jeﬀreys prior, introduced by Jeﬀreys
(1961):
f(σ2
z) = 1
σ2z
.
Per Rasmussen and Williams (2006), Chapter 2, these distributions can be viewed
as limiting cases of their strong counterparts as the prior variance of the parameters
is inﬁnitely large. Neither of these prior distributions is a proper distribution, but
this is not a concern as the resulting posterior distribution is proper; further details
can be found in Santner et al. (2003), Chapter 5. Using these priors, the posterior
predictive distribution is again gives a non-standardised t-distribution, but now with
the parameters ν∗ = n − p,
µ∗ = fT
n+1 ˆβ + cT
n+1C−1(yn − Fˆβ) , (2.7)
and
σ∗2 = Q2
ν∗
{
1 − (fT
n+1, cT
n+1)
[
−0 F T
F C
] (
fn+1
cn+1
) }
,
13

---

## Page 34

where
Q2 = yT
n
[
C−1 − C−1F(FTC−1F)−1FTC−1
]
yn ,
and
ˆβ = (FTC−1F)−1(FTC−1yn) . (2.8)
Also of interest is the simpler case in which the process variance σ2
z is treated as
known. In this case, a conjugate prior distribution is required for β only; this is, as in
the case of unknown process variance, a multivariate normal distribution with meanb0,
but its variance-covariance matrix is now τ 2V0 for a constant τ 2. Following a method
presented by several authors including Santner et al. (2003), Chapter 5, the resulting
posterior predictive distribution is a one-dimensional normal distribution,
f(Yn+1|Yn) ∼ N(µ∗, σ∗2) , (2.9)
with parameters
µ∗ = fT
n+1 ˆβ + cT
n+1C−1(yn − Fˆβ),
and
σ∗2 = σ2
z
{
1 − (fT
n+1, cT
n+1)
[
−σ2
z
τ 2 V−1
0 FT
F C
] (
fn+1
cn+1
) }
.
The posterior estimate of the regression coeﬃcients, ˆβ, is now given by
ˆβ =
(V−1
0
τ 2 + FTC−1F
σ2z
)−1(V−1
0 b0
τ 2 + FTC−1yn
σ2z
)
,
Again, the choice of the parameters of the prior distribution imposes strong infor-
mation on the posterior predictive distribution, so a non-informative approach is also
possible by setting the distribution for the regression coeﬃcients to f(β) = 1. This
again yields a normal distribution for the emulator output, with parameters
µ∗ = fT
n+1µβ + cT
n+1C−1(yn − Fˆβ)
and
σ∗2 = σ2
z
{
1 − (fT
n+1, cT
n+1)
[
−0 F T
F C
] (
fn+1
cn+1
) }
, (2.10)
where ˆβ is deﬁned in (2.8).
14

---

## Page 35

In the simplest case, the regression coeﬃcients β can also be considered to be known,
meaning that no prior distributions are required. Then, the posterior predictive distri-
bution is a normal distribution with mean
µ∗ = fT
n+1β + cT
n+1C−1(yn − Fβ) ,
and variance
σ∗2 = σ2
z(1 − cT
n+1Ccn+1) . (2.11)
It is useful to demonstrate prediction from a GP emulator using a simple one-
dimensional example. Consider a simulator deﬁned by the function
y = x4e−x + sin(2x) , −3.5 ≤ x ≤ 6.5 . (2.12)
We assume that the equation which deﬁnes the simulator is unknown, and construct
a GP emulator based on four simulator runs for diﬀerent values of x, with the design
ξ being deﬁned by the vector ξ = (3 .5, 4.5, 5.5, 6.5)T . A constant regression term
and a Mat´ ern correlation function with smoothness parameter ω = 5 /2 are used in
the emulator. The GP emulator is then used to predict the simulator output at 200
equally-spaced prediction points across the range of x.
The resulting predictions are plotted in Figure 2.1. The true simulator output is
shown in the plot as a solid black line, the design points in red, the mean prediction from
the emulator in blue, and the bounds of a 95% prediction interval from the emulator in
green. The plot demonstrates that the emulator mean is identical to the true simulator
output at the design points, but may diﬀer from it at untested inputs. The uncertainty
in the emulator estimates is zero at the design points where the simulator output is
known, and increases with the distance from the nearest design point.
Computational issues can arise whenC, the matrix of correlations between the design
points, is inverted. If the correlation between any pair of design points is very large,
or if the correlation between all pairs of design points is very small, C can be close to
singular. To overcome this, it is common to add a small error term δ, called a nugget,
to the diagonal of the matrix:
C = C + δI .
This deﬁnition of the nugget follows that of Andrianakis and Challenor (2012). Other
authors, including Gramacy and Lee (2012), deﬁne the nugget as a random term with
variance δ/σ 2
z. We can interpret the use of a nugget as introducing a small amount of
uncertainty into the simulator output at the design points. This ensures that C can
be inverted without diﬃculty. In Figure 2.1, the green lines would no longer meet at
the design points, but would lie a very small distance away from the true value. A
15

---

## Page 36

Figure 2.1: Prediction from a Gaussian process emulator for the simulator deﬁned in
equation (2.12).
fuller treatment of the use of a nugget was conducted by Andrianakis and Challenor
(2012), considering its eﬀect on prediction from the resulting emulator under various
conditions. In addition, Gramacy and Lee (2012) show that using a non-zero nugget
in a GP emulator can have a positive eﬀect on statistical properties including coverage
and predictive accuracy. For computational reasons, we makes use of a nugget in most
of the emulators constructed in our work.
GP emulation can occasionally produce poor predictions for the true simulator out-
put. The use of a stationary Gaussian process prior assumes that the correlation in
each dimension depends only on distance, not on location; that the simulator is smooth
and continuous; and that the residuals from our emulator estimate are equally likely
to lie on either side of the estimate in each dimension. These assumptions may not be
true for some simulators. The emulator also requires several parameters to be chosen,
either directly or through the speciﬁcation of prior distributions for Bayesian inference,
which can introduce a conﬂict with the data. These issues are discussed in detail by
O’Hagan (2006), and diagnostics which can be used to test the performance of an emu-
lator are introduced in the same paper; more recently, Bastos and O’Hagan (2009) also
considered diagnostics for a GP emulator.
Several software implementations for Gaussian process emulation exist in the R lan-
guage. The most popular package is ‘DiceKriging’ (Roustant et al., 2012), which in-
cludes many methods for fast calculation of emulators using a partially Bayesian frame-
work, with maximum likelihood estimation for the correlation parameters.‘DiceKriging’
supports two families of correlation functions: Mat´ ern with ω = 5/2 or ω = 3/2, and
power-exponential with 0 < α ≤ 2, including the special case of the Gaussian corre-
lation function. Another package, ‘mlegp’ (Dancik and Dorman, 2008), implements
16

---

## Page 37

the same methods for the Gaussian correlation function only.
2.3 Unknown parameters of the Gaussian process emula-
tor
It is not usually possible to know in advance which parameter values will lead to an
appropriate GP emulator. As demonstrated above, it is possible to integrate out some
of these parameters for certain choices of prior distribution, but this cannot be done
for the correlation parameters, and it is sometimes desirable to estimate the process
variance and regression coeﬃcients directly. Additionally, the appropriate size of the
nugget of the Gaussian process cannot typically be determined until the emulator is
ﬁtted. There are two main ways to estimate the unknown parameters.
2.3.1 Plug-in approach
The simpler method is a plug-in approach, in which a single value of each unknown
parameter is found and used throughout the following analysis in place of the full
distribution of the parameter(s). This has the advantage of being able to treat the
parameter as a single known value, allowing the theoretical results derived above to be
used directly. It is also less computationally intensive than other approaches.
A common method to estimate the unknown parameters by a single value is maxi-
mum likelihood estimation (MLE) , in which the value of the parameters is chosen to
maximise their joint likelihood given the observed data. This is an intuitively sensible
choice, since it ensures that the parameters are chosen in a way which makes the ob-
served data most likely to have been reached. Its use in GP emulation for computer
experiments dates to the beginnings of the ﬁeld itself, including in the work of Sacks
et al. (1989), and it remains the most widespread choice.
In practice, maximising the joint likelihood of the parameters is diﬃcult, so they
are typically estimated separately (see Chapter 5 of Fang et al., 2006). Maximum
likelihood estimation of the of the regression coeﬃcients, β, and process variance, σ2
z,
is particularly straightforward as the MLE for these parameters is available in closed
form. For the regression coeﬃcients, the MLE is the generalised least-squares regression
estimator introduced in equation (2.8). The MLE of the process variance is
ˆσ2
z = 1
n(yn − Fˆβ)TC−1(yn − Fˆβ) .
The MLE of the correlation parameters θ is not available in closed form, so this must
be found using an iterative numerical method. The matrix C, which appears in the
MLEs for β and σ2
z, depends on θ; it is thus necessary to update the estimates of β
and σ2
z after updating θ using the chosen numerical method. An algorithm to do this
is presented in Chapter 5 of Fang et al. (2006) .
17

---

## Page 38

Alternative approaches to simple maximum likelihood estimation also exist. The
restricted maximum likelihood (REML) method, introduced by Patterson and Thomp-
son (1971) for incomplete block design experiments, computes less biased estimates for
variance and covariance/correlation parameters than MLE. This is achieved by max-
imising the likelihood of a set of linearly independent combinations of the observed
data instead of the data itself. As for MLE, the REML estimate of σ2
z is available in
closed form, while the estimate of θ is not. Chapter 3 of Santner et al. (2003) provides
further details.
The likelihood function for the correlation parameters θ can often be very ﬂat in
practice, meaning there is a large variance in the maximum likelihood or REML esti-
mates. This can occur even in very simple examples, for example the one-dimensional
sinusoidal function given by Li and Sudjianto (2005). The same authors proposed
a solution using a penalised likelihood, in which a penalty function is added to the
likelihood before maximisation takes place. This can have the eﬀect of increasing the
variation around the maximum, reducing the variance of the resulting estimate. The
suggested penalty function is the smoothly clipped absolute deviation (SCAD) penalty
(Fan, 1997).
From a Bayesian perspective, MLE can be viewed as a special case of the more general
maximum a posteriori estimation (MAP). Instead of just maximising the likelihood,
this method maximises a posterior distribution derived from both the likelihood and a
prior distribution. This is also referred to as posterior mode estimation, and has been
considered as a method to obtain the parameters of a GP emulator by several authors
including Santner et al., 2003, Chapter 3, and Gu et al., 2018. The choice of the prior
distribution for the parameters is an important one, since this will signiﬁcantly eﬀect the
posterior distribution to be maximised. Maximum likelihood estimation corresponds
to the use of a uniform prior distribution on the parameters of interest. This is in
some ways a natural choice for parameters of a GP emulator, about which little may
be known in advance. When non-uniform conjugate priors are chosen to allow the
regression coeﬃcients and process variance to be integrated out, however, these should
be taken account of in the estimation of the correlation parameters. In addition, Gu
et al. (2018) presented an argument for using non-uniform priors on the correlation
parameters based on the robustness of the parameter estimates, as this is less likely to
lead to C being close to singular or to the identity matrix I.
It is worth reviewing parameter estimation in existing R packages for GP emula-
tion, since our code makes use of these packages in places. ‘mlegp’ uses exclusively
maximum likelihood estimation for all of the unknown parameters of the emulator.
‘DiceKriging’ also supports this approach, but provides additional options. Penalised
maximum likelihood estimation with a SCAD penalty function is also oﬀered. The pa-
rameters may also be entered by the user directly, which allows other methods to be
used.
18

---

## Page 39

One oddity concerning the two packages is the scaling of the correlation parameters of
the power-exponential correlation function. While ‘mlegp’ requires α = 2 and uses the
form given in equation (2.2), ‘DiceKriging’ allows α to vary and uses the alternative
parameterisation
R(h) = exp
[
−
q∑
j=1
1
2
(hj
bj
)α]
.
In our work, the form given in equation (2.1) is used. However, since we use the
‘DiceKriging’ package to estimate correlation parameters in some of our examples,
the values returned by the package must ﬁrst be transformed to our preferred scale.
Parameter estimation in the following chapters is conducted using MLE where applica-
ble, and MAP with conjugate priors for the regression coeﬃcients and process variance
where these parameters are integrated out. It should be noted that if MAP with a non-
uniform reference prior on the correlation parameters is considered, Gu et al. (2018)
suggest avoiding the parameterisation given in equation (2.1), but this is not an issue
for us as reference priors are not used in this thesis.
None of the plug-in estimation methods described above allow the form of the max-
imiser for the correlation parameters to be determined analytically, so this requires
numerical optimisation. This can be a diﬃcult problem, as the function to be opti-
mised may be either extremely ﬂat or have many local maxima. There are several
algorithms which could be used, many of which are listed in Chapter 3 of Santner
et al. (2003). The approach taken by ‘DiceKriging’ is based on a combination of the
Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm, an iterative method based on
local search and gradient descent, and a genetic algorithm for global search; it is de-
scribed in further detail by Roustant et al. (2012). Even with this combined method, it
is still common for only a local optimum to be found, but this can be partially overcome
by running the optimisation algorithm from many diﬀerent starting locations within
the space of the correlation parameters.
The main weakness of a plug-in approach to the unknown parameters is that it
ignores a source of uncertainty in predictions from the emulator. By treating the
unknown parameters as single values instead of a distribution of possible values, the
uncertainty in them is not captured in the analysis that follows, leading to potentially
low variance bounds and overconﬁdence in the resulting predictions. In the case of the
nugget, which exists only for computational purposes, this is not a problem provided
a reasonable value is chosen. For the correlation parameters, and (where relevant) the
process variance and regression coeﬃcients, it is more of a concern. Despite this, due to
its computational simplicity and widespread prior use in both literature and software
implementation, a plug-in method based on maximum likelihood estimation forms the
basis of our work in the remainder of the thesis. The following subsection discusses
an alternative approach which accounts for the uncertainty in the estimates of the
19

---

## Page 40

parameters in its predictions, but which was not taken forward due to the increased
computational resources required.
2.3.2 Markov chain Monte Carlo
A more complex alternative is a Bayesian approach in which a sample of values
for the parameters is generated using Markov chain Monte Carlo (MCMC). This is
typically done only for the correlation parameters θ, as the regression coeﬃcients and
process variance can instead be integrated out as described in Section 2.2. MCMC
is a set of methods which are designed to sample from a probability distribution by
constructing and sampling from a Markov chain with the target probability distribution
as its limiting distribution. Using this approach, it is possible to sample from the
distribution without knowing its constant of proportionality; we require only a density
proportional to that of the target. Detailed coverage of the topic can be found in books
by several authors, including Gamerman and Lopes (2006).
For a Markov chain with a continuous state space S, let A be a subset of S. Let
θ be the vector of parameters of interest, and θ(j) be the value of the parameters of
interest after j timesteps. A Markov chain is called time-homogeneous if its transition
probabilities do not depend on the number of steps made so far; the equality
P [θ(M +1) ∈ A|θ(M ), θ(M−1), ..., θ(0)] = P [θ(1) ∈ A|θ(0)]
holds for all M ∈ 0, 1, 2, ..., and A ∈ S. It is then possible to deﬁne a transition
function P (φ, A), called the kernel of the chain, which states the probability of moving
from a state φ to a subset A ∈ S in a single step. We require that the kernel is
a probability distribution over S for any φ, and that it is possible to evaluate it for
any choices of φ and A. The kernel can be used to generate the next state of the
chain. For two states ψ, φ we may choose to split the kernel P (ψ, φ) into a transition
kernel q(ψ), which determines a proposal φ for the next state from the kernel, and an
acceptance probability a(ψ, φ), which determines how often the proposal is accepted.
If the proposal is rejected the chain remains in the current state for a further timestep.
A Markov chain is irreducible if it is possible to reach any subset of the state space
from any other in a ﬁnite number of steps. The expected number of steps in which the
chain will return to the subset is called the mean recurrence time; a subset is positive
recurrent if its mean recurrence time is ﬁnite.
The stationary distribution, π, of a Markov chain is a distribution over its state space
such that if the probability of being in each state of the chain follows the distribution
π at any timestep of the chain, it will still follow π at the next timestep. This can be
expressed mathematically as
∫
π(ψ)P (ψ, φ)dψ = π(ψ) .
20

---

## Page 41

Consider an irreducible, time-homogeneous Markov chain in which every subset of the
state space is positive-recurrent. A result given in several sources including Nummelin
(1984) states that if this chain has a stationary distribution π, the distribution of the
states converges to π as the number of steps increases, irrespective of the initial state.
π is called the limiting distribution (sometimes equilibrium distribution or invariant
distribution) of the Markov chain.
A time-homogeneous Markov chain with limiting distribution π is reversible if
π(ψ)P (ψ, φ) = π(φ)P (φ, ψ) ∀ φ, ψ ∈ S (2.13)
which is called the detailed balance equation, and implies that the probability of making
a transition from ψ to φ is the same as that of transitioning from φ to ψ under the
limiting distribution. The converse is also true: if a distribution D satisﬁes equation
(2.13) for a Markov chain with kernel P (ψ, φ), then D is the limiting distribution of
the chain.
MCMC methods exploit this to create a Markov chain with the probability distri-
bution we wish to sample from as its limiting distribution. To be certain that the
properties of the chain approximate those of the target distribution, we require the
chain to be aperiodic. The period of a subset A of S is the greatest common divisor
of all possible numbers of steps in which the chain can return to A. A subset A is
aperiodic if it has period 1; a Markov chain is aperiodic if this is true for all A ∈ S.
Under the conditions of irreducibility, aperiodicity and positive recurrence of states, a
sample approximation to a function t(θ),
t′
M = 1
M
n∑
j=1
t[θ(j)] ,
converges with probability 1 to the expectation of t(θ) as M → ∞ . This means that
for a suﬃciently large sample size M, per sources such as Gamerman and Lopes (2006),
the sample average t′
M can be used as an estimate for t(θ).
To use MCMC to sample from the distribution D(θ) of the parameters of interest,
we must construct a chain with D(θ) as its limiting distribution. This is achieved by
choosing a kernel P (ψ, φ) which satisﬁes (2.13) for D(θ). The longest-established and
most common choice is the Metropolis-Hastings algorithm , which in its earliest form
was proposed by Metropolis et al. (1953) and was later generalised by Hastings (1970).
The transition kernel φ = q(ψ) is a random walk transition,
φ = ψ + w , (2.14)
where w is a randomly generated vector with probability density fw. A Markov chain
with a random walk transition kernel is reversible if fw is symmetric about 0, so sev-
eral options for this density are possible; the most common is a multivariate normal
21

---

## Page 42

distribution. The acceptance probability a(ψ, φ) is
a(ψ, φ) = min
{
1, D(φ)q(φ)
D(ψ)q(ψ)
}
= min
{
1, D(φ)
D(ψ)
}
,
where the second equality holds since q(ψ) is reversible. This is equivalent to
a(ψ, φ) = min
{
1, fD(φ)
fD(ψ)
}
, (2.15)
where fD(θ) is a function proportional to the target density D(θ), as the normalising
constant in the density appears in both the numerator and denominator of the second
term of the acceptance probability and thus cancels out. Algorithm 1 sets out the steps
of the Metropolis-Hastings algorithm formally.
Algorithm 1: Metropolis-Hastings algorithm
Input: Initial value θ(0); target sample size M
Output: Sample matrix Θ = (θ(1), ..., θ(M ))T from target density D(θ)
begin
for j ← 1 to M do
φ ← sample (q(θ(j−1))) ; // q() defined in (2.14)
p ← a(θ(j−1), φ) ; // a() defined in (2.15)
u ← sample (unif(0, 1)) ;
if u < p then θ(j) = φ;
else θ(j) = θ(j−1);
end
end
When a multivariate normal distribution is used to generate the proposals, the choice
of the covariance matrix can have a large eﬀect on the algorithm’s performance. The
covariance matrix can be either a scalar multiple of the identity matrix or of an esti-
mated matrix of correlations between the dimensions of the target density. In either
case the scalar which multiplies this matrix, called the variance parameter or v, must
be carefully chosen. If it is too large, the transitions proposed are also large and are
thus unlikely to be accepted as they will frequently take the chain to regions of the
state space where the target density is very low. Equally, a very small choice for v
means that the proposed transitions are also small, so the chain will take a long time to
explore the whole of the space. In extreme cases, the chain can remain in one region of
the state space where the density is high while failing to reach another similar region,
as few or no proposals will be large enough to make this jump. These issues were
discussed in detail by Roberts et al. (1997), with the conclusion that a good value for
v can be determined from the probability of a transition being accepted. The paper
22

---

## Page 43

demonstrates that, as the dimensionality of the state space tends to inﬁnity, the opti-
mal acceptance probability under certain conditions tends to 0.234. In one dimension,
the optimal acceptance probability was found to be close to 0.5.
Instead of a random walk, other transition kernels are possible. For example, Hamil-
tonian Monte Carlo (HMC) has a structure similar to that of the Metropolis-Hastings
algorithm, but the Markov chain used is deﬁned diﬀerently (Neal, 2011). Proposed tran-
sitions are generated using random sampling from a multivariate distribution deﬁned by
a process called Hamiltonian dynamics, which originated in physics as a 19th-century
reformulation of classical mechanics. This technique, introduced by Duane et al. (1987)
in the ﬁeld of molecular simulation, allows much larger transitions to be made than
random walk proposals.
For MCMC sampling to take place for the correlation parameters, we require a
density proportional to that of f(θ|Yn). Using the same informative conjugate prior
distributions for β|σ2
z and σ2
z as in Section 2.2, and following a method based on deriving
marginal distributions using integration presented in the context of Bayes linear models
by Banerjee (2010), the proportional density can be derived to be
f(θ|Yn) ∝ [c0 + eT (C−1 − C−1F(V−1
0 + FTC−1F)−1FTC−1)e]−ν0+n
2
|V−1
0 + FTC−1F|1/2|C|1/2 ,
where
e = yn − Fb0 .
If non-informative priors are instead chosen for β|σ2
z and σ2
z (again as in Section 2.2),
the result is
f(θ|Yn) ∝ [(yn)T (C−1 − C−1F(FTC−1F)−1FTC−1)(yn)]−n/2
|FTC−1F|1/2|C|1/2 .
Computing the actual value of these densities can be a challenge: as the number of
design points n increases, the power −(ν0 + n)/2 or −n/2 becomes large and negative,
with the result that any value raised to this power is extremely close to zero, causing
computational diﬃculties. This obstacle can be removed by working with the log-
likelihood instead of the density function of the pure likelihood. With informative
priors on β|σ2
z and σ2
z, this is given by
l(yn) ∝ K1 − 1
2 log
⏐⏐⏐(C + FV0FT )
⏐⏐⏐
−
(ν0 + n
2
)
log
[
1 + 1
c0
eT (C + FV0FT )−1e
]
,
23

---

## Page 44

where K1 is a constant with respect to θ. Similarly, with non-informative priors on
β|σ2
z and σ2
z, the log-likelihood is
l(yn) ∝ K2 − 1
2 log |FTC−1F| − 1
2 log |C|
− n
2 log
[
(yn)T (C−1 − C−1F(FTC−1F)−1FTC−1)(yn)
]
,
with K2 constant with respect to θ.
In practise, the determinants in these equations can be small enough to be computa-
tionally zero, leading to problems when their logarithm is taken. This can be overcome
by recalling that the determinant of a matrix is the product of its eigenvalues, which
we denote by λ1, ..., λn. Since the logarithm of a product of terms is equal to the sum-
mation of the logarithms of these terms, the logarithm of the determinant of a matrix
Λ can thus be rewritten as
log |Λ| =
n∑
i=1
log λ(i) ,
which is more computationally stable as it does not involve the product of the eigen-
values.
Using MCMC for the correlation parameters of the GP emulator allows a fully
Bayesian analysis which captures all sources of uncertainty in an emulator, leading to
more robust predictions. It is however more computationally intensive, and reduces the
use that can be made of theoretical results, instead requiring large simulations from the
emulator using the MCMC sample for the correlation parameters. In the early stages
of our work, MCMC was considered as the better approach and was implemented for
emulators for a single computational model. For chains of models, this was not taken
forward for two reasons: speed of execution of the linked emulator, and the wish to
make use of theoretical results which will be presented in Chapter 3. Incorporating
MCMC into the construction and analysis of linked emulators nonetheless remains a
potentially valuable avenue for future research.
2.4 Extensions of the GP emulator
Although Gaussian process emulation is a powerful modelling tool, there are cases
it cannot cover without further extension. The assumption of stationarity in the GP
emulator is a strong one, which will often not be met in the real world; it is common
to encounter models with much larger variation (and thus lower correlation) between
nearby points in some parts of the input space than others. One solution to this is the
use of a treed Gaussian process, in which treed partitioning is used to determine regions
of approximate stationarity, allowing the ﬁtted emulator to use diﬀerent stationary
GPs in diﬀerent regions of the design space. Gramacy and Lee (2008) provides further
24

---

## Page 45

details on this approach. The R package ‘tgp’ (Gramacy and Taddy, 2010) provides
a software implementation of this approach. Unlike the packages for standard GP
emulation discussed above, it allows the use of Markov chain Monte Carlo to obtain a
sample for the correlation parameters.
Categorical input variables are another complicating factor for GP emulation due
to their eﬀect on the correlation function of the Gaussian process. If a model with
one or more continuous inputs also takes an input with only two levels, any two input
conﬁgurations with diﬀerent levels of the binary variable are a ﬁxed distance apart in
the space of this input, at the maximum possible distance. A standard multiple-input
correlation function such as the product power-exponential or product Mat´ ern will give
a scale parameter in this dimension which returns correlations close to zero if the input
has a substantial eﬀect on the output, rendering correlations in the other dimensions
irrelevant and the overall correlation obtained not particularly meaningful. Qian et al.
(2009) attempt to address this by developing bespoke correlation functions to handle
a mixture of categorical and continuous input variables.
In many real processes to which ﬁtting an emulator would be useful - and, increas-
ingly, in many computational models - repeating a measurement at the same input
conﬁgurations will not return the same output. Such a model is called stochastic ;
if the variance depends on the inputs, the model is additionally heteroscedastic. A
standard GP emulator is not appropriate for such a model, since it will assume that
the variance at a design point is only that of the nugget (which may be unrealistically
low), and that the variance is the same at every design point (when it is likely to vary
across the input space). Instead, the stochasticity and heteroscedasticity in the output
should be accounted for directly.
Goldberg et al. (1998) propose a way to do this: ﬁt a stationary GP emulator to
the mean of the simulator response, and a second independent stationary GP emulator
to the variance of the response, with MCMC sampling for both the parameters of the
Gaussian processes and the posterior distribution of the variance. Kersting et al. (2007)
follow a similar approach, but with maximum likelihood estimation instead of MCMC,
and demonstrate that the method is eﬀective for several data sets. More recently, the R
package ‘hetGP’ has provided a software implementation of this; the associated paper
of Binois et al. (2018) considers in detail the problem of experimental design for a
heteroscedastic GP emulator, which is more complicated than for the traditional case
as replication is required to determine the nature of the variance of the response.
Finally, the framework described above holds only if the computer model of interest
returns a single output. Simulators with multiple outputs can be handled in a variety
of ways. If the number of outputs is small, a separate emulator may be built for each
output; this is done by Kyzyurova et al. (2018) among others. For high-dimensional
outputs, this becomes very computationally intensive. A speciﬁc example of relevance
25

---

## Page 46

to our application is dispersion modelling. The output in this case is typically the
concentration of a contaminant across a two-dimensional grid, often over time. Several
approaches have been suggested to deal with this by various authors.
In addition to several separate emulators, Conti and O’Hagan (2010) consider two
methods to deal with a simulator which returns a vector of outputs over time. The ﬁrst
is to explicitly build an emulator for all of the outputs simultaneously. The output of
the computer experiment is now multi-dimensional, and the joint posterior predictive
distribution for the simulator output at an arbitrary point in the input space given
the parameters of the Gaussian process is shown in the paper to follow a multivariate
normal distribution. Analogously to the univariate case, if the regression parameters
and the process variance are integrated out, the predictive distribution is multivariate
t. Treating time as an input to the model, and building a standard single-output
emulator based on this reformulation, is also considered. The multi-output emulator is
found to perform better than the time-input emulator or several separate emulators in
several examples. However, the computational cost of such an approach can be large,
as many model runs may be required before the behaviour of the true model is properly
understood.
Another alternative is to perform dimension reduction on the output. Instead of
building an emulator for the simulator output directly, a set of basis functions are
constructed which can be used to estimate the true output anywhere on a grid of points
in time. This requires the number of basis functions to be determined, which can be
done by considering the percentage of the variance explained by the approximation.
Univariate Gaussian process emulators are then used to emulate the coeﬃcients of
the basis functions, and the simulator output at an untested point is predicted using
a combination of the GP emulator and the basis function approximation. An early
example of this method, in which much of the underlying theory is developed, is found
in Higdon et al. (2008), where a principal component basis is used. Bowman and
Woods (2016) take a similar approach but consider a thin-plate spline basis in addition
to principal components; the thin-plate spline basis is found to perform better for
dispersion modelling on a grid in time.
2.5 Conclusions
This chapter reviews the existing theory behind the process of approximating a com-
plex computational model by means of a Gaussian process emulator. We reviewed
possible correlation functions and regression components of the GP emulator, and pre-
sented posterior predictive distributions in a variety of cases from a partially Bayesian
perspective. Methods to determine the unknown parameters of the emulator using
either plug-in estimation or Markov chain Monte Carlo sampling were also reviewed,
together with extensions of the GP emulator to properly handle a wider class of under-
lying computational models. Many of the ideas presented here will be taken forward
26

---

## Page 47

in the context of chains of models in Chapter 3.
27

---

## Page 48

28

---

## Page 49

Chapter 3
Emulation for chains of multiple
models
3.1 Introduction
A chain of multiple models is deﬁned for the purposes of our work as a series of
computational models with univariate output but potentially several input variables,
in which the output of one model in the chain is used as an input variable to a second
model and so on. We assume that the models are deterministic, so that the only
uncertainty arises from the values of the input variables, and that the models are
computationally expensive to run and must be approximated as described in Chapter
2.
There is a noteworthy body of literature on chains of computational models. The re-
view paper of Stevens and Atamturktur (2016) considers several established approaches
for veriﬁcation and validation of predictions from a chain of models using real-life data.
Examples of ﬁelds in which veriﬁcation and validation processes for chains of mod-
els have been considered include anisotropic contact surfaces in material science by
Konyukhov et al. (2008), and motion in a moored system in ﬂuid dynamics by Lin
and Yim (2006). In the context of Gaussian process emulation for chains of models,
Damianou and Lawrence (2014) presented an approach to uncertainty propagation us-
ing variational inference. This approach expands on the work of Titsias and Lawrence
(2010), and takes the output of the earlier model as an uncertain input to the next
model, which is then treated as a latent variable. A prior distribution is then chosen
for the latent space of the input, which allows it to be variationally integrated out using
an approximation to its true posterior distribution.
The most relevant prior work is that of Kyzyurova et al. (2018), which developed
methods to predict from a set of linked models in which the ﬁnal model may take
multiple inputs derived from distinct earlier models. This is a closely related problem
to the one which forms the basis of this thesis, but is not identical in its formulation: it
does not consider chains with more than two steps, while we do not allow more than one
29

---

## Page 50

input per model to arise from earlier models. The related problem of Gaussian process
emulation with an input known only up to a probability distribution is considered by
Girard et al. (2002) and Candela et al. (2003), with a speciﬁc focus on time series
forecasting. All of these papers are based on a theoretical result for the mean and
variance of a linked emulator for a chain of two models, which we consider further in
Section 3.3.
Before presenting our approach to the problem of emulating multiple models in a
chain, we must deﬁne some notation. Let yk be the output of the kth model in the
chain, and let
˜ xk = (xk,1, ..., xk,qk)T
be a vector of qk distinct inputs to model k. We use this notation since (for example)
x1 is potentially ambiguous given the existence of the inputs x1,1, x1,2, ..., x2,1, x3,1, ....
Each model in the chain does not necessarily takes the same number of inputs, so each
qk and thus the length of ˜ xk may diﬀer for distinct value of k.
For illustrative purposes, consider the simplest case: a chain of two models. The ﬁrst
model in the chain is deﬁned by the equation
y1 = η1(˜ x1) .
The second model in the chain is deﬁned by the equation
y2 = η2(˜ x2, y1) ,
as it depends not only on its own direct inputs ˜ x2 but also on the additional input y1
which is the output of model 1. Such a chain is depicted in Figure 3.1.
Figure 3.1: Diagram of a chain of two models
In order to make probabilistic predictions from multiple models in a chain, we need to
understand how uncertainty in the models will combine. As discussed in Chapter 1, our
30

---

## Page 51

work is based on emulating each model individually and linking the chain of emulators
together, instead of building a composite emulator for the chain as a whole. The use of
an emulator to approximate the ﬁrst model in the chain introduces uncertainty in our
predictions of the output, y1, of model 1, which is then carried forward into the second
model since y1 is also an input to model 2. In longer chains, the same applies to the
inputs y2 to model 3, y3 to model 4 and so on.
We deﬁne βk as the vectors of regression coeﬃcients for the emulator of model k, σ2
z,k
as the prior variance for the emulator of model k, and θk as the vectors of correlation
parameters for the emulator for model k. The matrix of regression functions for the
design points of the computer experiment for model k are denoted as Fk, and the
matrix of correlations between the design points as Ck. The vector of observed outputs
of the computer experiment at the n design points for model k is denoted by Yn,k.
We also require notation for prediction at an unknown set of inputs, analogous to the
vector xn+1 in the single-model case. Let ˜ xk,n+1 be the vector of directly controllable
inputs to model k at an untested input conﬁguration, so that for a chain of r models,
the set of all choosable inputs is ( ˜ x1,n+1, ˜ x2,n+1, ...,˜ xr,n+1). Similarly, let xk,n+1 be the
vector of all inputs to the model k at an untested input conﬁguration, including both
the directly controllable inputs ˜ xk and the unknown output yk−1 of the previous model
in the chain. We deﬁne the vector of regression functions at xk,n+1 as fn+1,k, and the
vector of correlations between xk,n+1 and the design points for model k as cn+1,k
We shall begin by simplifying the problem. Assume that weak priors are used
throughout, and that the process variances and correlation parameters of every model
in the chain are known. The emulator for model 1 is a standard GP emulator for a
single model, as none of the inputs to the ﬁrst model in the chain depend on the out-
put of another model. Following equations (2.9) and (2.10), the posterior predictive
distribution of y1 is
f(Y1|˜ x1, Yn,1) ∼ N(µ1, σ2
1) ,
where
µ1 = fT
n+1,1 ˆβ1 + cT
n+1,1C−1
1 (yn,1 − F1 ˆβ1) ,
and
σ2
1 = σ2
z,1
{
1 − (fT
n+1,1, cT
n+1,1)
[
0 F T
1
F1 C1
] (
fn+1,1
cn+1,1
) }
.
The estimate ˆβ1 of the unknown regression coeﬃcients β1 is the generalised least
squares regression estimator,
ˆβ1 = (FT
1 C−1
1 F1)−1(FT
1 C−1
1 yn,1) .
31

---

## Page 52

The emulator for a model k > 1 which occur later in the chain could still be treated as
standard GP emulator if the input yk−1 is conditioned on. This would lead to posterior
predictive distribution
f(Yk|˜ xk, y1, Yn,k) ∼ N(µk, σ2
k) ,
where
µk = fT
n+1,k ˆβk + cT
n+1,kC−1
k (yn,k − Fk ˆβk) ;
σ2
k = σ2
z,k
{
1 − (fT
n+1,k, cT
n+1,k)
[
0 F T
k
Fk Ck
] (
fn+1,k
cn+1,k
) }
;
ˆβk = (FT
k C−1
k Fk)−1(FT
k C−1
k yn,k) .
For simplicity, we shall now consider a chain of two models only. The predictive dis-
tribution for y2 depends on y1. At an untested input conﬁguration x1,n+1 of the inputs
to the ﬁrst model ˜ x1, the value of y1 is known only up to its predictive distribution.
The predictive distribution for y2 thus depends on an uncertain input.
The ideal situation would be to integrate out y1 altogether to obtain a predictive
distribution which depends only on the directly controllable inputs to the chain of
models:
f(y2|˜ x2, ˜ x1) =
∫
f(y2|˜ x2, y1)f(y1|˜ x1)dy1 . (3.1)
Let
f∗(y2) = f(y2|˜ x2, y1, Yn,2)f(y1|˜ x1, Yn,1)
be the product of the conditional densities for y1 and y2 given the outputs of the
computer experiments for model 1 and model 2. This is given by
f∗(y2) = 1√
2πσ2
1
exp
{
− (y1 − µ1)2
2σ2
1
}
× 1√
2πσ2
2
exp
{
− (y2 − µ2)2
2σ2
2
}
= 1
2πσ1σ2
exp
{
− (y2 − µ2)2
2σ2
2
− (y1 − µ1)2
2σ2
1
}
. (3.2)
In general, this is not integrable analytically, since µ2 and σ2
2 depend on y1 in a
complex, nonlinear way through fn+1,2 and cn+1,2:
fn+1,2 = [f2,1(x2,1), f2,2(x2,2), ..., f2,q2(x2,q2), f2,q2+1(y1)]T ; (3.3)
cn+1,2 = [R(x2,1 − x2,n+1), ..., R(x2,n − x2,n+1)]T . (3.4)
32

---

## Page 53

A natural approach to consider so that the integral in (3.1) can be calculated exactly
is to simplify the problem by constraining the form of fn+1,2 and cn+1,2. Assume a
constant regression term such that every entry of fn+1,2 and F2 is equal to 1, and a
squared exponential correlation function as deﬁned in (2.2). Then,
R(x2,1 − x2,n+1) = exp
{
−
q2∑
j=1
bj(x(j)
2,1 − x(j)
2,n+1)2 − by1(x(q2+1)
2,1 − y1)2
}
= exp
{
−
q2∑
j=1
bj(x(j)
2,1 − x(j)
2,n+1)2
}
exp
{
− by1(x(q2+1)
2,1 − y1)2
}
, (3.5)
where by1 is the correlation parameter in the input corresponding to the output y1 of
the ﬁrst model, and x(j)
2,1 is the jth entry of x2,1. Identical results are obtained for
R(x2,2 − x2,n+1), ..., R(x2,n − x2,n+1) up to diﬀerent indexing. However, even after this
simpliﬁcation, it is still not possible to solve (3.1) analytically as the form of the integral
is too complex. The remainder of this chapter considers two possible routes to make
predictions from a chain of emulators despite this restriction.
3.2 Approximating the linked emulator output by Monte
Carlo integration
Given the lack of an analytical solution to the integral of (3.2), a natural alternative is
to approximate it using a numerical approach. We choose to use a simple form of Monte
Carlo integration. For a given prediction point ( ˜ x1,n+1, ˜ x2,n+1)T , we draw a sample of
ﬁxed size from the predictive distribution for y1 given ˜ x1,n+1. We then draw a single
value from the predictive distribution for y2 given ˜ x2,n+1 and y1 for each realisation of
y1. The generated values of y2 then form an unbiased sample from the true posterior
predictive distribution for y2, which can be used to make inferences about the true
value of y2 at the prediction point.
In practise, the prior variances of the two Gaussian processes, σ2
z,1 and σ2
z,2, will not
usually be known. A Bayesian approach is to condition on these quantities as well,
leading to a diﬀerent form for the integrand in (3.1). Following equations (2.4) and
(2.7), the density that we wish to integrate with respect to y1 is thus a product of
two conditional t densities instead of normal densities. In the case of Monte Carlo
integration, this does not change the approach described above. This approach still
requires estimation of the correlation parameters of the GP emulators to the models in
the chain, but could if desired be made fully Bayesian using MCMC.
As an example of the Monte Carlo strategy, we consider a chain of two models which
are composed of known deterministic functions:
y1(x1,1, x1,2) = {sin(2πx3
1,1)}3 , −0.8 ≤ x1,1 ≤ 0.8 ;
33

---

## Page 54

y2(x2,1, y1) = sin(πy1) + exp(y1) . (3.6)
Since this system is deﬁned entirely by its ﬁrst input, we can compare the true value
of the target output, y2, at a given value ofx1,1 to the predictions made by the emulator
to test that the emulator’s behaviour is reasonable.
Figure 3.2: Prediction for y2 against x1,1 using the simulation method from the chain
of emulators in the two-model example.
For our emulation, we use a Gaussian correlation function in both models, with a
constant regression term and a nugget δ = 10−7. 20 design points are chosen, which
are equally spaced in the critical input x1,1 and randomly spaced in the trivial inputs
x1,2 and x2,1. This would not be a feasible design for an unknown model, but is useful
as an illustrative exercise to test that our predictions are reasonable. The outcome of
interest is prediction from the posterior predictive distribution for y2 across the range
−0.8 ≤ x1,1 ≤ 0.8; the same ranges are used for x1,2 and x2,1, which assuming a
reasonable correlation structure should have no impact on the predictions made.
The results of this are shown in ﬁgure 3.2. The true function is shown in black, the
design points in red, the mean of the emulator at each x1,1 in blue, and the upper and
lower bounds of an empirical 95% prediction interval in green. These predictions tally
well with what we would expect. The emulator mean tracks the true function well, and
the uncertainty is at its largest away from the design points, pinching to virtually zero
where the true output is known.
34

---

## Page 55

3.3 The mean and variance of the linked emulator
Although it is not possible to solve (3.1) analytically, which would produce a full
distribution for the linked emulator, it is possible to obtain theoretical expressions for
its mean and variance under certain conditions. This approach follows from the early
work of Girard et al. (2002) and Candela et al. (2003) on Gaussian process emulation
with uncertain inputs, and was developed in full for a chain of two models by Kyzyurova
et al. (2018). Assume that all of the parameters of each emulator are obtained by a plug-
in method, including the regression coeﬃcients β1 and β2. The posterior predictive
distributions on y1 and y2 given their GP emulators are found from equation (2.11);
they are normal distributions, with means and variances
µ1 = fT
n+1,1β1 + cT
n+1,1C−1
1 (yn,1 − F1β1) ;
σ2
1 = σ2
z,1(1 − cT
n+1,1C1cn+1,1) ;
µ2 = fT
n+1,2β2 + cT
n+1,2C−1
2 (yn,2 − F2β2) ;
σ2
2 = σ2
z,2(1 − cT
n+1,2C2cn+1,2) .
Assume a squared exponential correlation functions on the GP emulators for y1 and
y2, and assume the regression term of the GP emulator is constant. Under these
conditions, the following theorem holds for the output of a linked emulator for the
model 2 output y2:
Theorem 3.1. Let
E∗(y2) = E(y2|˜ x2, ˜ x1, Yn,2, Yn,1)
and let
V ar∗(y2) = V ar(y2|˜ x2, ˜ x1, Yn,2, Yn,1)
be the mean and variance of the posterior predictive distribution for y2 under the linked
emulator. Let a(i) be entry i of
a = C−1
2 (yn,2 − β2,0) .
Then, the posterior predictive distribution for y2 under the linked emulator has expec-
tation
E∗(y2) = β2,0 +
k∑
i=1
a(i)
q2∏
j=1
exp
{
− bj(x(j)
2,i − x(j)
2,n+1)2
}
Ii (3.7)
35

---

## Page 56

and variance
V ar∗(y2) = σ2
z,2 −
[ k∑
i=1
a(i)
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}Ii
]2
+
k∑
i=1
k∑
j=1
(a(i)a(j) − σ2
z,2C(i,j)
2 )
q2∏
d=1
exp{−bd[(x2,i,d − x(d)
2,n+1)2 + (x(d)
2,j − x(d)
2,n+1)2]}Ii,j ,
(3.8)
where
Ii = 1√
1 + 2σ2
1by1
exp
{
−
(µ1 − x(q2+1)
2,i )2
1
by1
+ 2σ2
1
}
and
Ii,j = 1√
1 + 4σ2
1by1
exp
{
− (µ1 −
x(q2+1)
2,i +x(q2+1)
2,j
2 )2
1/2by1 + 2σ2
1
−
by1(x(q2+1)
2,i − x(q2+1)
2,j )2
2
}
.
Proof. Using the law of total expectation, the expectation of Y2 can be expressed as
E∗(y2) = E{E(y2|˜ x2, Yn,2, Yn,1, y1)}
= Ey1(µ2)
= Ey1[β2,0 + cT
n+1,2C−1
2 (yn,2 − β2,0)]
= β2,0 +
∫
f(y1)cT
n+1,2C−1
2 (yn,2 − β2,0)dy1
= β2,0 +
∫ 1√
2πσ2
1
exp
{
− (y1 − µ1)2
2σ2
1
}
cT
n+1,2C−1
2 (yn,2 − β2,0)dy1 (3.9)
where cn+1,2 is deﬁned in (3.4). Let
a = C−1
2 (yn,2 − β2,0)
and let a(i) and c(i)
2 (i = 1, ..., k, where k is the number of design points to model 2) be
the ith entry of a and cn+1,2 respectively. We may then write
cT
n+1,2C−1
2 (yn,2 − β2,0) = cT
n+1,2 a
=
k∑
i=1
c(i)
2 a(i) ,
36

---

## Page 57

which is equivalent to
cT
n+1,2C−1
2 (yn,2 − β2,0) =
k∑
i=1
a(i) exp{−by1(x(q2+1)
2,i − y1)2}
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2} .
This gives
E∗(y2) = β2,0 +
∫ 1√
2πσ2
1
exp
{
− (y1 − µ1)2
2σ2
1
}
k∑
i=1
a(i) exp{−by1(x(q2+1)
2,i − y1)2}
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}dy1 ,
which may be written as
E∗(y2) = β2,0 +
k∑
i=1
a(i)
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}Ii , (3.10)
where
Ii = 1√
2πσ2
1
∫
exp
{
− (y2
1 − 2y1µ1 + µ2
1)
2σ2
1
− by1([x(q2+1)
2,i ]2 − 2x(q2+1)
2,i y1 + y2
1)
}
dy1 .
This is equivalent to
Ii = 1√
2πσ2
1
∫
exp
{
−
(1 + 2σ2
1by1)y2
1 − 2y1(µ1 + 2σ2
1by1x(q2+1)
2,i )
2σ2
1
−
µ2
1 + 2σ2
1by1[x(q2+1)
2,i ]2
2σ2
1
}
dy1 .
Completing the square and moving constants outside the integral gives
Ii = 1√
1 + 2σ2
1by1
exp
{
−
µ2
1 + 2σ2
1by1[x(q2+1)
2,i ]2 −
(µ1+2σ2
1by1x(q2+1)
2,i )2
1+2σ2
1by1
2σ2
1
}
ι ,
where
ι =
∫ 1√
2πσ2
1/(1 + 2σ2
1by1)
exp
{
−
(1 + 2σ2
1by1)
[
y1 −
µ1+2σ2
1by1x(q2+1)
2,i
1+2σ2
1by1
]2
2σ2
1
}
dy1 .
37

---

## Page 58

The integrand in this expression is the density of a normal distribution with mean
µ1+2σ2
1by1x(q2+1)
2,i
1+2σ2
1by1
and variance σ2
1
1+2σ2
1by1
. This integrates to 1, so ι = 1 and therefore
Ii = 1√
1 + 2σ2
1by1
exp
{
−
µ2
1 + 2σ2
1by1[x(q2+1)
2,i ]2 −
(µ1+2σ2
1by1x(q2+1)
2,i )2
1+2σ2
1by1
2σ2
1
}
= 1√
1 + 2σ2
1by1
exp
{
−
2σ2
1by1[x(q2+1)
2,i ]2 + 2µ2
1σ2
1by1 − 4µ1σ2
1by1x(q2+1)
2,i
2σ2
1(1 + 2σ2
1by1)
}
= 1√
1 + 2σ2
1by1
exp
{
−
[x(q2+1)
2,i ]2 + µ2
1 − 2µ1x(q2+1)
2,i
1
by1
+ 2σ2
1
}
= 1√
1 + 2σ2
1by1
exp
{
−
(µ1 − x(q2+1)
2,i )2
1
by1
+ 2σ2
1
}
, (3.11)
which leads to the expression for E∗(y2) given in Theorem 3.1.
The variance of Y2 can be expressed in terms of Y1 using the law of total variance as
V ar∗(y2) = V ar(E[Y2|˜ x2, x1, Yn,2, Yn,1, y1]) + E(V ar[Y2|˜ x2, ˜ x1, Yn,2, Yn,1, y1])
= V ary1(µ2) + Ey1(σ2
2) . (3.12)
The second term of (3.12) is
Ey1(σ2
2) = Ey1[σ2
z,2(1 − cT
n+1,2C2cn+1,2)]
= σ2
z,2 − σ2
z,2
∫
f(y1)cT
n+1,2C2cn+1,2dy1
= σ2
z,2 − σ2
z,2
∫ 1√
2πσ2
1
exp
{
− (y1 − µ1)2
2σ2
1
}
cT
n+1,2C2cn+1,2dy1 (3.13)
We have
cT
n+1,2C2cn+1,2 =
k∑
i=1
(c(i)
2
k∑
j=1
C(i,j)
2 c(j)
2 )
=
k∑
i=1
k∑
j=1
c(i)
2 C(i,j)
2 c(j)
2 ,
where C(i,j)
2 is the ( i, j)th entry of C2. From the deﬁnition of cn+1,2 in equation (3 .4)
and the form of the Gaussian correlation function in equation (2.2), we can express c(i)
2
and c(j)
2 as the products of several exponential functions:
38

---

## Page 59

c(i)
2 = exp{−by1(x2,i,p+1 − y1)2}
q2∏
d=1
exp{−bd(x(d)
2,i − x(d)
2,n+1)2} ,
with an identical expression for c(j)
2 except that every subscripted i is replaced with a
j. Substituting this into (3.13) and grouping exponential terms gives
Ey1(σ2
2) = σ2
z,2 − σ2
z,2
k∑
i=1
k∑
j=1
C(i,j)
2
q2∏
d=1
exp{−bd[(x(d)
2,i − x(d)
2,n+1)2 + (x(d)
2,j − x(d)
2,n+1)2]}Ii,j ,
where
Ii,j = 1√
2πσ2
1
∫
exp
{
− (y1 − µ1)2
2σ2
1
}
exp{−by1(x(q2+1)
2,i − y1)2}
exp{−by1(x(q2+1)
2,j − y1)2}dy1 .
This can be rewritten as
Ii,j = 1√
2πσ2
1
∫
exp
{
−
(1 + 4σ2
1by1)y2
1 − 2y1(µ1 + 2σ2
1by1x(q2+1)
2,i + 2σ2
1by1x(q2+1)
2,j )
2σ2
1
+
µ2
1 + 2σ2
1by1[x(q2+1)
2,i ]2 + 2σ2
1by1[x(q2+1)
2,j ]2
2σ2
1
}
dy1 .
Completing the square and moving terms which do not depend ony1 outside the integral
leads to
Ii,j = 1√
1 + 4σ2
1by1
exp
{
−
µ2
1 + 2σ2
1by1([x(q2+1)
2,i ]2 + [x(q2+1)
2,j ]2)
2σ2
1
}
exp
{
−
(µ1 + 2σ2
1by1x(q2+1)
2,i + 2σ2
1by1x(q2+1)
2,j )2
2σ2
1(1 + 4σ2
1by1)
}
ιi,j ,
where
ιi,j =
∫ 1√
2πσ2
1/(1 + 4σ2
1by1)
exp
{
−
(1 + 4σ2
1by1)
[
y1 −
µ1+2σ2
1by1x(q2+1)
2,i +2σ2
1by1x(q2+1)
2,j
1+4σ2
1by1
]2
2σ2
1
}
dy1 .
The integrand is the density of a normal distribution with mean
µ1+2σ2
1by1x(q2+1)
2,j +2σ2
1by1x(q2+1)
2,j
1+4σ2
1by1
and variance σ2
1
1+4σ2
1by1
, which integrates to 1 and therefore gives ιi,j = 1. The expression
for Ii,j therefore becomes
39

---

## Page 60

Ii,j = 1√
1 + 4σ2
1by1
exp
{
−
µ2
1 + 2σ2
1by1([x(q2+1)
2,i ]2 + [x(q2+1)
2,j ]2)
2σ2
1
−
(µ1 + 2σ2
1by1x(q2+1)
2,i + 2σ2
1by1x(q2+1)
2,j )2
2σ2
1(1 + 4σ2
1by1)
}
,
which can be rewritten and simpliﬁed to give
Ii,j = 1√
1 + 4σ2
1by1
exp
{
− (µ1 −
x(q2+1)
2,i +x(q2+1)
2,j
2 )2
1/(2by1) + 2σ2
1
−
by1(x(q2+1)
2,i − x(q2+1)
2,j )2
2
}
. (3.14)
Returning to equation (3.12), we must also ﬁnd an expression for the ﬁrst term. This
can be rewritten as
V ary1(µ2) = Ey1(µ2
2) − [Ey1(µ2)]2
and since we have already determined Ey1(µ2) = E∗(y2) earlier in the theorem, only
Ey1(µ2
2) remains to be found. This can be written as
Ey1(µ2
2) = Ey1{[β2,0 + cT
n+1,2C−1
2 (yn,2 − β2,0)]2}
= Ey1[β2
2,0 + 2β2,0cT
n+1,2C−1
2 (yn,2 − β2,0) + {cT
n+1,2C−1
2 (yn,2 − β2,0)}2]
= β2
2,0 + 2β2,0Ey1[cT
n+1,2C−1
2 (yn,2 − β2,0)] + Ey1[{cT
n+1,2C−1
2 (yn,2 − β2,0)}2] .
(3.15)
An expression for Ey1[cT
n+1,2C−1
2 (yn,2 − β2,0)] was derived in (3.9) and (3.10):
Ey1[cT
n+1,2C−1
2 (yn,2 − β2,0)] =
k∑
i=1
a(i)
p∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}Ii ,
where Ii is given in (3.11). To deal with the ﬁnal term of (3.15), we ﬁrst note that
{cT
n+1,2C−1
2 (yn,2 − β2,0)}2 = (cT
n+1,2 a)2
=
k∑
i=1
k∑
j=1
c(i)
2 c(j)
2 a(i)a(j) ,
so
Ey1[{cT
n+1,2a)}2] =
∫
f(y1)
k∑
i=1
k∑
j=1
c(i)
2 c(j)
2 a(i)a(j) dy1 .
Expressing c(i)
2 and c(j)
2 as the products of several exponential functions as above, and
collecting exponential and product terms, this is equal to
40

---

## Page 61

Ey1[{cT
n+1,2a)}2] =
k∑
i=1
k∑
j=1
a(i)a(j)
q2∏
d=1
exp{−bd[(x(d)
2,i − x(d)
2,n+1)2 + (x(d)
2,j − x(d)
2,n+1)2]Ii,j ,
where Ii,j is deﬁned in (3.14). Combining the terms of (3.12) calculated above, and
substituting in the expression for E∗(y2) found in (3.10), gives the ﬁnal result
V ar∗(y2) = σ2
z,2 −
[ k∑
i=1
a(i)
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}Ii
]2
+
k∑
i=1
k∑
j=1
(a(i)a(j) − σ2
z,2C(i,j)
2 )
q2∏
d=1
exp{−bd[(x(d)
2,i − x(d)
2,n+1)2 + (x(d)
2,j − x(d)
2,n+1)2]}Ii,j
For an example of this approach, we consider a chain of two models each taking a
single input. This example ﬁrst appeared in Kyzyurova et al. (2018). The models are
deﬁned by the known deterministic functions
y1 = 3x1,1 + cos(5x1,1) , −0.85 ≤ x1,1 ≤ 1 ,
and
y2 = cos(7y1
5 ) − y1 .
As in the original paper, six equally-spaced design points on x1,1 are used to build
the ﬁrst emulator, with the output values of y1 then taken as the design points for the
second emulator. Prediction across the space of x1,1 was then attempted using both the
Monte Carlo method with a sample size of 10,000, and the theoretical approximation.
The plot obtained from the theoretical approximation is shown in Figure 3.3; this is
virtually identical to those obtained in the previous research. It is also useful to compare
this plot to that obtained using the Monte Carlo method, which can be seen in Figure
3.4. This produces a plot which is almost indistinguishable from the theoretical method,
with one exception: while the empirical variance bands are continuous and noiseless
in Figure 3.3, the corresponding Monte Carlo result in Figure 3.4 has variance bands
which are not completely smooth but instead have small but visible additional peaks
and troughs, in particular when x1,1 is between -1 and 0.5. This suggests that even a
sample size of 10,000 is not suﬃcient to ensure that there is no noticeable Monte Carlo
error in the results obtained.
41

---

## Page 62

Figure 3.3: Prediction from the chain of emulators for y2 against x1,1 using the theo-
retical approximation.
3.4 Extending the simulation-based linked emulator to
longer chains
To extend the simulation framework to chains of more than two models, we can apply
the process described in Section 3.2 iteratively. For example, the posterior predictive
distribution for the third model in the chain can be found from
f(y3|˜ x3, ˜ x2, ˜ x1) =
∫ ∫
f(y3|˜ x3, y2)f(y2|˜ x2, y1)f(y1|˜ x1)dy2dy1 . (3.16)
This result can be further generalised to chains of any length. The integrals can
be done using a Monte Carlo method as in the two-model case with few changes: one
implementational diﬀerence concerns the way in which variables must be stored within
our code, since we now have multiple emulator outputs over which we must integrate.
We can test the Monte Carlo method on a chain of three closed-form deterministic
functions which depend on a single input:
y1(x1,1) = x1,1 + sin(3πx1,1) , 0 ≤ x1,1 ≤ 1 ;
y2(y1) = y1 − log(1 + y1) ;
y3(y2) = y2 + exp(−2y2) . (3.17)
42

---

## Page 63

Figure 3.4: Prediction from the chain of emulators for y2 against x1,1 using the Monte
Carlo method.
A Gaussian correlation and constant regression function are used in the three em-
ulators, with nuggets of δ = 10−7 and ten design points spaced equally on x1,1. The
predictions from the chain for y3 given x1,1 are shown in Figure 3.5. Note that in this
plot, the legend is omitted for clarity; the black, blue and green lines and the red circles
have the same meaning as in Figure 3.4. The results appear reasonable, with largely
accurate predictions across the input space, and uncertainty typically higher away from
design points.
3.5 Extending the theoretical linked emulator to longer
chains
Consider now a chain of three models in which Y3 is a function of Y2 and some ˜ x3,
and Y2 is a function of Y1 and some ˜ x2. For ease of notation, let
E∗(y3) = E(y3|˜ x3, ˜ x2, ˜ x1, Yn,3, Yn,2, Yn,1)
be the posterior expectation of y3 given the directly controllable inputs, observed data
and the linked emulator. Applying the law of total expectation gives
E∗(y3) = E[E(y3|˜ x3, Yn,3, Yn,2, Yn,1, y2)]
= Ey2(µ3)
=
∫
f(y2)µ3dy2 .
(3.18)
This cannot be solved directly, since the full distribution f(y2) cannot be obtained in
closed form. A seemingly natural alternative is to apply the law of total expectation
43

---

## Page 64

Figure 3.5: Prediction from the chain of emulators for y3 against x1,1 in the three-model
example - simulation method.
again, giving
E∗(y3) = Ey2(µ3)
= Ey1{Ey2[µ3|y1]}
= Ey1{Ey2[µ3|y1]}
= Ey1{Ey2[(β3,0 + cT
n+1,3C−1
3 (yn,3 − β3,0)]}
where the ﬁnal equality holds since, if y1 is conditioned upon, y2 follows a normal
distribution with known mean and variance; this in turn implies that y3 is the output
of a GP emulator in which one input, y2, is known only up to a normal distribution.
The inner expectation is therefore identical to that in (3.9) with the model numbers
within the chain increased by one, so its form is known from (3.7). Substituting this
result gives
E∗(y3) = Ey1
[ 1√
1 + 2σ2
2by2
exp
{
−
(µ2 − x(q3+1)
3,i )2
1/by2 + 2σ2
2
}]
=
∫
f(y1) 1√
1 + 2σ2
2by2
exp
{
−
(µ2 − x(q3+1)
3,i )2
1/by2 + 2σ2
2
}
dy1 . (3.19)
This is still, however, analytically intractable - both the mean µ2 and the variance σ2
2
of the model 2 output y2 depend on y1 in complex ways. Their combined presence in
three separate locations in the integrand of (3.19) means that the approach taken in
the two-model case to reduce the integral to one which can be solved are not applicable
44

---

## Page 65

here. Nor does this result naturally “scale up” to longer chains of models - even if
(3.19) could be solved analytically, this would not mean that a four-model chain could
be handled in the same way, since another application of the law of total expectation
would be required. The same problems apply to calculating the variance of the linked
emulator output, V ar∗(y3), given the directly controllable inputs and the simulator
runs.
A solution to this is provided by using an approximation to the distribution of y2.
When the theoretical results for the mean and variance of a GP emulator with an input
known only up to a normal distribution were introduced in Girard et al. (2002), they
were intended for use in time series analysis for multiple-step ahead forecasting - the
same emulator would be used for each step in the chain. The problem of approximating
the uncertain input at time steps later than the second was the reason for the use of
the normal approximation on the linked emulator output. By Lemma 3.2, we can use
this approach for predictions from chains of three or more models.
Lemma 3.2. Let yr be the output of a chain of r models, where the ﬁnal model is
deﬁned by the equation
yr = ηr(˜ xr, yr−1) .
Let the distribution f(yr−1) be approximated by a normal distribution with mean
µr−1 = βr−1,0 +
k∑
i=1
a(i)
qr−1∏
j=1
exp{−bj(x(j)
r−1,i − x(j)
r−1,n+1)2}Ir−1
i
and variance
σ2
r−1 = σ2
z,r−1 −
[ k∑
i=1
a(i)
qr−1∏
j=1
exp{−bj(x(j)
r−1,i − x(j)
r−1,n+1)2}Ii
]2
+
k∑
i=1
k∑
j=1
(a(i)a(j) − σ2
z,r−1C(i,j)
2 )
qr−1∏
d=1
exp{−bd[(x(d)
r−1,i − x(d)
r−1,n+1)2 + (x(d)
r−1,j − x(d)
r−1,n+1)2]}Ir−1
i,j ,
where
Ir−1
i = 1√
1 + 2σ2
r−2byr−1
exp
{
−
(µr−2 − x(qr−1+1)
r−1,i )2
1/byr−2 + 2σ2
r−2
}
and
45

---

## Page 66

Ir−1
i,j = 1√
1 + 4σ2
r−2byr−2
exp
{
− (µr−2 −
x
(qr−1+1)
r−1,i +x
(qr−1+1)
r−1,j
2 )2
1/(2byr−2) + 2σ2
r−2
−
byr−2(x(qr−1+1)
r−1,i − x(qr−1+1)
r−1,j )2
2
}
.
Then, yr has expectation
E∗(yr) = βr,0 +
k∑
i=1
a(i)
q2∏
j=1
exp{−bj(x(j)
r,i − x(j)
r,n+1)2}Ir
i
and variance
V ar∗(yr) = σ2
z,r −
[ k∑
i=1
a(i)
qr∏
j=1
exp{−bj(x(j)
r,i − x(j)
r,n+1)2}Ii
]2
+
k∑
i=1
k∑
j=1
(a(i)a(j) − σ2
z,rC(i,j)
2 )
qr∏
d=1
exp{−bd[(x(d)
r,i − x(d)
r,n+1)2 + (x(d)
r,j − x(d)
r,n+1)2]}Ir
i,j ,
where
Ir
i = 1√
1 + 2σ2
r−1byr−1
exp
{
−
(µr−1 − x(qr+1)
r,i )2
1/byr−1 + 2σ2
r−1
}
and
Ir
i,j = 1√
1 + 4σ2
r−2byr−1
exp
{
− (µr−1 −
x(qr +1)
r,i +x(qr +1)
r,j
2 )2
1/(2byr−1) + 2σ2
r−1
−
byr−1(x(qr+1)
r,i − x(qr+1)
r,j )2
2
}
.
Proof. Follows directly from the application of Theorem 3.1.
It is informative to examine how this approach compares to the simulation method
for the three-model example in Section 3.4. Using the same experimental design as
before, we evaluate the chain as described above using a Normal approximation to y2
given its theoretical mean and variance. The ﬁnal output y3 is plotted against x1,1 in
Figure 3.6. Again the legend is omitted for clarity; the black and blue lines and red
circles have the same meaning as Figure 3.4. Here, however, the green lines for the error
bounds are the mean plus or minus two standard deviations instead of an empirical
95% prediction interval.
46

---

## Page 67

Figure 3.6: Prediction from the chain of emulators for y3 against x1,1 in the three-model
example - theoretical method.
The results are similar to those seen in Figure 3.5. In particular, the mean of the
linked emulator is extremely similar in both cases. There are however some noteworthy
diﬀerences in the behaviour of the green lines. In general, we would expect that the
prediction interval in the simulation method would be wider than the ± 2 s.d. bands in
the theoretical method, since it takes account of the uncertainty in the process variances
for each of the GP emulators in the chain by integrating them out; the theoretical
method, by contrast, uses plug-in estimates for these parameters, which could have
the eﬀect of underestimating the true prediction variance. While this does occur in
places, there are several locations in the prediction space where the bounds are in fact
wider for the theoretical approach. This could be a result of the simulation method
using a relatively small sample size of 1000 repetitions per prediction point, and the
samples involved happening by chance to contain fewer extreme predictions than would
be expected in general.
3.6 Conclusions
In this chapter, we have presented two methods to make predictions from a chain
of computational models where emulation is required on the individual models in the
chain. Neither approach is entirely new, but both are developed further here than in
previous published work: earlier work on the simulation method has never been for-
malised to the extent presented in Section 3.2, while previous research on the theoretical
method has been focused on the narrower problems of two-model chains or time series
forecasting.
47

---

## Page 68

The methods introduced here form the basis of the remainder of this thesis. Chapters
4 and 5, dealing with experimental design and sensitivity analysis respectively, are both
built around the requirements and capabilities of the theoretical and simulation-based
linked emulators, which diﬀer greatly from those of a single emulator in isolation. It
is these methods which are implemented in code in Chapter 6, and which are demon-
strated on a real problem in Chapter 7 and in a simulation study in Chapter 8. The
alternative of a composite emulator for the entire chain is also considered in later chap-
ters, but for reasons which will become clear when direct comparisons are available, we
do not consider this to be a viable alternative in practice.
The two forms of linked emulator have very diﬀerent properties. The theoretical
method oﬀers exact results for the expectation and variance of the posterior predictive
distribution for the ﬁnal model output under the linked emulator in a two-model chain,
and near-exact results for longer chains - the normal approximation to the outputs of
the intermediate models in Lemma 3.2 is the only reason why the results are not exact.
It has the added beneﬁt of being extremely fast to execute; this is discussed further in
Chapter 6. Its main weakness is the highly restrictive set of assumptions under which
it is valid. Only a Gaussian correlation function may be used, and plug-in estimation
is required for a wide range of parameters of the individual emulators.
The simulation method oﬀers more ﬂexibility. It can be applied to emulators with any
correlation function; diﬀerent models in the chain could even use diﬀerent correlation
functions if desired. The variation arising from the process variance may be taken into
account using a conjugate prior. The correlation parameters could in theory be handled
using MCMC sampling, although this has not been implemented in our research. This
form of linked emulator is however signiﬁcantly more computationally intensive than
the theoretical approach, since it requires a large number of runs from the chain of
emulators. For a long chain with many inputs, very large Monte Carlo sample sizes
may be required. The simulation method is also open to Monte Carlo error if the
sample size chosen is too small, and it is not always possible to know in advance what
sample size is appropriate for a given chain.
The diﬀerences between the two methods will be considered further in Chapter 8,
where we shall demonstrate that even for short chains of relatively simple functions,
the behaviour exhibited by the methods can vary greatly.
48

---

## Page 69

Chapter 4
Experimental design for chains of
multiple models
4.1 Review of existing methods for experimental design
Experimental design for computer experiments concerns the choice of the design
points at which the simulator is run to produce the training data. Choosing the design
points eﬀectively is especially important if the simulator is expensive or time-consuming
to run, as it is then both impractical to run a large experiment and diﬃcult to add
additional design points if the result obtained is unsatisfactory. Intuitively, we would
like the design points to cover the range of the input variables as well as possible, as
for emulation our ability to predict at an unknown point is better the closer the point
is to a design point. This approach is called space-ﬁlling design, and is widely used in
previous literature. There are several techniques to achieve this goal.
The Latin hypercube design (LHD) was proposed by McKay et al. (1979). Given n
design points, the design space χ is divided into n equally-sized intervals for each input
variable , and the points are chosen such that exactly one point lies within each of these
intervals. Such designs are very easy to create; Chapter 3 of Fang et al. (2006), for
instance, described a simple algorithm to do so. Latin hypercube designs are popular
for their good one-dimensional projection properties: Sacks et al. (1989) interprets the
LHD as an extension of stratiﬁed sampling which ensures that the entire range of each
input variable is covered by the design. However, this does not by itself guarantee that
the points will cover the design space well; it is easy to generate an LHD which leaves
areas of the design space poorly covered by the design points.
Another popular approach is to use an optimality criterion to generate a space-ﬁlling
design. The two most common criteria were both proposed in Johnson et al. (1990)
. Let ξ be any possible experimental design in χ, and let d(xi, xj) be the distance
between two points xi, xj. A maximin distance design maximises the criterion
φMm(ξ) = mini̸=j d(xi, xj) , xi, xj ∈ ξ .
49

---

## Page 70

0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8 1.0
x1
x2
Figure 4.1: A maximin Latin hypercube design with 20 design points in two dimensions.
This is equivalent to maximising the minimum distance between any pair of design
points, with the eﬀect of spreading the design points as far across the design space as
possible. This ensures that the design points do not cluster together.
A minimax distance design minimises the criterion
φmM(ξ) = maxx′mini=1,...,n d(x′, xi) , xi ∈ ξ, x′ ∈ χ .
In contrast to the maximin criterion, this minimises the maximum of the distance
between every point in the design space and the nearest design point. This would
appear useful for emulation, as an emulator can make better predictions at points
close to a design point, so the minimax approach means that we can make reasonable
predictions everywhere in the design space. However, minimax designs can be very
computationally expensive to generate: instead of a single optimisation over a discrete
region, we now require two optimisations, one of which is over a continuous space. For
this reason they are less commonly used in practise.
An alternative is the coverage criterion, which is described in more detail by Nychka
et al. (1997). A coverage design minimises the criterion
Ck,l(ξ) =
{ ∑
x′∈S
dk(x′, ξ)
}(1/l)
,
where
dk(x′, ξ) =
{ n∑
i=1
d(x′, xi)k
}(1/k)
,
50

---

## Page 71

k and l are tunable parameters and S is a set of candidate points in χ. The coverage
criterion is much simpler to optimise than the minimax criterion, and can be made to
approximate it: as k → −∞ and l → ∞, Ck,l(ξ) → φmM(ξ).
It is possible to combine the use of an optimality criterion and a Latin hypercube
design: the class of designs which are considered is restricted to the set of possible LHDs,
and the chosen criterion is considered only over this reduced set. The most frequently
used example, primarily for reasons of ease of generation in practise, is the maximin
LHD. Figure 4.1 shows an example of a 20-point maximin LHD in two dimensions.
The ease with which these forms of optimal design can be computed in practice varies
widely between the speciﬁc designs. In general, coverage designs and Latin hypercube
designs can be generated with relatively little computational eﬀort and scale with in-
creasing dimensionality. Maximin and especially minimax designs are signiﬁcantly more
computationally intensive. Nonetheless, there are pre-existing R packages which can
generate all of these designs: coverage designs are supported by the ‘fields’ package,
presented by Nychka et al. (2016); maximin LHDs by the ‘SLHD’ package, presented
by Ba (2015); and maximin and minimax designs by the package ‘minimaxdesign’,
presented by Mak and Joseph (2018).
The designs discussed above require that the number of design points is known in
advance. It is possible that we would instead prefer to increment the number of design
points after observing the results of an experiment for some initial set of points.
This is called sequential or adaptive design, and was recommended for use in computer
experiments in the pioneering paper of Sacks et al. (1989). The major advantage of
such an approach is that the locations of the later design points can be chosen based
on what is already known about both the true function and our initial emulator for
it. For a large number of design points in many dimensions, sequential design may
also be less computationally intensive than optimal single-stage design, since single-
stage methods can suﬀer from the “curse of dimensionality” and become slow for large
problems. Sequential design procedures may still make use of the space-ﬁlling designs
described above, as a space-ﬁlling approach is a natural way to choose the initial set of
design points.
The early work of Sacks et al. (1989) suggests three potential criteria by which the
optimal location for a new design point may be determined, which remain the basis
of many modern sequential design algorithms. Two are based on the Mean Square
Prediction Error (MSPE). For a Gaussian Process emulator this is identical to the
predictive variance, σ∗2(x) (deﬁned in Section 2.2), at an untested input point. The
Maximum Mean Square Prediction Error (MMSPE) is deﬁned as
max
x∈X
σ∗2(x) ,
51

---

## Page 72

the maximum predictive variance of the GP emulator. The Integrated Mean Square
Prediction Error (IMSPE) criterion is deﬁned as
∫
X
σ∗2(x)dx ,
the integral of the predictive variance across the design spaceχ. Both of these measures
would be minimised by a good choice of design point. Also considered is a criterion
based on maximising the expected entropy change as a result of a new design point,
an idea which in the ﬁeld of traditional statistical experimentation dates to Lindley
(1956).
The MMSPE forms the basis of a method derived in MacKay (1992), and nowadays
commonly known as Active Learning - MacKay (ALM). For an interpolating model to
a true simulator, of which a GP emulator is an example, MacKay (1992) shows that
- up to a quadratic approximation - the expected total gain in information about the
simulator is maximised by placing a new design point at the location in the design space
where the MSPE is highest. This supports the intuitive argument that determining the
true value at the location where our knowledge about it is lowest is a good design
principle. However, more recent authors including Beck and Guillas (2016) have noted
that ALM’s tendency to place many points on the boundaries of the experimental design
region can be a weakness of the method, especially in high-dimensional problems.
An alternative algorithm proposed by Cohn et al. (1996), known as Active Learning
- Cohn (ALC), places the new design point at location in the design space which
minimises the expected IMSPE, thereby achieving the greatest expected reduction in
the variance across the design space. For stationary Gaussian process emulators, Seo
et al. (2000) compares the ALM and ALC algorithms, and concludes that ALC is
generally preferable in terms of the ﬁt of the emulator across the design space. The
main drawback of ALC, as highlighted by Billonis and Zabaras (2012) and Jun and
Horace (2009) amongst others, is its high computational cost.
Another approach to sequential design is based on the mutual information of two
random variables, which was ﬁrst used for experimental design by Caselton and Zidek
(1984). The aim is to choose the design points such that the mutual information is
maximised. For use in computer experiments, Krause et al. (2008) introduces an algo-
rithm to maximise the mutual information sequentially; Beck and Guillas (2016) adapt
this to deal with the case where a nugget is used in the Gaussian process, in the pro-
cess introducing a new criterion named Mutual Information for Computer Experiments
(MICE).
52

---

## Page 73

4.2 Single-stage design for chains of emulators
The design phase for multiple computer models faces additional challenges to that for
a single model. When only one model is used, the space for each of the model inputs is
known, and the value of the inputs at the design points can be directly chosen. Neither
of these properties is true for variables such as y1 and y2, which - while acting as inputs
to later models in the chain - depend on the values of the earlier inputs x1,1, x1,2, x2,1
and so on. This leads to diﬃculties in adapting existing design methods to our new
framework.
A natural ﬁrst step in design for a chain of computer experiments is to use a space-
ﬁlling design on the inputs to each model which we can choose directly, and use the
outputs of the simulator runs for the earlier models as the design points for the inputs
y1, y2, ... which come from earlier models in a chain. Since the space of y1 is unknown,
it appears intuitively sensible to use the output of y1 at each of our design points for
model 1 as our design points for y1 in model 2. A ﬁrst issue encountered with this
approach is that, if the second simulator takes more than one input, the values of
the other inputs at the design points must be chosen to avoid clashing with the pre-
determined values of y1. This can be done by generating a space-ﬁlling design on the
new inputs, and permuting the values of y1 to minimise the rank correlation with the
other inputs, which ensures that the eﬀect of y1 is not confounded with that of other
variables. This technique bears some resemblance to the work of Iman and Conover
(1982), which considers inducing desired correlations onto the inputs of a computer
model using rank correlation.
There is however a more signiﬁcant issue with the principle of using the simulator
runs from the ﬁrst model as the design points for y1 and so on. Space-ﬁlling design on
a single model is largely used because it ensures that the input space is relatively well
covered by the design points. When working with multiple models, however, space-
ﬁlling on the inputs which we can choose directly does not guarantee a good spread of
design points on the inputs we cannot directly control. In the simple two-model example
in Section 3.2, the design points were chosen to be space-ﬁlling on the important input
x1,1 and random on the trivial input x1,2, which ensured both that the GP emulator
for the ﬁrst model was able to identify that x1,1 was a signiﬁcant input and that we
were able to make reasonable predictions across the space of x1,1.
This does not, however, translate in general to a space-ﬁlling design for the second
model. Consider a chain of three models deﬁned by the functions
y1(x1,1) = x1,1 + {sin(2πx3
1,1)}3 , −0.5 ≤ x1,1 ≤ 0.5 ;
y2(y1) = {sin(2πy3
1)}3 ;
53

---

## Page 74

and
y3(y2) = sin(πy2) + exp(y2) .
We again use a Gaussian correlation function, constant regression term and nuggets
δ = 10−7, and use the output of y1 and y2 as the design points for these variables when
building emulators for the models to which they are inputs. 20 design points are chosen
for x1,1. These, and the corresponding values of y1 and y2 which go on to form the
designs for the second and third models, are given in Table 4.1 to four decimal places.
x1,1 y1 y2
-0.5 -0.8536 0.3328
-0.4474 -0.5991 -0.9296
-0.3947 -0.4483 -0.1542
-0.3421 -0.3575 -0.0227
-0.2895 -0.2930 -0.0039
-0.2368 -0.2374 -0.0006
-0.1842 -0.1843 0
-0.1316 -0.1316 0
-0.0789 -0.0789 0
-0.0263 -0.0263 0
0.0263 0.0263 0
0.0789 0.0789 0
0.1316 0.1316 0
0.1842 0.1843 0
0.2368 0.2374 0.0006
0.2895 0.2930 0.0039
0.3421 0.3575 0.0227
0.3947 0.4483 0.1542
0.4474 0.5991 0.9296
0.5 0.8536 -0.3328
Table 4.1: Initial experimental design for the three-model example.
Unlike in the examples in the previous chapter, this design is not satisfactory for this
chain of models. As seen in Figure 4.2, while the predictions are good for much of the
design space (with extremely low uncertainty over a large region), there is a noticeable
problem at each extreme of the design space for x1,1. The true function changes quickly
in these regions and there are no more design points than in the rest of the space, with
the result that our predictions are less accurate here. The estimate of the uncertainty
is also lower than it should be, with a 95% prediction interval failing to include the
true value in places.
In this chain, model 2 has large ﬂat regions, and - as can be seen in Table 4.1 - many
of the twenty design points lead to very similar values of y2 ≈ 0. This means that
very little of the space of y2 is covered by the design points. The result is the poor
54

---

## Page 75

Figure 4.2: Prediction from the chain of emulators for y3 against x1,1 in the new three-
model example, highlighting the experimental design issue.
predictions seen in Figure 4.2. Even greater issues could arise if more than one input
existed to the chain as a whole.
In fact, the second function in this chain is so ﬂat that this issue would arise even if
the ﬁrst model did not exist. Suppose the chain instead consisted of the true functions
y1(x1,1) = {sin(2πy3
1)}3, −0.5 ≤ x1,1 ≤ 0.5 ;
y2(y1) = sin(πy1) + exp(y1) .
Figure 4.3 plots the values of y1 arising from the 20 design points of x1,1 given
in Table 4.1, and the spacing of these points across the space of y1, in this simpler
case. Instead of 20 distinct design points, the design on y1 for the second computer
experiment is eﬀectively based on only 11 points, and there are some large gaps between
them. This demonstrates that the output of the simulator runs is not necessarily a good
set of points to use for experimental design in future emulators.
Assuming it is possible to directly choose y1, y2, ... , yn−1 at which we test the
next model in the chain, a simple remedy for this problem exists. A new set of design
points can be constructed for these inputs to later models. This allows y1, y2, ... ,
yn−1 to be treated identically to the other inputs in terms of design, and means that
existing space-ﬁlling design can be used on the later models without diﬃculty. The
interpretation of the process is a little more complex, since the values of yn obtained
from the ﬁnal computer experiment will not necessarily correspond to a speciﬁc set of
inputs ˜ x1, ˜ x2, ..., but this does not hinder the creation of the linked emulator. The only
problem remaining is to determine the range of the input. This can be done by using the
55

---

## Page 76

Figure 4.3: Example of a two-model chain in which space-ﬁling on the input x1,1 does
not lead to a space-ﬁlling design on y1.
largest and smallest values of the output for the previous model as an approximation
to the boundaries of the variable, while constructing a new set of design points.
An additional beneﬁt of this form of experimental design is that we are no longer
forced to choose the same number of design points for each model in the chain. The
models may have vastly diﬀerent computational costs and numbers of inputs, and
instead of ﬁxing the number of design points d for every model, the available resources
may thus be better used by allocating a diﬀerent number of model runs, n1, n2, ...nr
to each of the r models in the chain. A formal method for computer experimentation
using this experimental design approach is given in Algorithm 2.
The stronger performance of this method relative to the naive approach of reusing
the outputs can be seen by applying it to the three-model example presented above. For
simplicity, we keep the number of design points for each model in the chain unchanged
at 20. The new approach nonetheless leads to very diﬀerent designs on y1 and y2.
Together with the design points for x1,1, these are given in Table 4.2.
The results, which can be seen in Figure 4.4, are also substantially diﬀerent. The
uncertainty in the predictions near the middle of the input space is larger, and there
is new uncertainty at the x1,1 design points arising from the design points in the later
emulators no longer necessarily being at the values of y1 and y2 implied by the values
of x1,1 at which the ﬁrst model was run. More importantly, the predictions at the
fast-changing extremes of the true function have improved dramatically. Allowing the
56

---

## Page 77

Algorithm 2: Algorithm for computer experimentation using single-stage ex-
perimental design for a linked emulator
Input: Number of models, r; models in chain, η1, ..., ηr; design for model 1, ξ1;
number of design points for each model, n1, ..., nr; number of inputs to
each later model, q2, ..., qr; matrix of limits for controllable inputs to
each later model, L2, ...,Lr
Output: Experimental designs ξ1, ...ξr for each model in the chain; vector of
outputs y1, ...,yr at the design points identiﬁed for each model in
the chain
begin
y1 ← vector of length n1 ;
for i ← 1 to n1 do
y(i)
1 ← η1(ξ(i)
1 ) ;
// y(i)
1 element i of vector y1; ξ(i)
1 row i of design matrix ξ1
end
for k ← 2 to r do
Ly,k ← vector (min(yk−1), max(yk−1)) ;
ξk ← design of size nk in qk dimensions scaled by relevant values of Lk
or Ly,k ;
yk ← vector of length nk ;
for j ← 1 to nk do
y(j)
k ← ηj(ξ(j)
k ) ;
end
end
end
whole space of y1 and y2 to be covered equally by design points means that the true
shape of the function can be picked out more accurately by the chain of emulators, and
with reduced uncertainty. This is largely because the behaviour of the third model at
values of y2 far away from 0 is better understood, leading to better predictions at the
values of x1,1 which give extreme values of y2.
The method of experimentation presented in Algorithm 2 clearly oﬀers many beneﬁts
when compared to naively using the output values as design points for later models. It
is not, however, the ﬁnal word on experimental design for chains of models. Single-stage
design does not allow us to adapt our designs based on the results of the initial simulator
runs. This is more relevant for a chain of models than for a single model, since the
models may diﬀer in several respects, including computational intensity and the size
of the output variation with respect to their inputs. If this variation is understood in
advance, single-stage design can take account of it, for example by allocating more runs
to the less computationally intensive model. It is perhaps more likely that the variation
will not be understood in advance. For this reason, sequential design is potentially more
useful than single-stage design.
57

---

## Page 78

x1,1 y1 y2
-0.5 -0.8536 -0.8559
-0.4474 -0.7637 -0.7658
-0.3947 -0.6739 -0.6757
-0.3421 -0.5840 -0.5856
-0.2895 -0.4942 -0.4955
-0.2368 -0.4043 -0.4054
-0.1842 -0.3145 -0.3153
-0.1316 -0.2246 -0.2252
-0.0789 -0.1348 -0.1351
-0.0263 -0.0449 -0.0450
0.0263 0.0449 0.0450
0.07894 0.1348 0.1351
0.1316 0.2246 0.2252
0.1842 0.3145 0.3153
0.2368 0.4043 0.4054
0.2895 0.4942 0.4955
0.3421 0.5840 0.5856
0.3947 0.6739 0.6757
0.4474 0.7637 0.7658
0.5 0.8536 0.8559
Table 4.2: Experimental design for the three-model example using Algorithm 2.
4.3 Sequential design for chains of emulators
There are several new challenges introduced to sequential design by the linking of
multiple models. Firstly, methods for a single model rely on a closed-form expression
of the variance of the emulator output at a given set of inputs, which is only available
if the conditions imposed in Section 3.3 are applied here. The remainder of this section
assumes that this is the case. A simple approach to sequential design for multiple
models is to apply the ALM algorithm to the linked emulator: ﬁnd the maximum value
of the variance of the linked emulator, and add a design point at this location. The
new design point returned will be a point in the space of all of the inputs to any model
which do not depend on an earlier model. For example, in a chain of two models with
inputs ˜ xT
1 and (y1, ˜ x2)T , the design point proposed will be a set of values for ˜ x1 and ˜ x2.
This will therefore require both simulators to be run - the ﬁrst at the set ˜ xT
1 proposed
by the sequential design algorithm, and the second at the value of y1 obtained from
this run and the value of ˜ x2 found by the algorithm.
The problem can be visualised by considering the variance of the linked emulator
in an example with two models. The ﬁrst model takes a single input x1,1 and returns
output y1. The second model takes two inputs, y1 and x2,1, and returns output y2. We
are interested in the variance of the emulator for y2 given (x1,1, x2,1)T . We consider the
system deﬁned by the functions
y1 = 3x1,1 + cos(5x1,1), −1 ≤ x1,1 ≤ 0.85 ;
58

---

## Page 79

Figure 4.4: Prediction from the chain of emulators for y3 against x1,1 in the new three-
model example with space-ﬁlling designs on each input. Note that here the red points
are only the design points used for x1,1; the resulting values of y1 and y2 may not
correspond to design points for those variables.
y2 = [sin(2πy3
1)]3 + sin(πx2,1), −2.5 ≤ x2,1 ≤ 0.9 .
The emulators use a Gaussian correlation function, with the regression coeﬃcients and
process variance estimated using maximum likelihood estimation and plugged in di-
rectly. This allows the theoretical method to obtain the variance of the linked emulator
to be used.
For illustrative purposes, we consider two diﬀerent initial design strategies. Six design
points are chosen for model 1, using equal spacing on x1,1. First, the outputs y1 are
used as the design points for the second model, combined with six equally spaced values
of x2,1 on the same range; of the 720 ways in which the two sets of values could be
combined, the one with the least correlation between the two inputs is chosen. The
variance of the linked emulator is plotted as a function of x1,1 and x2,1 in Figure 4.5,
with the design points for x1,1 (in the ﬁrst computer experiment) and x2,1 (in the
second experiment) marked in black. This is similar to a standard plot of the variance
of a single Gaussian process emulator in two dimensions, with a variance of zero at the
design points, and much larger values as the distance from the design points increases.
Away from the design points, parts of the variance surface is relatively ﬂat, with many
values close to the maximum value of 1.4695. This could make optimisation somewhat
diﬃcult, but suggests that many possible locations for a new design point would be of
roughly equal value.
In the second instance, a maximin Latin hypercube design is used on for the second
computer experiment, with the ranges of the two inputs taken from the output of the
59

---

## Page 80

0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
−1.0 −0.5 0.0 0.5
−2
−1
0
1
2
x11
x21
Figure 4.5: Variance of the linked emulator for y2 given x1,1 and x2,1 under the ﬁrst
initial design.
simulator runs from model 1. The variance is given in Figure 4.6. No design points
are marked here, since there is no unique pair of inputs ( x1,1, x2,1)T at which the full
chain of models has been run; rather, we have an equally spaced set of values of x1,1
at which the ﬁrst model was run, and a set of values of x2,1 at which the second model
was run in tandem with values of y1 which do not necessarily correspond to the values
of y1 obtained when the ﬁrst model was run.
0.00
0.01
0.02
0.03
0.04
0.05
0.06
0.07
−1.0 −0.5 0.0 0.5
−2
−1
0
1
x11
x21
Figure 4.6: Variance of the linked emulator for y2 given x1,1 and x2,1 under the second
initial design.
In general, the variances are much lower than in the previous plot, with the largest
observed variance now below 0.07 - less than 5 % of the maximum variance under the
previous design. This is a result of the new design strategy, which allows for much more
information about the behaviour of the second model to be obtained. However, this
change also makes the plot more diﬃcult to analyse, as the areas of lowest variance do
60

---

## Page 81

not always correspond to the locations of design points in the space of x1,1 and x2,1
space. This is understandable: for example, a value of x1,1 at which a design point
was located may have led to a a value of y1 which lies a relatively large distance from
its nearest design points for the second experiment, so there may be relatively large
uncertainty about the behaviour of the linked emulator at this point.
Finding the maximum predictive variance can be done relatively easily using the
"optim" function in R, although care must be taken to ensure that the number starting
points for the optimisation is large enough that the global optimum is found. Doing this
for the example shown here results in a maximum of x1,1 = 0.8500, x2,1 = 0.5468 with a
variance 0.0686. A simple sequential design method would now run the ﬁrst simulator
at x1,1 = 0 .8500, store the result ynew
1 obtained from this model run, and run the
second model at the pair ( ynew
1 , 0.5468)T . It is clear that a set of linked simulator runs
at this point would have a beneﬁcial eﬀect on the quality of the linked emulator, since
the variance of the emulator output would be reduced at the point where it is highest.
In the following section, we discuss possible ways to improve upon this approach by
taking account of the potential diﬀerences between the simulators in the chain.
4.4 Conclusions
In this chapter, we have reviewed methods for experimental design for computer
experiments, and considered how they could be extended to deal with the additional
challenges posed by the framework of a chain of computer models. We have discussed
the reasons why using the output of earlier simulator runs as design points for later ex-
periments is not in general a sensible strategy, and proposed an alternative with respect
to single-stage designs. We also considered the more complex but potentially more re-
warding case of sequential design for chains of computational models, and presented an
example of what a simple approach to this could look like.
There are still signiﬁcant weaknesses associated with the sequential design method
considered above, however. If a very large proportion of the variance in the linked
emulator at the point comes from variance in one emulator in the chain, the method
may lead to resources being used for simulator runs which have little eﬀect on the
linked emulator. In the most extreme example, the value of y1 may be known exactly
at every point in ˜ x1, with all of the uncertainty in y2 at any set of inputs arising from
the second emulator. Unlikely though this case is, the principle it illustrates is likely
to occur in practice for some chains: if one of the simulators is much more complex
than the other and the number of initial design points is chosen to be the same for
each model, the emulator of the more complex simulator is likely to have much greater
uncertainty associated with its predictions.
One solution to this concern is to consider the variance in the individual emulators
at the relevant inputs before running the associated model. The variance in the ﬁrst
61

---

## Page 82

emulator at the proposed set ˜ x1 would be evaluated ﬁrst; if it was now decided not to
run the model, the mean of the emulator output for y1 at this point would be used as
the value of y1 for the next model in the chain. The same process would be performed
for each model in the chain sequentially. This would in theory remove the unnecessary
simulator runs, allowing the available budget to be used to greater eﬀect elsewhere.
The method to determine if the model should be run would reject a model run if the
variance is below a certain threshold. Ideally, this should be chosen as a proportion
of the total variance of the emulator, but it is unclear how this would be done for the
earlier models in the chain, since there is no obvious general relationship between the
variation in y1 and the variation in y2 when the model which links them is unknown
away from its design points.
A related issue is that choosing the point in ˜ x1 which reduces the variance in y2 the
most does not guarantee that the implied value of y1 has the same property. Running
the ﬁrst model to obtain an exact value of y1 given ˜ x1 may remove much of the variance
in y2 immediately, and it is not clear that the obtainedy1 is necessarily the most eﬀective
value at which the second model can be run to achieve the maximum reduction of the
variance of the linked emulator. It may instead be more beneﬁcial to choose a new
point in the design space of all of the inputs to model 2, ( ˜ x2, y1)T , after running the
ﬁrst model.
Further complexities arise when the computational cost of the individual simulators
is taken into account. If one model in the chain is ten times more expensive to run
than another, for instance, a good method for sequential design would not assume that
all of the models should be run equally often. For example, it may be more useful to
run the cheaper model eleven times and the expensive model once than to run both
models twice; the computational cost in both scenarios would be the same.
It may appear that simply looking at the individual emulators instead of the linked
emulator would solve the problems, but this is not the case. This is because improve-
ments to the separate emulators do not translate directly to the linked emulator. An
extreme example occurs in a two-model chain in which y1 is a complex function of ˜ x1,
and y2 is a function of y1 and ˜ x2 in which y1 plays little or no role in the value of y2. If
the second emulator is able to detect from its initial runs that y1 is not an important
input, then reducing the uncertainty in y1 will have no eﬀect on the linked emulator;
the only way to improve the performance of the linked emulator is to add design points
to the second emulator which improve our understanding of the eﬀect of varying ˜ x2 on
y2. The individual emulators therefore cannot safely be used as an analogue for the
linked emulator.
62

---

## Page 83

Chapter 5
Sensitivity analysis
5.1 Introduction
Sensitivity analysis is deﬁned by Saltelli et al. (2008), Chapter 1, as “the study of
how uncertainty in the output of a model can be apportioned to diﬀerent sources of
uncertainty in the model input”. This is distinct from uncertainty analysis, which seeks
only to quantify the uncertainty instead of attribute it to its sources, although the two
are often run in conjunction. Sensitivity analysis is useful for a number of reasons: it
allows us to better understand the nature of a complex model, can help to reveal errors
in the model formulation, establish which factors are most worthy of further research
and may be used for model simpliﬁcation. It is important to determine which of these
is the main focus of a sensitivity analysis beforehand, as the failure to do so can lead
to an unclear outcome of the analysis.
Our work is interested in extending the above deﬁnition of sensitivity analysis to
encompass chains of models in addition to the single-model case. There are two related
problems in the ﬁeld sensitivity analysis for chains of linked models. The ﬁrst concerns
sensitivity analysis for the ﬁnal model in a chain with respect to its own inputs, which
is complicated by the fact that the distribution of the input yn−1 which arises from the
output of an earlier model cannot be chosen directly. The second (and more complex) is
that of sensitivity analysis for the output of the ﬁnal model with respect to the directly
controllable inputs to all of the model in the chain. Before considering these problems,
however, it is necessary to review existing sensitivity analysis techniques for a single
model.
Sensitivity analysis can be subdivided into local and global analysis. Local analysis
uses the partial derivatives of the model to investigate the eﬀect of small changes to
the model inputs. Assuming the derivatives exist, this is computationally simple, but
provides only limited insight into the eﬀects of the inputs. The changes to the inputs
that are of most interest are typically too large for local sensitivity analysis to capture.
Global sensitivity analysis, which we shall focus on, provides much more information
in this respect, but is less straightforward to perform. (Saltelli et al., 2008)
63

---

## Page 84

In its broadest sense, sensitivity analysis encompasses a very wide range of techniques.
For instance, a simple visual representation of the eﬀect of an input variable upon
the model output can be obtained using a scatter plot of the input variable against
the output variable. Performing this for multiple inputs allows us to qualitatively
characterise the relative importance of the input variables (although care must be taken
to account for changes in the other inputs, which may be diﬃcult). This approach is
used on many occasions by Saltelli et al. (2008) as a ﬁrst step before attempting a more
formal sensitivity analysis. Scatter plots however have only limited use for sensitivity
analysis: they require a large amount of interpretation on the part of the researcher
performing the analysis, provide no quantiﬁable measure of uncertainty and cannot
account for the eﬀects of interactions between the inputs.
More formal approaches towards sensitivity analysis aim to quantify the eﬀect of
an input (or set of inputs) numerically. There are still simple methods to do this:
regression analysis, one of the most fundamental methods of applied statistics, can be
viewed within this framework. Standardised regression coeﬃcients provide a measure of
the proportion of variability explained by each input. The problem with this, however,
is that it depends on the relationship between the inputs and the output following pre-
deﬁned structure. If some of the variance explained by the inputs diﬀers in scope from
the assumed relationship, the regression coeﬃcients may fail to give an accurate picture
of the importance of each input. We would prefer our analysis to be independent of
any assumed model.
Functional analysis of variance (FANOVA) extends traditional ANOVA methods to
computational models. The strength of the relationship between the inputs and the
output is quantiﬁed in terms of the eﬀect of the input on the output variance. The
eﬀect of an input or set of inputs is deﬁned by integrating out the other variables; under
certain relatively relaxed conditions, this allows a simple decomposition of the output
variance into the variance of the marginal eﬀects of the inputs and their interactions
(Schonlau and Welch, 2006). Probabilistic sensitivity analysis, which we use as the
basis for our work, follows similar principals to FANOVA - although as we shall see,
this comes with its own challenges.
5.2 Probabilistic sensitivity analysis
Probabilistic sensitivity analysis has been discussed by various authors including
Oakley and O’Hagan (2004); the same approaches are covered by Saltelli et al. (2008),
although the name is not used explicitly. First, we deﬁne some notation. As before,
the inputs to a computational model consist of the vector x = (x1, ..., xq)T . Given a set
of indices κ, the subvector of x containing the elements with these indices is written as
xκ; x−κ is a subvector of x containing all elements not in the set κ. In the applications
we discuss here, κ is the empty set, a single index i or a pair of indexes i, j. The
uncertainty in the input vector x is deﬁned in terms of a probability distribution G(x).
64

---

## Page 85

We treat the simulator output as a random variable Y with expectation E(Y ). The
conditional expectation E(Y |xi) is the expectation of Y when the input xi is ﬁxed;
for two ﬁxed inputs xi and xj, the conditional expectation is E(Y |xi,j), and so on for
larger sets of ﬁxed inputs.
If we wish to understand how a model behaves with regards to its inputs, an impor-
tant step is to decompose the model’s output into a sum of main eﬀects and interactions:
η(x) = E(Y ) +
q∑
i=1
zi(xi) +
∑
i<j
zi,j(xi,j) + ... + z1,2,...,d(x) ,
where
zi(xi) = E(Y |xi) − E(Y ) , (5.1)
and
zi,j(xi,j) = E(Y |xi,j) − E(Y |xi) − E(Y |xj) + E(Y ) ,
with higher-order terms deﬁned similarly. The value of these functions depend, as we
would expect, on the choice of the distribution G. The function zi(xi) is called the main
eﬀect of xi; zi,j(xi,j) is the second-order interaction between xi and xj. Higher-order
interaction terms are similarly deﬁned, although these terms are usually of less interest
in sensitivity analysis. The main eﬀects and second-order interactions, however, provide
useful information on how the model output responds to the inputs. Welch et al. (1992)
were an early example of authors considering this approach.
It can also be useful in probabilistic sensitivity analysis to characterise the sensitivity
of the model output to its inputs in terms of the reduction in the variance of the output
when some of its inputs are ﬁxed. This approach is covered in detail by Chapter 4 of
Saltelli et al. (2008). In general, for a subset of inputs κ, we deﬁne:
Vκ = var{E(Y |Xκ)} , (5.2)
where we treat the non-ﬁxed inputs, denoted as x−κ, as a random variable X−κ. Vκ is
based on the variance of the main eﬀect of the subset of inputs xκ; it is the expected
reduction in the variance of Y when xκ is known. The measure can be normalised to
be scale-invariant by dividing by the total variance var(Y ). The normalised index, Sκ,
is usually referred to as a sensitivity index or Sobol’ index.
For a single input, two special cases of equation (5.2) have been considered to quantify
the reduction in variance associated with the input:
Vi = var{E(Y |Xi)} , (5.3)
65

---

## Page 86

and
VTi = var(Y ) − var{E(Y |X−i)} ,
which can be normalised to give the scale-invariant measures
Si = var{E(Y |Xi)}
var(Y ) ,
and
STi = var(Y ) − var{E(Y |X−i)}
var(Y )
= 1 − S−i .
The measure Vi is based on the variance of the main eﬀect of xi; it is the expected
reduction in the variance of Y when xi is known. In contrast, VTi is the remaining
uncertainty when we know everything other thanxi. A larger value of Vi or VTi (or their
scaled equivalents) indicates that the relevant xi has a larger role in the uncertainty in
Y . Dividing by the total variance var(Y ) transforms the absolute reduction in variance
to a proportion, with the result that
q∑
i=1
Si +
∑
i<j
Si,j + ... + S1,2,...,q = 1 ,
since the variance in the output of a deterministic model is explained entirely by its
inputs. The sum of the total eﬀect indices STi must be at least 1, and is equal to 1
only if the model is perfectly additive; if any interaction exists between any subset of
the inputs, the sum will be greater than 1. It is also true that STi ≥ Si for any i.
When the aim is to establish which factors should be focused on in future with the
aim of reducing uncertainty, Oakley and O’Hagan (2004) state that Si provides the
best measure of this; if precisely one factor could through some method be determined
exactly, the factor with the largestSi should be chosen. This does not necessarily extend
to multiple factors, as the reduction in total variance then depends on the interaction
between the factors as well as their main eﬀects; the second-order interactions Si,j
would also need to be considered.
It is possible to view model decomposition and variance-based sensitivity methods as
complementary tools. Both exist within the same framework, and can thus convey sim-
ilar information in diﬀerent ways. Variance indicators provide a quantiﬁable measure
of the proportion of the output variance explained by an input or set of inputs, which
allows us to easily identify important inputs, but they cannot be used to determine how
the model responds to these inputs. Model decomposition, by contrast, can be used for
66

---

## Page 87

this: by plotting the expected output of the simulator given a ﬁxed input at a range of
values across the input’s range, we can visualise the eﬀect of the input on the output
graphically. This can also be done for pairs of inputs using either three-dimensional
plotting or contour plots, although it is more diﬃcult for higher-order interactions. It
can sometimes be diﬃcult, however, to interpret these plots to determine which in-
puts or interactions are most important; this, together with dealing with higher-order
interactions, is where the Sobol’ indices are most powerful.
To actually compute either Sobol’ indices or model decomposition measures requires
several integrals to be calculated, since a number of expectations and variances are
needed. For instance, to calculate Vi for an input i using equation 5.3, we need to
calculate both the inner expectation (with respect to the other inputs x−i) and the
outer variance (with respect to the input xi). In general, these will not be available an-
alytically, so numerical integration must be used. An adapted Monte Carlo integration
method is typically chosen. Naively, this could be done as follows: a set of points is
chosen from the marginal distribution on the input xi, which we denote as Gi(xi), and
another set of points are chosen from the conditional distribution of the other inputs
x−i given each xi, which we denote as G−i|i(x−i|xi). The inner expectation E(Y |xi)
can then be estimated for each xi, and the variance across these estimates calculated
to give us the ﬁnal indicator.
A weakness of this approach, however, is its computational feasibility. Accurate
estimation of even a single indicator requires a large number of runs of the simulator
at diﬀerent input values. Saltelli et al. (2008), Chapter 4, provides a more eﬃcient
approach which substantially reduces the number of runs required, but even this is not
always suﬃcient: O’Hagan (2006) describes a case in which variance-based sensitivity
analysis requires several million runs, which is prohibitive even for a model of only
moderate computational complexity.
For a complex model which cannot feasibly be run enough times to perform classical
sensitivity analysis, several techniques are suggested by Saltelli et al. (2008), depending
on the nature of the model. If the complexity in the model stems from an extremely
large number of inputs, group sampling can be used: the inputs are grouped together
into a relatively small number of blocks, and the eﬀect of each block is investigated
using the methods described above. This is far more computationally feasible, but can
miss important inputs: if two variables in the same block have eﬀects of similar size
and opposite sign, their combined eﬀect will be small, so the size of the eﬀect of the
block may not accurately reﬂect the importance of the inputs contained within it.
A more nuanced approach is the elementary eﬀects (EE) method, introduced by
Morris (1991) and reﬁned by Campolongo et al. (2007). First, the space for each input
is discretised to ρ levels. The elementary eﬀect of the input xi is deﬁned as
67

---

## Page 88

EEi = (Y |x1, ...xi−1, xi + ∆, xi+1, ..., xk) − (Y |x1, ...xk)
∆ ,
where ∆ is a value in the set
[
1
ρ−1 , 2
ρ−1 , ...,1 − 1
ρ−1
]
; x must be chosen in such a way
that the transformed point x + ∆xi is within the input space for every i. A measure of
the sensitivity of the model output to each input can be obtained by calculating EEi
for each i at a set of l points across the input space and taking the mean of the absolute
value of the elementary eﬀects for i:
µ∗
i = 1
l
l∑
j=1
|EEj
i | .
If an eﬃcient sample of points is chosen, the number of model runs required in
the EE method is far lower than in variance-based sensitivity analysis. Campolongo
et al. (2007) demonstrated that µ∗
i is an eﬀective proxy to STi . Saltelli et al. (2008)
recommend the use of the EE method for input screening for models where the number
of inputs is suﬃciently large that variance-based methods are impractical, but not so
large that group sampling is required. Most authors are wary of using it as a method
for sensitivity analysis in its own right, however: it can only measure the total eﬀect of
an input, not its main eﬀect or the eﬀect of speciﬁc interactions, and the discretisation
step introduces some error into the calculation. It is usually performed as a ﬁrst step
to identify a subset of important inputs, which will then be the subject of a fuller
sensitivity analysis.
While these methods may be very helpful when the number of inputs is very large,
they cannot deal with the case of a model with a relatively small number of inputs which
is extremely computationally intensive to run: neither group sampling nor screening
using the EE method will be an eﬀective method to reduce the number of simulator
runs required. Emulation provides a possible solution.
5.3 Sensitivity analysis using emulation
Based on a small number of simulator runs, we can build a Gaussian Process emulator
using the methods described in Chapter 2, with the correlation parameters estimated
from the data. For the rest of this section, we assume that the regression coeﬃcients
and process variance are integrated out. This emulator can then be used to predict
the simulator output at the much larger number of input conﬁgurations required to
perform sensitivity analysis, overcoming many of the computational issues discussed
above. This approach is presented in detail by Oakley and O’Hagan (2004).
Since a GP emulator provides as its output not a single value but a probability
distribution for the true simulator output for a given set of inputs, the quantities
of interest in sensitivity analysis also take the form of a distribution. We will denote
68

---

## Page 89

expectations, variances and covariances with respect to the posterior distribution for the
GP emulator by E∗, V ar∗ and Cov∗ respectively. We denote by χκ the space of possible
values forxκ, and by χ−κ the space of possible values forx−κ. The marginal distribution
of xκ is called Gκ(xκ); similarly, G−κ|κ(x−κ|xκ) is the conditional distribution of x−κ
given xκ.
The main eﬀects and interactions of the input variables, which are linear functions
of the GP emulator, a posteriori follow non-standardised t-distributions with ν0 + n
degrees of freedom (or n degrees of freedom when a non-informative prior is used).
The means of these posterior distributions for the main eﬀects and interactions can be
found from a general result, given by Oakley and O’Hagan (2004):
E∗[E(Y |xκ)] = Rκ(xκ)ˆβ + Tκ(xκ)C−1(yn − Fˆβ) , (5.4)
where ˆβ is deﬁned for strong prior distributions in (2.6) and for weak prior distributions
in (2.8). Rκ(xκ) is deﬁned as
Rκ(xκ) =
∫
χ−κ
fn+1(x)dG−κ|κ(x−κ|xκ) , (5.5)
the integral of the vector of regression functions at an unseen input conﬁguration with
respect to the distribution of the unknown inputs across the space of these inputs.
Similarly, Tκ(xκ) is the integral of the vector of correlations between the unseen input
conﬁguration and the design points of the computer experiment with respect to the
same distribution and space:
Tκ(xκ) =
∫
χ−κ
cn+1(x)dG−κ|κ(x−κ|xκ) . (5.6)
The fact that the vectors fn+1 and cn+1 are functions of the conﬁguration of model
input The special cases of (5.5) and (5.6) where κ is the empty set are denoted as R
and T respectively, and are deﬁned as
R =
∫
χ
fn+1(x)dG ,
and
T =
∫
χ
cn+1(x)dG .
The posterior expectation of the function when no inputs are ﬁxed then follows from
(5.4) as
E∗[E(Y )] = Rˆβ + TC−1(yn − Fˆβ) . (5.7)
The posterior mean of the main eﬀect of an input xi can be calculated as
69

---

## Page 90

E∗[zi(xi)] = [Ri(xi) − R]ˆβ + [Ti(xi) − T]C−1(yn − Fˆβ) , (5.8)
where zi(xi) is deﬁned in (5.1). For the second-order interaction between inputs xi and
xj, we obtain:
E∗[zi,j(xi,j)] = [Ri,j(xi,j) − Ri(xi) − Rj(xj) − R]ˆβ
+ [Ti,j(xi,j) − Ti(xi) − Tj(xj) − T]C−1(yn − Fˆβ) .
(5.9)
A useful graphical summary of the eﬀect of each input variable on the output can
be obtained by plotting E∗[zi(xi)] against xi for i = 1, ..., q. It is tempting to assume
that the input showing the most variation in this plot is the most important. However,
Oakley and O’Hagan (2004) warn against this interpretation: the input showing the
most variation has the largest value of V ar{E∗[zi(xi)]}, but this is not the same as
E∗{V ar[zi(xi)]}. For this reason it can be useful to also consider the standard deviation
of the posterior distribution for each input. Standard deviations of the t-distributions
for the main eﬀects and interactions can be calculated from another general result of
Oakley and O’Hagan (2004). First, let
R∗(x, x′) = R(x − x′) − cn+1(x)TC−1cn+1(x) + [fn+1(x)T
− cn+1(x)TC−1F](FTC−1F)−1[fn+1(x′)T − cn+1(x′)TC−1F] ,
This is sometimes referred to as the posterior correlation between x and x′, and unlike
the correlation function R(x − x′), it may depend on the locations of the points x and
x′ as well as the distance between them. Given the values of two diﬀerent sets of ﬁxed
inputs, xκ and x′υ, let
Uκ,υ(xκ, x′υ) =
∫
χ−κ
∫
χ−υ
R∗(x, x′)dG−κ|κ(x−κ|xκ)dG−υ|υ(x′−υ|x′υ)
be the integral of R∗(x, x′) with respect to the conditional distributions of the two sets
of unknown inputs. The posterior covariance between the expectation of the simulator
output given the two sets of ﬁxed inputs is then
cov∗[E(Y |xκ), E(Y |x′υ)] = ˆσ2[Uκ,υ(xκ, x′υ) − Tκ(xκ)C−1Tυ(x′υ)T + {Rκ(xκ)
− Tκ(xκ)C−1F}(FTC−1F)−1{Rυ(x′υ) − Tυ(x′υ)C−1F}T ] ,
(5.10)
where the estimate ˆσ2 of the unknown process variance σ2 is
ˆσ2 = c0 + bT
0 V−1
0 b0 + yT
nC−1yn − ˆβ
T
(V−1
0 + FTC−1F)−1 ˆβ
n + ν0 − 2 , (5.11)
70

---

## Page 91

and ˆβ is deﬁned in equation (2.6). Equation (5.11) reduces when weak prior distribu-
tions are used to
ˆσ2 = yT
nC−1yn − ˆβ
T
(FTC−1F)−1 ˆβ
n − 2 ,
where ˆβ takes the simpler form seen in equation (2.8).
In practice, we would generally prefer to plot E∗[E(Y |xi)] (a simple rescaling of
E∗[zi(xi)] in which the mean is not subtracted) to see how the ﬁxed input changes the
expected output in absolute terms instead of in isolation. Similarly, a two-dimensional
contour or level plot can be used to display the shape of the function E∗[E(Y |xi, xj)]
and thus investigate how changing two factors in tandem aﬀects the expected output.
The Sobol’ index Si and the total eﬀect index STi are quadratic functions of the GP
emulator, so their posterior distributions are not t-distributions; indeed, they cannot be
derived analytically. We can, however, obtain the posterior means of the unnormalised
quantities Vi and VTi . In theory, their posterior variances could also be calculated, but
the formulae required to do this are extremely complicated and are omitted by existing
literature on the topic such as the important papers of Haylock and O’Hagan (1996)
and Oakley and O’Hagan (2004).
The posterior means of Vi and VTi , which we denote by E∗(Vi) and E∗(VTi ), can be
found from a result - again given by Oakley and O’Hagan (2004) - for the more general
case of E∗(Vκ) = E∗{V ar[E(Y |xκ)]}. We note as an intermediate step that
Vκ = E[E(Y |xκ)2] − E[E(Y |xκ)]2
= E[E(Y |xκ)2] − E(Y )2 ,
and that we can already calculate E∗[E(Y )2] from the results given in equations (5.7)
and (5.10), since
E∗[E(Y )2] = {E∗[E(Y )]}2 + V ar∗[E(Y )] . (5.12)
Thus E∗(Vκ) can be calculated if we can ﬁnd an expression for E∗{E[E(Y |xκ)2]}. This
is given by
E∗{E[E(Y |xκ)2]} =
∫
χκ
∫
χ−κ
∫
χ−κ
[ˆσ2R∗(x, x∗) + µ∗(x)µ∗(x∗)]
dG−κ|κ(x−κ|xκ)dG−κ|κ(x′−κ|x′κ)dGκ(xκ) ,
(5.13)
where x∗ is a vector containing the elements of xκ and x′−κ (this is not usually equal
to x, as x and x′ are distinct), and µ∗ is given in equation (2.4) for strong prior
distributions and in equation (2.7) for weak priors. Where previously µ∗ was deﬁned
71

---

## Page 92

implicitly in terms of xn+1, in this chapter, we treat µ∗ explicitly as a function, as we
are interested in the posterior mean at multiple untested input conﬁgurations.
Having obtained estimates forE∗(Vκ) and E∗(VTκ ), we can divide them byE∗[var(Y )]
for inference about Sκ and STκ (although it should be noted that this does not give
E∗(Sκ) and E∗(STκ ), which cannot be derived analytically). To obtain E∗[var(Y )], we
use a similar approach to that used to obtain E∗(Vκ):
E∗[V ar(Y )] = E∗[E(Y 2)] − E∗[E(Y )2] .
Equation (5.12) gives us an expression for the second term, so again we need only the
ﬁrst, which can be found from a result from Haylock and O’Hagan (1996):
E∗[E(Y 2)] =
∫
χ
E∗[η2(x)]dG(x)
=
∫
χ
[ˆσ2R∗(x, x) + µ∗(x)2]dG(x) . (5.14)
5.4 Practical issues
There are several practical considerations relating to the calculation of the indices
described above. An in-depth discussion of several of these can be found in Le Gratiet
et al. (2014). This paper recommends the use of a Monte Carlo method for numeri-
cally evaluating the multi-dimensional integrals required for emulation-based sensitivity
analysis instead of a quadrature-based method. This is due to the lower computational
resources required as the dimensionality of the input space increases, the natural exten-
sion of the calculation of the Sobol’ indices to multiple inputs instead of just one, and
the ability to take account of the numerical error arising from the numerical integration
estimates.
Some sensitivity analysis techniques have already been implemented in R. In particu-
lar, the package ‘sensitivity’ (Pujol et al., 2017) includes functions to estimate the
Sobol’ indices ˆSκ using a range of methods - including those based on GP emulation -
in a highly eﬃcient manner based on the work of Le Gratiet et al. (2014). The package
‘tgp’ (Gramacy and Taddy, 2010) also contains functions for both Sobol’ indices and
model decomposition using GP emulation and Monte Carlo methods. However, we
decided not to utilise this existing work but to write our own code instead. The main
reason for this is that the extension to the case of multiple linked models can be more
eﬀectively done using bespoke code. This will be discussed further in Chapter 6.
Following Le Gratiet et al. (2014), we use a numerical method based upon multi-
dimensional Monte Carlo integration (see for example Press and Farrar 1990). The
integration method chosen requires only a sample from the distribution we wish to
72

---

## Page 93

integrate with respect to (for double and triple integrals, two and three samples are
required respectively).
An example of this approach to Monte Carlo integration can be seen in our method
of calculation for the second term of equation (5.13),
E =
∫
χκ
∫
χ−κ
∫
χ−κ
µ∗(x)µ∗(x∗)dG−κ|κ(x−κ|xκ)dG−κ|κ(x′−κ|x′κ)dGκ(xκ) , (5.15)
for which we apply Algorithm 3.
Algorithm 3: Algorithm to calculate an approximate value of (5.15) using
Monte Carlo integration
Input: Monte Carlo sample size, M; marginal distribution Gκ for inputs xκ;
conditional distribution G−κ|κ for inputs x−κ given xκ
Output: Estimate ˆE for the value of E in (5.15)
begin
R ← vector of length M ;
xκ ← sample of size M from Gκ ;
x−κ ← sample of size M from G−κ|κ given xκ ;
x′
−κ ← sample of size M from G−κ|κ given xκ ; // x−κ, x′
−κ independent
samples
for i ← 1 to M do
x(i) ← (x(i)
κ , x(i)
−κ)T ;
x∗(i) ← (x(i)
κ , x′(i)
−κ)T ;
R(i) ← µ∗(x(i))µ∗(x∗(i)) ; // µ∗() defined in ( ??)
end
ˆE ← mean (R) ;
end
In practice, we assume that the distributions on the inputs are independent. This
allows Algorithm 3 to be simpliﬁed by drawing two samples from the full distribution
G of all the inputs x before any sensitivity analysis is performed, and partitioning these
into samples for xκ, x−κ and x′
−κ as required.
To demonstrate our methods in action, we recreate an example given in Oakley
and O’Hagan (2004). This example has 15 inputs split into three categories: the
inputs x1, ..., x5 play very little role in explaining the variance in the model; the inputs
x6, ..., x10 make a small contribution; and the inputs x11, ..., x15 explain the majority
of the variance. Following the original paper, we used 250 design points to ﬁt the
Gaussian process. The expected output E∗[E(Y |xi)] for each xi on the range ( −2, 2)
is shown in Figure 5.1.
73

---

## Page 94

-2 -1 0 1 2
5 10 15
xi
E(Y|xi)
Figure 5.1: Posterior expectation of Y given xi for i = 1, ...,5 (black lines), i = 6, ...,10
(red lines), i = 11, ...,15 (green lines) in the test example.
This plot is extremely similar to that obtained in the original paper. The three sets of
inputs can be clearly distinguished. We also calculated estimates of the Sobol’ indices
Si for each xi; in every case, our result was within 1% of that obtained in the original
paper. The paper does not include content on sensitivity indices or posterior means for
interaction eﬀects, or on uncertainty in the estimates of the posterior means.
Via a small alteration to Algorithm 3, it is also possible to encompass the case where
it is not possible to sample directory from the marginal and conditional distributions
Gκ and G−κ and must instead use importance sampling. If, instead of samples from
the distributions Gκ and G−κ, we have samples from importance distributions Sκ and
S−κ, only one line of Algorithm 3 would change: where µ∗(x(i))µ∗(x∗(i)) is calculated
and stored in R, this would be replaced with
[ Gκ(x(i)
κ )G−κ(x(i)
−κ)G−κ(x′(i)
−κ)
Sκ(x(i)
κ )S−κ(x(i)
−κ)S−κ(x′(i)
−κ)
]
µ∗(x(i))µ∗(x∗(i)) .
5.5 Example: CBR modelling
We present here a relevant example of sensitivity analysis for a single model. The
model considered is an illustrative example model provided by Dstl which has been
simpliﬁed for release to academia. The model predicts the casualty rate in the case
of a hazardous chemical, biological or radiological (CBR) release. It takes ten inputs
including four categorical variables; as these lie outside of the framework introduced in
previous sections, we will take these input to be ﬁxed throughout. The six remaining
inputs which we investigate are: time of release after vaccination, mass of release, wind
74

---

## Page 95

speed, wind direction, number of people in the area, and the radius of the region in
which the people are contained. The units in which these inputs are measured and
the assumed lower and upper bounds on these inputs are given in Table 5.1. These
ranges are identical to those used in earlier work on this model in a Masters thesis by
Plumb (2008); the choice of the lower and upper bounds is explained in this work with
reference to real examples.
Input Units Lower bound Upper bound
Release time seconds 0 72000
Release mass kilograms 0 10000
Wind speed metres per second 0 10
Wind direction degrees 0 360
People - 0 1000
Radius metres 0 2000
Table 5.1: Assumed ranges and units for the inputs to the CBR model, chosen for
consistency with previous research
Additionally, the model requires that release time, wind direction and number of
people are integers. The other three inputs of interest are deﬁned as ﬂoating point
numbers. Wind direction has the additional property of existing on a circle: its lower
and upper bounds are identical in the real world as they correspond to precisely the
same direction. Ideally, we would take account of this in our modelling, but this was
not investigated here.
The output of the model is the predicted casualties as a percentage of the number
of people, rounded to an integer value. Since the output is a percentage, it exists on
a bounded scale. This would pose problems when using a Gaussian process to model
the output, because the assumption that the residuals from the regression are equally
likely to be positive or negative would be violated close to the extremes of the scale.
To overcome this, we rescale the output to a [0 , 1] scale instead of [0 , 100] and apply
a logit transform, which maps the [0 , 1] interval to the entire real line; we then ﬁt a
Gaussian process emulator to the logit of the model output, and rescale our emulator
estimates by applying the inverse transform where necessary.
The experimental designs used for each of the settings described below are maximin
Latin hypercube designs with 50 points, and are obtained using the R package ‘SLHD’
(Ba, 2015). We ﬁt a Gaussian process emulator with a constant mean instead of a
more complex regression term. When ﬁtting the GP emulator to the logit of the model
output, we ﬁrst scale the inputs to the [0 , 1] interval. This should have no eﬀect on the
emulator we arrive at, but avoids the computational diﬃculties which can arise should
the correlation parameter for a variable on a large scale (the release mass input, for
instance) be small; it also ensures that the correlation parameters of the GP are on the
same in each dimension, which makes them easier to interpret. A nugget of δ = 10−7
is used in the emulator to provide computational stability.
75

---

## Page 96

Since our inputs lie in a bounded region, the distribution G on these inputs must
respect these constraints. In the case of a distribution for which some or all of the
inputs follow a normal or gamma distribution, for instance, we must use truncated
versions of the standard distribution. The R package ‘truncdist’ (Novometsky and
Nadarajah, 2016) allows us to do this without diﬃculty.
We begin by considering the CBR model with all six inputs of interest as potential
sources of uncertainty, and ﬁrst set the inputs to be identically distributed. The dis-
tribution we choose is a truncated normal distribution with mean 0.5 and variance 0.2.
The ﬁrst-order Sobol’ indices for this model are given to four decimal places in Table
5.2.
Input ˆSi
x1 0.2051
x2 0.0075
x3 0.0343
x4 0.0008
x5 0.0010
x6 0.7053
Table 5.2: Estimates of ˆSi for each input in the full CBR model
0.0 0.2 0.4 0.6 0.8 1.0
−0.5 0.0 0.5 1.0
xi
E(Y|xi)
x1
x2
x3
x4
x5
x6
Figure 5.2: Posterior expectation of Y given each xi in the full CBR model
The sixth input, radius of the region, appears to explain by far the largest proportion
of the variability. There is also a signiﬁcant contribution from x1, the release time. To
see the eﬀects of the inputs more clearly, we can look at the plot of the posterior
expectation of main eﬀects (Figure 5.2). It is again clear that x1 and x6 are the most
signiﬁcant variables; the average eﬀect of increasing each of these is to reduce the
expected value of the proportion of casualties, although the behaviour at the extremes
of radius is less clear. We can also now more clearly distinguish the eﬀects of the other
inputs: the curve for x3, wind speed, displays a generally negative trend as the value
76

---

## Page 97

0.0 0.2 0.4 0.6 0.8 1.0
−0.5 0.0 0.5 1.0
x6
E(Y|x6)
Figure 5.3: ±2 s.d. bounds on the posterior expectation of Y given x6 in the full CBR
model
of the input is increased, while x2, release mass, has the opposite eﬀect. Fixing inputs
x4 or x5 appears to tell us little about the average value of the output beyond what
is already known from the emulator mean, which is consistent with the extremely low
Sobol’ indices obtained for these two inputs.
It is also useful to consider the uncertainty in our estimates for the expected output
given a ﬁxed input. In this case, there is relatively little variance in the estimates: in
Figure 5.3, we plot the upper and lower bounds of a region within two standard devi-
ations of the expected value of the output given x6. While there is a little uncertainty,
in particular at the extremes of the region, the shape of the function is clear.
The sum of the ﬁrst-order Sobol’ indices is around 0.955, meaning that around 4.5%
of the output variance is not explained by main eﬀects but by higher-order terms.
We can investigate this further by looking at the sensitivity indices for the two-factor
interactions directly; these are given in Table 5.3.
ˆSi,j x2 x3 x4 x5 x6
x1 0 0.0063 0 0 0.0209
x2 - 0 0 0 0.0060
x3 - - 0 0 0.0063
x4 - - - 0 0
x5 - - - - 0
Table 5.3: Estimates of ˆSi,j for each pair of inputs in the full CBR model
The sum of these eﬀects is slightly under 0.04, so the main eﬀects and two-factor
interactions together explain nearly all of the output variation. Of the interaction
eﬀects, only the interaction between x1 and x6 appears to be of any real importance.
This can be investigated by a two-dimensional level plot, which can be seen in Figure
77

---

## Page 98

5.4. This plot is not easy to interpret, but the behaviour is more complex than a simple
combination of their main eﬀects.
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
2.5
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x1
x6
Figure 5.4: Contour plot of the posterior expectation of Y as the inputs x1 and x6 are
varied in the full CBR model
The choice of normal distributions for the six inputs is perhaps unrealistic. There is
no reason, for instance, to think that release time, release mass or radius should be less
likely to take extreme values than they should to be in the middle of their respective
ranges; uniform distributions may therefore be more appropriate. Wind speed is likely
to follow a skewed distribution, with low values making up more of the mass of the
distribution than high ones.
Following this reasoning, we rerun the above example with a diﬀerent set of input
distributions. The existing truncated normal distributions are maintained on inputs
x4 and x5. Inputs x1, x2 and x6 are given uniform distributions. The distribution
for input x3, wind speed, is a truncated gamma distribution with shape parameter 0.4
and scale parameter 2. This distribution is strongly positively skewed; the mean and
median of a truncated gamma distribution with these parameters on the [0 , 1] interval
are around 0.25 and 0.13 respectively.
Table 5.4 gives the Sobol’ index for the main eﬀect of each input, and Table 5.5
the Sobol’ index for each two-factor interaction. Little appears to have changed as a
result of this new approach, although there are some diﬀerences. The proportion of the
variance explained by x6 is somewhat reduced, and that explained by x1 and the x1-x6
interaction has increased. Perhaps surprisingly, the Sobol’ index for x3, which now has
a truncated gamma distribution, is also lower than in the previous example. The main
eﬀect plot (Figure 5.5) shows very little change in the curve for x6, while the curves
for the other inputs are similar in shape to those in Figure 5.2 but with their values
increased throughout. This is explained by the uniform distribution on x6, which gives
78

---

## Page 99

more weight to points at the lower extreme of the distribution, where the output is
generally high. The interaction plot for x1 and x6 (Figure 5.6), is similar to that seen
previously (Figure 5.4).
Input ˆSi
x1 0.2396
x2 0.0077
x3 0.0074
x4 0.0009
x5 0.0009
x6 0.6672
Table 5.4: Estimates of ˆSi for each input in the full CBR model with new input
distributions
0.0 0.2 0.4 0.6 0.8 1.0
−0.5 0.0 0.5 1.0
xi
E(Y|xi)
x1
x2
x3
x4
x5
x6
Figure 5.5: Posterior expectation of Y given each xi in the full CBR model with new
input distributions
ˆSi,j x2 x3 x4 x5 x6
x1 0.0005 0.0067 0 0 0.0440
x2 - 0 0 0 0.0041
x3 - - 0 0 0.0073
x4 - - - 0 0
x5 - - - - 0
Table 5.5: Estimates of ˆSi,j for each pair of inputs in the full CBR model with new
input distributions
Under both sets of input distributions, the relationship between the signiﬁcant inputs
and the output in this example is mostly linear in nature, with little role played by
interactions between the inputs. Indeed, a multiple linear regression model with the
79

---

## Page 100

−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x1
x6
Figure 5.6: Contour plot of the posterior expectation of Y as the inputs x1 and x6 are
varied in the full CBR model - new input distributions
six input variables as predictors is suﬃcient to explain over 90% of the variance in the
output. There is thus little need for the emulator-based sensitivity analysis we apply
here, since a much simpler and faster method is adequate.
Previous research into this model by Plumb (2008) focused on the case where the
radius input is ﬁxed, which produces more complex structures than the ones seen so
far. Following this approach, we ﬁx the radius input to the middle of its range -
1000 metres - and rerun the model with a 50-point maximin Latin hypercube design
on the remaining ﬁve dimensions. As we would expect, the posterior variance in the
output falls dramatically when this is done (to around 30% of its previous value), but
there remains enough variability that sensitivity analysis is both meaningful and useful.
There is still a signiﬁcant linear relationship between the inputs and the output - linear
regression explains slightly under 80% of the total variance - but there is also evidence
of more complex patterns.
Input ˆSi
x1 0.7939
x2 0.0608
x3 0.0918
x4 0.0010
x5 0.0053
Table 5.6: Estimates of ˆSi for each input in the CBR model with ﬁxed radius
With the variable responsible for the majority of the variance in the output no longer
playing a part, new patterns can be observed in the behaviour of the model with respect
to the other inputs. Again beginning with truncated normal (0.5, 0.2) distributions on
each of the ﬁve remaining inputs, the Sobol’ indices for the main eﬀects (Table 5.6)
80

---

## Page 101

ˆSi,j x2 x3 x4 x5
x1 0.0068 0.0110 0 0.0023
x2 - 0.0051 0 0.0008
x3 - - 0 0.0063
x4 - - - 0
Table 5.7: Estimates of ˆSi,j for each pair of inputs in the CBR model with ﬁxed radius
suggest that a large majority of the output variance is explained by input x1, with
smaller contributions from x2 and x3 and the eﬀects of x4 and x5 being negligible.
From Table 5.7, the only interaction term to account for more than 1% of the output
variance is the interaction between inputs x1 and x3, the two variables with the largest
main eﬀects.
0.0 0.2 0.4 0.6 0.8 1.0
−0.4 0.0 0.2 0.4
xi
E(Y|xi)
x1
x2
x3
x4
x5
Figure 5.7: Posterior expectation of Y given each xi in the CBR model with ﬁxed
radius
The main eﬀects plot (Figure 5.7) displays a largely linear negative trend as x1 is
increased, with a somewhat non-linear positive trend for x2 and a more complex eﬀect
as x3 is varied in isolation. Looking at the uncertainty in these estimates for the
two most signiﬁcant variables, we observe somewhat disparate results: there is little
uncertainty in the eﬀect of ﬁxing x1 (Figure 5.8), but substantially wider uncertainty
bounds on x3 (Figure 5.9). This is likely to be a result of the diﬀering amounts of
uncertainty remaining in the output when the two inputs are ﬁxed: around 21% of the
output uncertainty is unexplained once x1 is known, but around 91% is unexplained
when x3 is ﬁxed. The uncertainty in the eﬀect of x3 is enough to make the true shape of
the curve in Figure 5.7 unclear: the turning point in the centre (and to a lesser extent
the increase at the upper extreme of the input range) may not in fact accurately reﬂect
the eﬀect of the input.
81

---

## Page 102

0.0 0.2 0.4 0.6 0.8 1.0
−0.6 −0.2 0.2
x1
E(Y|x1)
Figure 5.8: ±2 s.d. bounds on the posterior expectation of Y given x1 in the CBR
model with ﬁxed radius
0.0 0.2 0.4 0.6 0.8 1.0
−0.2 0.0 0.2
x3
E(Y|x3)
Figure 5.9: ±2 s.d. bounds on the posterior expectation of Y given x3 in the CBR
model with ﬁxed radius
The eﬀect of the varying x1 and x3 in tandem can be seen in the contour plot in
Figure 5.10. The behaviour of the output here is much more complex than in previous
examples, reﬂecting both the strong (and, in the case of x3, non-linear) main eﬀects
of both inputs and the signiﬁcance of the interaction between them. There can be
little uncertainty associated with this plot, since almost 90% of the output variance is
explained by the two inputs.
In this more nuanced example, the choice of input distributions can have a signiﬁcant
eﬀect on the apportioning of the output uncertainty. To demonstrate this, consider
again the second set of distributions used in the previous case: uniform distributions on
x1 and x2, a truncated gamma distribution on x3 and truncated normal distributions on
x4 and x5. The sensitivity indices associated with this choice of distributions for the case
where radius is ﬁxed can be seen in Tables 5.8 (for main eﬀects) and 5.9 (interactions).
82

---

## Page 103

−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
0.8
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x1
x3
Figure 5.10: Contour plot of the posterior expectation of Y as the inputs x1 and x3 are
varied in the CBR model with ﬁxed radius
These are very diﬀerent to those seen with truncated normal distributions on all of the
inputs: the Sobol’ index for the main eﬀects of inputs x1 and x2 are reduced, while
that associated with the main eﬀect of x3 increases dramatically. There are also small
but noticeable increases in the indices for the x1-x2 and x2-x3 interactions.
Input ˆSi
x1 0.6572
x2 0.0454
x3 0.1985
x4 0.0000
x5 0.0000
Table 5.8: Estimates of ˆSi for each input in the CBR model with ﬁxed radius - new
input distributions
ˆSi,j x2 x3 x4 x5
x1 0.0366 0.0113 0 0.0037
x2 - 0.0191 0 0.0026
x3 - - 0 0.0030
x4 - - - 0
Table 5.9: Estimates of ˆSi,j for each pair of inputs in the CBR model with ﬁxed radius
- new input distributions
Considering the substantial nature of these changes, the main eﬀects plot (Figure
5.11) is surprisingly similar to the previous plot in Figure 5.7. While the scale on
which the curves move is substantially diﬀerent for all inputs bar x3, their shapes
do not diﬀer much from the previous case, with the exception of that for x2. The
83

---

## Page 104

uncertainty bounds on the curves for x1 and x3 are so similar to those in Figures 5.8
and 5.9 respectively that there is little need to include them here.
0.0 0.2 0.4 0.6 0.8 1.0
−0.4 0.0 0.2 0.4 0.6
xi
E(Y|xi)
x1
x2
x3
x4
x5
Figure 5.11: Posterior expectation of Y given each xi in the CBR model with ﬁxed
radius - new input distributions
−0.4
−0.2
0.0
0.2
0.4
0.6
0.8
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x1
x3
Figure 5.12: Contour plot of the posterior expectation of Y as the inputs x1 and x3 are
varied in the CBR model with ﬁxed radius - new input distributions.
The interaction between x1 and x3, investigated in the contour plot in Figure 5.12,
is also much the same as that seen before (Figure 5.10). However, the two newly-
signiﬁcant interactions display extremely complex patterns which were not previously
present. Figure 5.13 is a contour plot of the combined eﬀect of varying x1 and x2. This
gives us substantial insight into the behaviour of the model which could not be seen
from the main eﬀects plot or Sobol’ indices. While the main eﬀect of x1 is roughly
linear, when viewed in conjunction with x2, new complexity emerges: the reduction in
expected output as x1 is increased is more pronounced when x2 is close to its extreme
84

---

## Page 105

values, and less so when x2 is nearer to the middle of its range. The curvature in
the eﬀect of x2 can also be seen clearly. The eﬀect of varying x2 and x3 in tandem
(Figure 5.12) is equally complex, although this may be more a result of these two
inputs’ complex main eﬀects than the interaction between them.
−0.4
−0.2
0.0
0.2
0.4
0.6
0.8
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x1
x2
Figure 5.13: Contour plot of the posterior expectation of Y as the inputs x1 and x2 are
varied in the CBR model with ﬁxed radius - new input distributions.
−0.3
−0.2
−0.1
0.0
0.1
0.2
0.3
0.4
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
x2
x3
Figure 5.14: Contour plot of the posterior expectation of Y as the inputs x2 and x3 are
varied in the CBR model with ﬁxed radius - new input distributions.
Finally, we should note that there is some evidence that the Gaussian process emula-
tor does not entirely capture the underlying nature of the true model. Cross-validation
was performed on the two Gaussian process emulators used so far by ﬁtting a GP em-
ulator to 49 points in the design, predicting the output at the remaining point and
comparing this to the true output. While the emulator is usually able to predict the
missing point well, it struggles when the number of people is extremely low. Additional
85

---

## Page 106

model runs reveal that the expected casualty proportion is consistently high when num-
ber of people is low, and consistently lower once it increases beyond a certain threshold
(approximately 50, or 5% of the way into its range). An emulator based upon a sta-
tionary Gaussian process struggles to capture this as it assumes that the correlation
in each dimension depends only on the distance between a pair of points, not on the
actual values of the variable at the two, which does not appear to be the case for this
input. Number of people (input x5 in the above example) was deemed to explain a
trivial proportion of the output variance in all scenarios considered here, which may
not reﬂect its true eﬀect on the simulator output.
5.6 Sensitivity analysis for multiple models
We now return to the two related problems in sensitivity analysis for a chain of
models introduced at the beginning of this chapter, namely sensitivity analysis for the
ﬁnal model in a chain with respect to its own inputs, and sensitivity analysis of the full
chain of models with respect to the directly controllable inputs only.
5.6.1 Sensitivity analysis for the ﬁnal model in a chain with respect
to the model’s inputs
Sensitivity analysis on the ﬁnal model is in principle the same as for a single-model
case. The ﬁnal model is known up to a standard Gaussian process emulator, so posterior
estimates of the main eﬀects, interactions and Sobol’ indices for each of its inputs can
in theory be determined using the methods described above. All of these approaches,
however, require integration with respect to the distribution of the inputs to the ﬁnal
model. This means that there is an additional complication arising from the nature of
the input yn−1. While the distributions on the other inputs can be chosen using any
means discussed earlier in this chapter, we have less freedom to do this for yn−1, since
its distribution is determined by the earlier models in the chain (and, implicitly, by the
distributions of the controllable inputs to the earlier models).
This apparent stumbling block can, however, be overcome using methods already
discussed in this thesis. First, we recall that the Monte Carlo integration approach
introduced in Section 5.4 requires only a sample from the joint distribution of the
inputs to the model; we are not required to have an analytical form for this distribution.
Assuming that the inputs to the ﬁnal model are independent, and that the distributions
for its controllable inputs are known, sensitivity analysis can therefore be conducted if
we can obtain a sample from the distribution of yn−1.
In Chapter 3, we introduced two methods for prediction from a chain of multiple
models. This chain can be of any length, so these methods can be applied to a chain
of n − 1 models instead of n. Thus, it is possible to predict for yn−1 given the inputs
to the ﬁrst n − 1 models. This can be used to generate a sample from the empirical
86

---

## Page 107

distribution for yn−1. First, draw a sample from the joint distribution of ˜ x1, ...,˜ xn−1; as
in previous sections, this can be simpliﬁed by assuming the inputs are independent. For
each input conﬁguration, draw a single value for yn−1. For the simulation method, this
means running each input conﬁguration once and storing the result. For the theoretical
method, the mean and variance should be calculated, and a single value drawn from the
implied approximate normal distribution. The result is a sample from the distribution
of yn−1, which can then be used for sensitivity analysis on yn given the inputs to model
n.
A simpler result holds in the case of a chain of two models. Here, to conduct sensitiv-
ity analysis for model 2, a distribution is required for the uncontrollable input y1. Since
y1 is the output of a model which can be approximated directly by a Gaussian process
emulator, a probability distribution for y1 is available at each possible conﬁguration of
its inputs ˜ x1. A distribution for y1 can therefore be constructed directly if the joint
distribution of its inputs is known.
While the inputs to the ﬁrst n − 1 models in the chain, ˜ x1, ...,˜ xn−1, do not appear in
the ﬁnal sensitivity analysis for yn, they nonetheless play a signiﬁcant role in its results.
The implied distribution on yn−1 depends strongly on the choices of the distributions
from which the samples of ˜ x1, ...,˜ xn−1 are drawn. As seen in Section 5.5, changing
the input distributions in a single model can signiﬁcantly aﬀect the sensitivity analysis
results, so obtaining a reasonable empirical distribution foryn−1 is extremely important.
It is therefore crucial that the distributions of the controllable inputs to earlier models
are chosen in a way which reﬂects their true behaviour.
0.0 0.2 0.4 0.6 0.8 1.0
0.85 0.95 1.05 1.15
xi
E(Y|xi)
y2
x3,1
Figure 5.15: Posterior mean for y3 given y2 (black) and x3,1 (red) in the simple three-
model example chain
87

---

## Page 108

To test this technique, consider the three-model chain introduced in equation (3.17).
This chain is a function of a single input x1,1, so sensitivity analysis is not meaningful
as all of its variation is explained by this single input. However, the chain could be
rewritten to include several dummy inputs which do not aﬀect the ﬁnal output:
y1(x1,1) = x1,1 + sin(3πx1,1) , 0 ≤ x1,1 ≤ 1 ;
y2(y1, x2,1) = y1 − log(1 + y1) ;
y3(y2, x3,1) = y2 + exp(−2y2) . (5.16)
Sensitivity analysis on model 3 can be conducted with respect to its inputs, y2 and
x3,1, using the technique described above. For simplicity, we assume a uniform distri-
bution on each of the controllable inputs to the chain. For x1,1, the upper and lower
bounds of the uniform distribution are 0 and 1 respectively. For x2,1, the range is taken
to be same as that seen in the output of the simulator runs for y1; this avoids biasing
our results by having the two variables be on vastly diﬀerent scales, since we do not
use scaled inputs for this chain (as will be done in Chapter 7 for the real example).
Similarly, the range for x3,1 is chosen using the simulator runs for y2.
We ﬁt emulators with constant regression terms and Gaussian correlation functions
to the three models, and use the theoretical method for prediction from a two-model
chain to obtain a sample from the distribution of y2. 10 design points for each model
are chosen from a maximin Latin hypercube design, with algorithm 2 applied to ensure
the designs for y1 and y2 are reasonable. Standard results from Sections 5.3 and 5.4
then allow posterior estimates of the main eﬀects, interaction and Sobol’ indices to be
determined.
The posterior means of the main eﬀects of the two inputs can be seen in Figure 5.15.
The results conform entirely to what would be expected for a model in which only one
input has an eﬀect. Fixing the input x3,1 provides no information about the expected
output of y3, thus producing a ﬂat line at the unconditional expected value of y3, while
ﬁxing y2 recreates exactly the shape of the true function given in equation (5.16). The
Sobol’ index for y2 is Sy2 = 1 to ﬁve decimal places, while the index for x3,1 is Sx31 = 0,
and index for the interaction between the two inputs is zero to ﬁve decimal places. This
tells us that all of the variation in y3 is explained by y2, which we know is true for this
model.
This form of sensitivity analysis is limited, however, as it tells us little about the
eﬀects of the inputs x1,1, x1,2 and x2,1 on y3. It is useful to know that x3,1 plays no
role in explaining the variation in y3, and it is useful to know (through the posterior
expectation of the main eﬀect) the relationship between y2 and y3, but this is by no
88

---

## Page 109

means the full story. From this analysis alone, it would not be possible to determine that
x1,1 explains all of the variation iny3, and that x1,2 and x2,1 play no role. The same issue
applies for chains in which more than one (and potentially all) of the controllable inputs
have an eﬀect on the ﬁnal output; analysis of the ﬁnal model provides no information
about the relative importance of the inputs to earlier models. For this reason, a full
sensitivity analysis for the chain as a whole is more informative.
5.6.2 Sensitivity analysis for the ﬁnal output of a chain with respect
to the controllable inputs
When sensitivity analysis is required on the entire chain, the situation becomes signif-
icantly more complex. We are still interested in many of the same quantities as for the
single-model case, but the results described in the above sections no longer hold. Let E∗
denote an expectation with respect to the linked emulator, and x = (˜ x1, ˜ x2, ...,˜ xn)T be
the set of all directly controllable inputs to the chain of models. To assess, for example,
the main eﬀects and interaction eﬀects of the input variables, we are still interested in
E∗[E(Y |xκ)] = E∗
∫
χ−κ
η(x)dG−κ|κ(x−κ|xκ) (5.17)
but the result given in equation (5.4) for a single GP emulator no longer holds. The
additional complexity of a linked emulator framework - in which there are, for example,
multiple correlation matrices coming from each individual emulator, all of which refer to
diﬀerent sets of inputs - means that no simple closed-form expression for E∗[E(Y |xκ])
can be found, as the outer expectation E∗ is now with respect to a much more compli-
cated function.
Clearly, the only solution to this is to estimate the integral in (5.17) using another
method. The most natural way to do this is a numerical approximation by direct
simulation from the linked emulator. Since the linked emulator is substantially quicker
to run than the chain of models, this is more computationally feasible than running
the models themselves, and is a sensible choice where no theoretical results about the
linked emulator exist. For long chains with relatively large input spaces, however, this
method quickly becomes infeasible, as simulation from the linked emulator is slower
than that for a single GP emulator.
The theoretical results for the mean and variance of the linked emulator output
introduced in Chapter 3 provide a partial alternative. Using our notation for sensitivity
analysis, the posterior mean of the emulator output at an input set x can be written
as E∗[η(x)]. Let F [η(x)] be the distribution of Y = η(x) under the linked emulator.
We have
89

---

## Page 110

E∗[E(Y |xκ)] = E∗
∫
χ−κ
η(x)dG−κ|κ(x−κ|xκ)
=
∫ ∞
−∞
∫
χ−κ
η(x)dG−κ|κ(x−κ|xκ)dF [η(x)]
=
∫
χ−κ
∫ ∞
−∞
η(x)dF [η(x)]dG−κ|κ(x−κ|xκ)
=
∫
χ−κ
E∗η(x)dG−κ|κ(x−κ|xκ)
= E[E∗(Y |xκ)] . (5.18)
where the third equality holds because, as in the single-emulator case (see for example
Oakley and O’Hagan, 2004), the distribution of ˆY (x) is independent of that of x−κ|xκ
so the order of integration can be changed by a special case of Fubini’s theorem. We
can thus use the theoretical value for E∗[η(x)] to calculate the posterior expectations
of the main eﬀects and interactions of the inputs to a linked emulator. A numerical
method is still required for the integral over χ−κ, but this can be done using essentially
the same method described in Section 5.4. Similarly, we can obtain the expectation of
Y with no ﬁxed inputs by
E∗[E(Y )] =
∫
χ
E∗[η(x)]dG(x) .
Consider a two-model chain consisting of the models
y1(x1,1) = x1,1 + sin(3πx1,1) , 0 ≤ x1,1 ≤ 1 ;
y2(y1, x2,1) = y1 − log(1 + y1) ;
This is a subset of the chain deﬁned in equation (5.16) in which the third model has
been removed. It depends only on its ﬁrst input x1,1; the input x2,1 does not aﬀect the
output y2. Using the method described above, we can generate a plot of the posterior
mean of y2 given x1,1 and x2,1 with respect to the linked emulator. This is shown in
Figure 5.16.
The plot demonstrates that ﬁxing x2,1 provides no information about y2, and shows
the relationship between x1,1 and y2 exactly. For a model with multiple important
inputs, however, the plot may be less easy to interpret, and could be misleading as the
variance is not taken into account.
The situation for the variance of the main eﬀect or interaction,
V ar∗[E(Y |xκ)], is more complicated. Since
V ar∗[E(Y |xκ)] = E∗{[E(Y |xκ)]2} − {E∗[E(Y |xκ)]}2 ,
90

---

## Page 111

0.0 0.2 0.4 0.6 0.8 1.0
1.0 1.5 2.0 2.5
xi
E(Y|xi)
x1,1
x2,1
Figure 5.16: Posterior mean with respect to the linked emulator for y2 given x1,1 (black)
and x2,1 (red) in a subset of the three-model example chain containing only the ﬁrst
two models
and the second term is the square of what was already calculated in (5.18), we require
an expression for E∗{[E(Y |xκ)]2}. This is equivalent to
E∗{[E(Y |xκ)]2} = E∗
{[ ∫
χ−κ
η(x)dG−κ|κ(x−κ|xκ)
]2}
,
but here the outer expectation with respect to the linked emulator cannot be taken
inside the integral due to the presence of the squared term. An alternative would be
to note that
[E(Y |xκ)]2 = V ar(Y |xκ) − E[(Y |xκ)]2
and attempt to obtain expressions for E∗[V ar(Y |xκ)] and E∗{E[(Y |xκ)]2}. The same
problem arises again, however, and no theoretical result for these expressions is possible
given only E∗[η(x)] and V ar∗[η(x)].
In Section 5.3, the variance of the main eﬀect or interaction was found using the
general result in (5.10), attributable to Oakley and O’Hagan (2004). This result requires
knowing the covariance between the output of two independent realisations of the GP
emulator, so a similar approach could in theory be used for a linked emulator. A
derivation of the same covariance for the case of a linked emulator has to date not been
possible; this is discussed further in Chapter 9.
To obtain an estimate of the posterior expectation of the sensitivity indices for a set
of inputs xκ, we require
ˆSκ = E∗{V ar[E(Y |xκ)]}
E∗[V ar(Y )] .
91

---

## Page 112

As was the case for a single GP emulator, this is not an exact expression for Sκ since
the ratio of an expectation does not equal the expectation of a ratio. To calculate the
denominator, note that
E∗[V ar(Y )] = E∗[E(Y 2)] − E∗{[E(Y )]2}
= E[E∗(Y 2)] − E∗{[E(Y )]2}
= E[V ar∗(Y )] + E{[E∗(Y )]2} − E∗{[E(Y )]2}
= E[V ar∗(Y )] + E{[E∗(Y )]2} − V ar∗[E(Y )] − {E∗[E(Y )]}2
= E[V ar∗(Y )] + V ar[E∗(Y )] − V ar∗[E(Y )] (5.19)
Again, however, this is dependent on V ar∗[E(Y )], for which no result is currently avail-
able. Similar issues arise when attempting to derive an expression for the numerator,
and no result for this currently exists. The case of sensitivity analysis for a chain of
emulators which do not satisfy the constraints required for the theoretical means and
variances to be calculated also remains open unless direct simulation can be used.
5.7 Conclusions
This chapter reviews existing approaches to sensitivity analysis for a single compu-
tational model, and presents approaches to extend these to a chain of models. We
begin with a broad view of sensitivity analysis in its many forms, before focusing on
the speciﬁcs of model decomposition and variance-based sensitivity analysis, and how
they can be used within the framework of Gaussian process emulation. These tech-
niques were then applied to a model for casualties of a CBR release, demonstrating the
valuable insights which can be provided by sensitivity analysis in understanding the
behaviour of a model with respect to its inputs. This example is directly relevant to
our eventual research goals: Chapter 7 also deals with casualties from a CBR release,
but using a chain of models instead of a “one-hit” setup.
Our attempts to create methods for sensitivity analysis for a chain of models were
only partially successful. Nevertheless, a concrete method for sensitivity analysis for
the ﬁnal model in the chain is a valuable tool. It is noteworthy that this method is
only possible when combined with Monte Carlo integration for a single emulator; the
use of an alternative numerical method such as quadrature would complicate matters
signiﬁcantly, since only an empirical distribution is available for the input yn−1. As
discussed in Section 5.4, however, there are already several practical advantages to the
use of a Monte Carlo approximation to the unknown integrals even for the simpler
single-model case.
With regards to sensitivity analysis for the chain as a whole, there is still much work
to be done. Posterior estimates of the main eﬀects and interactions of the directly
92

---

## Page 113

controllable inputs are undoubtedly useful, but limited in scope. No quantiﬁcation of
the uncertainty in these estimates is possible, and reliable estimates of the Sobol’ indices
cannot be derived from them; the naive approach of simply estimating the Sobol’ index
of an input i by
E∗(Vi) ≈ V ar{E∗[E(Y |xi)]}
is not recommended since it takes no account of the variance in the estimate of the main
eﬀect. A full derivation would appear to depend on a theoretical result for the posterior
covariance between two outputs from the ﬁnal model under the linked emulator, which
has not so far been possible to determine, although the beginnings of a derivation are
given in Chapter 9.
Additionally, the posterior estimate of the main eﬀects and interactions presented
here is only possible when closed-form expression for the mean and variance of the ﬁnal
model output under the linked emulator are available, which is only the case under
the fairly restrictive set of assumptions given in Theorem 3.1. In terms of sensitivity
analysis for chains of emulators which do not satisfy these assumptions, there are several
ideas which may be of interest, but these require substantial further theoretical and
practical development. They are discussed further in Chapter 9.
93

---

## Page 114

94

---

## Page 115

Chapter 6
Software implementation
6.1 Introduction
The computer code associated with this research project, which was developed inde-
pendently, is written predominantly in the R programming language. Its chief function
is to provide methods for prediction from a chain of Gaussian process emulators. (Meth-
ods for a single GP emulator are also implemented, but these are not discussed here
as their primary use is as part of the process used for a chain.) Both the Monte Carlo
integration-based methods for chains of arbitrary length (see Sections 3.3 and 3.5) and
the theoretical methods to obtain the mean and variance of the linked emulator (see
Sections 3.4 and 3.6) are supported in our code.
The Monte Carlo method is computationally expensive to conduct, and an imple-
mentation entirely in R was found to be infeasibly slow even for relatively small prob-
lems. For this reason, much of the linear algebra and basic calculations required were
moved to the faster C++ language. The R packages ‘Rcpp’ (Eddelbuettel, 2013) and
‘RcppArmadillo’ (Eddelbuettel and Sanderson, 2014) are used to interface between
the two languages. The code requires that the vector of regression coeﬃcients in each of
the emulators is integrated out, and that the correlation parameters are estimated using
a plug-in method. The process variance may be dealt with in either manner; although
these two cases lead to substantially diﬀerent distributions on the emulator output at
each stage, our code was developed to support both methods. The correlation function
may be one of three standard types: Gaussian, Mat´ ern with smoothness parameter
ω = 5/2 and Mat´ ern with smoothness parameterω = 3/2. These were chosen due to
their prior use in single-model emulation packages such as ‘DiceKriging’ (Roustant
et al., 2012).
The theoretical approximation to the linked emulator also makes use of C++, despite
being relatively fast to calculate, as this allows large problems to be tackled in reason-
able time. Separate functions are used for the mean and variance at a prediction point,
and are both called by another function which calculates both. Due to the assumptions
required for the theoretical results to hold, only a Gaussian correlation may be speciﬁed
95

---

## Page 116

, and the regression coeﬃcients and process variance must be single values speciﬁed by
the user.
In addition, our code also includes methods for sensitivity analysis for the ﬁnal
model in a chain. This combines the multiple model prediction methodology (to obtain
a sample from the distribution for the input yn−1) with traditional emulation-based
sensitivity analysis for a single model.
The full set of functions used in our work are available on Github at https://
github.com/StephenGow/Thesis-Code.
The remainder of this chapter focuses on the practical uses of the code. The vast
majority of the 23 R and 34 C++ functions used are intended for “behind-the-scenes”
calculations, and should not need to be called directly by an end user. There are
four R functions which should be used directly - one each for prediction from a linked
emulator using simulation, prediction from a linked emulator using the theoretical
method, sensitivity analysis for the ﬁnal model in a chain, and posterior expectations
of the ﬁnal output of a chain given the directly controllable inputs. These are described
in detail in Section 6.2, with the code required for their usage in an example chain
presented in Section 6.3.
6.2 Details of usage
6.2.1 Prediction from a linked emulator using simulation
Function Name
MM pred simu
Description
Prediction from a linked emulator via the simulation method.
Arguments
• sampsize: Monte Carlo sample size.
• predpts: List of matrices of the prediction points for the controllable inputs to
each model.
• loc vec: Vector of locations of the variable yk−1 in the emulator for yk.
• designs: List of design matrices for the individual emulators.
• b vecs: List of vectors of correlation parameters for the individual emulators.
• res vecs: List of vectors of results from the simulator runs for each computer
experiment.
96

---

## Page 117

• F mats: List of matrices of regression functions for the individual emulators.
• corr mats: List of correlation matrices for the individual emulators.
• cov type: String determining the correlation function of the emulators. Op-
tions are a Gaussian correlation (“Gaussian”), Mat´ ern correlation with ω = 3/2
(“Matern 32”), and Mat´ ern correlation withω = 5/2 (“Matern 52”).
• scale params: Optional list of location and scale shift parameters for the second
and later emulators in the chain.
Notes
This function assumes that the regression coeﬃcients and process variance are inte-
grated out, and thus samples from a t-distribution for the output of each model in the
chain.
For the predpts input, entry k of the list should be a matrix containing the prediction
locations for the inputs ˜ xk. If model k takes no inputs except yk−1, entry k of the list
should be set to null.
For a chain consisting of r models, the loc vec input is a vector of length r − 1
containing the locations of the variable yk−1 in the emulator for yk. For example, “1”
corresponds to a two-model chain in which y1 is the ﬁrst variable in the emulator for
y2.
The scale params input should be used when the output yk is on a diﬀerent scale
to the one used in the emulator for yk+1. Default corresponds to a location shift of 0
and a scale shift of 1.
Value
A matrix of outputs from the linked emulator, where each row corresponds to a
distinct prediction point.
6.2.2 Prediction from a linked emulator using the theoretical method
Function Name
MM pred theory
Description
Prediction from a linked emulator via the theoretical method.
97

---

## Page 118

Arguments
• predpts: List of matrices of the prediction points for the controllable inputs to
each model.
• designs: List of design matrices for the individual emulators.
• b vecs: List of vectors of correlation parameters for the individual emulators.
• res vecs: List of vectors of results from the simulator runs for each computer
experiment.
• inv corrmats: List of inverted correlation matrices for the individual emulators.
• beta0s: List of regression coeﬃcients for the individual emulators.
• sig2s: List of process variances for the individual emulators.
• nuggets: List of nuggets for the individual emulators.
• scale params: Optional list of location and scale shift parameters for the second
and later emulators in the chain.
Notes
The correlation functions of all of the individual GP emulators are required to be
Gaussian. The regression components of the emulators must be constant terms instead
of linear. Each yk−1 must be the ﬁrst variable in the emulator for yk.
For the predpts input, entry k of the list should be a matrix containing the prediction
locations for the inputs ˜ xk. If model k takes no inputs except yk−1, entry k of the list
should be set to null.
The scale params input should be used when the output yk is on a diﬀerent scale
to the one used in the emulator for yk+1. Default corresponds to a location shift of 0
and a scale shift of 1.
Value
List of two elements: the mean of the output under the linked emulator at each
prediction point, and the corresponding variance at each prediction point.
6.2.3 Sensitivity analysis for the ﬁnal model in a chain
Function Name
SensFinal
98

---

## Page 119

Description
Sensitivity analysis on the ﬁnal model in a chain using the theoretical method for
prediction.
Arguments
• designs: List of design matrices for the individual emulators.
• b vecs: List of vectors of correlation parameters for the individual emulators.
• res vecs: List of vectors of results from the simulator runs for each computer
experiment.
• inv corrmats: List of inverted correlation matrices for the individual emulators.
• beta0s: List of regression coeﬃcients for the individual emulators.
• sig2s: List of process variances for the individual emulators.
• nuggets: List of nuggets for the individual emulators.
• samples1: List of matrices containing samples from the distribution for the con-
trollable inputs to each model.
• samples2: List of matrices containing samples from the distribution for the con-
trollable inputs to each model.
• seq length: Number of points in each variable to evaluate the main eﬀects and
(if speciﬁed) bounds and interactions at. Default is 200.
• bounds: Optional numeric vector containing the variable(s) for which posterior
variance bounds of ±2 standard deviations on the expected output across the
range of the variable(s) should be plotted.
• ints: Optional matrix containing the pairs of variables for which the two-way
interaction between them should be plotted.
• lim low: Optional vector of lower limits for the variables of the ﬁnal model. If
not supplied, defaults to 0 for all variables.
• lim up: Optional vector of upper limits for the variables of the ﬁnal model. If
not supplied, defaults to 1 for all variables.
• varnames: Optional vector of variable names.
99

---

## Page 120

Notes
This function works by using MM pred theory to obtain a sample for the input to
the ﬁnal model which arises as the output of the previous model in the chain, then
applying standard techniques for sensitivity analysis on a single emulator using Monte
Carlo integration. It assumes independence between the variables in the ﬁnal model,
so that their joint distribution is a combination of their one-dimensional distributions.
A Gaussian correlation function and constant regression component for the individual
GP emulators in the chain is required.
By default, the function plots the posterior mean of the expected output across the
range of each variable in the ﬁnal model, and calculates Sobol’ indices for each main
eﬀect and two-way interaction. The user may specify additional plots using the bounds
and ints arguments. The bounds input is a vector containing the location of the
relevant variable(s) in the emulator for the ﬁnal model. If s interactions are required,
the dimension of the matrix input ints should be s × 2, where each row contains the
locations of the relevant pair of variables in the emulator for the ﬁnal model. When
multiple plots are requested, they are separated by a user prompt to press the return
key.
The matrices of samples contained within the list argumentssamples1 and samples2
must be independent. If model k takes no inputs except yk−1, entry k of these lists
should be set to null.
The scale params input should be used when the output yk is on a diﬀerent scale
to the one used in the emulator for yk+1. Default corresponds to a location shift of 0
and a scale shift of 1.
The varnames argument controls the names used for each variable in plots of the main
eﬀects and (if speciﬁed) bounds and interactions. The default is x1, x2, ..., xq∗, where
q∗ is the number of variables in the ﬁnal model and consists of qr directly controllable
inputs plus yr−1.
Value
List of two elements: a vector of the Sobol’ indices for the individual variables, and
a matrix of Sobol’ indices for the two-way interactions.
6.2.4 Sensitivity analysis for the output of a chain in terms of the
directly controllable inputs
Function Name
Multimod calcME
100

---

## Page 121

Description
Posterior means of the expected output of a chain of two models as each of the
directly controllable inputs to the chain is ﬁxed to multiple values across its range.
Arguments
• samples: Matrix containing a sample from the joint distribution of all controllable
inputs to the chain.
• xn 1: Design matrix for the ﬁrst emulator.
• xn 2: Design matrix for the second emulator.
• y1: Vector of results from the simulator runs for the ﬁrst computer experiment.
• y2: Vector of results from the simulator runs for the second computer experiment.
• beta0 1: Regression coeﬃcient for the ﬁrst emulator.
• beta0 2: Regression coeﬃcient for the second emulator.
• inv corrmat1: Inverted correlation matrix for the ﬁrst emulator.
• inv corrmat2: Inverted correlation matrix for the second emulator.
• b1: Vectors of correlation parameters for the ﬁrst emulator.
• b2: Vectors of correlation parameters for the second emulator.
• sig2 1: Process variance for the ﬁrst emulator.
• sig2 2: Process variance for the second emulator.
• nugget 1: Nugget of the ﬁrst emulator.
• nugget 2: Nugget of the second emulator.
• seq length: Number of points in each variable to evaluate the main eﬀects and
(if speciﬁed) bounds and interactions at. Default is 200.
• lim low: Optional vector of lower limits for the variables of the ﬁnal model. If
not supplied, defaults to 0 for all variables.
• lim up: Optional vector of upper limits for the variables of the ﬁnal model. If
not supplied, defaults to 1 for all variables.
• varnames: Optional vector of variable names.
• scale params: Optional vector of location and scale shift parameters for the
second emulator in the chain.
101

---

## Page 122

Notes
Independence between the controllable inputs of the chain is assumed, so that their
joint distribution is a combination of their one-dimensional distributions. A Gaussian
correlation function and constant regression component for the individual GP emulators
in the chain is required.
In addition to its value, this function plots the posterior mean of the expected output
across the range of each variable.
The scale params input should be used when the output y1 is on a diﬀerent scale
to the one used in the emulator for y2. Default corresponds to a location shift of 0 and
a scale shift of 1.
The varnames argument controls the names used for each variable in plots of the
main eﬀects and (if speciﬁed) bounds and interactions. The default is x1, x2, ..., xq,
where q = q1 + q2 is the total number of directly controllable inputs to the chain.
In the longer term, it is hoped to extend this function to support chains of more
than two models, and to bring its inputs into line with the previous three functions
described.
Value
Matrix of expected outputs across the range of each variable to the chain. Each row
corresponds to a variable; each column corresponds to the location of the ﬁxed value
for each variable within the sequence.
6.3 Examples
We present in this section an example of how the functions described in Section 6.2
can be used for prediction and sensitivity analysis for a chain of models. The chain
we shall demonstrate our R code on is the three-model example presented in equation
(5.16), with a single important input and two dummy inputs which have no eﬀect on
the output y3. Note that where it is necessary to break a single line of code across
multiple lines of text, we shall use a tab at the beginning of the second and later lines
to indicate that these should be read as part of the preceding line of code.
We begin by inputting the three models into R.
t e s t f u n c 1 <− f u n c t i o n ( x1 ){
return ( x1 + s i n (3 ∗ pi ∗ ( x1 ) ) )
}
102

---

## Page 123

t e s t f u n c 2 <− f u n c t i o n ( x1 , x2 ){
return ( x1 − log (1 + x1 ) )
}
t e s t f u n c 3 <− f u n c t i o n ( x1 , x2 ){
return ( x1 + exp( −2∗x1 ) )
}
We now need to run computer experiments for each of these models, and extract the
relevant values for use in the linked emulator. Before doing this, however, we deﬁne a
function to set up the matrix of correlations between the design points of a computer
experiment, as this will be useful later.
corr mat setup <− f u n c t i o n ( c o r rf u n c , design , b , nugget ) {
design <− as . matrix ( design )
npts <− nrow ( design )
corr mat <− matrix ( nrow=npts , ncol=npts )
f o r ( i in 1 : npts ) {
f o r ( j in 1 : npts ) {
corr mat [ i , j ] <− c o r r f u n c (b , design [ i , ] − design [ j , ] )
}
}
corr mat <− corr mat + diag ( nugget , npts )
return ( corr mat )
}
To allow the theoretical linked emulator to be used, a Gaussian correlation function
and a constant regression term are used. The experimental designs are chosen as
described in Section 5.6. A nugget δ = 10−7 is used in each emulator. The mlegp
package is used to ﬁt the emulators. For the ﬁrst model, the code required to run the
computer experiment, set up the matrix of regression functions and nugget, build the
GP emulator, extract the correlation parameters and populate the matrix of correlations
is as follows:
l i b r a r y ( mlegp )
npts 1 <− 10
xn 1 <− seq (0 , 1 , len=npts 1 )
y1 <− vector ( length=npts 1 )
f o r ( i in 1 : npts 1 ){
y1 [ i ] <− t e s t f u n c 1 ( xn1 [ i ] )
103

---

## Page 124

}
F mat1 <− matrix ( rep (1 , npts 1 ) )
nugget 1 <− 1e −7
GP 1 <− mlegp ( xn 1 , y1 )
b1 <− GP 1$beta
corr mat1 <− corr mat setup ( corrfunc Gauss Cpp , xn 1 , b1 ,
nugget 1 )
The function corrfunc Gauss Cpp is a C++ function to calculate the correlation be-
tween two points under a Gaussian correlation model, which is not repeated here for
reasons of space. With some slight alterations to account for the second and third
model being (nominally) functions of two inputs, and an adaptation in the experimen-
tal design procedure as described in Algorithm 2, the code for the remaining two models
is broadly similar.
y1 design <− seq ( min ( y1 ) , max( y1 ) , length=npts 1 )
x21 design <− r u n i f ( npts 1 , min ( y1 ) , max( y1 ) )
xn 2 <− cbind ( y1 design , x21 design )
y2 <− vector ( length=npts 1 )
f o r ( i in 1 : npts 1 ){
y2 [ i ] <− t e s t f u n c 2 ( xn2 [ i , 1 ] , xn 2 [ i , 2 ] )
}
F mat2 <− matrix ( rep (1 , npts 1 ) )
nugget 2 <− 1e −7
GP 2 <− mlegp ( xn 2 , y2 )
b2 <− GP 2$beta
corr mat2 <− corr mat setup ( corrfunc Gauss Cpp , xn 2 , b2 ,
nugget 2 )
y2 design <− seq ( min ( y2 ) , max( y2 ) , length=npts 1 )
x31 design <− r u n i f ( npts 1 , min ( y2 ) , max( y2 ) )
xn 3 <− cbind ( y2 design , x31 design )
y3 <− vector ( length=npts 1 )
f o r ( i in 1 : npts 1 ){
y3 [ i ] <− t e s t f u n c 3 ( xn3 [ i ] , xn 3 )
}
F mat3 <− matrix ( rep (1 , npts 1 ) )
nugget 3 <− 1e −7
GP 3 <− mlegp ( xn 3 , y3 )
104

---

## Page 125

b3 <− GP 3$beta
corr mat3 <− corr mat setup ( corrfunc Gauss Cpp , xn 3 , b3 ,
nugget 3 )
Since this chain is a function of x1,1 only for a known set of functions, it can be
visualised by plotting the linked emulator predictions and the true value of y3 across
the range of x1,1, as in Figures 3.5 and 3.6. We therefore set up two functions to do
this, one for the simulation-based linked emulator and one for the theoretical linked
emulator, which diﬀer based on how the upper and lower bounds of the credible interval
for y3 are calculated.
plotemutest simu <− f u n c t i o n ( GPsample , x seq , true y , xn , vn ) {
mean <− apply ( GP sample , 1 , mean)
boundlow <− apply ( GP sample , 1 , quantile , 0 . 0 2 5 )
boundup <− apply ( GP sample , 1 , quantile , 0 . 9 7 5 )
p l o t ( xseq , true y , type=” l ” , ylim=c ( min ( boundlow , t r u e y ) ,
max( boundup , t r u e y ) ) , xlab=vn [ 1 ] , ylab=vn [ 2 ] )
l i n e s ( xseq , mean , c o l=”blue ”)
l i n e s ( xseq , boundlow , c o l=”green ”)
l i n e s ( xseq , boundup , c o l=”green ”)
}
plotemutest theory <− f u n c t i o n ( means , vars , x seq ,
true y , xn , vn ) {
sds <− s q r t ( vars )
boundlow <− means − 2 ∗ sds
boundup <− means + 2 ∗ sds
p l o t ( xseq , true y , type=” l ” , ylim=c ( min ( boundlow , t r u e y ) ,
max( boundup , t r u e y ) ) , xlab=vn [ 1 ] , ylab=vn [ 2 ] )
l i n e s ( xseq , means , c o l=”blue ”)
l i n e s ( xseq , boundlow , c o l=”green ”)
l i n e s ( xseq , boundup , c o l=”green ”)
}
We now need to set up the set of prediction points for the linked emulator. A set
of 201 points are chosen in a sequence between 0 and 1 for the ﬁrst input x1,1, with
random values drawn for x2,1 and x3,1. Since the true form of the chain is known, we
can also calculate the actual value of y3 at each of the prediction points.
105

---

## Page 126

n p t s t e s t <− 201
x1 pred <− seq (0 , 1 , length=n p t s t e s t )
x2 pred <− r u n i f ( n p t st e s t , min ( y1 ) , max( y1 ) )
x3 pred <− r u n i f ( n p t st e s t , min ( y2 ) , max( y2 ) )
true y1 <− apply ( as . matrix ( x1 pred ) , 1 , t e s t f u n c 1 )
true y2 <− apply ( as . matrix ( true y1 ) , 1 , t e s t f u n c 2 )
true y3 <− apply ( as . matrix ( true y2 ) , 1 , t e s t f u n c 3 )
Inputs for the function MM pred simu are then set up as described in Section 6.2,
with a sample size of 1000 repetitions at each prediction point.
predpts <− l i s t ( x1 pred , x2 pred , x3 pred )
d e s i g n s<− l i s t ( xn 1 , xn 2 , xn 3 )
b vecs <− l i s t ( b1 , b2 , b3 )
r e s v e c s <− l i s t ( y1 , y2 , y3 )
F mats <− l i s t ( F mat1 , F mat2 , F mat3 )
corr mats <− l i s t ( corr mat1 , corr mat2 , corr mat3 )
GP sampsize <− 1000
l o c v e c <− c (1 , 1)
We are now in a position to use the MM pred simu function to obtain a sample of
1000 values for y3 from the simulation-based linked emulator at each prediction point.
The plot generated is the same as in Figure 3.5, but with the red dots for the design
points removed, as the experimental design procedure introduced in Algorithm 2 does
not allow for the design points in x1,1 to be associated with a speciﬁc value of y3.
y3 samples simu <− MM pred simu ( GP sampsize , predpts , l o c v e c ,
designs , b vecs , r e s v e c s , F mats , corr mats ,
cov type =‘Gaussian ’ )
The output of the simulation-based linked emulator can be visualised and compared
to the true value of y3 at the prediction points using the function we set up earlier for
this purpose. We use the expression function to generate the correct variable names
in the plot labels.
plotemutest simu ( y3 samples simu , x1 pred , true y3 , xn 1 ,
c ( e x p r e s s i o n ( ‘ x ’ [ ’ 1 , 1 ’ ] ) , e x p r e s s i o n ( ‘ y ’ [ 3 ] ) ) )
106

---

## Page 127

The additional inputs required for the MM pred theory function are set up as follows.
beta0 1 <− mean( y1 )
beta0 2 <− mean( y2 )
beta0 3 <− mean( y3 )
beta0s <− l i s t ( beta0 1 , beta0 2 , beta0 3 )
s i g 2 1 <− var ( y1 )
s i g 2 2 <− var ( y2 )
s i g 2 3 <− var ( y3 )
s i g 2 s <− l i s t ( s i g 21 , s i g 2 2 , s i g 2 3 )
inv corrmat1 <− chol2inv ( chol ( corr mat1 ) )
inv corrmat2 <− chol2inv ( chol ( corr mat2 ) )
inv corrmat3 <− chol2inv ( chol ( corr mat3 ) )
inv corrmats <− l i s t ( inv corrmat1 , inv corrmat2 , inv corrmat3 )
nuggets <− l i s t ( nugget 1 , nugget 2 , nugget 3 )
MM pred theory can now be used to generate the mean and variance of y3 under the
theoretical linked emulator at each prediction point. These are again visualised and
compared to the true values using the relevant function deﬁned earlier in this section.
MM pred theory returns a list containing the means and variances of y3, so these must
be passed to the plotting function separately. The plot is that seen in Figure 3.6 with
the red dots for the design points removed as described above.
y 3 r e s u l tt h e o r y<− MM pred theory ( predpts , designs , b vecs ,
r e s v e c s , inv corrmats , beta0s , s i g 2 s , nuggets )
y3 means <− y3 result theory$means
y3 vars <− y 3 r e s u l tt h e o r y $ v a r s
plotemutest theory ( linked means , l i n k e d v a r s , x1 pred , true y3 ,
xn 1 , c ( e x p r e s s i o n ( ‘ x ’ [ ’ 1 , 1 ’ ] ) , e x p r e s s i o n ( ‘ y ’ [ 3 ] ) ) )
We now move on to sensitivity analysis. As in Section 5.6, we assume a uniform
distribution on each of the controllable inputs to the chain. A sample size of 10000 will
be used. We require two sets of samples, which are generated using the in-built runif
function.
SA sampsize <− 10000
sample x11 1 <− r u n i f ( SAsampsize )
107

---

## Page 128

sample x11 2 <− r u n i f ( SAsampsize )
sample x21 1 <− r u n i f ( SAsampsize , min ( y1 ) , max( y1 ) )
sample x21 2 <− r u n i f ( SAsampsize , min ( y1 ) , max( y1 ) )
sample x31 1 <− r u n i f ( SAsampsize , min ( y2 ) , max( y2 ) )
sample x31 2 <− r u n i f ( SAsampsize , min ( y2 ) , max( y2 ) )
Given these samples, we can conduct a complete sensitivity analysis on the third
model in the chain given the inputs y2 and x3,1 using the SensFinal function. The
samples must be formatted into two lists for use in the function. SensFinal generates
a main eﬀects plot of each input, and returns the Sobol’ indices for the main eﬀects
and second-order interaction term. In this example, we do not specify any plots of
bounds on the main eﬀects, nor a contour plot of the interactions, but these can easily
be added if desired. The plot generated can be seen in Figure 5.15.
samples1 <− l i s t ( sample x11 1 , sample x21 1 , sample x31 1 )
samples2 <− l i s t ( sample x11 2 , sample x21 2 , sample x31 2 )
SensFinal ( designs , b vecs , r e s v e c s , inv corrmats , beta0s ,
s i g 2 s , nuggets , samples1 , samples2 ,
varnames=c ( e x p r e s s i o n ( ‘ y ’ [ ‘ 2 ’ ] ) , e x p r e s s i o n ( ‘ x ’ [ ‘ 3 , 1 ’ ] ) ) )
We are also able to generate a plot of the main eﬀect of each directly controllable
input to a two-model chain using the Multimod calcME function. We therefore use this
to generate such a plot for y2 against x1,1 and x2,1. Only one sample for the controllable
inputs is required, which must be structured as a matrix instead of a list.
sample 2mod <− cbind ( sample x11 1 , sample x21 1 )
Multimod calcME ( sample 2mod , xn 1 , xn 2 , y1 , y2 , beta0 1 ,
beta0 2 , inv corrmat1 , inv corrmat2 , b1 , b2 , s i g 2 1 ,
s i g 2 2 , nugget 1 , nugget 2 ,
varnames=c ( e x p r e s s i o n ( ‘ x ’ [ ‘ 1 , 1 ’ ] ) , e x p r e s s i o n ( ‘ x ’ [ ‘ 2 , 1 ’ ] ) ) )
This code generates the plot seen in Figure 5.16, and returns the numerical values
which make up the plot in case these are required for further use. At present, our code
does not allow us to generate a main eﬀects plot for each controllable input to a chain of
three models or more, hence why the ﬁnal output y3 is not considered in this example.
108

---

## Page 129

Chapter 7
Application: casualty prediction
from a CBR release
To demonstrate the methods introduced above, we consider a chain for CBR mod-
elling. The chain is designed to predict the probability of casualty from a CBR release,
and consists of two models. It can be viewed as a simpliﬁed version of the chain intro-
duced in Figure 1.1. The second model in the chain is a dose-response model for the
probability of casualty. This takes two inputs, one of which is dosage. This input is not
of direct interest in research terms, since it is itself inﬂuenced by many other factors.
The ﬁrst model in the chain deals with atmospheric dispersion. The model provides
its output on a grid of points in the form of either the concentration of the contaminant
at speciﬁed time intervals, or the average concentration per hour across the simulation
period. The latter value multiplied by the number of seconds in the simulation period
gives the dosage of the pollutant received by a person at each point on the grid over
the simulation period. This model can therefore be used to generate the dosage input
for the casualty model, leading to a chain of two models. The models themselves are
described in detail in Sections 7.1 and 7.2 respectively.
7.1 Dispersion model
The ﬁrst model in the chain deals with the dispersion of a contaminant such as a
chemical or biological agent. The Hybrid Single Particle Lagrangian Integrated Trajec-
tory Model (HYSPLIT) model was developed by the Air Resources Laboratory of the
National Oceanic and Atmospheric Administration in the United States of America,
and is available for download publicly. Details of the model are available in Stein et al.
(2015). The model is relatively computationally intensive, and has a high overhead in
terms of setting up new runs, so is one which beneﬁts signiﬁcantly from emulation.
The inputs to the HYSPLIT model consist of meteorological data on a geographical
grid, and the physical and emission properties of the contaminant. The model has an
extremely large number of inputs, many of which are either not suitable (due to being
109

---

## Page 130

categorical instead of continuous) or not of interest for our purposes. It was therefore
decided to focus only on varying three of the inputs, while keeping the others ﬁxed.
The three inputs chosen were release rate, release duration and release time. Ranges
and units for these inputs are given in Table 7.1.
Input Units Lower bound Upper bound
Release rate units of contaminant / hour 0 2
Release duration hours 0 12
Release time minutes 0 360
Table 7.1: Ranges and units for the three inputs to the HYSPLIT model which are
allowed to vary in our example
A single contaminant from a single release location was assumed. The simulation
time was ﬁxed at 12 hours. The release location is ﬁxed at latitude 40 degrees north,
longitude 90 degrees west, with an elevation of 10 metres. This is the default release
location in the HYSPLIT program, and corresponds to a location in central Illinois,
United States. The default meteorology ﬁle and default values for other inputs such as
the half-life and diﬀusivity of the pollutant were also used.
0.0 0.5 1.0 1.5 2.0
0e+00 2e−11 4e−11 6e−11
HYSPLIT output
Release rate (units/hour)
Dosage
Figure 7.1: HYSPLIT output at the 20 design points against release rate
While the output is given on a grid, we are less interested in considering the eﬀect
across space and more concerned with the eﬀect of the three inputs of interest. For this
reason, a single point is chosen for analysis: the point with latitude 39.95 degrees north,
longitude 90 degrees west. This is very close to the release location, diﬀering only in
being slightly further south. Since the wind direction speciﬁed in the meteorology ﬁle
includes a strong northerly component, this location thus receives a relatively large dose
of the pollutant over the course of the simulation compared to most on the measurement
110

---

## Page 131

0 2 4 6 8 10 12
0e+00 2e−11 4e−11 6e−11
HYSPLIT output
Release duration (hours)
Dosage
Figure 7.2: HYSPLIT output at the 20 design points against release duration
grid, although it is still possible for this dosage to be very small if the inputs of interest
are chosen such that the absolute amount of pollutant released is low.
0 50 100 150 200 250 300 350
0e+00 2e−11 4e−11 6e−11
HYSPLIT output
Release time (minutes)
Dosage
Figure 7.3: HYSPLIT output at the 20 design points against release time
All of the work which follows requires an emulator on the HYSPLIT model. A
maximin Latin hypercube design with 20 points on the three inputs of interest (release
rate, hours of emission and release time) is used to generate the data to which the
emulator for the dosage output at the chosen spatial location is ﬁtted. This is not a
large design for a three-dimensional design space, so there is a relatively high level of
uncertainty in prediction from the resulting emulator. The emulator is ﬁtted using theR
package ‘DiceKriging’, with a Gaussian correlation function; the nugget is estimated
from the data during the ﬁtting process. The input variables are on widely diﬀering
111

---

## Page 132

ranges, so are rescaled to the [0 , 1] interval before the emulator is ﬁtted.
0.0 0.5 1.0 1.5 2.0
0e+00 2e−11 4e−11 6e−11
Mean emulator prediction
Release rate (units/hour)
Dosage
Figure 7.4: Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release rate
0 2 4 6 8 10 12
0e+00 2e−11 4e−11 6e−11
Mean emulator prediction
Release duration (hours)
Dosage
Figure 7.5: Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release duration
To understand how the model behaves, it is useful to look at both the results of the
simulator runs and the predictions made by the emulator for diﬀerent input conﬁg-
urations. We can plot the true HYSPLIT output against the three inputs at the 20
points for which it is known. Figures 7.1, 7.2 and 7.3 suggest that there is a strongly
increasing relationship between the release rate and dosage. A weaker relationship can
be seen between release time and dosage, while there is no obvious pattern to the eﬀect
of release duration. These patterns are largely replicated, as we would expect, in the
112

---

## Page 133

0 50 100 150 200 250 300 350
0e+00 2e−11 4e−11 6e−11
Mean emulator prediction
Release time (minutes)
Dosage
Figure 7.6: Mean emulator prediction for the HYSPLIT output at the 200 prediction
points against release time
mean predictions of the emulator we ﬁt to the data, displayed in Figures 7.4, 7.5 and
7.6. The observed trends in the model are not what may have been expected: typically,
increasing the duration of release would cause the dosage to increase, while releasing
the pollutant later may be associated with lower dosages. The unusual patterns seen
here may be a result of the decision to focus on the dosage at a single geographical
location close to the source of the release. It should also be noted that it is not easy
to draw ﬁrm conclusions from these plots, as each individual scatter plot ignores the
eﬀect of changes in the other two variables.
One interesting feature of the predictions is that for seven of the 200 points, the mean
emulator output is less than 0. This is of course not realistic, since a negative dosage
of a pollutant cannot exist, and the HYSPLIT model does not return such values.
Further analysis of these predictions shows that the variances associated with them
are relatively large. It is also observed that all seven negative mean predictions occur
when both the release rate and release time are low, a combination which is particularly
diﬃcult for the emulator to deal with since it leads to very low dosages. With only
20 design points for the computer experiment, it can be diﬃcult for the emulator to
make good predictions at extreme regions of the design space, especially when these
regions are associated with extreme predictions. One way to deal with this would be
to transform the output onto an unbounded scale before ﬁtting an emulator. In this
work, however, we shall continue to use the emulator described here for simplicity.
7.2 Casualty model
The second model concerns the probability of casualty arising from a given dose of a
chemical or biological agent. It takes as inputs the dosage received by a person, together
113

---

## Page 134

with two additional inputs D50 and slope which are properties of the contaminant. The
output is the probability that the aﬀected individual dies due to the agent.
The model equation for this particular dose response model is
P = 0.5
{
1 + erf
[ s√
2 log10
x
d
]}
(7.1)
where erf is the error function, P is the probability of casualty, x is the dosage, d is the
D50 and s is the slope. This model was suggested by Dstl to be indicative of what may
be seen, and is termed a probit model for dose response. The use of probit models for
casualty response to dosage has a long history, ﬁrst appearing in Bliss (1934). Other
dose response models are also available - Berkson (1944), for example, prefers the use
of a logistic model, while Prentice (1976) introduces a four-parameter generalisation of
both models.
In our work, the D50 and dosage are considered of interest to vary, while the slope
is arbitrarily set to s = 3; this corresponds to a relatively gradual increase in the
probability of casualty, with values of exactly 0 and 1 only at very extreme values of
the other parameters. This was done to better demonstrate out methods and is not
based on any real pollutants.
The model can be viewed as a simple reparameterisation of the standard probit
regression equation, in which the constant term has been adjusted such that the role
of the D50 input - a known or estimated property of the agent, corresponding to the
dosage at which the probability of casualty is 0.5 - is made explicit. Equation (7.1)
could be rewritten as
P = 0.5
{
1 + erf
[ s√
2(log10 x − log10 d)
]}
= 0.5{1 + erf[β0 + β1 log10 x]}
where β1 = s/
√
2 and β0 = s log10d√
2 . This is the standard form of a probit regression
model.
7.3 Prediction from the chain
For this particular chain, there are several approaches that could be taken for predic-
tion. The dose-response model is not computationally expensive to run, so Gaussian
process emulation is not strictly required in order to make inferences about its be-
haviour. For the purposes of demonstrating our methodology, however, it will nonethe-
less be useful to emulate it anyway. In addition, while simulation-based methods lend
themselves naturally to a chain of models in which only some will require emulation,
the theoretical results derived in chapter 3 are speciﬁc to the case where all models in
114

---

## Page 135

the chain are emulated. However, simulation using the true model provides a useful
benchmark to compare our results again.
The following subsections will therefore consider four cases: a simulation in which
only the ﬁrst model is emulated; a composite emulator, where the output of the second
model is modelled directly as a function of the controllable inputs to the chain only
a linked emulator constructed by Monte Carlo integration in which both models are
emulated; and a linked emulator constructed such that its theoretical mean and variance
are known. To test prediction across the space of the four controllable inputs, a maximin
Latin hypercube with 200 points on four dimensions is used. This prediction set will
form the basis for comparisons between the diﬀerent methods considered in this chapter.
7.3.1 Direct simulation on the dose-response model
Prediction in the ﬁrst case is achieved by generating a set of 1000 predictions from
the emulator for the HYSPLIT model for the values of release rate, release time and
release duration at each prediction point, then feeding each of these outputs into the
true simulator for dose response together with the value of D50 at the relevant prediction
point. Since this method has no uncertainty arising from the second model, we would
expect this to approximate the system better than one which has uncertainty in both
stages of the chain, so this will be used as the benchmark to which the other methods
are to be compared.
The plots of mean probability of casualty against the four inputs of interest (Figure
7.7) reveal a mixed picture. The most important input would appear to be D50,
with low values strongly associated with high probabilities and high values with low
ones. There is also a clear relationship between low release rates and low probability
of casualty, although the eﬀect across the rest of the range of this input is less clear.
Release time shows a weaker relationship with casualty probability, while there is no
obvious evidence of a pattern in the plot of probability against release duration. These
results are consistent with what would be expected based on the preceding two sections.
Dosage (not included in these plots as it is not a directly controllable input to the chain)
and D50 should account for similar proportions of the variation in the probability of
casualty. A low value of D50 means that only a small dosage is required to reach a
probability of casualty of 0.5, while a high value means that a larger dosage is needed,
so the pattern seen is this plot is to be expected.
The relationship between dosage and casualty probability is positive (since a high
dosage is more likely to have a signiﬁcant eﬀect than a low one). In Section 7.1, we
saw that increasing the release rate and release time is associated with an increase in
dosage, so we would expect a positive relationship between these inputs and probability
of casualty - but since dosage is a function of three inputs, the relationship should be
less strong than between D50 and probability of casualty. The absence of a clear link
115

---

## Page 136

0.0 0.5 1.0 1.5 2.0
0.0 0.2 0.4 0.6 0.8 1.0
Relase rate (units/hour)
E*(Probability of casualty)
0 2 4 6 8 10 12
0.0 0.2 0.4 0.6 0.8 1.0
Release duration (hours)
E*(Probability of casualty)
0 50 100 150 200 250 300 350
0.0 0.2 0.4 0.6 0.8 1.0
Release time (minutes)
E*(Probability of casualty)
0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.0 0.2 0.4 0.6 0.8 1.0
D50
E*(Probability of casualty)
Figure 7.7: Mean prediction of probability of casualty against release rate (top left),
release duration (top right), release time (bottom left) and D50 (bottom right) at the
200 prediction points - direct simulation on the dose-response model
between release duration and casualty probability is also consistent with what was seen
in Section 7.1. Additionally, it is interesting to note that there are more predictions
close to 0 than to 1.
It is also of interest to brieﬂy investigate the variance of the predictions from the
chain. Since all of the variation arises from the ﬁrst model, it may be expected that the
variance in our predictions would be related to the inputs to the ﬁrst model in some
way. However, the opposite is the case: as seen in Figure 7.8, the variance is generally
very low across the predictions, with large values occurring almost entirely when D50
is low. The plots for the other inputs reveal no comparable trend in the location of
the high-variance points. This may be because low values of D50 lead to potentially
very high probabilities of casualty, which means that changes in the dosage obtained
from the ﬁrst emulator could have a large knock-on eﬀect in the probability of casualty
obtained from the second model.
7.3.2 Composite emulator
To build an emulator for the entire chain, a 20 point Latin hypercube design is again
used, but this is now in four dimensions instead of three since D50 must be accounted
for at this stage. The ﬁrst model is run at the 20 conﬁgurations of its three inputs,
and the obtained dosage is used as an input to the second model together with the D50
116

---

## Page 137

0.0 0.5 1.0 1.5 2.0
0.00 0.02 0.04 0.06
Relase rate (units/hour)
Var*(Probability of casualty)
0 2 4 6 8 10 12
0.00 0.02 0.04 0.06
Relase duration (hours)
Var*(Probability of casualty)
0 50 100 150 200 250 300 350
0.00 0.02 0.04 0.06
Relase time (minutes)
Var*(Probability of casualty)
0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.00 0.02 0.04 0.06
D50
Var*(Probability of casualty)
Figure 7.8: Prediction variance of probability of casualty against release rate (top left),
release duration (top right), release time (bottom left) and D50 (bottom right) at the
200 prediction points - direct simulation on the dose-response model.
value speciﬁed by the design. An emulator is then built to approximate the probability
of casualty directly from the four inputs. A Gaussian correlation function is used,
with all parameters including the regression coeﬃcients, process variance and nugget
estimated from the data.
Predicting the output at the 200 prediction points gives a very diﬀerent set of plots
to those seen before. The composite emulator shows little link between release duration
and probability of casualty, as the method based on direct simulation did, but disagrees
with it on the eﬀect of the other variables. While some evidence of the previously-
observed patterns in release rate and release time are still present, much of their eﬀect
is lost, particularly at the lower end of release rate. The trend of decreasing probabilities
with increasing D50 remains, but is bucked by an increased probability of casualty as
the extreme upper end of its distribution; across most of the rest of the input range,
predictions are too concentrated, with the emulator largely unable to predict outside of
a relatively narrow range at similar values of D50 almost regardless of the other inputs.
More of the mean predictions are close to 1 than in the previous case, and there are
several mean predictions below 0 or above 1 (an artefact of emulating on a bounded
scale instead of an unbounded one). In addition, the prediction variances are generally
much larger than seen previously (although this is to be expected, since the second
model is now a source of uncertainty), with little pattern in the variance relative to the
117

---

## Page 138

0.0 0.5 1.0 1.5 2.0
0.0 0.2 0.4 0.6 0.8 1.0
Relase rate (units/hour)
E*(Probability of casualty)
0 2 4 6 8 10 12
0.0 0.2 0.4 0.6 0.8 1.0
Relase duration (hours)
E*(Probability of casualty)
0 50 100 150 200 250 300 350
0.0 0.2 0.4 0.6 0.8 1.0
Relase time (minutes)
E*(Probability of casualty)
0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.0 0.2 0.4 0.6 0.8 1.0
D50
E*(Probability of casualty)
Figure 7.9: Mean prediction of probability of casualty against release rate (top left),
release duration (top right), release time (bottom left) and D50 (bottom right) at the
200 prediction points - composite emulator
inputs.
Many of these problems are explained by the experimental design used to build the
emulator. A 20-point design over a four-dimensional space is not especially large, and
leaves sizable regions of the design space uncovered. This could be overcome by using
a larger design, but this would require an increased number of runs of the complex
HYSPLIT model. In addition, while the 20 design points are evenly spread on the
four controllable inputs, they are not evenly spread on the dosage input to the casualty
model. The increase in the predicted probability of casualty at the highest values
of D50 is a result of these issues: the two design points with the largest values of
D50 happen to occur at distinct conﬁgurations of the other three inputs which lead
to higher-than-average dosages, which confuses the emulator into assuming that the
higher probabilities observed are a result of the D50 input instead of the release rate
and release time which actually explain the observations. Emulating the two models
separately oﬀers more ﬂexibility in this respect, since the number of design points for
the computer experiment on each model need not be the same.
7.3.3 Theoretical linked emulator
To construct the linked emulator, we require separate emulators for the two models in
the chain. The HYSPLIT model is handled as before, using the 20 design points intro-
118

---

## Page 139

0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.00 0.04 0.08 0.12
D50
Var*(Probability of casualty)
Figure 7.10: Prediction variance of probability of casualty against D50 - composite
emulator
duced in Section 7.1. For the signiﬁcantly cheaper casualty model, we take advantage
of the split nature of the emulators to use a larger experimental design with 50 points.
This is chosen using a two-dimensional maximin Latin hypercube, with the range on
which dosage is taken to vary determined by the results of the 20 HYSPLIT model
runs. This approach is preferable to using the results of the HYSPLIT model runs
as design points for the reasons discussed in Chapter 4; the more complex sequential
design ideas are not considered here, but could potentially be of use for future study
on the same topic. A Gaussian correlation function is chosen for both emulators.
We ﬁrst consider a linked emulator where the theoretical mean and variance can be
determined. Plug-in estimates of the regression coeﬃcients and process variances for
each emulator are obtained using the ‘DiceKriging’ package.
Plotting the probability of casualty against the four inputs (Figure 7.11) reveals a
similar picture to that seen in Figure 7.7. The same inputs are deemed to be important,
and their eﬀects on the output is largely similar in nature. This suggests that the linked
emulator has captured the features of the chain of models relatively well. There are
however several predictions outside of the [0 , 1] range on which probability of casualty
lies, which is a source of some concern, but these are fewer in number and generally
lower in magnitude than under the composite emulator. These could in theory be dealt
with using a transformation which takes the probability of casualty to the whole real
line, but when this was attempted in practice, the result was an emulator which failed
to accurately capture the behaviour of the casualty model.
119

---

## Page 140

0.0 0.5 1.0 1.5 2.0
0.0 0.2 0.4 0.6 0.8 1.0
Relase rate (units/hour)
E*(Probability of casualty)
0 2 4 6 8 10 12
0.0 0.2 0.4 0.6 0.8 1.0
Release duration (hours)
E*(Probability of casualty)
0 50 100 150 200 250 300 350
0.0 0.2 0.4 0.6 0.8 1.0
Release time (minutes)
E*(Probability of casualty)
0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.0 0.2 0.4 0.6 0.8 1.0
D50
E*(Probability of casualty)
Figure 7.11: Mean prediction of probability of casualty against release rate (top left),
release duration (top right), release time (bottom left) and D50 (bottom right) at the
200 prediction points - linked emulator, theoretical method
7.3.4 Simulation-based linked emulator
The simulation approach allows for more ﬂexibility. We use this to integrate out the
regression coeﬃcients and process variances instead of using plug-in estimates, which
allows us to better account for the uncertainty arising from their unknown status. The
simulation itself proceeds as described in Section 3.2, with 1000 repetitions at each
design point.
Again reviewing the plots of probability of casualty against the four inputs (Figure
7.12), we observe that the patterns are very similar to those seen in Figure 7.11 when
the theoretical method was used. Integrating out the additional parameters of the two
GP emulators does not appear to have changed the mean response signiﬁcantly. This
is as expected: the two methods use the same data and similar structures for the two
emulators in the chain, so it would be highly concerning if they disagreed markedly.
However, the additional uncertainty captured in the simulation method may lead to
larger changes in the variance. This is investigated in Figure 7.13, where the variances
of the two methods are plotted together against D50. First, it is important to note that
the pattern in the variances is much more like that of the direct simulation method than
the composite emulator, which further suggests that the linked emulator is capturing
the behaviour of the chain well. Both linked emulator approaches give larger variances
than direct simulation on the casualty model, which is again to be expected as the
120

---

## Page 141

0.0 0.5 1.0 1.5 2.0
0.0 0.2 0.4 0.6 0.8 1.0
Relase rate (units/hour)
E*(Probability of casualty)
0 2 4 6 8 10 12
0.0 0.2 0.4 0.6 0.8 1.0
Release duration (hours)
E*(Probability of casualty)
0 50 100 150 200 250 300 350
0.0 0.2 0.4 0.6 0.8 1.0
Release time (minutes)
E*(Probability of casualty)
0e+00 1e−11 2e−11 3e−11 4e−11 5e−11 6e−11
0.0 0.2 0.4 0.6 0.8 1.0
D50
Probability of casualty
Figure 7.12: Mean prediction of probability of casualty against release rate (top left),
release duration (top right), release time (bottom left) and D50 (bottom right) at the
200 prediction points - linked emulator, simulation method.
second emulation step introduces additional uncertainty into the predictions.
It is also clear from Figure 7.13 that the variances in the simulation method (plotted
in red) are consistently slightly larger than those of the theoretical method (in black) at
the same prediction points. The diﬀerence in variance is not uniform across the space:
it aﬀects some points more than others, and is generally larger where the variance is
already relatively high; this may be a true reﬂection of an underlying pattern, or an
artefact of Monte Carlo error in the simulation. The observed variances nonetheless
remain low relative to the scale of the predictions themselves. It is clear that although
considering for uncertainty in the GP parameters does increase prediction variance, the
extra variability accounted for is not especially large in this case. It should however
be noted that this method does not take account of uncertainty in the correlation
parameters of the two GP emulators, which would have to be dealt with using a Markov
chain Monte Carlo approach as discussed in Section 2.3.
7.4 Sensitivity analysis
Having concluded that the linked emulator provides a reasonable approximation to
the chain, we now move on to sensitivity analysis. Both sensitivity analysis on the dose-
response model (with respect to its inputs, dosage and D50) and sensitivity analysis
121

---

## Page 142

Figure 7.13: Prediction variance of probability of casualty against D50 - linked emula-
tor, theoretical method (black) and simulation method (red)
for the entire chain will be considered.
Before any analysis can be conducted, we require distributions for the four control-
lable input variables. We have no particular information about the three inputs to the
HYSPLIT model - release rate, release duration and release time - beyond the range
on which each can occur. They are thus best handled using uniform distributions on
their range. The distribution which best represents the behaviour of the D50 input is
more debatable. Unlike the three inputs previously discussed, in which diﬀerent con-
ﬁgurations correspond to diﬀerent types of release which may all be of interest, D50
is a property of the agent being released itself. Assuming the agent is the same in
each, this has a single true value, but it may not be known exactly. A symmetrical
distribution about the most likely value would thus appear sensible; the obvious choice
is a truncated normal distribution with mean at the centre of the range of possible
values for D50. The variance of the normal distribution could be chosen in several
ways depending on how uncertain we are about the true value. The limiting case of the
variance being eﬀectively inﬁnite on the input range corresponds to a uniform distri-
bution for D50. In this work, we consider a uniform distribution; a normal distribution
with ﬁnite variance would also be a reasonable choice, with the variance chosen based
on discussions with a subject-matter expert.
First, we consider sensitivity analysis for the dose-response model given its inputs.
The dosage input arises as the output of the HYSPLIT model, so the distribution
of this input must be derived empirically by prediction from the GP emulator for the
HYSPLIT model across a large set of input conﬁgurations from the chosen distributions
on release rate, duration and time. The resulting Sobol’ indices are 0.4576 for dosage,
0.4809 for D50 and 0.0615 for the interaction between them. This suggests that both
inputs are of similar importance given the speciﬁed distributions on the controllable
122

---

## Page 143

inputs. The corresponding main eﬀects plot (Figure 7.14) shows that the eﬀect of
increasing dosage is to increase the probability of casualty on average, while the eﬀect
of increasing D50 is to reduce it on average; this is consistent with what might be
expected based on the form of the dose-response model given in (7.1).
0.0 0.2 0.4 0.6 0.8 1.0
0.0 0.2 0.4 0.6 0.8
xi
E(Y|xi)
Dosage
D50
Figure 7.14: Posterior expectation of probability of casualty given the two inputs to
the dose-response model.
To analyse the chain as a whole requires substantially more input conﬁgurations to
be tested than the previous small-scale prediction studies, so execution speed is of the
essence, which means the slower simulation-based methods are of less use here. The
theoretical results from the linked emulator are therefore used as the basis for our
analysis.
Figure 7.15. shows a (scaled) main eﬀects plot for each controllable input to the
chain. The inputs are scaled to the [0 , 1] interval so that they can be directly compared
on the same plot; only the posterior expectation is considered. Each input is ﬁxed at
50 equally-spaced values across its range, with 1000 random values drawn from the
distribution of the unﬁxed variables, and the expectation of the linked emulator means
across these 1000 runs taken to obtain an estimate of the posterior expectation of the
probability of casualty given the ﬁxed input.
Having removed the confounding eﬀects of the other variables, it is now possible to
see the patterns in the behaviour of the probability of casualty more clearly. There is
a strongly negative relationship between D50 and probability of casualty, with the rate
of decrease slowing as the input becomes larger. Increasing release rate is associated
with increased probability of casualty, but the relationship is highly non-linear, with a
slower rate of increase at the two extremes of its range. Release time has a small but
123

---

## Page 144

0.0 0.2 0.4 0.6 0.8 1.0
0.2 0.4 0.6 0.8
xi
E(Y|xi)
Release rate
Release duration
Release time
d50
Figure 7.15: Posterior expectation of probability of casualty given each input to the
linked emulator.
noticeable eﬀect, which is initially positive but later negative in nature as the variable
is increased across its range. Release duration has little eﬀect: ﬁxing it to any value
provides no substantial information on the output of the chain of models. Despite the
previously-observed individual predictions outside of the range [0 , 1], there is no value
of any input which gives a posterior expectation of the expected value of probability of
casualty outside of this range.
Ideally, we would of course like to consider sensitivity analysis for the full chain
further, by constructing variance bounds for the main eﬀects and calculating Sobol’
indices for the main eﬀects and two-way interactions. As discussed in Chapter 5, this is
not currently possible. For this speciﬁc example, further analysis of the chain could be
conducted by simulation by making use of the emulator for the HYSPLIT model and
using direct simulation on the dose-response model. This is not directly relevant to the
framework we have constructed in this thesis, however, so was not considered here.
7.5 Conclusions
This chapter uses the methods developed throughout this thesis to make predictions
from a chain of models for a real-life scenario. Being a CBR chain, it is directly rel-
evant to the research goals set out in Chapter 1. Taking advantage of the simplicity
of the second model allowed our predictions to be compared directly to the output of
a simulation where only one model is emulated, which should better reﬂect the true
nature of the chain. The results conﬁrmed both the consistency of the two linked emu-
lator approaches, and that both outperform the composite emulator for this particular
chain, thus validating the linked emulator approach. The results also serve as a com-
124

---

## Page 145

parison between the two linked emulator strategies, demonstrating both the speed and
exact nature of the theoretical method and the ﬂexibility and more robust uncertainty
estimates arising from the Monte Carlo method.
Sensitivity analysis demonstrates that the D50 input of signiﬁcant importance - ef-
fectively equal to that of the dosage, and greater than that of any individual input to
the HYSPLIT model. One conclusion from these results, since the inputs to the dis-
persion model have a range of interest on which they can vary while D50 has a single
true (but unknown) value, is that learning more about D50 would have a signiﬁcant
eﬀect in reducing the uncertainty in predictions from the chain of models.
We should note that this chain of models is far from ideal for the purposes of making
new inferences using our methodology. The chain is only two models long, and could
thus have already been analysed using the pre-existing methods set out in Section 3.3;
a longer chain would oﬀer more potential for new results that could not already have
been obtained. More importantly, the second model is too simple to require emulation
at all. The chain is also incomplete when compared to the diagram in Figure 1.1, with
many more modelling aspects which could be considered. This is discussed further in
Chapter 9.
125

---

## Page 146

126

---

## Page 147

Chapter 8
Simulation study
8.1 Introduction
In Chapter 7, we presented an analysis of the linked emulator method when applied
to a real-world problem. Our results demonstrate that both of the linked emulator ap-
proaches considered in this thesis can make better predictions than the simpler method
of a composite emulator. However, it is diﬃcult to draw conclusions from the analysis
of a single chain of models, especially a chain in which the second function is very
smooth and does not present a signiﬁcant challenge to emulate.
A further aspect of linked emulator methodology which we have not yet explored in
detail is the diﬀerence between the theoretical and simulation approaches. In both the
dispersion-dose response chain in Chapter 7 and the one-dimensional synthetic chains
in Chapters 3 and 4, the theoretical and simulation methods produced largely similar
results. If this were true in general, there would be no need for the simulation method
to be used, as it is signiﬁcantly slower than the theoretical approach. But in all of these
examples, the simulators being emulated were suﬃciently smooth that a Gaussian corre-
lation function could be used to build the emulators. The Gaussian correlation function
produces inﬁnitely diﬀerentiable sample paths, so there are some functions which can-
not be emulated well using this correlation function. Stein (1999), pp.30-31 and 69-70,
advises against using the Gaussian correlation function when modelling any physical
process, citing both theoretical concerns and evidence in real examples of predictions
which would be highly implausible in the context of the process being modelled. While
computer experimentation does not involve modelling physical processes directly, a sim-
ulator that approximates a physical process should have similar behaviour to it. It is
therefore of interest to investigate the behaviour of the two classes of linked emulators
when a diﬀerent correlation function may be more appropriate.
The comparatively poor performance of a composite emulator relative to its linked
emulator counterparts in previous examples is also worthy of further consideration.
A similar result was previously observed for a chain of simple synthetic functions by
Kyzyurova et al. (2018), and it is especially noteworthy in the real example in Chapter
127

---

## Page 148

7. It is however unclear if the failure of the composite emulator is speciﬁc to the types of
chain considered so far, or a more widespread phenomenon. This is especially relevant
to chains containing models which a Gaussian correlation function is not appropriate,
as the simulation method for linked emulation is very slow in comparison to simply
ﬁtting a single emulator.
8.2 Simulation setup
These questions can be investigated by constructing a chain from models which
require a less smooth correlation function but which also consist of known, easily com-
putable functions. A set of simple functions with these properties are those with dis-
continuous derivatives, notably the absolute value function. We will therefore consider
a chain of two models deﬁned by the following relationships:
y1 = [1 − (|x1| ∗ |x2|3/2)a]3 ;
y2 = cos[(1 − 2 ∗ |0.8 − y1|b)3] ,
where −1 ≤ x1 ≤ 1 and −1 ≤ x2 ≤ 1. The values a and b are tunable parameters..
For the purposes of this study, we will consider ﬁve values each for these parameters:
a = {2, 2.5, 3, 3.5, 4} and b = {1, 1.2, 1.4, 1.6, 1.8}. These two sets combine to give 25
chains of models to investigate.
For each of these 25 chains, we build two linked emulators - one each using the
theoretical and simulation methods - and a composite emulator. The composite emu-
lators use a constant regression term, and a Mat´ ern correlation function as deﬁned in
equation (2.3). The smoothness parameter of the Mat´ ern correlation function is set to
ω = 3/2, with the remaining correlation parameters and the nugget estimated from the
data. This choice of correlation function and smoothness parameter implies a Gaussian
process prior which is diﬀerentiable only once, so is likely to be appropriate for a chain
made up of less smooth simulators.
An experimental design is required for the directly controllable inputs x1 and x2 for
the composite emulator. The same design can be used for all values of a and b; we
choose 15 design points using a maximin Latin hypercube design, which thus requires
the two simulators to be run 15 times each for a total computational cost of 30 simulator
runs. The design points are given in Table 8.1.
In the interests of fairness, the two linked emulators for each chain share an ex-
perimental design and thus diﬀer only in how they are ﬁtted to the training data.
However, since the ﬁrst model in the chain is a function of two inputs x1 and x2, while
the second is a function of just one input y1, the linked emulator would beneﬁt from
allocating more simulator runs to the ﬁrst model than the second. We thus allocate 20
128

---

## Page 149

x1 x2
-0.9333 0.2667
-0.8 -0.2667
-0.6667 0.6667
-0.5333 -0.6667
-0.4 0
-0.2667 0.5333
-0.1333 -0.9333
0 -0.4
0.1333 0.1333
0.2667 0.8
0.4 -0.8
0.5333 -0.1333
0.6667 0.4
0.8 0.9333
0.9333 -0.5333
Table 8.1: Experimental design for the complete chain of models for the composite
emulator
design points to the ﬁrst model and 10 to the second. Since both simulators have very
similar computational cost, the total computational cost of the 30 simulator runs per
linked emulator is virtually identical to that of the 30 simulator runs required for each
composite emulator.
The design points for x1 and x2 are independent of a and b and can therefore be the
same for all 25 chains. A 20-point maximin Latin hypercube design is used, with the
design points presented in Table 8.2. The 10 design points for y1 in the second model
are chosen by following the procedure in Algorithm 2, and thus depend on the output
of the simulator runs for the ﬁrst model. The second simulator is univariate so the
design points are equally spaced on the ﬁve diﬀerent implied ranges of y1, which are
dependent on the value of a so cannot be made identical for every chain.
The linked emulator for the theoretical method is composed of two individual emu-
lators, one for each simulator, with constant regression terms and Gaussian correlation
functions as deﬁned in equation (2.2). The regression coeﬃcients, process variances,
correlation parameters and nuggets are estimated from the data. The linked emulator
for the simulation method is composed of two emulators with constant regression terms
and Mat´ ern correlation functions whereω = 3/2, as for the composite emulators. The
correlation parameters and nuggets are estimated from the data, using the likelihood
marginal to the regression coeﬃcients and process variances.
For an additional comparison to a non-emulation method, we shall also consider a
linear regression model for y2 against x1 and x2:
y2 = β0 + β1x1 + β2x2 + ϵ ,
129

---

## Page 150

x1 x2
-0.95 0.05
-0.85 0.65
-0.75 -0.45
-0.65 -0.95
-0.55 0.25
-0.45 0.75
-0.35 -0.25
-0.25 -0.75
-0.15 0.15
-0.05 0.55
0.05 0.95
0.15 -0.55
0.25 -0.05
0.35 0.45
0.45 -0.85
0.55 -0.35
0.65 0.85
0.75 0.35
0.85 -0.65
0.95 -0.15
Table 8.2: Experimental design for the ﬁrst model in the chain for the linked emulator
where ϵ is an error term and the coeﬃcients β0, β1, β2 are estimated using maximum
likelihood estimation.
To test the predictive capabilities of the four methods, we require a set of prediction
points. We choose 1000 points across the space of x1, x2 from a maximin Latin hyper-
cube. The ﬁrst simulator was run at each of these points, and the resulting value of y1
fed into the second simulator to obtain the true output of the chain. These true values
are used as a comparison set for the predictions made by the composite emulator, the
two linked emulators and the linear regression model at the same 1000 points. We
consider two measures of predictive ability for the three methods. The ﬁrst is the root
mean squared error (RMSE) of the mean prediction from the regression and emulation
methods versus the true value across the 1000 prediction points. Let η∗ be the estimate
of the true chain of models η, and let x1,i be the ith prediction point. The RMSE of
η∗ is deﬁned as
RM SE(η∗) =
√ 1
n
1000∑
i=1
[η∗(x1,i) − η(x1,i)]2 .
This is chosen instead of, say, the mean absolute error as it has the property of
penalising large errors at individual prediction points more heavily, which is important
as we do not wish the worst predictions made to be very large. The second measure
is based on coverage. The composite emulator, both linked emulators and the linear
regression model can generate nominal 95% prediction intervals for the output of the
130

---

## Page 151

chain at any input set. A useful measure of the accuracy of the uncertainty estimates
of the four methods is to compare this to the true percentage of the prediction set
for which the calculated interval includes the true output. In particular, if for any
method this is consistently below 95 or occasionally dramatically lower, the method is
understating the uncertainty in its predictions.
8.3 Results
The resulting RMSE and coverage for each of the three methods across the 25 chains
of models are presented in Table 8.3. For presentational reasons, we deﬁne the following
abbreviations: Simu, the simulation-based linked emulator; Theory, the theoretical
linked emulator; Comp, the composite emulator; Linear, the linear regression model.
a b RMSE Coverage (%)
Simu Theory Comp Linear Simu Theory Comp Linear
2 1 0.0804 0.0688 0.0980 0.1073 95.7 72.3 91.7 95.2
2 1.2 0.0833 0.0670 0.1126 0.1193 96.3 65.7 90.3 96.8
2 1.4 0.0805 0.0628 0.1186 0.1229 96.5 57.0 91.0 98.7
2 1.6 0.0781 0.0611 0.1199 0.1238 97.8 45.3 99.1 98.1
2 1.8 0.0779 0.0609 0.1207 0.1249 98.4 43.4 99.4 92.6
2.5 1 0.0896 0.0870 0.0936 0.1179 99.0 90.7 84.7 99.1
2.5 1.2 0.0955 0.0917 0.1057 0.1304 97.8 86.1 84.4 99.5
2.5 1.4 0.0946 0.0933 0.1089 0.1314 95.5 81.5 85.8 100
2.5 1.6 0.0937 0.0941 0.1186 0.1275 93.6 79.2 75.0 97.3
2.5 1.8 0.0941 0.0946 0.1246 0.1230 93.0 76.4 71.7 92.6
3 1 0.0893 0.0910 0.0879 0.0944 95.6 87.8 59.8 95.9
3 1.2 0.0993 0.1027 0.0987 0.1076 92.6 85.2 58.1 97.4
3 1.4 0.1012 0.1067 0.1028 0.1114 92.5 82.0 57.4 98.9
3 1.6 0.1000 0.1063 0.1025 0.1101 92.0 78.9 56.3 96.9
3 1.8 0.0990 0.1042 0.0998 0.1072 92.3 78.1 56.7 93.4
3.5 1 0.0875 0.0894 0.0836 0.0789 96.8 91.9 65.5 97.6
3.5 1.2 0.0968 0.1010 0.0984 0.0886 95.1 87.1 62.0 98.1
3.5 1.4 0.0979 0.1040 0.1026 0.0921 93.5 82.8 61.6 98.7
3.5 1.6 0.0959 0.1022 0.1005 0.0920 93.2 80.7 62.5 96.5
3.5 1.8 0.0939 0.0989 0.0960 0.0904 93.0 79.5 63.9 94.6
4 1 0.0794 0.0824 0.1103 0.0706 95.9 91.0 74.5 95.6
4 1.2 0.0878 0.0915 0.1190 0.0789 94.8 87.6 73.0 95.4
4 1.4 0.0893 0.0942 0.1164 0.0809 93.6 83.7 70.3 95.6
4 1.6 0.0879 0.0932 0.1082 0.0797 93.0 82.2 68.8 92.1
4 1.8 0.0857 0.0905 0.0987 0.0777 93.0 80.6 67.0 91.3
Table 8.3: RMSE and coverage for the simulation (S) and theoretical (T) linked emu-
lators, for the composite emulator (C), and for the linear regression model (L).
There are several points of interest in these results. Firstly, the performance of the
composite emulator is comparatively poor in most cases: across the 25 values of a and b
given here, the RMSE for the composite emulator is the lowest of the three emulation-
based methods in only two cases, compared to 15 cases where it is the highest. Only
131

---

## Page 152

when a = 3 or a = 3.5 is the composite emulator competitive. There is also a connection
to value of b: the composite emulator predicts better when b is small, except when a is
large. The coverage of the nominal 95% prediction intervals for the composite emulator
are also of concern, falling below 95% in all but two cases, and consistently very low
whenever a is not equal to 1. When a = 3, which produces the relatively best RMSEs
for the composite emulator, all ﬁve actual coverages are unacceptably low at below
60%.
The linear model varies strongly with the value of a in its predictive accuracy. For
a ≤ 3, its RMSE is consistently the largest of the four methods, suggesting a model
which approximates the true chain poorly. When the value of a is 3.5 or 4, however,
the situation is reversed: the linear model now outperforms all three emulation-based
approaches. Despite this improved performance for a subset of the chains, it is clear
that a linear model is insuﬃcient to make good predictions in general. The coverage
achieved by the linear model is strong for every chain, consistently exceeding 90% and
exceeding 95% in 19 of the 25 cases. If anything, this suggests the prediction intervals
provided are in fact too wide, although it is noteworthy that the coverage falls below
95% whenever b = 1.8.
The relative performances of the two linked emulators in terms of RMSE is varied,
with 17 cases in which the simulation method produces the lower RMSE and 8 in
which the theoretical method is the more accurate. Again, these are closely linked to
the value of a. When a = 2, the theoretical method consistently produces the lower
RMSE; for a = 2.5, there is little to separate the two linked emulators; while for a ≥ 3,
the RMSE of the simulation method is consistently lower. The main diﬀerence between
the two methods is the choice of correlation function, so this suggests that low values
of a produce a smoother simulator which is better suited to the Gaussian correlation
function, while larger values of a lead to simulators which require a rougher correlation
function like the Mat´ ern. The composite emulator performs poorly when a is large
despite also using a Mat´ ern correlation function, which again indicates that the linked
emulator approach is preferable.
However, the two types of linked emulator are vastly diﬀerent in terms of the cover-
ages of their nominal 95% prediction intervals. The coverages seen when the simulation
method is used are largely consistent with what would be expected from a genuine 95%
prediction interval: 12 are greater than and 13 less than 95%, with no value lower
than 90%. The coverage is typically somewhat lower when both a and b are large, but
the eﬀect on the coverage of varying these parameters is not as pronounced as for the
composite emulator.
The same cannot be said of the linked emulator constructed using the theoretical
method. Instead, all 25 actual coverages are below 95%, suggesting a consistent prob-
lem of underestimating the uncertainty in the predictions made. The coverage is con-
132

---

## Page 153

sistently poorer when b is large or when a = 2, and falls below 50% when a = 2, b = 1.6
and when a = 2 , b = 1 .8. This is particularly surprising as, for these two parameter
conﬁgurations, the theoretical linked emulator produced not only the lowest RMSEs of
the four approaches, but the lowest RMSEs of any method across any of the 25 chains.
While the theoretical linked emulator makes comparatively very accurate mean predic-
tions in these cases, there is a substantially greater variance associated with prediction
than the method would suggest.
As discussed in Chapter 3, the probability distribution of the prediction from a the-
oretical linked emulator given the inputs to the chain is approximated by a normal
distribution with the variance calculated using equation 3.8. The consistently low cov-
erages would thus suggest that this equation in fact produces an underestimate of the
true variance. This is not entirely surprising: the theoretical linked emulator uses
plug-in estimation for the regression coeﬃcients, process variance and correlation pa-
rameters, ignoring a potential source of predictive uncertainty. The simulation-based
linked emulator also uses plug-in estimation for the correlation parameters, so its im-
pressive performance in terms of actual coverage implies that - at least when Mat´ ern
correlation function is used - the uncertainty in the correlation parameters contributes
little to the predictive uncertainty for this chain of emulators.
This simulation study of 25 chains of simulators demonstrates several noteworthy
points about the diﬀerent methods considered in this thesis. We observe that the com-
posite emulator generally performs poorly compared to both classes of linked emulator.
There are some chains for which a theoretical linked emulator provides good approxi-
mations, and others for which it is not a viable choice. The simulation method oﬀers
greater robustness, delivering reasonable predictions and trustworthy 95% prediction
intervals across all of the chains. The theoretical method shows signs of consistently
underestimating the variance in its predictions and thus providing unreasonably nar-
row prediction intervals. The much simpler linear regression model can perform well for
some chains with more linear relationships between the input and output, but performs
poorly in the majority of cases.
The simulation method however has a clear disadvantage in speed. Benchmarking
the computational time required to make predictions at the 1000 prediction points for
each of the three methods, we found that the composite emulator was the fastest. This
is to be expected, as ﬁtting and making predictions from a single emulator is a swift
process, and while the theoretical linked emulator is substantially slower, it is clear from
the consistently poor performance of the composite emulator that the speed advantage
alone does not make this method worth pursuing. However, the simulation-based linked
emulator is around 50 times slower than the theoretical linked emulator. The additional
computational resources required mean that the performance advantages oﬀered by
the simulation method would need to be extremely large to be worth pursuing, and for
133

---

## Page 154

chains with a large number of models or inputs, the method may not be computationally
feasible at all.
For this reason, when utilising a linked emulator for a real problem, we would choose
the theoretical method whenever it could be expected to give reasonable results. But
identifying which chains of models can be approximated appropriately by a theoretical
linked emulator is a diﬃcult problem. It is not usually possible to know in advance
whether the models in the chain are smooth enough for a Gaussian correlation function
to perform well. One possibility is to ﬁt GP emulators with both Gaussian and Mat´ ern
correlation functions to each model in the chain from the same simulator runs, and use
the diagnostics for GP emulator performance discussed by Bastos and O’Hagan (2009)
to assess if these emulators are appropriate before linking them together. It may also
be possible to narrow the performance gap between the two linked emulator methods
by improving the speed of the simulation method, for example by writing more eﬃcient
code, although its dependence on Monte Carlo approximation means it will always be
the slower of the two approaches.
Perhaps the most important conclusion from this study is that the 95% prediction
interval of a theoretical linked emulator should not be considered entirely trustworthy.
In all 25 chains considered here, the actual coverage was well below 95, with the lowest
coverages coming when the mean predictions were on average closest to the true output
of the chain. This could be improved by integrating out the regression coeﬃcients of
the individual emulators instead of using plug-in estimation, although it would not
be possible to integrate out the process variance as the resulting distribution on the
output of the earlier models in the chain would no longer be normal. Finally, while
the much less complex linear regression model is unable to match the performance
of the linked emulator methods in general, its comparatively strong performance for
certain chains highlights the potential beneﬁts of using emulators with linear instead
of constant regression terms for each model in the chain.
134

---

## Page 155

Chapter 9
Conclusions and future work
9.1 Conclusions
In this thesis, we considered approaches towards the analysis of chains of complex
computational models using Gaussian process emulation. We have presented a variety
of methods by which such chains can be handled. We reaﬃrm existing results that sug-
gest that a linked emulator (in which the models in the chain are emulated separately,
and the uncertainty passed between them) is preferable to a composite emulator (in
which a single emulator is built for the chain of models as a whole), and present two
methods for analysis from such chains - a ﬂexible approach involving simulation and
Monte Carlo integration, and a faster theoretical approximation for a speciﬁc class of
emulators. Both methods were generalised from a simple two-model chain to a longer
chain, the latter using an approximation to a probability distribution which is not avail-
able in closed form. A simulation study was conducted to investigate the diﬀerences
between the two approaches to linked emulation, demonstrating that the simulation
method is more robust if the models in the chain are less smooth than ideal for an
emulator with a Gaussian correlation function. The advantages of a linked emulator
approach over the much simpler technique of linear regression was also demonstrated,
with the caveat that the occasionally very good performance of linear regression pro-
vides a strong argument for the use of emulators which include a linear component.
We have also highlighted the related problems of experimental design for chains of
models. We focus on experimental design for models at the second and later steps
in the chain, illustrating why this is both an important and a diﬃcult problem, and
present a simple algorithm for single-stage design which nonetheless oﬀers signiﬁcant
beneﬁts over more naive approaches. Some thought was also given to sequential design
for chains of models, both in terms of why this may be beneﬁcial and to potentially
productive strategies to accomplish it.
Sensitivity analysis for a chain of models was another area of focus. We developed
an algorithm for sensitivity analysis for the ﬁnal model in the chain in terms of its own
inputs. We also worked towards sensitivity analysis for the ﬁnal output of the chain in
135

---

## Page 156

terms of the directly controllable inputs to any model in the chain, with a theoretical
result presented for the posterior expectation of the main eﬀects and interactions of an
input or set of input.
Our work was tested on models supplied by Dstl, which form a simpliﬁed chain
demonstrating some of the principles of casualty modelling from a CBR release. Al-
though this example is imperfect - a two-model chain with a relatively simple second
model - it nonetheless highlights the potential applications of our research. In addition,
we were able to demonstrate fast predictions from the chain of models for diﬀerent in-
put conﬁgurations, and to draw new conclusions about the relative importance of the
inputs to the model output.
There are many avenues of relevant future research that could be considered. These
are discussed in detail below.
9.2 Future work: experimental design
One of the most promising ﬁelds for further research would appear to be experimental
design for chains of computational models. This is a broad and complex topic with
signiﬁcant potential for further research. Our method for single-stage design for chains
of emulators, presented in Section 4.2, eﬀectively reduces the problem to one which has
already been solved. As discussed in the same section, however, this is not perhaps the
most rewarding approach to the design problem for chains of models.
Even here, however, there are open questions. Our method uses the results of the
simulator runs for model 1 to construct a design space for y1 in the second emulator.
This is potentially problematic if the simulator output does not include values in the
extremes of the true range for y1. The extremes would then be poorly covered by the
resulting design for the second emulator, meaning prediction from the chain at the
values of the model 1 inputs ˜ x1 which lead to extreme values of y1 may be unreliable.
This could be overcome by simply adding some ﬁxed amount to the range of y1 when
constructing its design space, but this risks placing design points at values of y1 which
may not in fact be in its true range.
Perhaps more signiﬁcantly, sequential design for chains of models has the potential
for signiﬁcant improvement over the simple method presented in Section 4.3. This could
include algorithms for sequential design which make better use of the available resources
than can be achieved by simply applying standard methods for sequential design for
a stand-alone emulator. By accounting for potential diﬀerences in computational cost
and output variation between the individual models in the chain, it may be possible
to learn signiﬁcantly more about the behaviour of the chain without a substantial
increase in computational cost. Learning more about the behaviour of the models
allows better emulators to be built, so this could be extremely beneﬁcial in terms of
136

---

## Page 157

making predictions from the chain as a whole. Section 4.4 sets out some initial ideas as
to how this could be achieved, but further research and implementation of these ideas
is required.
9.3 Future work: sensitivity analysis
Sensitivity analysis is another area in which our work could be expanded substan-
tially. While methods for the analysis of the ﬁnal model are available, further work
is required on analysis of the chain as a whole. As discussed in Section 5.6, the most
plausible route to full sensitivity analysis for a chain under the assumptions required
in Sections 3.4 and 3.6 is via a derivation for the covariance between two independent
predictions from the linked emulator. A natural way to achieve this is by a similar
process to the derivation of the posterior predictive variance of a single linked emulator
output in Section 3.3. We present the beginnings of this below, but have been unable
to complete the derivation.
Let Y2 and Y′
2 be two independent realisations of the linked emulator at distinct input
points, and let ˜ x′
1, ˜ x′
2, y′
1 and c′
n+1,2 be the associated model 1 inputs, model 2 inputs,
model 1 output and vector of correlations with the model 2 design points respectively.
For ease of notation, let
Cov∗(Y2, Y′
2) = Cov[Y2, Y′
2|˜ x2, ˜ x1, ˜ x′
2, ˜ x′
1, Yn,2, Yn,1]
be the covariance between the two realisations given all of the inputs except y1 and y′
1.
Also, let
c∗(Y2, Y′
2) = Cov[Y2, Y′
2|˜ x2, ˜ x1, ˜ x′
2, ˜ x′
1, Yn,2, Yn,1, y1, y′
1]
be the covariance between the two realisations given all of the inputs including y1
and y′
1 (which are unknown beyond their probability distributions). The law of total
covariance allows us to express Cov∗(Y2, Y′
2) in terms of c∗(Y2, Y′
2), µ2 and µ′
2 as
Cov∗(Y2, Y′
2) = Cov(µ2, µ′
2) + E[c∗(Y2, Y′
2)] (9.1)
The second term of (9.1) is given by
E[c∗(Y2, Y′
2)] = E[σ2
z,2{R[(˜ x2, y1)T , (˜ x′
2, y′
1)T ] − cT
n+1,2C2c′
n+1,2}]
which reduces to
E[c∗(Y2, Y′
2)] =σ2
z,2
q2∏
d=1
exp[−bd(x2,d − x′
2,d)2]E
{
exp[−by1(y1 − y′
1)2]
}
− σ2
z,2E[cT
n+1,2C2c′
n+1,2] .
(9.2)
137

---

## Page 158

Let
u = cT
n+1,2C2c′
n+1,2 .
For the expectation in the second term of (9.2), we thus have
E[u] = E
[ k∑
i=1
k∑
j=1
exp{−by1(x(q2+1)
2,i − y1)2}P1C(i,j)
2 exp{−by1(x
′(q2+1)
2,j − y′
1)2}P2
]
,
where
P1 =
q2∏
d=1
exp{−bd(x(d)
2,i − x(d)
2,n+1)2}
and
P2 =
q2∏
d=1
exp{−bd(x
′(d)
2,j − x
′(d)
2,n+1)2} .
Following a similar approach to that in Chapter 3 leads to
E[u] =
k∑
i=1
k∑
j=1
C(i,j)
2
p∏
d=1
exp{−bd[(x(d)
2,i − x(d)
2,n+1)2 + (x
′(d)
2,j − x
′(d)
2,n+1)2]}I∗
i,j
where
I∗
i,j =
∫ ∫ 1
2πσ1σ′
1
exp
{
− (y1 − µ1)2
2σ2
1
− (y′
1 − µ′
1)2
2σ
′2
1
}
exp{−by1[(x(q2+1)
2,i − y1)2 + (x
′(q2+1)
2,j − y′
1)2]}dy1dy′
1 .
(9.3)
For ease of notation, let
W1 = exp
{
−
µ2
1 + 2σ2
1by1[x(q2+1)
2,i ]2 −
(µ1+2σ2
1by1x(q2+1)
2,i )2
1+2σ2
1by1
2σ2
1
}
,
and analogously,
W′
1 = exp
{
−
µ
′2
1 + 2σ
′2
1 by1[x
′(q2+1)
2,j ]2 −
(µ′
1+2σ
′2
1 by1x
′(q2+1)
2,j )2
1+2σ′2
1 by1
2σ
′2
1
}
.
We also deﬁne
V1 =
(1 + 2σ2
1by1)
[
y1 −
µ1+2σ2
1by1x(q2+1)
2,i
1+2σ2
1by1
]2
2σ2
1
,
and
138

---

## Page 159

V′
1 =
(1 + 2σ
′2
1 by1)
[
y′
1 −
µ′
1+2σ
′2
1 by1x
′(q2+1)
2,j
1+2σ′2
1 by1
]2
2σ
′2
1
.
Further algebraic manipulation of (9.3) leads to
I∗
i,j = C1I1
where
C1 = 1√
(1 + 2σ2
1by1)(1 + 2σ
′2
1 by1)
W1W′
1
and
I1 =
∫ ∫ √
1 + 2σ2
1by1
√
1 + 2σ
′2
1 by1
2πσ1σ′
1
exp{−V1 − V′
1}dy1dy′
1
The integrand in I1 is the density of a bivariate normal distribution with zero correla-
tion, where the other parameters are given by
µ(y1) =
µ1 + 2σ2
1by1x(q2+1)
2,i
1 + 2σ2
1by1
;
µ(y′
1) =
µ′
1 + 2σ
′2
1 by1x
′(q2+1)
2,j
1 + 2σ
′2
1 by1
;
σ(y1) = σ1√
1 + 2σ2
1by1
;
σ(y′
1) = σ′
1√
1 + 2σ
′2
1 by1
.
When integrated with respect to y1 and y′
1, this is equal to 1, so I1 = 1, leaving
I∗
i,j = C1 ,
but the complicated form of C1, W1 and W′
1 suggests that further simpliﬁcation is
required before this quantity is used in the full covariance expression.
The ﬁrst term of (9.1) is
Cov(µ2, µ′
2) = E(µ2µ′
2) − E(µ2)E(µ′
2) .
E(µ2) and E(µ′
2) are found from equation (3.7), so we only need to calculate
E(µ2µ′
2) = Ey1{[β2,0 + cT
n+1,2C−1
2 (yn,2 − β2,0)][β2,0 + c
′T
n+1,2C−1
2 (yn,2 − β2,0)]} ,
139

---

## Page 160

which simpliﬁes to
E(µ2µ′
2) =β2
2,0 + β2,0E[cT
n+1,2C−1
2 (yn,2 − β2,0)] + β2,0E[c
′T
n+1,2C−1
2 (yn,2 − β2,0)]
+ E[{cT
n+1,2C−1
2 (yn,2 − β2,0)}{c
′T
n+1,2C−1
2 (yn,2 − β2,0)}]
(9.4)
An expression for E[cT
n+1,2C−1
2 (yn,2 − β2,0)] (and by extension the case where c
′T
n+1,2 is
used instead) was derived in (3.9):
E[cT
n+1,2C−1
2 (yn,2 − β2,0)] =
k∑
i=1
a(i)
q2∏
j=1
exp{−bj(x(j)
2,i − x(j)
2,n+1)2}Ii ,
where Ii is given in (3.11). To deal with the remaining expectation, note that
{cT
n+1,2C−1
2 (yn,2 − β2,0)}{c
′T
n+1,2C−1
2 (yn,2 − β2,0)} = (cT
n+1,2 a)(c
′T
n+1,2 a)
=
k∑
i=1
k∑
j=1
c(i)
2 c
′(j)
2 a(i)a(j) ,
so
E
[
{cT
n+1,2C−1
2 (yn,2 − β2,0)}{c
′T
n+1,2C−1
2 (yn,2 − β2,0)}
]
= E
[ k∑
i=1
k∑
j=1
c(i)
2 c
′(j)
2 a(i)a(j)
]
.
Algebraic manipulation similar to that seen in Chapter 3 gives
E
[ k∑
i=1
k∑
j=1
c(i)
2 c
′(j)
2 a(i)a(j)
]
=
k∑
i=1
k∑
j=1
a(i)a(j)P3I∗
i,j ,
where
P3 =
q2∏
d=1
exp{−bd[(x(d)
2,i − x(d)
2,n+1)2 + (x(d)
2,j − x
′(d)
2,n+1)2]} .
As above, this expression depends on further simpliﬁcation of I∗
i,j but is otherwise
complete.
For ease of notation, let
c∗
y = exp[−by1(y1 − y′
1)2] .
The expectation in the ﬁrst term of (9.2) is then
E(c∗
y) =
∫ ∫
f(y1)f(y′
1) exp[−by1(y1 − y′
1)2]dy1dy′
1 ,
which, when the distributions are substituted in and like terms collected, reduces to
140

---

## Page 161

E(c∗
y) = 1
2πσ1σ′
1
∫ ∫
exp
[
− N1
2σ2
1σ
′2
1
]
dy1dy′
1 ,
where
N1 = σ
′2
1 (1 + 2σ2
1by1)y2
1 − 2σ
′2
1 µ1y1 − 2σ2
1y′
1µ′
1 − σ2
1(1 + 2σ
′2
1 by1)y
′2
1 − 4σ2
1σ
′2
1 by1y1y′
1 .
However we have been unable to make further progress on this integral. This is the
main reason why the covariance derivation is incomplete.
Even if this were completed, it would provide full sensitivity analysis only when
the conditions required for the theoretical approximation to hold are met. Sensitivity
analysis for chains with diﬀerent correlation or regression structures, or where the pro-
cess variances are integrated out of the individual emulators, would require a diﬀerent
method.
One option is to consider a form of decomposition of the Sobol’ indices of a chain
of models. For example, consider a two-model chain with ﬁnal output y2, where the
second model includes the input y1 which is the output of an earlier model. Let
Sy2(x1,1) = var{E(Y2|X1,1 = x1,1)}
var(Y2) . (9.5)
be the Sobol’ index for the input x1,1 with respect to the output y2. We have
Sy2(y1) = var{E(Y2|Y1 = y1)}
var(Y2)
and
Sy1(x1,1) = var{E(Y1|X1,1 = x1,1)}
var(Y1) .
A simple approximation could be provided by
Sy2(x1,1) ≈ Sy2(y1) × Sy1(x1,1) .
The logic for this is as follows: Sy2(y1) corresponds to the proportion of the variance
in y2 that is explained by y1. Similarly, Sy1(x1,1) is the proportion of the variance in
y1 explained by x1,1. It therefore appears natural that the product of the two indices
should correspond to the proportion of the variance in y2 which is explained by x1,1,
since there is no additional source of uncertainty in y1 other than its inputs. However,
no theoretical result exists to demonstrate that this is a good approximation for two
(or more) complex non-linear simulators, although initial simulation studies to test this
empirically for simple chains were encouraging.
141

---

## Page 162

Another possible solution is to bypass the chain of emulators by using a single ap-
proximation. We have already seen that a composite emulator does not perform well
for the chains of computational models covered in this thesis. However, for sensitivity
analysis a composite emulator has two major advantages: it is signiﬁcantly less com-
putationally intensive to make predictions from than a linked emulator, and allows the
pre-existing sensitivity analysis results from Section 5.3 to be used without alteration.
A possible compromise, therefore, is to build a linked emulator as discussed before,
but then approximate this again by a single emulator. While this adds another layer
of uncertainty to the process, it neatly bypasses many of the problems associated with
both the linked and the composite emulators when conducting sensitivity analysis.
Since the linked emulator is generally much less computationally intensive than the
chain of simulators (but still too intensive for sensitivity analysis to be done directly),
a relatively large set of design points could reasonably be used. The linked emulator is
however a stochastic function, so any emulator to it must account for this; the methods
discussed in Section 2.4 would need to be used. The design points used to train the
linked emulator could themselves be used as design points for the single stochastic
emulator, with a known uncertainty in the linked emulator output of 0 at these points.
This somewhat esoteric approach has not been implemented, but may be of interest in
the future.
9.4 Future work: other areas
There are also other ways in which our methodology could be extended. The chains
of models considered in this thesis all obey a relatively restrictive set of assumption, and
a signiﬁcantly wider class of problems could also be approached using similar methods.
One natural extension would be to unify our framework with that of Kyzyurova et al.
(2018), in which multiple inputs to the same computational model may come from
other models. This would allow more complicated structures than just a chain to be
considered. Such a uniﬁcation process should be relatively straightforward, as adding
additional inputs from other models does not change the theoretical results for the
linked emulator substantially, so adapting the theoretical results presented here to the
more general framework may not present a great challenge.
The individual emulators considered here are also somewhat restrictive. Incorporat-
ing Markov chain Monte Carlo inference for the correlation parameters of the Gaussian
process emulators would allow the uncertainty in these parameters to be incorporated
into our predictions. Emulators which account for non-stationarity in the underlying
computational models may also have a role to play in broadening the set of problems
which our methodology can be applied to.
The framework we present for emulation applies to a speciﬁc type of model, with
a single deterministic output and continuous inputs. Models with multiple outputs
142

---

## Page 163

and/or categorical inputs could also be considered as part of the chain. Models with
stochastic instead of deterministic output are another avenue worthy of exploration.
These extensions would require incorporating some of the processes introduced in Sec-
tion 2.4. Given that these processes change the underlying nature of the emulators
involved, it is likely that the theoretical results discussed in this thesis would no longer
hold, so new theoretical derivations would be required if anything beyond a simple
Monte Carlo method were to be used.
Finally, the application to a chain of models for probability of casualty from a chain of
models for a CBR release could also be expanded. Real world dispersion and casualty
models can be far more complex than those considered here. There are many more
inputs that could be taken into account in addition to release rate, release duration
and release time. Examples include the release location and meteorological conditions
such as wind speed and wind direction, the latter of which are in fact inputs to the
single model for a CBR release in Chapter 5. It would also be useful to consider the
probability of casualty across a range of locations, instead of at a single point; this
would need the emulator for the ﬁnal model to be able to handle multiple outputs, as
discussed above. A full study of the CBR problem would include at least one additional
model in the chain, for the meteorological conditions, and potentially another for the
placement of sensors to detect a release.
143

---

## Page 164

144

---

## Page 165

Bibliography
R.J. Adler. The Geometry of Random Fields . John Wiley, 1981.
I. Andrianakis and P. G. Challenor. The eﬀect of the nugget on Gaussian process
emulators of computer models. Computational Statistics and Data Analysis , 56:
4215–4228, 2012.
S. Ba. Package ‘slhd’. R package vignette, 2015.
S. Banerjee. Bayesian linear model: Gory details. http://www.biostat.umn.edu/
~{}ph7440/pubh7440/BayesianLinearModelGoryDetails.pdf, 2010.
L. S. Bastos and A. O’Hagan. Diagnostics for Gaussian process emulators. Technomet-
rics, 51:425–438, 2009.
J. Beck and S. Guillas. Sequential design with mutual information for computer exper-
iments (MICE): Emulation of a tsunami model. Journal of Uncertainty Quantiﬁca-
tion, 4:739–766, 2016.
J. Berkson. Application of the logistic function to bio-assay. Journal of the American
Statistical Association, 39:357–365, 1944.
I. Billonis and N. Zabaras. Multi-output local Gaussian process regression: Applications
to uncertainty quantiﬁcation. Journal of Computational Physics , 231(17):5718–5746,
2012.
M. Binois, J. Huang, R. B. Gramacy, and M. Ludkovski. Replication or exploration?
Sequential design for stochastic simulation experiments. Technometrics, pages 1–43,
2018.
C.I. Bliss. The method of probits. Science, 79(2037):38–39, 1934.
V.E. Bowman and D.C. Woods. Emulation of multivariate simulators using thin plate
splines with application to atmospheric dispersion. SIAM/ASA Journal on Uncer-
tainty Quantiﬁcation, 4:1323–1344, 2016.
F. Campolongo, J. Cariboni, and A. Saltelli. An eﬀective screening design for sensitivity
analysis of large models. Environmental Modelling and Software, 22:1509–1518, 2007.
J.Q. Candela, A. Girard, J. Larsen, and C.E. Rasmussen. Propagation of uncertainty in
Bayesian kernel models - application to multiple-step ahead forecasting. Proceedings
145

---

## Page 166

of the 2003 IEEE Conference on Acoustics, Speech, and Signal Processing , 2:II–701,
2003.
W. F. Caselton and J. V. Zidek. Optimal monitoring network designs. Statistics &
Probability Letters, 2(4):223–227, 1984.
D. A. Cohn, Z. Ghahramani, and M. I. Jordan. Active learning with statistical models.
Journal of Artiﬁcial Intelligence Research , 4:129–145, 1996.
S. Conti and A. O’Hagan. Bayesian emulation of complex multi-output and dynamic
computer models. Journal of Statistical Planning and Inference , 140(3):640–651,
2010.
A. C. Damianou and N. D. Lawrence. Deep Gaussian Processes. In Proceedings of the
16th International Conference on Artiﬁcial Intelligence and Statistics , 2013.
A. C. Damianou and N. D. Lawrence. Uncertainty propagation in Gaussian process
pipelines. In NIPS workshop on modern non-parametrics , 2014.
G.M. Dancik and K.S. Dorman. mlegp: statistical analysis for computer models of
biological systems using R. Bioinformatics, 2008.
S. Duane, A.D. Kennedy, B. Pendleton, and D. Roweth. Hybrid Monte Carlo. Physics
Letters B, 195:216–222, 1987.
D. Eddelbuettel. Seamless R and C++ Integration with Rcpp . Springer, 2013.
D. Eddelbuettel and C. Sanderson. RcppArmadillo: Accelerating R with high-
performance C++ linear algebra. Computational Statistics and Data Analysis , 71,
2014.
J. Fan. Comment on ”Wavelets in statistics: A review” by A. Antoniadis. Journal of
the Italian Statistical Society , 6(2):131–138, 1997.
K. Fang, R. Li, and A. Sudjianto. Design and Modelling for Computer Experiments .
Chapman and Hall, Boca Raton, 2006.
D. Gamerman and H.F. Lopes. Markov Chain Monte Carlo: Stochastic Simulation for
Bayesian Inference (Second Edition). Chapman and Hall, 2006.
A. Girard, C. E. Rasmussen, J.Q. Candela, and R. Murray-Smith. Gaussian process
priors with uncertain inputs - application to multiple-step ahead time series fore-
casting. In Advances in Neural Information Processing Systems , volume 15, pages
529–536, 2002.
P. W. Goldberg, C. K. I. Williams, and C.M. Bishop. Regression with input-dependent
noise: A Gaussian process treatment. In Advances in Neural Information Processing
Systems, volume 10, pages 493–499, 1998.
146

---

## Page 167

R. B. Gramacy and H. K. H. Lee. Bayesian treed Gaussian process models with an
application to computer modeling. Journal of the American Statistical Association ,
103:1119–1130, 2008.
R. B. Gramacy and H. K. H. Lee. Adaptive design and analysis of supercomputer
experiments. Technometrics, 51(2):130–145, 2009.
R. B. Gramacy and H. K. H. Lee. Cases for the nugget in modeling computer experi-
ments. Statistics and Computing , 22(3):713–722, 2012.
R. B. Gramacy and M. A. Taddy. Categorical inputs, sensitivity analysis, optimization
and importance tempering with tgp version 2, an r package for treed Gaussian process
models. Journal of Statistical Software , 33(6), 2010.
M. Gu, X. Wang, and J.O. Berger. Robust Gaussian stochastic process emulation. The
Annals of Statistics , 46(6A):3038–3066, 2018.
W.K. Hastings. Monte Carlo sampling methods using Markov Chains and their appli-
cations. Biometrika, 57(1):97–109, 1970.
R.G. Haylock and A. O’Hagan. On inference for outputs of computationally expensive
algorithms with uncertainty on the inputs. Bayesian Statistics, 5:629–637, 1996.
D. Higdon, J. Gattiker, B. Williams, and M. Rightley. Computer model calibration
using high dimensional output. Journal of the American Statistical Association , 103
(482):570–583, 2008.
R. L. Iman and W. J. Conover. A distribution-free approach to inducing rank correla-
tion among input variates. Communication in Statistics - Simulation and Computa-
tion, 11(3):311–334, 1982.
H. Jeﬀreys. Theory of Probability. Oxford University Press, 1961.
M.E. Johnson, L.M. Moore, and D. Ylvisaker. Minimax and maximin distance designs.
Journal of Statistical Planning and Inference , 26:131–148, 1990.
V. R. Joseph, L. Gu, and W. Myers. Space-ﬁlling designs for robustness experiments.
Technometrics, 61(1):24–37, 2019.
J. Jun and I. Horace. Active learning with SVM. In J. Ram´ on, R. Dopico, J. Dorado,
and A. Pazos, editors, Encyclopedia of Artiﬁcial Intelligence , volume 3, pages 1–7.
ICI Global, 2009.
K. Kersting, C. Plagemann, P. Pfaﬀ, and W. Burgard. Most likely heteroscedastic
Gaussian process regression. In Proceedings of the International Conference on Ma-
chine Learning, pages 393–400, 2007.
A. Konyukhov, P. Vielsack, and K. Schweizerhof. On coupled models of anisotropic
contact surfaces and their experimental validation. Wear, 264(7-8):579–588, 2008.
147

---

## Page 168

A. Krause, A. Singh, and C. Guestrin. Near-optimal sensor placements in Gaussian
processes: Theory, eﬃcient algorithms and empirical studies. Journal of Machine
Learning Research, 9:235–284, 2008.
K.N. Kyzyurova, J.O. Berger, and R.L. Wolpert. Coupling computer models through
linking their statistical emulators.SIAM/ASA Journal on Uncertainty Quantiﬁcation
(JUQ), 6(3):1151–1171, 2018.
L. Le Gratiet, C. Cannamela, and B. Iooss. A Bayesian approach for global sensitiv-
ity analysis of (multi-ﬁdelity) computer codes. SIAM/ASA Journal on Uncertainty
Quantiﬁcation (JUQ), 2:336–363, 2014.
R. Li and A. Sudjianto. Analysis of computer experiments using penalized likelihood
in Gaussian kriging models. Technometrics, 47(2):111–120, 2005.
H. Lin and S. Yim. Coupled surge-heave motions of a moored system. I: Model cal-
ibration and parametric study. Journal of Engineering Mechanics , 132(6):671–680,
2006.
D. V. Lindley. On a measure of the information provided by an experiment. Annals of
Mathematical Statistics, 27(4):986–1005, 1956.
D. MacKay. Information-based objective functions for active data selection. Neural
Computation, 4(4):590–604, 1992.
S. Mak and V. R. Joseph. Minimax and minimax projection designs using clustering.
Journal of Computational and Graphical Statistics , 27(1):166–178, 2018.
B. Matern. Spatial variation. Meddelanden Fran Statens Skogs-Forskningsinstitut, 49
(5), 1960.
M.D. McKay, R.J. Beckman, and W.J. Conover. A comparison of three methods for
selecting values of input variables in the analysis of output from a computer code.
Technometrics, 21:239–245, 1979.
N. Metropolis, A.W. Rosenbluth, M.N. Rosenbluth, A.H. Teller, and E. Teller. Equation
of state calculations by fast computing machines. Journal of Chemical Physics , 21
(6):1087–1092, 1953.
D. M. Morris. Factorial sampling plans for preliminary computational experiments.
Technometrics, 33:161–174, 1991.
R. M. Neal. Bayesian learning for neural networks . Springer, 1996.
R. M. Neal. Handbook of Markov Chain Monte Carlo , chapter MCMC Using Hamilto-
nian Dynamics. Chapman and Hall, 2011.
F. Novometsky and S. Nadarajah. Package ‘truncdist’. R package vignette, 2016.
148

---

## Page 169

E. Nummelin. General Irreducible Markov Chains and Non-Negative Operators . Cam-
bridge University Press, 1984.
D. Nychka, Q. Yang, and J.A. Royle. Constructing spatial designs for monitoring
air pollution using subset regression . Statistics for the Environment 3: Pollution
Assessment and Control. Wiley, 1997.
D. Nychka, R. Furrer, J. Paige, and S. Sain. Package ‘ﬁelds’. R package vignette, 2016.
J.E. Oakley and A. O’Hagan. Probabilistic sensitivity analysis of complex models: a
Bayesian approach. Journal of the Royal Statistical Society , 66:751–769, 2004.
A. O’Hagan. Bayesian analysis of computer code outputs: A tutorial. Reliability
Engineering and System Safety , 91:1290–1300, 2006.
H.D. Patterson and R. Thompson. Recovery of inter-block information when block
sizes are unequal. Biometrika, 58(3):545–554, 1971.
A. Plumb. Metamodelling for hazard prediction. Master’s thesis, University of
Southampton, 2008.
R.L. Prentice. A generalization of the probit and logit methods for dose response curves.
Biometrics, 32(4):761–768, 1976.
W.H. Press and G.R. Farrar. Recursive stratiﬁed sampling for multidimensional Monte
Carlo integration. Computers in Physics , 4(190), 1990.
G. Pujol, B. Iooss, and A. Janon. Package ‘sensitivity’. R package vignette, February
2017.
Z. G. Qian, H. Wu, and C. F. J. Wu. Gaussian process models for computer experiments
with qualitative and quantitative factors. Technometrics, 50:383–396, 2009.
C. E. Rasmussen and C. K. I. Williams. Gaussian processes for machine learning. MIT
Press, Cambridge, MA, 2006.
G.O. Roberts, A. Gelman, and W.R. Gilks. Weak convergence and optimal scaling
of random walk Metropolis algorithms. The Annals of Applied Probability , 7(1):
110–120, 1997.
O. Roustant, D. Ginsbourger, and Y. Deville. DiceKriging, DiceOptim: Two R Pack-
ages for the Analysis of Computer Experiments by Kriging-Based Metamodeling and
Optimization. Journal of Statistical Software , 51(1), 2012.
J. Sacks, W. J. Welch, T. J. Mitchell, and H. P. Wynn. Design and analysis of computer
experiments (with discussion). Statistical Science, 4:409–435, 1989.
A. Saltelli, M. Ratto, T. Andres, F. Campolongo, J. Cariboni, D. Gatelli, M. Saisana,
and S. Tarantola. Global Sensitivity Analysis . Wiley, 2008.
149

---

## Page 170

T. J. Santner, B. J. Williams, and W. I. Notz. The Design and Analysis of Computer
Experiments. Springer, New York, 2003.
M. Schonlau and W. J. Welch. Screening Methods for Experimentation in Industry,
Drug Discovery and Genetics , chapter Screening the Input Variables to a Computer
Model Via Analysis of Variance and Visualization, pages 308–327. Springer, 2006.
S. Seo, M. Wallat, T. Graepel, and K. Obermayer. Gaussian process regression: Active
data selection and test point rejection. In Proceedings of the International Joint
Conference on Neural Networks , volume 3, pages 241–246. IEEE, 2000.
A. F. Stein, R. R. Draxler, G. D. Rolph, B. J. B. Stunder, M. D. Cohen, and F. Ngan.
NOAA’s HYSPLIT Atmospheric Transport and Dispersion Modeling System. Bul-
letin of the American Meteorological Society , 2015.
M. L. Stein. Interpolation of Spatial Data: Some Theory for Kriging . Springer, 1999.
G. Stevens and S. Atamturktur. Mitigating error and uncertainty in partitioned anal-
ysis: A review of veriﬁcation, calibration and validation methods for coupled simu-
lations. Archives of Computational Methods in Engineering , pages 1–15, 2016.
M. Titsias and N. D. Lawrence. Bayesian Gaussian process latent variable model.
Journal of Machine Learning Research - Proceedings Track, 9:844–851, 2010.
W. J. Welch, R. J. Buck, J. Sacks, H. P. Wynn, T. J. Mitchell, and M. D. Morris.
Screening, predicting, and computer experiments. Technometrics, 1992.
150

---

## Page 171

Index
active learning - Cohn, 52
active learning - MacKay, 52, 58
adaptive design, see sequential experi-
mental design
CBR release modelling, 2, 74, 92, 109,
143
correlation functions, 9
Gaussian, 10, 16, 48, 95, 96
Mat´ ern, 10, 15, 16, 95
power-exponential, 10, 16, 19
squared-exponential, see correlation
functions, Gaussian
covariance function, 9
coverage design, 50, 51
deep Gaussian process, 4
dose response model, 114
Dstl, 2, 74, 80, 114
elementary eﬀects method, 67
HYSPLIT, 109
input screening, 68
Latin hypercube design, 49
maximin distance design, 49, 51
maximum likelihood estimation, 17
mean square prediction error, 51
Metropolis-Hastings algorithm, 21
minimax distance design, 50, 51
model decomposition, 65, 67, 69
Monte Carlo integration, 33, 41, 42, 67,
72, 73
mutual information for computer exper-
iments, 52
neural network, 4
non-standardised t-distribution, 12, 69
nugget, 15, 17, 19, 52
prior distribution, 4, 8, 12, 69
conjugate prior, 12, 14, 23
non-informative prior, 13, 14, 23
sensitivity index, see Sobol’ index
sequential experimental design, 51, 57,
61
Sobol’ index, 65, 67, 71, 93, 141
stochastic model, 25, 143
total eﬀect index, 66, 68, 71
uncertain input, 30, 32, 35, 44
variance index, see Sobol’ index
variational inference, 29
151

---
