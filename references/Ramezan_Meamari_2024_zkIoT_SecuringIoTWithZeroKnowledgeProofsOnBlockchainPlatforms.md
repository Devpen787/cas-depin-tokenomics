# Ramezan_Meamari_2024_zkIoT_SecuringIoTWithZeroKnowledgeProofsOnBlockchainPlatforms.pdf

## Page 1

zk-IoT: Securing the Internet of Things with
Zero-Knowledge Proofs on Blockchain Platforms
Gholamreza Ramezan
FidesInnova
g2n@fidesinnova.io
Ehsan Meamari
FidesInnova
e2i@fidesinnova.io
Abstract—This paper introduces the zk-IoT framework, a
novel approach to enhancing the security of Internet of Things
(IoT) ecosystems through the use of Zero-Knowledge Proofs
(ZKPs) on blockchain platforms. Our framework ensures the
integrity of firmware execution and data processing in potentially
compromised IoT devices. By leveraging the concept of ZKP, we
establish a trust layer that facilitates secure, autonomous com-
munication between IoT devices in environments where devices
may not inherently trust each other. The framework includes
zk-Devices, which utilize functional commitment to generate
proofs for executed programs, and service contracts for encoding
interaction logic among devices. It also utilizes a blockchain layer
and a relayer as a ZKP storage and data communication protocol,
respectively. Our experiments demonstrate that proof generation,
reading, and verification take approximately 694, 5078, and 19
milliseconds in our system setup, respectively. These timings
meet the practical requirements for IoT device communication,
demonstrating the feasibility and efficiency of our solution. The
zk-IoT framework represents a significant advancement in the
realm of IoT security, paving the way for reliable and scalable
IoT networks across various applications, such as smart city
infrastructures, healthcare systems, and industrial automation.
Index Terms—Zero-knowledge proof, Internet of Things, func-
tional commitment, blockchain.
I. I NTRODUCTION
Internet of Things (IoT) refers to a network of intercon-
nected physical devices, objects, or “things” that are embedded
with sensors, software, and network connectivity, allowing
them to collect and exchange data over the Internet. IoT
applications range from items such as wearable devices, smart
home appliances, and drones to more specialized industrial
equipment and vehicles. IoT technology enables these devices
to communicate with each other and with central systems,
enabling data collection, monitoring, and automation.
A significant challenge facing IoT is ensuring trust. Without
robust security mechanisms to ensure mutual trust among IoT
devices, the functionality of each IoT device remains isolated,
limiting the full potential that could be realized through
integrated IoT solutions. An adversary may interfere with the
device’s firmware or modify its hardware or software to gen-
erate incorrect output from a legitimate device, posing a threat
to the integrity of the device’s computations. Additionally, the
adversary may introduce a rogue IoT device to generate and
transmit data to other users or IoT actuators, compromising
the system’s integrity. Hence, the concern about IoT functions,
which is a result of executing its firmware or program, hinders
the ability to fully leverage the interconnected capabilities of
IoT device [1].
Addressing the above-mentioned challenge not only ensures
the integrity of executed computations but also paves the way
for autonomous IoT device communication. The scheme en-
ables mutually distrustful IoT devices, that are from different
manufacturers and are in separate IoT ecosystems such as Ring
and Ecobee IoT systems, to perform distributed computations
that run indefinitely, while ensuring that the correctness of
every intermediate state of the computation can be verified
efficiently. For instance, in the electric vehicle sector, repre-
sented by companies like Tesla, a decentralized trusting IoT
framework would enable cars to securely communicate and
receive real-time information about road conditions from vehi-
cles traveling in the opposite direction. Additionally, it ensures
that various components within a vehicle can authenticate
whether commands received from the car’s main computer
are the result of legitimate computation (not hacked system),
thereby establishing trust in the system’s integrity.
The mentioned trust challenge can be addressed through
the use of IoT devices built within a single IoT device
manufacturer ecosystem. However, IoT devices are engineered
across diverse ecosystems by various manufacturers, leading
to a situation where the specific functionalities encoded within
their firmware are not consistently disclosed. However, the
principal features of their operational capabilities are generally
recognized. Furthermore, companies may be reluctant to share
detailed information about the architecture or firmware of their
devices.
Zero-Knowledge Proof (ZKP) is a cryptographic technique
enabling one party (the prover) to demonstrate the truth of
a statement to another (the verifier) without revealing any
information beyond the statement’s truth itself. Fig. 1 illus-
trates the roles of the prover and verifier in a ZKP scenario.
Here, the prover shares only the output of a specific function,
without disclosing the input (secret), along with a proof. In the
ZKP realm, functional commitment is a protocol that hides a
function f from the verifier, yet allows the verifier to confirm
the correctness of the function’s execution without needing to
rerun it or know the precise function [2], [3].
Tackling the issue of computational integrity within the IoT
realm paves the way for the development of solutions that
facilitate autonomous device communication among devices
that may not inherently trust each other. Moreover, various
arXiv:2402.08322v2  [cs.CR]  19 Feb 2024

