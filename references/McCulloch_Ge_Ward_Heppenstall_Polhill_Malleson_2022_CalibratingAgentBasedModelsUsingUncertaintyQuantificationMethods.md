# McCulloch_Ge_Ward_Heppenstall_Polhill_Malleson_2022_CalibratingAgentBasedModelsUsingUncertaintyQuantificationMethods.pdf

## Page 1

Calibrating Agent-Based Models using
Uncertainty Quantification Methods
Josie McCulloch/one.pnum,/two.pnum, Jiaqi Ge/one.pnum, Jonathan A. Ward/one.pnum,/three.pnum, Alison
Heppenstall/four.pnum,/five.pnum, J. Gareth Polhill/six.pnum, Nick Malleson/one.pnum,/four.pnum
/one.pnumLeeds Institute for Data Science, University of Leeds, Worsley Building, LS/two.pnum, /nine.pnumNL, Leeds, UK
/two.pnumSchool of Geography, University of Leeds, AB/one.pnum/five.pnum /eight.pnumQH, Leeds, UK
/three.pnumSchool of Mathematics, University of Leeds, LS/two.pnum /nine.pnumJT , UK
/four.pnumAlan T uring Institute, /two.pnumQR, John Dodson House, /nine.pnum/six.pnum Euston Rd, London NW/one.pnum /two.pnumDB, UK
/five.pnumUniversity of Glasgow, School of Social and Political Sciences, Bute Gardens, G/one.pnum/two.pnum /eight.pnumRT ,
Glasgow, UK
/six.pnumThe James Hutton Institute, Craigiebuckler, Aberdeen, AB/one.pnum/five.pnum /eight.pnumQH, UK
Correspondence should be addressed to J.McCulloch@leeds.ac.uk
Journal of Artificial Societies and Social Simulation /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum
Doi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum Url: http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.html
Received: /one.pnum/nine.pnum-/zero.pnum/five.pnum-/two.pnum/zero.pnum/two.pnum/one.pnum Accepted: /two.pnum/nine.pnum-/zero.pnum/one.pnum-/two.pnum/zero.pnum/two.pnum/two.pnum Published: /three.pnum/one.pnum-/zero.pnum/three.pnum-/two.pnum/zero.pnum/two.pnum/two.pnum
Abstract: Agent-based models (ABMs) can be found across a number of diverse application areas ranging from
simulating consumer behaviour to infectious disease modelling. Part of their popularity is due to their ability to
simulate individual behaviours and decisions over space and time. However, whilst there are plentiful examples
within the academic literature, these models are only beginning to make an impact within policy areas. Whilst
frameworks such as NetLogo make the creation of ABMs relatively easy, a number of key methodological issues,
including the quantification of uncertainty, remain. In this paper we draw on state-of-the-art approaches from
the fields of uncertainty quantification and model optimisation to describe a novel framework for the calibra-
tion of ABMs using History Matching and Approximate Bayesian Computation. The utility of the framework is
demonstrated on three example models of increasing complexity: (i) Sugarscape to illustrate the approach on
a toy example; (ii) a model of the movement of birds to explore the eﬀicacy of our framework and compare it to
alternative calibration approaches and; (iii) theRISC model of farmer decision making to demonstrate its value
in a real application. The results highlight the eﬀiciency and accuracy with which this approach can be used to
calibrate ABMs. This method can readily be applied to local or national-scale ABMs, such as those linked to the
creation or tailoring of key policy decisions.
Keywords: Calibration, Optimisation, History Matching, Approximate Bayesian Computation, Uncertainty, Agent-
Based Modelling
Introduction
/one.pnum./one.pnumAgent-based modelling has grown in popularity over the past twenty years (Heppenstall et al. /two.pnum/zero.pnum/two.pnum/zero.pnum). Its ability
to simulate the unique characteristics and behaviours of individuals makes it a natural metaphor for modelling
and understanding the impacts of individual decisions within social and spatial systems. Applications range
from creating models of daily mobility (Crols & Malleson /two.pnum/zero.pnum/one.pnum/nine.pnum), consumer behaviour (Sturley et al. /two.pnum/zero.pnum/one.pnum/eight.pnum) and
infectious disease modelling (Li et al. /two.pnum/zero.pnum/one.pnum/seven.pnum).
/one.pnum./two.pnumHowever, there remain important methodological challenges to be resolved if the full potential of agent based
modelling is to be realised. The maturation of the agent based modelling approach is reflected in several re-
cent position pieces (Polhill et al. /two.pnum/zero.pnum/one.pnum/nine.pnum; Manson et al. /two.pnum/zero.pnum/two.pnum/zero.pnum). These contributions, whilst wide ranging in their
perspectives, have a number of common themes including issues such as common practice for creation of rule
sets, embedding behaviour, and establishing robust calibration and validation routines.
/one.pnum./three.pnumWithin this paper, we focus on developing a more robust approach to the calibration of model parameters within
ABMs. Calibration involves running the model with diﬀerent parameters and testing, for each case, how well
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 2

the model performs by comparing the output against empirical data. The goal is to find parameter sets that
minimise the model’s error and can be used to provide a range of predictions or analyses (Huth & Wissel /one.pnum/nine.pnum/nine.pnum/four.pnum;
Ge et al. /two.pnum/zero.pnum/one.pnum/eight.pnum; Grimm et al. /two.pnum/zero.pnum/zero.pnum/five.pnum; Purshouse et al. /two.pnum/zero.pnum/one.pnum/four.pnum).
/one.pnum./four.pnumThere are three specific problems related to the calibration of ABMs that need to be addressed. First,computa-
tional cost: ABMs are o/f_ten computationally expensive and thus calibration algorithms that require large num-
bers of model-runs can be infeasible. Finding optimal parameters while minimising the number of model-runs
is essential. Second, there are o/f_tenuncertainties in the real-world process that an ABM is designed to simulate.
This can be because any observations taken are inaccurate or because the system is stochastic and, therefore,
multiple observations lead to diﬀerent results. Third,model discrepancy: models will only ever be abstractions
of real-world systems, there will always be a degree of error between an optimised model and an observation
(Strong et al. /two.pnum/zero.pnum/one.pnum/two.pnum).
/one.pnum./five.pnumAddressing these issues requires a diﬀerent perspective to be taken by agent-based modellers. We present a
novel framework that adapts established methods from the field of uncertainty quantification (UQ). We use his-
tory matching (HM) (Craig et al. /one.pnum/nine.pnum/nine.pnum/seven.pnum) to quickly rule outimplausible models and reduce the size of the parameter
space that needs to be searched prior to calibration. This also reduces the computational cost of calibration.
To address uncertainties, we identify and quantify the various sources of uncertainty explicitly. The quantified
uncertainties are used to measure the implausibility of parameters during HM, and to inform a threshold of
acceptable model error during calibration. Finally, to gain a better understanding of model discrepancy, Ap-
proximate Bayesian Computation (ABC) is used to provide credible intervals over which the given parameters
could have created the observed data (Csilléry et al. /two.pnum/zero.pnum/one.pnum/zero.pnum; Marin et al. /two.pnum/zero.pnum/one.pnum/two.pnum; Turner & Van Zandt /two.pnum/zero.pnum/one.pnum/two.pnum; Sunnåker
et al. /two.pnum/zero.pnum/one.pnum/three.pnum) .
/one.pnum./six.pnumThis framework is successfully applied to three models of increasing complexity. First, we use the well doc-
umented model ‘Sugarscape’ (Epstein & Axtell /one.pnum/nine.pnum/nine.pnum/six.pnum) as a toy example to show step-by-step how to apply the
framework, highlighting its simplicity and eﬀectiveness. Second, we use a model that simulates the popula-
tion and social dynamics of territorial birds, which has previously been used in a detailed study of parameter
estimation using a variety of methods, including ABC (Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum). With this model, we highlight the ad-
vantages of using our framework over other methods of calibration in the literature. In this case the number
of model-runs required for calibration is reduced by approximately half by using HM before ABC, compared to
using ABC alone. Finally, we apply our framework to a more complex ABM that simulates the changes in the
sizes of cattle farms in Scotland over a period of /one.pnum/three.pnum years (Ge et al. /two.pnum/zero.pnum/one.pnum/eight.pnum).
/one.pnum./seven.pnumThe contribution of this paper is a flexible, more eﬀicient and robust approach to ABM calibration through a
novel framework based on uncertainty quantification. The code and results are available online at https:
//github.com/Urban-Analytics/uncertainty.
Background
Uncertainty and agent-based models
/two.pnum./one.pnumUnderstanding and quantifying sources of uncertainty in the modelling process is essential for successful cal-
ibration. Indeed, quantifying uncertainty (Heppenstall et al. /two.pnum/zero.pnum/two.pnum/zero.pnum) as well as sensitivity analysis, calibration
and validation more generally (Windrum et al. /two.pnum/zero.pnum/zero.pnum/seven.pnum; Crooks et al. /two.pnum/zero.pnum/zero.pnum/eight.pnum; Filatova et al. /two.pnum/zero.pnum/one.pnum/three.pnum) are seen as ongoing
challenges in agent-based modelling.
/two.pnum./two.pnumFortunately there is a wealth of prior research to draw on; the field of Uncertainty Quantification oﬀers a means
of quantifying and characterising uncertainties in models and the real world (Smith /two.pnum/zero.pnum/one.pnum/three.pnum). Typically, there are
two forms of uncertainty quantification: forward uncertainty propagation investigates the impacts of random
inputs on the outputs of a model (i.e., sensitivity analysis), whereas inverse uncertainty quantification is the
process of using experimental data (outputs) to learn about the sources of modelling uncertainty (Arendt et al.
/two.pnum/zero.pnum/one.pnum/two.pnum) (i.e., parameter estimation or calibration). Here we are concerned with the latter. In the context of ABMs,
there are several acknowledged sources from which uncertainty can originate and then propagate through the
model. These sources include: parameter uncertainty, model discrepancy/uncertainty, ensemble variance, and
observation uncertainty (Kennedy & O’Hagan /two.pnum/zero.pnum/zero.pnum/one.pnum).
/two.pnum./three.pnumParameter uncertainty can stem from the challenge of choosing which parameters to use (the model may have
too few or too many) as well as the values of the parameters themselves. The values may be incorrect because
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 3

