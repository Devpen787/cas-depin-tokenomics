# Corn_Murko_Podrzaj_2025_DePINsForSolarEnergy_ImpactOfNetworkDensityOnForecastingAccuracyAndEconomicViability_Forecasting.pdf

## Page 1

Academic Editors: Grzegorz Mentel
and Xin Zhao
Received: 30 October 2025
Revised: 26 November 2025
Accepted: 3 December 2025
Published: 10 December 2025
Citation: Corn, M.; Murko, A.;
Podržaj, P . Decentralized Physical
Infrastructure Networks (DePINs) for
Solar Energy: The Impact of Network
Density on Forecasting Accuracy and
Economic Viability. Forecasting 2025, 7,
77. https://doi.org/10.3390/
forecast7040077
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
Decentralized Physical Infrastructure Networks (DePINs) for
Solar Energy: The Impact of Network Density on Forecasting
Accuracy and Economic Viability
Marko Corn *,†
 , Anže Murko † and Primož Podržaj †
Faculty of Mechanical Engineering, University of Ljubljana, 1000 Ljubljana, Slovenia;
anze.murko@outlook.com (A.M.)
* Correspondence: marko.corn@fs.uni-lj.si
† These authors contributed equally to this work.
Highlights
What are the main findings?
• Increasing DePIN density significantly enhances solar forecasting accuracy, with optimal
gains achieved using data from the first 10–15 neighboring PV systems.
• These accuracy improvements translate directly into a substantial reduction in imbalance
costs for energy traders—by up to 45% compared to non-data-driven baselines.
What are the implications of the main findings?
• The results provide a blueprint for DePIN deployment, indicating that the optimal
cost–benefit balance is achieved by fostering dense local clusters within a 5–10 km radius.
• The quantified marginal benefits of data sharing offer a foundation for designing sustain-
able, tokenized incentive mechanisms that align individual participation with collective
value creation in decentralized energy markets.
Abstract
This study explores the role of decentralized physical infrastructure networks (DePINs) in
enhancing solar energy forecasting, focusing on how network density influences prediction
accuracy and economic viability. Using machine learning models applied to production
data from 47 residential PV systems in Utrecht, Netherlands, we developed a hierarchical
forecasting framework: Level 1 (clear-sky baseline without historical data), Level 2 (solo
forecasting using only local historical data), and Level 3 (networked forecasting incorpo-
rating data from neighboring installations). The results show that networked forecasting
substantially improves accuracy: under solo forecasting conditions (Level 2), the Ran-
dom Forests model reduces Mean Absolute Error (MAE) by 17% relative to the Level 1
baseline, and incorporating all available neighbors (Level 3) further reduces the MAE
by an additional 34% relative to Level 2, corresponding to a total improvement of 45%
compared with Level 1. The largest accuracy gains arise from the first 10–15 neighbors,
highlighting the dominant influence of local spatial correlations. These forecasting im-
provements translate into significant economic benefits. Imbalance costs decrease from
EUR 1618 at Level 1 to EUR 1339 at Level 2 and further to EUR 884 at Level 3, illustrating
the financial impact of both solo and networked data sharing. A marginal benefit analysis
reveals diminishing returns beyond approximately 10–15 neighbors, consistent with spatial
saturation effects within 5–10 km radii. These findings provide a quantitative foundation
for incentive mechanisms in DePIN ecosystems and demonstrate that privacy-preserving
data sharing mitigates data fragmentation, reduces imbalance costs for energy traders, and
Forecasting 2025, 7, 77 https://doi.org/10.3390/forecast7040077

---

## Page 2

Forecasting 2025, 7, 77 2 of 30
creates new revenue opportunities for participants, thereby supporting the development of
decentralized energy markets.
Keywords: DePIN; solar energy; machine learning; forecasting; network density; economic
impact; data silos
1. Introduction
The global transition toward renewable energy sources has accelerated in recent years,
driven by the urgent need to mitigate climate change and enhance energy security [ 1,2].
Among various renewable options, solar power has emerged as a particularly attractive
choice due to its declining costs, scalability, and widespread resource availability [ 3].
Nevertheless, the integration of solar power into conventional grids presents significant
challenges related to its inherent variability and intermittency. Fluctuations in solar ir-
radiance due to weather conditions, seasonal patterns, and diurnal cycles can introduce
substantial uncertainty into power generation [4,5].
Accurate forecasting of solar power output is crucial for minimizing the economic
and technical issues associated with this variability. When forecasts are inaccurate, energy
providers often face imbalance costs as they must rely on expensive backup power or bal-
ancing services to meet contractual obligations [6]. This challenge becomes more pressing
as the share of solar power in the energy mix grows, increasing the grid’s vulnerability to
forecast errors [7,8].
Despite widespread smart meter deployment, operational PV data remain fragmented
across balance groups: BRPs do not routinely access meter-level production from other
BRPs’ portfolios due to confidentiality, competition, and governance constraints embedded
in current market roles and data-access regimes [9–13]. Public EU data services focus on
aggregated market information rather than cross-party, meter-level operational streams
needed for localized spatio-temporal PV nowcasting (e.g., the ENTSO-E Transparency
Platform) [14].
A promising solution to address data fragmentation and improve solar forecasting
accuracy lies in decentralized physical infrastructure networks (DePINs), which offer a funda-
mentally different, user-driven approach to decentralized data collection [15]. Rather than
relying on top-down systemic changes or limited regional data sources, a DePIN empowers
individual photovoltaic (PV) owners—prosumers—to voluntarily share localized production
data via tokenized incentive mechanisms and blockchain-based platforms [16–21]. This cre-
ates a bottom-up, privacy-preserving data commons that bypasses traditional institutional
barriers [20,22,23], generating cross-balance-group operational streams needed for accurate
nowcasting while maintaining commercial confidentiality . By fostering a dense, geographi-
cally distributed array of solar nodes, the DePIN provides granular insights into fluctuating
weather conditions and real-time nowcasting, thereby enhancing prediction models with ad-
vanced machine learning integration [5,24]. This facilitates direct participation in peer-to-peer
data and energy markets, with automated mechanisms incentivizing contributors, unlocking
novel economic opportunities in the solar sector, and aligning with evolving EU data-sharing
frameworks [9,10].
Moreover, although decentralized energy systems have garnered attention for fa-
cilitating peer-to-peer trading and grid flexibility, the existing literature often examines
market design, transaction mechanisms, or blockchain frameworks without systematically
quantifying the direct relationship between network density, forecast accuracy, and eco-
nomic returns [20]. Consequently, there is a pressing need for an integrated study that

---

## Page 3

Forecasting 2025, 7, 77 3 of 30
links these three components—network density, solar forecasting accuracy, and financial
viability—within a decentralized physical infrastructure network (DePIN) setting.
This study complements three major strands of existing research. First, most prior
work in spatial PV forecasting has relied on satellite-derived irradiance fields, reanalysis
datasets, or mesoscale numerical weather prediction models. Studies using dense networks
of physical PV installations are far less common, and analyses quantifying how forecast
accuracy scales with the number of proximate sensors are particularly limited. By using real
production measurements from closely spaced PV systems in a single, well-instrumented
region, spatial correlation and network-density effects were examined in this study at
a micro-climatological scale that is rarely addressed in the previous literature. Second,
while sensor-density research in temperature, precipitation, and air-quality monitoring
consistently shows diminishing returns beyond several kilometers, PV forecasting is gov-
erned by much shorter decorrelation lengths due to small-scale cloud dynamics. Our
results indicate a higher density threshold (approximately 10–15 neighbors) for saturation,
aligning with findings from high-resolution cloud-motion studies but applied here to oper-
ational PV systems rather than atmospheric proxies. Third, our contribution is empirical
and operational relative to the DePIN literature, which has predominantly focused on
token design, governance structures, incentive mechanisms, and interoperability. We do
not introduce new blockchain mechanisms; instead, we evaluate how decentralized data
availability influences forecasting accuracy and imbalance-cost proxies. Thus, the work
positions the DePIN primarily as a data-access layer that enables improved spatial fore-
casting, rather than as a conceptual advance in decentralized infrastructure design itself.
These clarifications provide a more precise positioning of the manuscript and delineate its
contributions within the broader contexts of spatial forecasting, sensor-density research,
and decentralized data-sharing architectures.
We provide three key advancements:
• Network density vs. forecast accuracy: An empirical, machine-learning-based analy-
sis that quantifies how forecast performance scales with the number of neighboring
PV installations in a single, well-instrumented region.
• Cost-saving analysis: A simplified imbalance-cost proxy that maps observed MAE
reductions into monetary terms using real portfolio energy volumes and a represen-
tative Dutch imbalance price, providing an interpretable link between forecasting
improvements and expected financial impact for a BRP .
• DePIN-oriented value allocation: A marginal-benefit framework that illustrates
how the resulting imbalance-cost reductions could, in principle, fund data-sharing
incentives in DePIN-like architectures, without specifying a concrete tokenomics or
governance design.
By bridging the technical and economic dimensions of solar forecasting, our study
provides valuable insights into how dense, decentralized sensor networks can facilitate
more accurate prediction, reduce operational costs, and create new revenue streams in
emerging energy markets.
The remainder of this paper is organized as follows: Section 2 reviews the relevant
literature on solar forecasting methods, the DePIN paradigm, and the economic implications
of accurate predictions. Section 3 outlines our dataset, forecasting methodology, and
the economic model for DePIN profitability. Section 4 presents the results, highlighting
improvements in forecast accuracy and associated cost savings. Section 5 discusses key
findings and practical implications, followed by Section 6, which concludes with a summary
of contributions and future research directions.

---

## Page 4