---

## Page 2

Prover Verifier
(y = F(x), ㄫ )
 x  = Input
 F = Compute
 y  = Output
ㄫ  = Proof
Fig. 1: Key components of zero-knowledge proofs (ZKPs).
IoT Device at Step 1
f1 f2兀1  for  “y1=f1(x1)”
IoT Device at Step 2
(x1,    )
(x1,    )
(y’
1, 兀’1) → (x
3, 兀3)
f3
兀’1  for  “y’1=f1(x1)”
IoT Device 
at Step 3
f4
IoT Device at Step 4
(y1, 兀1) → (x2, 兀2) (y2, 兀2) → (x41, 兀41)
兀2  for  “y2=f2(x2)”
(y4, 兀4)
input output
(y3, 兀3) → (x
42, 兀42)
兀3  for  “y3=f3(x3)”
Fig. 2: A sample Internet of Things (IoT) devices setup.
traditional IoT attacks can be addressed such as the injection
of malicious code that can alter processing results.
In the realm of automatic IoT device communication, every
device at every step of a communication process should trust
the data generated by the previous step’s IoT device. proof-
carrying data (PCD) primitive enables the composition of
proofs to attest to the correctness of computations [4]. This
primitive is particularly significant in scenarios where data and
computations need to be verified across multiple parties (e.g.,
IoT devices) that may not fully trust each other. PCD allows
for constructing proofs that not only certify the correctness of a
computation but also carry data relevant to that computation.
These proofs can be composed, meaning that the output of
one computation, along with its proof, can be used as an
input to another computation, creating a chain of trustworthy
computations. This concept is crucial in decentralized systems,
such as blockchain technology, where trust and verification are
distributed among many participants [4].
Fig. 2 demonstrates the application of PCD in the IoT
domain. The process initiates with a known input x1. This
input is then processed by an IoT device, which applies
function f1 to x1 along with any other internal inputs it may
receive from its sensors. Subsequently, the device produces
an output and a proof verifying that the function has been
executed correctly. This sequence persists until the final IoT
device in the chain generates the output and proof for its
operation.
This paper proposes a framework designed to automate
communication among untrusted IoT devices, thereby expand-
ing IoT functionalities and enabling innovative IoT services
that are not achievable by an isolated IoT device or a collection
of IoT devices controlled by a central authority. The main
contributions of this paper are as follows.
• We introduce the zk-IoT framework, designed for auto-
matic communication between untrusted IoT devices. It
comprises components including zk-Devices, blockchain
nodes, relayers, and service contracts, as well as a
blockchain protocol and a ZKP scheme.
• We introduce a ZKP scheme designed to ensure the
integrity of IoT firmware execution through functional
commitment (FC) within a distributed IoT setup.
• We also introduce several key concepts: a service con-
tract, which encodes the interaction logic among IoT
devices; zk-Devices, which utilize ZKP to generate proofs
of IoT firmware execution; and a blockchain protocol,
designed for automatic communication between untrusted
IoT devices.
• We include a performance evaluation within a blockchain
context, demonstrating the feasibility of implementing the
zk-IoT framework.
This paper is structured as follows. In Section 2, we review the
related works. Section 3 will introduce the proposed zk-IoT
framework. In Section 4, we perform a performance analysis.
Section 5 concludes.
II. R ELATED WORK
This section provides an overview of existing ideas on how
ZKP can empower IoT and introduces our proposal to further
enhance IoT using ZKP.
Traditional authentication methods use robust encryption
protocols to secure data transfer, ensuring protection from
unauthorized access and interception. However, ZKPs revo-
lutionize this approach. Chen et al. [5] review ZKP-based
IoT authentication, highlighting its benefits over traditional
methods in terms of anonymity and reduced computational
complexity. Walsh et al. [6], proposed non-interactive ZKPs
in a Merkle tree structure for authentication, along with
methods combining ring signatures with ZKPs for enhanced
privacy [7]. W¨ohnert et al. [8] proposed ZKP-based algorithms
for verifiable identity in IoT, emphasizing accountability and
integrity. Access control mechanisms in IoT using ZKPs
have also been explored, leveraging Ethereum smart contracts
and the Groth16 proof generation mechanism [9]. Verifiable
anonymous identity management (V AIM) models have been
proposed, focusing on privacy-preserving user-centric identity
verification [10].
In the realm of blockchain-based IoT, challenges related
to data immutability and General Data Protection Regulation
(GDPR) compliance have prompted research into blockchain
erasure models, combining ring signatures and ZKPs for
enhanced privacy [11], [12]. Furthermore, balancing privacy
with accountability in blockchain identity management is
essential, as asserted by studies advocating for traceability
services in ZKP-based systems [13], [14]. These systems
combine authentication with privacy and traceability, using
shared secrets among verification nodes and central authority
oversight to detect and manage malicious behavior.
ZKPs can also be instrumental in proving the validity of
the executed process without revealing the actual software
code or detailed information about the process. This method
improves security as it eliminates the risk of exposing software

