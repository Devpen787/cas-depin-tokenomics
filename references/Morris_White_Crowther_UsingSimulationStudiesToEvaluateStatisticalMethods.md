# Morris_White_Crowther_UsingSimulationStudiesToEvaluateStatisticalMethods.pdf

## Page 1

Received <day> <Month>, <year>; Revised <day> <Month>, <year>; Accepted <day> <Month>, <year>
DOI: xxx/xxxx
TUTORIAL IN BIOSTATISTICS
Using simulation studies to evaluate statistical methods
Tim P Morris*1 | Ian R White1 | Michael J Crowther2
1London Hub for Trials Methodology
Research, MRC Clinical Trials Unit at
UCL, London, UK
2Biostatistics Research Group, Department
of Health Sciences, University of Leicester,
Leicester, UK
Correspondence
*Tim P Morris, MRC Clinical Trials Unit at
UCL. Email: tim.morris@ucl.ac.uk
Present Address
90 High Holborn, London WC1V 6LJ, UK
Abstract
Simulationstudiesarecomputerexperimentswhichinvolvecreatingdatabypseudo-
randomsampling.Thekeystrengthofsimulationstudiesistheabilitytounderstand
the behaviour of statistical methods because some ‘truth’ is known from the pro-
cess of generating the data. This allows us to consider properties of methods, such
as bias. While widely used, simulation studies are often poorly designed, analysed
and reported. This article outlines the rationale for using simulation studies and
oﬀers guidance for design, execution, analysis, reporting and presentation. In par-
ticular, we provide: a structured approach for planning and reporting simulation
studies;coherentterminologyforsimulationstudies;guidanceoncodingsimulation
studies; a critical discussion of key performance measures and their computation;
ideasonstructuringtabularandgraphicalpresentationofresults;andnewgraphical
presentations. With a view to describing current practice and identifying areas for
improvement,wereview100articlestakenfromVolume34of StatisticsinMedicine
which included at least one simulation study.
KEYWORDS:
Simulation studies; Monte Carlo; Experimental design; Reporting
1 INTRODUCTION
Simulation studies are computer experiments which involve creating data by pseudo-random sampling from known probability
distributions. They are an invaluable tool for statistical research, particularly for the evaluation of new methods and the com-
parison of competing methods. Simulation studies are much used in the pages ofStatistics in Medicine, but our experience is
thatmanystatisticianslackthenecessaryunderstandingtoexecuteasimulationstudywithconﬁdence.Properunderstandingof
simulation studies would enable such people to run simulation studies themselves and to critically appraise published simula-
tion studies. Issues with design and reporting, which we will demonstrate later, lead to uncritical use or appraisal of simulation
studies. In this context, better understanding of the rationale, design, execution, analysis and reporting of simulation studies is
necessary to improve what researchers can learn from them.
Simulation studies are used to obtain empirical results about the behaviour of statistical methods in certain scenarios, as
opposed to analytic results, which may cover many settings. It is not always possible to obtain analytic results, or may be
extremely diﬃcult. Simulation studies come into their own when methods make wrong assumptions or data are messy; that is,
they can assess the resilience of methods. This is not always possible with analytic results, which may assume that data arise
from a speciﬁc model.
arXiv:1712.03198v1  [stat.ME]  8 Dec 2017

---

## Page 2

2 TP Morris, IR White, MJ Crowther
Monte Carlo simulation has several uses that are not simulationstudies. It is used in any analysis with a stochastic element,
for example multiple imputation and Markov chain Monte Carlo methods. The remainder of this paper does not consider these
uses of Monte Carlo simulation, except where the properties of some such method are being evaluated by a simulation study.
There are many ways to use simulation studies in medical statistics. Some examples are:
◦ Where a new statistical method has been derived mathematically, to check algebra (and code), e.g. approximations, or to
provide reassurance that no large error has been made.
◦ Absoluteevaluationofaneworexistingstatisticalmethod.Oftenanewmethodischeckedusingsimulationtoensureitworks
in the scenarios it was designed for.
◦ Comparative evaluation of two or more statistical methods.
◦ Calculation of sample size / power, when designing a study under certain assumptions about the data-generating process(1).
Thisarticleisfocusedprimarilyontheevaluationofmethods,butmanyoftheprinciplesoutlinedareapplicablemoregenerally.
Simulations are typically motivated by frequentist theory and used to evaluate frequentist properties of methods (even if the
methods are Bayesian).
Simulation studies are empirical experiments, and statisticians – particularly those doing working in applications such as
clinical trials – should be familiar with good practice regarding design, analysis, presentation and reporting. It seems that as a
professionwefailtofollowthispracticeinourmethodologicalwork,aspreviouslylamentedbyHoaglin&Andrews(2),Hauck
& Anderson(3), Ripley(4), Burtonet al.(5), and Koehler, Brown & Haneuse(6). For example, few reports of simulation studies
acknowledge that Monte Carlo procedures will give diﬀerent results when based on a diﬀerent set of random numbers; failing
to report measures of uncertainty would be unacceptable in medical research. There are some wonderful books on simulation
methodsingeneral(4,7,8)andseveralexcellentarticlesencouragingrigourinspeciﬁcaspectsofsimulationstudies(forexample
(1, 2, 3, 6, 9, 10, 11, 12)) but no uniﬁed practical guidance on simulation studies.
This article outlines the rationale for using simulation studies and oﬀers practical guidance for design, execution, analysis,
reportingandpresentation.Namelywe:introduceastructuredapproachforplanningandreportingsimulationstudies;introduce
coherentterminologyforsimulationstudies;provideguidanceoncodingsimulationstudies;criticallydiscusskeyperformance
measures and their computation; make suggestions for structuring tabular and graphical presentation of results; and introduce
some new graphical presentations. This guidance is designed to enable practitioners to execute a simulation study for the ﬁrst
timeandalsocontainsmuchformoreexperiencepractitioners.Forreference,themainstepsinvolved,decisionstobemadeand
recommendations are summarised in table 1 .
The structure of this tutorial is as follows. We describe a review of a sample of the simulation studies reported inStatistics
in MedicineVolume 34 (section 2). In section 3 we outline a systematic approach to planning simulation studies, using the
‘ADMEP’ structure (which we deﬁne there). Section 4 gives generic guidance on coding simulation studies. In section 5, we
discuss the uses of various performance measures and their computation, stressing the importance of estimating and reporting
measures of Monte Carlo uncertainy. Section 6 outlines how to report simulation studies, again using theADMEP structure,
and oﬀers guidance on tabular and graphical presentation of results. Section 7 works through a simple simulation to illustrate
in practice the approaches we advocate. Section 8.1 considers some future directions, and section 8 oﬀers some concluding
remarks.Examplesaredrawnfromthereviewandfromtheauthors’areasofinterest(whichrelatemainlytomodellingsurvival
data, missing data, meta-analysis and randomised trial design).
2 SIMULATION IN PRACTICE: A REVIEW OFSTATISTICS IN MEDICINE, VOLUME 34
We conducted a review of practice in articles published in Volume 34 ofStatistics in Medicine(2015). This review recorded
information relevant to the ideas in this article. In this section we brieﬂy outline the review but do not give results. Instead,
results appear in the paper at relevant points.
We restricted attention toresearch articles, which is the type of article in which simulation studies are typically reported.
This excludes the article types:tutorial in biostatistics, commentary, book review, correction, letter to the editorand authors’
response. In total, this returned 264 research articles. Of these, 199 (75%) included at least one simulation study.

---

## Page 3

TP Morris, IR White, MJ Crowther 3
TABLE 1Key steps and decisions in the planning, coding, analysis and reporting of simulation studies
Section
Planning 3
⋅ Identify the aims, data-generating mechanisms, methods to evaluate, estimands or other ‘targets’,
and performance measures
3.2–3.6
Aims 3.2
⋅ Identifyspeciﬁcaimsofsimulationstudy,particularlyintermsofthe‘phase’(e.g.proof-of-concept)
Data-generating mechanisms 3.3
⋅ Inrelationtotheaims,decidewhethertouseresamplingorsimulationfromsomeparametricmodel
⋅ Forparametricsimulation,decidehowsimpleorcomplexthemodelshouldbeandwhetheritshould
be based on real data
⋅ Determine factors to vary and levels of factors to use 3.3
⋅ Decide whether factors should be varied fully factorially, partly factorially or one-at-a-time
Methods 3.4
⋅ Identify methods to be evaluated. For method comparison studies, make a careful review of the
literature to ensure inclusion of relevant methods.
Estimand / target of analysis 3.5
⋅ Deﬁne estimands and/or other targets of the simulation study, relating to the applied contexts for
which method is intended to be used.
Performance measures 3.6, 5.2
⋅ Listallperformancemeasurestobeestimated,justifyingtheirrelevancetoestimandsorothertargets.
⋅ For less-used performance measures, give explicit formulae for the avoidance of ambiguity. 5.2
⋅ Choose a value ofnsim which achieves acceptable MCSE for key performance measures. 5.4
Coding 4
⋅ Separate scripts used to analyse simulated datasets from scripts to analyse estimates datasets.
⋅ Start small and build up code, including plenty of checks.
⋅ Set the random number seed once per simulation repetition.
⋅ Store the random number states at the start of each repetition.
⋅ If running chunks of the simulation in parallel, use separate streams of random numbers (13).
Analysis 5
⋅ Conduct exploratory analysis of results, particularly graphical
⋅ Along with estimates of performance, compute Monte Carlo SE
Reporting 6
⋅ Structuregraphicalandtabularpresentationstoplaceperformancemeasuresforcompetingmethods
side-by-side.
⋅ Include estimates of simulation uncertainty.
⋅ Publish code to execute simulation study including user-written routines.
Inplanningthereview,weneededtoselectasamplesize.Mostofthequestionsofinterestinvolvedbinaryanswers.Forsuch
questions, to estimate proportions with maximum standard error of 0.05 (occurring when the proportion is 0.5), we randomly
selected 100 articles which involved a simulation study, before randomly assigning articles to a reviewer. This meant that TPM
reviewed 35 simulation studies, IRW reviewed34 and MJC reviewed 31. In case the reviewer was an author orco-author of the
article, the simulation study was swapped with another reviewer. TPM also reviewed ﬁve of the simulation studies allocated to
each of the other reviewers to check agreement on key information.

---

## Page 4

4 TP Morris, IR White, MJ Crowther
TABLE 2Description of notation
 An estimand (conceptually); also true value of the estimand
nobs Sample size of a simulated dataset
nsim Number of repetitions used; the simulation sample size
i = 1, …,nsim Indexes the repetitions of the simulation
̂i the estimate of from theith repetition
Var(̂i) the estimate of Var(̂)from theith repetition
Var(̂) is the empirical (long-run) variance of̂
 the nominal signiﬁcance level