Forecasting 2025, 7, 77 4 of 30
2. Literature Review
2.1. Solar Forecasting Methods and Networked Systems
Solar photovoltaic (PV) power forecasting has become an increasingly important research
topic as the share of solar generation in modern power systems continues to rise [1,3]. Accu-
rate forecasts reduce imbalance costs and improve grid stability by mitigating the uncertainty
caused by rapidly changing solar irradiance [6,7]. Over the past decade, three major method-
ological directions have emerged in the forecasting literature: physical models, statistical
models, and machine learning approaches.
Physical models rely primarily on numerical weather prediction (NWP) or satellite-
derived irradiance fields to estimate incoming solar radiation. These irradiance estimates
are then transformed into power using PV system models that incorporate module char-
acteristics, array geometry, and inverter behavior. Although such methods offer physical
interpretability and broad spatial coverage, their resolution is often too coarse to capture
localized cloud effects, and their performance depends heavily on the accuracy of both the
weather model and PV system parameters [7,8].
Statistical forecasting approaches represent a second major research line. Classical
models such as ARIMA, SARIMA, and time-series regression techniques rely on historical
PV or irradiance data to extract temporal correlations, seasonality patterns, and longer-term
trends [25]. These models are computationally efficient and require fewer input variables
compared with physical models. However, they tend to struggle under highly dynamic
weather conditions or when changes in irradiance occur at spatial and temporal scales
smaller than their modeling assumptions.
The third major class of forecasting techniques consists of machine learning and deep
learning models. Artificial neural networks (ANNs), support vector machines (SVMs),
Random Forests, and especially deep architectures such as Long Short-Term Memory
(LSTM) networks have demonstrated strong performance in capturing nonlinear and
high-dimensional relationships in PV generation data [ 26–28]. More complex hybrid
models combine data-driven learning with physical constraints, achieving strong general-
ization and improved robustness across varying locations and weather regimes [29]. Mellit
et al. [24] provided a detailed overview of the evolution of these techniques, emphasizing
the growing importance of hybrid frameworks that leverage both physical knowledge and
data-driven adaptability.
Despite the extensive literature, most forecasting models historically rely on data
collected at a single site. Such approaches capture only local irradiance conditions and
therefore fail to account for spatial changes in cloud cover and microclimatic effects [ 7].
In contrast, networked forecasting systems integrate measurements from geographically
distributed PV installations, which allows models to exploit spatial correlations and antici-
pate cloud movement more effectively. Dense sensor networks capture fine-scale irradiance
variations and improve real-time awareness of cloud dynamics. Studies such as those of
Graabak et al. [ 30] and Droste et al. [ 31] showed that distributed datasets significantly
enhance the spatial resolution of solar forecasts, while Hintz et al. [32] reported reductions
in variability and improved robustness. More recent advances in artificial intelligence,
including spatio-temporal graph neural networks [ 28,33], exploit these dense data net-
works to achieve significant improvements in short-term solar forecasting, particularly
over horizons of minutes to hours.
Overall, the transition from single-site approaches to networked, spatially informed
forecasting frameworks marks a major step forward in improving forecast accuracy, relia-
bility, and robustness for distributed PV systems.

---

## Page 5

Forecasting 2025, 7, 77 5 of 30
2.2. Network Density and Forecasting Accuracy: Insights from Cross-Domain Applications
The value of dense sensor networks is not unique to solar forecasting; it is a consistent
finding across multiple scientific and engineering domains. In meteorology, for example,
increasing observation density enhances the ability to capture fine-scale spatial and tem-
poral weather patterns. Droste et al. [ 31] showed that urban air temperature retrieval
in São Paulo improves significantly when more than 700 smartphone-based temperature
sensors are available, while Meier et al. [ 34] demonstrated that dense citizen weather
station networks in Berlin provide far more detailed insights into urban heat island patterns
than traditional meteorological stations. Similarly, Hintz et al. [32] demonstrated that even
noisy smartphone pressure measurements can meaningfully improve atmospheric analyses
when assimilated into numerical weather prediction models, aligning with earlier work by
Madaus and Mass [35].
Transportation forecasting also benefits from dense sensor networks. Gagliardi et al. [36]
show that carefully optimized sensor placement enables more accurate reconstruction of traffic
flows and pollutant emissions. IoT-enabled smart city systems, described by Harmon [37], rely
on large volumes of real-time measurements to predict and manage traffic conditions more
effectively . Deep learning models, such as those studied by Ma et al. [38] and Lv et al. [39],
depend on high-frequency , high-density data to capture nonlinear dynamics in traffic behavior
and to produce stable, accurate predictions.
Agricultural forecasting further reinforces these insights. Dense multisensor remote-
sensing networks enable predictive models to capture subtle spatial variations in crop
conditions. Adsuara et al. [40] showed that nonlinear distribution regression techniques
benefit from grouped, spatially diverse observations, while Mateo-Sanchis et al. [ 41]
demonstrated that combining optical and microwave remote-sensing features substantially
improves crop yield prediction. Zhao et al. [42] found that soil nutrient forecasting accuracy
increases when machine learning models are trained on densely sampled multisensor
datasets, and Soussi et al. [ 43] discussed how smart agriculture relies on dense sensor
networks to produce actionable “smart data.”
Across these domains, the conclusion is consistent: higher sensor network density
systematically improves forecasting accuracy by providing richer spatial and temporal in-
formation. These cross-disciplinary findings strongly support the hypothesis that increased
PV network density can similarly enhance solar forecast performance.
2.3. Decentralized Physical Infrastructure Networks (DePINs)
Decentralized physical infrastructure networks (DePINs) refer to blockchain-coordinated
systems in which geographically distributed physical assets, such as sensors, energy devices,
or communication nodes, are owned and operated by independent participants rather than
by a central authority . A DePIN architecture typically consists of three core layers: (i) a
distributed hardware layer contributed by many small-scale operators, (ii) a blockchain-based
coordination and verification layer that records contributions and enforces transparent rules,
and (iii) a token-based incentive mechanism that rewards participants for providing reliable
physical services. This conceptualization is aligned with recent taxonomies and architectural
analyses of DePIN systems [15,44]. Furthermore, token-based coordination of distributed
physical infrastructure has been shown to enable efficient, trust-minimized collaboration
across large-scale networks, distinguishing DePINs from traditional decentralized IoT or
peer-to-peer energy platforms [45].
While DePINs share certain characteristics with adjacent decentralized frameworks,
they differ in several important ways. Peer-to-peer (P2P) energy trading platforms primarily
enable bilateral electricity exchanges between prosumers [46,47], but they do not coordinate
or verify large-scale deployment of distributed physical assets. Decentralized IoT and sensor-

---

## Page 6

Forecasting 2025, 7, 77 6 of 30
sharing networks facilitate data collection across many devices [48,49], yet they typically
rely on centralized cloud platforms for coordination and lack tokenized, on-chain incentive
mechanisms. Tokenized real-world asset (RWA) models focus on representing physical assets
as digital tokens for ownership and settlement purposes [50,51], but they do not govern how
the physical hardware contributes operationally to a network. In contrast, DePINs integrate
distributed physical infrastructure, blockchain-based verification, and token-driven incentives
into a unified architecture designed specifically for coordinating geographically dispersed
hardware at scale [15,44]. This positions DePINs as a distinct category of decentralized system,
extending beyond data-only or trading-focused architectures.
Decentralized physical infrastructure networks (DePINs) build on these capabilities to
create distributed systems governed by participants rather than centralized operators [15,44].
By linking physical assets to blockchain-based incentives, DePINs coordinate thousands
of small-scale contributors who provide data, computing, or physical services. Smart con-
tracts automate payments, verify contributions, and ensure transparent accounting, reducing
reliance on trust and central intermediaries.
Real-world examples illustrate how DePINs deploy large-scale sensor networks. Helium
rewards participants for deploying wireless hotspots that provide IoT connectivity [52], while
HiveMapper creates up-to-date global maps by incentivizing users to contribute dashcam
imagery [53]. In the energy sector, emerging initiatives such as Arkreen aim to aggregate
distributed solar production and facilitate peer-to-peer energy trading, enabling new moneti-
zation pathways for prosumers [54]. These systems demonstrate that decentralized partici-
pation can generate high-density , high-quality datasets while distributing value fairly across
the network.
2.4. Economic Implications of Forecasting Accuracy
Forecast accuracy directly affects financial performance in modern electricity markets.
Operators typically purchase and schedule energy in advance; deviations from scheduled
production create imbalances that must be corrected in real time [55]. Positive imbalances
(excess generation) and negative imbalances (deficits) both incur financial penalties, and
the severity of these penalties depends on timing, regional market structure, and TSO
intervention policies. Kraas et al. [56] showed that advanced forecasting systems reduce the
magnitude of such imbalances, while Brancucci Martinez-Anido et al. [57] demonstrated
that improved day-ahead forecasting lowers overall generation costs by reducing the need
for expensive reserve activation. Goodarzi et al. [58] further highlighted that forecast errors
not only increase imbalance volumes but also elevate real-time spot prices, exacerbating
market volatility.
Additional research quantifies the broader economic value of forecasting improvements.
Kaur et al. [59] showed that more accurate solar forecasts reduce the burden on flexibility
reserves, while Jonsson et al. [60] analyzed how forecast error drives electricity price volatility .
Gonzalez-Aparicio and Zucker [61] demonstrate that forecast uncertainty significantly in-
creases integration costs in Spain, and Pierro et al. [62] highlighted how even small reductions
in error can materially reduce imbalance penalties. Forecast accuracy also interacts with
market design: van der V een and Hakvoort [63] show that imbalance settlement schemes can
either amplify or mitigate financial exposure, and Cui et al. [64] argued that increased data
availability reduces error costs within game-theoretic market frameworks.
A growing body of work also emphasizes the role of networked and high-density
data sources in improving both technical and economic performance. Perez et al. [ 55],
Pierro et al. [62], and Lorenz et al. [8] demonstrated that forecasts improve when geograph-
ically distributed data are incorporated. More recent studies show that richer datasets
not only improve accuracy but also reduce financial exposure: Visser et al. [ 65,66] and

---

## Page 7

Forecasting 2025, 7, 77 7 of 30
Klyve et al. [67] quantified how distributed PV data networks lower imbalance settlement
costs. Complementary strategies, such as the joint scheduling methods proposed by Das
et al. [68] and the intra-hour imbalance prediction tools of Salem et al. [69], demonstrate
additional pathways for cost reduction. Market design analysis by Moon et al. [ 70] further
suggests that appropriate settlement rules can magnify the economic benefits of improved
forecasting accuracy.
Collectively, these studies highlight the strong economic motivation for improving
solar forecasting accuracy. Investments in dense sensor networks and advanced forecasting
models reduce imbalance penalties, stabilize market operations, and support more efficient
integration of renewable energy. These findings provide a compelling argument for the role
of decentralized physical infrastructure networks (DePINs), which naturally create dense
data ecosystems that improve both technical forecasting performance and downstream
financial outcomes.
3. Research Methodology
3.1. Data Collection
Dataset Overview
The electricity production data used in this study were obtained from the Zenodo
repository [66]. This dataset comprises one-minute resolution measurements collected
over four years from 175 residential solar power systems in the Utrecht region of the
Netherlands. In addition to the power production time series, the repository provides
important metadata for each installation, including a unique identifier (ID); the start
and end times of measurements; estimated capacities for both direct current (DC) and
alternating current (AC); and information on the system’s tilt, azimuth, annual yield, and
geographic location.
For forecasting purposes, only the AC power output measurements were used. Initially ,
the metadata were filtered based on the measurement period, location, and completeness of
the data. We retained only those installations with continuous data records over the entire four-
year period. However, upon review, it was determined that all systems experienced extended
periods of missing data in 2016; consequently , data from 2016 were excluded from further
analysis. In addition, installations lacking location information or with more than 20% missing
values were removed. This filtering process resulted in a final sample of 47 solar power
systems. Due to computational constraints, our forecasting experiments were conducted on a
subset of data spanning nine months (from January 2017 to September 2017), which, given the
one-minute resolution, amounts to 348,481 data points.
3.2. Data Preprocessing
3.2.1. Outliers Removal
Improving data quality is critical for effective forecasting. Extreme outlier values can
distort underlying patterns and reduce model performance [71]. To mitigate this issue, we
applied a Z-test for outlier detection. The Z-value for each data point in a given time series
was computed using
zi(t) = pi(t) − pi
s ,
where pi(t) represents the power output of the ith installation at time t, pi is the mean
output for that system, and s is the standard deviation of the time series. Data points with
Z-values exceeding a threshold (set to zthreshold = 3) were removed from the dataset.

