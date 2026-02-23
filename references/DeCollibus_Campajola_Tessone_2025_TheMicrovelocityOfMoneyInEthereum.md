# DeCollibus_Campajola_Tessone_2025_TheMicrovelocityOfMoneyInEthereum.pdf

## Page 1

Zurich Open Repository and Archive
University of Zurich
University Library
Strickhofstrasse 39
CH-8057 Zurich
www.zora.uzh.ch 
Year: 2025
The microvelocity of money in Ethereum
De Collibus, Francesco Maria; Campajola, Carlo; Tessone, Claudio J
DOI: https://doi.org/10.1140/epjds/s13688-024-00518-6
Posted at the Zurich Open Repository and Archive, University of Zurich 
ZORA URL: https://www.zora.uzh.ch/handle/20.500.14742/229449
Journal Article
Published Version
The following work is licensed under a Creative Commons: Attribution 4.0 International (CC BY 4.0)
License.
Originally published at:
De Collibus, Francesco Maria; Campajola, Carlo; Tessone, Claudio J (2025). The microvelocity of money in
Ethereum. EPJ Data Science, 14:11.
DOI: https://doi.org/10.1140/epjds/s13688-024-00518-6


---

## Page 2

DeCollibusetal. EPJDataScience           (2025) 14:11 
https://doi.org/10.1140/epjds/s13688-024-00518-6
RESEARCH OpenAccess
ThemicrovelocityofmoneyinEthereum
FrancescoMariaDeCollibus 1,2* ,CarloCampajola 2,3,4 andClaudioJ.Tessone 1,2
*Correspondence:
francescomaria.decollibus@uzh.ch
1BlockchainandDistributedLedger
TechnologiesGroup,Universityof
Zurich,Andreasstrasse15,8050,
Zurich,Switzerland
2UZHBlockchainCenter,University
ofZurich,Andreasstrasse15,8050,
Zurich,Switzerland
Fulllistofauthorinformationis
availableattheendofthearticle
Abstract
Thetransfervelocityofmoneyisamacroeconomicquantitythatmeasuresthe
frequencyofexchangesinaneconomy.Forcryptoassetsitcanbeexactlymeasured
adoptinganewapproach,MicroVelocity.Inthisstudyweapplytheframeworkto
Ether,thenativecryptocurrencyoftheEthereumblockchain,toinvestigatevelocity
anditstopcontributorsandhowtheycanbecharacterisedintheEthereum
ecosystem.Whiletheinequalitiesandheterogeneityinwealtharewellknown,we
hereﬁndthatthesameinequalitiesoccuraswellforMicroVelocitydistributionand
thatthisinequalityisnotexplainedjustbywealth,butratherbythebehaviourand
economicactivityofeachindividualagent.
Keywords: Blockchain;Ether;Ethereum;VelocityofMoney;MicroVelocity;Transfer
Velocity;Cryptocurrency;Cryptoassets;DigitalCurrency
1 Introduction
The concept of money, as a tool providing a uniform measure for the exchange of goods,
products,andservices, isfundamentaltothedisciplineofeconomics.
One historically successful approach to studying it is the quantity theory of money, in
which the velocity of money links supply with the general price level. The velocity of
moneyistypicallydeﬁnedastheaveragefrequencyatwhichaunitofmoneyisusedtopur-
chasegoodsandserviceswithinagivenperiod[ 1], or in other words, the ratio of money
ﬂow to the money stock in economic activity. Velocity is important in macroeconomic
models, as it can also be considered as an (inverse) indicator of money demand. Fisher’s
equation[2],which establishes theconnectionbetween moneysupply,velocityandprice
levels,isgenerallygivenas:
PQ=MV (1)
In thisequation,M denotesthemoneysupply, V isthevelocityofmoney, P represents
thepricelevel,and Qstandsforrealproductionoutput.
A more mechanistic description of economic activity in terms of payment systems in-
troducesthe transfervelocityofmoney,whichcanbecalculatedas“theratiobetweenthe
total transaction volume over a period of time and the average total balance of the pay-
mentsysteminthatperiod”[ 3,4].Thetransfervelocityofmoneycanbedeﬁnedusingan
©TheAuthor(s)2025. OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The
imagesorotherthirdpartymaterialinthisarticleareincludedinthearticle’sCreativeCommonslicence,unlessindicatedotherwise
in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright
holder.Toviewacopyofthislicence,visit http://creativecommons.org/licenses/by/4.0/.

---

## Page 3

DeCollibusetal. EPJDataScience           (2025) 14:11 Page2of23
identity similartothatexpressingthequantitytheoryofmoney,
V = FT
MT (2)
where FT is the total transfer volume, or the total ﬂow of money over a given period of
length T,M is theamountof money in circulation,andV is the average transfer velocity
ofmoneyoverthatsameperiodoftime.
The transfer velocity of money has seen an increase in attention as data from digital
payment systems becomes more accessible.
MbitiandWeil[ 3]examinethetransfervelocityofe-moneywithinKenya’sM-Pesasys-
tem,calculatedasthetotalvalueofperson-to-persontransfersdividedbytheaverageout-
standing balance of e-money. The study suggests that M-Pesa was used not just for rapid
transfers but at least initially also as a temporary store of value, as its transfer velocity is
relativelylowforadigital paymentsystem.
Mattsson et al. [4] develop an estimation technique for the transfer velocity of money
within the context of the digital community currency Sarafu, using micro-level transac-
tion data. Their results suggest that conventional aggregate measures of money velocity
can hide important variations at the spatial and temporal level, which may be crucial for
eﬀectivemonetarypolicywhenscaledtothebroadereconomy.
Asamatteroffact,quantifyingthetransfervelocityofmoneyinconventionaleconomic
systems poses challenges due to diﬃculties in tracking currency in its many forms (e.g.,
cash, credit cards, money transfers, lending), constraints by physical limitations of the
mediumandconcernsrelatedtoprivacyandregulation.Thatiswhythevelocityofmoney,
outsideofdigitalcurrenciesandcryptocurrencies,istypicallymeasuredindirectlyviaag-
gregatedvaluessuchastheGrossDomesticProductwithinaspeciﬁedtimeframedivided
by the monetary supply. These aggregate estimators prevent a more granular view of the
behaviour of individual agents in the system, which, as we will see, is instead better char-
acterisedby lookingattheholdingtimeoftheirmoney.
Campajolaetal.[ 5]introduceameasureofvelocitybasedonmicroeconomicdata,called
MicroVelocity,whichtogetherwithenhanceddataaboutindividualagentsallowstobreak
down the total velocity into multiple individual contributions. Using blockchain transac-
tion data from four cryptocurrencies, the authors ﬁnd that contributions to the total ve-
locityareveryunevenlydistributedandcorrelatestronglywithagentwealth,andthatthis
feature is common to multiple cryptocurrencies. The paper also identiﬁes high-velocity
intermediariesandhighlightstheconcentrationofeconomicactivityinveryfewdominant
entities,challengingthedecentralisedandpeer-to-peernarrativesurroundingcryptocur-
renciesintheirearlyyears.
The data deﬁciencies of traditional economies are mitigated in cryptocurrencies [6,7],
becauseinpublicblockchainseverytransferisvisiblewithinthesharedledger.Inthispa-
per we adapt the methods originally developed for cryptocurrencies using the Unspent
TransactionOutput(UTXO)accountingstandardtoaccount-basedcryptocurrencies,an
approach that is applicable in principle to any other account-based system, such as bank
transfers or theCentral Bank Digital Currencies(CBDC,[8]) that arecurrentlybeing de-
signed and tested by central banks worldwide. In this article we apply this adapted Mi-
croVelocitymeasureto investigate Ethereum’snative cryptocurrencyEther, which canbe
considered asa referencemodel for alltheaccount-basedcryptocurrencies.

---

## Page 4

