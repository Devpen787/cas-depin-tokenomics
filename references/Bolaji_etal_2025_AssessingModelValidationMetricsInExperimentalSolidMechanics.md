# Bolaji_etal_2025_AssessingModelValidationMetricsInExperimentalSolidMechanics.pdf

## Page 1

Assessing Model Validation Metrics in Experimental 
Solid Mechanics 
Authors: 
• Elena M. Rodriguez, Ph.D. (Department of Mechanical and Aerospace Engineering, 
University of California, San Diego) 
• Kenji Tanaka, Ph.D. (Institute of Industrial Science, The University of Tokyo) 
• Fatima Al -Zahrani, Ph.D. (Center for Advanced Materials, King Abdullah 
University of Science and Technology) 
• Marcus Thiel,  Ph.D. (Laboratory for Mechanics of Advanced Materials, Swiss 
Federal Institute of Technology Zurich) 
Abstract 
The proliferation of computational models, particularly Finite Element Analysis (FEA), in 
engineering design and safety assessment necessitates rigorous, standardized methods for 
establishing their credibility. This paper synthesizes current research to ad dress the critical gap 
between qualitative, graphical comparisons and robust, quantitative validation in experimental 
solid mechanics. We examine the evolution of validation from a subjective assessment to a 
quantifiable process governed by formal metrics , tracing its conceptual foundations in statistical 
confidence intervals and its operationalization through full -field experimental techniques like 
Digital Image Correlation (DIC). The analysis focuses on two emergent, advanced methodological 
paradigms: pr obabilistic and adaptive threshold metrics, and full -field data fusion (FFDF) 
frameworks. We argue that while probabilistic metrics, such as the Moment Validation Metric 
(MVM), advance the field by incorporating uncertainty propagation for individual data descriptors, 
they are inherently limited to comparative analysis. In contrast, FFDF represents a transformative 
shift by creating a unified, high -fidelity data space from multiple experimental and numerical 
sources, enabling not only validation but also th e generation of novel performance parameters. 
This paper concludes that the future of model validation lies in integrated methodologies that 
combine the statistical rigor of advanced metrics with the holistic, information -rich approach of 
data fusion. This  synthesis is intended to provide a coherent framework for analysts and 
experimentalists, promoting best practices and enhancing the peer acceptance of computational 
model predictions in both academic and industrial contexts. 
Keywords: Model Validation, Verification and Validation (V&V), Validation Metrics, Finite 
Element Analysis (FEA), Digital Image Correlation (DIC), Full-Field Data Fusion, Experimental 
Solid Mechanics, Uncertainty Quantification 
1. Introduction 

---

## Page 2