---

## Page 8

Forecasting 2025, 7, 77 8 of 30
3.2.2. Handling Missing Data
The dataset still contained missing values despite initial filtering. Given the sensitivity
of forecasting models to missing information, it was essential to fill these gaps in a princi-
pled way. Rather than discarding incomplete records, we employed the Multivariate Impu-
tation by Chained Equations (MICE) method implemented via the IterativeImputer()
function from scikit-learn [72].
In this multivariate setting, each PV installation’s time series was imputed using
the contemporaneous observations of all other installations. For each timestamp t, the
missing value pi(t) was estimated from a regression model using the remaining systems as
predictors represented by Equation (1):
pi(t) = β0,i +
k
∑
j̸=i
βj pj(t), (1)
where β0,i is the intercept, βj are the regression coefficients, and k is the total number of
installations considered. This formulation ensures that imputation relies exclusively on
same-timestamp information from other PV systems, thereby preventing the use of future
values and avoiding information leakage into subsequent forecasting steps.
The imputation procedure was executed iteratively: for each series, the regression
model was first fitted on all available (non-missing) observations, missing entries were
updated, and the process cycled through all variables until convergence. No temporal
lags were included in the imputation model as lagged structures are explicitly captured
later during feature construction for forecasting. This choice avoids introducing artificial
temporal autocorrelation that may arise when temporal predictors are included directly in
the imputation step. Visual inspection of imputed segments and comparison with neigh-
boring installations confirmed that the method preserved realistic short-term variability
without oversmoothing. All imputations were performed on the original one-minute data
prior to resampling to fifteen-minute resolution, ensuring consistency and minimizing the
influence of high-frequency missingness on later aggregation steps.
3.2.3. Removal of Negative and Non-Operational Values
Since negative power values do not make sense in the context of solar energy pro-
duction, any negative readings were set to zero. Measurements recorded during the
non-operational period (between 22:00 and 05:00) were also set to zero as no production
occurs during these hours.
3.2.4. Resampling
After filling missing values and removing erroneous readings, we resampled the
dataset originally recorded at a 1-min resolution to a 15-min resolution by aggregating the
data. This preprocessing step reduced computational complexity during model training
and mitigated the impact of extreme deviations in the original measurements. Similar to
the approach outlined by Visser et al. [66], the resampling process reduced the dataset from
348,481 to 23,233 data points.
3.2.5. Normalization
To further improve the model training efficiency, each time series was normalized.
We applied min–max normalization to scale the data into a range between 0 and 1 using
the MinMaxScaler() function from scikit-learn [72]. This transformation is expressed in
Equation (2):

---

## Page 9

Forecasting 2025, 7, 77 9 of 30
pi,norm(t) = pi(t)
pi,max
, (2)
where pi(t) is the original value and pi,max is the maximum observed value for that series.
3.3. Input Feature Construction
Prior to applying the forecasting models, we constructed input features using lagged
variables to capture temporal patterns in the data. Lagged variables are created by shifting
past values of the normalized power output forward in time, enabling the models to account
for seasonality, trends, and other time-dependent dynamics. For each PV installation, the
lagged variables b(t)
i are defined as
b(t)
i = p(t−τ)
i,norm,
where p(t)
i,norm is the preprocessed and normalized power output at time t, and τ is the
lag parameter. Given that this study focuses on short-term forecasting with a 1-h horizon
(tnap = 1 h = 60 min) and the data is resampled to a 15-min resolution, the lag parameter is
calculated as
τ = tnap
15 min = 4.
The value of τ indicates that each lagged variable incorporates the fourth historical
value preceding the current time step being predicted. This results in a vector of lagged
features for each installation:
bi =


b(t)
i
b(t+1)
i
b(t+2)
i
...
b(t+n)
i


.
These lagged features form the basis for the input data in Levels 2 and 3 of the
forecasting model, enhancing the ability to predict solar power output 1 h ahead while
aligning with the temporal resolution of the dataset. This specification is crucial as shorter
forecasting horizons can significantly influence imbalance costs in energy markets, where
penalties often escalate with reduced prediction lead times.
3.4. Forecasting Model
We propose a three-tier forecasting model to systematically evaluate the impact of
historical data and network density on solar power prediction accuracy: Level 1 (Solo, No
Data) baseline forecasting without historical patterns or network data, Level 2 (Solo with
History) individual forecasting using only local historical data, and Level 3 (Networked)
collaborative forecasting incorporating neighboring installation data.
This hierarchical approach allows us to isolate and quantify the incremental benefits
of historical data utilization and network effects.
3.4.1. Level 1: Solo Forecasting (No Historical Data)
The baseline level represents the simplest forecasting scenario, where predictions are
made without access to historical patterns or neighboring data. Specifically, we employ
the Haurwitz clear-sky Global Horizontal Irradiance (GHI) model [73], which calculates

---

## Page 10

Forecasting 2025, 7, 77 10 of 30
solar irradiance using only astronomical inputs such as the solar zenith angle. The model
computes the clear-sky GHI, as shown in Equation (3):
GHIcs = 1098 · exp

−0.059/ max(µ, 10−6)

· µ, (3)
where µ = cos(θz) is the cosine of the solar zenith angleθz, clamped to non-negative values,
and GHI is set to zero when µ ≤ 0. This irradiance is then converted to estimated PV power
output using system-specific metadata, including tilt, azimuth, and efficiency factors. The
solar position is determined via a vectorized NOAA-style algorithm based on date and
time components, incorporating the equation of time and solar declination for accuracy.
This approach serves as our performance baseline, representing scenarios with minimal
data availability.
3.4.2. Level 2: Solo Forecasting with Historical Data
Level 2 uses only the target installation’s own historical production to capture temporal
regularities and site-specific behavior, without any neighbor information. As a simple and
transparent solo benchmark, we use the day-profile averaging model:
ˆpL2i (t) = 1
d
d
∑
k=1
b(t−24 τ (k−1))
i , (4)
where d is the number of past days included and τ is the time-resolution factor.
3.4.3. Level 3: Networked Forecasting
Level 3 augments solo forecasting by incorporating information from neighboring
PV installations and explicitly modeling network density. The core idea is that nearby
systems experience related cloud dynamics and microclimate effects; leveraging these
spatial correlations improves short-term predictions for a target unit.
Spatial Definition of Network Density
We define network density as the number of neighboring PV installations, the data
of which are integrated into the forecast for unit i. Rather than fixing a geographic ra-
dius (which can produce uneven neighbor counts), we rank all candidates by geographic
distance and select the top n neighbors, as shown in Equation (5):
mi = f (i, n), (5)
where mi is the index set of the n closest neighbors for installation i and n ∈ N directly
controls density. This number-based definition makes it straightforward to study accuracy
as a function of n and to compare sites with different local deployment patterns. Figure 1
illustrates how increasing n expands the spatial footprint captured by the forecaster, thereby
enriching the representation of cloud motion and local variability.

---

## Page 11

Forecasting 2025, 7, 77 11 of 30
Figure 1. Effect of increasing the inclusion radius on the number of neighboring PV installations
considered for forecasting (example: installation ID010).
Empirical Justification of Geographic Neighbor Selection
To validate the use of geographical proximity as a basis for selecting neighbors, we
conducted a correlation–distance analysis using the measured AC power output of all PV
systems. We computed the pairwise Pearson correlation of the measured time series of each of
the 1081 installation pairs and related it to their geographical separation using the Haversine
formula. In Figure 2, the results display a clear decay of PV output similarity with distance:
nearby installations (within 5–10 km) exhibit very high correlations(r ≈ 0.90–0.97), while
similarity gradually decreases beyond approximately 15–20 km. The relationship is strongly
monotonic (Spearman ρ = −0.512, p < 10−16), confirming that geographic distance is a
reliable proxy for shared irradiance dynamics. This provides an empirical foundation for the
top-k nearest-neighbor selection used in Level 3.
0 10 20 30 40 50 60
Distance between installations (km)
0.55
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0.95
1
Pearson correlation (measured PV output)
Figure 2. Pearson correlation of measured PV output versus geographical distance.

---

## Page 12

Forecasting 2025, 7, 77 12 of 30
Alternative Spatial Neighbor-Selection Approaches
While geographic proximity provides a strong and empirically validated baseline for
identifying informative neighbors, we acknowledge that more advanced spatial-selection
strategies could further enhance networked forecasting. Possible alternatives include
correlation-based neighbor selection, in which units are chosen based on historical produc-
tion similarity rather than distance; cloud-motion-aware dynamic neighborhoods derived
from satellite or sky-imager nowcasting; spatial interpolation and kriging methods that es-
timate continuous irradiance fields; and graph-based learning approaches where neighbor
relationships are learned endogenously by the model. These techniques typically require
additional data sources or more complex architectures and are therefore beyond the scope
of the present study, but they represent promising directions for future work.
Feature Construction from Neighbors
After selecting mi, we form a neighbor feature block Bi(n) that stacks the lagged
production histories of the n neighbors over the same window used for the target:
Bi(n) =
h
bmi,1 bmi,2 . . . bmi,n
i
, (6)
where each columnbmi,k contains the lagged power values of neighbormi,k over t−L:t−1.
The complete Level 3 input concatenates the target’s own historybi with the neighbor block:
Xi(n) =
"
bi
Bi(n)
#
. (7)
This design captures both temporal structure (lags) and spatial context (neighbors). If de-
sired, one may append simple spatial summaries (e.g., neighbor mean, range, or dispersion)
or distance weights, but these are not required by the core formulation.
Because the input Xi(n) explicitly depends on the number of neighbors, the forecast
accuracy is directly linked to network density n, as shown in Equation (8):
ˆpL3i (t) = F(Xi(n); θ), (8)
where ˆpi(t) is the predicted power output for installationi at time t, F is the chosen learning
algorithm, and θ is the learned parameters.
Training Structure Across Installations
All forecasting models in this study are trained on an installation-by-installation
basis. For each PV unit i, we constructed a dedicated training dataset derived from its
own production history and the lagged histories of its n nearest neighbors, as defined in
Equations (5)–(7). Because the set of neighbors mi and the corresponding input matrix
Xi(n) differ across installations, a centralized training strategy would not be appropriate:
different units do not share identical feature structures. Likewise, regional grouping was
not used, since the spatial correlations captured by the Level 3 design depend specifically
on each unit’s local neighborhood rather than on administrative or geographic region
boundaries. Each installation therefore receives its own trained model Fi(θi), ensuring that
forecasts are tailored to its local microclimatic and network context.
Including neighbors provides two complementary benefits: (i) anticipation of local
changes as upwind neighbors partially reveal imminent cloud passages and (ii) noise reduc-
tion, since multiple sources help distinguish true irradiance shifts from sensor anomalies. As
n increases, accuracy typically improves rapidly at first (the closest neighbors are most infor-
mative), then saturates as marginal neighbors add redundant or weakly correlated signals.