the measuring device is inaccurate, or the parameters may be inherently unknown and cannot be measured
directly in physical experiments (Arendt et al. /two.pnum/zero.pnum/one.pnum/two.pnum).
/two.pnum./four.pnumA further complication with parameter uncertainty is that ofidentifiability or equifinality, where the same model
outcomes can arise from diﬀerent sets of parameter values. This problem is prevalent in agent-based mod-
elling due to the large numbers of parameters that o/f_ten characterise models. This means standard sensitivity
analysis—a commonly used means of assessing the impact of parameters on model results—may have limited
utility when performed on an ABM because the model may be insensitive to diﬀerent parameter values (ten
Broeke et al. /two.pnum/zero.pnum/one.pnum/six.pnum). This also makes model calibration problematic because it might be diﬀicult to rule out im-
plausible parameter combinations at best, or at worst there may be many ‘optimal’ parameter combinations
with very diﬀerent characteristics.
/two.pnum./five.pnumModel discrepancy, also referred to asmodel uncertainty, is the “diﬀerence between the model and the true data-
generating mechanism” (Lei et al. /two.pnum/zero.pnum/two.pnum/zero.pnum). The model design will always be uncertain as it is impossible to have
a perfect model of a real-world process. Instead, a simplification must be made that will rely on assumptions
and imperfections (e.g., missing information). If model discrepancy is not accounted for in calibration then
the estimated parameter, rather than representing physically meaningful quantities, will have values that are
“intimately tied to the model used to estimate them” (Lei et al. /two.pnum/zero.pnum/two.pnum/zero.pnum). A further diﬀiculty is that it can be hard to
separate parameter uncertainty from model discrepancy, which exacerbates the identifiability problem (Arendt
et al. /two.pnum/zero.pnum/one.pnum/two.pnum).
/two.pnum./six.pnumThe third form of uncertainty, ensemble variance, refers to the uncertainty that arises naturally with stochastic
models. If the model is stochastic, then each time it is run the results will diﬀer. Typically stochastic uncer-
tainty is accounted for by running a model a large numbers of times with the same parameter combinations
(an ensemble of model instances) and the variance in the ensemble output provides a quantitative measure of
stochastic uncertainty.
/two.pnum./seven.pnumFinally observation uncertainty arises due to imperfections in the process of measuring the target system. This
is typically the case when either the equipment used to collect observations provides imprecise or noisy data
(Fearnhead & Künsch /two.pnum/zero.pnum/one.pnum/eight.pnum), or in cases when multiple observations diﬀer due to the natural variability of the
real world.
Calibration of agent-based models
/two.pnum./eight.pnumThe quantitative calibration of ABMs can be categorised into two groups: point estimation, and categorical or
distributional estimation (Hassan et al. /two.pnum/zero.pnum/one.pnum/three.pnum). The former tries to find a single parameter combination that will
produce the best fit-to-data, while the latter assigns probabilities to multiple parameter combinations over a
range of plausible values. A variety of point estimation methods have been used, including minimum distance
(e.g., least squared errors), maximum likelihood estimation (Zhang et al. /two.pnum/zero.pnum/one.pnum/six.pnum), simulated annealing (Neri /two.pnum/zero.pnum/one.pnum/eight.pnum),
and evolutionary algorithms (Heppenstall et al. /two.pnum/zero.pnum/zero.pnum/seven.pnum; Moya et al. /two.pnum/zero.pnum/two.pnum/one.pnum). Other methods include ordinary and
diﬀerential equations, and linear regression (Pietzsch et al. /two.pnum/zero.pnum/two.pnum/zero.pnum).
/two.pnum./nine.pnumExamples of categorical or distributional calibration include Pattern Oriented Modelling (POM), HM, Bayesian
networks (Abdulkareem et al. /two.pnum/zero.pnum/one.pnum/nine.pnum) and ABC (van der Vaart et al. /two.pnum/zero.pnum/one.pnum/five.pnum). While point estimation methods aim
to find a single parameter point with the best fit-to-data, a selection of the best fitting parameters exposes
how diﬀerent mechanisms in the model explain the data (Purshouse et al. /two.pnum/zero.pnum/one.pnum/four.pnum). Furthermore, categorical and
distributional estimation methods provide additional information on the uncertainty of the parameters and the
model outputs.
/two.pnum./one.pnum/zero.pnumPattern Oriented Modelling (POM), also called inverse modelling, is an approach to develop models that will
reproduce multiple patterns from various hierarchical levels and diﬀerent spatial or temporal scales (Grimm
et al. /two.pnum/zero.pnum/zero.pnum/five.pnum). It is both a calibration approach and a design principle for individual or agent-based modelling.
Model elements not needed to reproduce the desired patterns are removed or modified during the model de-
velopment process. An advantage of this is that validation does not solely happen a/f_ter creation of the model
and on one set of final results alone. Instead, it is validated while being built on multiple patterns, which makes
the model more robust and credible (Waldrop /two.pnum/zero.pnum/one.pnum/eight.pnum).
Approximate Bayesian Computation (ABC)
/two.pnum./one.pnum/one.pnumBayesian approaches have been used to calibrate ABMs (Grazzini et al. /two.pnum/zero.pnum/one.pnum/seven.pnum). The Bayesian approach to cali-
bration is not new (Kennedy & O’Hagan /two.pnum/zero.pnum/zero.pnum/one.pnum), but the diﬀiculty in calculating a likelihood function for complex
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 4

models hinders the use of this approach for models that aren’t entirely based on mathematically tractable prob-
ability distributions.
/two.pnum./one.pnum/two.pnumMore recently approximate Bayesian computation (ABC) has been proposed which, unlike traditional Bayesian
statistics, does not require the calculation of a likelihood function (Turner & Van Zandt /two.pnum/zero.pnum/one.pnum/two.pnum). This is useful for
ABMs because deriving a likelihood function for this approach is usually infeasible. The goal of ABC diﬀers fun-
damentally from the simulated minimum diﬀerence. ABC does not attempt to find only the single maximum
likelihood parameter, but instead estimates a full posterior distribution that quantifies the probability of pa-
rameter values across the entire sample space producing the observed data.
/two.pnum./one.pnum/three.pnumABC involves sampling a set of parameters from a prior distribution and testing if the model error using those
parameters is less than a chosen threshold ϵ. If the error is smaller than ϵ then the parameter set is accepted,
otherwise it is rejected. Testing a suﬀiciently large and diverse range of parameters tested facilitates the approx-
imation of the posterior distribution, i.e., the probability of a parameter set given the data. However, sampling
the parameter space and running the model for each set of parameters can be time-consuming, particularly
if there are many dependent parameters or the model takes a long time to run. Therefore, eﬀicient sampling
methods are necessary. Many diﬀerent ABC algorithms, such as rejection sampling and sequential Monte Carlo,
have been applied in the literature, a selected summary of which can be found by Turner & Van Zandt (/two.pnum/zero.pnum/one.pnum/two.pnum) and
Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum).
History Matching
/two.pnum./one.pnum/four.pnumHistory matching (HM) is a procedure used to reduce the size of the candidate parameter space (Craig et al. /one.pnum/nine.pnum/nine.pnum/seven.pnum)
to those that are plausible. HM has been applied to ABMs in recent literature (Li et al. /two.pnum/zero.pnum/one.pnum/seven.pnum; Andrianakis et al.
/two.pnum/zero.pnum/one.pnum/five.pnum; Stavrakas et al. /two.pnum/zero.pnum/one.pnum/nine.pnum) but, despite its power, use of the method with ABMs remains limited.
/two.pnum./one.pnum/five.pnumHM involves sampling from the parameter space and measuring the implausibility of each sample. The implau-
sibility is defined by the error of the simulation run (with the chosen parameters) and the uncertainties around
the model and observation. Each sample is labelled asnon-implausible (the model could produce the expected
output) or implausible (the model is unlikely to produce the expected output with the chosen parameters).
HM is carried out in waves. In each wave, the parameter space is sampled and split into implausible and non-
implausible regions. Each subsequent wave samples from the non-implausible region found in the previous
wave. Throughout the procedure, the non-implausible region should decrease as the waves narrow towards
the best set of parameters.
/two.pnum./one.pnum/six.pnumNote that HM does not make any probabilistic statements (e.g., a likelihood or posterior distribution) about the
non-implausible space (Andrianakis et al. /two.pnum/zero.pnum/one.pnum/five.pnum). By contrast, Bayesian calibration methods create a posterior
probability distribution on the input space and do not discard implausible areas.
Methods
/three.pnum./one.pnumHere, we describe the process of HM, ABC and our framework that combines the two in more detail. Figure /one.pnum
highlights the process used. Note that although the diagram describes the rejection sampling method of ABC,
any alternative method may be used instead. Whilst HM and ABC are useful when used alone, they become
more powerful when used together. Using HM before ABC is advantageous because HM takes uncertainties of
the model and observation into account whilst searching the parameter space. This enables the researcher to
decide if a parameter may be plausible based on a single run of the model instead of requiring an ensemble of
runs for each parameter tested. This allows exploration of the parameter space with fewer runs of the model
than with an ABC method alone.
/three.pnum./two.pnumWe treat the non-implausible space found through HM as a probabilistic uniform distribution of parameters that
fit the model. We propose using this distribution as an informed prior for the ABC procedure, which will then
provide a more detailed posterior distribution.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 5

Figure /one.pnum: An overview of the proposed framework combining HM with ABC. Note that the figure demonstrates
the process of the ABC rejection sampling process, but any other ABC process may be used.
History Matching (HM)
/three.pnum./three.pnumConsider a total ofR observations andR simulation outputs that are intended to match the observations. Let
zr be the rth observation, and f r(x) be the rth output from the simulator f with parametersx. For HM, we
calculate the implausibility thatx is an acceptable input (i.e., the possibility that the parameter will lead to the
expected output). To achieve this, we can compare the model output against the expected output as (Craig
et al. /one.pnum/nine.pnum/nine.pnum/seven.pnum):
I r(x) = d2(
zr,f r(x)
)
V ro +V rs +V rm
, (/one.pnum)
whered2(
zr,f r(x)
)
is the squared error of the model output compared against the expected output. If not
explicitly given, we assume this to be
(
zr−f r(x)
)2
. The variable V r
o is the variance associated with the ob-
servation aroundzr (observation uncertainty),V r
s is the ensemble variance, andV r
m is the model discrepancy.
Note it is not always necessary to include all of these terms of uncertainty (Papadelis & Flamos /two.pnum/zero.pnum/one.pnum/nine.pnum; Vernon
et al. /two.pnum/zero.pnum/one.pnum/zero.pnum). In the case of multiple outputs (i.e.,R >1), a separate measure of implausibility is measured per
output and the maximum implausibility is used (Andrianakis et al. /two.pnum/zero.pnum/one.pnum/five.pnum).
/three.pnum./four.pnumEnsemble variability is sometimes assumed to be independent of the inputs (Papadelis & Flamos /two.pnum/zero.pnum/one.pnum/nine.pnum), and
so only one possible input (or input vector) is tested. However, ensemble variability may actually diﬀer de-
pending on the input tested and, therefore, it is important to test a small selection of possible inputs in the
non-implausible space (Andrianakis et al. /two.pnum/zero.pnum/one.pnum/five.pnum).
/three.pnum./five.pnumWe use a constant threshold, denotedc, to determine ifx is implausible or otherwise according to the implaus-
bility scoreI r(x) given by Equation /one.pnum. IfI r(x)≥ c then the error between the simulation output and obser-
vation is considered too great, even when considering all of the associated uncertainties. If I r(x) < c, thenx
is retained as part of the non-implausible space. The value of c is usually chosen using Pukelsheim’s 3σ rule
(Pukelsheim /one.pnum/nine.pnum/nine.pnum/four.pnum). This implies that the correct set of parametersx will result inI r(x) < 3 with a probability
of at least /zero.pnum./nine.pnum/five.pnum. This process is repeated for multiple pointsx within the sample space, discarding those values
ofx that are deemed implausible and retaining those that are not implausible. The retained values are then
explored in the next wave. For each subsequent wave we must:
• Re-sample within the space that was found to be non-implausible.
• Re-calculate the model discrepancy and ensemble variance. This is necessary because our search space
has narrowed towards models that fit better and so it is expected that the uncertainties about this new
space will also reduce.
• Perform a new wave of HM within the narrowed space using its newly quantified uncertainties.
/three.pnum./six.pnumThe HM process continues until one or more stopping criteria are met (Andrianakis et al. /two.pnum/zero.pnum/one.pnum/five.pnum). For example, it
may be stopped when all of the parameters are found to be non-implausible. Other common criteria are when
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 6