The discipline of solid mechanics has undergone a profound transformation with the integration 
of computational modeling as a central pillar of research, design, and failure analysis. Finite 
Element Analysis (FEA), in particular, has evolved from a special ized tool to an indispensable 
instrument for predicting mechanical behavior under complex loading and boundary conditions. 
This predictive capability is especially critical in fields pushing material and structural limits, such 
as aerospace engineering, bi omedical implant design, and renewable energy infrastructure (e.g., 
wind turbine blades). However, the utility and credibility of any computational model are 
intrinsically contingent upon demonstrable agreement with physical reality. Consequently, the 
processes of Verification and Validation (V&V) have emerged as the foundational protocols for 
establishing model credibility and justifying the reliance placed on simulation outcomes for 
consequential decision-making . 
Within the V&V framework, verification answers the question, "Are we solving the equations 
correctly?" by ensuring the computational model is free of coding errors and numerical 
inaccuracies. Validation, the more epistemologically challenging endeavor, addresses the question, 
"Are we solving the correct equations?" by assessing the model's fidelity to the actual physical 
system it represents  . Historically, validation in solid mechanics has been largely qualitative, 
relying on graphical overlays of simulation results and experimental data —often comparing a 
handful of strain gauge readings or displacement points. This approach, while intuitive,  is 
fundamentally inadequate. It lacks the rigor to quantify the degree of agreement, systematically 
account for uncertainties inherent in both experimentation and simulation, or objectively assess 
model accuracy across the entire domain of interest  . The absence of standardized, quantitative 
methods has led to a reproducibility crisis and skepticism regarding model -based conclusions, 
particularly when extrapolated beyond their calibrated conditions. 
This paper posits that the central challenge in contemporary experimental solid mechanics is the 
transition from qualitative, subjective validation to a paradigm governed by quantitative validation 
metrics. A validation metric is defined as a computable measure that quantitatively compares 
computational predictions and experimental measurements for a System Response Quantity 
(SRQ), explicitly incorporating estimates of numerical error and experimental uncer tainty . The 
development and adoption of such metrics are not merely technical refinements but are essential 
for bridging the communicative gap between computational analysts, experimentalists, and 
ultimate stakeholders like certification agencies and clinicians . 
The primary objective of this synthesis is to critically analyze the evolution, current state, and 
future trajectory of quantitative validation methodologies. We focus on two interconnected 
frontiers: first, the development of advanced probabilistic and ad aptive validation metrics that 
move beyond simple global error norms; and second, the emergence of Full -Field Data Fusion 
(FFDF) as a holistic framework that transcends mere comparison to enable novel forms of analysis. 
The central research question interrogates how these advanced methodologies collectively address 
the limitations of traditional validation practices and what conceptual and practical synthesis is 
required to establish a robust, standardized validation protocol for high -fidelity computational  

---

## Page 3

solid mechanics. By examining these developments, this paper aims to provide a consolidated 
reference point for advancing the science of model credibility. 
2. Literature Review: From Qualitative Comparison to Quantitative Metrics 
The scholarly discourse on model V& V has evolved significantly over the past three decades, 
migrating from specialized fields like computational fluid dynamics (CFD) to become a central 
concern in computational solid mechanics. Early foundational work by Roache and guidelines 
from professional bodies like the AIAA and ASME established the core philosophical distinction 
between verification and validation and argued for the necessity of quantitative assessment . These 
works established that "validation is a process," not a singular event, and that its goal is to 
assess modeling error—the discrepancy between reality and the simulation due to assumptions in 
geometry, material properties, and physics . 
2.1 The Limitations of Traditional Graphical Methods and Early Metrics  
The traditional practice of graphical comparison, while valuable for initial inspection, suffers from 
critical deficiencies. It is inherently qualitative, lacks a mechanism to incorporate measurement 
uncertainty, and cannot objectively weigh discrepancies across an entire field of data. As 
Oberkampf and Barone argued, such methods are ill -suited for the quantitative validation needed 
in high-consequence engineering . In response, the first generation of quantitative metrics focused 
on global error norms, such as the root -mean-square (RMS) error or correlation coefficients 
computed over full -field displacement or strain maps obtained from techniques like DIC. 
Researchers like Babinsky & Hine and Gendre et al. explored the application of various L¹, L², 
and L∞ norms to gauge the magnitude of discrepancy between experimental and computational 
fields . 
However, these global norms possess significant limitations. They provide a single, aggregate 
value that can mask localized but critical areas of mismatch, such as stress concentrations at a 
notch root. Furthermore, they treat all regions of the field with  equal importance and fail to 
distinguish between discrepancies arising from true modeling error and those stemming from 
acknowledged experimental uncertainties or numerical approximation errors. This conflation is a 
major shortcoming, as a validation metr ic must, ideally, isolate and quantify the modeling error 
itself . 
2.2 The Incorporation of Uncertainty and Probabilistic Frameworks  
The recognition of uncertainty as an inescapable component of both experiment and simulation 
marked a pivotal advancement. Error, a quantifiable difference, must be distinguished from 
uncertainty, a potential deficiency due to lack of knowledge or inherent  variability . Modern 
validation methodologies explicitly require the quantification of uncertainties from various 
sources: random measurement noise, bias in experimental setups, uncertainty in constitutive model 
parameters, and numerical discretization errors. 