---

## Page 13

Forecasting 2025, 7, 77 13 of 30
Justification of Forecasting Model Selection
The learning algorithms used in this study—Random Forests (RFs), Extreme Gradient
Boosting (XGB), Support Vector Regression (SVR), and Multi-Layer Perceptron (MLP)—
were chosen because they represent the four most widely adopted and consistently high-
performing model families in short-term solar power forecasting. Ensemble tree methods
such as RF and XGB have been repeatedly shown to handle nonlinear irradiance–power
relationships, heterogeneous feature sets, and noisy measurements with strong robust-
ness [74,75]. Kernel-based models such as SVR are well established in irradiance and PV
forecasting due to their ability to model complex nonlinear patterns in high-dimensional
spaces using appropriate kernel functions [ 76,77]. Neural approaches such as MLPs re-
main a standard baseline in PV forecasting and achieve strong performance when learning
smooth nonlinear mappings from past observations to future power output [ 26]. Using
these four model classes enables a comparison across complementary learning paradigms
(ensembles, boosting, kernel methods, and neural networks), all of which have demon-
strated reliability and competitive accuracy in prior solar forecasting studies.
3.5. Hyperparameter Tuning and Configuration
To ensure optimal performance across all machine learning models, we implemented a
systematic hyperparameter optimization process using randomized search with 5-fold time-
series cross-validation. This approach preserved temporal dependencies while identifying
robust parameter configurations. We tuned the number of estimators, maximum depth, and
regularization parameters of the tree-based ensembles to balance model complexity and
generalization capability. The Multilayer Perceptron architectures were optimized through
variations in hidden layers, neuron counts, and activation functions, while Support Vector
Regression focused on kernel parameters and penalty terms. All models shared consistent
training configurations, including temporal splitting to maintain chronological integrity
and early stopping to prevent overfitting. The complete hyperparameter search spaces for
each algorithm are detailed in Table 1.
Table 1. Hyperparameter configurations and search ranges for machine learning models.
Model RF (Random Forests)
Hyperparameters n_estimators, max_depth, min_samples_split, min_samples_leaf, bootstrap, max_features
Search range 100–500, 3–20, 2–10, 1–4, {True,False}, {sqrt,log2}
Model XGB (XGBoost)
Hyperparameters learning_rate, n_estimators, max_depth, subsample, colsample_bytree, reg_alpha,
reg_lambda
Search range 0.01–0.3, 100–500, 3–15, 0.7–1.0, 0.7–1.0, 0–1, 0–1
Model SVR
Hyperparameters C, gamma, kernel, epsilon
Search range 0.1–10, {scale,auto}, {rbf,linear}, 0.01–0.1
Model MLP
Hyperparameters hidden_layer_sizes, activation, solver, alpha, learning_rate_init, early_stopping
Search range {(32,), (64,), (32,32), (64,64)}, {relu,tanh}, adam, 0.0001–0.1, 0.001–0.01, {True,False}
Training config. TimeSeriesSplit(n_splits = 5), random_state = 42, n_jobs = −1, scoring = MAE, n_iter = 50
The hyperparameter tuning process employed randomized search with 50 iterations
per model, optimizing for negative Mean Absolute Error to align with our primary evalua-
tion metric. This comprehensive approach ensured that performance comparisons across

---

## Page 14

Forecasting 2025, 7, 77 14 of 30
forecasting levels reflected model capabilities rather than suboptimal configurations, pro-
viding a fair basis for evaluating the impact of network density on prediction accuracy.
Temporal Splitting and Prevention of Information Leakage
All hyperparameter optimization and model training procedures were performed
using strictly time-aware data splits to ensure chronological integrity. We employed scikit-
learn’sTimeSeriesSplit for all models, which guarantees that training folds contain only
past observations and validation folds contain strictly future observations. This prevents
any leakage of future information into the learning process.
To avoid feature leakage through preprocessing, normalization and imputation were
performed after each time split, using statistics computed only on the training portion of
each fold. Forecasting models therefore never had access to future values, future-derived
normalization parameters, or future lagged features during training. The same procedure
was applied consistently across Level 2 and Level 3 experiments to ensure comparability.
3.6. Statistical Significance Testing
We performed a paired Wilcoxon signed-rank test on the per-installation MAE values
to verify that the improvement from solo forecasting (Level 2) to networked forecasting
(Level 3) is statistically robust. The test compares matched errors from the same PV units
under Level 2 and Level 3 conditions and is appropriate here because MAE distributions
are non-normal and the samples are paired across installations. We evaluated the one-sided
hypothesis that Level 3 achieves lower MAE than Level 2.
3.7. Economic Model
3.7.1. Imbalance Costs
The economic impact was evaluated from the perspective of Balance Responsible
Parties (BRPs), focusing on total imbalance costs.
In liberalized electricity markets, each Balance Responsible Party (BRP)—typically a
utility or trader—must keep its portfolio’s production and consumption in line with the
schedule it submits. If the actual production–consumption balance in a settlement period
deviates from the scheduled balance, the Transmission System Operator (TSO) restores system
balance in real time and settles the difference with the BRP as an imbalance cost [63].
While imbalance pricing can be asymmetric in practice, we employed a simplified
model using a single, representative average imbalance price ¯m (EUR/MWh). This ap-
proach is suitable for estimating the expected financial impact of forecast errors. The total
imbalance cost C (EUR) over a given horizon can be approximated as the product of this
price, the scale of the forecast error, and the relevant energy volume. The Mean Absolute
Error (MAE) is used as the error metric, as shown in Equation (9):
C ≈ ¯m · MAE · E, (9)
where E is the total energy volume (MWh). In this framing, any reduction inMAE translates
directly into lower imbalance costs, creating a direct and measurable monetary value for
improved forecasting.
We can define the imbalance costs for each of our three forecasting levels based on the
respective Mean Absolute Error (MAE) achieved. Specifically, the imbalance cost for Level
1 (solo forecasting without historical data) is approximated as CL1 ≈ ¯m · MAEL1 · E, where
MAEL1 reflects the baseline error from the clear-sky model. For Level 2 (solo forecasting
with historical data), the cost is CL2 ≈ ¯m · MAEL2 · E, capturing improvements from
incorporating local temporal patterns. Finally, for Level 3 (networked forecasting), the cost
becomes CL3 ≈ ¯m · MAEL3 · E, which benefits from spatial correlations and thus typically

---

## Page 15

Forecasting 2025, 7, 77 15 of 30
yields the lowest MAE. This formulation enables a direct comparison of economic savings
across levels, quantifying how incremental enhancements in forecast accuracy—driven by
historical data and network density—translate into reduced imbalance penalties for BRPs.
In the DePIN context, the economic improvements observed at Level 2 are enabled by
the decentralized network’s ability to aggregate and make historical data readily available
for individual installations, facilitating portfolio-wide accuracy gains through incentivized
data contributions without requiring cross-sharing. At Level 3, further enhancements arise
not only from addressing the data silo problem inherent in traditional BRP structures—
where confidentiality and competition limit access to cross-portfolio operational data—but
also from enhancing predictions within a single BRP’s own PV portfolio through the integra-
tion of spatial forecasting methods if not already employed. By enabling privacy-preserving
neighbor-based sharing, DePINs reduce these barriers, unlocking spatial correlations that
drive down forecast errors and imbalance costs.
3.7.2. Marginal Benefit Analysis
We introduce a marginal benefit analysis to quantify the economic value of increasing
data access within the DePIN network. The marginal benefit of providing additional
neighbor data access is defined as the reduction in total imbalance costs attributable to each
additional data connection made available to participants.
The marginal benefit for increasing from k − 1 to k neighbors per PV system is calcu-
lated as shown in Equation (10):
MBk = Ck−1 − Ck
k − (k − 1) = Ck−1 − Ck (10)
where MBk is the marginal benefit per additional data connection (EUR), Ck is the total
imbalance cost with k neighbors accessible per PV system (EUR), and Ck−1 is the total
imbalance cost with k − 1 neighbors accessible per PV system (EUR).
This analysis was conducted within the fixed network of 47 PV systems, where we
varied the number of neighboring systems for which the data could be accessed by each
participant (from 0 to 46 neighbors). The approach quantifies how increasing data sharing
density, rather than network size, contributes to collective forecasting improvements and
enables the design of economically sustainable incentive structures in DePIN networks.
4. Results
This section presents the findings from our experiments, focusing on the impact of par-
ticipation levels in the DePIN on forecasting accuracy and the resulting economic benefits.
We evaluate performance across the three forecasting levels outlined in the methodology:
Level 1 (clear-sky baseline with no data sharing), Level 2 (solo forecasting using historical
data from individual PV systems), and Level 3 (networked forecasting incorporating data
from neighboring PV systems). Forecasting accuracy is assessed using the Mean Absolute
Error (MAE), as defined in the methodology, to quantify prediction performance. Economic
benefits are evaluated through total imbalance costs (C), approximated as C ≈ ¯m · MAE · E,
where ¯m is the average imbalance price and E is the total energy volume, enabling direct
comparisons of cost savings (∆C) across levels. Several forecasting methods are compared,
namely, a clear-sky model (CS), baseline averaging (AVG) model, Support Vector Regres-
sion (SVR), Random Forests (RFs), Extreme Gradient Boosting (XGB), and a Multilayer
Perceptron (MLP), to provide a comprehensive assessment.

---

## Page 16