DeCollibusetal. EPJDataScience           (2025) 14:11 Page3of23
Ethereum [9] is a public blockchain featuring a Turing-complete computing platform
with smart contracts, i.e. programs stored and executed directly on the blockchain.
Ethereum employs an account-based model in which each address is associated with a
balance. Transactions take place directly between addresses, where the sender’s address
transmits data to the recipient’s address. This data can represent a speciﬁed amount of
valuetobetransferredorrawdatasuchasafunctioncall.EachaddressinEthereumcor-
responds toan ExternallyOwned Account(EOA)or a SmartContract(SC).The address
ofanEOAisderivedfromapublickeythatisuniquelylinkedtoaprivatekey,whichcanbe
ownedbyanindividual (asitismostlythecase)oranoﬀ-chainprogram.Conversely, the
addressesofSCsaregovernedpurelybythelogicofcodeinsidetheblockchain,exposing
functions that can be invoked by EOAs or other contracts. Ethereum plays a pivotal role
in DecentralisedFinance (DeFi)applications: Schär[10]describesDeFiasa“blockchain-
based ﬁnancial infrastructure that refers to an open, permissionless, and highly interop-
erableprotocolstack builton publicsmartcontractplatforms”,which “replicates existing
ﬁnancialservicesinamoreopenandtransparentway’.
DeFi applications on the Ethereum platform cover a wide range of functions and prod-
ucts, such as Fungible and Non-Fungible Tokens (NFTs), decentralised lending and bor-
rowingplatforms,DecentralisedExchanges(DEXs),aswellasinnovativeformsoforgani-
sationslikeDecentralisedAutonomousOrganisations(DAOs).Amidstthisgrowingland-
scapeoftokensandpossibilities,Ether,Ethereum’snativecryptocurrency,remainscrucial:
Ether is in fact necessary to pay forgas, the commodity required to execute transactions
andsmartcontractmethods,renderingitthelifebloodofthewholeEthereumecosystem.
Intheperiodweconsider,thatisfromitsinceptionin2015tothesummerof2021,Ether
wasprimarilyissuedthroughaprocessknownas mining. As with many other cryptocur-
rencies,miningservesasarewardmechanismtosecurethenetworkagainstmaliciousat-
tacks.However,theissuanceofnewcryptocurrencyhasbeenshowntoresultineconomic
concentration,regardless oftheunderlyingconsensusalgorithmemployed[ 11,12].
Given the fast-paced evolution of the crypto ecosystem, it is not surprising that the
Ether valuation - tracked by its market price - experienced cycles of booms and busts.
Ourdatasetforinstanceincludesthesigniﬁcantsurgeandcrashin2017-2018duringthe
period commonly referred to as the “ICO Craze”, where ICO stands for “Initial Coin Of-
fering”,a clearreferencetothe“Initial PublicOﬀering” in traditional ﬁnance.Duringthis
time, theEthereum market wasinundated with a largenumber of new tokens and proto-
cols;whilesomeoftheseprojectsintroducedinnovativeideasanddemonstratedﬁnancial
vision,themajoritywereeithershort-livedattemptstocapitaliseonthemomentumor,in
somecases,outrightfraudulentschemes[ 13].
Several recent studies have characterised the value transfers in cryptocurrencies via
transaction network representations [11, 14–18]. Ethereum itself has also been analysed
in its multi-layered economy encompassing multiple tokens and services [19–22]. These
network-based approaches have delivered signiﬁcant insights into the structural and dy-
namic properties of their networks. In particular they showed a growing degree of spe-
cialisationofagentsandanincreasedlevelofintermediation,adynamicsthatmimicsthe
evolutionoftraditionalﬁnancialandeconomicsystemsfrompeer-to-peertocentralised,
hub-and-spoketopologies.Inourworkwecomplementthisperspectivebycharacterising
thetopologicaldistributionofthevelocityofmoneyacrossthesetransactionnetworks.

---

## Page 5

DeCollibusetal. EPJDataScience           (2025) 14:11 Page4of23
T h er e s to ft h ep a p e ri so r g a n i s e da sf o l l o w s :i nS e c t .2 we introduce the concept of
MicroVelocity and its theoretical foundations; in Sect.3 we report our methodological
frameworkandcharacteriseourvelocityestimator;inSect. 4wereporttheresultsofour
analysisoftheEthercryptocurrency;Sect. 5concludes the paper.
2M i c r o V e l o c i t y
ThedeﬁnitionofMicroVelocityasin[ 5]wasbuiltonthemodelofWangetal.[ 23],where
thestatisticaldescriptionofthevelocityofmoneycirculationisbasedontheholdingtime
ofmoney,deﬁnedasthetimeintervalbetweentwotransactions.Theydeﬁnetheholding
time as a random variable, whose probability distribution is determined by the hetero-
geneity of economic agents’ behaviours. Thanks to this modelling approach, velocity can
beexpressedasanequilibriumpropertyoftheeconomy,connectingthemacroeconomic
variabletothemicroeconomicchoicesofeveryagent.
The original argument by Wang et al. can be summarised as follows: consider the time
between two transactions involving the same unit of currency, the holding timeτ,a n d
assumethat τisarandomvariablewithprobabilitydistribution p(τ).Acondition p(0)=0
has to be enforced since a holding time of 0 is meaningless for the description. Deﬁning
M the total number of coins in circulation,Mp(τ)dτis the number of coins with a hold-
ing time in the interval[τ,τ+ dτ). Assuming stationarity ofp(τ),t h em o n e yﬂ o wF(τ)
generatedbycoinswithholdingtime τis:
F(τ)=M1
τp(τ)dτ (3)
The total circulating ﬂow in the economy amounts, by deﬁnition, toF =PQ.I ti st h e n
straightforwardtointegrateEq.( 3)forall τ>0toﬁnd
MV =F =
∫︂∞
0
F(τ)=M
∫︂∞
0
1
τp(τ)dτ (4)
Andthusitfollowsthatvelocityreads:
V =
∫︂+∞
0
1
τp(τ)dτ (5)
Oneconsideration canbe madeon theassumption ofstationarity, i.e. thatp(τ)is inde-
pendentoftime t.AsshowninMattssonetal.[ 4]thiscanberelaxedbyincorporatingan
explicittimedependence
F(τ;t)dt=M(t)1
τp(τ;t)dτdt (6)
wheretheaboveequation,ifintegratedinatimeinterval t ∈ [T0,T1]andover τ∈ [0,+∞ ),
leadstoEq.( 3)inthepaper[ 4].F(τ;t)istheﬂowdensitygeneratedbycoinswithholding
time τ: integrating over all holding times in the economy gives the total ﬂow in the time
interval [t,t+dt)
F(t)dt=
(︃∫︂∞
0
F(τ;t)dτ
)︃
dt=M(t)
(︃∫︂∞
0
1
τp(τ;t)dτ
)︃
dt

---

## Page 6

DeCollibusetal. EPJDataScience           (2025) 14:11 Page5of23
F(t)isthentheinstantaneousdensity ofﬂowforthewholeeconomy,anddividing itby
thenowtime-varying supply M(t)givesaninstantaneousmeasureofvelocity
V(t)= F(t)
M(t)dt=
(︃∫︂∞
0
1
τp(τ;t)dτ
)︃
dt (7)
Thisdepictionmapstotheonegiven byMattsson etal.[ 4]if T =T1 – T0 → 0.
In our case, time is intrinsically discrete since transfers can only happen when a new
block is appended to the blockchain. It follows that bothM(t) and F(t) are piece-wise
constantfunctionsovereachunittimeincrementwhen t isdiscretisedinblocktimes,i.e.
M(t) = M(b) and F(t)= F(b) for t ∈ [tb,tb +1 ),w h e r etb is the timestamp associated with
block bintheblockchain.Consequentlywecanmeasurethevelocityatblock bas
V(b) = F(b)
M(b) =
∞∑︂
τ=1
1
τP(b)(τ) (8)
This in practice amounts to calculatingF(b) via the estimation of the probability mass
function P(b)(τ), which replaces the probability densityp(τ;t) f o rd i s c r e t et i m e s .W ew i l l
discusst hepracticalim plemen ta tionindetailinSect.3.
Another core assumption of the original model by Wang et al. [23]i st h a tu n i t so fc u r -
rencycannotbedistinguishedfromoneanother,i.e.thattheyare fungible.Thevelocityof
money is then an emerging property of the economy, arising from theaveragebehaviour
ofagentsspendingtheirincomesmoreorlessquickly.Thisbringstolighttheunderlying
reason to deﬁne MicroVelocity as done in Campajola et al. [5] :w h i l ei ti st r u et h a tu n i t s
of money are fungible, individuals that make up the economy are not. Indeed there is lit-
tle reason to believe that Eq. (5)i si na n yw a yr e p r e s e n t a t i v eo ft h eb e h a v i o u ro fa l lt h e
diﬀerent entities that participate in the economy, as it only describes theaveragevelocity
of money. Depending on agent characteristics, e.g. their business, wealth or income, the
holdingtimesdistributionofagivenagentcanbedramaticallydiﬀerentfromtheonethat
describes an average coin in the economy. This also means thatV can be reframed as an
average of averages: the average velocity of an agent’s coin, averaged over all the diﬀerent
agents.
Letusthendeﬁne p
i(τ;t)asthedistributionofholdingtimesoftokensheldbyagent iat
time t,w i t hi ∈{1,2,..., N}. CallingMi(t) the amount held at timet by agenti,s u c ht h a t∑︁
i Mi(t)=M(t),wecanr ewrit eEq.(7)as
V(t)=
(︄∫︂∞
0
1
τ
∑︂
i
Mi(t)
M(t)pi(τ;t)dτ
)︄
dt=
= 1
M(t)
∑︂
i
(︃∫︂∞
0
1
τMi(t)pi(τ;t)dτ
)︃
dt= 1
M(t)
∑︂
i
Mi(t)Vi(t) (9)
wherewehaveintroducedtheindividual MicroVelocity
Vi(t)=
(︃∫︂∞
0
1
τpi(τ;t)dτ
)︃
dt (10)