---

## Page 3

Trust Layer
Blockchain network
Data Layer
Decentralized oracle network
Physical Layer
4- Blockchain Node
1- zk-Device
3- Service Contract
2- ZKP Scheme
5- Relayer 
6- Blockchain Protocol
Fig. 3: The main components of the zk-IoT framework.
integrity mechanisms that hackers could potentially exploit to
circumvent the attestation process. In [15], a novel approach
for attested cameras is proposed to verify that images were
taken by a camera. Zero-knowledge succinct non-interactive
argument of knowledge (zk-SNARK) allows verification of
image transformations non-interactively with only standard
cryptographic hardness assumptions. Unfortunately, this work
does not preserve input privacy, is impractically slow, and/or
requires custom cryptographic arguments [16].
In addition to its previous applications, ZKP can be utilized
to enable IoT devices to demonstrate that they have executed
a particular function (firmware) on specific data, thereby
ensuring the integrity of both the data and the function.
This application, when combined with blockchain technology,
enhances the capabilities of IoT for future applications. The
focus of this paper is to propose an architecture that facilitates
this enhancement.
III. ZK-IOT FRAMEWORK
The Zero-Knowledge Internet of Things (zk-IoT) frame-
work ensures the integrity of firmware execution in IoT devices
and facilitates automatic communication between untrusted
IoT devices. Hence, it enables IoT devices to collaboratively
offer innovative services to users by integrating functionalities
and processed data across all devices. As it is shown in Fig.
3, the zk-IoT framework consists of six main elements: zk-
Devices, ZKP scheme, service contracts, blockchain nodes,
relayers, and blockchain protocol. The architecture is struc-
tured across three tiers. The top tier, known as the physical
layer, houses the zk-Devices. The middle tier, or the data layer,
includes the relayers from a decentralized oracle network,
which facilitates data transfer and bridges the physical world
with the blockchain realm. The bottom tier, the blockchain
layer, serves as the trust foundation for the framework. It
incorporates blockchain nodes to store ZKPs and uses smart
contracts to facilitate the data transfer process.
A. zk-Device
In the zk-IoT framework, every IoT device is equipped with
a ZKP generator to validate the integrity of its executed pro-
grams. Fig. 4, shows the inputs for the computation originating
from IoT sensors, while the program is stored within the IoT
device’s memory.
The zk-Device ensures that its output originates from a
circuit designed by the manufacturer, certifying that the IoT
device operates exactly as intended by its maker. It also guar-
antees that both the program and its inputs remain unchanged.
As a result, the device’s output is reliable and trustworthy.
Upon completion of the computation, the output, along with
the generated proof, is transmitted from the IoT device to the
external physical world. It is important to note that the proof
guarantees the execution of the program and the data inputted
into the device either after analog-to-digital converters (ADC)
or before digital-to-analog converters (DAC). This means that
the boundary of the computation is confined to the digital part
of the system where computations can be performed.
zk-Device
Charging 
Stations
Environment
Data
Road 
Condition
(data, proof)
Fig. 4: zk-Device
B. ZKP Scheme
zk-Devices implement a ZKP scheme that utilizes FC and
PCD to verify a chain of computations across a series of IoT
devices interacting during an automation process. As discussed
in section I, the scheme enables mutually distrustful IoT
devices to perform distributed computations that run indefi-
nitely while ensuring that the correctness of every intermediate
state of the computation can be verified efficiently. In other
words, the scheme is designed to verify a claim of the form
f T (x11, .., x1m) = yT where m is the number of IoT devices
and f T denotes a computation of an automation process with
T steps. Also, (x11, .., x1m) is the input to the first IoT device
in the automation process. yT is the final process result.
Without loss of the generality, the scheme is described on
one IoT device at Step i of the computation with a private
function fi and public inputs (xi1, ..., xim) as shown in Fig.
5. This scheme is structured as a tuple (S ETUP , C OMMIT ,
PROOF ) where:
• SETUP (1λ, Cfi ) → (ppi, pki, vki): for a security param-
eter λ and circuit Cfi := fi(xi1, ..., xim) − yi, produces
the public parameter ppi, proving key pki and verification
key vki.
• COMMIT (ppi, Ai, Bi, Ci) → (Com Ai , ComBi , ComCi ):
Prover represents circuit Cfi by matrices Ai, Bi, Ci
in Fn×n where F is a field that wires of circuit
fi
IoT device
(xi1, 兀i1)
(xi2, 兀i2)
(xim, 兀im)
…
(yi, 兀i+1)
Fig. 5: A sample IoT device at step i in an automation process.