Forecasting 2025, 7, 77 16 of 30
4.1. Forecasting Accuracy
4.1.1. Forecasting Accuracy at Level 1
At Level 1, no data is shared, and forecasting relies solely on a clear-sky model, which
estimates PV production based on astronomical parameters without historical or real-time
data. Specifically, we employ the Haurwitz clear-sky Global Horizontal Irradiance (GHI)
model, which calculates solar irradiance using only astronomical inputs such as solar zenith
angle [73].
The performance metrics for this level were calculated across the 47 PV installations
in the dataset, comparing the model’s predictions against actual power output. The
distribution statistics of these metrics are summarized in Table 2. The clear-sky model
exhibits relatively high errors, with a mean Mean Absolute Error (MAE) of 0.0817 ± 0.0045,
a mean Root Mean Square Error (RMSE) of 0.1488 ± 0.0075, and a mean Coefficient of
Determination (R2) of 0.6313 ± 0.0407. These values highlight the limitations of non-data-
driven approaches, particularly in accounting for cloud cover, atmospheric conditions, and
other localized variabilities that affect solar output.
Table 2. Distribution statistics of forecasting performance metrics across PV installations using the
Haurwitz clear-sky GHI model.
Metric Mean Standard Deviation
MAE 0.0817 0.0045
RMSE 0.1488 0.0075
R2 0.6313 0.0407
4.1.2. Forecasting Accuracy at Level 2
At Level 2, forecasting relies solely on historical data from the individual PV installa-
tion, without incorporating spatial information from neighboring systems. This represents
a solo forecasting approach that leverages temporal patterns from the system’s own pro-
duction history.
We compared the performance of several forecasting methods in this configuration:
a baseline averaging model (AVG), which uses simple day-profile averaging based on
historical data without machine learning, and advanced machine learning models, namely,
Support Vector Regression (SVR), Random Forests (RFs), Extreme Gradient Boosting (XGB),
and a Multilayer Perceptron (MLP). This evaluation quantifies the benefits of machine
learning over the simple history-based AVG approach for solo forecasting.
The results are summarized numerically in Table 3. Three common forecasting ac-
curacy metrics were employed: Mean Absolute Error (MAE), Root Mean Square Error
(RMSE), and the Coefficient of Determination (R2).
Table 3. Forecasting accuracy for evaluated models at Level 2 (mean ± std across PV units).
Model MAE RMSE R2
AVG 0.0795 ± 0.0040 0.1496 ± 0.0062 0.6416 ± 0.0222
SVR 0.1046 ± 0.0060 0.1325 ± 0.0054 0.6941 ± 0.0215
RF 0.0676 ± 0.0026 0.1218 ± 0.0047 0.7418 ± 0.0140
XGB 0.0697 ± 0.0026 0.1236 ± 0.0048 0.7340 ± 0.0145
MLP 0.0727 ± 0.0031 0.1213 ± 0.0050 0.7414 ± 0.0164
The results demonstrate that all Level 2 models, including the simple AVG baseline,
achieve comparable or slightly better performance than the Level 1 clear-sky model, un-
derscoring the value of incorporating historical data from individual PV systems. Notably,
the machine learning models (except SVR) outperform the AVG baseline, highlighting the

---

## Page 17

Forecasting 2025, 7, 77 17 of 30
advantages of data-driven approaches in capturing complex temporal patterns over both
the non-data-driven Level 1 baseline and the history-only AVG method. Among them,
the Random Forests model achieved the lowest MAE (0.0676 ± 0.0026) and highest R2
(0.741 ± 0.014), while the MLP achieved the lowest RMSE (0.1213 ± 0.005), indicating its
superior ability to model non-linear relationships in historical data. XGB also showed
substantial improvements over AVG and Level 1, further validating the value of machine
learning for solo forecasting. Interestingly, the AVG model achieved a lower MAE than
SVR (0.1046 ± 0.0060), suggesting that simple averaging can be effective for minimizing
average absolute errors, though it underperforms in explaining variance and handling
variability compared with the better machine learning methods and offers only marginal
gains over Level 1.
4.1.3. Forecasting Accuracy at Level 3: Impact of Network Density
At Level 3, forecasting incorporates historical data from both the target PV installation
and a varying number of neighboring installations, leveraging spatial correlations to
enhance predictions. This networked approach builds directly on the solo machine learning
models from Level 2 (equivalent to 0 neighbors), allowing us to quantify the incremental
benefits of increasing network density.
Figures 3–5 present the evolution of forecasting accuracy metrics with the increase in
the number of neighboring installations. The figures illustrate the distribution of forecasting
results across PV units for each level of network density, with the first box (0 neighbors)
representing the Level 2 solo performance for the machine learning models.
Figure 3. Distribution of MAE values as a function of the number of neighboring PV installations
included.

---

## Page 18

Forecasting 2025, 7, 77 18 of 30
Figure 4. Distribution of RMSE values as a function of the number of neighboring PV installations
included.
Figure 5. Distribution of R2 values as a function of the number of neighboring PV installations
included.

---

## Page 19

Forecasting 2025, 7, 77 19 of 30
The results show that MAE decreases sharply when the first few neighboring installa-
tions are added, with most of the improvement occurring within the first 10–15 neighbors.
Beyond this point, the curve flattens, indicating diminishing marginal forecasting benefits
as spatial redundancy increases.
RMSE follows the same pattern as MAE: the accuracy improves quickly with initial
increases in network density, and the gains saturate once roughly 10–15 neighbors are
incorporated. This reinforces that short-term irradiance dynamics are primarily informed
by geographically close systems.
The R² metric increases significantly as nearby neighbors are included, confirming
that spatial information enhances the explanatory power of the model. The improvement
tapers off with larger neighbor counts, consistent with the saturation behavior observed in
MAE and RMSE.
Across all forecasting models (RF, XGB, SVR, and MLP), the results consistently
demonstrate improvements in forecasting accuracy as additional neighboring installations
are included, extending the gains observed at Level 2 over the non-data-driven Level 1
baseline. MAE and RMSE decrease with network density, while R2 increases, indicating
closer alignment between predicted and actual production compared with solo forecasting.
We applied a paired Wilcoxon signed-rank test to the Random Forests MAE values
across all 47 PV installations to confirm that the observed improvement from Level 2 to Level 3
is statistically significant. The test indicated a highly significant reduction in error when using
10 nearest neighbors(V = 0, z = −5.96, p = 1.24 × 10−9). This shows that the gain from
network-based forecasting is not due to random variation but is statistically robust.
Model comparisons reveal distinctive sensitivities to network density. To quantify
these observations, we computed Spearman correlation coefficients between the number of
neighboring PV installations and the three forecasting metrics. These coefficients, annotated
in Figures 3–5, confirm the visual trends:
• XGB consistently achieves the strongest correlations (absolute values ≳ 0.8), underlin-
ing its robustness to spatial data integration.
• RF follows closely, with correlation values around 0.7–0.8, also indicating high sensi-
tivity to network density.
• SVR and the MLP show weaker coefficients (absolute values generally < 0.6), reflect-
ing limited responsiveness to neighboring installations.
In summary, the analysis establishes a robust link between forecasting accuracy and
network density at Level 3, with clear thresholds (about ten neighbors), beyond which
additional data provide diminishing returns. It highlights the superior adaptability of XGB
and RF in networked settings, reinforces the critical role of spatial correlation in decen-
tralized solar forecasting, and demonstrates substantial gains over the solo approaches at
Levels 1 and 2.
4.2. Economic Impact
4.2.1. Imbalance Costs at Level 1
The imbalance price used in this study was determined based on market data from
the Dutch electricity sector. Specifically, we adopted the average price for shortages in 2023,
which was 198 EUR/MWh according to a Rabobank report [78]. This value serves as the
representative average imbalance price ( ¯m) in our simplified economic model, reflecting
the costs incurred by Balance Responsible Parties (BRPs) for deviations in the balancing
market. Given that our forecasting model provides predictions 1 h ahead, this aligns with
intraday market dynamics, where imbalance costs often increase due to the urgency of
short-term grid adjustments. This estimate helps quantify the financial implications of
forecast errors, emphasizing the potential for cost reductions through improved accuracy

---

## Page 20

Forecasting 2025, 7, 77 20 of 30
in DePIN frameworks. At Level 1, where no data is shared and forecasting relies on the
clear-sky model, the imbalance costs represent the baseline economic burden for the BRP .
The economic burden of Level 1 participants is quantified through the imbalance costs they
impose, as shown in Equation (9):
CL1 ≈ ¯m · MAEL1 · E = 198 × 0.0817 × 100.08 ≈ EUR 1618 (11)
where CL1 represents the imbalance costs attributable to Level 1 forecasting inaccuracy,
¯m = 198 EUR/MWh is the average imbalance price, MAEL1 = 0.0817 is the forecasting
error using the clear-sky model, and E = 100.08 MWh is the total energy volume for the
portfolio of 47 PV systems over the 9-month period (January to September 2016, com-
puted from the de-normalized energy production data totaling 100,078.90 kWh). This
level highlights the financial inefficiencies associated with non-data-driven forecasting,
where the full imbalance costs are borne by the BRP without any mitigating contributions
from participants.
4.2.2. Imbalance Costs at Level 2
At Level 2, where forecasting incorporates historical data from individual PV systems
without cross-sharing, the imbalance costs are reduced compared with Level 1 due to
improved accuracy from local temporal patterns. We evaluated the economic burden using
the Mean Absolute Error (MAE) from various models, as detailed in the methodology.
The imbalance costs for each model are quantified using Equation (9), with¯m = 198
EUR/MWh and E = 100.08 MWh. The cost for the Random Forests (RFs) model, which
achieves the lowest MAE and highest relative savings, is calculated as shown in Equation (12):
CL2,RF ≈ 198 × 0.0676 × 100.08 ≈ EUR 1339. (12)
Similar calculations apply to the other models (Table 4). The 17.24% relative savings
with the RF model represent the portfolio-wide economic benefit if the historical data from
all PV systems—covering the full energy production of the portfolio—are shared within
the DePIN, enabling these accuracy improvements across the entire network.
Table 4. Imbalance costs and relative savings for evaluated models at Level 2 (mean across PV units).
Relative savings are calculated using (CL1 − CL2)/CL1 × 100%, where CL1 ≈ EUR 1618.
Model MAE Imbalance Cost (EUR) Relative Savings ( %)
AVG 0.0795 1574 2.72
SVR 0.1061 2100 −29.79
RF 0.0676 1339 17.24
XGB 0.0698 1383 14.52
MLP 0.0725 1435 11.31
This level demonstrates the economic benefits of utilizing historical data within a
DePIN framework, where participants contribute their own data to enable these accuracy
gains, potentially receiving tokenized rewards from the resulting cost savings borne by the
BRP . Note that some models, such as SVR, may yield higher costs than Level 1, highlighting
the importance of selecting appropriate forecasting methods.
4.2.3. Imbalance Costs at Level 3
At Level 3, where forecasting incorporates historical data from both the target PV
installation and neighboring installations, the economic benefits are substantially enhanced
through the network effect. The relationship between network density and economic costs
follows a similar pattern to the forecasting accuracy improvements observed in Figures 3–5.

---

## Page 21

Forecasting 2025, 7, 77 21 of 30
Figure 6 illustrates the reduction in imbalance costs as the network density increases,
using the Random Forests model as representative. The economic costs show a clear decreas-
ing trend with the increase in the network density, mirroring the improvements in forecast-
ing accuracy. The most significant cost reductions occur within the first 10–15 neighboring
installations, with diminishing returns beyond this threshold.
Figure 6. Economic cost (EUR) as a function of the number of neighboring PV installations included.
To quantify these improvements, the imbalance costs for key network densities using
the Random Forests model are reported in Table 5. The Level 2 configuration (0 neighbors)
results in an imbalance cost of EUR 1339, whereas incorporating only five neighbors reduces
this to EUR 1002. Increasing to ten neighbors yields EUR 953, while the full-network
scenario (46 neighbors) achieves the lowest cost of EUR 884.
Table 5. Imbalance costs at different network densities (Random Forests model).
Network Configuration Imbalance Cost (EUR)
Level 2 (0 neighbors) 1339
Level 3 (5 neighbors) 1002
Level 3 (10 neighbors) 953
Level 3 (15 neighbors) 940
Level 3 (46 neighbors) 884
4.2.4. Sensitivity to Imbalance Price Variability
We performed a sensitivity analysis by varying the representative imbalance price by
±20% around the Dutch 2023 average (198 EUR/MWh) to evaluate the robustness of the
economic conclusions with respect to real-world imbalance price volatility. Table 6 reports
the resulting imbalance costs for key network densities.