---

## Page 4

This led to the development of probabilistic validation metrics (PVMs). Building on statistical 
frameworks, these metrics treat experimental data and sometimes model parameters as 
distributions rather than deterministic values. The validation assessment then becomes a statistical 
comparison, often evaluating the probability that the computational predictions lie within the 
confidence intervals of the experimental data, or vice versa  . The work of Jiang, Chen, & Huang 
on probabilistic metrics under experimental uncertainty exemplifies this trend, aiming to provide 
a statement of confidence in the model's predictive capability rather than a binary pass/fail 
judgment. A parallel, sophisticated approach is found in Bayesian frameworks, which update the 
belief in model parameters or model form based on experimental evidence, though these are often 
more aligned with model calibration than pure validation. 
2.3 The Advent of Full -Field Data and Descriptor -Based Validation  
The widespread adoption of full -field measurement techniques, primarily DIC, has provided an 
abundance of high -spatial-resolution data, rendering point -wise comparisons impractical and 
elevating the need for intelligent data reduction. This spurred the development of descriptor-based 
validation. Instead of comparing millions of pixel values, the full -field data (both experimental 
and computational) are compressed into a set of representative features or descriptors. Common 
approaches include decomposition into spatial basis functions, such as Zernike polynomials or 
Proper Orthogonal Decomposition (POD) modes. The comparison is then performed on the 
weights (moments) of these descriptors. The core hypothesis is that if the dominant descriptors 
agree within uncertainty bounds, the fields are effectively equivalent for engineering purposes . 
Recent innovations, such as the Moment Validation Metric (MVM) proposed by Sáez Landete et 
al., push this paradigm further. The MVM critiques earlier PVMs that applied a constant 
uncertainty threshold to all Zernike moments. It introduces an  adaptive, moment -specific 
threshold derived from a rigorous propagation of the uncertainty from the original 
displacement/strain maps to each individual moment. This recognizes that lower -order moments 
(capturing global trends) and higher -order moments (capturing local details) are affected 
differently by noise and reconstruction error. Consequently, the MVM applies stricter tolerances 
to influential moments and more lenient ones to less impactful or noisier ones, theoretically 
providing a more sensitive and accurate detection of meaningful discrepancies . 
2.4 Synthesis and Identified Gap  
The literature demonstrates a clear trajectory: from qualitative graphics, to global error norms, to 
uncertainty-aware probabilistic metrics, and finally to adaptive, descriptor -based methods. This 
evolution represents a concerted effort to make validation  more objective, quantitative, and 
informative. However, a critical gap persists. Even the most advanced probabilistic or descriptor-
based metrics are fundamentally  comparative in nature. They assess the degree of similarity or 
difference between two entities—the model and the experiment. They do not inherently create new 
knowledge or insights beyond this comparison. The next section explores a nascent but 
transformative paradigm that addresses this gap: Full-Field Data Fusion, which shifts the objective 
from comparison to integration and synthesis. 

---

## Page 5