---

## Page 4

carry their values of it and n is the number of con-
straints such that Cfi (xi1, ..., xim, yi) = 0 iff there is
(wi1, ..., win−m) in Fn−m such that (Aizi)o(Bizi) =
Cizi where zi = ( xi1, .., xim, wi1, ..., win−m) and op-
eration o denotes to component-wise product of two
equal size vectors. This function produces commitment
Com Ai = (Com RowAi
, ComCol Ai
, ComV alAi
) where:
– Com RowAi
is a commitment to polynomial RowAi
that is made by non-zero elements in Ai such that
RowAi (γj) = ωrj where rj is the row number
of jth non-zero element and γ is a generator of a
multiplicative subgroup of field F of order m. Also,
m is the maximum number of non-zero elements of
matrices Ai, Bi and Ci. Also, ω is a generator of a
multiplicative subgroup of field F of order n.
– Com Col Ai
is a commitment to polynomial Col Ai
that is made by non-zero elements in Ai such that
Col Ai (γj) = ωcj where cj is the column number of
the jth non-zero element.
– Com V alAi
is a commitment to polynomial V alAi
that is made by non-zero elements in Ai such that
V alAi (γj) = vj where vj is the value of jth non-
zero element. The Com Bi and Com Ci are also made
similarly.
• PROOF (pki, Ai, Bi, Ci) → (πAi , πBi , πCi ): produce πAi
and πBi to prove Ai and Bi are lower triangular matrix
based on protocol ”SLT Test” in [3] and πCi to prove Ci
is a diagonal matrix based on protocol ”Diag Test” in [3].
• VERIFY (vki, πAi , πBi , πCi ) → { accept, reject}: Veri-
fies that matrices Ai and Bi is lower triangular matrix
based on protocol ”SLT Test” in [3] and Ci is a diagonal
matrix based on protocol ”Diag Test” in [3].
C. Service Contract
Realizing automated IoT device communication requires
a mechanism to encode the interaction logic among IoT
devices. This is achieved through what we call a Service
Contract. A Service Contract specifies the protocol for IoT
device communication, detailing how data produced by one
IoT device can be utilized by others. Additionally, it ensures
the integrity of the data generated at each step by verifying the
ZKPs produced by IoT devices engaged in a contract. Service
contracts unlock the potential of IoT devices by amalgamating
the functions of individual, isolated devices to create new,
integrated functionalities. For example, employing a service
contract to merge the functionalities of temperature sensors in
a wide residential area with a siren in a fire department can
create an effective fire detection system. Similarly, integrating
a temperature display in a hydro company could lead to an
efficient energy management system. These types of integra-
tions serve as prime examples of how service contracts can
innovatively augment the capabilities of IoT devices.
Algorithm 1 outlines the basic logic contained in a service
contract, which processes a set of inputs including GPS
coordinates, a timestamp, a road status (possible car-accident
or road problem), the device type, and a proof verifying the
integrity of the firmware execution that produced the input
data. The process begins by verifying the proof. If the device
is identified as a Tesla and the data’s location is pinpointed
to Seattle, the algorithm then forwards the road condition
information and timestamp to the next device in the service
chain. The practical implementation of this process for a multi-
sensor system will be explored in the performance evaluation
section, with examples using JavaScript programming.
Algorithm 1 Service Contract Pseudocode.
Input: Proof P
Input: GPS L
Input: Timestamp Ti
Input: Collision Ci
Input: Device Type D
Output: Temperature To
Output: Temperature Co
Require: V erif y(P ) == valid
Require: Compliance(P, D,′ T esla′) == valid
1: if city(L)==’Seattle’ and type(D)==’Tesla’then
2: Return Ti as To
3: Return Ci as Co
D. Blockchain node
The blockchain node is a critical component in blockchain
technology, responsible for executing blockchain algorithms,
including consensus algorithms, smart contract execution,
block creation, and transaction verification. It also maintains
the blockchain data in what we call ’hot storage,’ which is
replicated across all nodes in the network.
Within the IoT domain, each device is required to transmit
its physical data to a storage system and may receive com-
mands from it. We call it ’cold storage’. This data exchange
is secure and exclusive, establishing a direct trust relationship
between a node and an IoT device.
In the zk-IoT framework, IoT functionalities are integrated
into the blockchain node, creating a node that features two
distinct databases for hot and cold storage. Hot storage is
dedicated to blockchain data, such as ZKPs, transactions, and
smart contracts. Cold storage, on the other hand, houses a
local copy of data from zk-Devices and service contracts.
Unlike hot storage, cold storage is not automatically shared
across the network. Instead, data transfer between source and
target nodes occurs through a relayer in a decentralized oracle
network, activated by a service contract.
E. Relayer
Decentralized oracle networks (e.g., Chainlink) act as essen-
tial connectors between blockchain systems and the external
environment, enabling the seamless flow of data from off-
chain sources to on-chain smart contracts. This process allows
blockchain applications to interact with real-world data. Within
these networks, relayers are key components, facilitating com-
munication among nodes.