---

## Page 22

Forecasting 2025, 7, 77 22 of 30
Table 6. Price sensitivity of imbalance costs in low ( −20%), baseline, and high (+20%) imbalance
price scenarios.
Network Configuration Low ( −20%) Baseline High ( +20%)
Level 2 (0 neighbors) 1071 1339 1607
Level 3 (5 neighbors) 802 1002 1202
Level 3 (10 neighbors) 762 953 1144
Level 3 (15 neighbors) 752 940 1128
Level 3 (46 neighbors) 707 884 1061
Because the imbalance-cost model is linear in the imbalance price (Equation (9)),
absolute costs scale proportionally with the price level. Importantly, however, the relative
savings achieved with networked forecasting remain unchanged. For example, the cost
reduction from Levels 2 to 3 with full-network access remains approximately 33% across
all three price scenarios, and the reduction from Levels 2 to 3 with ten neighbors remains
28.9%. This demonstrates that the economic benefits of network-based forecasting are
robust to realistic fluctuations in imbalance pricing.
4.2.5. Marginal Benefits and Spatial Analysis
The analysis evaluates the marginal benefit (MB), defined as the reduction in total
imbalance cost per additional participating PV system. Figure 7 illustrates the relationship
between marginal benefit and the number of participants, revealing a strong trend of dimin-
ishing marginal returns. As the collaborative forecasting pool scales, total costs decrease
from EUR 1340 (with 0 participants) to EUR 885 (with 46 participants), demonstrating
significant improvements in cost efficiency through network expansion.
Figure 7. Marginal Benefit versus Number of Participating PV Systems.
The marginal benefit analysis shows that the initial participants provide the most
substantial value, with the first additional system yielding EUR 155.28 in cost savings. Be-
yond approximately 20 participants, the marginal benefit stabilizes at low levels, generally
remaining below EUR 3 per additional system.
Table 7 and Figure 8 detail how system interconnections evolve with the increase in
the geographical radius, revealing three distinct phases of network development.

---

## Page 23

Forecasting 2025, 7, 77 23 of 30
Table 7. Neighborhood density evolution with the increase in radius.
Radius (km) Mean Median Std Dev Network Phase
2.5 3.32 2.00 3.30 Immediate neighborhood
5.0 9.32 10.00 7.26 Local cluster formation
7.5 16.04 19.00 10.29 Cluster integration
10.0 21.96 28.00 12.26 Regional network
15.0 28.34 35.00 13.17 Near-complete connectivity
20.0 32.81 37.00 10.90 Saturation phase
30.0 41.96 43.00 6.07 Full network integration
Figure 8. Average number of neighbors as a function of radius.
During the rapid local clustering phase (0–7.5 km), connectivity grows exponentially
with a 483% increase in mean neighbors from 2.5 to 7.5 km, forming dense local clusters with
strong spatial correlation. The Transition to Regional Network phase (7.5–15 km) shows
continued growth at a reduced rate (77% increase), integrating local clusters into a regional
network. Finally, the Saturation and Completion phase (15–30 km) exhibits dramatically
slowed growth (48% increase over 15 km), approaching full network integration.
Intermediate radii (5–15 km) show median exceeding mean, demonstrating above-
average connectivity for most systems. Large radii (≥20 km) exhibit convergence of mean
and median values, indicating uniform connectivity as the network approaches complete-
ness. The standard deviation pattern peaks at 15 km radius ( 13.17) when connectivity
variability is maximized, then decreases with network uniformity.
5. Discussion
This study provides the first integrated analysis of how network density in decentral-
ized physical infrastructure networks (DePINs) affects both the solar forecasting accuracy
and economic viability. By separating descriptive results from interpretive insights, the
following discussion synthesizes the key mechanisms behind the observed performance
patterns and highlights their broader implications.

---

## Page 24

Forecasting 2025, 7, 77 24 of 30
5.1. Technical Implications for Solar Forecasting
Across all machine learning models, the forecasting accuracy improved consistently
with the inclusion of neighboring PV installations, but these gains followed a clear sat-
uration pattern. The strongest improvements occurred within the first 10–15 neighbors,
after which additional installations contributed increasingly redundant information. This
behavior reflects the underlying spatial correlation structure: nearby PV systems experi-
ence highly similar irradiance dynamics due to shared cloud movements and micro-local
weather patterns, while installations beyond roughly 10–15 km—corresponding to typical
cloud field scales in the Utrecht region—exhibit markedly weaker correlations. Conse-
quently, the diminishing returns observed in the MAE, RMSE, and R2 metrics directly stem
from the reduced informational value of more distant nodes.
The model-specific behavior further elucidates the mechanisms of networked fore-
casting. Random Forests and XGBoost achieved the largest accuracy gains, confirming
their capacity to exploit fine-grained non-linear relationships embedded in spatially dis-
tributed data. In contrast, the SVR and MLP displayed flatter improvements and higher
variability across installations, suggesting weaker sensitivity to spatial features and greater
dependence on hyperparameters. The strong negative Spearman correlations between the
network density and both the MAE and RMSE, and the corresponding positive correlations
with R2, reinforce that increased density systematically enhances predictive power up to
the saturation threshold.
Overall, the technical findings indicate that DePIN-based forecasting benefits substan-
tially from local clustering, with approximately 10 neighbors providing a practical upper
bound for meaningful improvements in short-term solar predictions.
5.2. Economic Viability and Market Transformation
The economic analysis showed that network-driven gains in accuracy translate directly
into substantial reductions in imbalance costs. The relative cost savings remained stable
across different imbalance price scenarios because the economic model is linear in price;
thus, improvements in MAE retain their proportional value under both high- and low-
price conditions. This robustness strengthens the practical relevance of the observed
cost reductions.
Interpreting the cost curve reveals the same saturation behavior visible in the fore-
casting metrics. The steepest decrease in imbalance costs occurs when moving from zero
to approximately ten neighbors, consistent with the region of highest spatial correlation.
Beyond this range, marginal cost reductions taper off sharply. The marginal benefit analysis
further illustrates this phenomenon: the first few additional neighbors offer large reduc-
tions in imbalance costs, but the marginal value rapidly declines until stabilizing at very
low levels once the network becomes fully interconnected.
These diminishing marginal returns have important implications for DePIN economics.
Incentive structures should not reward unlimited expansion of data connectivity but rather
prioritize reaching an optimal local density. High rewards are justified for early contributors
who help establish the first few meaningful data links, while subsequent connections should
receive smaller rewards to avoid over-incentivizing redundant data.
5.3. DePIN as a Solution to Data Fragmentation
Beyond the forecasting performance, the results underscore the role of the DePIN
as a mechanism for overcoming entrenched data fragmentation in electricity markets.
Traditional BRP frameworks prevent cross-portfolio access to operational PV measurements
due to confidentiality and governance constraints. The DePIN enables prosumers to

---

## Page 25

Forecasting 2025, 7, 77 25 of 30
voluntarily and securely share data with privacy-preserving incentives, thereby unlocking
spatial correlations that conventional market structures cannot access.
The two-layer benefit structure—improvements from solo historical data (Level 2) and
additional improvements from spatial data (Level 3)—shows that DePINs can be deployed
incrementally. Participants receive immediate value from sharing their own data, with
additional value unlocked as local clusters densify. This gradual adoption pathway is
particularly relevant for real-world deployment, where network density develops unevenly
over time.
5.4. Practical Implementation Considerations
The spatial analysis revealed three distinct phases in the growth of neighbor con-
nectivity: rapid local clustering within 5–10 km, a transition phase up to 15 km, and a
saturation phase beyond 15 km where nearly all systems become interconnected. These
phases closely match the marginal benefit behavior observed economically, confirming that
spatial topology directly drives the forecasting value.
The alignment between geographical distance and forecasting benefit suggests that
DePIN deployment strategies should aim to achieve dense local clusters before attempting
broad regional coverage. Urban and suburban environments—where distances between in-
stallations are naturally small—represent ideal early deployment regions. Nevertheless, the
strong performance of the forecasting models even with only 47 installations demonstrates
that meaningful value can be created in medium-density regions as well.
Regulatory considerations further support DePIN implementation. The emerging EU
Data Act and interoperability frameworks emphasize user consent, privacy preservation,
and data portability, all of which align with the DePIN architecture. As a result, decentral-
ized data sharing through tokenized participation can operate within existing regulatory
constraints while enhancing grid resilience.
5.5. Limitations and Research Boundaries
Several limitations should be considered when interpreting these results. First, the
analysis is restricted to a single geographical region (Utrecht), the relatively homogeneous
climate and dense urban layout of which may not reflect conditions in other areas. Spatial
correlation patterns, cloud dynamics, and irradiance variability can differ substantially
across climates. In addition, the study focuses exclusively on residential-scale PV systems;
utility-scale installations may exhibit different spatial and temporal behavior, and the extent
to which our results generalize to those settings remains uncertain.
Second, the forecasting horizon examined here is limited to one hour ahead, which is
relevant for intraday market decisions but represents only one segment of the forecasting
landscape. Very short-term horizons (minutes ahead) or longer-term forecasts (day-ahead)
are governed by different physical processes and may exhibit different relationships be-
tween network density and accuracy. As a result, the density–accuracy patterns identified
in this study should not be assumed to hold uniformly across other horizons.
Finally, the economic model adopts a simplified imbalance pricing scheme based
on a single representative average price. While this abstraction helps isolate the effect
of forecasting accuracy, real-world settlement systems often include asymmetric pricing,
time-dependent penalties, and ancillary services that can amplify or diminish the financial
impact of forecast errors. Moreover, the 198 EUR/MWh reference value reflects conditions
in the Dutch market during 2023 and may differ substantially in other regulatory or market
contexts. Consequently, the economic results should be interpreted as illustrative rather
than universally transferable.

---

## Page 26