pi the p-value returned by theith repetition
3 PLANNING SIMULATION STUDIES USING ADMEP
3.1 Notation
For clarity about the concepts that will follow, we introduce some notation in table 2 .
In the following sections, we outline theADMEP structured approach to planning simulation studies. This acronym comes
from:Aims, Data-generating mechanisms, Methods, Estimands, Performance measures.
3.2 Aims
In considering the aims of a simulation study it is instructive to ﬁrst consider desirable properties of an estimator of from a
frequentist perspective.
1. ̂ should be consistent: asn → ∞, ̂ → . It is also desirable that̂ be unbiased for in ﬁnite samples: E(̂) = . Some
estimators may be consistent but exhibit small-sample bias (logistic regression for example). Kahan reports a procedure
that appears to be unbiased but inconsistent(14).
2. The sample estimateVar(̂) should be a consistent estimate of the long-run variance of̂ (see for example (15)).
3. Conﬁdence intervals should have the property that at least100(1 −)% of intervals contain (see section 5.2).
4. It is desirable that Var̂() be as small as possible: that̂ be an eﬃcient estimator of.
There are other properties we may hope for, but these generally involve combinations of the above.
Theaimsofasimulationstudywilltypicallybesetoutinrelationtotheaboveproperties,dependingonwhatspeciﬁcallywe
wish to learn. A simulation study might primarily investigate: Large- or small-sample bias (e.g. White, 1997 (16); Precision,
particularly relative to other available methods (e.g. White and Thompson, 2005 (17)); Variance estimation (e.g. Hughes, 2014
(18)); or Robustness to misspeciﬁcation (e.g. Morris, 2014 (19)).
There is a distinction between simulation studies that oﬀer a proof-of-concept and those aiming to stretch or break methods.
Both are useful and important in statistical research. For example, one may be faced with two competing methods of analysis,
both of which are equally easy to implement. Even if the choice is unlikely to materially aﬀect the results, it may be useful to
have unrealistically extreme data-generating mechanisms to understand when and how methods break; see for example (19).
Alternatively, it may be of interest to compare methods where some or all have been shown to work in principle but the
methods under scrutiny deal with slightly diﬀerent problems. They may be put head-to-head in realistic scenarios. This could
be to investigate properties when one method is correct –How badly do others fail?– or when all are incorrect in some way –
Which is most robust?No method will be perfect and it is useful to understand how methods are likely to perform in the sort of
scenariosthatmightbeexpectedinpractice.However,suchanapproachposestoughquestionsintermsofgeneratingdata: Does
the data-generating mechanism favour certain methods over others? How can this be justiﬁed?One common justiﬁcation is by
referencetomotivatingdata.However,thiscarriesariskoffailingtoconvinceothersthatmethodsshouldbeusedmorewidely.

---

## Page 5

TP Morris, IR White, MJ Crowther 5
3.3 Data-generating mechanisms
We use the term ‘data-generating mechanism’ to denote how random numbers are used to produce a simulated dataset. This is
inpreferencetotheterm‘data-generating model’,whichimpliesparametricmodelsandsoisaspeciﬁcclassofdata-generating
mechanism. It is not the purpose of this article to explain how speciﬁc data should be generated. See Ripley (4) or Morgan (7)
for methods to simulate data from speciﬁc distributions.
Data may be generated by producing parametric draws from a known model (once or many times), or resampling with
replacement many times from a speciﬁc dataset where the model from which data are generated is unknown.
The choice of data-generating mechanism(s) will depend on the aims. As noted above, we might investigate a method in a
simple scenario, a realistic scenario, or a completely unrealistic scenario that is designed to stretch a method to breaking point.
It was noted in the introduction that simulation studies provide us with approximate results for speciﬁc scenarios. For this
reason,simulationstudieswillofteninvolvemorethanonedata-generatingmechanismtoensurecoverageofdiﬀerentscenarios.
For example, it is very common to vary the sample size of simulated datasets.
Muchcanbecontrolledinasimulationstudy,andsostatisticalprinciplesfordesigningexperimentscanandshouldbecalled
on. In particular, there is often more than one factor that will vary across speciﬁc data-generating mechanisms. Varying them
factorially is likely to be more informative than one-by-one as doing so permits exploration of interactions between factors.
There are however practical implications which might make this infeasible. The ﬁrst regards presentation of results (covered in
section 6) and the second computational time. If the issue is simply around presentation, it may be preferable to deﬁne a ‘base
case’ but perform a factorial simulation study anyway. If the results are consistent with no interaction, presentation can vary
factors away from the base case one-by-one.
Ifthemainissuewithexecutingafullyfactorialdesigniscomputationaltime,andthisisinadmissible,thenitmaybenecessary
for the simulation study to follow a non-factorial structure. Two checks for interaction are outlined below.
A ﬁrst pragmatic check may be to consider interactions only where main eﬀects exist. If performance seems acceptable and
doesnotvaryaccordingtofactorA,itwouldseemunlikelytohavechosenadata-generatingmechanismthathappenedtoexhibit
this property given that performance would have been poor for other choices of data-generating mechanism.
A second and more careful approach is based on making and checking predictions beyond the data-generating mechanisms
initially considered; an idea similar to external validation. Say we have two factors, A and B, where A∈ {1 , …, 8} and B ∈
{1, …, 5}in the data-generating mechanism. If the non-factorial portion of the design varies A from 1 to 8 holding B= 1, and
variesBfrom1to5holdingA = 1,theperformancemeasurescouldbe predictedforA = 8,B = 5 basedonthemarginaleﬀects
from the non-factorial simulation. Predictions may be purely qualitative (‘bias increases as A increases and as B increases so
whenweincreasebothtogetherwewouldexpectevenlargerbias’),orquantitative(asaresultofﬁttingamain-eﬀectsmodelto
existingresultstoproduceexplicitpredictionsatunexploredvaluesofAandB).Thesimulationstudycanthenbere-runforthe
singleDGM,sayA = 8,B = 5.Departuresfromthepredictedresultsimplyinteraction,witharesponsibilitytoexplorefurther.
Inourreview,97simulationstudiesusedsomeformofparametricmodeltogeneratedatawhilethreeuseresamplingmethods.
Of those which simulated from a parametric model, 27 based parameters on data, one based parameters partly on data, and
the remaining 69 on no data. Of the 97 simulation studies using a parametric data-generating model, 91 (94%) provided the
parameters used. One simulation study (20) explored analysis of meta-analysis data and drew the design factors from empirical
dataon14,886performedmeta-analysesfrom1,991CochraneReviews.ThetotalnumberofDGMspersimulationstudyranged
from 1 to6 × 1011; ﬁgure A1 (in the appendix) summarises aspects of the data-generating mechanisms.
3.4 Methods
The term ‘method’ is intended to be generic. It most often refers to a model for analysis, but might refer to a design or some
procedure (such as a decision rule). For example, (14) and (21) both evaluated procedures which involved choosing an analysis
based on the result of a preliminary test in the same data.

---

## Page 6

6 TP Morris, IR White, MJ Crowther
In some simulation studies there will be only one method with no comparators. In this case, selecting the method to be
evaluatedisverysimple.Whenweaimtocompareseveralmethods,theaimwillbetoidentifythebest.Itisthereforeimportant
to include serious contenders. There are two issues.
First: it is necessary to have knowledge of previous work in the area to understand which methods are and are not serious
contenders.Somemethodsmaybelegitimatelyexcludediftheyhavealreadybeenshowntobeﬂawed,anditmaybeunnecessary
toincludesuchmethodsiftheironlypurposeistorepeatpreviousresearchandbloattheresultsofthecurrentwork.Anexception
mightbe ifaﬂawed methodisused lotsinpractice (forexample lastobservation carriedforward withincomplete longitudinal
data, or the ‘3 + 3’ design for dose-escalation).
Second: code. New methods are sometimes published but not implemented in any software (for example (22) and (23)),
implemented poorly, or implemented in unfamiliar software. Although R and Stata tend to dominate for user-written methods,
it is not uncommon to see methods implemented in other packages. See section 4.3 for a discussion of this issue as it impinges
on simulation studies. Note that one important role of simulation is to verify that code is correct.
ThenumberofmethodsevaluatedinourreviewofVolume34rangedfrom1to33(seeﬁgureA2 ),reﬂectingthebroadrange
of simulation studies in terms of aims.
Non-convergencemaybeanissueforcertainmodels.Insuchasituation,thereisaconceptualissuewithdeﬁningthe‘method’.
A pure method evaluation would simply assess performance of the model when it converges. However, in practice an analyst
whose model does not convergence would then use some other model until one converges. Thus, evaluation of this procedure
maybeofinterestinsimulationstudies.Crowther,LookandRileyevaluatesuchaprocedure:ifamodelfailedtoconverge,they
applied a model with more quadrature points.(24) We commment further on this issue in section 5.2.
3.5 Estimands and other targets
Themajorityofsimulationstudiesevaluateorcomparemethodsforestimatingoneormorequantities,whichweterm estimands
and denote by. Usually an estimand is a parameter of the data generating model, but occasionally it is some other quantity.
For example, when ﬁtting regression models with parameter = (0 …c), the estimand may be a speciﬁc, a measure of
prognostic ability, the ﬁtted E(Y ), or something else. To choose a relevant estimand it is important to understand the aims of
analysis in practice.
Thechoiceofestimandisrarelymadeexplicitbutisimportant.Forexample,incase–controlstudieslogisticregressionisused
toestimateoddsratios.Theestimatedoddsratioforthismodelisasymptoticallyunbiased,buttheestimateofodds(theintercept)
isbiased.Thisbiasshouldnotconcernusbecausecase–controlstudiesarenotusedtoestimateodds(withoutknowledgeofthe
sampling fraction). Thus the estimand here should be the (log) odds ratio and not the intercept.
Identifyingwhetherdiﬀerentmethodstargetthesameestimandcanbesubtle.Forexample,inarandomisedtrialwithbinary
outcome, one might compare two logistic regression analyses, one unadjusted and one adjusted for a baseline covariate, where
the estimand is the log odds ratio for randomised group. In a simulation study, one would be likely to ﬁnd that the two methods
givediﬀerentmeanestimates,anditwouldbetemptingtoconcludethatatleastoneofthemethodsisbiased.However,thetwo
methods target diﬀerent estimands – that is, the true unadjusted and adjusted log odds ratios diﬀer.(25)
Onewaytotackletheproblemofmultipleestimandsistoensurethatbothmethodsestimatethesameestimand:inthelogistic
regressioncase,thiswouldinvolvepost-processingtheadjustedregressionresultstoestimatethe‘marginaladjustedoddsratio’
(26). This of course implies that the adjustmentvs. non adjustment is the method comparison we are interested in (it may not
be),andthattheconditionalestimandisanuisancepartofstandardadjustment.Analternativebutlesssatisfactorywaytotackle
theproblemistotargetthenullhypothesisthattheoddsratioequals1,becausethisspeciﬁcnullhypothesisisthesamewhether
the odds ratio is conditional or marginal.
Notallsimulationstudiesevaluateorcomparemethodswhichconcernanestimand.Othersimulationstudiesevaluatemethods
for testing a null hypothesis, for selecting a model, or for prediction. We refer to these astargetsof the simulation study. The
same statistical method could be evaluated against multiple targets. For example, the best method to select a regression model
to estimate the coeﬃcient of an exposure (targeting an estimand) may diﬀer from the best model for prediction of outcomes

---

## Page 7

TP Morris, IR White, MJ Crowther 7
TABLE 3Possible targets of a simulation study and relevant performance measures
Statistical task Target Examples of performance Example
measures
Analysis
Estimation Estimand Bias, mean-squared error,
coverage
Kuss compares a number of existing methods in
terms of bias, power and coverage (20)
Testing Null hypothesis Type I error rate, power Chaurasia and Harel compare new methods inn
terms of type I and II error rates (27)
Model selection Model Correctmodelrate,sensitiv-
ity or speciﬁcity for covari-
ate selection
Wu et al.compare four new methods in terms of
‘true positive’ and ‘false positive’ rates of covari-
ate selection (28)
Prediction Prediction/s Measuresofpredictiveaccu-
racy, calibration, discrimi-
nation
Ferrantecomparesfourmethodsintermsofmean
absolute prediction error, etc. (29)
Design
Design a study Selected design Sample size, expected sam-
ple size, power / precision
Zhang compares designs across multiple data-
generating mechanisms in terms of number of
signiﬁcant test results (described as ‘gain’) and
frequency of achieving the (near) optimal design
(30)
(targeting prediction). Where a simulation study evaluates methods for design, rather than analysis, of a biomedical study, the
design is the target.
Table3 summarisesdiﬀerentpossibletargetsofasimulationstudyandshowswhichperformancemeasures(describedmore
fully below) may be relevant for each target.
Inourreview,64simulationstudiestargetedanestimand,21targetedanullhypothesis,eighttargetedaselectedmodel,three
targeted predictive performance, and four had some other target. Of the 64 simulation studies targeting an estimand, 51 stated
whattheestimandwas(eitherinthedescriptionofthesimulationstudyorelsewhereinthearticle).Aﬁguredetailingthenumber
of estimands in simulation studies which targeted an estimand is given in the appendix, ﬁgure??
3.6 Performance measures
Theterm‘performancemeasure’describesanumericalquantityusedtoassesstheperformanceofamethod.Statisticalmethods
forestimationmayoutputforexampleanestimate ̂,itsvariance Var(̂)orSE(̂),degreesoffreedom,conﬁdenceintervals,test
statistics and more (such as an estimate of prognostic ability).
The performance measures required in a simulation study depends on what the study targets (see section 3.5). When the
target is an estimand, the most obvious performance measure to consider is bias: the amount by whicĥ exceeds on average.
Precisionandcoverageof (1−)conﬁdenceintervalsmayalsobeofinterest.Meanwhile,ifthetargetisanullhypothesis,power
andtypeI errorrateswillbeof primaryinterest.Asimulationstudy targetinganestimandmayof coursealsoassesspowerand
type I error.
The performance measures seen in our review are summarised in table 4 . The denominator changes according across per-
formance measures because some are not applicable for some simulation studies. Further, sometimes simulation studies had
secondary targets. For example, nine simulation studies primarily targeted a null hypothesis but secondarily targeted an esti-
mand and could have assessed bias, and one of these did so. For eight articles, some performance measures were unclear. In

---

## Page 8

8 TP Morris, IR White, MJ Crowther
TABLE 4Performance measures evaluated in review of Volume 34 (frequency and %)
Overall By primary target
Null hyp- Selected Predictive
Performance Estimand othesis model performance Other
measure (n = 64) ( n = 21) ( n = 8) ( n = 3) ( n = 4)
Convergence 12/85 (14%) 10/61 (16%) 1/15 (7%) 1/6 (17%) 0/2 0/1
Bias 63/80 (79%) 59/64 (92%) 1/9 (11%) 0/2 2/3 1/2
Empirical SE 31/78 (40%) 31/62 (50%) 0/9 0/2 0/3 0/2
Mean squared error 26/78 (33%) 22/62 (35%) 2/9 (22%) 0/2 1/3 1/2
Model SE 22/77 (29%) 21/62 (34%) 1/9 (11%) 0/2 0/3 0/1
Coverage 42/79 (53%) 39/63 (62%) 1/9 (11%) 0/2 1/3 1/2
Type I error 31/95 (33%) 8/62 (13%) 18/21 (86%) 4/6 0/3 1/3
Power 28/95 (29%) 8/63 (13%) 14/20 (17%) 4/6 0/3 2/3
Conf. int. width 11/80 (14%) 9/63 (14%) 0/10 0/2 1/3 1/2
Note – denominator changes across performance measures because not all are applicable in all simulation studies
TABLE 5The diﬀerent datasets involved in a simulation study
Dataset Description and notes
Simulated A dataset of size nobs produced with some element of random-number
generation and to which one or more methods are applied to produce
somequantityrelatingtothe targetofthestudy,suchasanestimateof .
Estimates† Datasetcontaining nsim summariesofinformationfromrepetitions(e.g.
̂ or indication of hypothesis rejection) for each combination of DGM,
method and target (e.g. each estimand).
States Datasetscontainingthestart-and/orend-of-repetitionrandom-number-
generator states for each simulated dataset (see section 4.1).
Performance
measures
Dataset containing estimated performance measures and Monte Carlo
standard errors for each DGM, method and target.
†or corresponding summaries for non-estimand targets
some,aperformancemeasurewasgivenanamewhichitsformulademonstratedtobemisleading,emphasisingtheimportance
of clear terminology in simulation studies.
Descriptionandcomputationofcommonperformancemeasuresofinterestaregiveninsection5.Animportantpointtoappre-
ciateindesignandanalysisisthatsimulationstudiesareempiricalexperiments,meaningperformancemeasuresarethemselves
estimatesandaresubjecttoerror.Thisfundamentalfeatureofsimulationstudiesdoesnotseemtobewidelyappreciated,aspre-
viouslynoted(4).Thismeansthatﬁrst,aswithanyotherempiricalexperiment,wemustnotactasifperformanceareknownbut
present estimates of uncertainty (described in section 5); second, there are implications for choosing the number of repetitions.
4 COMPUTATIONAL AND PROGRAMMING ISSUES IN SIMULATION STUDIES
In this section we discuss how to code a simulation study. It is useful to understand what sort of data are involved. There may
be up to four classes of dataset, listed and described in table 5 .

---

## Page 9

TP Morris, IR White, MJ Crowther 9
4.1 Random-numbers: setting seeds and storing states
In what follows, ‘seed’ refers to input planted by the user; ‘state’ refers to the speciﬁc state of the random-number generator at
a particular point in time.
All statistical packages capable of Monte Carlo simulation use a random-number generator. The numbers produced are in
fact pseudo-random and follow a completely deterministic path, given the initial state. For example, in R and Stata, each time
a number is ‘drawn’, the state of the random-number generator moves forward by one. So if a vector ofn random numbers is
generated, the state of the random number generator changesn times.
The‘pseudo’elementtorandom-numbergeneratorsissometimescharacterisedasnegative.Thisisperhapsanartefactofthe
factthatsomeearlyalgorithmsprovidedverypoorimitationsofrandomnumbers.However,modern-eraalgorithmssuchasthe
MersenneTwisterdonotsuﬀerfromtheseproblemsare,toallintentsandpurposes,trulyrandom.Thetossofacoinorrollofa
die may be regarded as equally deterministic, albeit the result of a complex set of unknown factors that act in an uncontrollable
fashion. These are not denigrated with the term ‘pseudo-random’: in statistical teaching they are often given as the ultimate
example of randomness. However, many stage magicians can control the ﬂip of a coin! If a computer pseudo-random number
generatorissuﬃcientlyunpredictableandpassesthevarioustestsforrandomness,itischurlishtoregardthe‘pseudo’aspectas
a weakness.
Thereareseveral positiveimplicationsofusingadeterministicandreproducibleprocessforgeneratingrandomnumbers.First,
if the number of repetitions is regarded as insuﬃcient, the simulation study can take oﬀ again from its landing state. Second,
if a certain repetition results in some failure, such as non-convergence, the starting state can be noted and the repetition re-run
under that state, enabling better understanding of when the method does not work so that issues leading to non-convergence
canbetackled.Finally,thewholesimulationstudycanbeindependentlyrunbyotherresearchers,givingthepotentialforexact
(rather than approximate) reproduction of results and the scope for additional methods to be included.
Our practical advice for utilising the deterministic nature of random-number generators is simple but strong: 1.set the seed
at the beginning, once and only once; 2.store the state of the random-number generator often(ideally once at the beginning of
each repetition). This is important, and the following chunk of pseudocode demonstrates the concept:
SET randomseed to #
FOR repetition 1 to n_sim
STORE repetition and randomstate in StatesData[repetition]
GENERATE simulated dataset
...
END FOR
When ‘stream’ random number generation is used (which invokes a ‘jump-ahead’ to allow simulations to be run in parallel),
this practical advice applieswithin a stream(13). There are several user-written R packages allowing independent streams of
random numbers. In Stata (from version 15), it is achieved with
. set rngstream #
prior to setting the seed.
The reason for this advice is to avoid unintended dependence between simulated datasets. We illustrate our caution with an
anecdote:onemethodofrecordingthestatesfor rrepetitionsistosetaseedandgenerateavectorof nsimintegersbygeneratinga
singlerandomnumber,recordingthestate,generatinganotherrandomnumber,recordingthestate,andsoon.Forthesimulation
itself, the seed for theith repetition is set to theith of the stored states. To clarify the problem, letnobs = nsim = 5 and let the
ﬁrstsimulationstepbegenerationofvector xfromaUniform(0,1)distribution.Theﬁrstrepetitionsimulates x1 (whichchanges

---

## Page 10

10 TP Morris, IR White, MJ Crowther
the random number state ﬁve times) and proceeds. The second repetition then simulatesx2, which is made up of observations
2 to 5 fromi = 1 plus one new value. The resulting draws ofx for the ﬁve repetitions are then:
x1 =(0.3488717, 0.2668857, 0.1366463, 0.0285569,0.8689333)
x2 =(0.2668857, 0.1366463, 0.0285569,0.8689333, 0.3508549)
x3 =(0.1366463, 0.0285569,0.8689333, 0.3508549, 0.0711051)
x4 =(0.0285569,0.8689333, 0.3508549, 0.0711051, 0.3233680)
x5 =(0.8689333, 0.3508549, 0.0711051, 0.3233680, 0.5551032)
Notetheboldelementoneachline:Theﬁfthelementof x1istheﬁrstelementof x5andappearsinallrepetitions.Onlywhen i>n
is the draw ofx independent of the ﬁrst repetition. Such dependency in simulated data has implications for both performance
measures and Monte Carlo SE’s and is best avoided. (Note that this structure is not certain because the way input seeds map to
states and vice versa is not 1:1.)
If the advice to set the seed once only is followed, there are implications for parallelisation, namely that it is inadvisable to
parallelise within a run (unless streams are being used (13)). Say we wish to produce the estimates dataset for a given DGM
via runs on two parallel processors. To be sure to avoid correlation between simulated datasets caused by one run ‘jumping in’
on the chain of random numbers used by the other, the landing state of the ﬁrst run must beknown for the starting seed of the
second to be set. Stream random-number generators ensure that the starting seed of the second run is (a long way) ahead of the
ﬁnal state of the ﬁrst. In the absence of streams, it is sensible to simply run all repetitions in one go.
When a simulation study uses diﬀerent data-generating mechanisms, these may be run in parallel. Because performance
measures will be computed separately for diﬀerent data-generating mechanisms, jumping in is less of a problem.
Many programs execute methods involving some stochastic element. Examples include multiple imputation, the bootstrap,
the g-computation formula, multistate models and Bayesian methods which use Markov chain Monte Carlo. Commands to
implementthesemethodsinvolvesomerandom-numbergeneration.Itisimportanttocheckthatsuchprogramsdonotmanipulate
the seed. Some packages do have a default seed if not input by the user. The implication is that many of thensim results will be
highly correlated, if not identical, and results should not then be trusted. With the number of user-written packages available in
R and Stata which may or may not rely on simulation somewhere, checking for such behaviour is worthwhile. A diagnostic for
whether any random-number generation is used is to display the current state, twice issue the command, and display the state
after each run. If the ﬁrst and second states are the same then the program probably does not use random numbers. If the ﬁrst
andsecondstatesdiﬀerbutthesecondandthirddonot,thisisacauseforconcernbecauseitindicatesthattheseedisbeingset
deterministically by the program.
4.2 Start small and build up code
It is all too easy to obtain misleading results in a simulation study through very minor coding errors; see for example the
comments in reference (31). Such errors are often detected when results are unexpected, for example, when bias appears much
greaterthantheoryorinstinctssuggest.Onedesignimplicationisthatmethodswithknownpropertiesshouldbeincludedwhere
possible as a check that these properties are exhibited. Mistakes in code are diﬃcult to avoid. One straightforward and intuitive
approach for minimising errors is to start small and speciﬁc for one repetition, then build and generalise, including plenty of
built-in checks.
Inasimulationstudywith nsim> 1andseveralsimulatedvariables,thestartingpointcouldbetocreateonerepetitionundera
largesamplesize.Ifvariablesarebeinggeneratedseparatelythenthecodeforeachshouldbeaddedonebyoneandthegenerated
dataexploredto1)checkthatthecodebehavesasexpectedand2)ensurethedatahavethedesiredcharacteristics.Forexample,
inStata,the rnormal(m,s) functionsimulatesnormalvariateswithmean m andstandarddeviation s.Theusualnotationfor
anormaldistributionusesameanand variance.Anecdotally,wehaveseenthissyntaxtripupgoodprogrammers.Bychecking
the variance of a variable simulated byrnormal in a large simulated dataset, it will be obvious if it does not behave in the
expectedfashion.Thesimulationﬁlecanbebuilttoincludediﬀerentdata-generatingmechanisms,methodsorestimands,again