---

## Page 5

The zk-IoT framework utilizes a relayer to facilitate com-
munication among blockchain nodes, streamlining the process
and ensuring integrity and trust.
F . Blockchain protocol
In the context of zk-IoT, every automated interaction in-
volves a series of steps designed to facilitate communication
and execution among different IoT devices. These interactions
are grounded in the fundamental premise of a straightforward
exchange between two IoT devices. Without loss of generality,
this section will focus on the interaction of only two devices
under a service contract. The first device generates data, which
the second device then receives, verifies, and uses as input for
its own firmware execution, subsequently generating new data
along with a ZKP for the next device.
The workflow of the blockchain protocol is detailed in
Figure 6. The process is initiated by a service contract but
requires sufficient funding from the second device, which
receives the data. To illustrate this, we describe the process
beginning with zk-Device B depositing funds into a smart
contract distinct from the service contract. This dedicated
smart contract serves solely as a reserve pool specifically for
data transactions and is designed to hold and disburse funds
according to a predefined sequence.
1) Deposit Tokens: The receiving IoT device (zk-Device
B) deposits sufficient funds into a smart contract for data
transfer.
2) Submit Proof and New Data Notification: Upon trans-
mitting new data, zk-Device A activates a function within
Blockchain Node X’s service contract to prompt a signal
to the Relayer and submits proof to the smart contract.
3) Fund Verification: The Relayer checks if the funds for
the transaction are adequate and confirms sufficient funds.
4) Transfer Data: Service Contract X relays the data from
zk-Device A to the Relayer.
5) Pass Data: The Relayer passes the data to Service
Contract Y on Blockchain Node Y .
6) Verify Proof: Service Contract Y checks the proof.
7) Acknowledgment: Service Contract Y sends an acknowl-
edgment to the Relayer.
8) Data Received Notification: The Relayer sends a noti-
fication to Service Contract X.
9) Release Fund Notification: Following successful data
processing, Service Contract Y instructs the Relayer to
issue a Fund Release command to the Smart Contract.
10) Release Funds: The Relayer requests the release of
funds.
11) Withdraw Tokens: zk-Device A can withdraw the funds
from the smart contract.
IV. P ERFORMANCE EVALUATION
We have developed a preliminary version of the zk-IoT
system as described below. The service contracts were crafted
using JavaScript due to available ZKP libraries like SnarkJS
that enable the users to verify the proof while letting the user to
Relayer
(decentralized 
oracle network)
Smart
Contract
Service
Contract Service
Contract
Data Data
Blockchain
zk-Device A’s 
Wallet zk-Device B’s 
Wallet
2b- New data notification
3- Fund Verification
4- Send data
5- Transfer data
7- Acknowledge
8- Data Received 9- Release fund notification
10- Release fund
11- withdraw tokens 1- Deposit tokens
Node X Node Y
2a- Submit a proof
 6- Verify the proof