Forecasting 2025, 7, 77 26 of 30
5.6. Broader Implications for Energy Transition
The collective results point to broader implications for the future of renewable energy
systems. By enabling privacy-preserving, incentive-aligned data sharing, DePINs effec-
tively transform distributed PV assets into a collaborative sensing network. This bottom-up
architecture complements traditional centralized grid monitoring and forecasting, offering
resilience, redundancy, and cost-effective scalability.
The demonstrated success of ensemble machine learning models highlights the grow-
ing importance of AI techniques in managing distributed energy resources. As renewable
penetration increases, accurate short-term forecasting will play a critical role in mitigating
volatility and reducing infrastructure stress.
Finally , the principles demonstrated here—network-density-driven accuracy improve-
ments, diminishing marginal returns, and decentralized incentive structures—extend naturally
to other distributed resources, such as wind turbines, batteries, electric vehicles, and demand-
responsive loads. DePIN architectures thus offer a foundational framework for the next
generation of decentralized, user-centric, and economically sustainable energy systems.
6. Conclusions
This study presents a systematic analysis of how decentralized data sharing in de-
centralized physical infrastructure networks (DePINs) can improve both the technical
and economic performance of solar power forecasting. Using real-world data from 47 PV
systems in Utrecht, we developed a hierarchical forecasting framework that isolates the
contributions of historical data (Level 2) and spatial neighbor information (Level 3). The
results demonstrate that increasing network density substantially improves forecasting
accuracy, with the most pronounced gains occurring when approximately 10–15 neigh-
boring installations are included. These technical improvements translate directly into
economic benefits: networked forecasting reduces imbalance costs by up to 45% relative to
the non-data-driven Level 1 baseline and by 34% compared with Level 2 solo forecasting.
These reductions reflect the strong spatial correlations in PV production within 5–10 km
radii, where local cloud dynamics dominate short-term irradiance variability.
The main contributions of this work are threefold. First, we provide an empirical
characterization of the relationship between the network density and forecasting accu-
racy, identifying a clear diminishing-returns pattern beyond 10–15 neighbors. Second,
we quantify how the resulting accuracy gains reduce imbalance costs, including a sen-
sitivity analysis demonstrating that the relative financial benefits persist across realistic
price-volatility scenarios. Third, we show that DePIN-style data sharing could help over-
come operational data fragmentation by enabling privacy-preserving access to distributed
PV measurements.
While these findings highlight the potential of DePIN-enabled forecasting, they should
not be interpreted as universally transferable. The analysis focuses on a single region,
a one-hour forecasting horizon, and residential-scale PV systems. Future work should
evaluate the density–accuracy relationship across diverse climates, geographies, and system
scales and investigate how advanced spatio-temporal models (e.g., graph neural networks)
interact with network density. In addition, real-world DePIN deployments will require
careful design of token-based incentives and privacy safeguards, which remain open
research directions.
Overall, our results suggest that decentralized data-sharing architectures hold promise
for improving short-term forecasting and reducing imbalance costs. Rather than definitive
claims of scalability, these findings should be viewed as a foundation for future exploration
of DePIN-based forecasting in larger and more heterogeneous energy systems.

---

## Page 27

Forecasting 2025, 7, 77 27 of 30
Author Contributions: Conceptualization, M.C.; Methodology, M.C. and A.M.; Validation, M.C.
and P .P .; Formal analysis, P .P .; Investigation, M.C. and A.M.; Resources, A.M.; Data curation, A.M.;
Writing—original draft, M.C. and A.M.; Writing—review & editing, P .P .; Visualization, A.M.; Supervi-
sion, M.C. and P .P .; Project administration, M.C.; Funding acquisition, P .P . All authors have read and
agreed to the published version of the manuscript.
Funding: Slovenian Research Agency: P2-0270; Ministry of Higher Education, Science and Technol-
ogy of the Republic of Slovenia: 100-15-0510.
Data Availability Statement: The processed photovoltaic dataset used in this study, including the
15-min aggregated power measurements from 47 residential PV systems in Utrecht (The Netherlands)
and the corresponding forecasting results, is openly available at the GitHub repository [ 79]. The
original raw data is publicly available as the Utrecht Solar PV Dataset [66].
Conflicts of Interest: The authors declare no conflicts of interest.
References
1. Intergovernmental Panel on Climate Change (IPCC). Technical Summary. In Climate Change 2021—The Physical Science Basis ;
Cambridge University Press: Cambridge, UK, 2023; pp. 35–144. [CrossRef]
2. IEA. World Energy Outlook 2022; IEA Report; IEA: Paris, France, 2022.
3. IEA. Renewable Energy Statistics 2023; IRENA Report; IEA: Paris, France, 2023.
4. Antonanzas, J.; Pozo-Vázquez, D.; Fernandez-Jimenez, L.A.; Martinez-de Pison, F.J. The value of day-ahead forecasting for
photovoltaics in the Spanish electricity market. Sol. Energy 2017, 158, 140–146. [CrossRef]
5. Diagne, M.; David, M.; Lauret, P .; Boland, J.; Schmutz, N. Review of solar irradiance forecasting methods and a proposition for
small-scale insular grids. Renew. Sustain. Energy Rev. 2013, 27, 65–76. [CrossRef]
6. Morales, J.M.; Conejo, A.J.; Madsen, H.; Pinson, P .; Zugno, M.Integrating Renewables in Electricity Markets: Operational Problems;
International Series in Operations Research & Management Science; Springer: Boston, MA, USA, 2014; Volume 205. [CrossRef]
7. Inman, R.H.; Pedro, H.T.; Coimbra, C.F. Solar forecasting methods for renewable energy integration. Prog. Energy Combust. Sci.
2013, 39, 535–576. [CrossRef]
8. Lorenz, E.; Scheidsteger, T.; Hurka, J.; Heinemann, D.; Kurz, C. Regional PV power prediction for improved grid integration.
Prog. Photovoltaics Res. Appl. 2011, 19, 757–771. [CrossRef]
9. European Union. Regulation (EU) 2023/2854 on Harmonised Rules on Fair Access to and Use of Data (Data Act); European Union:
Brussels, Belgium, 2023.
10. European Commission. Commission Regulation (EU) 2017/2195 of 23 November 2017 Establishing a Guideline on Electricity Balancing;
Official Journal of the European Union: Brussels, Belgium, 2017; pp. 6–53, L 312.
11. CEER. Data Sharing in the Energy Sector: Best Practices and Recommendations ; Technical Report; Council of European Energy
Regulators (CEER): Brussels, Belgium, 2022.
12. European Data Protection Supervisor. Opinion on Smart Metering; Technical Report; EDPS: Brussels, Belgium, 2012.
13. OECD. Competition and Privacy in Digital Markets: Policy Interactions; Technical Report; Organisation for Economic Co-Operation
and Development: Paris, France, 2024.
14. ENTSO-E. ENTSO-E Transparency Platform. Available online: https://transparency.entsoe.eu/ (accessed on 7 October 2025).
15. von der Assen, J.; Killer, C.; De Carli, A.; Stiller, B. Performance Analysis of Decentralized Physical Infrastructure Networks and
Centralized Clouds. arXiv 2024, arXiv:2404.08306. [CrossRef]
16. Helium Systems, Inc. Helium: A Decentralized Wireless Network; Helium Systems, Inc.: San Francisco, CA, USA, 2021.
17. Hivemapper Inc. Hivemapper Litepaper: A Decentralized Mapping Network; Helium Systems, Inc.: San Francisco, CA, USA, 2023.
18. Ocean Protocol Foundation. Ocean Protocol: A Decentralized Data Exchange Protocol to Unlock Data for AI; Ocean Protocol Foundation:
Singapore, 2020.
19. Streamr Network. The Streamr Network: A Decentralized Real-Time Data Transport Protocol; Streamr Network: Zug, Switzerland,
2023.
20. Andoni, M.; Robu, V .; Flynn, D.; Abram, S.; Geach, D.; Jenkins, D.; McCallum, P .; Peacock, A. Blockchain technology in the energy
sector: A systematic review of challenges and opportunities. Renew. Sustain. Energy Rev. 2019, 100, 143–174. [CrossRef]
21. Alladi, T.; Chamola, V .; Rodrigues, J.J.P .C.; Kozlov, S.A. Blockchain in Smart Grids: A Review on Different Use Cases.Sensors
2019, 19, 4862. [CrossRef]
22. Kairouz, P .; McMahan, H.B.; Avent, B.; Bellet, A.; Bennis, M.; Bhagoji, A.N. Advances and Open Problems in Federated Learning.
Found. Trends Mach. Learn. 2021, 14, 1–210. [CrossRef]

---

## Page 28