---

## Page 11

TP Morris, IR White, MJ Crowther 11
checkingthatbehaviourisasexpected.Usingtheaboveexampleagain,ifthebasicdata-generatingmechanismusedN (, 1),the
issuewithspecifyingstandarddeviations vs.varianceswouldnotbedetected,butitwouldforotherdata-generatingmechanisms.
Once satisﬁed that one large run is behaving sensibly, it is worth setting the sample size required for the simulation study
and exploring the simulated datasets produced under a handful of diﬀerent seeds. When satisﬁed that the program still behaves
sensibly,itmaybeworthrunningafew(saytensof)repetitions.Ifforexampleconvergenceproblemsareanticipated,orbiasis
expected to be 0, this can be checked without the full set of simulations.
After thoroughly checking through and generalising code, the full set ofnsim repetitions may be run. However, recall the
precautioninsection4.1tostorethestatesoftherandom-numbergenerator.Therearetworeasonsforthis.First,programsmay
fail.Ifthishappensinrepetition4,120of5,000,wewillwanttounderstandwhy.Inthiscase,arecordofthe4,120thstatemeans
we can reproduce the problematic dataset instantly.
While the ability to reproduce speciﬁc errors is useful, it is also practically helpful to be able to continue even when an error
occurs.Forthispurpose,wedirectreaderstothe capture commandinStataandthe try commandinR.Thefailedanalysis
must be recorded as a missing value in the Estimates dataset; together with reasons if possible.
4.3 Using diﬀerent software packages for diﬀerent methods
Sixty two simulation studies in our review mentioned software. Table A1 (in the appendix) describes the speciﬁc statistical
software mentioned. Seven simulation studies mentioned using more than one statistical package.
Itisoftenthecasethatcompetingmethodsareimplementedindiﬀerentsoftwarepackages,anditwouldbemoreburdensome
to try and code them all in one package than to implement them in diﬀerent packages. There are two possible solutions. The
ﬁrst is to simulate data separately in the diﬀerent packages and then use the methods on those data. The second is to simulate
data in one package and export simulated data so that diﬀerent methods are based on the same simulated datasets.
Bothapproachesarevalidinprinciplebutweadvocatethelatterfortworeasons.First,itiscumbersometodoajobtwice,and
becausediﬀerentsoftwarepackageshavediﬀerentquirks,itwillnotbeeasytoensuredatareallyarebeinggeneratedidentically.
Second, if data are generated independently for diﬀerent methods, there will be diﬀerent (random) Monte Carlo error aﬀecting
eachrepetition.Byusingthesamesimulateddataforbothcomparisons,thisMonteCarloerrorwillaﬀectmethods’performance
in the same way because methods are matched on the same generated data.
5 ANALYSIS OF ESTIMATES DATA
5.1 Checking the estimates data and preliminaries
This section describes the computation of performance measures and Monte Carlo standard errors. We advocate two prelimi-
naries: checking for missing estimates and plots of the estimates data.
ThenumberofmissingestimatesandmissingSE’s(forexampleduetonon-convergence)aretheﬁrstperformancemeasures
to assess. Ideally, a method returning missing values should be explored under failed runs (see section 4) and the code made
more robust to ensure fewer or no failures.
Missing values in theestimates dataset pose a missing data problem regarding the analysis of other performance measures.
It is extremely implausible that values are missing completely at random(32); estimates will usually be missing due to non-
convergencesowilllikelydependonsomecharacteristic/sofagivenrealisationofthedata.Whenthe‘method’beingevaluated
involves an ‘analyst’s procedure’, where the model changes if the ﬁrst-choice model does not converge, this reduces or removes
missing values from the estimates data (see section 3.4).
Ifmorethantwomethodsareevaluatedandonemethodalwaysreturnsanestimate ̂i,thenmissingvaluesforanothermethod
may be related to the returned values for the ﬁrst method. In the presence of a non-trivial proportion of missing estimates data,
analysis of further performance measures should be tentative, particularly when comparing methods with diﬀerent numbers of
̂i missing.