3. Methodology: Framing the Analysis of Validation Paradigms 
This paper employs a conceptual and analytical research design to synthesize and critically 
evaluate advanced methodologies in model validation. Given the theoretical and applied nature of 
the topic, the methodology is not empirical but rather focused on comparative analysis, conceptual 
integration, and critical appraisal of existing scholarly frameworks. The aim is to construct a 
coherent narrative that maps the evolution of validation concepts, elucidates the operational 
principles of cutting -edge techniques, and synthesizes their relative strengths and limitations to 
propose a forward-looking framework. 
3.1 Research Design and Conceptual Framework  
The analysis is structured around two primary analytical axes, derived from the reviewed literature. 
The first axis examines validation through the lens of  quantification and uncertainty 
management, tracing the progression from deterministic to probabilistic and adaptive metrics. 
The second axis examines validation through the lens of  data utilization and information 
synthesis, contrasting comparative metrics with integrative fusion frameworks. These axes are not 
mutually exclusive but represent complementary dimensions of a comprehensive validation 
strategy. The core conceptual framework is the established V&V paradigm, which strictly 
separates the processes of verification (solving equations right) and validation (solving the right 
equations) . This analysis focuses exclusively on the validation thread. 
3.2 Analytical Procedure  
The procedure involves three interconnected phases: 
1. Taxonomic Classification:  Emerging techniques from the literature, such as the 
MVM  and FFDF  , are classified based on their primary operational principle (e.g., 
statistical confidence intervals, adaptive thresholding, spatial data fusion), their input data 
requirements, and their primary output (a scalar metric vs. a fused data field). 
2. Comparative Functional Analysis: The classified methodologies are analyzed for their 
functional capabilities. This includes assessing how each method handles experimental and 
numerical uncertainty, whether it provides localized or global assessment, its sensitivity to 
different types of error, and its utility for guiding model improvement. 
3. Synthesis and Gap Analysis: The findings from the comparative analysis are synthesized 
to identify complementarities and tensions between different approaches. This phase 
explicitly identifies limitations within current paradigms and proposes integrative 
pathways that combine their strengths. 
3.3 Scope and Delimitations  
The scope of this study is confined to validation methodologies applicable to continuum solid 
mechanics models, primarily nonlinear FEA, where validation is performed against full -field 
experimental data. Methodologies specific to model calibration, parameter identification, or purely 
stochastic models are referenced but not deeply analyzed. The primary data sources considered are 

---

## Page 6

DIC and Thermoelastic Stress Analysis (TSA), as they represent the most prevalent full -field 
techniques for spatial validation. The analysis draws upon representative, high-impact scholarship, 
including formal metric definitions  , applications in biomechanics  , and recent innovations in 
metrics  and data fusion . 
3.4 Validity and Rigor  
Conceptual rigor is maintained by grounding all analyses in the foundational definitions and 
principles established by authoritative sources in the V&V literature . The comparative analysis is 
structured to be transparent and reproducible, with clear criteria for evaluating each methodology. 
The argumentation is constructed to highlight not only technological capabilities but also the 
underlying philosophical assumptions of each approach, ensuring a critical rather than descriptive 
synthesis. 
4. Results and Findings: Advanced Paradigms in Validation 
The critical analysis of contemporary literature reveals two dominant, advanced paradigms that 
address the shortcomings of traditional validation: sophisticated probabilistic/adaptive metrics and 
holistic data fusion frameworks. Their operational principle s, outputs, and inherent philosophies 
differ significantly. 
4.1 Adaptive Probabilistic Metrics: The Moment Validation Metric (MVM)  
The MVM, as a representative of the latest evolution in descriptor -based metrics, operationalizes 
validation as a  multi-threshold statistical hypothesis test . Its procedure, as detailed by Sáez 
Landete et al., is systematic : 
1. Data Reduction:  Both the experimental displacement field (from DIC) and the 
computational displacement field are projected onto a Zernike polynomial basis. This 
yields two sets of Zernike moments: {𝑀𝑖
𝑒𝑥𝑝} and {𝑀𝑖
𝑛𝑢𝑚}. 
2. Uncertainty Propagation:  Crucially, the uncertainty in the experimental displacement 
map (e.g., from correlation noise) is not assumed constant. It is propagated through the 
moment calculation algorithm to compute a distinct standard 
uncertainty 𝑢(𝑀𝑖
𝑒𝑥𝑝) for each Zernike moment 𝑖. 
3. Adaptive Threshold Definition: The validation threshold for moment 𝑖 is not a universal 
constant but is defined as  𝑇𝑖 = 𝑘 ⋅ 𝑢(𝑀𝑖
𝑒𝑥𝑝), where  𝑘 is a coverage factor (e.g., 2 for 
approximately 95% confidence). This creates an adaptive envelope: moments with low 
inherent uncertainty (typically lower -order, high-signal moments) have a tight tolerance, 
while moments with high uncertainty (higher -order, detail -capturing moments often 
contaminated by noise) have a wider tolerance. 
4. Metric Calculation: The metric itself can be formulated as a binary outcome per moment 
(pass if ∣ 𝑀𝑖
𝑛𝑢𝑚 − 𝑀𝑖
𝑒𝑥𝑝 ∣< 𝑇𝑖) or as a normalized, aggregated score quantifying the overall 
distance relative to the adaptive thresholds. 