---

## Page 7

DeCollibusetal. EPJDataScience           (2025) 14:11 Page6of23
andusedthefactthat
p(τ;t)=
∑︂
i
Mi(t)
M(t)pi(τ;t).
We can also easily derive a discrete time form of MicroVelocity, which will be useful in
thespeciﬁccaseofablockchainapplication.RepeatingthelogicalstepsleadingtoEq.( 8),
weﬁnd
V(b)
i =
∞∑︂
τ=1
1
τP(b)
i (τ). (11)
The total velocityV(t) then is thewealth weighted averageof individual contributions,
the MicroVelocitiesVi(t). As a consequence, in a population with homogeneous spend-
ingpatterns,thecontributionstomoneyvelocityareuniquelydeterminedbywealth.But
in real world economies the heterogeneity of participants (institutions, households, gov-
ernmentsetc.)andoftheirspendinghabitsaﬀectstheirMicroVelocities.Themacroscale
thereforeemergesasacompositionofmanymicroscales,muchlikethemacroscopictem-
peratureofagasemergesfromthemovementandcollisionoftheatomsthatcomposeit.
Wang et al. [23]didnotconductempiricalstudiestovalidatetheirtheoreticalapproach,
but limited their tests to computer simulations, also due to the lack of complete, micro-
leveltransactiondata.Theinnovationprovidedbypublicblockchains,wherebydefaultall
transactionsarevisibleinsidetheledger,oﬀersnowtheuniqueopportunitytodetermine
MicroVelocitiesinareal-worldscenario,measuredonacurrencythatoperatesonaglobal
scale,ratherthanbeing conﬁnedtoaregionalscope.WhiletheoriginalstudyofMicroV-
elocity [5] focused on UTXO-based blockchains, in this paper we analyse the Ethereum
blockchain, which is account based, and the velocity of its native cryptocurrency, Ether.
Further studies have applied similar frameworks to other digital currencies: notably the
already mentioned Mattsson et al. [4] proposed a modiﬁed version of the Wang et al. ar-
gument and applied it to a community currency in Kenya. However, in their approach
coins are considered to contribute to velocity only within the time period in which they
arespentratherthanthroughouttheirentireholdingperiod.Wediscussthisdiﬀerencein
more detail in the next section as we describe our estimator, and leave a more thorough
comparisonofthetwoapproachesforfutureresearch.
3 Dataandmethodologies
3.1 MeasuringMicroVelocity
The estimation ofMicroVelocityfollowsfromthe deﬁnition in Eq.(10). Inthesamplewe
considered,eventsarerecordedontheEthereumblockchainevery13.5secondsonaver-
age, when a new block is added. The Ethereum Proof-of-Work protocol - which was the
consensusprotocoluntilSeptember2022-triestomaintaintheinter-blocktimebetween
12to20secondbyadjustingthediﬃcultyofthecryptographic“puzzle”.Theconsequence
isthattimeiseﬀectivelydiscretized,and τiseasilyexpressedintermsofnumberofblocks
betweentransactions, τ∈N\{0}.Blockswillthereforebeusedasourunitoftime,unless
otherwisespeciﬁed.
We measureF
(b) by ﬁrst estimating the currentP(b)(τ) = p(τ;tb), i.e. the holding time
distribution at the time of blockb, which is deﬁned over all tokens in the economy, not

---

## Page 8

DeCollibusetal. EPJDataScience           (2025) 14:11 Page7of23
only the ones that are being transacted in blockb. This means that our holding times are
measured over the entire dataset: if a token being held at blockb is being spent atb′>b,
then its holding time is also taken into account in theP(b)(τ). All tokens that are never
transacted beyond blockb are considered to be held indeﬁnitely, thus producing a null
contributiontotheﬂowandtovelocity.
Weestimatetheholdingtimesprobabilitymassfunction P(b)
i (τ)foruser i’scoinsatblock
busingtheempirical frequencies
ˆP(b)
i (τ)= w(b)
i (τ)
M(b)
i
(12)
where w(b)
i (τ) is the total amount of coins ini’s wallet with holding timeτ, M(b)
i is their
balance at blockb and, trivially,∑︁
τw(b)
i (τ) = M(b)
i . Plugging this into Eq. (11)g i v e st h e
empiricalestimatorofagent i’s MicroVelocity at blockb
ˆV(b)
i =
∑︂
τ
1
τ
w(b)
i (τ)
M(b)
i
(13)
or,fortheentiresupply,
ˆV(b) = 1
M(b)
∑︂
i
M(b)
i ˆV(b)
i =
∑︂
τ
1
τ
w(b)(τ)
M(b) (14)
whose unit of measurement isblocks–1 or b–1 in short, and where we have introduced
w(b)(τ)asthetotalamountofcoinswithagivenholdingtime.Weneglectadditionalcon-
siderationsonthedeﬁnitionofcirculatingsupply,astheywouldrequirearbitraryassump-
tionsandwouldhaveamarginalimpactonourresults.
Notably, this estimator is a lower bound to the true value ofV (b),i . e .V(b) ≥ ˆV(b).T h i s
comes from the fact that the frequency estimator of theP(b)
i (τ) suﬀers from the right-
censoring of τdue to the ﬁnite sample size, i.e. there are coins whose holding time is
n o tm e a s u r e db e c a u s et h e yw i l lb es p e n ta tb l o c k st h a ta r eb e y o n dt h ea v a i l a b l ed a t a s e t .
The impact of this right-censoring can however be quantiﬁed: callingB the last available
block in the data, letU(b)(B) be the set of coins whose holding time is unknown at block
b because they are not spent beforeB.I fac o i nc ∈U(b)(B) has been last spent at block
bc <b,itfollowsthatcoin c’sholdingtimeis τc ≥ B+1– bc.Thisimpliesthatthescenario
where ˆV(b) is most inaccurate is when allc ∈U(b)(B) get spent atB+1,t h ush a vi n gt h e
minimumunobservableholdingtime,whileitisexactwhennotransactionsoccuroutof
sample.Itfollowsthatthetruevalueof V(b) satisﬁes
ˆV(b) ≤ V(b) ≤ 1
M(b)
∑︂
τ
w(b)(τ)
τ = 1
M(b)
∑︂
τ
(︄
w(b)(τ)
τ + w(b)
U (τ)
τ
)︄
= 1
M(b)
∑︂
τ
w(b)(τ)
τ +
∑︂
c∈U(b)(T)
1
(B+1– bc) = ˆV(b) + ˆV(b)
U
Clearly,since bc <b by deﬁnition, the smaller the diﬀerenceB– band the largerthe set
U(b)(B)get, the bigger the impact of the “unseen”velocityV (b)
U .T h isr es ultiscrucia l,asi t

---

## Page 9