---

## Page 12

12 TP Morris, IR White, MJ Crowther
Before undertaking a formal analysis of the estimates dataset it is sensible to undertake some exploratory analysis. In some
cases this may be suﬃcient for analysis. For example, Kahan and Morris (33) aimed to show that balancing treatments in
randomisedtrialsinducesacorrelationbetweenthemeanoutcomesintwogroups.Asimplesimulationwasusedandindividual
estimates presented in a scatterplot of the mean in one group against the other. This was suﬃcient to demonstrate the issue. A
second example can be found in (14), which assessed the performance of a two-stage procedure for analysing factorial trials.
Althoughtheprocedurewastechnicallyunbiased,ahistogramof ̂i exhibitedabimodaldistributionwithmodesequallyspaced
at either side of the truth but with almost no values of̂i close to!
For simulation studies targeting an estimand, the following plots are often informative:
1. Aunivariateplotofthedistributionof ̂i andSE(̂i)foreachDGM,estimandandmethod,toinspectthedistributionand,
in particular, to look for outliers.
2. A bivariate plot ofSE(̂i) vs. ̂i for each DGM, estimand and method, with the aim of identifying bivariate outliers.
3. Bivariate plots of̂i for one methodvs.another for each DGM and estimand. The purpose here is to look for correlations
between methods and any systematic diﬀerences. Where there are more than two methods being compared a graph of
every methodvs.every other orvs.the comparator can be useful.
4. A plot of conﬁdence intervals ranked by the signiﬁcance of the interval’s test (as in ﬁgure 5 ). This is a means of
understanding any issues with coverage.
These plots will be demonstrated and interpreted in the worked example (section 7).
Wenowdescribecommonperformancemeasures:propertiestheyaredesignedtoassess,computationandMonteCarloSE’s.
5.2 Computing common performance measures and their standard errors
This section outlines some common performance measures, pros and cons, how they are computed and how Monte Carlo
standard errors (MCSEs) are computed. We suppress the hat notation for performance measures, but emphasise that they are
estimates.
The formulas for Monte Carlo SEs are particularly needed. In our review of simulation studies inStatistics in Medicine
Volume 34, 93 did not mention Monte Carlo SEs for estimated performance measures.
Theﬁrstperformancemeasureofinterestisoftenbias,whichquantiﬁeswhethertheestimatortargets onaverage.Frequentist
theory holds unbiasedness to be a key property. The calculation is
Bias = 1
nsim
nsimÉ
i=1
̂i −
MCSE =
yxxw 1
nsim − 1
nsimÉ
i=1
(̂i −)2
Themeanof ̂i, ̄ isoftenreportedinstead.Thisiscalculatedinthesamewaybutwithoutsubtractingtheconstant ,andsohas
the same MCSE. It is sometimes preferable to report the relative per cent bias, rather than absolute bias. If diﬀerent values of
are used for diﬀerent data-generating mechanisms then per cent bias permits a more straightforward comparison across values.
However,relativebiascanbeusedonlyfor ðð> 0.Lackofbiasisonlyonepropertyofanestimator;whileitisoftenofcentral
interest, we may sometimes accept small biases because of other good properties.
The empirical SE depends only on̂ and does not require knowledge of. It estimates the long-run standard deviation of̂
over thensim repetitions.
EmpSE =
yxxw 1
nsim − 1
nsimÉ
i=1
(̂i − ̄)2
MCSE = EmpSE
√
2(nsim − 1)

---

## Page 13

TP Morris, IR White, MJ Crowther 13
FIGURE1 Bias,varianceandMSEfortwomethods.Method1isunbiasedbutimprecise;Method2isbiasedbutmoreprecise.
The method with lower MSE depends onn.
Method AMethod B012320406080100nobsBiasMethod AMethod B012320406080100nobsEmpirical SEMethod AMethod B012320406080100nobsRoot MSE
The empirical SE is a measure of the precision or eﬃciency of the estimator of. Several other designations in common use;
in our review we saw the terms ‘empirical standard deviation’, ‘Monte Carlo standard deviation’, ‘observed SE’, the ‘sampling
SE’ and more.
When comparing methods, it may be of interest to investigate the relative precision of methods against a comparator. The
precision of method B relative to method A is
Relative % increase in precision= Var(̂A)
Var(̂B)
=
0EmpSEA
EmpSEB
12
MCSE ≃ 2Var(̂A)
Var(̂B)
v
1 −2
AB
nsim − 1
where2
AB is the correlation of̂A and ̂B (10). Note that if either method is biased, the relative precision should be interpreted
with caution because an estimator which is biased towards the null can have a small empirical SE as a result of the bias:̂∕2
necessarily has smaller empirical SE than̂.
A related measure, which also takes the true value of into account, is the mean squared error.
MSE = 1
nsim
nsimÉ
i=1
(̂i −)2
MCSE =
yxxxxw
nsim∑
i=1
(̂i −)2 −MSE2
nsim(nsim − 1)
The MSE is the sum of the squared bias and variance of̂. This appears a natural way to integrate both measures into one sum-
maryperformancemeasure,buttherelativeinﬂuenceofbiasandofvarianceontheMSEvarieswith nobs,makinggeneralisation
of results diﬃcult.
The problem is summarised in ﬁgure 1 , which depicts the bias, empirical standard error and root MSE (RMSE, favoured
here because it is on the same scale as EmpSE) for two hypothetical methods. Method A is unbiased but imprecise (and so
RMSEissimplytheempiricalSE),whilemethodBisbiasedbutmoreprecise(asisoftenthecasewithbiasedmethods,seefor
example (34)). Fornobs> 50, RMSE is lower for method B, but fornobs> 50, RMSE is lower for method A. The lesson is that
comparisons of MSE are more sensitive to sample size than comparisons of bias or empirical SE alone.