the uncertainty in the emulator is smaller than the other uncertainties, or if the output from the simulator is
considered to be close enough to the observation. In our examples, we stop the process when either all of the
parameters are found to be non-implausible, or the area of the non-implausible space does not decrease (even
if some parameters within the area are found to be implausible).
Approximate Bayesian Computation (ABC)
/three.pnum./seven.pnumWe now describe the process of the rejection sampling ABC algorithm, which we use in our examples. Note,
however, that alternative ABC methods that search the sample space more eﬀiciently may be used, such as
Markov chain Monte Carlo or sequential Monte Carlo (Turner & Van Zandt /two.pnum/zero.pnum/one.pnum/two.pnum; Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum). To conduct
ABC, samples are selected from a prior distribution. As HM does not tell us if any parameter set is more or less
probable than another, our prior is represented as a uniform distribution. We use n particles that search the
non-implausible parameter space. Large values of n (above 10, 000) will provide accurate results, whereas a
smallern may be used at the expense of decreasing the power of the result. For each particle, we sample from
our prior and run the model. If the error of the model output is less thanϵ we keep the sample for that particle.
Otherwise, if the error is too large then we re-sample from the prior until we find a successful parameter set for
that particle.
/three.pnum./eight.pnumChoosing an optimum value forϵ can be challenging. Settingϵ close to zero would ensure a near exact posterior,
but will result in nearly all samples being rejected, making the procedure computationally expensive (Sunnåker
et al. /two.pnum/zero.pnum/one.pnum/three.pnum). Increasingϵ allows more parameters to be accepted but may introduce bias (Beaumont et al. /two.pnum/zero.pnum/zero.pnum/two.pnum).
One common method to deal with this is to choose a large value in the initial run of the algorithm and gradually
decreaseϵ over subsequent runs. In this case, each value of ϵ may be set ahead of time (Toni et al. /two.pnum/zero.pnum/zero.pnum/nine.pnum) or
may be adapted a/f_ter each iteration (Del Moral et al. /two.pnum/zero.pnum/one.pnum/two.pnum; Daly et al. /two.pnum/zero.pnum/one.pnum/seven.pnum; Lenormand et al. /two.pnum/zero.pnum/one.pnum/three.pnum). In our case,
we propose using the uncertainties quantified in the final wave of HM to inform the initial choice ofϵ and then
adapting the value in any further iterations.
/three.pnum./nine.pnumOnce each particle has a successful parameter set, the posterior distribution can be estimated. Kernel density
estimation is a common approach to approximate the posterior (Beaumont et al. /two.pnum/zero.pnum/zero.pnum/two.pnum). The posterior may then
be further refined by re-running the ABC process using the posterior from the first run as the prior for the second
run.
A framework for robust validation: SugarScape example
/three.pnum./one.pnum/zero.pnumIn this paper, we propose using HM together with ABC to calibrate the structure and parameters of an ABM.
Specifically, the proposed process consists of the following four steps:
• Define the parameter space to be explored.
• Quantify all uncertainties in the model and observation.
• Run HM on the parameter space.
• Run ABC, using the HM results as a prior.
/three.pnum./one.pnum/one.pnumFrom these steps, we gain a posterior distribution of the parameters, which can be sampled to obtain a distri-
bution of plausible outcomes from the model. The uncertainties quantified in the second step can then be used
to understand the reliability of the model’s outputs.
/three.pnum./one.pnum/two.pnumIn this section, we describe the process of these steps for the general case. We then demonstrate each step
using the toy model SugarScape (Epstein & Axtell /one.pnum/nine.pnum/nine.pnum/six.pnum).
Define the parameter space to be explored
/three.pnum./one.pnum/three.pnumWe must first decide the ranges that each parameter could take (i.e., the parameter space to be explored). This
may be decided qualitatively, through expert judgement (Cooke & Goossens /two.pnum/zero.pnum/zero.pnum/eight.pnum; Zoellner et al. /two.pnum/zero.pnum/one.pnum/nine.pnum). In some
cases, the potential values of a parameter are directly measurable (e.g., the walking speed of pedestrians) and,
therefore, quantitative measurements can be used to choose an appropriate range of values for the parameter.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 7

Quantify all uncertainties in the model and observation
/three.pnum./one.pnum/four.pnum Model discrepancy.When searching the parameter space of a model, we estimate the model discrepancy by
taking a subset of the samples that are tested for implausibility, ensuring the subset covers the parameter space
well (i.e., samples are not clustered together). The model is run once for each sample and the variance of the
errors across the samples is calculated as:
V r
m = 1
N− 1
N∑
n=1
(
d
(
zr,f r(xn)
)
−Er(x)
)2
, (/two.pnum)
whereN is the total number of samples used,d is the measure of error between therth expected output (zr) and
therth model output (f r(xn)) for the parametersxn, andEr(X) is the average model error for each parameter
set inx.
/three.pnum./one.pnum/five.pnumWe measure the error of multiple samples (instead of using only a single sample) because diﬀerent samples
within the space will likely result in diﬀerent quantified errors, and the variance of diﬀerent samples should
provide a better overview of the whole space than a single sample.
/three.pnum./one.pnum/six.pnum Ensemble variance.We select a subset of N samples that will be tested as part of HM. For each sample, run
the modelK times; larger values ofK will result in a more accurate result at the expense of increasing compu-
tational time. The variance is calculated between theK runs, and the average variance across theN samples
is calculated. Specifically, we measure:
V r
s = 1
N
N∑
n=1
[ 1
K− 1
K∑
k=1
(
d
(
zr,f r
k(xn)
)
−Er
K(xn)
)2]
, (/three.pnum)
whereK is the total number of runs in an ensemble,f r
k(xn) is therth output from thekth run of the model with
parametersxn, andEr(xn) is average model error across the ensembles as:
Er
K(xn) = 1
K
K∑
k=1
d
(
zr,f r
k(xn)
)
. (/four.pnum)
/three.pnum./one.pnum/seven.pnum Observation uncertainty.How observation uncertainty can be measured depends on how the observations
are obtained. If the real world process is directly measurable then multiple direct observations can be made
and their variance can be used to quantify the uncertainty.
/three.pnum./one.pnum/eight.pnumIt may also be the case that only indirect measurements can be obtained, and so there will be uncertainty in
transforming them so that they can be compared against the model output (Vernon et al. /two.pnum/zero.pnum/one.pnum/zero.pnum). If an observa-
tion cannot be measured, expert judgments may be useful in determining the expected model output and the
uncertainty around the expected output. For example, experts may provide quantiles of the expected output,
from which uncertainty can be understood (O’Hagan et al. /two.pnum/zero.pnum/zero.pnum/six.pnum).
Run HM on the parameter space
/three.pnum./one.pnum/nine.pnumGiven the defined parameter space (in step /one.pnum) and the uncertainties quantified (in step /two.pnum), we next apply HM. In
large or continuous parameter spaces, we use Latin-Hypercube Sampling (LHS) to select samples.
Run ABC, using the HM results as a uniform prior
/three.pnum./two.pnum/zero.pnumThe final non-implausible space found through HM is used as a uniform prior for ABC. Any appropriate ABC
method may be used, such as rejection sampling or sequential Monte Carlo. We propose using the uncertainties
measured in the final wave of HM to inform the initial value ofϵ. Based on Equation /one.pnum, let:
ϵ = 3(V r
o +V r
s +V r
m). (/five.pnum)
In subsequent iterations of ABC,ϵ may be adaptively reduced as suggested by Del Moral et al. (/two.pnum/zero.pnum/one.pnum/two.pnum) and Lenor-
mand et al. (/two.pnum/zero.pnum/one.pnum/three.pnum).
/three.pnum./two.pnum/one.pnumThe result of performing ABC is a posterior distribution over the non-implausible parameter space identified by
HM. Note that we do not perform ABC on the full initial parameter space chosen in step /one.pnum.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 8

A Step-by-Step Example: SugarScape
/four.pnum./one.pnumIn this section, we provide a step-by-step example of the proposed framework using the Sugarscape model
(Epstein & Axtell /one.pnum/nine.pnum/nine.pnum/six.pnum). Sugarscape is an environment that contains a resource (sugar) and agents that collect
and metabolise this resource. The environment is a grid in which sugar is distributed such that some regions are
rich with sugar, whilst others are scarce or bare. Figure /two.pnum shows the environment where darker regions indicate
higher amounts of sugar. The amount of sugar in a given location is an integer in the range[0, 4]. At the start of
the simulation, /one.pnum/zero.pnum/zero.pnum agents are placed in a random location of the environment. We use the Sugarscape example
provided by the Python-Mesa toolkit by Kazil et al. (/two.pnum/zero.pnum/two.pnum/zero.pnum). This implements a simple version of the model, in
which each agents’ only goal is to search for sugar to stay alive. We made minor changes to the code (detailed
in our source code) enabling us to change the maximum vision and metabolism of the agents).
Figure /two.pnum: The Sugarscape environment. The amount of sugar at each grid square is an integer ranging from /zero.pnum to
/four.pnum, where /zero.pnum is indicated by the lightest green and /four.pnum by the darkest.
/four.pnum./two.pnumIn each time step, the agents move, collect sugar, and consume sugar. More specifically, the agent movement
rule is (Epstein & Axtell /one.pnum/nine.pnum/nine.pnum/six.pnum):
• Observe all neighbours within vision range in the von Neumann neighbourhood.
• Identify the unoccupied locations that have the most sugar.
• If multiple locations have the same amount of sugar choose the closest.
• If multiple locations have the same amount of sugar and are equally close, randomly choose one.
• Move to the chosen location.
• Collect all of the sugar at the new location.
• Eat the amount of sugar required to survive (according to the agent’s metabolism).
• If the agent does not have enough sugar, they die.
/four.pnum./three.pnumIn each time step, the sugar grows back according to the sugar grow-back rule:
• Increase sugar amount by one if not at the maximum capacity of the given space.
/four.pnum./four.pnumIn this example, there are two parameters that we wish to explore. These are:
• The maximum possible metabolism of an agent
• The maximum possible vision of an agent
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 9

where metabolism defines how much an agent needs to eat in each step of the model, and vision defines how far
an agent can see and, consequently, how far they can travel in each step. Both of these parameters take integer
values, and the minimum metabolism or vision an agent may have is /one.pnum. The metabolism and vision given to an
agent is a random integer between /one.pnum and the calibrated maximum.
/four.pnum./five.pnumThe simulation begins with /one.pnum/zero.pnum/zero.pnum agents. However, some do not survive as there is not suﬀicient food. As such,
our measured outcome is the size of the population that the model can sustain . We create observational
data using the output of an identical twin model (a model run to gain an artificial real-world observation). With
the maximum metabolism as /four.pnum and the maximum vision as /six.pnum, the model was able to sustain a population of /six.pnum/six.pnum
agents.
/four.pnum./six.pnumStochasticity in the model arises from several sources. The initial locations of the agents are chosen randomly
in each run. When moving, if multiple locations are equally fit for an agent to move to, the location the agent
chooses out of these will be random. The metabolism and vision of each agent is an integer randomly chosen
within the defined range. These random choices leads to a stochastic model that will produce diﬀerent results
with each run.
Define the parameter space to be explored
/four.pnum./seven.pnumWe choose the plausible values for maximum metabolism to be in the range[1, 4]. We choose /four.pnum as the maximum
as there is no location in Sugarscape that has more than /four.pnum sugar. We choose the values for maximum vision to
be in the range [1, 16]. We choose /one.pnum/six.pnum as the maximum as this is the furthest distance from an empty location
(i.e., with no food) to a non-empty location.
Quantify all uncertainties in the model and observation
Model discrepancy
/four.pnum./eight.pnumWe are interested in finding the parameters that lead to a model that sustains a population of /six.pnum/six.pnum agents. To test
this, we ran the model with three diﬀerent parameter sets over /one.pnum/zero.pnum/zero.pnum model steps. We repeated this for a total
of /three.pnum/zero.pnum times to take into account ensemble uncertainty. The parameters are where {metabolism, vision} is {/one.pnum,/one.pnum},
{/two.pnum, /one.pnum/zero.pnum} and {/four.pnum, /seven.pnum}. For each case, we find that in all runs the agent population is stable by step /three.pnum/zero.pnum (see Figure
/three.pnum). To quantify the error of the model, we measure the absolute diﬀerence between the population at step /three.pnum/zero.pnum
and the expected population observed (i.e., /six.pnum/six.pnum). Therefore, to measure model discrepancy, we use Equation /two.pnum
wherez = 66 andd
(
z,f (xn)
)
=|z−f(xn)| (note that we have only one measured output and observation in
Sugarscape so we omitr from the formulae).
Figure /three.pnum: The total agent population in Sugarscape over /one.pnum/zero.pnum/zero.pnum steps for /three.pnum/zero.pnum runs of /three.pnum diﬀerent parameter sets.
Ensemble variance
/four.pnum./nine.pnumWe tested changes in ensemble variance across increasing ensemble sizes to find an optimal size. We tested
ensemble variance for the same three parameter sets used to determine when the model has stabilised. These
are where {metabolism, vision} is {/one.pnum,/one.pnum}, {/two.pnum, /one.pnum/zero.pnum} and {/four.pnum, /seven.pnum}. Figure /four.pnum shows how the ensemble variance changes with
ensemble size. We find the variance stabilised a/f_ter approximately /two.pnum/zero.pnum/zero.pnum runs, and so use this as our ensemble
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 10