DeCollibusetal. EPJDataScience           (2025) 14:11 Page8of23
allowsustodeﬁne arangeofvalueswithin which thetruevelocity V (b) lieswithabsolute
certainty.
Wehaven’tyetspeciﬁedhowwemeasureholdingtimes.SinceEthereumisanaccount-
basedblockchain,itisnecessarytoadoptaruletodecidewhichcoinsarespentﬁrstwhen
generating a new transaction. We consider a Last-In-First-Out (LIFO) policy, assuming
that users tend to ﬁrst use the money that they received last. If the money from the latest
received transaction is not suﬃcient, “older” money is spent, with a larger holding time.
Thisisaneconomicallymeaningfulchoice,asitnaturallyproduces“liquid”money-what
wouldbetheM0orM1moneysupplyintraditionaleconomics-thatisalwaysatthetopof
thepockets,and“illiquid”money,whichisusedasalonger-termsaving/investmentasset.
These considerations are in broad agreement with the existing approaches to identifying
trajectoriesofmoneytransfers,asdoneinMattssonandTakes[ 24].Consistentlywiththeir
work we also tested First-In-First-Out (FIFO) and random mixing as alternative criteria,
buttheresultswerenotsigniﬁcantly diﬀerent fromtheonesusingLIFO.
Inthenextsection,whenweanalysethedistributionsofMicroVelocity,weremoveval-
uesof ˆV
(b)
i =0 b–1.Thesemayoccurformultiplereasons:theagentmayhavenotentered
themarketyetorhasquit,thustheywillhave0wealthandvelocity,butitmayalsobethat
theyowncoinsthatareneverspentagainduringtheanalysedtimeperiod.Thelattercan
itself be caused by a behavioural choice of holding the coins indeﬁnitely - the so-called
“HODLers”, a slang expression in the cryptocurrency world originated in a mistyping of
“Holders” -, by the right-censoring of data we previously discussed or by technical prob-
lemssuchaslostpasswordsorhacks:thisuncertaintyleadsustoexcludealsoagentswith
non-zerowealththathavezeroMicroVelocity.
To summarise our estimation technique, we provide a simple example of the computa-
tionof ˆV
(b)
i :thisexamplecanbefollowedinFig. 1.ConsidertheaddressofAlicereceives
transactionA,withavalueof5Ether,atblock10,followedbytransaction Bfor10Etherat
block20.Atblock30Alicesendstransaction C,withavalueof10Ether ,toBob.Sinceshe
only needs to consume the coins from transactionB, the holding time of those 10 Ether
is 10 blocks. For all the time those Ether have been in Alice’s wallet then they contribute
to her MicroVelocity by 10/10=1 Ether/block. But what if transactionC had transferred
15 Ether instead of 10? The coins Alice received at block 20 would not be enough, so she
would need to use the 5 Ether that she received in block 10. The holding time of those 5
Ether is 20 blocks, resulting in a contribution of 5/20=0.25 Ether/block to Alice’s veloc-
ity in that time frame. So in the interval of blocksb ∈ [10,20 ] the velocity contribution
M
(b)
i ˆV(b)
i ofAlicewillbe0.25Ether/block,whilefor b ∈ [21,30 ]itwouldbethesumofthis
velocitycontributionandtheonewecomputedbefore,so 1.25 Etherperblock.
It is now straightforward to turn toˆV(b)
i simply dividing by the balanceM(b)
i at each
blockb.Inthiscase ˆV(b)
Alice iszerobeforeblock10(becauseAlicehasnobalance), 0.05 b–1
in every block between block 10 and 20, 0.083b–1 between block 20 and 30, and again
zeroafterwards.
While in this example we have been talking about Alice and Bob, a limitation to inter-
pretingourresultscomesfromthefactthatEthereumhasnoaccountveriﬁcation.Inour
analysis we assume equivalence between addresses (i.e. accounts) and agents, thus disre-
gardingthefactthatthesameagentmaycontrolmultipleaccounts.Aggregatingmultiple
addressesisinprinciplepossible(asshownbyVictor[ 25])buthardtovalidate,and-given

---

## Page 10

DeCollibusetal. EPJDataScience           (2025) 14:11 Page9of23
Figure1 AsimpleexampleoftheMicroVelocityestimator:AlicestartsatBlock0withabalanceof0Ether
andreceives5Etheratblock10and10Etheratblock20.AlicesendsmoneytoBobatblock30.Duringallthis
exampleBob’stokenshaveavelocityzero,becauseheisnotsendinghismoneytoanyone
the transaction fees for moving Ether around accounts linked to the same entity - we as-
sumetheimpactofthisphenomenontobelimited.
For the sake of interpretability, the values ofˆV(b) we report in our results have been
annualised by multiplying the velocity per block by the average number of blocks in a
year.Therateofnewblocksisnotdeterministic,butonaverageiskeptatoneblockevery
13.5seconds,or2’336’000peryear.
3.2 Analysismethods
We characterise the cross-sectional distribution of the resulting individual MicroVeloci-
tiesandcontributionstothetotalvelocitybyﬁttingparametricdistributionstotheempir-
icaldata.Weﬁndthattherighttailofthesedistributionsfollowsverycloselyapower-law
p(V) ∼ V–α
whose parameters Vmin, i.e. the minimum value ofV after which the power law be-
haviourisexpected,andtailexponent αhavebeenestimatedminimisingtheKolmogorov-
Smirnovdistancefromtheempiricaldistribution asinAlstottetal.[ 26].
To complement our MicroVelocity-based estimator, in our analyses we adopt methods
fromnetworksciencethathavebeensuccessfullyappliedtocryptocurrencydatainthelit-
erature.Inparticular,weconsiderMicroVelocityasanattributeofnodesinthetransaction
networkrepresentationoftheblockchainrecords.Economicandﬁnancialnetworksoften
exhibit a “core-periphery structure” [27–29], a characteristic that has been reported also
for cryptocurrency economies [30]. These networks display a macro-level characteristic
wherea subsetofnodes(knownasthe“core”)exhibitshigh levelsofinterconnectedness,
while the remaining nodes (known as the “periphery”) have relatively few links to other
peripheralnodesandaremostlylinkedtocorenodes.
Extending the results of [30], after building weekly transaction networks of Ether, we
apply the eﬃcient core-periphery classiﬁcation algorithm from [31]t om a r kt h en o d e s
belonging to the core and the ones belonging to the periphery, and we characterise the
distribution ofMicroVelocitybetween thecoreandperipheryofthenetworks.

---

## Page 11

DeCollibusetal. EPJDataScience           (2025) 14:11 Page10of23
Wealsomeasurethecorrelationcoeﬃcientbetweenvelocitiesacrossneighbournodes,
whichwecalltheMicroVelocityassortativitycoeﬃcient,calculatedas
rv =
∑︁N
i=1
∑︁N
j=1(Vi – ¯V )(Vj – ¯V )Aij
∑︁N
i=1
∑︁N
j=1(Vi – ¯V )2Aij
(15)
where Vi is the velocity of nodei, ¯V is the average velocity of all nodes in the network,
and Aij is the adjacency matrix element indicating whether nodesi and j are connected.
A positive coeﬃcient indicates that nodes with similar velocities tend to be connected to
eachother,whileanegative coeﬃcientindicates theopposite.
3.3 Data
Forouranalysis,weemployedafullysynchronisedEthereumclienttoextractthefollowing
records:
• The genesis block, which includes the one-time initial preallocation of Ether
distributedtofounders,earlyinvestorsandsupporters(alsoknownasthe“pre-mine”).
• All mining anduncle blockrewards.
• All gasfeespaid pertransaction.
• All Ethertransfertransactionsinitiated fromExternally OwnedAccounts(EOAs).
Internal transactions, executed by Smart Contracts, are not directly stored on the
blockchain. These transactions, generated on the internal execution stack, are treated as
transient states. Only nodes running in “full archive” mode maintain a record of these
states.Forthisstudy, weextractedinternaltransactionsfromtheEtherscanAPI[ 32].
Ourdatacollectionextendsuptoblock12950000(dated3rdAugust2021),justpriorto
the“London”upgradeofEthereum.Miningrewards,inclusiveofso-called“uncle”blocks
rewards(orphanblocksnotdirectlyincorporatedintothemainchain),factorintothecal-
culationofthetotalsupply,asupplythat-unlikeBitcoin-lacksapredeterminedschedule.
The Proof of Stake consensus mechanism, introduced recently in September 2022, is be-
yond the scope of this study.
Daily Ether prices and market capitalizations have been obtained from Coinmarket-
cap.
1 OurdatasetiscomplementedbylabelsregardingaddressextractedfromEtherscan
API [32]. Etherscan uses labels to categorise and provide additional information about
Ethereum addresses, making it easier for users to identify the purpose, the owner, or the
possible aﬃliations of a given address. These labels are created and curated by Etherscan
directlytoimprovetransparencyandaidintheanalysisofon-chainactivities.
4R e s u l t s
4.1 Holdingtimesdistributions
InFig. 2weseetheempiricaldistributionofholdingtimesatdiﬀerentpointsinthehistory
of Ethereum, namely mid-November 2018, 2019 and 2020. We see that a large portion of
the supply has long holding times, with only a relatively small fraction of the Ether being
movedonhourlyordailytimescales.Thisobservationisconsistentwithotherdigitalpay-
ment systems that have been studied in the literature [3,4], where it has been found that
1https://coinmarketcap.com.

---

## Page 12