---

## Page 14

14 TP Morris, IR White, MJ Crowther
The average estimated SE, which we term the ‘model SE’, is
ModSE =
yxxw 1
nsim
nsimÉ
i=1
Var(̂i)
MCSE ≃
yxxw Var[Var(̂i)]
4nsim × ¦ModSE
2
Thisiscomputedonthevariance,ratherthanstandarderror,scalebecauseitisonthisscalethatstandardtheoryyieldsunbiased
estimates.BecausethemodelSEtargetstheempiricalSE,relativeerrorinthemodelSEisaninformativeperformancemeasure.
Relative % error in ModSE= 100
0
ModSE
EmpSE − 1
1
MCSE = 100
0
ModSE
EmpSE
1yxxw Var[Var(̂i)]
4nsim × ¦ModSE
4 + 1
2(n − 1)
Coverage is a key property for the long-run frequentist behaviour of an estimator. It is deﬁned as the probability that a
conﬁdence interval contains. For a two-sided interval, the coverage proportion is estimated by
Coverage = 1
nsim
nsimÉ
i=1
1(̂low,i ≤ ≤ ̂upp,i) (1)
MCSE =
v
Coverage × (1 −Coverage)
nsim
(2)
Under-coverage is to be expected if for example i) Bias≠ 0, ii) ModSE< EmpSE, iii) the distribution of̂ is not normal
and intervals have been constructed assuming normality, or iv)Var(̂i) is too variable. Over-coverage occurs as a result of
ModSE> EmpSE. This may occur either in the absence or presence of issues (i) and (iii).
Note that Neyman’s original description of conﬁdence intervals deﬁned the property ofrandomisation validityas exactly
100(1 −)% of intervals containing (see (35, 36, 37)).Conﬁdence validityis the property that the true percentage is at least
100(1 −). This latter deﬁnition is less well known than the former, with the result that over- and under-coverage are regarded
as similarly bad(38). Of course, randomisation validity would usually be preferred over conﬁdence validity because it implies
shorterintervals–butthisisnotalwaysthecase!Thereareexamplesofproceduresthatreturnbothshorterintervalsandhigher
coverage (see for example (36, 37)).
As noted previously, under-coverage may be due to bias, while under- or over-coverage may be due to ModSE≠ EmpSE.
Weproposedecomposingpoorcoverageintoitscauseswithanewperformancemeasure:‘bias-correctedcoverage’.Inessence,
the bias of a method is eliminated from conﬁdence intervals by studying coverage of conﬁdence intervals for̂ rather than.
Bias-corrected coverage is computed as follows:
Bias-corrected coverage = 1
nsim
nsimÉ
i=1
1(̂low,i ≤ ̂ ≤ ̂upp,i)
with MCSE as for coverage.
Powerisoftenofprincipalinterestinsimulationstudieswhichtargetanullhypothesis,orwhensamplesizerequirementsare
beingestimatedbysimulation.Assumewehavep-values pi intheestimatesdataandareconsideringnominalsigniﬁcancelevel
. Thep-values may be derived from a Wald statistic using and ModSE, or directly output, for example by a likelihood-ratio
test or score test. The computation is as with other performance measures based on binary estimates data:
Power = 1
nsim
nsimÉ
i=1
1(pi ≤)
with MCSE as for coverage.

---

## Page 15

TP Morris, IR White, MJ Crowther 15
TABLE 6Coverage conditional on size of ModSE
Approach nsim analysed Coverage (SE)
All observations 30,000 95.0% (0.1%)
Conditional: ModSE in highest third 10,000 98.0% (0.1%)
Conditional: ModSE in middle third 10,000 95.5% (0.2%)
Conditional: ModSE in lowest third 10,000 91.5% (0.3%)
Wehavedescribedthemostcommonlyreportedandgenerallyapplicableperformancemeasures,particularlywhenasimulation
studytargetsanestimand.Thereareothersthataresometimesused(suchastheproportionoftimesthecorrectdoseisselected
in dose–response methods) and others that we have not yet thought of.
5.3 Estimation of conditional performance
Note that the relevance of diﬀerent performance measures will depend on the aims and targets of the simulation study. For
example, with linear models, the issue of missing estimates will not be relevant.
Conditional performance will sometimes, but not always, be of interest. Consider the following scenario:nobs = 30 observa-
tions are simulated fromy ∼ N(, 2), with = 0,2 = 1. For each repetition, 95% conﬁdence intervals for are constructed
using thet-distribution. The process is repeatednsim = 30, 000 times, and we study the coverage, ﬁrst for all repetitions, and
then according to tertiles of the model SE. The results are given in table 6 . Note that coverage is seen to be below 95% for the
lowest third of standard errors, above 95% for the highest third, and slightly above for the middle third. If coverage were cor-
rect regardless of any value of the SE, this may be viewed as positive, but poor conditional performance should be no cause for
concern. Methods rarely, if ever, claim to provide good performance in this sense.
Oneissuewiththeexampledescribedisthat,inanalysingdata,onewouldneverknowifthemodelSElayinthelower,middle
or higher third of all possible model SEs.
In fact, conditional evalutation of performance may sometimes be of central interest. This is particularly true of simulation
studieswhichaimtoevaluatestudydesigns,forexamplewheredesigndecisionsaremadebasedontheearlydata.Twosimulation
studies in our sample explored two-stage procedures in randomised trials, where the estimand is selected after the ﬁrst stage:
the estimand is the treatment eﬀect in a selected subpopulation (39) or the eﬀect of a selected treatment (40). In both cases,
estimatorsweredesignedtobeconditionallyunbiased.Kimanireportedbiasconditionaloneachpossibleselectionofestimand
(39),whileCarrerasaveragedthebiasacrossestimands(40).Theformermethodisstricterandarguablymoreappropriatesince,
having selected an estimand, the observer is not interested in the other case(41).
Notethatperformanceconditionalon true(ratherthansample-estimated)parameterswhichvaryacrossdata-generatingmech-
anismsisofcoursewheremethods should beexpectedtoprovidegoodperformance,andwedonotrecommendaveragingover
these.
We do not make any general recommendation other than to carefully consider whether to evaluate performance measures
conditional on sample statistics.
5.4 Sample size for simulation studies
Inchoosing nsim,thecentralissueisMonteCarloerror:keyperformancemeasuresneedtobeestimatedtoanacceptabledegree
of precision.
The values ofnsim reported in our review are shown in ﬁgure A1 . Four simulation studies did not reportnsim. Common
sample sizes arensim = 500 andnsim = 1, 000, as previously reported by Burtonet al.(5). Of the 87 studies reportingnsim, four
provided some justiﬁcation of the choice. The justiﬁcations were:

---

## Page 16

16 TP Morris, IR White, MJ Crowther
• ‘To evaluate the asymptotic biases’ (42)
• ‘errors can be reduced by the large number of simulation replicates’ (43)
• ‘number was determined mainly to keep computing time within a reasonable limit. A reviewer pointed out that, as an
additionaljustiﬁcation,byusing10,000meta-analysesthestandarderrorofanestimatedpercentage(e.g.,fortheempirical
coverage) is guaranteed to be smaller than 0.5.’ (20)
• Marozzi gives an explicit derivation of Monte Carlo SE (44)
Clearly this is a sub-optimal state of aﬀairs. For some more concrete justiﬁcations, see the worked illustrative example in
section 7, Keogh and Morris(45), or Morriset al.(46)
There exist situations where only one repetition is necessary, particularly when investigating large-sample bias; see for
example (16).Here, the aimwas to demonstratelarge-sample bias of anestimator and thesingle estimate of̂ was manymodel
standard errors from its true value.
Where the key performance measure is coverage,nsim can be deﬁned as follows. The Monte Carlo SE is given in section 5.2.
Plugging in the expected coverage (for example 95%) and rearranging, we get
nsim = E(Coverage) × (1 −E(Coverage))
(MCSEreq)2 (3)
with a similar expression ifnsim is to be determined based on power. For example, if the SE required for a coverage of 95% is
0.5%,
nsim = 95 × 5
0.52 = 1, 900 repetitions.
Coverageisestimatedfrom nsim binarysummariesoftherepetitions,sotheworst-caseSEoccurswhencoverageis50%.Inthis
scenario, to keep the required MCSE of 0.5% , (3) says thatnsim = 10, 000 repetitions will achieve this MCSE.
AconvenientfeatureofsimulationstudiesisthatMonteCarloSEcanbeassessedand nsim increasedmuchmorecheaplythan
with other empirical studies. The cost is computational time. For any such scenario it is important to have stored the landing
state of the random-number generator (which can be set to take back oﬀ without fear of a collision with a previously visited
state) or to use a diﬀerent stream.
5.5 Remarks on analysis
We have emphasised repeatedly that simulation studies are empirical experiments. In many biomedical experiments, ‘controls’
areusedasabenchmarkandtheestimatedeﬀectsofotherconditionsareestimatedasacontrast vs.control.However,simulation
studies often beneﬁt from having a known ‘truth’, meaning that the contrastvs. a control is not often of interest (hence the
term ‘comparator’ in section 3.4). That is, bias need not be estimated as thediﬀerence between ̂ for method A and̂ for the
comparator; rather the bias for a method stands alone, being computed against. There are benchmarks for other performance
measures as well, such as coverage (the nominal %) and precision (the Cramér–Rao lower bound(47, 48)).
Insomecases,thetruevalueof  isunknown:itmaynotappearinthedata-generatingmechanism.Ifperformancemeasures
involving are not of interest, this poses no problem. Otherwise, one solution is to estimate by simulation. Williamsonet al.
simulated data from a logistic model, but was not the conditional odds ratio used to generate data; was the marginal odds
ratio, risk ratio and risk diﬀerence(49). They thus estimated for each of these estimands from a large simulated dataset.
In our review, nine of 74 studies which included some estimated it, 57 used a known and 8 were unclear. Estimating
is in our view a sensible and pragmatic approach. However, such an approach must simulate a dataset so large that it is fair to
assumethatthevarianceof‘ ’isnegligible,particularlycomparedtothatof ̂,andensurethatthestatesoftherandom-number
generators used in the simulation study do not overlap with the states used for the purpose of estimating. In practice, the way
to do this is either to use a separate stream for the random numbers, or to run the-estimation simulation immediately before
the main run.

---

## Page 17