size. The measured variance at these points where {metabolism, vision} is {/one.pnum,/one.pnum} is /one.pnum/three.pnum./zero.pnum, for {/two.pnum, /one.pnum/zero.pnum} is /one.pnum/two.pnum./zero.pnum/five.pnum, and for
{/four.pnum, /seven.pnum} is /one.pnum/eight.pnum./three.pnum/four.pnum.
Figure /four.pnum: The ensemble variance measured across ensemble sizes with {metabolism, vision} parameters {/one.pnum, /one.pnum}
(solid), {/two.pnum, /one.pnum/zero.pnum} (dashdot) and {/four.pnum, /seven.pnum} (dashed).
Observation uncertainty
/four.pnum./one.pnum/zero.pnumAs Sugarscape is a toy model, we have no uncertainty in our observation and consequentlyVo = 0 in Equation
/one.pnum.
Run HM on the parameter space
/four.pnum./one.pnum/one.pnumAs we have a reasonably small sample space, we measure the implausibility of each parameter pair. Note that
typically the sample space is too large and, as described above, LHS sampling is used instead. We performed
/one.pnum/zero.pnum waves of HM. Wave /one.pnum/zero.pnum did not reduce the non-implausible parameter space further so the procedure was
stopped. Figure /five.pnum shows the results of the first and final waves, where dark grey represents implausible regions
and light orange represents non-implausible regions. The figure shows the whole space explored; that is, prior
to wave /one.pnum the full set of a parameters is assumed to be non-implausible (and would be pictured entirely orange),
and each set of parameters in the space was tested for implausibility.
/four.pnum./one.pnum/two.pnumIn each wave, we retested each of the parameters that were found to be non-implausible in the previous wave.
For example, Figure /five.pnum shows the results of the sample space at the end of wave /one.pnum. The non-implausible (orange)
space here was used as the input for wave /two.pnum. In this example, the same parameters were retested because
the parameter space is discrete and so there were no other values to test. However, in a continuous space
(demonstrated later), new values within the plausible region are typically tested instead of retesting the same
values (Andrianakis et al. /two.pnum/zero.pnum/one.pnum/five.pnum).
Figure /five.pnum: Results of the first and final waves of HM on Sugarscape. Grey regions were found to be implausible,
whilst orange regions were found to be non-implausible.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 11

Run ABC, using the HM results as a uniform prior
/four.pnum./one.pnum/three.pnumFor Sugarscape, Figure /six.pnum shows the results of the ABC rejection sampling method. The results show that the
parameters with the highest probability of matching the observation (i.e., sustaining a population of /six.pnum/six.pnum agents)
are where {metabolism, vision} are {/four.pnum, /seven.pnum}, with the true parameters {/four.pnum, /six.pnum} (used to create the observation) also
obtaining a similarly high probability.
Figure /six.pnum: Results of ABC rejection sampling on the non-implausible Sugarscape parameters identified by HM.
/four.pnum./one.pnum/four.pnumThis example illustrates how HM can successfully reduce the space of possible parameter values and ABC can
quantify the probability that these non-implausible parameter values could have produced the observed data.
Experiments and Results
/five.pnum./one.pnumIn this section, we apply our HM and ABC framework to two ABMs of real-world processes. The first model
simulates the movement of territorial birds (Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum). This model was chosen because many traditional
calibration methods have been demonstrated using this model, enabling us to compare our approach with a
range of commonly used alternative approaches. The second model is more complex, simulating changes in
Scottish cattle farms from external policies over time (Ge et al. /two.pnum/zero.pnum/one.pnum/eight.pnum). This model was chosen because (i) it
provides a real-world test for the proposed framework and (ii) the calibration results themselves can provide
interesting insight into the behaviour of the real system.
Case Study /one.pnum: Comparing against alternative calibration methods
/five.pnum./two.pnumWe now compare our proposed approach to alternative calibration methods, including point-estimation meth-
ods (such as simulated annealing) and distribution-estimation methods (such as ABC alone, without HM).
Overview of the model
/five.pnum./three.pnumWe use an example model by Railsback & Grimm (/two.pnum/zero.pnum/one.pnum/nine.pnum). The purpose of this model to explore the social groups
that occur as a result of birds scouting for new territories. The entities of the model are birds and territories that
they may occupy. There are /two.pnum/five.pnum locations arranged in a one-dimensional row that wraps as a ring. Each step of
the model represents one month in time, and the simulation runs for /two.pnum/two.pnum years, the first two of which are ignored
for the results. In each step, ‘non-alpha’ birds will decide whether to scout for an alpha-bird free location where
they can become an alpha-bird. A full ODD of the model used, as well as a link to the source code, is provided
by Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum).
/five.pnum./four.pnumTwo model parameters are considered for calibration. These are the probability that a non-alpha bird will ex-
plore new locations, and the probability that it will survive the exploration. These are described as thescouting
probability and survival probability, respectively. Calibration of the model involves finding values for these two
parameters that enable the model to fit three criteria. Measured over a period of /two.pnum/zero.pnum years, the criteria are: /one.pnum) the
average total number of birds, /two.pnum) the standard deviation of total birds, and /three.pnum) the average number of locations
that lack an alpha bird. More details on the model and fitting criteria are provided by Railsback & Grimm (/two.pnum/zero.pnum/one.pnum/nine.pnum);
Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum). Priors of the parameters are uniformly distributed in the ranges
• Scouting probability: [0, 0.5], and
• Survival probability: [0.95, 1].
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 12

Uncertainties in the model
/five.pnum./five.pnumThe model aims to match the three criteria above, based on observational data. These criteria are combined
to obtain a single measurement of error (therefore only one model output) as provided by Railsback & Grimm
(/two.pnum/zero.pnum/one.pnum/nine.pnum). Specifically, we measure:
d2(z,f (x)) =e(f(x)1,z 1) +e(f(x)2,z 2) +e(f(x)3,z 3), (/six.pnum)
wheref(x)1 is the first model output, and z1 is the corresponding empirical data that is given as an interval
range of acceptable values that f(x)1 can fall in. The error in Equation /six.pnum is used with HM in Equation /one.pnum. An
interval is used instead of a single value to represent the uncertainty of the observation. The errore is:
e(f r(x),z r) =



0 f r(x)∈zr
(
¯z1−f r(x)
¯zr
)2
otherwise,
(/seven.pnum)
where ¯zr is the mean value of the range zr. We use Equation /six.pnum as the measurement of error for both HM and
ABC.
/five.pnum./six.pnum Observations.The observation variance is captured as a range of values each output can fall within. Instead of
treating this variance separately (withinVo in Equation /one.pnum), it is handled when measuring model error in Equation
/six.pnum.
/five.pnum./seven.pnum Model discrepancy.To measure model discrepancy, we select a random sample of /five.pnum/zero.pnum parameter sets using an
LHS design. We then measure the model discrepancy using Equation /two.pnum with the model error given in Equation
/six.pnum.
/five.pnum./eight.pnum Ensemble variance.We measure ensemble variance as given in Equations /three.pnum and /four.pnum. To choose the size of an
ensemble we selected /five.pnum/zero.pnum samples using an LHS design and ran the model for each sample across a variety of
ensemble sizes, measuring the variance for each case. Figure /seven.pnum shows the resulting ensemble variance as the
total runs of the model within an ensemble is increased. Figure /seven.pnuma shows that one sample stands out having
a much higher ensemble variance compared to the remaining /four.pnum/nine.pnum samples, which are indistinguishable from
each other in the figure. Figure /seven.pnumb shows the ensemble variance for these remaining /four.pnum/nine.pnum samples. The variance
appears to stabilise a/f_ter about /three.pnum/zero.pnum runs, so we choose this as our ensemble size.
Figure /seven.pnum: Results of ensemble variance in the birds model across diﬀerent ensemble sizes for /five.pnum/zero.pnum diﬀerent sam-
ples.
Results
/five.pnum./nine.pnumWe use LHS to generate /five.pnum/zero.pnum samples within the initial plausible space (this is the same number of LHS samples
as used by Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum).
/five.pnum./one.pnum/zero.pnumIn the first wave, the HM procedure judged that /one.pnum/eight.pnum of these /five.pnum/zero.pnum samples are non-implausible. We then re-sampled
(using a new set of /five.pnum/zero.pnum samples) within the new non-implausible region. A/f_ter the third wave of this procedure,
HM was unable to decrease the area of non-implausible space any further.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 13

/five.pnum./one.pnum/one.pnumFigure /eight.pnum shows the results of each wave. Each point represents an explored parameter that was found to be
implausible (grey) or non-implausible (orange). The results show that the model is more sensitive to scout-
ing survival than to scouting probability. The range of plausible values for scouting survival has reduced to
[0.9606, 0.9925], whereas the range of plausible values for scouting probability remains at [0, 0.5]. These re-
sults are similar to those found with ABC methods by (Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum).
Figure /eight.pnum: Results of three waves of HM on the birds model. Each point represents an explored parameter that
was found to be implausible (grey) or non-implausible (orange).
/five.pnum./one.pnum/two.pnumNext, we use the ABC rejection sampling method with /one.pnum/zero.pnum/zero.pnum/zero.pnum particles to obtain a probability distribution within
the sample space. Our prior is a uniform distribution of the non-implausible space found by HM. Figure /nine.pnuma
shows the resulting posterior distribution, where lighter shades indicate a higher probability. The results show
the model is able to match the criteria best if the scouting probability is in the approximate range[0.2, 0.5] and
if survival probability is approximately0.98. By contrast, we also performed ABC with the same number of par-
ticles but without the HM-informed prior. Figure /nine.pnumb shows that the posterior is much broader when information
from HM is not used. The results of ABC alone in Figure /nine.pnumb is not much more informative than the results from
HM alone in Figure /eight.pnum. These results are similar to those found using ABC alone (Thiele et al. /two.pnum/zero.pnum/one.pnum/four.pnum).
/five.pnum./one.pnum/three.pnumWe achieved a posterior with /three.pnum/one.pnum/eight.pnum/five.pnum runs of the model using HM and ABC. By contrast, Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum) obtained
similar results with ABC alone using over /one.pnum/one.pnum,/zero.pnum/zero.pnum/zero.pnum runs. They also demonstrate that simulated annealing and
evolutionary algorithms can be used to explore the parameter space. While these methods require fewer runs
of the model (/two.pnum/five.pnum/six.pnum and /two.pnum/nine.pnum/zero.pnum, respectively) than HM alone (/four.pnum/two.pnum/zero.pnum), they are intended to only provide the best fitting
parameters that were tested, whilst HM has the advantage of discovering a region of parameters that fits well
and ABC provides a posterior distribution within this region. Note that fewer runs may be used to estimate the
ensemble variance, therefore making HM computationally faster, but this may decrease its accuracy and lead
to non-implausible samples being quantified as implausible.
Figure /nine.pnum: Results of ABC rejection sampling on the birds model, using (a) HM results as an informed prior and
(b) an uninformed prior.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 14