DeCollibusetal. EPJDataScience           (2025) 14:11 Page11of23
Figure2 HistogramofholdingtimesofETHon15November2018,2019and2020.Bothaxesarein
logarithmicscale
despite not paying any interest e-money is used not only as a liquid medium of exchange
butalsoasastoreofvalueoverlongertimeperiods.
As discussed in Sect.2, the MicroVelocity approach includes these infrequently ex-
changed portions of money supply in the computation, whereas to a certain extent both
theconventionalestimatorandthemorerecentlyintroducedonebyMattssonetal.would
primarilyincludeitsmostliquidportion.Sincethesecoinshaveverylargeholdingtimes,
their impact on the total velocity is marginal, but nonetheless the MicroVelocity frame-
work allows ﬂexibility in the selection of the money supply by setting a threshold in the
holdingtimesdistribution,ratherthanarbitrarilychoosingequivalenceclassessuchasthe
M0,M1orM2moneysupplies.
4.2 Transfervelocityofmoney
Our methodology leads to estimate the average transfer velocity of money in the system
as V
(b) = ∑︁
i M(b)
i V(b)
i /M(b). This means that we are able to capture a measure ofV that is
asgranularintimeaspossible,contrarytoconventionalestimatorsthatrelyonperiodical
time aggregations to calculate ﬂows (e.g. monthly or yearly). This has two consequences:
ﬁrstly, our measure is taking into account lower frequency modes in the movement of
money, i.e. portions of the monetary supply that are being held for longer than a given
time window; secondly, we are able to calculate the velocity at arbitrary points in time
without needing to resample, thus making our measure more ﬂexible than conventional
estimators.
We show in Fig.3 the comparison between the MicroVelocity-based estimatorˆV
(b) at
intervals of 4 weeks, and the conventional one based on ﬂows over the same period of
time, VConventional = FT
MTT where T is the trailing 4 weeks andMT the average supply in

---

## Page 13

DeCollibusetal. EPJDataScience           (2025) 14:11 Page12of23
Figure3 Toppanel:EstimationofthetransfervelocityofmoneyadoptingtheMicroVelocity-basedestimator
ˆV(b),andtheconventional VConventional,togetherwiththemarketpriceofEther.Pearsoncorrelationbetween V
andlogreturnsofprice,computedoverthewholedataset,is0.2594for ˆV(b) and0.2057for VConventional.
Bottompanel:Upperboundontherelativeerror
ˆV(b)
U
ˆV(b) asafunctionoftime.Weseethatevenapproachingthe
endofthedatasettheerrorisverycontained
the period. All quantities are annualised. We also report the upper bound to the true ve-
locity ˆV(b) + ˆV(b)
U , which is however barely distinguishable from the base estimator. The
maximum discrepancy occurs on the last month of data, where the upper bound to the
relative error of the MicroVelocity-based estimator - measured asˆV(b)
U / ˆV(b) -i sl e s st h a n
15%,whileforthevastmajorityofthesampleitisbelow1%,asshowninthebottompanel
of Fig.3. We stress that this is an upper bound to the error, since we have shown that the
true V(b) as deﬁned in Eq. (8)s a t i s ﬁ e sˆV(b) ≤ V(b) ≤ ˆV(b) + ˆV(b)
U : the results indicate that
theMicroVelocity-based estimatorisextremelyprecise.
Weﬁndthatthereisagoodagreementbetweenthetwo,asshouldbeexpected,butalso
that our metric captures more variability. We notice a sharp increase around the second
half of 2017 and the beginning 2018, roughly around the ﬁrst price surge of Ether, when
the market was “bullish”. Anecdotally, temporary surges in velocity seem to permanently
increasepricesofEther.Afteralong“bear”marketbetween2018and2020,weseeaseries
ofvelocitypeaksinthesecondhalfof2020andthebeginningof2021,thatcouldanticipate
thesecondsurgeinEtherprice.MicroVelocityseemstodescribethisdynamicbetterthan
Velocitycomputedintheconventionalway.
MicroVelocity distribution The MicroVelocity formulation enables the examination of
themoneyvelocitydistributionacrosseconomicagents,thuscharacterisingthediversity
among participants. In Fig.4 we plot the empirical probability density function of the
estimatedMicroVelocities ˆV
(b)
i alongsideapowerlawdistributionﬁttedviaminimisation
oftheKolmogorov-Smirnovdistance,measuredatfourdiﬀerent pointsintime.

---

## Page 14

DeCollibusetal. EPJDataScience           (2025) 14:11 Page13of23
Figure4 Empiricalprobabilitydensityfunction(PDF)ofMicroVelocities ˆV(b)
i atdiﬀerentpointsintime,
togetherwiththeiroptimalpowerlawﬁt.ThelargerpanelsatthetopshowtheresultusingtheLIFOmethod.
Thebottom-leftpanelsuseaFIFOmethod,whilethebottom-rightpanelsusearandommixingmethod.
Thesealternativemethodsyieldedstrikinglyconsistentresults
Ascanbeseen,thedistributionof Vi nicelyﬁtsapowerlawoverseveralordersofmag-
nitude,withanexponentthatisverycloseto α=2.Theobservationthatthedistribution
of Vi follows a power law implies that relatively few agents have a high velocity, i.e. they
moveaveryhighportionoftheirbalanceveryfrequently,whilethevastmajorityaremov-
ingnegligiblefractionsofit.Asisthecaseforincome,wealthandsocialconnectionsinthe

---

## Page 15

DeCollibusetal. EPJDataScience           (2025) 14:11 Page14of23
Figure5 IndividualrelativecontributionstoVelocity M(b)
i ˆV(b)
i ,isolatingthetop5contributorscomparedtoall
others
literature, interestingly velocity too is far from being equally distributed. As a robustness
check, we changed the holding time calculationcriterion fromthe economicallyjustiﬁed
LIFO(toppanels)tothealternativeFIFO(bottom-left)andrandommixing(bottom-right)
criteria. Ascanbeseenfromtheﬁgure,thediﬀerencesarenegligible.
The emergence of power laws is generally tied to generative accumulation processes
suchastheMattheworproportionalgrowtheﬀect,butalsotothecombinationofBrow-
nianmotionswithabsorbingstates,asshowninGabaix[ 33]andSaichevetal.[ 34].While
the determination of the causes of this empirical observation is outside the scope of this
paper,wewouldencouragefurtherresearchontheseaspects.
How does this distribution aﬀect the total transfer velocity? The latter is in fact the
wealth-weightedaverageoftheindividualMicroVelocities,asshownbyEq.( 14):isitalso
the case that a minimal number of accounts is responsible for the majority of the trans-
fer velocity? The individual contributions,M
iVi, also display signiﬁcant heterogeneity, as
shown in Fig.5. We can observe that as few as ﬁve accounts contribute over half of the
totalvelocityattimes.Consideringthattherearemillionsofaddressesactiveatanygiven
moment,thisﬁndingisparticularlynoteworthy.
It is important to acknowledge the remarkablelevel of inequality revealed in our study.
The broader literature on cryptocurrencies conﬁrm that the Gini index of wealth distri-
bution is exceptionallyhigh for allthe principal cryptocurrencies[21,30,35]. Even when
considering custodial exchanges, which may aggregate cryptoassets from multiple users
under a single address, the disparity in holdings is substantial, presenting a signiﬁcant
challengetotheproclaimedethosofdecentralisation.
The obvious explanation for the observations of Fig.5 would then be that the extreme
inequalityinthewealthoftheseaddressesgeneratestheheterogeneityinMicroVelocities,
astheindividual contributionsareweighted bywealthwhenaddedupinthetotal V.
Thequestionisthenwhetherthatistheonlysourceofheterogeneityorthereareother
mechanismsthatleadtotheobservations.InFig. 4,wherewearenotconsideringbalances
bylookingatthe ˆV
i themselves,weﬁndthattheheterogeneity persists.
Thequestiontheniswhethersomehiddenpropertyofagentsmayexplainbothhetero-
geneities inVi andMi.Ifso,wewouldexpecttheirvaluestobecorrelated.
To investigate this, we compute the Spearman rank correlation between balancesMi
and MicroVelocityVi. The relation betweenVi and Mi s ee m st oc h a n g eo v e rt i m e ,a n di t
appears to be signiﬁcantly positive in periods where the Ether price is about to increase.

---

## Page 16