TP Morris, IR White, MJ Crowther 17
6 REPORTING
6.1 The ‘methods’ section
Our rationale for the ordering of elements inADMEP is that this is usually the best order to report them in a methods section. If
the simulation study has been planned and written out before it is executed then the methods section is largely written. This is
a particularly helpful ordering for other researchers who might wish to replicate it.
Details should be included to allow reproduction as far as possible, such as the value ofnsim and how this was decided on,
dependence among simulated datasets.
Another important element to report is a justiﬁcation of the chosen targets for particular applied contexts.
6.2 Presentation of results
Some simulation studies can be very small, for example exploring one or two performance measures under a single data-
generatingmechanism.Thesecanbereportedintext(asinHe etal. (50)).Inothercases,thereareenoughresultsthatitbecomes
necessary to report them in tabular or graphical form. For any tabulation or plot of results, there are four potential dimensions:
data generating mechanisms, methods, estimands and performance measures. This section provides some considerations for
presenting these results.
In tabular displays, it is common to divide rows according to data-generating mechanisms and methods as columns (as in
Chen,et al.(51)), though if there are more methods than data-generating mechanisms it may be better to swap these (as in Hsu,
Taylor and Hu (52)). Performance measures and estimands may vary across columns or across rows depending on what makes
the table easier to digest (see for example Alonsoet al.(53)).
There are two key considerations in the design of tables. The ﬁrst is how to place the important comparisons side-by-side.
The most important comparisons will typically be of methods, so bias for diﬀerent methods (for example) should be arranged
in adjacent rows or columns. But it may also be useful to compare across any of the other dimensions.
The second consideration regards presentation of Monte Carlo SEs, and this tends to confound the ﬁrst. By presenting them
nexttoperformancemeasures,forexamplesinparentheses,thetablebecomesclutteredandhardtodigest,obscuringinteresting
comparisons.Forthisreason,someauthorsreportthemaximumMonteCarleSEinthecaptionoftables(forexample(54,34)).
Results should not be presented to a greater accuracy than is justiﬁed by the MCSE. In our review of Volume 34, seven articles
presented Monte Carlo SEs for estimated performance measures: three in the text, two in a table, one in a graph, and one in a
ﬂoat caption.
The main advantage of displaying performance measures graphically is that it is easier to quickly spot patterns, particularly
over dimensions which are not compared side-by-side. A second advantage is that it becomes possible to present raw data
estimates (for example thêi) rather than performance measures summarising them (see for example ﬁgure 3 of (55)). In our
experience,theseplotsarepopularandintuitivewaystosummarisethe ̂iandmodelSE’s.Anotherexampleofaplotofestimates
data is a histogram given in Kahan(14). This is particularly important as Bias≃ 0, but the procedure he studies is inconsistent,
and almost nôi is close to. This is easily detected by plotting the estimates data. Thus, even if plots of estimates are not
plannedtobeincludedinpublicationsweurgetheiruseinexplorationofsimulationresults.Themaindisadvantagesofgraphical
displaysofresultsisthatplotscanbelessspace-eﬃcientthantables,itisnotpossibletoreadoﬀtheexactnumbers,andseparate
plots will usually be required for diﬀerent performance measures.
Comparedwithtables,itiseasiertoaccommodatedisplayofMonteCarloSE’sdirectlyinplotsofperformancemeasures,and
this should be done, for example as 95% conﬁdence intervals. However, the considerations about design for the most relevant
comparisonsapplysimilarly.Methodsoftenhavenamesthatarehardtoarrangesidebysideinalegiblemanner.Itmaythusbe
preferable to arrange methods in horizontal rows and performance measures moving horizontally in a style similar to a forest
plot.
As noted previously, full factorial designs can pose problems for presentation of results. One option for presentation is to
present data assuming no interaction unless one is obviously present. Rücker and Schwarzer present an approach to presenting
results of a full factorial simulation study with4 × 4 × 4 × 4 × 3 = 768 data-generating mechanisms, and comparison of

---

## Page 18

18 TP Morris, IR White, MJ Crowther
six methods(56). Their suggestion is to use a ‘nested-loop plot’, which loops through nested factors, usually data-generating
mechanisms, for an estimand, and plots results for diﬀerent methods on top of each other(56). This is a useful method, but will
not suit all designs. There are also challenges: how should the nesting of factors be determined? Should this be planned at the
design stage or should it be decided on seeing results (e.g. where the top level of nesting is the factor with the largest inﬂuence
on results)?
There is no one correct way to present results, but we encourage careful thought to facilitate readability, considering the
comparisons that need to be made.
7 WORKED ILLUSTRATIVE EXAMPLE
Tomakecleartheideasdescribedinthisarticleanddemonstratehowtheyshouldbeputintopractice,weconductoneexample
simulationstudy.Wehopethattheaimsandmethodsaresimpleenoughtobeunderstoodbyallreaders.Further,weincludethe
ﬁles required to run the simulation in Stata.
7.1 Design of example
The example is a comparison of three diﬀerent methods for estimating the hazard ratio in a randomised trial with a survival
outcome.
Consider the proportional hazards model, where we have the hazard rate for theith patient
ℎi(t) =ℎ0(t)exp(Xi), (4)
with ℎ0(t) the baseline hazard function,Xi a binary treatment indicator variable coded 0 for control and 1 for the research
arm, and the log hazard ratio for the eﬀect of treatment. There are various ways to estimate this hazard ratio, with common
approachesbeingtheCoxmodel,andstandardparametricsurvivalmodels,suchastheexponentialandWeibull.Theparametric
approaches make assumptions about the form of the baseline hazard functionℎ0(t) whereas the Cox model makes no such
assumption. We now describe a simulation study to evaluate the three methods in this simple setting.
Aims: To evaluate the impacts of 1) misspecifying the baseline hazard function on the estimate of the treatment eﬀect; 2) of
ﬁtting too complex a model when an exponential is suﬃcient; and 3) of avoiding the issue by using a semiparametric model.
Data-generating mechanisms:We consider two data-generating mechanisms. For both, data are simulated onnobs = 500
patients, representing a possible phase III trial with survival outcome. LetXi ∈ (0, 1) be an indicator denoting assignment
to treatment, where assignment is generated usingXi ∼ Bern(0.5) – simple randomisation with an equal allocation ratio. We
simulate survival times from the model in equation 4, assuming that = −0.5, corresponding to a hazard ratio of 0.607 (3dp).
We letℎ0(t) = t−1. The two data-generating mechanisms diﬀer only in the values of:
1:  = 0.1, = 1 ←both an exponential and a Weibull model
2:  = 0.1, = 1.5 ←a Weibull but not an exponential model
A plot of the hazard rateℎi(t) for the two data-generating mechanisms is given in ﬁgure 2 .
DataaresimulatedusingStata15usingthe64-bitMersennetwisterforrandomnumbergeneration.Theinputseedis‘72789’.
Methods:Each simulated dataset is analysed in three ways, using:
1. An exponential proportional-hazards model
2. A Weibull proportional-hazards model
3. A Cox proportional-hazards model
Note that the exponential model is correctly speciﬁed for the ﬁrst data-generating mechanism but misspeciﬁed for the second;
the Weibull model is correctly speciﬁed for both mechanisms; and the Cox model does not make any assumption about the
baseline hazard so is not misspeciﬁed for either mechanism.
Estimands: Our estimand is the log-hazard ratio forX = 1 vs. X = 0 , which would represent the treatment eﬀect in a

---

## Page 19

TP Morris, IR White, MJ Crowther 19
FIGURE 2 Visualisation of the true hazard rate over follow-up time in the two DGMs. Blue (ﬂat) lines are for the ﬁrst data-
generating mechanism where = 1; red curves are for the second, where = 1.5
γ=1, hi(t)|X=0
γ=1, hi(t)|X=1
γ=1.5, hi(t)|X=0
γ=1.5, hi(t)|X=10.00.10.20.30.4h(t)012345Time (years)
randomised trial.
Performance measures:We will assess bias, coverage, empirical and model-based standard errors for̂.
Bias is our key performance measure of interest, and we will assume that SD(̂) ≤ 0.2, meaning that Var(̂) ≤ 0.04. We
decide that we require MCSE lower than 0.005 on the estimate of bias. Given that
MCSE =
t
Var(̂)∕nsim,
this implies that we need 1,600 repetitions. If coverage of all methods is 95%, the implication of usingnsim = 1, 600 is
MCSE =
u
95 × 5
1, 600 = 0.54.
With 50% coverage, the MCSE is maximised at 1.25. We ﬁnd this satisfactory and so proceed withnsim = 1, 600(to be revised
if, for example, SD(̂)> 0.2).
7.2 Exploration and visualisation of results
Beforecomputingperformancemeasuresweﬁrstexploretherawresults.Figure3 plotstheestimates ̂i andSE(̂)i forthetwo
data-generating mechanisms and three methods. The left panels plot̂i. It is clear that, when = 1, the mean and variance of
̂i is very similar for the three methods. The mean is close to the true value of = −0.5for all methods. When in truth = 1.5,
thevarianceof ̂i isslightlyhigherforallmethods(becausetherearefewereventsamongthe500observationsunderthisdata-
generating mechanism). The exponential proportional-hazards model is now misspeciﬁed and we observe a shift of the mean
of ̂i towards the null, indicating some bias. The right panels of ﬁgure 3 plot the estimated standard errorsSE(̂)i. These are
lower for the upper panel ( = 1) than the lower ( = 1.5) but there is very little to choose between the methods.
We next compare these estimates by plottinĝi for each methodvs. every other method, and the same forSE(̂)i. The data
pairs come from the same repetition (i.e.they are estimated in the same simulated dataset) and are compared to a line ofy =x.
Thisisdoneinﬁgure4 ,fortheseconddata-generatingmechanismonly(  = 1.5),whichisinterestingbecausetheexponential
model is misspeciﬁed. We can see that the estimates of botĥi and SE(̂i) are highly correlated across all methods. The upper
triangleofplotsinﬁgure4 showsthat,while ̂i isalmostidenticalfortheWeibullandCoxmodels,ittendstobesystematically
closerto0fortheexponentialmodel.Theestimatesof SE(̂i)showthatagain,theestimatesareextremelysimilarfortheWeibull
and Cox models, they are very slightly larger for the exponential model.
Figure5 isanewvisualisation,the‘zipplot’,whichhelpstounderstandcoveragebyviewingtheconﬁdenceintervalsdirectly.
For each data-generating mechanism and method, the conﬁdence intervals are centile-ranked according to their signiﬁcance
against the null that = 0.5. This ranking is used for the vertical axis and is plotted against the intervals themselves. Intervals

---

## Page 20