Testing the accuracy of the proposed approach
/five.pnum./one.pnum/four.pnumTo test the accuracy of our proposed approach of using HM followed by ABC, we compare results from this
approach against using ABC alone across a range of parameter values. To do this, we generated /one.pnum/zero.pnum/zero.pnum pseudo-
random pairs of the survival probability and scouting probability parameters. The values were chosen using an
LHS design to ensure the samples eﬀectively cover the sample space. For each parameter pair, we want to use
the model to produce synthetic data that we then use to calibrate the model. In the previous sections, we cali-
brated the model using the acceptable ranges of model outputs described in paragraph /five.pnum./four.pnum, which derived from
observational studies. We have seen in Figure /nine.pnum that a relatively small range of scouting and survival probabili-
ties are likely to fall within these criteria. Since we are now using the model to produce ‘ground truth’ data over
a range of parameter values, we need to identify corresponding ranges of outputs that are acceptable. Thus for
each parameter pair, we ran the model /one.pnum/zero.pnum times to produce /one.pnum/zero.pnum observations, then we set the acceptable range
of each of the model fitting criteria to be the corresponding minimum and maximum from the /one.pnum/zero.pnum observations.
Using these observational ranges, we then performed HM followed by ABC rejection sampling using the same
process as described in the previous section (i.e., using Equation /six.pnum to measure error, a total of /three.pnum/zero.pnum model runs
to measure ensemble variance, a total of /five.pnum/zero.pnum samples across the plausible space for each wave of HM, and /one.pnum/zero.pnum/zero.pnum/zero.pnum
samples for ABC rejection sampling). This was carried out for each of the /one.pnum/zero.pnum/zero.pnum parameter pairs.
/five.pnum./one.pnum/five.pnumAcross the /one.pnum/zero.pnum/zero.pnum parameter pair tests, there were nine examples where the model outputtotal vacant locations
(see criteria /three.pnum in paragraph /five.pnum./four.pnum) was /zero.pnum when the model was run to generate observational data. This occurred
when the input survival probability was close to /one.pnum. The measurement error used by Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum) is not fit
for this situation (resulting in division by zero) and so HM (or any form of calibration) was unable to be performed
against these observations. In the /nine.pnum/one.pnum remaining tests, HM retained the correct parameters in /nine.pnum/zero.pnum cases and failed
in one case where the expected value for scouting probability was not found. However, in all other tests the plau-
sible range of scouting probability contained the correct test value/one.pnum. On average, the non-implausible space for
scouting probability was reduced to /eight.pnum/eight.pnum% of its original size, and the space for survival probability was reduced
to /four.pnum/two.pnum% of its original size.
/five.pnum./one.pnum/six.pnumWe next performed ABC rejection sampling with /one.pnum/zero.pnum/zero.pnum/zero.pnum particles on the /nine.pnum/one.pnum cases where HM could be run. We wish
to compare the results of using HM before ABC against using ABC alone. Therefore, we run ABC once using the
non-implausible space found through HM as an informed prior, and once using an uninformed prior. We found
that, on average, ABC required /two.pnum/zero.pnum/four.pnum/seven.pnum more model-runs when given an uninformed prior compared to when given
the HM-informed prior. The HM procedure required between /eight.pnum/zero.pnum and /three.pnum/two.pnum/zero.pnum runs. Taking this into account, if we
subtract the total model runs used to carry out HM from the total runs saved in the ABC process by using the
HM-informed prior for each of the /nine.pnum/one.pnum tests, then we find we saved an average of /one.pnum/five.pnum/seven.pnum/nine.pnum total model runs by using
HM before ABC, compared to not using HM. If more particles are used to generate a more accurate posterior this
diﬀerence is likely to increase.
/five.pnum./one.pnum/seven.pnumWe analysed the results by measuring the percentage of times the expected value was within the /nine.pnum/five.pnum% credible
interval (CI) across the /nine.pnum/one.pnum tests for both scouting probability and survival probability. We also measured the
average mean absolute error (MAE) and size of the /nine.pnum/five.pnum% CI across all tests. Table /one.pnum shows the results. The results
indicate that combining HM with ABC produces slightly smaller MAEs and slightly narrower CIs compared with
using ABC alone. However, the true parameter is less o/f_ten contained within the /nine.pnum/five.pnum% CI. Therefore, using HM
with ABC provides results that are more precise (as shown by the smaller MAEs) and more eﬀicient (requiring
fewer model runs), but at the cost of CIs that may be too small.
Contained within /nine.pnum/five.pnum% CI Mean Absolute Error Size of /nine.pnum/five.pnum% CI
ABC
scouting prob. /nine.pnum/two.pnum./three.pnum/one.pnum /zero.pnum./one.pnum/three.pnum/two.pnum /zero.pnum./four.pnum/four.pnum/seven.pnum
survival prob. /nine.pnum/six.pnum./seven.pnum/zero.pnum /zero.pnum./zero.pnum/zero.pnum/four.pnum /zero.pnum./zero.pnum/two.pnum/one.pnum
ABC and HM
scouting prob. /nine.pnum/zero.pnum./one.pnum/one.pnum /zero.pnum./one.pnum/three.pnum/zero.pnum /zero.pnum./four.pnum/three.pnum/four.pnum
survival prob. /nine.pnum/three.pnum./four.pnum/one.pnum /zero.pnum./zero.pnum/zero.pnum/three.pnum /zero.pnum./zero.pnum/one.pnum/five.pnum
Table /one.pnum: Information on the percentage of tests where the true parameter is contained within the /nine.pnum/five.pnum% credible
interval (CI) of the model runs, the average mean absolute error between the expected and actual results across
all runs, and the average size of the /nine.pnum/five.pnum% CI when using ABC alone or using HM before ABC.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 15

Case Study /two.pnum: Trends in Scottish Cattle Farms
/five.pnum./one.pnum/eight.pnumIn this section, we demonstrate that this framework is well suited for Pattern-Oriented Modelling (POM). In POM,
patterns are observed within the system being modelled. The structure of the ABM is then designed to explain
these observed patterns (Grimm et al. /two.pnum/zero.pnum/zero.pnum/five.pnum). Multiple plausible models are tested, and those which recreate
the observed patterns are retained (Rouchier et al. /two.pnum/zero.pnum/zero.pnum/one.pnum). We use HM to explore diﬀerent potential models and
rule out those that are implausible (i.e., could not recreate the data even when uncertainties about the model
and observed patterns are taken into account). Following HM, we use ABC to calculate the probabilities that the
remaining models can recreate the observations.
Overview of the model
/five.pnum./one.pnum/nine.pnumGe et al. (/two.pnum/zero.pnum/one.pnum/eight.pnum) developed a Rural Industries Supply Chain (RISC) ABM that simulates changes in the size of cattle
farms over time in Scotland, UK, where size is based on the total number of cattle. The purpose of the model is to
explain the phenomenon of farm size polarisation (the trend of disappearing medium-size farms), and predict
changes in farm sizes caused by diﬀerent possible scenarios that could occur as a result of the United Kingdom
leaving the European Union. The entities are agriculture holdings that farm cattle. Each step represents one
year and the simulation is run for /one.pnum/three.pnum years. The full ODD of the model is provided by Ge et al. (/two.pnum/zero.pnum/one.pnum/eight.pnum).
/five.pnum./two.pnum/zero.pnumThe model simulates changes in cattle farms over a historic period of /one.pnum/three.pnum years, from /two.pnum/zero.pnum/zero.pnum/zero.pnum to /two.pnum/zero.pnum/one.pnum/two.pnum. The empirical
data for this period was collected through an annual survey. Farms are categorised as small, medium or large
depending on the total cattle held. The model outputs one time-series for each of these three categories, show-
ing how the total number of farms in each category change over time. For each size category, the model output
is compared against the empirical data.
/five.pnum./two.pnum/one.pnumIn the RISC model, each year every farm owner makes a decision that will aﬀect the number of cattle and, there-
fore, the size of the farm. This decision may be influenced by diﬀerent circumstances and preferences. Four
factors were considered a potential influence on whether the owner decides to decrease, increase or maintain
the size of the holding (Weiss /one.pnum/nine.pnum/nine.pnum/nine.pnum). These are,
• Succession. Whether or not the owner has a successor to take over running the farm.
• Leisure. Whether farming is considered as a secondary (rather than primary) source of income.
• Diversification. Whether the farm is considered for diversification into tourism. This is strongly influ-
enced by whether or not neighbouring farms have diversified.
• Industrialisation. Whether a professional manager could be employed to help with an increased farm
size.
An ABM was designed to explore the dynamics behind changes in farm size over the years. In the model, the
above four parameters may be either switched on (aﬀecting farm owners’ decisions) or oﬀ. There are /one.pnum/six.pnum to-
tal possible combinations of these four factors. We wish to perform HM followed by ABC on these /one.pnum/six.pnum possible
models to explore which of them are plausible.
Uncertainties in the model
/five.pnum./two.pnum/two.pnumTo measure model error, we calculate the mean absolute scaled error (MASE) between the model output (from
one run) and the empirical data. The error of therth output (out of three) in thejth model (out of /one.pnum/six.pnum) is:
d(zr,f rj(x)) =
1
n
∑n
t=1|f rj
t (x)−zr
t|
1
n−1
∑n
t=2|zr
t−zr
t−1|, (/eight.pnum)
wheref(x)rj
t is the result of therth output from thejth model at timet,zr
t is the empirical data at timet, and
N is the total number of measurements collected. In this case,n = 13 as data is collected once per year over a
period of /one.pnum/three.pnum years. We use Equation /eight.pnum as the measurement of error for both HM and ABC.
/five.pnum./two.pnum/three.pnumTo perform HM, we must first quantify all of the uncertainties associated with the RISC model. We consider three
diﬀerent sources of uncertainty:
/five.pnum./two.pnum/four.pnum Observations.The empirical data is collected through a mandatory survey. Although typographical errors in
the data are possible, they are unknown and assumed to be negligible.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 16