DeCollibusetal. EPJDataScience           (2025) 14:11 Page15of23
Figure6 Spearmancorrelationbetween ˆV(b)
i andM(b)
i plottedtogetherwithEtherpriceinUSD.All
correlationcoeﬃcientsarestatisticallysigniﬁcanttothe p<0.01level
We ﬁnd this result quite surprising, as we would have expected the two quantities to be
negatively correlated, as wealthier individuals should tend to spend smaller fractions of
theirholdingsintime.
To better characterise this relation we consider the four snapshots shown in Fig.7.W e
presentascatterplotof ˆV
i versusMi,withtherespectivemarginalsatthesideoftheplot.
Theplotsshowhowtherelationbetweenbalanceandvelocityisextremelynoisythrough-
out thesampleand, despite the statistical signiﬁcance of therankcorrelations(which are
insensitivetooutliers)itishardtoattributealinearpatternbetweenthetwo.Investigating
potentialgenerative mechanismswouldhelpinshedding lightonthisrelation.
4.3 Networkanalysis
To further explore this heterogeneity we now turn our attention to MicroVelocity as a
topological property of the economy. An economic system can be represented as a net-
workoftransactions,wherenodesrepresentagentsthatareconnectedifatransactionbe-
tweenthemoccurredinagiventimeperiod,whichwechoosetobeaweekasitallowsusto
neglectintraweekseasonalpatterns(e.g.weekendshavinglessactivityetc).Thisapproach
hasbeenrecentlyappliedtoseveralcryptoeconomies[ 14,30],andwebuildonitstudying
how MicroVelocity relates to the agents’ position in these networks. This time instead of
snapshotsweconsidercumulativeweeklytransactionnetworksandcomputetheaverage
MicroVelocity of each agent in the considered time frames, that isV
i(K)= 1
|K|
∑︁
b∈K ˆV(b)
i ,
whereK isthesetofblocksaddedtotheblockchaininagivenweek.Weanalogouslytake
the average contribution to total velocityMi(K)Vi(K)asthetimeaverageof M(b)
i ˆV(b)
i .
It has to be pointed out that the MicroVelocity on a given week can still be aﬀected by
transactions happening on other weeks and that are not represented in the weekly trans-
actionnetworks.
This framework allows us to characterise how MicroVelocity relates to the networks
structure and the position of nodes within the economy, as well as investigating the rela-
tionsbetweenagentstoseehowsimilarinMicroVelocityarenodesthathavebeencoun-
terpartiesintransactions.
Using the deﬁnition we reported in Eq. (15), we calculate the assortativity coeﬃcient
forboth V
i(K)andMi(K)Vi(K),whichweshowinF ig. 8.Forbothquantitiesweconsider
alsotherankassortativitycoeﬃcient,i.e.theequivalenttoSpearman’scorrelationadapted

---

## Page 17

DeCollibusetal. EPJDataScience           (2025) 14:11 Page16of23
Figure7 ScatterplotsreportingtheestimatedMicroVelocity ˆV(b)
i andthebalance M(b)
i .Marginalsareshown
atthesideanddensityofpointsisreportedincolour
to the network topology. We choose to consider both statistics as the rank correlation is
lesssensitivetonon-normalityandoutliers,whichaswehaveshowninthedistributional
analysischaracteriseourdata.
Weobservethattheassortativitycoeﬃcientisratherstableandmildlynegativethrough-
outthesampleforthewealth-weightedMicroVelocities M
i(K)Vi(K),butiscloserto0for
t h eb a r eq u a n t i t i e sVi(K). This diﬀerence can be attributed to the wealth inequality and
its topological distribution on the network, which has been reported in [30]. The rank
correlationcoeﬃcientinsteadshowsamorevarieddynamics,particularlyduringsomeof
the most volatile periods for Ethereum around 2017-2018 and 2020. These spikes might
be interesting because they seem to anticipate the surge in total Velocity and Ether price
weseeinFig. 3.
To determine whether the assortativity coeﬃcients we calculate are statistically sig-
niﬁcant, we compute p-values by simulating 200 random reshuﬄings of theV
i(K) (or
Mi(K)Vi(K))onthenodesoftheweeklynetwork.Thisprocedureyieldssigniﬁcanceatthe
p<0.05 level for a two-tailed test against a null hypothesis that MicroVelocities are ran-
domly distributed in the network, however the alternative hypothesis is not uniquely de-
ﬁnedandamorestructuredtheoreticalmodelfortheformationofthesenetworkswould
beneeded.
IfatthepairwisecorrelationsleveltherelationbetweennetworktopologyandMicroV-
elocity is unclear, more can be said when looking at the mesoscopic structure of the net-

---

## Page 18

DeCollibusetal. EPJDataScience           (2025) 14:11 Page17of23
Figure8 Mi(K)Vi(K)(t oppanel)and Vi(K)(bottompanel)assortativityandrankassortativitycoeﬃcientsover
time,measuredonweeklytransactionnetworks.Thevelocityassortativityisalwayssigniﬁcantatthe p<0.05
levelagainstarandomassignmentof Vi onthenetwork
work, and particularly when it comes to the distribution of MicroVelocity between the
coreandperipherynodes.
In the top panel of Fig.9 we show the fraction of nodes in the core of the transaction
network (orange line), which varies from 0.7% in the ﬁrst year to then consistently stay
between 0.01% and 0.05% of the total network size from 2017 onwards, compared with
thefractionoftotalvelocitythatthesamenodescontributeonaverage,i.e.
∑︁
i∈C Mi(K)Vi(K)∑︁
iMi(K)Vi(K) ,
where C is the set of nodes in the network core, which is varying between 5% and 40%
overtime.This observation canbeexplainedbytwohypotheses, possiblycombined: one
isthatcorenodesholdafractionofthesupplythatismuchlargerthanperipheralnodes,
thuscontributingmoretotheweightedaverageofEq.( 14)becauseoftheirlargerweights;
the other is that core nodes have a much faster turnover of their assets than peripheral
nodes. Both views are consistent with the growing evidence of emerging centralised in-
termediationandspecialisationofagentsincryptoeconomies,andthankstoouranalysis
wear ea blet odiscrimina t ebetweent hetwo.
Indeed,wecanmeasuretheaveragetransfervelocityinthecoreandoutside,calculated
using Eq. (14)b u tr e s t r i c t i n gt h es u mt oi ∈C or i /∈C respectively. We show the result
in the bottom panel of Fig.9. Coins held by core nodes have approximately 10-100 times
the velocity of peripheral ones, conﬁrming a signiﬁcant behavioural diﬀerence between
thetwoclassesofeconomicagentsthatcannotbeduetothelargerbalancesofcorenodes
[30]. Notably, during the ICO bubble of 2017-2018 the diﬀerence sharply reduces, possi-

---

## Page 19

DeCollibusetal. EPJDataScience           (2025) 14:11 Page18of23
Figure9 Toppanel:Fractionofnodesclassiﬁedinthenetworkcore(orangeline)andfractionof Mi(K)Vi(K)
contributedbynodesinthecore(blueline).Bottompanel:Averagevelocityofaunitofmoneyinsidethe
core(blueline)andofaunitofmoneyoutsidethecore(orangeline)
bly due to the large quantity of ERC-20 tokens that were being launched during that pe-
riodandthatmayhavefragmentedtheEthereumcommunityintosmaller,lesscentralised
communities.
Itappearsclearthenthattheconcentrationofvelocitycontributionsinthecoreiscaused
bybotheﬀects:corenodesarewealthierthanperipheralnodes,buttheyalsohavehigher
MicroVelocity.Itisnoteworthythatthisrelationonlyemergesifthenetworkedstructure
oftheeconomyistakenintoaccount:therankcorrelationcoeﬃcientsbetweenwealthand
MicroVelocity,shown inFig. 6, wereinconclusive.
4.4 Identityoftopcontributors
ThenetworksanalysisprovidedusefulinsightabouttheheterogeneityofMicroVelocity.Is
itpossiblehowevertogainabetterunderstandingofwhoisbehindthecore/topcontribut-
ing addresses and possibly classify them? To maintain consistency in our analysis and to
keepthecomputationsagile,giventhatnetworksizeandtransfersvaryovertime,wewill
only consider the top 10 contributors to the velocity, sampled with weekly frequency. As
wehave312weeks in oursample,wecouldhaveupto 3120 topcontributingaddresses if
nonewererepeated.However,itturnsoutthatwhenweconsidertotalvelocitycontribu-
tions M
(b)
i ˆV(b)
i we only have 426 unique addresses appearing in the top 10, while for the
MicroVelocitiesthemselves ˆV(b)
i weﬁnd794uniqueaddresses,implyingthatthereissome
levelofpersistenceinbothseries.
TheﬁrstaspectwecaninvestigateiswhethertheaddressesareSmartContractsornot.
Thiscanbedeterminedthroughalgorithmicproceduresbycheckingifcodeispresentat
their address. The proportion of actual smart contracts is not particularly relevant. Our

---

## Page 20