---

## Page 7

Table 1: Comparison of Validation Metric Philosophies 
Feature Traditional Global 
Norm (e.g., RMS) 
Probabilistic/Adaptive 
Metric (e.g., MVM) 
Full-Field Data 
Fusion (FFDF) 
Core Philosophy Deterministic, 
aggregate difference 
Statistical, uncertainty -
aware comparison 
Integrative 
synthesis into 
unified data space 
Primary Output Single scalar error 
value 
Scalar metric or moment -
by-moment assessment 
A new, fused full -
field data set (e.g., 
stiffness map) 
Uncertainty 
Handling 
Implicit or ignored Explicit, propagated to 
decision threshold 
Explicit, used to 
weight data 
sources in fusion 
Localizing 
Capability 
Poor (aggregates all 
error) 
Good (can identify 
discrepant descriptors) 
Excellent 
(provides point -
wise fused data) 
Utility for Model 
Improvement 
Low 
(indicates if wrong) 
Moderate 
(suggests what aspect is 
wrong) 
High (provides 
direct field for 
discrepancy 
analysis) 
The key finding regarding the MVM is its enhanced discriminatory power. By applying stricter 
thresholds to well-characterized moments, it prevents the model from getting "undeserved credit" 
for matching noisy data and raises alerts for significant discrepancies in physically important, low-
uncertainty features. However, its limitation remains its comparative nature; the output is still a 
statement about agreement, not a new, enriched representation of the physical phenomenon. 
4.2 Transformative Integration: The Full -Field Data Fusion (FFDF) Framework  
In stark contrast, the FFDF methodology, as demonstrated by Dulieu -Barton and colleagues on a 
complex wind turbine blade substructure, fundamentally redefines the objective of experimental -
computational analysis . Its core principle is integration over comparison. Instead of asking "Do 
the FEA and DIC data match?", FFDF asks "What new understanding can we generate by 
seamlessly combining data from FEA, DIC, and TSA?" 
1. Data Unification: The first step is not compression but spatial registration and resolution 
matching. Disparate data sets (DIC strains, TSA stress information, FEA predictions) are 
mapped to a common, high-resolution spatial grid. This eliminates errors from comparing 
non-coincident points. 

---

## Page 8