zk-Device A
 zk-Device B
Fig. 6: zk-IoT communication on blockchain layers.
encode the complex interactions required for automating pro-
cesses across multiple IoT devices. The underlying blockchain
network utilizes Ethereum technology, supplemented by a spe-
cially modified blockchain node designed to run IsolatedVM,
enabling it to execute JavaScript-based service contracts. Also,
the blockchain node supports the Message Queuing Telemetry
Transport (MQTT) protocol for the non-blockchain part to
communicate with zk-Devices. The desired framework utilizes
a decentralized oracle network for data transfer, however, the
preliminary version incorporates relayer functionality inside
our blockchain node. Additionally, the zk-Device is built
around the ESP32 micro-controller, Espressif, integrating ZKP
libraries.
Figures 7 and 8 showcase the schematic and photograph,
respectively, of a ZKP-enabled environmental sensor hard-
ware design. This design includes functionalities such as a
temperature sensor, hygrometer, motion detector, and smart
button. For the purposes of this performance evaluation report,
the demonstration of ZKP functionality is confined to the
smart button component, which generates a notification upon
being pressed. The system has been developed using two ZKP
methods: the halo2 proofs library (version 0.3.0) in Rust, and
Circom. We implemented a straightforward communication
protocol between two IoT devices.
zk-Device
GPIO (ADC)
 UART
I2C
I2C
GPIO
Light
GPS
Temperature/
Hygrometer
Wearable 
sensors
Motion
Input
Program
Memory
Sensors
Proof
 Output
Actuator
Main 
Processor
ZKP 
Generator
Fig. 7: ZKP-enabled environmental sensor: general architec-
ture.
Figure 9 presents the prover and verifier times for two
distinct ZKP proving systems: Groth16 and Plonk. It is shown
that Groth16 requires 694 milliseconds, which is less than
Plonk’s 777 milliseconds for prover time. Additionally, the
verification times for Groth16 and Plonk are 19 milliseconds

---

## Page 6