DeCollibusetal. EPJDataScience           (2025) 14:11 Page19of23
Figure10 Frequencyoflabelsintop10velocitycontributors,sampledweekly
ﬁndings reveal that, out of the 426 top contributing addresses forM(b)
i ˆV(b)
i ,5 0a r es m a r t
contracts(likelyDeFiservices),while376arenot.Similarly,for ˆV(b)
i ,outof794addresses,
78aresmartcontractsand716arenot.
We then proceed to study the attribution of addresses to known entities. An address
maynotbeaSmartContractbutmaystillbeutilisedbynon-physicalpersons,suchasex-
changes,foundations,ICOproviders,escrowservices,orcustodians.Afeasibleapproach
to determine the purpose of an address is through labelling, a human-driven process in
which certain addresses are reclaimed by their owners or categorised in speciﬁc ways by
thecommunityorbyanexpertpanel,matchingthemtotheirownersthroughthird-party
sources. Although not all addresses are labelled, a relatively crucial subset of them is. In
ourdatasetofEthertransfersuptoJuly2021,weencounteredover160millionaddresses.
Outofthese,265,687 addresses, or0.166%,havebeenlabelledonEtherscan.
Wemeasurethefrequencywithwhichaparticularlabelappearsattachedtoanaddress
that is among the top 10 contributors ofM
i ˆV(b)
i or in the 10 addresses with the highest
MicroVelocity. In Fig.10 we show the percentage of addresses in the top 10 of velocity
contributions,measuredweekly,sortedbylabel.Weseethatthelabel“ Exchange”isfound
for more than half of top 10 contributors to the total velocity. Even the immediately fol-
lowingonesarereferringtospeciﬁcexchanges(“ Binance”, “Bitﬁnex”, “Kraken”, etc.) as it is
madeclearbythediﬀerentcolours.
On the other hand, consideringˆV(b)
i , we ﬁnd a completely diﬀerent scenario, as high-
lighted by Fig.11. More than 90% of addresses in the top 10 have no label: while this is
signiﬁcantly less than the 99.834% that one could expect by picking random addresses, it
is nevertheless clear that the results are much less sharp than when weighting by wealth.
The most frequent label to appear is now “Mining”: we indeed expect mining pools and
miningrelatedaddressestohaveahigherMicroVelocity,sincetheyredistributethefreshly
minedEthertotheirpoolmembersrelativelyquickly.Exchangesstillfeatureprominently,
with “Fiat Gateway” collecting all the payment providers used by exchanges to onboard
clients and exchange their ﬁat money for Ether or other tokens, and popular exchanges

---

## Page 21

DeCollibusetal. EPJDataScience           (2025) 14:11 Page20of23
Figure11 Frequencyoflabelsintop10velocitynodes,sampledweekly.The“Nolabel”addressesnow
accountformorethan90%andarenotreportedforthesakeofreadability
“Gemini”and“Coinbase”soonafter.Interestingly,thewell-knownPonzischeme“ Celsius
Network”2 featuresprominentlyinthischart.
5C o n c l u s i o n s
Inthisarticle,wecontributedanovelimplementationoftheMicroVelocityﬁrstproposed
byCampajolaetal.[ 5],adaptingittothecontextofEthereumandaccount-basedsystems
byintroducingLIFOtransactionmatchingasaspendingrule.Moreover,weaddedtothe
theorybycalculatingtheupperboundtotheerroroftheMicroVelocity-basedestimatorof
thetransfervelocityofmoneyduetotheright-censoringofdata, ˆV
(b)
U .W ehaveshownthat,
at least for the dataset at hand, this error is mostly negligible, making theˆV(b) estimator
a strong choice to compute the transfer velocity of money given micro-level transaction
data.
We then characterised the distribution of MicroVelocity in the Ethereum ecosystem,
ﬁndingastrongheterogeneitycharacterisedbyafat-tailedpowerlawdistribution,ingen-
eral agreement with the existing measurements made on UTXO-based cryptocurrencies
[5]. We ﬁnd the tail exponent of the power law to be relatively stable and close toα=2,
whichisslightlyhigher-suggestingathinnertail-thantheonereportedforUTXO-based
systems.
While the inequality of wealth has been extensively studied and attributed to various
factors, such as the “Matthew” or “rich get richer” eﬀect, the reasons for signiﬁcant dis-
parities in MicroVelocity remain unclear and require deeper theoretical work. Agents on
the Ethereum blockchain exhibit diverse behaviours: when we analyse each agent’s con-
tributiontothetotalvelocity-afunctionoftheirwealth, M
(b)
i ˆV(b)
i -weﬁndthatthenodes
with the highest balance, often aligned with the centralised ﬁnancial sector of the cryp-
toasseteconomy,areindeedthemostsigniﬁcantcontributors.Exchangesandcustodians
notably account for the majority of these contributions, as our labels analysis showed in
Fig.10.
However,thelandscapeshiftsmarkedlywhenweconsiderMicroVelocity, ˆV(b)
i ,whichis
not a function of agents’ wealth. In this context, addresses with high throughput, such as
2UnitedStates Attorney Oﬃce, PressRelease Number: 23-248.

---

## Page 22

DeCollibusetal. EPJDataScience           (2025) 14:11 Page21of23
those associated with distributing mining rewards, ﬁat gateways and Ponzi schemes, rise
to the top of the ranks.
The complex topology of the economic system also plays a crucial role in characteris-
ing this heterogeneity. The transaction network representation highlights how the core-
periphery structure is matched by a concentration of high balance and high velocity
nodes in the core, which we ﬁnd to be consistent with the growing evidence that crypto
economies are much more centralised and intermediated than one would expect. In this
respect, the MicroVelocity measure oﬀers an additional feature to characterise complex
economic systems, integrating the topological information captured by network struc-
ture with the speed at which money ﬂows through the system. Our results support the
argument that the velocity of money is an emergent property of the system, aggregat-
ingbehaviouralpatternsandbusinessmodelsatthemicro-levelintothemacroeconomic
quantity. There could be intrinsic and extrinsic motivations for the strong heterogeneity
of ˆV
(b)
i in time and between agents: risk-aversion, motivation to hold cryptocurrencies
as investment or for political ideas, preferred areas of investment (such as DeFi, trading,
lending), price volatility, pressures from regulators, availability of exchanges, to name a
few. Users might be using Ether as a store of value, while others may be using it for ev-
eryday transactions, or to conduct hard-to-predict investment patterns in Decentralised
Finance(DeFi)protocolswhichuseEthereumtoruntheirSmartContracts.
Our contribution does not apply exclusively to cryptocurrencies. In this paper we laid
outaconceptualframeworkforcomputingvelocityatthemicroscaleofindividualagents
(MicroVelocity), being able to characterise them in their diversity of behaviour. We used
cryptocurrenciesbecauseofthefullvisibilitywehaveintransactions,balancesandtrans-
fers, but the framework can be easily adapted to more traditional payment and currency
systems.Withthegrowingavailabilityofdataanddiﬀusionofdigitalcurrencies,MicroV-
elocityprovidesmoregranularandtimelyinformationaboutthemodiﬁcationsinvelocity
comparedtoconventionalmethods.
Moreover, instead of relying on the conventional and arbitrary selection of equivalent
asset classes like M0, M1, or M2 money supplies, the MicroVelocity framework provides
a more adaptable approach to determining the money supply by establishing a threshold
within thedistribution ofholdingtimes.
For future research we aim to extend this methodology to traditional economic sys-
tems, with the potential to inform monetary policymaking by nowcasting lagging eco-
nomic indicators like inﬂation and GDP, as well as forecasting the impact of policy at a
more granular level. Lastly, we envision that ﬁnding generative processes that generate
theobservedpowerlawdistributionofMicroVelocitieswouldbearemarkabletheoretical
achievement,asthecomprehensionoftheunderlyingmechanismscouldpavethewayto
theunderstanding ofabroaderclassofeconomicalproblems.
Abbreviations
API,ApplicationProgrammingInterface;CBDC,CentralBankDigitalCurrency;DEFI,DecentralizedFinance;EOA,Externally
OwnedAccount;ERC-20,EthereumRequestforComments-20-FungibleTokens;ETH,Ether,Ethereum’scryptocurrency;
FIFO,First-In-First-Out;FT,FungibleToken;GDP,GrossDomesticProduct;ICO,InitialCoinOﬀering;LIFO,Last-In-First-Out;
NFT,Non-FungibleToken;PDF,ProbabilityDensityFunction;SC,SmartContract;UTXO,UnspentTransactionOutput.
Acknowledgements
Theauthorsthankananonymousreviewerforsigniﬁcantimprovementstotheﬁrstversionofthemanuscript.

---

## Page 23