/five.pnum./two.pnum/five.pnum Model discrepancy.For each model and each output, we measure the model error using Equation /eight.pnum. We then
average the errorsV rj
m across all /one.pnum/six.pnum possible models, resulting in a single model discrepancy term per output,
denotedV r
m.
/five.pnum./two.pnum/six.pnum Ensemble variance.The models are stochastic, meaning each time we run them the results will be diﬀerent.
We want to know how much variance there is across multiple runs. We run each model a total of /one.pnum/zero.pnum/zero.pnum times
and measure the variance in the results. We do this separately for each model and each output. Then, for each
output, we average the variance across all models. Note that it is not necessary to calculate ensemble variance
for each parameter set, but as there are only /one.pnum/six.pnum models, we have the computational resources to measure them
all. Figure /one.pnum/zero.pnum shows the results. We can see that the ensemble variance has stabilised for each output at an
ensemble size of /one.pnum/zero.pnum/zero.pnum runs.
Figure /one.pnum/zero.pnum: The ensemble variance in the RISC model across increasing ensemble sizes for each output (number
of small, medium and large farms).
/five.pnum./two.pnum/seven.pnumTo calculate ensemble variance for a given model j, we measure the diﬀerence between each ensemble run
with each other ensemble run using MASE (see Equation /eight.pnum). Given /one.pnum/zero.pnum/zero.pnum runs, this makes for a total of /four.pnum/nine.pnum/five.pnum/zero.pnum com-
parisons.
/five.pnum./two.pnum/eight.pnumFirst, the set of comparisons is given as
Dr
j =
99⋃
a=1
100⋃
b=a+1
max{V rj
m (f r
a(x),f r
b (x)), V rj
m (f r
b (x),f r
a(x))}, (/nine.pnum)
wheref r
a(x) is the result of the rth output in the ath run of the model. Note that V rj
m (see Equation /eight.pnum) is non-
symmetric, so we compare f r
a(x) withf r
b (x) in both directions in Equation /nine.pnum. Note that to ensure ensemble
variance and model discrepancy are directly comparable, we measure both using MASE.
/five.pnum./two.pnum/nine.pnumNext, we calculate the variance of the set of ensemble runs given in Equation /nine.pnum. This is:
V r
j = 1
4949
4950∑
a
(
Dr
ja−E(dr
j)
)2
, (/one.pnum/zero.pnum)
whereDr
ja is theath value in the setDr
j , andE(dr
k) is the average of the set.
/five.pnum./three.pnum/zero.pnumFinally, we calculate the average ensemble variance across the /one.pnum/six.pnum models for outputr as
V r
e = 1
16
16∑
j=1
V r
j . (/one.pnum/one.pnum)
These three steps (Equations /nine.pnum–/one.pnum/one.pnum) are performed for each outputr. Therefore, we have a separate measure of
ensemble variance per output.
Results
/five.pnum./three.pnum/one.pnumThree waves of HM were performed, a/f_ter which HM was unable to reduce the non-implausible space any fur-
ther, so the procedure was stopped. In the first wave, the non-implausible space was reduced from /one.pnum/six.pnum scenarios
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 17

to seven. The second wave further reduced the plausible space to four scenarios. Table /two.pnum shows the four mod-
els that were found to be plausible and which factors were switched on. These results match those in Ge et al.
(/two.pnum/zero.pnum/one.pnum/eight.pnum), who use POM to select plausible models. The common feature of these four models is that succession
and leisure are always turned on, whereas the remaining two factors (diversification and industrialisation) are
mixed.
Model ID Succ. Leisure Divers. Indust.
/one.pnum/three.pnum x x x
/one.pnum/four.pnum x x
/one.pnum/five.pnum x x x x
/one.pnum/six.pnum x x x
Table /two.pnum: The plausible farming models indicating their ID numbers and which factors are switched on (where x
is present).
/five.pnum./three.pnum/two.pnumTable /three.pnum shows the ensemble variances (Ve) and model discrepancies (Vm) in each wave. There is little stochas-
ticity in the model as shown by the relatively small ensemble variances, whereas there is noticeable discrepancy
between the model result and empirical data. Therefore ensemble variance has little eﬀect on the implausibility
score of each model, whilst model discrepancy has a strong eﬀect.
Table /three.pnum: The measured ensemble variance (Ve) and model discrepancy (Vm) at each wave of HM.
small medium large
wave /one.pnumVs /zero.pnum./zero.pnum/two.pnum/eight.pnum /zero.pnum./zero.pnum/three.pnum/five.pnum /zero.pnum./zero.pnum/two.pnum/five.pnum
Vm /seven.pnum./five.pnum/six.pnum/eight.pnum /five.pnum./three.pnum/three.pnum/five.pnum /one.pnum/seven.pnum./five.pnum/three.pnum/nine.pnum
wave /two.pnumVs /zero.pnum./zero.pnum/three.pnum/seven.pnum /zero.pnum./zero.pnum/four.pnum/six.pnum /zero.pnum./zero.pnum/two.pnum/nine.pnum
Vm /four.pnum./four.pnum/nine.pnum/three.pnum /four.pnum./one.pnum/one.pnum/five.pnum /seven.pnum./one.pnum/eight.pnum/two.pnum
wave /three.pnumVs /zero.pnum./zero.pnum/zero.pnum/four.pnum /zero.pnum./zero.pnum/zero.pnum/three.pnum /zero.pnum./zero.pnum/zero.pnum/seven.pnum
Vm /one.pnum./eight.pnum/zero.pnum/five.pnum /two.pnum./two.pnum/two.pnum/nine.pnum /five.pnum./five.pnum/five.pnum/one.pnum
/five.pnum./three.pnum/three.pnumHM has helped narrow down our list of plausible models from /one.pnum/six.pnum to four. This reduction of the parameter space
was achieved quickly (with /one.pnum/six.pnum/zero.pnum/zero.pnum model-runs) compared to the number of runs that would be required with
alternative calibration methods. The result also matches that found using POM (Ge et al. /two.pnum/zero.pnum/one.pnum/eight.pnum). However, HM
does not provide the probability that these four models can accurately match the empirical data. Instead, each
model is considered equally plausible. To gain insight into the probabilities, we use the rejection sampling
method of ABC.
/five.pnum./three.pnum/four.pnumWe initially setϵ to be the sum of the uncertainties found in the final wave of HM, as given in Table /three.pnum. We ran
each of the four models /one.pnum/zero.pnum/zero.pnum times, resulting in /five.pnum/three.pnum runs of model /one.pnum/three.pnum accepted, and no runs of the remaining
three models. Increasing this threshold by 0.95, however, resulted in most runs being accepted for models /one.pnum/three.pnum
and /one.pnum/five.pnum, and less than a quarter of the runs accepted for models /one.pnum/four.pnum and /one.pnum/six.pnum (see Figure /one.pnum/one.pnum). If the threshold is any
lower, than no runs for /one.pnum/four.pnum or /one.pnum/six.pnum are accepted, but over /nine.pnum/zero.pnum are accepted for /one.pnum/three.pnum and /one.pnum/five.pnum. These results suggest that
models /one.pnum/three.pnum and /one.pnum/five.pnum have the best probability of successfully simulating changes in the size of Scottish cattle farms
over time. Both of these models include industrialisation (as well as succession and leisure) as part of the farm
holder’s decision making. Models /one.pnum/four.pnum and /one.pnum/six.pnum, which are less likely to match the empirical data, do not include
industrialisation.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 18

Figure /one.pnum/one.pnum: Percentage of runs that produced an error smaller than the threshold for each output across models
/one.pnum/three.pnum-/one.pnum/six.pnum, where the threshold was set as the sum of the uncertainties +1.5
/five.pnum./three.pnum/five.pnumThrough ABC rejection sampling, we have found the best models that fit the empirical data and have learnt the
relative importance of each of the four factors considered. This was achieved through measuring the uncer-
tainties associated with the model and using those uncertainties to help choose appropriate thresholds for the
rejection sampling procedure.
Discussion
/six.pnum./one.pnumWe used two models to demonstrate the utility of the proposed framework. First, we use the territorial birds
model to compare our proposed approach against existing approaches. Thiele et al. (/two.pnum/zero.pnum/one.pnum/four.pnum) demonstrate a range
of calibration methods on the model, including random sampling, simulated annealing and ABC. We showed
that by performing HM before ABC, we can obtain equivalent results to using ABC alone using considerably
fewer runs of the model, thus saving on computational time. We can also obtain an accurate prior with HM
alone, which is useful for cases where performing ABC a/f_terwards is computationally infeasible. This is achieved
through identifying the uncertainties of the model.
/six.pnum./two.pnumWe also demonstrate that HM provides more information than point-estimation calibration methods, as it pro-
vides a region of parameters that perform well whilst also accounting for uncertainties in the model and data.
While this required more runs of the model than a point-estimation method, the information gained is valuable.
/six.pnum./three.pnumSecond, for the farming example (the RISC model), HM helped to rule out the implausible models. Specifically,
models without leisure and succession are not chosen, which is consistent with model selection using POM (Ge
et al. /two.pnum/zero.pnum/one.pnum/eight.pnum). Our approach enhances our understanding of the role of diﬀerent processes that co-exist in the
Scottish dairy farms. We have found that the lack of succession (which explains the increasing number of small
farms) and leisure (which explains the existence of non-profitable small farms) are the primary driving forces
behind the polarisation of Scottish dairy farms.
/six.pnum./four.pnumIn addition to HM, ABC further distinguishes models with industrialisation (employing a professional manager
to help expand a farm) as having a higher probability of matching the empirical data than those without. This
indicates that although industrialisation may not be the primary driving force of the trend of polarisation, it is
likely that it does play a role. This role may explain the increasing number of large farms. Without considering
industrialisation, the model fails to capture the growth of large farms. This finding is new, and was not picked
up by POM previously, or by HM alone. The reason is that both POM and HM are categorical, so they accept
models both with and without industrialisation elements, as they are all plausible. ABC, however, estimates
that models with industrialisation have a higher probability of matching the data than those without. This new
insight is a direct consequence of combining HM with ABC to calibrate an ABM.
/six.pnum./five.pnumIf a point-estimation method of calibration was used on the RISC model, we would only discover a single best
fitting model and would have not discovered that multiple models provide a good fit, which has lead to a better
understanding of the factors that aﬀect farmers’ decision making. The advantage of using ABC over POM is that
we are able to find the probabilities that these factors aﬀect decision making. Furthermore, by using HM before
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 19