Fig. 8: ZKP-enabled environmental sensor.
and 22 milliseconds, respectively. While Groth16 demonstrates
faster processing times, it necessitates a circuit-specific ZKP
key generation. In contrast, Plonk benefits from a universal
setup, allowing the keys generated to be applied across various
circuits.
Prover Time Verifier Time
0
100
200
300
400
500
600
700
800Time (ms)
694
19
776
22
Groth16
Plonk
Fig. 9: Prover and verifier time: Groth16 vs. Plonk comparison.
Fig. 10 illustrates the time required for writing and reading
proofs on the blockchain within the zk-IoT framework. Specif-
ically, submitting the proof to the smart contract for storage
takes 3,437 milliseconds, writing the proof and receiving the
first confirmation takes 11,969 milliseconds, and reading the
proof requires 5,078 milliseconds. These durations highlight
that blockchain operations are considerably slower than proof
generation and verification, underscoring the need for faster
blockchain technology that is more compatible with the zk-
IoT framework.
Write (no conf.) Write (one conf.) Read
0
2000
4000
6000
8000
10000
12000Time (ms)
3437
11969
5078
Fig. 10: Blockchain proof write and read time.
V. C ONCLUSION
In this paper, we have introduced the zk-IoT framework as a
groundbreaking development in enhancing the security of IoT
ecosystems, utilizing ZKP and blockchain technology. This
innovative framework is adept at verifying the correctness of
IoT firmware execution and ensuring data integrity, even in
scenarios where devices may be compromised. Our approach
not only fortifies the security of IoT devices communications
but also fosters new opportunities for dependable and au-
tonomous interactions within IoT networks. These advance-
ments are vital for the progress of smart city infrastructures,
healthcare systems, and the realm of industrial automation.
The practical implementation and preliminary performance
analysis of the zk-IoT framework, as demonstrated in our
work, confirm its practicality and effectiveness. This signals
a shift towards a more secure and trustworthy era of IoT
operations. We plan to present the detailed performance eval-
uation in a subsequent paper, following the completion of a
full implementation.
REFERENCES
[1] B. Wu, R. Zhong, Y . Wang, J. Wan, J. Zhang, and W. Shi, “Vpi: Vehicle
programming interface for vehicle computing,” Journal of Computer
Science and Technology , 2024.
[2] L. de Castro and C. Peikert, “Functional commitments for all functions,
with transparent setup and from sis,” in Annual International Conference
on the Theory and Applications of Cryptographic Techniques , pp. 287–
320, Springer, 2023.
[3] D. Boneh, W. Nguyen, and A. Ozdemir, “Efficient functional commit-
ments: How to commit to a private function.” Cryptology ePrint Archive,
Paper 2021/1342, 2021. https://eprint.iacr.org/2021/1342.
[4] A. Chiesa, “Proof-carrying data,” Master’s thesis, Massachusetts Institute
of Technology, Cambridge, MA, 2010. Available at MIT DSpace: https:
//dspace.mit.edu/handle/1721.1/61151.
[5] Z. Chen, Y . Jiang, X. Song, and L. Chen, “A survey on zero-knowledge
authentication for internet of things,” Electronics, vol. 12, no. 5, 2023.
[6] M. Walshe, G. Epiphaniou, H. Al-Khateeb, M. Hammoudeh, V . Katos,
and A. Dehghantanha, “Non-interactive zero knowledge proofs for the
authentication of iot devices in reduced connectivity environments,” Ad
Hoc Networks , vol. 95, p. 101988, 2019.
[7] Z. Mahmood and J. Vacius, “Privacy-preserving block-chain framework
based on ring signatures (rss) and zero-knowledge proofs (zkps),”
in 2020 International Conference on Innovation and Intelligence for
Informatics, Computing and Technologies (3ICT) , pp. 1–6, IEEE, 2020.
[8] K. H. W ¨ohnert, S.-J. W ¨ohnert, T. Thiel, R. Weißbach, and V . Skwarek,
“Secure cyber-physical object identification in industrial iot-systems,”
Procedia Manufacturing, vol. 51, pp. 1221–1228, 2020.
[9] L. Song, X. Ju, Z. Zhu, and M. Li, “An access control model for the inter-
net of things based on zero-knowledge token and blockchain,” EURASIP
Journal on Wireless Communications and Networking , vol. 2021, no. 1,
pp. 1–20, 2021.
[10] G. Ra, T. Kim, and I. Lee, “Vaim: verifiable anonymous identity
management for human-centric security and privacy in the internet of
things,” IEEE Access , vol. 9, pp. 75945–75960, 2021.
[11] H. R. Elgabri, M. S. Hassanein, A. A. El-Sawy, and M. Taha,
“Blockchain authentication access control framework to secure iot de-
vices in smart cities,” Journal of Southwest Jiaotong University , vol. 58,
no. 4, 2023.
[12] D. C. Rani, S. G. Janakiraman, K. S. Chandra, E. P. Thangavel, G. A.
Kothamasu, K. L. Bhaskaran, and G. Jayabalasamy, “A multi-round zero
knowledge proof algorithm for secure iot and blockchain environments.,”
International Journal of Safety & Security Engineering , vol. 13, no. 4,
2023.
[13] I. Damg ˚ard, C. Ganesh, H. Khoshakhlagh, C. Orlandi, and L. Siniscalchi,
“Balancing privacy and accountability in blockchain identity manage-
ment,” in Topics in Cryptology – CT-RSA 2021 (K. G. Paterson, ed.),
(Cham), pp. 552–576, Springer International Publishing, 2021.

---

## Page 7

[14] D. A. Luong and J. H. Park, “Privacy-preserving identity management
system on blockchain using zk-snark,” IEEE Access, vol. 11, pp. 1840–
1853, 2023.
[15] D. Kang, T. Hashimoto, I. Stoica, and Y . Sun, “Zk-img: Attested images
via zero-knowledge proofs to fight disinformation,” arXiv preprint
arXiv:2211.04775, 2022.
[16] S. Fang, Q. Liu, F. Zhang, N. Chen, and X. Li, “Application of
internet of things and blockchain in information security and privacy
protection of global organizations,” Journal of Organizational and End
User Computing (JOEUC) , vol. 35, no. 3, pp. 1–16, 2023.

---