DeCollibusetal. EPJDataScience           (2025) 14:11 Page22of23
Authorcontributions
CCandCJTdevelopedthetheoreticalframework.FMDCandCCadaptedthemethodology.FMDCcollectedthedata,ran
theexperiments,analysedtheresultsandwrotetheinitialversionofthedraft.CCdirectedtheresearchandsuggested
theanalysismethods.Allauthorsreviewedandapprovedthisversion.
Funding
CCacknowledgespartialﬁnancialsupportfromSwissNationalScienceFoundationGrant#200021_18265.
Dataavailability
ThedataofthispaperispubliclyavailablefromanysynchronisedEthereumNode.Forconveniencethedataisalso
publiclyavailablefromtheGoogleCloudPlatform
3.ThesourcecodeusedfortheanalysisofMicroVelocityhasbeen
publishedonanopensourcerepository 4.Furtherinformationisavailablefromtheﬁrstauthoruponrequest.
Declarations
Competinginterests
Theauthorsdeclarethattheyhavenocompetinginterests.
Authordetails
1BlockchainandDistributedLedgerTechnologiesGroup,UniversityofZurich,Andreasstrasse15,8050,Zurich,
Switzerland. 2UZHBlockchainCenter,UniversityofZurich,Andreasstrasse15,8050,Zurich,Switzerland. 3DLTScience
Foundation,London,UnitedKingdom. 4InstituteofFinanceandTechnology,UniversityCollegeLondon,London,United
Kingdom.
Received:27November2023 Accepted:26December2024
References
1. MishkinFS(2007)Theeconomicsofmoney,banking,andﬁnancialmarkets.Pearson/AddisonWesley,Boston
2. FisherI(1911)Thepurchasingpowerofmoney:itsdeterminationandrelationtocredit.Interestandcrises.
Macmillan,NewYork
3. MbitiI,WeilDN(2013)Thehomeeconomicsofe-money:velocity,cashmanagement,anddiscountratesofm-pesa
users.AmEconRev103(3):369–374. https://doi.org/10.1257/aer.103.3.369
4. MattssonCES,LuedtkeA,TakesFW(2023)Inverseestimationofthetransfervelocityofmoney. arXiv:2209.01512
5. CampajolaC,D’ErricoM,TessoneCJ(2022)MicroVelocity:rethinkingtheVelocityofMoneyfordigitalcurrencies.
arXiv:2201.13416
6. PerniceIGA,GentzenG,ElendnerH(2021)CryptocurrenciesandtheVelocityofMoney.CryptoeconSyst. https://
cryptoeconomicsystems.pubpub.org/pub/pernice-cryptocurrencies-velocity
7. ZhangY,ChegeniM,TessoneC(2024)Velocity,HoldingTimeandLifespanofCryptocurrencyinTransactions. arXiv:
2406.16587
8. BordoMD,LevinAT(2017)entralbankdigitalcurrencyandthefutureofmonetarypolicy.NationalBureauof
EconomicResearch.WorkingPaperNo.23711. https://doi.org/10.3386/w23711
9. ButerinV(2013)Ethereumwhitepaper:anextgenerationsmartcontract&decentralizedapplicationplatform
10. SchärF(2021)Decentralizedﬁnance:onblockchain-andsmartcontract-basedﬁnancialmarkets.FederalReserve
BankofStLouisReview,SecondQuarter2021,153–174. https://doi.org/10.20955/r.103.153-74
11. VallaranoN,SquartiniT,TessoneCJ(2023)ExploringtheBitcoinMesoscale. arXiv:2307.14409
12. LiS-N,SpychigerF,TessoneCJ(2023)Rewarddistributioninproof-of-stakeprotocols:atrade-oﬀbetweeninclusion
andfairness.IEEEAccess11:134136–134145. https://doi.org/10.1109/ACCESS.2023.3336418
13. ZetzscheDA,BuckleyRP,ArnerDW,FohrL(2019)Theicogoldrush:it’sascam,it’sabubble,it’sasuperchallengefor
regulators.HarvInt’lLJ60:267
14. BovetA,CampajolaC,MottesF,RestocchiV,VallaranoN,SquartiniT,TessoneCJ(2022)Theevolvingliaisonsbetween
thetransactionnetworksofbitcoinanditspricedynamics.JPSConfProc40:011002. https://doi.org/10.7566/JPSCP.
40.011002
15. VallaranoN,TessoneCJ,SquartiniT(2020)Bitcointransactionnetworks:anoverviewofrecentresults.FrontPhys8.
https://doi.org/10.3389/fphy.2020.00286
16. LinJ-H,PrimicerioK,SquartiniT,DeckerC,TessoneCJ(2020)Lightningnetwork:asecondpathtowards
centralisationofthebitcoineconomy.NewJPhys22:083022. https://doi.org/10.1088/1367-2630/aba062
17. KondorD,PósfaiM,CsabaiI,VattayG(2014)Dotherichgetricher?Anempiricalanalysisofthebitcointransaction
network.PLoSONE9(2):86197
18. MakarovI,SchoarA(2021)Blockchainanalysisofthebitcoinmarket.Technicalreport,NationalBureauofEconomic
Research
19. FerrettiS,D’AngeloG(2020)OntheEthereumblockchainstructure:acomplexnetworkstheoryperspective.Concurr
ComputPractExp32(12):5493. https://doi.org/10.1002/cpe.5493
20. KondorD,BulatovicN,StégerJ,CsabaiI,VattayG(2021)Therichstillgetricher:empiricalcomparisonofpreferential
attachmentvialinkingstatisticsinbitcoinandEthereum.FrontBlockchain4. https://doi.org/10.3389/fbloc.2021.
668510
21. DeCollibusFM,PartidaA,PiškorecM,TessoneCJ(2021)Heterogeneouspreferentialattachmentinkey
Ethereum-basedcryptoassets.FrontPhys9. https://doi.org/10.3389/fphy.2021.720708
3https://cloud.google.com/blockchain-analytics/docs/dataset-ethereum.
4https://github.com/fdecollibus/MicroVelocityAnalyzer.

---

## Page 24

DeCollibusetal. EPJDataScience           (2025) 14:11 Page23of23
22. DeCollibusFM,PiškorecM,PartidaA,TessoneCJ(2022)Thestructuralroleofsmartcontractsandexchangesinthe
centralisationofEthereum-basedcryptoassets.Entropy24(8):1048. https://doi.org/10.3390/e24081048
23. WangY,DingN,ZhangL(2003)Thecirculationofmoneyandholdingtimedistribution.PhysA,StatMechAppl
324(3):665–677.https://doi.org/10.1016/S0378-4371(03)000
24. MattssonCE,TakesFW(2021)Trajectoriesthroughtemporalnetworks.ApplNetwSci6(1):35
25. VictorF(2020)AddressclusteringheuristicsforEthereum.In:Financialcryptographyanddatasecurity:24th
internationalconference,FC2020,KotaKinabalu,Malaysia,February10–14,2020,Revisedselectedpapers,Springer,
Berlin,pp617–633. https://doi.org/10.1007/978-3-030-51280-4_33
26. AlstottJ,BullmoreE,PlenzD(2014)Powerlaw:apythonpackageforanalysisofheavy-taileddistributions.PLoSONE
9(1):1–11.https://doi.org/10.1371/journal.pone.0085777
27. BorgattiSP,EverettMG(2000)Modelsofcore/peripherystructures.SocNetw21(4):375–395
28. BaruccaP,LilloF(2016)Disentanglingbipartiteandcore-peripherystructureinﬁnancialnetworks.ChaosSolitons
Fractals88:244–253
29. BardosciaM,BattistonS,CaccioliF,CaldarelliG(2017)Pathwaystowardsinstabilityinﬁnancialnetworks.Nat
Commun8(1):1–7
30. CampajolaC,CristodaroR,DeCollibusFM,YanT,VallaranoN,TessoneCJ(2022)TheEvolutionofCentralisationon
CryptocurrencyPlatforms. arXiv:2206.05081
31. LipSZ(2011)Afastalgorithmforthediscretecore/peripherybipartitioningproblem.arXivpreprint. arXiv:1102.5511
32. EtherscanAPIDocumentation.Accessedon03.01.2023. https://etherscan.io/apis
33. GabaixX(2009)Powerlawsineconomicsandﬁnance.AnnuRevEcon1:255–293
34. SaichevA,MalevergneY,SornetteD(2010)TheoryofZipf’slawandbeyond.Lecturenotesineconomicsand
mathematicalsystems,vol632.Springer,Harmondsworth
35. SaiAR,BuckleyJ,LeGearA(2021)Characterizingwealthinequalityincryptocurrencies.FrontBlockchain4. https://
doi.org/10.3389/fbloc.2021.730122
Publisher’sNote
SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmapsandinstitutionalaﬃliations.

---