2. Fusion and Synthesis: In this unified data space, operations beyond comparison become 
possible. For instance, DIC provides full-field strain (𝜖), and TSA under certain conditions 
provides a signal proportional to the sum of principal stresses ( 𝜎1 + 𝜎2). By fusing 
these experimental data sets, one can potentially infer a full-field, experimental estimate of 
material stiffness variation, a parameter not directly measurable by any single technique. 
The FEA -predicted stiffness field can then be compared to this fused experimental 
benchmark. 
3. Mutual Validation of Experiments: A powerful secondary benefit is that FFDF allows 
experimental techniques to cross -validate each other. Inconsistencies between DIC and 
TSA in a particular region can highlight areas where one technique's assumptions are 
violated (e.g., plastic yielding br eaking TSA's adiabatic elasticity assumption) or where 
processing parameters (like DIC subset size) introduce artifact . 
The primary finding for FFDF is its role as an  enabler of emergent insight. It moves validation 
from a post-hoc checking procedure to an integral part of the  analytical discovery process. The 
output is not just a metric but a new, high-fidelity data product—like a validated, full-field stiffness 
map—that itself has direct utility for assessing material performance or design modifications, 
potentially reducing reliance on costly full-scale tests . 
5. Discussion 
The presented findings illuminate a bifurcation in the future of validation: one path refines the 
science of quantitative comparison, while the other pursues a paradigm of integrative synthesis. 
This discussion interprets these paths, examines their implic ations, and argues for a necessary 
convergence. 
5.1 Interpretation of Paradigms: Refinement vs. Transformation  
The development of adaptive probabilistic metrics like the MVM represents the refinement of the 
comparative paradigm. It addresses precise, previously nebulous issues: how to fairly weight the 
importance of different spatial features and how to rigorously account for heterogeneous 
uncertainty. This refinement is essential for achieving defensible, high -confidence validation in 
regulatory or safety-critical contexts where a clear, auditable statement of agreement is required. 
Its strength lies in its specificity and its foundation in statistical rigor. 
Conversely, FFDF embodies a  transformative paradigm shift . It reconceptualizes validation 
from a gatekeeping function to a generative one. By creating a common, multi -modal data 
environment, it leverages the complementary strengths of different data sources. For example, DIC 
excels at in -plane deformation but is  insensitive to through -thickness effects, while TSA 
measurements are influenced by a complex volumetric stress state. Their fusion, guided by an FEA 
model's theoretical framework, can yield insights inaccessible to any approach in isolation  . This 
aligns with the broader engineering need to not just validate models but to use them, in concert 

---

## Page 9

with experiments, to discover new phenomena or optimize designs in ways not possible through 
testing alone. 
5.2 Synthesis: Toward an Integrated Validation Workflow  
The most compelling forward path is not to choose one paradigm over the other but to synthesize 
them into a cohesive, tiered validation workflow . We propose the following conceptual 
integration: 
1. Level 1 (Global Screening):  Use an adaptive probabilistic metric (e.g., MVM) as an 
initial, automated screening tool. It provides a rapid, objective "go/no-go" assessment and 
can pinpoint which spatial frequency bands or general types of descriptor show significant 
discrepancy. 
2. Level 2 (Diagnostic Fusion):  If a discrepancy is flagged, employ a targeted FFDF 
approach. Fuse the experimental data sets and the FEA predictions in the regions of interest. 
This fusion can help diagnose the root cause: for instance, a localized stiffness anomaly in 
the fused experi mental data might point to a material model defect, while a discrepancy 
only in the TSA -FEA comparison might indicate an error in modeling multiaxial stress 
effects. 
3. Level 3 (Predictive Enrichment): For a fully validated model, use FFDF prospectively to 
generate enriched validation benchmarks. A model validated against fused DIC/TSA data 
for one loading condition gains higher credibility. It can then be used to predict the TSA 
response for a new, unseen loading condition, providing a much richer validation test than 
displacement alone. 
5.3 Limitations and Future Research  
Both paradigms face challenges. Adaptive metrics require accurate propagation of complex 
uncertainty sources, which can be computationally intensive and relies on assumptions about error 
distributions. FFDF requires careful handling of registration errors and the development of robust 
fusion algorithms that do not introduce their own artifacts. A significant future research direction 
is the  integration of uncertainty quantification directly into the fusion process , creating 
probabilistic fusion frameworks that output not just a fused field but also its associated uncertainty. 
Furthermore, the development of standardized benchmark problems incorporating multi-modal 
experimental data and prescribed "modeling errors" is crucial for objectively testing and 
comparing the performance of these advanced validation methodologies. 
6. Conclusion 
This paper has synthesized the critical evolution of validation methodologies in experimental solid 
mechanics, arguing that the field is transitioning from an era of qualitative assessment to one 
defined by sophisticated quantitative and integrative framew orks. We have demonstrated that 
while advanced probabilistic and adaptive metrics, exemplified by the Moment Validation Metric, 
bring necessary statistical rigor and sensitivity to the comparative validation process, they are 

---

## Page 10

inherently limited to assessing agreement. In contrast, Full -Field Data Fusion represents a more 
profound advancement by repositioning validation as a synergistic process that generates novel, 
high-fidelity information from the confluence of experiment and simulation. 
The central scholarly contribution of this work is the articulation of these two paradigms —
comparative refinement and integrative transformation —and the proposal for their synthesized 
application. The future of credible computational mechanics lies not in the exclusive adoption of 
one sophisticated technique, but in the development of structured workflows that leverage adaptive 
metrics for efficient, objective screening and employ data fusion for deep diagnostic analysis and 
predictive enrichment. For practitioners, this implies moving beyond the quest for a single perfect 
metric and instead building a validation toolkit equipped with both precise comparators and 
powerful synthesizers. For the academic community, it underscores the need for continued 
research at the intersection of uncertainty quantification, information theory, and multi -physics 
experimentation to fully realize the promise of integrated validation, ultimately accelerating the 
development of safer, more efficient, and more innovative engineered systems. 
References 
1. Armandei, M., & Carolan, D. (2019). Quantitative metrics for validating finite element 
models with full -field experimental data. Experimental Mechanics , 59(4), 483 –497. 
https://doi.org/10.1007/s11340-018-00455-6 
2. Ali, N. K. a. A. (2025a). A hybrid Experimental -Numerical Benchmark for stress 
Concentration at a circular hole: Rigor, validation, and Uncertainty in photoelastic analysis. 
Power System Technology, 49(4), 2122–2138. https://doi.org/10.52783/pst.2796  
3. Babinsky, H., & Hine, A. (2011). Error norms and validation metrics for experimental –
computational comparisons in solid mechanics. Journal of Fluids and Structures , 27(3), 
394–406. https://doi.org/10.1016/j.jfluidstructs.2010.10.006 
4. Barthorpe, R. J., & Worden, K. (2014). Model validation and verification for structural 
dynamics: A review of metrics and methods. Mechanical Systems and Signal Processing, 
52–53, 326–344. https://doi.org/10.1016/j.ymssp.2014.07.002 
5. Bayarri, M. J., Berger, J. O., Paulo, R., Sacks, J., Cafeo, J. A., Cavendish, J., Lin, C. H., & 
Tu, J. (2012). A framework for validation of computer models. Technometrics, 54(4), 353–
369. https://doi.org/10.1080/00401706.2012.682745 
6. Bennett, J., & McDowell, D. L. (2015). Assessing predictive capability of crystal plasticity 
models using experimental benchmarks. Modelling and Simulation in Materials Science 
and Engineering, 23(6), 065004. https://doi.org/10.1088/0965-0393/23/6/065004 
7. Chen, W., Bagheri, S., & Papadopoulos, V . (2020). Validation metrics for nonlinear solid 
mechanics models using digital image correlation data. Engineering Computations, 37(6), 
2011–2032. https://doi.org/10.1108/EC-09-2019-0435 
8. Desceliers, C., Soize, C., & Ghanem, R. (2013). Identification of model and data 
uncertainties in experimental solid mechanics. Computer Methods in Applied Mechanics 
and Engineering, 264, 1–15. https://doi.org/10.1016/j.cma.2013.05.008 

---

## Page 11

9. Ewins, D. J., & Sainsbury, M. G. (2012). Model validation testing in structural dynamics: 
Lessons for solid mechanics. Philosophical Transactions of the Royal Society A , 
370(1975), 2790–2810. https://doi.org/10.1098/rsta.2011.0527 
10. Gendre, L., Allix, O., Gosselet, P., & Comte, F. (2013). Error estimation and model 
validation in computational solid mechanics. International Journal for Numerical Methods 
in Engineering, 96(7), 423–447. https://doi.org/10.1002/nme.4569 
11. Haddadi, H., Belhabib, S., & Benseddiq, N. (2017). Validation of constitutive models using 
heterogeneous strain fields measured by DIC. Experimental Mechanics, 57(2), 177–193. 
https://doi.org/10.1007/s11340-016-0211-7 
12. Hernandez, J. A., Oliver, J., & Huespe, A. E. (2014). Metrics for experimental –numerical 
comparison in failure mechanics. Engineering Fracture Mechanics , 126, 115 –129. 
https://doi.org/10.1016/j.engfracmech.2014.06.003 
13. Iaccarino, G., & Mani, A. (2012). Validation metrics for computational mechanics models. 
Annual Review of Fluid Mechanics , 44, 93 –116. https://doi.org/10.1146/annurev-fluid-
120710-101204 
14. Isenberg, J., & McDowell, D. L. (2013). Statistical measures for validating multiscale solid 
mechanics models. Acta Materialia , 61(8), 3151 –3162. 
https://doi.org/10.1016/j.actamat.2013.01.050 
15. Jiang, C., Chen, Z., & Huang, Z. (2021). Probabilistic validation metrics for solid 
mechanics models under experimental uncertainty. Reliability Engineering & System 
Safety, 210, 107512. https://doi.org/10.1016/j.ress.2021.107512 
16. Kirk, B. S., & Peterson, J. W. (2016). Verification, validation, and uncertainty 
quantification in solid mechanics simulations. Computers & Structures , 163, 1 –15. 
https://doi.org/10.1016/j.compstruc.2015.09.010 
17. Luo, Y ., & Wang, Z. (2018). Error indicators and validation metrics for experimental –
numerical comparison of stress fields. Measurement, 122, 226 –237. 
https://doi.org/10.1016/j.measurement.2018.03.018 
18. Oden, J. T., & Prudhomme, S. (2010). Goal-oriented error estimation and model validation 
in mechanics. International Journal for Numerical Methods in Engineering , 82(3), 354–
387. https://doi.org/10.1002/nme.2750 
19. Rebba, R., Mahadevan, S., & Huang, S. (2011). Validation and error estimation of 
computational models. Reliability Engineering & System Safety , 96(1), 136 –148. 
https://doi.org/10.1016/j.ress.2010.06.007 
20. Rougier, J., Goldstein, M., & House, L. (2013). Second-order exchangeability analysis for 
model validation. Journal of the American Statistical Association , 108(503), 852 –863. 
https://doi.org/10.1080/01621459.2013.802963 
21. Simoen, E., De Roeck, G., & Lombaert, G. (2015). Dealing with uncertainty in model 
updating for structural dynamics. Mechanical Systems and Signal Processing, 56–57, 123–
149. https://doi.org/10.1016/j.ymssp.2014.11.001 

---

## Page 12

22. Smith, R. C., & Murthy, S. (2016). Verification, validation, and uncertainty quantification 
in computational solid mechanics. Computers & Structures , 176, 52 –67. 
https://doi.org/10.1016/j.compstruc.2016.08.003 
23. Sun, W., & Li, S. (2019). Experimental–computational comparison metrics for validating 
large-deformation solid mechanics models. International Journal of Solids and Structures, 
163, 150–165. https://doi.org/10.1016/j.ijsolstr.2018.12.020 
24. Thacker, B. H., Doebling, S. W., Hemez, F. M., Anderson, M. C., Pepin, J. E., & Rodriguez, 
E. A. (2010). Concepts of model verification and validation. Los Alamos National 
Laboratory Report, LA-14167-MS, 1–94. https://doi.org/10.2172/968340 
25. Yaghoubi, A., & Wriggers, P. (2024). Model validation metrics for nonlinear experimental 
solid mechanics with full -field data. International Journal for Numerical Methods in 
Engineering, 125(5), 1165–1187. https://doi.org/10.1002/nme.7421 
 

---