20 TP Morris, IR White, MJ Crowther
FIGURE 3 Plot of the 1,600̂i (left panels) andSE(̂)i (right panels) by data-generating mechanisms, for the three analysis
methods. The vertical axis is repetition number, to provide some separation between points.
CoxWeibullExponentialCoxWeibullExponential-1.5-1-.50.5-1-.50DGM: γ=1DGM: γ=1.5
θᵢ
Cox
Weibull
Exponential
Cox
Weibull
Exponential
.18.2.22.24.26
.14.15.16.17
DGM: γ=1
DGM: γ=1.5
SE(θᵢ)
forwhichatwo-sidedtestyields p< 0.05arecolouredpurple(towardsthetop),whiletheremainderareinblue(atthebottom).
When a method has 95% coverage, the colour of the intervals switches at 95 on the vertical axis. Finally, the yellow horizontal
lines are Monte Carlo 95% conﬁdence intervals for per cent coverage.
Inﬁgure5 ,theupperpanelagaindisplaystheresultswhen  = 1 andthelowerpanelwhen  = 1.5.Despitecoveragebeing
approximately 95% as advertised, there are more intervals to the right of = −0.5 than to the left, particularly for those which
donotcover .ThisindicatesthatthemodelSEsmustoverestimatetheempiricalSE,becausecoverageisadequatedespitebias.
Figure 5 helps to make such a feature clear.
7.3 Analysis of example
The previous section suggested some useful exploratory analyses. Next, we compute the performance measures of interest and
presenttheminatableinwhich(wehope)theADMEPstructureisclear:diﬀerentperformancemeasuresarestackedvertically;
for each performance measure, the results for the two data-generating mechanisms each occupy one row; results for diﬀerent
methods are arranged across three columns (with MCSEs in parantheses at a smaller point size than the estimate); there is only
one estimand.
The results in table 7 conﬁrm more formally some of the features we saw in our exploration of the estimates data. The
interesting features concern the exponential model when = 1.5, since the Weibull and Cox models behave well in all cases.
Weseethattheexponentialmodelsuﬀerssomebiastowardsthenull,whichisapproximately10%ofthetruevalue.Thisisnon-
negligible.Next,weseethatcoverageisstilloverthenominal95%,whichissurprisinginthepresenceofbias.TheempiricalSE
is the same for all models when = 1 and lowest for the exponential model when = 1.5, while the Weibull and Cox models
areverysimilar;recallhoweverthatinthepresenceofdiﬀerentbiases,theempiricalSEisnotcomparableacrossmethods.For
relative precision (vs. the Weibull model) a very similar pattern is seen as for empirical SE. The Model SE is the same for all
methodsanddata-generatingmechanisms.Thisexplainswhytheexponentialmodelhasacceptablecoveragewhen  = 1.5:the
bias is cancelled out by the fact that the model SE is overestimated. This is conﬁrmed by the relative error in Model SE.

---

## Page 21

TP Morris, IR White, MJ Crowther 21
FIGURE 4 Comparison of estimates for methods when = 1.5, where each point represents one repetition. Upper triangle
displays ̂i; lower triangle displaysSE(̂i).
Exponential
θᵢ
SE(θᵢ)
-1
-.5
0
-1-.50-1
-.5
0
-1-.50
.14
.15
.16
.17
.14.15.16.17
Weibull
θᵢ
SE(θᵢ)
-1
-.5
0
-1-.50
.14
.15
.16
.17
.14.15.16.17.14
.15
.16
.17
.14.15.16.17
Cox
θᵢ
SE(θᵢ)
TABLE 7Estimates of performance measures of interest(MCSEs in parentheses)
Performance Data-generating Method
measure mechanism Exponential Weibull Cox
Bias  = 1 −0.003 (0.005) −0.003 (0.005) −0.002 (0.005)
 = 1.5 0.049 (0.003) 0.005 (0.004) 0.006 (0.004)
Coverage  = 1 95.4% (0.5) 95.4% (0.5) 95.4% (0.5)
 = 1.5 96.0% (0.5) 95.6% (0.5) 95.8% (0.5)
Bias-corrected  = 1 95.6% (0.5) 95.3% (0.5) 95.4% (0.5)
coverage  = 1.5 97.2% (0.4) 95.7% (0.5) 96.1% (0.5)
Empirical SE  = 1 0.209 (0.004) 0.209 (0.004) 0.209 (0.004)
 = 1.5 0.138 (0.002) 0.152 (0.003) 0.151 (0.003)
Relative precision  = 1 0.2% (0.1) 0 (–) 0.3% (0.1)
gainvs.Weibull  = 1.5 20.5% (0.4) 0 (–) 0.6% (0.2)
Model SE  = 1 0.208 (<0.001) 0.208 (<0.001) 0.208 (<0.001)
 = 1.5 0.154 (<0.001) 0.154 (<0.001) 0.154 (<0.001)
Relative error in  = 1 −0.7% (1.8) −0.7% (1.8) −0.5% (1.8)
Model SE  = 1.5 11.5% (2.0) 1.7% (1.8) 2.1% (1.8)
Lookingattable7 ,theMCSEsoftheperformancemeasuresareallacceptableandsowewouldbehappytodrawconclusions
about the methods based on the 1,600 repetitions.

---

## Page 22

22 TP Morris, IR White, MJ Crowther
FIGURE5 ‘Zipplot’ofthe 1, 600conﬁdenceintervalsforeachdata-generatingmechanismandanalysismethod.Thevertical
axis is the centile of the two-sidedp-value againstH0 ∶ = −0.5 associated with the conﬁdence interval.
5509555095-2-1012-2-1012-2-1012DGM: γ=1, ExponentialDGM: γ=1, WeibullDGM: γ=1, CoxDGM: γ=1.5, ExponentialDGM: γ=1.5, WeibullDGM: γ=1.5, CoxCovererNon-covererCentile of ranked p-values for null: θ=–0.595% confidence intervals
7.4 Conclusions of example
When an exponential model is misspeciﬁed the hazard ratio can be biased. Probably not by much. Further research is needed
(using diﬀerent values ofnobs and of).
8 CONCLUDING REMARKS
Simulation studies are an invaluable tool for research into statistical methods, evidenced by the large proportion of Volume 34
Statistics in Medicinearticles whose conclusions relied in part on simulation studies. Because methods promoted may be used
in medical research, transparent reporting of the design and execution of simulation studies is critical.
While simulation studies are widely used, they tend to be poorly reported by those who publish their results.
Therearemanyareastobeimprovedinthereportingofsimulationstudies.Ourviewisthatthetwomainshortcomingsare(i)
lack of clarity over the design, whichADMEP aims to deal with, and (ii) failure to report estimates of Monte-Carlo uncertainty.
We have described – and advocate – a structured approach to the planning of simulation studies which involves identifying
aims,data-generating mechanisms,methods,estimandsandperformance measures. All of these and the rationale for decisions
should be included in reporting. For an excellent example of a clearly described design, see Austin and Stuart(57). Reports

---

## Page 23

TP Morris, IR White, MJ Crowther 23
of simulation studies are now beginning to explicitly use theADMEP structure; see Thompsonet al.(58), Sayerset al.(59) and
Morris et al(46).
WehavegivenformulasforcomputingtheMonteCarlostandarderrorforthemostcommonperformancemeasures,andmade
somesuggestionsaboutreporting.NotethattheStatapackage simsum automatesthisprocessforcommonlyusedperformance
measures(10).
8.1 Simulation studies evaluating methods of widespread and general interest
Oneissuethatariseswithchoosingdata-generatingmechanismsisthatdiﬀerentresearchgroupsmayreachdiﬀerentconclusions.
Methods are created by researchers who are most concerned with handling the speciﬁc problems they have seen. From those
researchers’ perspectives, their simulation scenarios will be appropriate (this does not imply ‘cheating’).
It is worth noting two areas where diﬀerent research groups have been working on similar problems, and very diﬀerent
strategies have been taken. The ﬁrst concerns heterogeneity variance estimators in meta-analysis, and the second, methods for
handling incomplete data with a multilevel structure.
Langan, Higgins and Simmonds provide a comprehensive review of simulation studies comparing heterogeneity variance
estimators for meta-analysis(60). A bewildering array of methods – and of simulation studies – exist for this problem. The
authorsnotedthatingeneral,‘resultswerebasedondatathatdonotrepresentmeta-analysesobservedinpractice,’anddescribed
‘conﬂict(s) of interest in these non-independent studies’(60). Their article ends by saying that they, not having invented any of
the methods, are conducting further simulation studies to address these limitations(60). Petropolou and Mavridis then recently
published an article attempting this(61).
Several research groups have been developing methods for handling incomplete data in datasets with a multilevel structure
since around 2010. In summer 2013, a meeting was held at LSHTM to come exchange ideas. There were several points of
confusion among presenters about the design of simulation studies, particularly regarding data-generating mechanisms. It was
not obvious why certain methods had fared well in some simulation studies but not others. As a result, the day stimulated
collaboration,leadingtosimulationstudiesinvolvingrepresentativesfromallthegroups(62).Thiscanactasabasefromwhich
future simulation studies can be designed.
Bothsituationshighlightthepotentialvalueofopenrepositoriesofdataandcode,ofcleardescriptionoftheappliedsettings
for which methods are intended, and a description of situations in which new methods should be tested.
8.2 Final remark
We hope that this guidance will improve researchers’ understanding, planning, execution and future reporting of simulation
studies.
CONFLICTS OF INTEREST
All authors declare that they developed, and regularly deliver, a short course on simulation studies, from which this work grew,
and from which one or more person beneﬁts ﬁnancially.
ACKNOWLEDGEMENTS
Tim Morris and Ian White are supported by the Medical Research Council (grant numbers MC_UU_12023/21 and
MC_UU_12023/29). Michael Crowther is partly supported by an MRC New Investigator Research Grant (grant number
MR/P015433/1).

---

## Page 24

24 TP Morris, IR White, MJ Crowther
Forthought-provokingdiscussionsandinputtothiswork,wewishtothankTraPham,BrennanKahan,RuthKeogh,Alessan-
dro Gasparini, Clémence Leyrat and Christian Hennig. We also thank the many participants who have attended our courses,
whose questions and feedback provided the motivation for this article.
References
[1] Feiveson A. H.. Power by simulation.The Stata Journal.2002;2(2):107–124.
[2] Hoaglin D. C., Andrews D. F.. The reporting of computation-based results in statistics.The American Statistician.1975;29(3):122–126.
[3] Hauck W. W., Anderson S.. A survey regarding the reporting of simulation studies.The American Statistician.1984;38(3):214–216.
[4] Ripley B. D..Stochastic Simulation. New York: Wiley; 1987.
[5] BurtonA.,AltmanD.G.,RoystonP.,HolderR.L..Thedesignofsimulationstudiesinmedicalstatistics. StatisticsinMedicine. 2006;25(24):4279–4292.
[6] KoehlerE.,BrownE.,Haneuse.OntheassessmentofMonteCarloerrorinsimulation-basedstatisticalanalyses. TheAmericanStatistician. 2009;63:155–
162.
[7] Morgan B. J. T..Elements of simulation. Boca Raton: Chapman & Hall/CRC; 1995.
[8] Chang M..Monte Carlo simulation for the pharmaceutical industry : concepts, algorithms, and case studies. CRC Press; 2011.
[9] Díaz-Emparanza I.. Is a small Monte Carlo analysis a good analysis?.Statistical Papers.2002;43(4):567–577.
[10] White I. R.. simsum: Analyses of simulation studies including Monte Carlo error.Stata Journal.2010;10(3):369–385.
[11] Smith M. K., Marshall A.. Importance of protocols for simulation studies in clinical drug development.Statistical Methods in Medical Research.
2011;20(6):613–622.
[12] Crowther M. J., Lambert P. C.. Simulating biologically plausible complex survival data.Statistics in Medicine.2013;32(23):4118–4134.
[13] Haramoto H., Matsumoto M., Nishimura T., Panneton F., L’Ecuyer P.. Eﬃcient jump ahead for F2-linear random number generators.INFORMS Journal
on Computing.2008;20(3):385–390.
[14] Kahan B. C.. Bias in randomised factorial trials.Statistics in Medicine.2013;32(26):4540–4549.
[15] Kenward M. G., Roger J. H.. Small sample inference for ﬁxed eﬀects from restricted maximum likelihood.Biometrics.1997;53:983–997.
[16] WhiteI.R..LettertotheEditor:SurvivalanalysisofrandomizedclinicaltrialsadjustedforpatientswhoswitchtreatmentsbyM.G.LawandJ.M.Kaldor,
Statistics in Medicine, 15, 2069–2076 (1996).Statistics in Medicine.1997;16(22):2619–2620.
[17] White I. R., Thompson S. G.. Adjusting for partially missing baseline measurements in randomised trials.Statistics in Medicine.2005;24(7):993–1007.
[18] Hughes R. A., Sterne J. A. C., Tilling K.. Comparison of imputation variance estimators.Statistical Methods in Medical Research.2014;:n/a+.
[19] Morris T. P., White I. R., Royston P.. Tuning multiple imputation by predictive mean matching and local residual draws.BMC Medical Research
Methodology.2014;14(1):75+.
[20] Kuss O.. Statistical methods for meta-analyses including information from studies without any events—add nothing to nothing and succeed nevertheless.
Statistics in Medicine.2015;34(7):1097–1116.
[21] Campbell H., Dean C. B.. The consequences of proportional hazards based model selection.Statistics in Medicine.2014;:1042–1056.
[22] Robins J. M., Wang N.. Inference for imputation estimators.Biometrika. 2000;87(1):113–124.
[23] Reiter J. P.. Multiple imputation when records used for imputation are not used or disseminated for analysis.Biometrika. 2008;95(4):933–946.
[24] Crowther M. J., Look M. P., Riley R. D.. Multilevel mixed eﬀects parametric survival models using adaptive Gauss–Hermite quadrature with application
to recurrent events and individual participant data meta-analysis.Statistics in Medicine.2014;33(22):3844–3858.
[25] Hauck W. W., Anderson S., Marcus S. M.. Should we adjust for covariates in nonlinear regression analyses of randomized trials?.Controlled Clinical
Trials.1998;19:249–256.
[26] Zhang Z.. Estimating a marginal causal odds ratio subject to confounding.Communications in Statistics - Theory and Methods.2008;38(3):309–321.
[27] ChaurasiaA.,HarelO..PartialF-testswithmultiplyimputeddatainthelinearregressionframeworkviacoeﬃcientofdetermination. StatisticsinMedicine.
2015;34(3):432–443.