ABC we were able to discover this with significantly fewer runs than would have been required with ABC alone
(because the sample space was narrowed to a more accurate region by HM), thereby saving computational time.
Conclusions
/seven.pnum./one.pnumDesigning and calibrating ABMs is a challenge due to uncertainties around the parameters, model structure and
stochasticity of such models. We have illustrated a process of calibrating an ABM’s structure and parameters
that quantifies these uncertainties through the combined use of HM and ABC. The code and results used in this
paper are all available online at https://github.com/Urban-Analytics/uncertainty.
/seven.pnum./two.pnumWe show that HM can be used to eﬀiciently reduce parameter space uncertainties; moreover, by quantifying
the model uncertainties it is only necessary to test each chosen parameter once. Following this, ABC provides a
more detailed exploration of the remaining parameter space, quantifying uncertainties in terms of a probability
distribution over non-implausible values.
/seven.pnum./three.pnumWe demonstrate this process with a toy example (Sugarscape) and two models of real-world processes, which
simulate the movement of territorial birds and the changing sizes of cattle farms in Scotland. In the territorial
birds model, we demonstrate that our approach is more informative than point-estimation calibration methods,
and more eﬀicient than Bayesian calibration methods alone without HM. We show that the number of model-
runs required for calibration is approximately halved if HM is used before ABC, compared to using ABC alone.
While this is shown with a simple model and simple ABC method, we believe that using HM will be beneficial
with more complex models even when more eﬀicient methods of ABC (e.g., sequential Monte Carlo) are used. In
the farming model, we show that HM was able to test competing sociological theories and removed all models
with a structure that was expected to be implausible based on an alternative POM approach (Ge et al. /two.pnum/zero.pnum/one.pnum/eight.pnum).
We then show that ABC provides insights into the factors that are important in Scottish cattle farmers when
deciding to change the size of their farm.
/seven.pnum./four.pnumAs the number of parameters in a model increases, the resources required to calibrate the model grows to be-
come prohibitive. We have suggested using HM to quickly find a narrow area of the search space, which can
then be explored in more detail with a rigorous approach, such as ABC. For a particularly large parameter space
or computational demanding model, one could use the non-implausible space found by HM to build a surro-
gate model. This simpler surrogate may be used in place of the real model to carry out ABC with more feasible
resources (Lamperti et al. /two.pnum/zero.pnum/one.pnum/eight.pnum).
/seven.pnum./five.pnumIn future work, we will explore our proposed approach further using new results generated with the RISC model.
We will create true data generated using the best fitting parameters found in this paper and investigate if our
method still finds the correct parameters to be the most likely sets to fit ourtrue data.
/seven.pnum./six.pnumIf ABMs are to achieve their potential as a go to tool for policymakers and academics, robust calibration and
uncertainty quantification handling methods need to be developed. Using the proposed process, calibration of
ABMs can be carried out eﬀiciently whilst taking into account all uncertainties associated with the model and
the real-world process.
Acknowledgements
This project has received funding from the European Research Council (ERC) under the European Union’s Hori-
zon /two.pnum/zero.pnum/two.pnum/zero.pnum research and innovation programme (grant agreement No. /seven.pnum/five.pnum/seven.pnum/four.pnum/five.pnum/five.pnum) and was supported by The Alan
Turing Institute.
AH was also supported by grants from UKPRP (MR/S/zero.pnum/three.pnum/seven.pnum/five.pnum/seven.pnum/eight.pnum//two.pnum), Medical Research Council (MC_UU_/zero.pnum/zero.pnum/zero.pnum/two.pnum/two.pnum//five.pnum)
and Scottish Government Chief Scientist Oﬀice (SPHSU/two.pnum/zero.pnum).
We also gratefully acknowledge the eﬀort made by the reviewers to help improve this manuscript.
Appendix: Notation
See Table /four.pnum for a list of mathematical notation used in the paper.
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 20

Term Meaning
R total observations/outputs
zr the rth observation
f r(x) the rth model output
f rj (x) the rth of the jth (RISC example)
d(zr, f r(x) error measure between the rth model output and observation
N total parameters sampled
xn the nth parameter set
vr
o observation variance of the rth observation
vr
s ensemble variance of the rth output
vr
m model discrepancy of the rth output
I r(c) implausibility measure of the rth output
c implausibility threshold
S total runs in an ensemble
Table /four.pnum: Mathematical notations used throughout the paper and their meaning.
Notes
/one.pnumNote that in three of the /nine.pnum/one.pnum tests, although the plausible range for survival probability contains the true
value, if our precision was higher (to /four.pnum d.p. instead of /three.pnum d.p.) these cases would have been rejected
References
Abdulkareem, S., Mustafa, Y., Augustijn, E.-W. & Filatova, T . (/two.pnum/zero.pnum/one.pnum/nine.pnum). Bayesian networks for spatial learning: A
workflow on using limited survey data for intelligent learning in spatial agent-based models.GeoInformatica,
/two.pnum/three.pnum(/two.pnum), /two.pnum/four.pnum/three.pnum–/two.pnum/six.pnum/eight.pnum
Andrianakis, I., Vernon, I. R., McCreesh, N., McKinley, T . J., Oakley, J. E., Nsubuga, R. N., Goldstein, M. & White,
R. G. (/two.pnum/zero.pnum/one.pnum/five.pnum). Bayesian history matching of complex infectious disease models using emulation: A tutorial and
a case study on HIV in Uganda. PLoS Computational Biology, /one.pnum/one.pnum(/one.pnum), e/one.pnum/zero.pnum/zero.pnum/three.pnum/nine.pnum/six.pnum/eight.pnum
Arendt, P . D., Apley, D. W. & Chen, W. (/two.pnum/zero.pnum/one.pnum/two.pnum). Quantification of model uncertainty: Calibration, model discrep-
ancy, and identifiability. Journal of Mechanical Design, /one.pnum/three.pnum/four.pnum, /one.pnum/zero.pnum/zero.pnum/nine.pnum/zero.pnum/eight.pnum
Beaumont, M. A., Zhang, W. & Balding, D. J. (/two.pnum/zero.pnum/zero.pnum/two.pnum). Approximate Bayesian computation in population genetics.
Genetics, /one.pnum/six.pnum/two.pnum(/four.pnum), /two.pnum/zero.pnum/two.pnum/five.pnum–/two.pnum/zero.pnum/three.pnum/five.pnum
Cooke, R. M. & Goossens, L. L. (/two.pnum/zero.pnum/zero.pnum/eight.pnum). TU Del/f_t expert judgment data base.Reliability Engineering & System
Safety, /nine.pnum/three.pnum(/five.pnum), /six.pnum/five.pnum/seven.pnum–/six.pnum/seven.pnum/four.pnum
Craig, P . S., Goldstein, M., Seheult, A. H. & Smith, J. A. (/one.pnum/nine.pnum/nine.pnum/seven.pnum). Pressure matching for hydrocarbon reservoirs: A
case study in the use of Bayes linear strategies for large computer experiments. In C. Gatsonis, J. S. Hodges,
R. E. Kass, R. McCulloch, P . Rossi & N. D. Singpurwalla (Eds.), Case Studies in Bayesian Statistics , vol. /three.pnum, (pp.
/three.pnum/seven.pnum–/nine.pnum/three.pnum). Berlin Heidelberg: Springer
Crols, T . & Malleson, N. (/two.pnum/zero.pnum/one.pnum/nine.pnum). Quantifying the ambient population using hourly population footfall data and
an agent-based model of daily mobility. GeoInformatica, /two.pnum/three.pnum(/two.pnum), /two.pnum/zero.pnum/one.pnum–/two.pnum/two.pnum/zero.pnum
Crooks, A., Castle, C. & Batty, M. (/two.pnum/zero.pnum/zero.pnum/eight.pnum). Key challenges in agent-based modelling for geo-spatial simulation.
Computers, Environment and Urban Systems, /three.pnum/two.pnum(/six.pnum), /four.pnum/one.pnum/seven.pnum–/four.pnum/three.pnum/zero.pnum
Csilléry, K., Blum, M. G. B., Gaggiotti, O. E. & François, O. (/two.pnum/zero.pnum/one.pnum/zero.pnum). Approximate Bayesian Computation (ABC) in
practice. Trends in Ecology & Evolution, /two.pnum/five.pnum(/seven.pnum), /four.pnum/one.pnum/zero.pnum–/four.pnum/one.pnum/eight.pnum
Daly, A. C., Cooper, J., Gavaghan, D. J. & Holmes, C. (/two.pnum/zero.pnum/one.pnum/seven.pnum). Comparing two sequential Monte Carlo samplers
for exact and approximate Bayesian inference on biological models. Journal of The Royal Society Interface,
/one.pnum/four.pnum(/one.pnum/three.pnum/four.pnum), /two.pnum/zero.pnum/one.pnum/seven.pnum/zero.pnum/three.pnum/four.pnum/zero.pnum
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 21

Del Moral, P ., Doucet, A. & Jasra, A. (/two.pnum/zero.pnum/one.pnum/two.pnum). An adaptive sequential Monte Carlo method for Approximate Bayesian
Computation. Statistics and Computing, /two.pnum/two.pnum(/five.pnum), /one.pnum/zero.pnum/zero.pnum/nine.pnum–/one.pnum/zero.pnum/two.pnum/zero.pnum
Epstein, J. M. & Axtell, R. (/one.pnum/nine.pnum/nine.pnum/six.pnum).Growing Artificial Societies: Social Science from the Bottom Up. Washington, DC:
Brookings Institution Press
Fearnhead, P . & Künsch, H. R. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Particle filters and data assimilation.Annual Review of Statistics and Its
Application, /five.pnum(/one.pnum), /four.pnum/two.pnum/one.pnum–/four.pnum/four.pnum/nine.pnum
Filatova, T ., Verburg, P . H., Parker, D. C. & Stannard, C. A. (/two.pnum/zero.pnum/one.pnum/three.pnum). Spatial agent-based models for socio-ecological
systems: Challenges and prospects. Environmental Modelling & So/f_tware, /four.pnum/five.pnum, /one.pnum–/seven.pnum
Ge, J., Polhill, J. G., Matthews, K. B., Miller, D. G. & Spencer, M. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Not one Brexit: How local context and
social processes influence policy analysis. PloS ONE, /one.pnum/three.pnum(/one.pnum/two.pnum), e/zero.pnum/two.pnum/zero.pnum/eight.pnum/four.pnum/five.pnum/one.pnum
Grazzini, J., Richiardi, M. G. & Tsionas, M. (/two.pnum/zero.pnum/one.pnum/seven.pnum). Bayesian estimation of agent-based models.Journal of Eco-
nomic Dynamics and Control, /seven.pnum/seven.pnum, /two.pnum/six.pnum–/four.pnum/seven.pnum
Grimm, V., Revilla, E., Berger, U., Jeltsch, F., Mooij, W. M., Railsback, S. F., Thulke, H.-H., Weiner, J., Wiegand, T . &
DeAngelis, D. L. (/two.pnum/zero.pnum/zero.pnum/five.pnum). Pattern-oriented modeling of agent-based complex systems: Lessons from ecology.
Science, /three.pnum/one.pnum/zero.pnum(/five.pnum/seven.pnum/five.pnum/zero.pnum), /nine.pnum/eight.pnum/seven.pnum–/nine.pnum/nine.pnum/one.pnum
Hassan, S., Arroyo, J., Galán, J., Antunes, L. & Pavón, J. (/two.pnum/zero.pnum/one.pnum/three.pnum). Asking the oracle: Introducing forecasting prin-
ciples into agent-based modelling. Journal of Artificial Societies and Social Simulation, /one.pnum/six.pnum(/three.pnum)
Heppenstall, A., Crooks, A., Malleson, N., Manley, E., Ge, J. & Batty, M. (/two.pnum/zero.pnum/two.pnum/zero.pnum). Future developments in geograph-
ical agent-based models: Challenges and opportunities. Geographical Analysis, /five.pnum/three.pnum(/one.pnum), /seven.pnum/six.pnum–/nine.pnum/one.pnum
Heppenstall, A., Evans, A. & Birkin, M. (/two.pnum/zero.pnum/zero.pnum/seven.pnum). Genetic algorithm optimisation of an agent-based model for
simulating a retail market. Environment and Planning B: Planning and Design, /three.pnum/four.pnum(/six.pnum), /one.pnum/zero.pnum/five.pnum/one.pnum–/one.pnum/zero.pnum/seven.pnum/zero.pnum
Huth, A. & Wissel, C. (/one.pnum/nine.pnum/nine.pnum/four.pnum). The simulation of fish schools in comparison with experimental data.Ecological
Modelling, /seven.pnum/five.pnum, /one.pnum/three.pnum/five.pnum–/one.pnum/four.pnum/six.pnum
Kazil, J., Masad, D. & Crooks, A. (/two.pnum/zero.pnum/two.pnum/zero.pnum). Utilizing python for agent-based modeling: The Mesa framework. In
R. Thomson, H. Bisgin, C. Dancy, A. Hyder & M. Hussain (Eds.), Social, Cultural, and Behavioral Modeling, (pp.
/three.pnum/zero.pnum/eight.pnum–/three.pnum/one.pnum/seven.pnum). Cham: Springer International Publishing
Kennedy, M. C. & O’Hagan, A. (/two.pnum/zero.pnum/zero.pnum/one.pnum). Bayesian calibration of computer models.Journal of the Royal Statistical
Society: Series B (Statistical Methodology), /six.pnum/three.pnum(/three.pnum), /four.pnum/two.pnum/five.pnum–/four.pnum/six.pnum/four.pnum
Lamperti, F., Roventini, A. & Sani, A. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Agent-based model calibration using machine learning surrogates.
Journal of Economic Dynamics and Control, /nine.pnum/zero.pnum, /three.pnum/six.pnum/six.pnum–/three.pnum/eight.pnum/nine.pnum
Lei, C. L., Ghosh, S., Whittaker, D. G., Aboelkassem, Y., Beattie, K. A., Cantwell, C. D., Delhaas, T ., Houston, C.,
Novaes, G. M., Panfilov, A. V., Pathmanathan, P ., Riabiz, M., dos Santos, R. W., Walmsley, J., Worden, K., Mirams,
G. R. & Wilkinson, R. D. (/two.pnum/zero.pnum/two.pnum/zero.pnum). Considering discrepancy when calibrating a mechanistic electrophysiology
model. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences ,
/three.pnum/seven.pnum/eight.pnum(/two.pnum/one.pnum/seven.pnum/three.pnum), /two.pnum/zero.pnum/one.pnum/nine.pnum/zero.pnum/three.pnum/four.pnum/nine.pnum
Lenormand, M., Jabot, F. & Deﬀuant, G. (/two.pnum/zero.pnum/one.pnum/three.pnum). Adaptive approximate Bayesian computation for complex mod-
els. Computational Statistics, /two.pnum/eight.pnum(/six.pnum), /two.pnum/seven.pnum/seven.pnum/seven.pnum–/two.pnum/seven.pnum/nine.pnum/six.pnum
Li, T ., Cheng, Z. & Zhang, L. (/two.pnum/zero.pnum/one.pnum/seven.pnum). Developing a novel parameter estimation method for agent-based model
in immune system simulation under the framework of history matching: A case study on Influenza A virus
infection. International Journal of Molecular Sciences, /one.pnum/eight.pnum(/one.pnum/two.pnum), /two.pnum/five.pnum/nine.pnum/two.pnum
Manson, S., An, L., Clarke, K. C., Heppenstall, A., Koch, J., Krzyzanowski, B., Morgan, F., O’Sullivan, D., Runck,
B. C., Shook, E. & Tesfatsion, L. (/two.pnum/zero.pnum/two.pnum/zero.pnum). Methodological issues of spatial agent-based models.Journal of
Artificial Societies and Social Simulation, /two.pnum/three.pnum(/one.pnum), /three.pnum
Marin, J.-M., Pudlo, P ., Robert, C. P . & Ryder, R. J. (/two.pnum/zero.pnum/one.pnum/two.pnum). Approximate Bayesian Computational methods.Statis-
tics and Computing, /two.pnum/two.pnum(/six.pnum), /one.pnum/one.pnum/six.pnum/seven.pnum–/one.pnum/one.pnum/eight.pnum/zero.pnum
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 22

Moya, I., Chica, M. & Cordón, O. (/two.pnum/zero.pnum/two.pnum/one.pnum). Evolutionary multiobjective optimization for automatic agent-based
model calibration: A comparative study. IEEE Access, /nine.pnum, /five.pnum/five.pnum/two.pnum/eight.pnum/four.pnum–/five.pnum/five.pnum/two.pnum/nine.pnum/nine.pnum
Neri, F. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Combining machine learning and agent-based modeling for gold price prediction. Italian Work-
shop on Artificial Life and Evolutionary Computation
O’Hagan, A., Buck, C. E. & Daneshkhah, A. (/two.pnum/zero.pnum/zero.pnum/six.pnum).Uncertain Judgements: Eliciting Experts’ Probabilities. Hobo-
ken, NJ: John Wiley & Sons
Papadelis, S. & Flamos, A. (/two.pnum/zero.pnum/one.pnum/nine.pnum). An application of calibration and uncertainty quantification techniques for
agent-based models. In H. Doukas, A. Flamos & J. Lieu (Eds.),Understanding Risks and Uncertainties in Energy
and Climate Policy: Multidisciplinary Methods and Tools for a Low Carbon Society, (pp. /seven.pnum/nine.pnum–/nine.pnum/five.pnum). Cham: Springer
International Publishing
Pietzsch, B., Fiedler, S., Mertens, K. G., Richter, M., Scherer, C., Widyastuti, K., Wimmler, M.-C., Zakharova, L. &
Berger, U. (/two.pnum/zero.pnum/two.pnum/zero.pnum). Metamodels for evaluating, calibrating and applying agent-based models: A review.Journal
of Artificial Societies and Social Simulation, /two.pnum/three.pnum(/two.pnum), /nine.pnum
Polhill, J., Ge, J., Hare, M., Matthews, K., Gimona, A., Salt, D. & Yeluripati, J. (/two.pnum/zero.pnum/one.pnum/nine.pnum). Crossing the chasm: A ‘tube-
map’ for agent-based social simulation of policy scenarios in spatially-distributed systems. GeoInformatica,
/two.pnum/three.pnum(/two.pnum), /one.pnum/six.pnum/nine.pnum–/one.pnum/nine.pnum/nine.pnum
Pukelsheim, F. (/one.pnum/nine.pnum/nine.pnum/four.pnum). The three sigma rule.The American Statistician, /four.pnum/eight.pnum(/two.pnum), /eight.pnum/eight.pnum–/nine.pnum/one.pnum
Purshouse, R. C., Ally, A. K., Brennan, A., Moyo, D. & Norman, P . (/two.pnum/zero.pnum/one.pnum/four.pnum). Evolutionary parameter estimation for
a theory of planned behaviour microsimulation of alcohol consumption dynamics in an English birth cohort
/two.pnum/zero.pnum/zero.pnum/three.pnum to /two.pnum/zero.pnum/one.pnum/zero.pnum. Proceedings of the /two.pnum/zero.pnum/one.pnum/four.pnum Annual Conference on Genetic and Evolutionary Computation, New
York, NY, USA
Railsback, S. F. & Grimm, V. (/two.pnum/zero.pnum/one.pnum/nine.pnum).Agent-Based and Individual-Based Modeling: A Practical Introduction. Prince-
ton, NJ: Princeton University Press
Rouchier, J., Bousquet, F., Requier-Desjardins, M. & Antona, M. (/two.pnum/zero.pnum/zero.pnum/one.pnum). A multi-agent model for describing tran-
shumance in North Cameroon: Comparison of diﬀerent rationality to develop a routine.Journal of Economic
Dynamics and Control, /two.pnum/five.pnum(/three.pnum), /five.pnum/two.pnum/seven.pnum–/five.pnum/five.pnum/nine.pnum
Smith, R. (/two.pnum/zero.pnum/one.pnum/three.pnum).Uncertainty Quantification: Theory, Implementation, and Applications. Philadelphia, PA: Society
for Industrial and Applied Mathematics
Stavrakas, V., Papadelis, S. & Flamos, A. (/two.pnum/zero.pnum/one.pnum/nine.pnum). An agent-based model to simulate technology adoption quan-
tifying behavioural uncertainty of consumers. Applied Energy, /two.pnum/five.pnum/five.pnum(/one.pnum), /one.pnum/one.pnum/three.pnum/seven.pnum/nine.pnum/five.pnum
Strong, M., Oakley, J. E. & Chilcott, J. (/two.pnum/zero.pnum/one.pnum/two.pnum). Managing structural uncertainty in health economic decision mod-
els: A discrepancy approach. Journal of the Royal Statistical Society: Series C (Applied Statistics), /six.pnum/one.pnum(/one.pnum), /two.pnum/five.pnum–/four.pnum/five.pnum
Sturley, C., Newing, A. & Heppenstall, A. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Evaluating the potential of agent-based modelling to capture
consumer grocery retail store choice behaviours. The International Review of Retail, Distribution and Con-
sumer Research, /two.pnum/eight.pnum(/one.pnum), /two.pnum/seven.pnum–/four.pnum/six.pnum
Sunnåker, M., Busetto, A. G., Numminen, E., Corander, J., Foll, M. & Dessimoz, C. (/two.pnum/zero.pnum/one.pnum/three.pnum). Approximate bayesian
computation. PLoS Computational Biology, /nine.pnum(/one.pnum), e/one.pnum/zero.pnum/zero.pnum/two.pnum/eight.pnum/zero.pnum/three.pnum
ten Broeke, G., van Voorn, G. & Ligtenberg, A. (/two.pnum/zero.pnum/one.pnum/six.pnum). Which sensitivity analysis method should I use for my
agent-based model? Journal of Artificial Societies and Social Simulation, /one.pnum/nine.pnum(/one.pnum), /five.pnum
Thiele, J. C., Kurth, W. & Grimm, V. (/two.pnum/zero.pnum/one.pnum/four.pnum). Facilitating parameter estimation and sensitivity analysis of agent-
based models: A cookbook using NetLogo and ’R’. Journal of Artificial Societies and Social Simulation, /one.pnum/seven.pnum(/three.pnum),
/one.pnum/one.pnum
Toni, T ., Welch, D., Strelkowa, N., Ipsen, A. & Stumpf, M. P . (/two.pnum/zero.pnum/zero.pnum/nine.pnum). Approximate Bayesian Computation scheme
for parameter inference and model selection in dynamical systems. Journal of the Royal Society Interface ,
/six.pnum(/three.pnum/one.pnum), /one.pnum/eight.pnum/seven.pnum–/two.pnum/zero.pnum/two.pnum
Turner, B. M. & Van Zandt, T . (/two.pnum/zero.pnum/one.pnum/two.pnum). A tutorial on Approximate Bayesian Computation.Journal of Mathematical
Psychology, /five.pnum/six.pnum(/two.pnum), /six.pnum/nine.pnum–/eight.pnum/five.pnum
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---

## Page 23

van der Vaart, E., Beaumont, M. A., Johnston, A. S. & Sibly, R. M. (/two.pnum/zero.pnum/one.pnum/five.pnum). Calibration and evaluation of individual-
based models using Approximate Bayesian Computation. Ecological Modelling, /three.pnum/one.pnum/two.pnum, /one.pnum/eight.pnum/two.pnum–/one.pnum/nine.pnum/zero.pnum
Vernon, I., Goldstein, M., Bower, R. G. et al. (/two.pnum/zero.pnum/one.pnum/zero.pnum). Galaxy formation: A bayesian uncertainty analysis.Bayesian
Analysis, /five.pnum(/four.pnum), /six.pnum/one.pnum/nine.pnum–/six.pnum/six.pnum/nine.pnum
Waldrop, M. M. (/two.pnum/zero.pnum/one.pnum/eight.pnum). Free agents.Science, /three.pnum/six.pnum/zero.pnum(/six.pnum/three.pnum/eight.pnum/five.pnum), /one.pnum/four.pnum/four.pnum–/one.pnum/four.pnum/seven.pnum
Weiss, C. R. (/one.pnum/nine.pnum/nine.pnum/nine.pnum). Farm growth and survival: Econometric evidence for individual farms in Upper Austria.
American Journal of Agricultural Economics, /eight.pnum/one.pnum(/one.pnum), /one.pnum/zero.pnum/three.pnum–/one.pnum/one.pnum/six.pnum
Windrum, P ., Fagiolo, G. & Moneta, A. (/two.pnum/zero.pnum/zero.pnum/seven.pnum). Empirical validation of agent-based models: Alternatives and
prospects. Journal of Artificial Societies and Social Simulation, /one.pnum/zero.pnum(/two.pnum), /eight.pnum
Zhang, H., Vorobeychik, Y., Letchford, J. & Lakkaraju, K. (/two.pnum/zero.pnum/one.pnum/six.pnum). Data-driven agent-based modeling, with appli-
cation to roo/f_top solar adoption.Autonomous Agents and Multi-Agent Systems, /three.pnum/zero.pnum(/six.pnum), /one.pnum/zero.pnum/two.pnum/three.pnum–/one.pnum/zero.pnum/four.pnum/nine.pnum
Zoellner, C., Jennings, R., Wiedmann, M. & Ivanek, R. (/two.pnum/zero.pnum/one.pnum/nine.pnum). EnABLe: An agent-based model to understand
Listeria dynamics in food processing facilities. Scientific reports, /nine.pnum(/one.pnum), /one.pnum–/one.pnum/four.pnum
JASSS, /two.pnum/five.pnum(/two.pnum) /one.pnum, /two.pnum/zero.pnum/two.pnum/two.pnum http://jasss.soc.surrey.ac.uk//two.pnum/five.pnum//two.pnum//one.pnum.htmlDoi: /one.pnum/zero.pnum./one.pnum/eight.pnum/five.pnum/six.pnum/four.pnum/jasss./four.pnum/seven.pnum/nine.pnum/one.pnum

---