Forecasting 2025, 7, 77 28 of 30
23. Energy Web Foundation. Decentralized Operating System (EW-DOS): Digital Infrastructure for the Energy Transition ; Technical
Report; Energy Web: Zug, Switzerland, 2020.
24. Mellit, A.; Pavan, A.M.; Ogliari, E.; Leva, S.; Lughi, V . Advanced Methods for Photovoltaic Output Power Forecasting: A Review.
Appl. Sci. 2020, 10, 487. [CrossRef]
25. Wang, S.; Li, C.; Lim, A. Why Are the ARIMA and SARIMA not Sufficient. arXiv 2019. [CrossRef]
26. Mellit, A.; Kalogirou, S.A. Artificial intelligence techniques for photovoltaic applications: A review. Prog. Energy Combust. Sci.
2008, 34, 574–632. [CrossRef]
27. Lee, W.; Kim, K.; Park, J.; Kim, J.; Kim, Y. Forecasting Solar Power Using Long-Short Term Memory and Convolutional Neural
Networks. IEEE Access 2018, 6, 73068–73080. [CrossRef]
28. Jang, S.Y.; Oh, B.T.; Oh, E. A Deep Learning-Based Solar Power Generation Forecasting Method Applicable to Multiple Sites.
Sustainability 2024, 16, 5240. [CrossRef]
29. Bouzerdoum, M.; Mellit, A.; Massi Pavan, A. A hybrid model (SARIMA–SVM) for short-term power forecasting of a small-scale
grid-connected photovoltaic plant. Sol. Energy 2013, 98, 226–235. [CrossRef]
30. Graabak, I.; Svendsen, H.; Korpås, M. Developing a wind and solar power data model for Europe with high spatial-temporal
resolution. In Proceedings of the 2016 51st International Universities Power Engineering Conference, UPEC 2016, Coimbra,
Portugal, 6–9 September 2016; pp. 1–6. [CrossRef]
31. Droste, A.M.; Pape, J.J.; Overeem, A.; Leijnse, H.; Steeneveld, G.J.; Van Delden, A.J.; Uijlenhoet, R. Crowdsourcing urban air
temperatures through smartphone battery temperatures in São Paulo, Brazil. J. Atmos. Ocean. Technol. 2017, 34, 1853–1866.
[CrossRef]
32. Hintz, K.S.; Vedel, H.; Kaas, E. Collecting and processing of barometric data from smartphones for potential use in numerical
weather prediction data assimilation. Meteorol. Appl. 2019, 26, 733–746. [CrossRef]
33. Simeunovi´ c, J.; Schubnel, B.; Alet, P .J.; Carrillo, R.E. Spatio-temporal graph neural networks for multi-site PV power forecasting.
IEEE Trans. Sustain. Energy 2021, 13, 1210–1220. [CrossRef]
34. Meier, F.; Fenner, D.; Grassmann, T.; Otto, M.; Scherer, D. Crowdsourcing air temperature from citizen weather stations for urban
climate research. Urban Clim. 2017, 19, 170–191. [CrossRef]
35. Madaus, L.E.; Mass, C.F. Evaluating Smartphone Pressure Observations for Mesoscale Analyses and Forecasts. Weather. Forecast.
2017, 32, 511–531. [CrossRef]
36. Gagliardi, G.; Gallelli, V .; Violi, A.; Lupia, M.; Cario, G. Optimal Placement of Sensors in Traffic Networks Using Global Search
Optimization Techniques Oriented towards Traffic Flow Estimation and Pollutant Emission Evaluation. Sustainability 2024,
16, 3530. [CrossRef]
37. Harmon, R.R.; Castro-Leon, E.G.; Bhide, S. Smart cities and the Internet of Things. Portland Int. Conf. Manag. Eng. Technol. 2015,
2015, 485–494. [CrossRef]
38. Ma, X.; Tao, Z.; Wang, Y.; Yu, H.; Wang, Y. Long short-term memory neural network for traffic speed prediction using remote
microwave sensor data. Transp. Res. Part C Emerg. Technol. 2015, 54, 187–197. [CrossRef]
39. Lv, Y.; Duan, Y.; Kang, W.; Li, Z.; Wang, F.Y. Traffic Flow Prediction with Big Data: A Deep Learning Approach.IEEE Trans. Intell.
Transp. Syst. 2015, 16, 865–873. [CrossRef]
40. Adsuara, J.E.; Perez-Suay, A.; Munoz-Mari, J.; Mateo-Sanchis, A.; Piles, M.; Camps-Valls, G. Nonlinear distribution regression for
remote sensing applications. IEEE Trans. Geosci. Remote Sens. 2019, 57, 10025–10035. [CrossRef]
41. Mateo-Sanchis, A.; Piles, M.; Muñoz-Marí, J.; Adsuara, J.E.; Pérez-Suay, A.; Camps-Valls, G. Synergistic integration of optical and
microwave satellite data for crop yield estimation. Remote Sens. Environ. 2019, 234, 111460. [CrossRef] [PubMed]
42. Zhao, W.; Chuluunbat, G.; Unagaev, A.; Efremova, N. Soil nitrogen forecasting from environmental variables provided by
multisensor remote sensing images. arXiv 2024. [CrossRef]
43. Soussi, A.; Zero, E.; Sacile, R.; Trinchero, D.; Fossa, M. Smart Sensors and Smart Data for Precision Agriculture: A Review. Sensors
2024, 24, 2647. [CrossRef]
44. Ballandies, M.C.; Wang, H.; Law, A.C.C.; Yang, J.C.; Gösken, C.; Andrew, M. A Taxonomy for Blockchain-based Decentralized
Physical Infrastructure Networks (DePIN). arXiv 2023, arXiv:2309.16707. [CrossRef]
45. Messina, A.; Mettler, M.; Singh, A. Token-Based Coordination of Distributed Physical Infrastructure. J. Networked Syst. 2024,
12, 225–242.
46. Zhu, T.; Huang, X.; Guo, K.; Xu, Y.; Wang, K. Peer-to-peer energy trading: A review of the literature. Appl. Energy 2020,
268, 114978.
47. Talari, S.; Shafie-Khah, M.; Siano, P .; Loia, V .; Tommasetti, A.; Catalão, J.P . A Review of Smart Cities Based on the Internet of
Things Concept. Energies 2017, 10, 421. [CrossRef]
48. Atzori, L.; Iera, A.; Morabito, G. The Internet of Things: A survey. Comput. Netw. 2010, 54, 2787–2805. [CrossRef]
49. Gubbi, J.; Buyya, R.; Marusic, S.; Palaniswami, M. Internet of Things (IoT): A vision, architectural elements, and future directions.
Future Gener. Comput. Syst. 2013, 29, 1645–1660. [CrossRef]

---

## Page 29

Forecasting 2025, 7, 77 29 of 30
50. Chen, S.; Jiang, M.; Luo, X. Exploring the Security Issues of Real World Assets (RWA). In Proceedings of the DeFi 2024—
Proceedings of the Workshop on Decentralized Finance and Security, Salt Lake City, UT, USA, 14–18 October 2024; pp. 31–40.
[CrossRef]
51. Schär, F. Decentralized Finance: On Blockchain- and Smart Contract-Based Financial Markets. SSRN Electron. J. 2020. [CrossRef]
52. Dzhunev, P . Helium Network—Integration of Blockchain Technologies in the Field of Telecommunications. In Proceedings of the
13th National Conference with International Participation, ELECTRONICA 2022, Sofia, Bulgaria, 19–20 May 2022. [CrossRef]
53. ˇCerba, O.; Andrš, T.; Fournier, L.; Vanˇ ek, M. Cartography & Web3.Int. J. Cartogr. 2023, 9, 437–448. [CrossRef]
54. 2025 Arkreen Network. What Is Arkreen|Arkreen Documentation. Available online: https://docs.arkreen.com/ (accessed on 7
October 2025).
55. Perez, R.; Schlemmer, J.; Hemker, K.; Kivalov, S.; Kankiewicz, A.; Dise, J. Solar energy forecast validation for extended areas &
economic impact of forecast accuracy. In Proceedings of the 2016 IEEE 43rd Photovoltaic Specialists Conference (PVSC), Portland,
OR, USA, 5–10 June 2016; pp. 1119–1124. [CrossRef]
56. Kraas, B.; Schroedter-Homscheidt, M.; Madlener, R. Economic merits of a state-of-the-art concentrating solar power forecasting
system for participation in the Spanish electricity market. Sol. Energy 2013, 93, 244–255. [CrossRef]
57. Brancucci Martinez-Anido, C.; Botor, B.; Florita, A.R.; Draxl, C.; Lu, S.; Hamann, H.F.; Hodge, B.M. The value of day-ahead solar
power forecasting improvement. Sol. Energy 2016, 129, 192–203. [CrossRef]
58. Goodarzi, S.; Perera, H.N.; Bunn, D. The impact of renewable energy forecast errors on imbalance volumes and electricity spot
prices. Energy Policy 2019, 134, 110827. [CrossRef]
59. Kaur, A.; Nonnenmacher, L.; Pedro, H.T.; Coimbra, C.F. Benefits of solar forecasting for energy imbalance markets. Renew. Energy
2016, 86, 819–830. [CrossRef]
60. Jónsson, T.; Pinson, P .; Madsen, H. On the market impact of wind energy forecasts. Energy Econ. 2010, 32, 313–320. [CrossRef]
61. González-Aparicio, I.; Zucker, A. Impact of wind power uncertainty forecasting on the market integration of wind energy in
Spain. Appl. Energy 2015, 159, 334–349. [CrossRef]
62. Pierro, M.; Perez, R.; Perez, M.; Moser, D.; Cornaro, C. Italian protocol for massive solar integration: Imbalance mitigation
strategies. Renew. Energy 2020, 153, 725–739. [CrossRef]
63. Van Der Veen, R.A.; Hakvoort, R.A. Balance responsibility and imbalance settlement in Northern Europe—An evaluation. In
Proceedings of the 2009 6th International Conference on the European Energy Market, EEM 2009, Leuven, Belgium, 27–29
May 2009. [CrossRef]
64. Cui, J.; Gu, N.; Zhao, T.; Wu, C.; Chen, M. Forecast Competition in Energy Imbalance Market. IEEE Trans. Power Syst. 2022,
37, 2397–2413. [CrossRef]
65. Visser, L.R.; AlSkaif, T.A.; Khurram, A.; Kleissl, J.; van Sark, W.G. Probabilistic solar power forecasting: An economic and
technical evaluation of an optimal market bidding strategy. Appl. Energy 2024, 370, 123573. [CrossRef]
66. Visser, L.R.; Elsinga, B.; Alskaif, T.A.; Van Sark, W.G. Open-source quality control routine and multi-year power generation data
of 175 PV systems. J. Renew. Sustain. Energy 2022, 14, 043501. [CrossRef]
67. Klyve, O.S.; Nygård, M.M.; Riise, H.N.; Fagerström, J.; Marstein, E.S. The value of forecasts for PV power plants operating in the
past, present and future Scandinavian energy markets. Sol. Energy 2023, 255, 208–221. [CrossRef]
68. Das, S.S.; Das, A.; Dawn, S.; Gope, S.; Ustun, T.S. A Joint Scheduling Strategy for Wind and Solar Photovoltaic Systems to Grasp
Imbalance Cost in Competitive Market. Sustainability 2022, 14, 5005. [CrossRef]
69. Salem, T.S.; Kathuria, K.; Ramampiaro, H.; Langseth, H. Forecasting Intra-Hour Imbalances in Electric Power Systems. Proc.
AAAI Conf. Artif. Intell. 2019, 33, 9595–9600. [CrossRef]
70. Moon, H.; Lee, D.; Han, J.; Yoon, Y.; Kim, S. Impact of Imbalance Pricing on Variable Renewable Energies with Different Prediction
Accuracies: A Korean Case. Energies 2021, 14, 3976. [CrossRef]
71. Benallal, H.; Abouelaziz, I.; Mourchid, Y.; Falou, A.A.; Tairi, H.; Riffi, J.; Hassouni, M.E. A new approach for removing point
cloud outliers using the standard score. Pattern Recognit. Track. XXXIII 2022, 12101, 56–62. [CrossRef]
72. Pedregosa, F.; Varoquaux, G.; Gramfort, A.; Michel, V .; Thirion, B.; Grisel, O.; Blondel, M.; Prettenhofer, P .; Weiss, R.; Dubourg, V .;
et al. Scikit-learn: Machine learning in Python. J. Mach. Learn. Res. 2011, 12, 2825–2830. [CrossRef]
73. Haurwitz, B. Isolation in relation to cloud type. J. Atmos. Sci. 1948, 5, 110–113. [CrossRef]
74. Voyant, C.; Notton, G.; Kalogirou, S.; Nivet, M.L.; Paoli, C.; Motte, F.; Fouilloy, A. Machine learning methods for solar radiation
forecasting: A review. Renew. Energy 2017, 105, 569–582. [CrossRef]
75. Ahmed, R. A survey on solar forecasting: Methods, applications, and challenges. Sol. Energy 2020, 187, 678–713.
76. Mellit, A.; Pavan, A. An SVM-based model for forecasting solar radiation. Energy Convers. Manag. 2010, 51, 135–145.
77. Birkeland, D.; AlSkaif, T.; Duivenvoorden, S.; Meeng, M.; Pennings, J.M.E. Quantifying and Modeling Price Volatility in the
Dutch Intraday Electricity Market. Energy Rep. 2024, 12, 3830–3842. [CrossRef]

---

## Page 30

Forecasting 2025, 7, 77 30 of 30
78. de Boer, S. The Dutch Electricity Sector—Part 4: Changing Electricity Markets Present Opportunities and Risks for Businesses
and Households. RaboResearch. 2024. Available online: https://www.rabobank.com/knowledge/d011430987-the-dutch-
electricity-sector-part-4-changing-electricity-markets-present-opportunities-and-risks-for-businesses-and-households (accessed
on 7 October 2025).
79. Corn, M.; Murko, A.; Podržaj, P . DePIN Solar Forecasting Dataset—47 PV Systems (Utrecht, NL). 2025. Available online:
https://github.com/markocorn/depin-solar-forecasting-data-47pv (accessed on 30 January 2025).
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

---