---

## Page 25

TP Morris, IR White, MJ Crowther 25
[28] WuC.,ShiX.,CuiY.,MaS..Apenalizedrobustsemiparametricapproachforgeneâ/uni0102/uni015Eenvironmentinteractions.StatisticsinMedicine. 2015;34(30):4016–
4030.
[29] Ferrante L., Skrami E., Gesuita R., Cameriere R.. Bayesian calibration for forensic age estimation.Statistics in Medicine.2015;34(10):1779–1790.
[30] Zhang Z., Wang C., Troendle J. F.. Optimizing the order of hypotheses in serial testing of multiple endpoints in clinical trials.Statistics in Medicine.
2015;34(9):1467–1482.
[31] Bartlett J..Combining bootstrapping with multiple imputation.2016.
[32] Rubin D. B.. Inference and missing data.Biometrika. 1976;63:581–592.
[33] Kahan B. C., Morris T. P.. Improper analysis of trials randomised using stratiﬁed blocks or minimisation.Statistics in Medicine.2012;31(4):328–340.
[34] White I. R., Royston P.. Imputing missing covariate values for the Cox model..Statistics in Medicine.2009;28(15):1982–1998.
[35] Neyman J.. On the Two Diﬀerent Aspects of the Representative Method: The Method of Stratiﬁed Sampling and the Method of Purposive Selection.
Journal of the Royal Statistical Society, Series A.1934;97(4):558–625.
[36] Meng X. L.. Multiple-imputation inferences with uncongenial sources of input.Statistical Science.1994;9:538–558.
[37] Rubin D. B.. Multiple imputation after 18+ years.Journal of the American Statistical Association.1996;91(434):473–489.
[38] Morris T. P.. Rank minimization with a two-step analysis should not replace randomization in clinical trials.Journal of Clinical Epidemiology.
2012;65(7):810–811.
[39] Kimani P. K., Todd S., Stallard N.. Estimation after subpopulation selection in adaptive seamless trials.Statistics in Medicine.2015;34(18):2581–2601.
[40] Carreras M., Gutjahr G., Brannath W.. Adaptive seamless designs with interim treatment selection: a case study in oncology.Statistics in Medicine.
2015;34(8):1317–1333.
[41] Efron B., Hastie T..Computer age statistical inference.Cambridge University Press; 2016.
[42] TaguriM.,ChibaY..Aprincipalstratiﬁcationapproachforevaluatingnaturaldirectandindirecteﬀectsinthepresenceoftreatment-inducedintermediate
confounding.Statistics in Medicine.2015;34(1):131–144.
[43] Li P., Redden D. T.. Small sample performance of bias-corrected sandwich estimators for cluster-randomized trials with binary outcomes.Statistics in
Medicine. 2015;34(2):281–296.
[44] Marozzi M.. Multivariate multidistance tests for high-dimensional low sample size case-control studies.Statistics in Medicine.2015;34(9):1511–1526.
[45] Keogh R. H., Morris T. P..Multiple imputation in Cox regression when there are time-varying eﬀects of exposures.2017.
[46] Morris T. P., Fisher D. J., Kenward M. G., Carpenter J. R.. Meta-analysis of Gaussian individual patient data: two stage or not two stage?.Statistics in
Medicine. in-press 2017;.
[47] Cramér H. C..Mathematical Methods of Statistics. Princeton, NJ: Princeton University Press; 1946.
[48] RaoC.R..Informationandtheaccuracyattainableintheestimationofstatisticalparameters. BulletinoftheCalcuttaMathematicalSociety. 1945;37:81–91.
[49] WilliamsonE.J.,ForbesA.,WhiteI.R..Variancereductioninrandomisedtrialsbyinverseprobabilityweightingusingthepropensityscore. Statisticsin
Medicine. 2014;33(5):721–737.
[50] He X., Whitmore G. A., Loo G. Y., Hochberg M. C., Lee M-L T.. A model for time to fracture with a shock stream superimposed on progressive
degradation: the Study of Osteoporotic Fractures.Statistics in Medicine.2015;34(4):652–663.
[51] Chen Y., Hong C., Riley R. D.. An alternative pseudolikelihood method for multivariate random-eﬀects meta-analysis. Statistics in Medicine.
2015;34(3):361–380.
[52] HsuC.H.,TaylorJ.M.G.,HuC..Analysisofacceleratedfailuretimedatawithdependentcensoringusingauxiliaryvariablesvianonparametricmultiple
imputation. Statistics in Medicine.2015;34(19):2768–2780.
[53] Alonso A., Milanzi E., Molenberghs G., Buyck C., Bijnens L.. A new modeling approach for quantifying expert opinion in the drug discovery process.
Statistics in Medicine.2015;34(9):1590–1604.
[54] Seaman S. R., Bartlett J. W., White I. R.. Multiple imputation of missing covariates with non-linear eﬀects and interactions: an evaluation of statistical
methods..BMC Medical Research Methodology.2012;12(1):46+.
[55] LambertP.C.,DickmanP.W.,RutherfordM.J..Comparisonofdiﬀerentapproachestoestimatingagestandardizednetsurvival.. BMCMedicalResearch
Methodology.2015;15(1):64+.
[56] Rücker G., Schwarzer G.. Presenting simulation results in a nested loop plot.BMC Medical Research Methodology.2014;14(1):129+.

---

## Page 26

26 TP Morris, IR White, MJ Crowther
TABLE A1Software mentioned in simulation reports, review ofStatistics in MedicineVolume 34. Note that there are more
than 100 entries as some articles reported more than one package.
Software Freq.
None mentioned 38
C 1
JAGS 1
MATLAB 1
R 41
SAS 17
SaTScan 1
Stata 4
StatXact 1
WinBUGS 3
[57] Austin P. C., Stuart E. A.. Optimal full matching for survival outcomes: a method that merits more widespread use. Statistics in Medicine.
2015;34(30):3949–3967.
[58] Thompson J. A., Fielding K. L., Davey C., Aiken A. M., Hargreaves J. R., Hayes R. J.. Bias and inference from misspeciﬁed mixed-eﬀect models in
stepped wedge trial analysis.Statistics in Medicine.2017;36(23):3670–3682.
[59] Sayers A., Crowther M. J., Judge A., Whitehouse M. R., Blom A. W.. Determining the sample size required to establish whether a medical device is
non-inferior to an external benchmark.BMJ Open.2017;7(8):e015397+.
[60] LanganD.,HigginsJ.P.T.,SimmondsM..Comparativeperformanceofheterogeneityvarianceestimatorsinmeta-analysis:areviewofsimulationstudies.
Res. Syn. Meth..2017;8(2):181–198.
[61] Petropoulou M., Mavridis D.. A comparison of 20 heterogeneity variance estimators in statistical synthesis of results from studies: a simulation study.
Statistics in Medicine.2017;36(27):4266–4280. Assess ’mean absolute error’ and claim it is bias.
[62] Audigier V., White I. R., Jolani S., et al.Multiple imputation for multilevel data with continuous and binary variables.2017.
APPENDIX A: REVIEW: SUMMARY OF INFORMATION AROUND DATA-GENERATION.
Figure A1 gives summary information about how data were generated. Panel (a) shows that there was great variation in the
total number of data-generating mechanisms, with the majority of simulation studies using under 20, but the largest number
being 600 billion. Panel (b) shows that simulation studies tended to vary few factors (with one exception). For the simulation
studies varying more than one factor, the most common way to do this was in a fully factorial manner (panel (c)). However,
some studies varied the factors one-at-a-time and others mixed the two together. Unfortunately, not all simulation studies noted
the number of repetitions (panel (d)). The most common choices ofnsim were, in descending order:1, 000, 500and 10, 000.
FigureA2 showsthenumberofmethodsevaluatedbythesimulationstudiesincludedinthereview.Themajorityevaluated
fewmethods(withfourthemostcommonnumber).Thissuggeststhatsimulationstudiesprovideaproof-of-concept,orthatthe
methods are designed for new problems for which there are few alternatives available.
Figure ?? shows the number of estimands evaluated by the simulation studies included in the review. In general, there were
few, with a single estimand the most common.
Table A1 lists the software packages mentioned and the number of mentions in simulation studies included in the review.
This was based on a lenient judgement: for example, many articles mentioned a software package in which a method was
implemented but did not mention what software was used to run the simulation study.

---

## Page 27

TP Morris, IR White, MJ Crowther 27
FIGURE A1 Results of Statistics in Medicine Volume 34 review for data-generating mechanisms: (a) number of data-
generating mechanisms used; (b) number of factors varied across data-generating mechanisms; (c) how factors were varied (if
>1 factor); (d) number of repetitionsnsim.
036912frequency6.00e+119600909028819216816214410896908481726056555452363230292827262420181614121097654321(a) Total number of data-generating mechanisms
051015202530frequency324149876543210(b) Number offactors varied0204060frequencyPartly factorialOtherOne-at-a-timeN/AFactorial(c) How factorswere varied
010203040frequency100000010000020000100005000300020001000500400200100501Not stated(d) Number of repetitions(nsim) per DGM

---

## Page 28

28 TP Morris, IR White, MJ Crowther
FIGURE A2 Results ofStatistics in MedicineVolume 34 review for number of methods evaluated.
0510152025frequency331816141210987654321Number of methods evaluated
FIGURE A3 Results ofStatistics in MedicineVolume 34 review for number of estimands evaluated in a simulation study.
0102030frequency3226221916141398754321Number of estimands evaluated

---
