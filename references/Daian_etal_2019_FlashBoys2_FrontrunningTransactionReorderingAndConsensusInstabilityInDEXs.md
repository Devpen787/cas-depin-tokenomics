# Daian_etal_2019_FlashBoys2_FrontrunningTransactionReorderingAndConsensusInstabilityInDEXs.pdf

## Page 1

Flash Boys 2.0:
Frontrunning, Transaction Reordering, and
Consensus Instability in Decentralized Exchanges
Philip Daian
Cornell Tech
phil@cs.cornell.edu
Steven Goldfeder
Cornell Tech
goldfeder@cornell.edu
Tyler Kell
Cornell Tech
sk3259@cornell.edu
Yunqi Li
UIUC
yunqil3@illinois.edu
Xueyuan Zhao
CMU
xyzhao@cmu.edu
Iddo Bentov
Cornell Tech
ib327@cornell.edu
Lorenz Breidenbach
ETH Z ¨urich
lorenz.breidenbach@inf.ethz.ch
Ari Juels
Cornell Tech
juels@cornell.edu
Abstract—Blockchains, and speciﬁcally smart contracts, have
promised to create fair and transparent trading ecosystems.
Unfortunately, we show that this promise has not been met. We
document and quantify the widespread and rising deployment of
arbitrage bots in blockchain systems, speciﬁcally in decentralized
exchanges (or “DEXes”). Like high-frequency traders on Wall
Street, these bots exploit inefﬁciencies in DEXes, paying high
transaction fees and optimizing network latency to frontrun, i.e.,
anticipate and exploit, ordinary users’ DEX trades.
We study the breadth of DEX arbitrage bots in a subset of
transactions that yield quantiﬁable revenue to these bots. We also
study bots’ proﬁt-making strategies, with a focus on blockchain-
speciﬁc elements. We observe bots engage in what we call priority
gas auctions (PGAs), competitively bidding up transaction fees in
order to obtain priority ordering, i.e., early block position and
execution, for their transactions. PGAs present an interesting
and complex new continuous-time, partial-information, game-
theoretic model that we formalize and study. We release an
interactive web portal, frontrun.me, to provide the community
with real-time data on PGAs.
We additionally show that high fees paid for priority transac-
tion ordering poses a systemic risk to consensus-layer security.
We explain that such fees are just one form of a general phe-
nomenon in DEXes and beyond—what we call miner extractable
value (MEV)—that poses concrete, measurable, consensus-layer
security risks. We show empirically that MEV poses a realistic
threat to Ethereum today.
Our work highlights the large, complex risks created by
transaction-ordering dependencies in smart contracts and the
ways in which traditional forms of ﬁnancial-market exploitation
are adapting to and penetrating blockchain economies.
I. I NTRODUCTION
Cryptocurrency exchanges today handle more than $10
billion in trade volume per day. The vast majority of this
volume occurs in centralized exchanges, which hold custody
of customer assets and settle trades. At best loosely regulated,
centralized exchanges have experienced scandals ranging from
high-proﬁle thefts [38] to malfeasance such as price ma-
nipulation [22]. One popular alternative is what is called a
decentralized exchange (or “DEXes”). 1 In a DEX, a smart
contract (a program executing on a blockchain) or other form
of peer-to-peer network executes exchange functionality.
At ﬁrst glance, decentralized exchanges seem ideally de-
signed. They appear to provide effective price discovery and
fair trading, while doing away with the drawbacks of central-
ized exchanges. Trades are atomically executed by a smart
contract and visible on the Ethereum blockchain, providing
the appearance of transparency. Funds cannot be stolen by the
exchange operator, because their custody and exchange logic
is processed and guaranteed by the smart contract.
Despite their clear beneﬁts, however, many DEXes come
with a serious and fundamental weakness: on-chain, smart-
contract-mediated trades are slow. 2 Traders thus may attempt
to take orders that have already been taken or canceled but
appear active due to their views of messages sent on the net-
work. Worse still, adversaries can frontrun orders, observing
them and placing their own orders with higher fees to ensure
they are mined ﬁrst.
Past work has acknowledged “transaction ordering depen-
dence” as an anti-pattern and vector for potential frontrun-
ning [30, 34]. Unfortunately, these analyses have previously
proved overly broad: virtually every smart contract can be said
to have some potential dependence on transaction order, the
majority of which is benign. As a result, effective practical
mitigations for these issues have failed to materialize, and
few deployed smart contracts feature ordering protections.
Other work has focused on systematizing knowledge around
smart contract frontrunning [18], including citing early public
versions of this work, but has not measured the size of this
economy or formalized its connection to protocol attacks.
1“Decentralized” exchange is something of a misnomer, as many such
systems have centralized components; most systems we call “decentralized”
exchanges could more accurately be classiﬁed as non-custodial: users trade
without surrendering control of their funds to a third party in the process.
2The average Ethereum block time is roughly 15s at the date of writing [19].
1
arXiv:1904.05234v1  [cs.CR]  10 Apr 2019

---

## Page 2

In this work, we explain that DEX design ﬂaws threaten
underlying blockchain security. We study a community of ar-
bitrage bots that has arisen to exploit DEX ﬂaws. We show that
these bots exhibit many similar market-exploiting behaviors—
frontrunning, aggressive latency optimization, etc.—common
on Wall Street, as revealed in the popular Michael Lewis
expos´e Flash Boys [33]. We explore the DEX design ﬂaws
that spawned arbitrage bots, measure and model these bots’
behavior, and illuminate systemic smart-contract ecosystem
risks implied by our observations. Our main focuses are:
Pure revenue opportunities : A speciﬁc sub-category of
DEX arbitrage representative of broader activity, these are
blockchain transactions that issue multiple trades atomically
through a smart contract and proﬁt unconditionally in every
traded asset. We choose these opportunities as a focus because
their simplicity makes them especially amenable to study and
measurement. We experimentally determine a lower bound
on this economy of over USD 6M to date and describe its
participating exchanges and bots.
Priority gas auctions (PGAs) : Because pure revenue op-
portunities offer unconditional revenue, arbitrage bots often
compete against each other by bidding up transaction fees
(gas) in what we call PGAs. We formally model bot PGA
behavior and observe a cooperative equilibrium. We show that
empirical measurements of the evolution of bot PGA strategies
validate key features of our model.
Miner-extractable value (MEV): We introduce the notion of
MEV , value that is extractable by miners directly from smart
contracts as cryptocurrency proﬁts. One particular source of
MEV is ordering optimization (OO) fees , which result from a
miner’s control of the ordering of transactions in a particular
epoch. PGAs and pure revenue opportunities provide one
source of OO fees. We show that MEV creates systemic
consensus-layer vulnerabilities.
Fee-based forking attacks: We show that OO fees can incen-
tivize miners to mount forking attacks. While fee-based attacks
were previously studied theoretically in Bitcoin [14], we
empirically demonstrate a current, realistic threat in Ethereum.
Time-bandit attacks : We show that high-MEV regimes
in general lead to a new attack in which miners rewrite
blockchain history to steal funds allocated by smart contracts
in the past. We call these time-bandit attacks. Our experiments
show that MEV from pure revenue proﬁts and PGA bot fees
sufﬁce to enable time-bandit attacks on today’s Ethereum.
Our results are surprising for two key reasons.
First, they identify a concrete difference between the
consensus-layer security model required for blockchain pro-
tocols securing simple payments and those securing smart
contracts. In a payment system such as Bitcoin, all independent
transactions in a block can be seen as executing atomically,
making ordering generally unproﬁtable to manipulate. Our
work shows that analyses of Bitcoin miner economics fail to
extend to smart contract systems like Ethereum, and may even
require modiﬁcation once second-layer smart contract systems
that depend on Bitcoin miners go live [32].
Second, our analysis of PGA games underscores that pro-
tocol details (such as miner selection criteria, P2P network
composition, and more) can directly impact application-layer
security and the fairness properties that smart contracts offer
users. Smart contract security is often studied purely at the
application layer, abstracting away low-level details like miner
selection and P2P relayers’ behavior in order to make analysis
tractable (e.g. [9, 25, 50, 51]). Our work shows that serious
blind spots result. Low-level protocol behaviors pose funda-
mental challenges to developing robust smart contracts that
protect users against exploitation by proﬁt-maximizing miners
and P2P relayers that may game contracts to subsidize attacks.
To illuminate the behaviors explored in this paper, we
release a web dashboard, frontrun.me, that presents PGA data
in real time. We open-source all associated code and hundreds
of gigabytes of raw data on the Ethereum PGA economy (with
processed data). 3
We hope our efforts in general offer insight into the broad,
application- and consensus-layer risks created by ordering de-
pendencies in smart contracts and into the effects of traditional
ﬁnancial-market exploitation on blockchain consensus.
II. B ACKGROUND
We now provide background required to understand PGAs.
A. Smart Contracts
Smart contracts are small computer programs executed
without user intervention, often by a system that allows all
of its participants to verify these programs’ correct execution.
Smart contracts often use a public blockchain network as the
underlying infrastructure for their execution [45, 49].
Ethereum [49] is currently the largest smart contract system
that is Turing-complete, i.e., allows encoding of arbitrary
smart-contract functionality. Ethereum smart contracts have
been used or proposed for a range of complex transaction
types, including shareholder voting [36], stakeholder-owned
investment funds and vehicles [11, 16], fair exchange protocols
for goods [51], complex key management solutions [50], video
games [26], virtual casinos [39], and more.
The most popular smart contracts on Ethereum by daily
active users primarily concern virtual sub-currencies called
tokens. These tokens can represent any scarce item, e.g.
collectible resources in a video game [26] or shares in a
venture [21]. The latter fueled a 12 billion USD token-based
capital-investment craze called the “ICO boom”. DEXes are a
popular type of smart contract that allow users to trade such
tokens in a non-custodial manner [48].
3Our Github repository at https://github.com/pdaian/ﬂashboys2 contains all
infrastructure, data processing, and visualization code and data, plus code for
our original arbitrage trade bot.
2

---

## Page 3

B. Gas and Fees in Ethereum
An Ethereum transaction either sends money to a non-
executing account address or sends input data (and possibly
money) to a smart contract address , representing a program
stored in the network’s state. Transactions are gossiped to all of
the nodes in the underlying peer-to-peer network to signal their
availability for inclusion in a future mined block. Transactions
can be in one of three states: unconﬁrmed and not yet mined,
conﬁrmed and considered to have been executed, or rejected
as invalid by the network of Ethereum peers.
Ethereum transactions consume gas, a pseudo-currency
reﬂecting the number of computational steps performed by
a miner (and other network nodes) executing a transaction.
Ethereum contracts may contain complex logic, loops, etc., so
their gas consumption can only be determined via execution.
Ethereum meters gas consumption via a ﬁxed mapping from
contract op-codes to units of gas [49].
Every transaction submitted to the network for mining
speciﬁes a gas price, the per-gas-unit rate the sender will pay
in Ether (ETH). The gas price times the units of gas consumed
determines the fee in ETH paid by the transaction sender to
the node that ultimately mines the transaction. (Bitcoin fees,
by contrast, depend simply on transaction byte lengths.)
Transactions must also specify a gas limit , the maximum
number of steps a network node should attempt before reject-
ing a transaction. The gas limit prevents inﬁnite loops and
other DoS vectors, and allows immediate veriﬁcation that a
sender has adequate available funds to pay the transaction
fee—up to gasPrice · gasLimit ETH.
Clients can also perform what is called a “gas replacement”
transaction, resubmitting a transaction with a higher transac-
tion fee (gasPrice · gasLimit) in the hope that miners will more
quickly incorporate the transaction into a block. The mecha-
nism for doing this is nonce-based. Each transaction issued on
the network carries a nonce, and valid canonical blockchains
must only include one transaction per (account, nonce) pair on
the network. When a user reissues an unconﬁrmed transaction
with the same (account, nonce) pair but a higher gas price, a
miner will prefer the reissued transaction—with its ostensibly
higher transaction fee—to the replaced one.
Note that a higher gas price only corresponds to a higher
fee if the reissued transaction uses the same amount of gas as
the replaced one , which may not hold true. Mining software
assumes this to be the case, in part because computing gas
consumption incurs the computational burden of executing a
contract. Arbitrageurs leverage this heuristic to pay reduced
transaction fees, as we detail in Section V-A.
C. Continuous-Limit Exchanges
Classic exchanges for trading stocks, commodities, and even
cryptocurrencies generally share an accepted and common
exchange design known as a continuous-limit orderbook. Such
an orderbook consists of a list of all open offers from buyers
and sellers in the system. Prospective buyers place a limit
buy order, which speciﬁes a maximum price at which they
are willing to buy an asset; sellers correspondingly place
limit sell orders. A centralized counterparty, the exchange
operator, matches buyers and sellers, completing transactions
automatically when there is a sell order on the books with a
lower price than a buy order on the books. Orders are matched
and / or placed on the books continuously by the exchange
operator, which processes orders as quickly as possible in the
order they are received. As soon as orders match, they are
processed by the operator and trigger balance changes.
D. Decentralized Exchanges (DEXes)
DEXes manage continuous-limit order books using smart
contracts. Traders / users hold their assets on chain and the
smart contract plays the traditional role of exchange operator.
Order books are typically maintained off-chain. In some
DEX designs, a counterparty selects a fresh order in the
order book and presents it to the smart contract with a
signed counterorder. The smart contract executes the order and
counterorder, clearing the order from the order book. Traders
themselves thus perform order matching. This approach is used
by Etherdelta and some applications of the 0x protocol. In
an alternative approach, used by, e.g., IDex and Paradex, the
exchange itself performs matching off chain and submits order
/ counterorder pairs to the smart contract for processing.
A more radical DEX design, called an automated market
maker [3], bypasses order books altogether. The DEX consists
of a smart contract that itself holds a reserve of tokens and/or
Ether. Consider two assets A and B. The contract allows a
user to trade between A and B at any time using its reserves
as a counterparty, at a set rate. If a user buys A using B, the
price of A denominated in B offered by the smart contract for
the next trade is increased. If a user instead sells A forB, the
price decreases. In this way, single parties can trade without
counterparty discovery or matching. Consequently, constant
arbitrage between these and other exchanges is required to
keep the rate offered in lockstep with the market rate for a
commodity. Uniswap [46] and Bancor [1] are examples of
such exchanges.
E. Frontrunning and Proﬁts through Arbitrage
Traditional exchanges experience a classic form of preda-
tory market behavior called frontrunning [4]. In regulated
markets, frontrunning is often illegal, and has resulted in
prosecutions [35] and tarnished the reputations of ﬁnancial
institutions caught practicing it.
Frontrunning generally exploits information asymmetries
created by power structures within a ﬁnancial structure, e.g.,
brokers having privileged access to user information. Because
there is no single party playing the role of a broker in
decentralized systems, information asymmetries can arise for
actors in advantageous positions in underlying infrastructure.
Frontrunning can also occur based on changes in public
market information (for example, reacting to breaking news
that impacts stock prices). In this form, it is not only legal,
but serves as the basis of a multi-billion-dollar high-frequency
trading economy. One potential source of proﬁt is price
discrepancies across exchanges trading the same or correlated
3

---

## Page 4

assets. Another is information asymmetries in the speed of
processing or interpreting news.
Automated market bots from high frequency trading ﬁrms
compete to proﬁt from both at extremely high speed. They
regularly build physical networks costing billions of dollars
and approaching speed-of-light transmission across consider-
able distances. Many economists view this behavior as a zero-
sum game that proﬁts exchanges in the long term, and argue
formally that the existence of such rents is a fundamental
limitation of market design that is a natural consequence of
arbitrage opportunities across exchanges [8]. This, however,
remains a controversial viewpoint.
We explore both cases where bots frontrun user orders and
cancellations directly, e.g., in the event of a typo or market
structure weakness, and cases where bots exploit market
inefﬁciencies to extract rent. We argue that both degrade the
economic security of the underlying consensus protocol.
III. F ROM DECENTRALIZATION TO ARBITRAGE
In this section, we take a deep dive into a particular exam-
ple of frontrunning, arbitrage, and high-frequency automated
trading on a decentralized exchange. This concrete example
will provide context for the remainder of our discussions on
modeling this market and of its impact on the security of the
underlying smart contract systems.
One source of potential proﬁt, price differences, seems
inherent in an environment such as smart-contract-based ex-
change. Today, blockchains operate with transactions pro-
cessed in discrete batches (blocks). Furthermore, transactions
are inherently dependent and therefore serial: order failures
depend on past order attempts, and in some exchanges prices
depend directly on order history. With multiple exchanges op-
erating on the same system, it is possible that price differences
will occur across exchanges while transactions in a block, and
therefore trades on exchanges, are executed sequentially.
A. Smart-Contract-Enabled Trade Atomicity
Smart contract arbitrage opportunities have an additional,
distinctive characteristic absent in traditional cross-exchange
arbitrage. Because of the atomic batch-based processing of
transactions, and because transactions can themselves be
initiated by smart contracts, is possible to build bots that
trade across exchanges through proxy contracts. These proxy
contracts can execute batches of orders sequentially within a
single transaction, reverting previous trades by throwing an
exception if any trade in the batch fails.
This means arbitrageurs have the opportunity to compose
single transactions that execute multiple trades across multiple
exchanges atomically, with an all-or-nothing failure model.
One example of such a transaction is buying an asset for price
x and selling it immediately for price x′ > x; if performed
atomically, these transactions together generate guaranteed
revenue in the base asset. For example, a smart contract proxy
could execute a trade buying a type- X token for 2 ETH, and
another selling it for 3 ETH. If both orders are on the books
on some decentralized exchange, a smart contract executing
both guarantees a revenue to the arbitrageur of 1 ETH.
In traditional cross-exchange arbitrage, trades are viewed
probabilistically, as there is a high likelihood that one of two
trades will succeed while the other fails. This makes smart-
contract-based arbitrage in many ways simpler to observe,
analyze, and study than traditional cross-exchange arbitrage,
as bot intent is often explicit in order requests.
In our measurements, we focus on a small subset of these
multi-trade arbitrage opportunities, which potentially involve
multiple decentralized exchanges. We restrict our focus to pure
revenue opportunities. In these opportunities, a single smart-
contract based transaction executes multiple trades across one
or more exchanges, and the transaction generates revenue for
the trader in every traded asset. A range of more complex and
nondeterministic bot behaviors exist, described in Appendix A,
but they are outside the scope of this work.
B. Pure Revenue by Example
ETH0.142123
1.55496e+08 1.55e+08
0.93
Trade #1 (Tokenstore)1.09409e+09 FREE/ETH
Free Coin (FREE)0x2f141ce366a2462f02cea3d12cf93e4dca49e4fd
Trade #2 (Tokenstore)1.66667e+08 FREE/ETH
Fig. 1. Example pure revenue opportunity observed in Ethereum transaction
0xc889bd13594f75e4dd824f04f0c2ad03896cb7ec6518df02455e9560367bb9c4,
exploiting an orderbook cross on the TokenStore DEX. Edges of the same
color are generated by a single trade. As a pure revenue opportunity, it
generates net proﬁt in both FREE and ETH.
Figure 1 shows one example of a pure revenue transaction,
executed on November 15, 2018. In this transaction, two trades
are executed on a decentralized exchange, TokenStore, which
features a design conceptually similar to that of Etherdelta.
The ﬁrst executed trade buys Free Coin, an obscure token.4 By
inspection, this difference in rates is a clear result of someone
using the exchange API and committing an off-by-one error,
offering to buy tokens at 10x the market rate. This created
a cross in the order book (sell order at more than a buy
order would pay), which when both executed by the same
arbitrage counterparty, generates the ﬂow of funds in Figure 1.
While this opportunity probably arose from a typo, a variety of
revenue sources exist. For example, inconsistent price feeds,
or variance across exchange designs that respond to market
movements at different speeds can also create pure revenue.
Note that both orders are executed inside a single Ethereum
contract, and are executed in an atomic batch through a smart
contract proxy. In general, we model each opportunity as a
graph as shown in Figure 1. Edges represent currency ﬂows,
4As of writing on Mar 13 2019, Free Coin is listed at currency rank 303
by market cap https://coinmarketcap.com/currencies/free-coin/.
4

---

## Page 5

0 2 4 6 8 10 12 14
0
0.2
0.4
0.6
0.8
1
·104
Time Since Start (s)
Gas Bid (gwei)
Example 2-Bot PGA Visualized
0x6BEc..6542/1453 Bids
0xb8D7..7a3f/1512 Bids
Auction Winner
Auction Loser
Seconds
ElapsedQuantity @ Price BidEthereum Transaction Origin (Public Key Hash)Nonce Transaction Hash
0.000 192085 @ 25.100x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b1465421453 0xd32653ca9694a6d1299335f3c04f74cc159bee48c1d32d3a421db08c638ffc78
1.593 231520 @ 25.000xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f1512 0xb901e6dc2c229fd9105448fcc23eaebdedb476c21b6c6e7ddf8d2df4e838d2c7
1.624 231520 @ 28.750xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f1512 0x9f592504eb71a7452b7a395a7f5ecd34eaa5d090da1162e74221562af54c8f67
1.679 227534 @ 28.810x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b1465421453 0x83e2a6774654a9540c3fad8837afcc88b4c932ab2374819254f887305c3a4b22
... ... ... ... ...
4.949 227534 @ 134.020x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b1465421453 0xc889bd13594f75e4dd824f04f0c2ad03896cb7ec6518df02455e9560367bb9c4
5.599 231520 @ 133.760xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f1512 0xaa86d782328c0c9c422e3f2a3170ff41ae21a27ad395c48db76b0080898f85db
... ... ... ... ...
13.383 227534 @ 5834.770x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b1465421453 0xb0dc97140394c5f65332ebc459d5e66f89099dbb4d335c866b32280270102858
13.416 227534 @ 7716.480x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b1465421453 0x1825be6951577e72a1dafc8de564ce1ccfe5d284173e11e77b2e7f6b1b44571c
13.462 231520 @ 7701.080xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f1512 0xa9823358c99149f0e6343c604c35988468d01d02868437d8251b3cee282dc92b
m13.759 231520 @ 8856.240xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f1512 0x366c30a534b5f3d8a6d251f97d401997624d1fe8d3af07ede4d19105dc970942
Fig. 2. One example PGA that was observed over the Ethereum peer-to-peer network, resulting from the proﬁt opportunity in Figure 1. The top graph shows
the gas bids of two observed bots over time, while the bottom table details the ﬁrst and last two bids placed by each bot and the two mined bids (center).
and nodes are either exchanges nodes (which receive one
currency and output another at the stated exchange rate), or
asset nodes (which are either sources or sinks for same-color
trade subgraphs, depending on whether they are bought or
sold). We label exchange nodes with the exchange name and
trade rate, and asset nodes with the asset symbol.
The net revenue in each traded asset is the sum of in-
ﬂows minus outﬂows in the corresponding asset node. In
the trade in Figure 1, the revenue for ETH was therefore
0.93 ETH − 0.14123 ETH ≈ .79 ETH, or approximately
267 USD in equivalent value (at November 15, 2018 prices
of 338.15 USD per ETH). Approximately 496,000 residual
FREE was also left in the arbitrageur’s account, although less
signiﬁcant and liquid than the ETH revenue.
To calculate the transaction proﬁt, we subtract the cost from
the revenue, in this case the gas paid by the transaction that
was mined for the arbitrageur. Transaction 0xc889...b9c4 paid
a gas price of 134.02 Gwei (the canonical unit for representing
gas rates; 1 Gwei = 10−9 ETH). The transaction used 113, 265
gas, approximately equivalent to 113, 265 computational steps.
It is worth noting that transactions that cancel their bids can
use less gas, as they pay only for attempted execution (execu-
tion requires costly computational steps). This will be relevant
to later models in Section V-A. Furthermore, complex con-
ditional transactions, price queries, or other computationally
intensive order preferences will obviously cost more, making
optimizing for gas consumption important in the development
of competitive bots. The total cost of this transaction was
therefore 113265 · 134.02 Gwei = 0.01518 ETH, or around
5.13 USD at the time of the transaction. The associated proﬁt
was therefore ≈.79 −.01518 =.77 ETH, or 267 USD.
C. PGAs, Ordering Fees, and... HFT?
Ethereum transactions are routed in a peer-to-peer gossip
multicast protocol by client node software. This means that
all transaction information is available to all participants in
this network, but earlier to participants with advantageous
positions in the gossip topology. Additionally, nodes can
simulate the outcome of every transaction given the current
or expected system state. Once an arbitrage transaction is
submitted, therefore, the sequence of trades it involves is
publicly known by the network’s peer-to-peer nodes.
A natural question then arises: how is priority determined
between arbitrageurs? Because each pure proﬁt opportunity
carries some computable proﬁt p and is broadcast globally,
a competitive game naturally ensues among arbitrage bots
to be the ﬁrst to execute an atomic transaction that exploits
the opportunity. The mechanics of the system dictate that
all subsequent transactions in the game will fail. How this
particular game plays out depends on the peer-to-peer relay
network mechanics of the underlying blockchain, as well
as mining pool strategies and order book designs in the
underlying exchanges. We present a greatly simpliﬁed model
of this game formally in Section V-A.
In Ethereum, the PGA game we observe consists of transac-
tions issued with the same (account, nonce) pair, expressing a
bid to a miner, where the miner is paid gas fees as described
5

---

## Page 6

in Section II-B. We call this interaction of issuing repeated
bids a priority gas auction , or PGA.
To place a bid on an arbitrage opportunity, an arbitrageur
simply issues a smart contract transaction with associated gas
price g that atomically bundles multiple trades (performing
the arbitrage). If they later wish to increase this bid, either for
strategic reasons or because they notice a higher bid that would
eliminate their proﬁt issued on the peer to peer relay network,
they simply reissue the transaction with the same nonce and
a higher gas price g′. If two arbitrageurs are bidding against
each other, what emerges is essentially an auction, as shown
in Figure 2. It is in a miner’s interest to order ﬁrst whichever
transaction offers the highest price (if the miner does not plan
on itself arbitraging the market). This approach will encourage
arbitrageurs to bid each other up for transaction priority.
Figure 2 shows the action that occurs in such an auction
from the point of view of the network. Each row in the
associated table is a transaction observed by our Ethereum
monitor on the peer to peer network, using the experimental
harness described in Section IV. In this example, we see two
accounts, 0x6BEc...6542 with nonce 1453 and 0xb8D7...7a3f
with nonce 1512, bidding against each other for priority. These
accounts issue transactions with ever increasing gas prices:
bot 0x6BEc...6542 issues 42 transactions in 13.4 seconds, and
0xb8D7...7a3f issues 43 transactions in 12.1 seconds. In 4.94
seconds, the auction is over. The transaction that eventually
ends up mined with priority is shown with a green star, and is
transaction 0xc889...b9c4 issued by bot 0x6BEc...6542. This
bot is considered the winner, and pays the full gas price to
reap the revenue as described in the previous section. The
transaction was mined in block 6709727 by the mining pool
“MiningPoolHub”. The transaction shown in the red square,
with hash 0xaa86...85db by bot 0xb8D7...7a3f, is also mined
and included in the ﬁnal block, as each (account, nonce) pair
can include one transaction in the next block to be mined as
per the protocol. Miners are incentivized to include even failed
transactions, as these transactions pay for attempted execution.
Note that while the winning transaction used 113,265 gas in
execution, the losing transaction paid for 33,547 gas units, a far
smaller sum. In game theoretic terms, each auction represents
a variant of all pay auction, where instead of paying their full
bid, the loser is forced to pay a percentage to the miner.
IV. A RBITRAGE PREVALENCE MEASUREMENT STUDY
We now present empirical measurements of the prevalence
of arbitrage. We discuss our methodology (and its limitations).
A. Experimental Setup
We ﬁrst describe the experimental harness used to observe
PGA transactions, displayed in Figure 3. On-chain data is
not sufﬁcient to analyze PGAs, as all but the ﬁnal “winner”
transaction are discarded by the network. Furthermore, be-
cause transactions are replaced so quickly and nodes don’t
propagate replaced transactions, many transactions are never
even propagated to all Ethereum nodes.
Ethereum
Ohio
Oregon
S. Carolina
Frankfurt
Sao Paulo
Seoul
Monitoring infraDatabases
Google
Postgres
Python parsing &processing scripts
WebCSVs released Figures
for reproducibilityinterface and graphs
SQL DB
BigQuery
network
Fig. 3. Deployed PGA measurement infrastructure architecture.
No tools existed for analysis of unconﬁrmed and rejected
transactions, so we wrote our own. We forked the Go-
Ethereum client to record unconﬁrmed transaction in the mem-
pool. We deployed six geodistributed nodes across multiple
data centers, with timestamps synchronized to the nanosecond
level by NTP. We collected an observation every time one of
the ≈ 256 nodes peered with one of our deployed modiﬁed
nodes relayed a transaction to us. We collected nine months of
data, amounting to over 300 gigabytes, including 708,385,840
unique observations of PGA arbitrage bots. Node locations
are shown in Figure 3, although not all nodes were online
throughout the experiment. (We ultimately sacriﬁced timing
resolution to reduce prohibitive ongoing costs.)
Because it is technically infeasible to store observations of
every Ethereum transaction, we focus on a list of suspected
arbitrage bot transactions. This list is seeded with accounts
we observe performing pure revenue transactions on the
blockchain, and is updated dynamically any time a high-value
gas replacement transaction is seen at an order of magnitude
over current gas market price. We also built a web interface
to manage the uptime of our nodes and associated bot lists.
We supplemented this mempool data we collected on PGAs
with on-chain data sourced from Google’s BigQuery Ethereum
service (as well as other on-chain metadata, like block times-
tamps), allowing us to parse logs for successful transactions
and determine their proﬁt. We also used daily price data from
coinmetrics.io for USD conversions.
We then developed a suite of Python scripts to combine
and analyze this data. These scripts use a heuristic to place
all observations on a timeline, identifying a PGA whenever a
high-value gas replacement transaction occurs. All transactions
in a time interval around this observation are then considered
part of the “auction,” and broken down per bot. The scripts also
aggregate meta-statistics on PGAs, calculating strategy and
latency trends in observed bots. This data is used to generate
both our web interface and the ﬁgures in this paper. We
release all source and processed/derived data in CSV format
for further analysis by the community on our Github.
1) Instrumentation Limitations: The above instrumentation
has limitations that may affect our data quality. We describe
them at a high level here, and mention any impact these
6

---

## Page 7

limitations may have on our derived results throughout.
It is possible that a transaction will be replaced before
reaching our nodes, though this seems unlikely, since each of
our observed transaction tends to have hundreds of associated
observations. More critically, our time-slicing method for
identifying PGAs may lump together unrelated bot activity
into a single “auction.” Manual inspection suggests that be-
cause auctions are relatively infrequent (every few hours), the
majority consist of correlated bot activity. Time-slicing could
also harvest unrelated transactions from other arbitrage bots
that are not PGA behavior; we prune these in our aggregate
statistics by only including bots that have placed at least 4
“bids” in an observed PGA, and as a result may lack data
on bots that place < 4 bids. We also may miss bots whose
addresses are not in our PGA lists, leading to missing bidders
in certain auctions.
Lastly, our instrumentation calculates pure revenue oppor-
tunities by parsing transaction logs on supported exchanges
for transactions that contain more than two trades executed
by a smart contract. We support only a limited subset of pop-
ular DEXes, omitting revenue opportunities on unsupported
exchanges. Because we aim to establish a lower bound (i.e. a
potentially too conservative result), we feel this is acceptable.
Our supported exchanges include the top ﬁve DEXes by
sustained volume at the time of infrastructure development.
This subset still proves sufﬁcient to provide substantial
insight on the PGA market not afforded to regular nodes in
a blockchain context, highlighting the limits of the “trans-
parency” afforded users by these systems.
B. Observations
We now describe key results of our data gathering.
07-17 01-18 08-18 02-1910−1
100
101
102
103
104
Date (MM-YY)
Daily Pure Revenue Captured (ETH)
Pure Revenue Market Size (ETH)
200
400
600
800
1000+
# Trades
Fig. 4. Lower bound size of the observed pure revenue market, ETH. Black
line shows a 14-day moving average of market size, while the dotted orange
line plots cumulative market size. Scatter plot colorings/shading indicates
number of daily pure revenue trades. The pink vertical line shows the release
of [2] associated with early versions of this work becoming public.
Figure 4 shows the size (breadth) of the arbitrage market,
denominated in ETH. We choose to use ETH denominations
04-18 07-18 10-18 01-19
10−2
10−1
100
101
102
103
Date (MM-YY)
Cumulative Pure Revenue Captured (ETH)
Pure Revenue Per Exchange Since 04/18
Market Total
Etherdelta
Bancor
0x v1
Tokenstore
Kyber
0x v2
Fig. 5. Top exchanges by cumulative pure revenue offered bots since 04/18.
in the rest of the work as they display a relatively consistent
distribution, as shown in the ﬁgure. USD revenues are more
volatile, as is visible in the market revenue graph discussed in
Appendix B-A.
This distribution is consistent with common understanding
of arbitrage as sourced from market structure design, as ETH
is the most liquid traded token on this market. As seen in
this graph, after the initial market development in late 2017, a
relatively active period of arbitrage occurred during which bots
often performed over 1,000 daily trades for a daily revenue of
10-100 ETH. Later, the market matured into a more steady
and consistent proﬁt distribution, with 1-10 ETH available
for arbitrage daily. Recently, an increasing number of pure
revenue trades is observed, showing the trend of the DEX
market to smaller retail transactions and more efﬁcient market
designs, decreasing the average opportunity size but presenting
more frequent opportunities to a more efﬁcient bot market. The
limitations in our instrumentation mean, however, result in an
underestimate of market size, as described in Section IV-A1.
Interestingly, Figure 4 also highlights the origin story of
this work. In August 2017, we published a preliminary report
on the dangers of decentralized arbitrage and associated bot
designs in [2]. The date of our blog release is shown as
the vertical line on the graph. As part of this post, we
actively probed the Etherdelta orderbook for pure revenue
opportunities, measuring available proﬁt at 4,472.75 USD /
day or 1.6M+ USD / year. We executed our own trading bot
to conﬁrm the technical feasibility of proﬁt, observing a total
58% rate of success in capturing pure revenue for our own bots
(soon outcompeted by other bots after the release of our post).
We calculated the expected daily proﬁt of an arbitrage bot at
the time, before most decentralized exchanges were online,
at 0.32 ETH/day ·58.3% success ·45 − 0.004 · (1 − 58.3%)
failure cost * 45 observed opportunities = 8.32 ETH (2500
USD) daily proﬁt. Note in Figure 6 that the majority of
proﬁtable bots today joined shortly after our public release,
7

---

## Page 8

07-17 08-17 10-17 11-17 01-18 03-18 04-18 06-18 08-18 09-18 11-18 01-19 02-19
10−2
100
102
104
Date (MM-YY)
Daily Pure Revenue Proﬁt (USD)
Pure Revenue Proﬁt Per Bot, 14-Day Moving Average
Market Total
0x0000f7..
0x44e05b..
0xaa2432..
0xb3707d..
0xf13ecd..
0x5a2896..
0xbb3a8c..
0xa53170..
0x905451..
0x00bd1f..
Fig. 6. Proﬁt (revenue minus estimated costs) for pure revenue bots over time. We observe that the median proﬁt is 65% of the size of the pure revenue
opportunity across 138,948 observed pure revenue transactions.
−1 −0.5 0 0.5 1 1.5 2 2.5
100
101
102
103
Amount (ETH)
Number of Observed PGAs
Proﬁtability of Pure Revenue PGA Winners
Proﬁt
Revenue
Fig. 7. Distribution of proﬁt and revenue in competitive PGAs. We focus on
amounts from -1 to 2.5 ETH, which by inspection comprise the majority of
the distribution body. 29 of 2,135 proﬁts fall outside this range.
which inadvertently sparked a thriving cottage bot economy!
Figure 5 shows the breakdown of the pure revenue market
by exchanges, since 04/18 (the ﬁrst signiﬁcant pure revenue
opportunities outside Etherdelta, representing new exchanges
coming online). An oligopolistic pure revenue market is ob-
served, with Etherdelta generating the majority of observed
pure revenue. Nonetheless, a range of other exchanges fur-
nishes a growing and relatively consistent distribution of
opportunities for bots. Because we only support certain ex-
changes, unsupported exchanges may be missing from this
graph, and the market total provides a lower bound only.
Figure 6 shows the top ten transaction senders we observe
in the competitive pure revenue market, and their associated
proﬁts. The cost we measure for these bots includes only the
gas fees for the pure revenue transactions they make, and thus
may underestimate their total fees (e.g. for failed transactions).
We also do not include any bots that do not trade on our
supported exchanges. Note that we make no effort to group
transaction senders together to consolidate multiple senders
operated by a single entity; some heuristics are available for
doing this (e.g. monitoring use of similar arbitrage contracts),
but we leave such aggregation to future work. We focus on
USD on this graph, as we believe that most actors use ﬁat
currencies to pay participation costs.
As in the exchange breakdown, this ﬁgure suggests an
oligopolistic market, with single bots often dominating the
proﬁt space for extended time periods (for example, 0xaa24...
dominates the recent pure revenue space, where 0x0000...
experienced a long period of dominance through late 2017
and early 2018). This diagram also shows the behavior of top
bots exiting the market after failing to update their strategies.
For example 0xa53... exits around 03/18, and 0xf13... exits in
late 2017, early in the market. Nonetheless, many bots enjoy
extended runs of proﬁtability, and continue operating for years.
Interestingly, the revenue and proﬁt graphs for these bots
have nearly identical shapes (the revenue graph is described
in Appendix B-A). Proﬁt-to-revenue ratios are relatively well
distributed, with a median of 65% of the revenue of an
opportunity captured by the winning bot according to our proﬁt
heuristics. Most opportunities are also uncontested, providing
the bots a steady stream of income.
Thusfar, we have focused exclusively on pure revenue
opportunities, which may lead to PGAs or may be claimed by
a single bot uncontested. A natural question becomes whether
the proﬁtability of opporutnities persists in a competitive
market, or whether competition among bots creates a generally
unproﬁtable zero-sum or negative-sum environment.
Figure 7 describes the breakdown between the proﬁt and
revenue of observed pure revenue opportunities involved in
priority gas auctions, indicating that at least one bot placed
a competitive gas replacement bid to capture such an oppor-
tunity. While there is a spike around 0 proﬁt, indicating that
many PGA opportunities are zero or negative sum for their
players, the vast majority of these opportunities see relatively
insigniﬁcant costs, and the proﬁt distribution still provides a
mean proﬁt to winning bots that offers them a majority of
8

---

## Page 9

associated revenue. This conﬁrms our suspicious that bots
may be engaging in uncoordinated cooperation to maintain
the proﬁtability of the PGA market at the expense of miners,
which we model fully in Section V.
07-17 01-18 08-18 02-190
1
2
3 ·105
Date (MM-YY)
Mean Gas Used Per Trade
Gas Trends in Pure Revenue
2
2.2
2.4
2.6
2.8
Mean Trades/TX
Fig. 8. Trends in quantity of gas used per trade by observed pure revenue
transactions. The vertical line indicates the release date of a gas optimization
token by the authors and others as part of this study, described in [7].
A ﬁnal natural question to ask about the market is the
extent to which the gas used in a transaction (representing
the “quantity bid” in a PGA) is an important competitive
optimization vector for pure revenue bots. Figure 8 shows
this optimization over time. Before 04/18, primarily Etherdelta
trends are observed. As we expect, we see bots optimizing
their gas costs with a clear downward trend over time, de-
spite relatively consistent execution of primarily pure revenue
transactions containing two trades per transaction.
The advent of more sophisticated exchanges shows market
maturation, with more complex opportunities executed that re-
quire more gas per trade. The number of trades per transaction
has also increased, now averaging well over two trades per
transaction. Part of this trend is due to “liquidity pooling”
exchange designs like Kyber, which allow use of an exchange
contract as a proxy to trade on other exchanges.
The dotted orange line on this graph shows the authors’
public release of a token called GasToken [7]. It leverages a
feature in Ethereum’s incentive model enabling arbitrageurs to
perform gas arbitrage over time, banking gas at below market
rates and deploying it to win PGAs. The mechanism by which
this gas arbitrage is performed yields a transaction refund
in the quantity bid to miners, tricking miners into accepting
smaller than expected bids. Because this allows bots to bid
higher gas prices for less quantity at the same level of cost,
this token is now a requirement for participating competitively
in the pure revenue arbitrage market. This is reﬂected in
our trends graph as a sharp downtrend in gas quantity bots
demand from miners after release of our token. This anecdote
provides unusual insight on consequences of performing active
experiments on emerging competitive markets.
C. User Comments
One unique feature of Ethereum over other market designs
is the public nature of some of its trading data. For example,
the addresses of the arbitrageurs in Figure 6 are known, and
can link different trades by a single actor. This often allows
users to see which arbitrage bot targeted a transaction they may
have made, and to comment on bot activity on generic public
comment pages on blockchain explorers. The top sender in
Figure 6, for example, appears to often proﬁt off typographical
errors users make in their decentralized exchange trades. 5 One
user, “Getcoin Hub Inc.”, pleads with this arbitrage bot, saying
“This was obviously a mistake transaction - any chance you
can ﬁnd it in your heart to send it back?”. Another, Benjamin
Huffman, pleads with the bot that “I am a single parent trying
to make ends meet at a job I hate. Please have some mercy.”
Yet another, Alﬁe, leaves a comment requesting the return of
their ETH, stating ”Please I ask you to send me the ETH back
as I really need it to continue my education. I might need to
sell my car to pay what is already due for this semester.” Worse
still, one user, Rajesh Kumar, claims “sir this was error order.
please give back eth sir. this all of my village rupee I trade
for them. if i do not receive back eth i will be in the **** sir
please”.
While it is impossible to verify the authenticity of these
anonymous comments, their existence does point to the effect
that exchanges with bad usability properties and ﬂawed market
designs can have on the guarantees provided their users. The
existence of multiple users losing a large chunk of funds
through such ﬂawed exchange designs embodies the need for
carefully considered and formalized guarantees for DEXes.
V. P RIORITY GAS AUCTION (PGA) M ODELING
To shed light on the strategies we observe in practice, we
present a formal model for PGAs in this section. We then
explain the notion of advantage that we use to understand
strategies’ effectiveness, and study several classes of observed
strategies in the context of our model.
We provide informal, high-level intuition about the games
both miners and bots play in Appendix C.
A. Model properties
We model a PGA as a sequential game among a set of n
players {P0, P1,..., Pn−1} who bid against one another to
obtain a payoff of $1.6
This game has the following properties, which model
blockchain dynamics:
a) Continuous time: Players act in continuous time,
rather than discrete rounds (as in typical extensive-form
games). This is because blockchain networks are asyn-
chronous.
5These comments were sourced from https://etherscan.io/address/
0x0000F7F39325076881E5fC566E99595542532aE2#comments, though
similar pages exist for several of the bots in Figure 6 and our data.
6In this “dollar auction,” $1 represents a normalization of any payoff
amount w.l.o.g., and includes gas costs for the winner.
9

---

## Page 10

b) Imperfect information: Players eventually see one
another’s bids, but not immediately, a feature modeling
blockchain network latency. Player Pi observes other players’
bids after some ﬁxed time ∆i. Players may have differing
latencies, small ones conferring a competitive advantage.
We measure latency as a relative ﬁgure to the latency of the
miners, which are typically the best connected nodes in the
network. Thus ∆i = 0 indicates that Pi has a superior network
position and observes other player’s bids with no additional
delay over that of the miners.
c) All pay: In PGAs, losing players pay gas costs for
their failed transactions. Our model captures this cost by
having a losing player P pay ℓ($blast), where $blast is the
last bid made by P and ℓ() is a loss function .7 This type of
all-pay auction in which players can submit multiple bids is
known as a dollar auction [44], in which not only the winner,
but losers pay. In our study, we typically observe auctions that
are partial all-pay, i.e., ℓ($blast)< $blast.
d) Probabilistic auction duration: The auction ter-
minates at a randomly determined time, namely when the
next block is mined. For proof-of-work blockchains such as
Ethereum, we model a block interval as a random variable D,
which is exponentially distributed.
e) Rate-limited bidding: A player cannot raise her own
bids continuously, but must wait a short interval δ to do so.
This reﬂects throttling that blockchain peer-to-peer networks
perform to prevent ﬂooding attacks. As miners are always free
to include the highest paying transaction that they observed,
players can only raise bids, not lower them (a natural auction
feature that holds in Ethereum PGAs).
f) Minimum starting bid: While there is no required
minimum gas price in Ethereum, in practice PGA participants
will want to start their bid at a price that gives them a good
chance of getting included in the next block. Put another way,
if one bids too low, then even if nobody else bids against
them, a miner may not include the transaction in their block.
Thus, although not strictly enforced, we model our auctions
as having a minimum starting bid, s.
g) Minimum bid increments: Players do not have
freedom to raise bids by arbitrary increments. Instead, there
is a minimum bid raise, ι, measured as a function of the
player’s previous bid. This matches Ethereum dynamics in
which one can replace their transaction with another one, but
it will only be relayed by the peer-to-peer network if the gas
price has increased by a minimum threshold. Parity, the most
common Ethereum node software, enforces a default minimum
increment of 12.5%.
Importantly, the bid increment restriction for Pi is entirely
a function of the Pi’s previous bid, but there is no enforced
relationship between the bids of competing players. That is,
players can outbid one another by arbitrarily small quantities
so long as they are sufﬁciently raising their own previous bid.
In practice, network latencies and transaction-interval times
are stochastic, but we assume constants ∆i and δ to simplify
7As we explain above, bots use various tricks to reduce ℓ.
our analyses. We believe that this simpliﬁcation does not
signiﬁcantly affect strategy outcomes.
Continuous-time, imperfect-information games have seen
only limited study. Most similar to our work is FlipIt, a
continuous-time game with imperfect information that models
advanced persistent threats (APTs) [47]. We are unaware of
any prior work on such games with random play times or in
general with the structure of PGAs.
B. Formal PGA model
For simplicity, we focus on games where n = 2, i.e., that
involve a pair of players (P0, P1). Our formalism, though,
can be generalized to any n. The restriction to two players
is supported by our empirical observations, which shows that
most PGAs were played out between two players.
We let b = (t, $b;i) denote a bid by player Pi. Here t is
the time at which the bid is placed, $b is the bid price, and
i ∈ {0, 1} is the identity of the bidder.
We denote by b∗ the sequence of all bids published to the
network by all players at the current time t∗, and b the full
sequence of all bids made by all players up to the point at
which the auction ends. We let b[t] denote b at a particular
time t. We let bi and its variants (e.g., bi[t]) denote a bid
sequence of player Pi.
A strategySi for player Pi is a procedure for participating in
a PGA, and may be probabilistic (“mixed,” in game-theoretic
terminology). Si takes the following form, where input t∗ is
the current time and σi is the current local state of Pi:
(a,tw,σ′) ←$Si(b∗,t∗
,σ).
The output a is an action by Pi. Either a =b for some bid b,
or else a = ⊥, indicating the player is not placing a bid. The
output σ′
i represents an internal state update for the player.
Finally, tw≥t∗ is a wake time . This is the time when Pi
schedules its next execution assuming no bids appear in the
meantime. The use of wake times means that w.l.o.g., we can
assume that a player always emits a bid b = (t∗, $b;i), i.e., for
immediate publication. We also assume that when executed at
an emitted wake time, a player always emits a bid; a player
that chooses not to schedule a bid can set tw=∞.
a) Game execution: A game between P0 and P1 involves
an execution Exec(S0,S 1, [D,ℓ ()]) of their respective strate-
gies, and accounts for players’ imperfect information due to
their latencies. We specify the procedure for Exec in Figure 19
in Appendix D.
b) Payoffs: Players (bots) compete for ﬁnancial rewards.
We measure these rewards using the standard game-theoretic
notion of a payoff. An execution Exec(S0, ∆0,S 1, ∆1[D,ℓ ()])
outputs a pair ($r0, $r1). These are the respective payoffs
(proﬁts or losses) of P0 and P1.
We deﬁne the payoff of S0 against S1 as follows:
POExec
(S0,∆0)(S1,∆1)[(D,ℓ ())] =
E[$r0 | ($r0, $r1) ←$ Exec(S0, ∆0,S 1, ∆1, [D,ℓ ()]).
10

---

## Page 11

.
We refer to a strategy S0 as null-proﬁtable if
POExec
(S0,∆0)(S∅,∅[(D,ℓ ())] > 0 when S∅ is the null strategy
(i.e., a strategy that never bids and thus its latency is also
irrelevant).
C. Why repeated bidding?
To understand the signiﬁcance of our model, it is helpful to
see why players’ optimal strategies involve placing multiple
bids over time. To show why, it is helpful by contrast to
observe two settings in which players’ optimal strategies
involve placing a single bid.
a) Sealed-bid auction: Suppose that instead of the com-
plex game just outlined, a PGA were a standard sealed-bid
auction (either ﬁrst or second price, withℓ() = 0) [41]. Players
bid once and ties are broken randomly.
Players would then be incentivized to cast a single bid as
close as possible to 1, throwing away almost the entirety of
their potential proﬁt. This behavior is intuitive.
If bids are discrete, with tick sizes (smallest increments) of
ϵ, then there is a Nash equilibrium for S0 =S1, the strategy
of bidding 1 −ϵ. In this case, POExec
S0,S1[(D, 0)] =ϵ/2. Notice
that since only one bid is cast and its sealed, we omit the
latency parameter as it is irrelevant. This is the only Nash
equilibrium for deterministic strategies, since a deviation that
bids an extra ϵ would otherwise be proﬁtable. For randomized
strategies, non-cooperative players will converge towards this
equilibrium after playing multiple games in which they study
one another’s behavior.
b) Fixed block duration: Returning to our model, when
∆i, ∆j > 0, placing multiple bids is a useful strategy only
whenD is a random variable. The reason is that given a block
interval of ﬁxed durationd, players can place the equivalent of
sealed bids in the interval [d −δ,d ] after the mining of the last
block. Thus, in this setting the only reason for repeated bidding
is on-chain signaling of intent, which is more expensive than
out-of-band communication.
c) Proof-of-stake blockchains: Notably, sealed-bid auc-
tions are likely to be the norm on proof-of-stake blockchains,
due to two reasons. First, in many proof-of-stake protocols the
identity of near future miners is known in advance (perhaps
anonymously, i.e., only the individual miner knows her time
slot). This implies that miners can accept bids over secure
(encrypted and authenticated) out-of-band channels. Second,
the block duration is quite predictable in proof-of-stake chains
– miners forfeit their time slot unless they broadcast their block
before a limit (measured according to the local clocks of other
miners) is reached. There is some measure of unpredictability:
the limit should be generous in order to accommodate propa-
gation delays in the network, and miners may wish to collect
many transactions that pay lucrative fees before broadcasting
their block. Still, the block duration should behave according
to statistical patterns that differ greatly from the stochastic
process of PoW blockchains. Our following analysis may thus
apply to proof-of-stake systems with a high enough measure
of unpredictability, though sealed-bid auctions are signiﬁcantly
more likely in such systems.
D. What’s a good strategy?
Subject to their individual latencies, all players have iden-
tical strategy spaces, and thus we can directly compare strate-
gies while only considering the latencies of the players that
executed them. We deﬁne
Advexec
(S0,∆0),(S1,∆1)(D,ℓ ()) =POExec
(S0,∆0,(S1,∆1)[(D,ℓ ())]−
POExec
(S1,∆1),(S0,∆0)[(D,ℓ ())].
VI. P RIORITY -GAS-AUCTION STRATEGIES
We now report on classes of strategies that we have observed
empirically and examine them within the context of our model.
Given the large strategy space, we restrict our focus to the most
prevalent PGA strategies that we have observed.
We thus consider three classes of strategies. The ﬁrst two
strategies are blind raising and counterbidding, which are
often used in competition with one another. We then consider
a cooperative strategy in which players take turns bidding.
While we don’t claim that we are seeing perfect cooperation
(since if we were there would be no need for on-chain bidding
at all), we show the cooperative strategy approximates and
predicts a large class of behaviors that we have observed on-
chain. Finally, we show that under conditions consistent with
the PGAs we are observing on Ethereum, there exist Nash
equilibria for cooperative strategies.
A. Latency Wars
For all strategies that we consider, our model predicts that
players with a lower latency will have an advantage. Validating
this feature of our model, we have observed empirically
that players are consistently and substantially reducing their
respective latencies over time (Figure 9).
B. Blind raising
Blind raising is a simple non-adaptive strategy. Player Pi
raises her own bids under a predetermined schedule, and the
strategy is invariant to b∗
1−i, the history of the other player’s
bids. In PGAs that we have observed, this schedule often
involves repeated increases by ﬁxed fractional increments
(e.g., 12.5%, 21% or 70%). Basic blind raising is thus also
deterministic (“pure”). A basic version may be modeled as
follows:
Blind raising (S0): P0 emits a bid with amount $b0 at
time τ = 0 and $b0 × (1 +f)k at time kδ.
At ﬁrst glance, this strategy, and non-adaptive strategies in
general, seem like a bad idea: They fail to exploit information
available to the player in b∗.
Surprisingly, however, the imperfect information created
by network latency means that a non-adaptive strategy can
achieve an advantage over natural adaptive strategies . The
intuition is this: By playing non-adaptively, a player can
publish a bid faster than by waiting to see the opposing
11

---

## Page 12

06-18 08-18 10-18 11-18 01-19 03-190
0.2
0.4
0.6
0.8
1
Date (MM-YY)
Mean Observed Time Between Bids (s)
Bot Latency Evolution
10
20
30
40
50+
# of Raises
Fig. 9. Evolution of the PGA bots’ latency strategies over time. Each point
is the mean latency of a bot in some observed auction on the plotted date.
The coloring of dots shows the number of total raises each bot placed in
that respective auction. Early in the observed market, the majority of auctions
contained 0-10 raises per bot. Over time, these auctions increasingly contained
more raises and a lower mean latency. We exclude all observed mean latencies
that do not fall between 0 and 1 seconds; there are such latencies, which are
the result of the limitations of our monitoring architecture mentioned in IV-A1.
The number of opportunities per bot, however, illustrates a trend that is far
less vulnerable to instrumentation limitations, as it does not depend on the
order or precise timing of observed transactions.
Reactive counterbidding (S1) :
• At time τ = 0, P1 bids s.
• Denote the most recent bid by P1 as $b1. P1
waits until it sees a bid $b0 > $b1 cast by P0.
P1 immediately counterbids min(max($b1 ×(1+
ι), $b1 +ϵ), 1 +ℓ($b1)).
Fig. 10. Reactive counterbidding PGA strategy. ϵ is the minimum bid tick,
ι is the minimum bid increment, and s is the minimum starting bid. By
bidding max($b1× (1 +ι),P1 ensures that its bid meets the minimum bid
requirement and is also higher than P0’s bid. However, it would never make
sense forP1’s bid to exceed 1 +ℓ($b1)) as at this point it is more proﬁtable
to not bid and instead pay ℓ($b1).
player’s bid and reacting to it. We explain below in particular
how blind raising can achieve an advantage over a natural,
adaptive strategy called reactive counterbidding.
C. Counterbidding
Counterbidding is a strategy in which a player observes
an opponent’s bidding strategy and reacts by placing higher
opposing bids. A simple example of this strategy is what we
call reactive counterbidding, an adaptive strategy that a player
P1 might execute against another player P0. The strategy is
described formally in Figure 10.
Reactive counterbidding can achieve an advantage over a
blind raising strategy— provided, as we shall see, that ∆1 is
small with respect to δ. Counterbidding involves outbidding
P0 as quickly as possible by a small amount, provided that
the bid is raised by the required minimum.
As P0 has interval ≥ δ between bids, reactive counterbid-
ding achieves an interval ≥δ between the bids of P1.
Many consensus algorithms (e.g., Nakamoto consensus)
exhibit D exponentially distributed with mean λ. Under the
simplifying assumption that ℓ($b) = $ c, we can show the
following two observations, which we prove in Appendix D.
Observation 1. Let ∆i = 0 and $r =
Advexec
(S0,∆0),(S∅,∅)(D, $c) be the payoff of null-proﬁtable
blind raising strategy S0 against S∅. Then for
$c
$r + $c <e−λδ,
as ϵ → 0, reactive counterbidding strategy S1 has positive
payoff.
We now show, somewhat counterintuitively, that with the
right parameters—speciﬁcally, when ∆1 is high w.r.t. δ —
blind raising has an advantage over reactive counterbidding.
Observation 2 (Latency Ampliﬁcation). For ∆1 > δ, there
exists a null-proﬁtable, blind raising strategy, S0, such that
for any pure reactive counterbidding strategy S1,S0 achieves
Advexec
(S0,∆0),(S1,∆1)(D,ℓ ())> 0.
D. Cooperation
We now turn our focus to cooperative strategies, which we
believe to be a close approximation to a common behavioral
pattern we observe in which players slowly alternate raising
bids. We demonstrate a cooperative Nash Equilibrium for the
PGA game that helps shed light on the most common bidding
behaviors that we observed.
Notice that as bids are non-decreasing, with each successive
bid that players submit, the maximum proﬁtability of the
opportunity decreases. Intuitively then, it is beneﬁcial for all
players to decrease the total number of bids in the game.
It is natural then to assume that, whenever possible, players
will coordinate out-of-band to split the proﬁts rather than
decrease their proﬁts by competitively bidding on-chain. How-
ever, by the very virtue of us seeing on-chain PGAs, we know
that perfect cooperation does not exist.
For example, if we consider a repeated game in which the
same set of players is bidding on multiple (say for simplicity,
equal value) opportunities, they can coordinate off-chain so
that each opportunity only has a single bid on-chain and the
proﬁt for bidders is maximized. Indeed, in our measurement,
we found many arbitrage opportunities for which there was
only a single player, and it is entirely possible that off-chain
coordination is at play here, although by its very nature there
is insufﬁcient data on chain to conﬁrm this.
While off-chain cooperation may make sense, particularly
in a repeated game, it has some drawbacks including lack of
anonymity. We restrict our analysis here to the more interesting
case of single game instances where players are bidding on-
chain and coordinate their strategies to maximize expected
proﬁts Chief among them is that off-chain coordination is
cumbersome and requires participants to identify themselves
12

---

## Page 13

Cooperative (Si) with parameters D,W :
• At timeτ =V [2k+i], Pi emits a bid with amount
W [2k +i].
• If Pi observes a bid of value $b at time t such
that t<V [2k +i] but $b>W [2k +i − 1], then
Pi immediately bids $1 +ℓ($b).
Fig. 11. Grim-trigger cooperative PGA strategy
and sacriﬁce anonymity. This allows us to gain insight into
the on-chain competitive auctions that we have observed.
As we will see, the cooperative strategies that we study
help explain the behaviors in many of the PGAs that we have
observed. Moreover, we show that under suitable parameters,
there is a Nash Equilibrium for both players to follow a
cooperative strategy.
We stress that for our cooperative equilibrium to emerge, it’s
not necessary that players explicitly coordinate out-of-band,
but this behavior can develop organically on-chain. Indeed, we
have seen evidence that over time, players have moved closer
toward a cooperative equilibrium, which is consistent with well
known results in experimental game theory that participants in
the wild will converge to an equilibrium over time [40, 13].
a) Grim trigger equilibrium: We now describe a partic-
ular cooperative strategy in which any defection is responded
to by immediately bidding the maximum amount, thereby
eliminating all proﬁtability from the auction.
This strategy class is similar to the grim trigger strategy
that appears in the game theory literature in the context of re-
peated games [42]. Notice that since PGAs involve successive
opportunities to bid potentially in response to the bids of other
players, even a single iteration of our auction has elements of
a repeated game.
Consider two players who coordinate with the following
strategies: at set intervals, players alternate their bids, each
time bidding the minimum increase. If any player deviates
either by bidding too soon or by raising the bid higher than
they are supposed to, the other player will respond by raising
their bid such that the game is no longer proﬁtable. This
strategy is characterized by following parameters: V is the
set of agreed upon times at which bids will be scheduled, and
W is the set of agreed upon bid values, such that that W [i]
will be bid by the appropriate player at time V [i].
The grim-trigger cooperative strategy is formally described
in Figure 11.
Notice that in the second condition, we assume that Pi can
determine the time t that the bid was emitted by P1−i. This is
consistent with our model in which the latency of each player
is known. Thus, even though Pi will not observe P1−i’s bid
until time t+∆i, it can compute t by subtracting ∆i from the
time that it ﬁrst observed the bid.
As we will see, the knowledge gap due to latency is an
important feature when determining if our model has an
equilibrium. All defections will eventually be detected, but
06-18 08-18 10-18 11-18 01-19 03-190
20
40
60
Date (MM-YY)
Median Raise Percent Over Own Bid
Raise Strategy Evolution
y=15
y=12.5
0
0.2
0.4
0.6
0.8
1+
Revenue (ETH)
Fig. 12. Evolution of the PGA bots’ median raise strategies over time for bots
with more than 4 bids in pure revenue PGAs. Note the strategy convergence
in the iterated game to almost exclusively the 12.5 (minimum raise) and 15%
(deviation from minimum raise) levels. Opportunities below the y = 12.5
line are likely artifacts of bots emitting multiple transactions from globally
distributed nodes; these opportunities correspondingly show a bias towards
high revenue compared to those using the predicted strategies. We trim outliers
and omit points with median raises over 75%; we observe 5 such high-raise
outliers of 4,007 total observations.
depending on the latencies, there may still be sufﬁcient time
to proﬁt from deviating.
b) Minimum bid raises: In a cooperative PGA, the main
function of bidding on-chain is to alternate bids between
players, but all players are incentivized to keep the actual bid
price as low as possible to maximize proﬁt. The following
observation follows:
Observation 3. In a grim-trigger cooperative PGA, for all
i ≤imax, the optimal choice for bids is W [0] =s andW [i] =
W [i − 1] × (1 +ι).
Remarkably as shown in Figure 12, in our observed PGAs,
players converge over time to a minimum bid raise of 12.5%,
which is the minimum allowed raise in the Parity client. It
is known that players in the wild will converge to Nash
Equilibria [13, 40] and this on-chain behavior is consistent
to a convergence toward elements of cooperative equilibrium.
We stress that we don’t claim that perfect cooperation is
occurring or even that our exact equilibrium is on play. We
do claim, however, that players are converging to a more
cooperative state, that is approximated by our model, in which
they allow opportunities for other players in an effort to
maximize their own expected proﬁt over time.
c) Nash equilibrium: We now present our main result
showing that there exist Nash equlibria for a wide range of
parameters using the grim-trigger cooperative strategy.
Theorem 1. For parameters consistent with Ethereum PGAs,
there exist a grim-trigger Nash equilibria for a 2 player PGA
where both players follow a D,W cooperative strategy.
Figure 13 and Figure 14 show the expected payoff of
the bidder and non-bidder in a cooperative PGA. The x-axis
13

---

## Page 14

Fig. 13. Cooperative PGA with interval t = 2
Fig. 14. Cooperative PGA with interval t = 0.4
indicates the starting time of the interval, where the expected
duration of the game is 1/λ = 15 seconds. The y-axis indicates
the expected payoff. Note that the players are alternating: if
Player 1 is the bidder and Player 2 is the non-bidder when the
ﬁrst interval starts, then Player 1 is the non-bidder and Player 2
is the bidder when the second interval starts. These ﬁgures also
display the proﬁtability of deviation, i.e., the expected payoff
of the non-bidder (according to latency parameters) in case
she deviates when the interval begins.
If the deviation payoff surpasses the non-bidder payoff at
any point (as with the delay=3 plot in Figure 13), then
a Nash equalibrium cannot hold for those parameters – a
backward induction argument implies that if it is proﬁtable
for the non-bidder (say, Player 1) of interval i to deviate, then
it must also be proﬁtable for the non-bidder (Player 2) of
intervali − 1 to deviate, and so on.
Figure 14 corresponds to the Ethereum parameters per our
empirical measurements: t = 0.4 seconds is the mean interval
length and δ = 0.1 seconds is the estimated latency in our
measurements.
To prove our main claim, let us recall that each player’s bid
increments her previous bid by 12.5%. Given our measure-
ments, this implies 17 rounds before the players give the entire
auction’s reward to the miners. We can thus verify that in each
of the few dozens of intervals prior to the end of the game,
the expected payoff of adhering to the cooperative strategy
is larger than the expected payoff upon deviation. Indeed,
the Ethereum parameters that are plotted in Figure 14 show
that the expected non-bidder payoff is always greater than the
expected payoff of deviation. Theorem 1 thus follows.
VII. M INER -E XTRACTABLE VALUE AND BLOCKCHAIN
SECURITY
PGAs and DEX arbitrage may not seem immediately harm-
ful or relevant to the security of an underlying blockchain.
They might simply seem an efﬁcient mechanism for convey-
ing market information among network participants. Unfortu-
nately, we now argue, DEXes in fact present a serious security
risk to the blockchain systems on which they operate, i.e., at
the consensus layer . In other words, a key result of our work
is that application-layer security poses a current and direct
threat to consensus-layer security .
In a stable blockchain, block rewards incentivize honest
miner behavior. As we show empirically in this section,
though, order optimization (OO) fees, or implicit fees a miner
is able to reap by leveraging their control of a consensus
epoch, can exceed the block reward and instead incentivize
forking attacks. To capture OO fees, a miner can reorder
users’ transactions and potentially insert their own, reaping
proﬁt in Ether directly to their account. For example, a miner
could execute the pure revenue transactions described in this
work themselves, while still claiming the PGA fees for all the
“losing” arbitrage bots attempting to do the same.
OO fees represent one case of a more general quantiﬁable
value we call miner-extractable value (MEV). MEV refers to
the total amount of Ether miners can extract from manipulation
of transactions within a given timeframe, which may include
multiple blocks’ worth of transactions. In systems with high
MEV , the proﬁt available from optimizing for MEV extraction
can subsidize forking attacks of two different forms. The ﬁrst
is a previously shown undercutting attack [14] that forks a
block with signiﬁcant MEV . The second is a novel attack,
called a time-bandit attack, that forks the blockchain retroac-
tively based on past MEV .
Undercutting attacks were previously considered a risk
primarily in the distant future, when block rewards in Bitcoin
are expected diminish below transaction fees. By measuring
the signiﬁcance and magnitude of OO fees, our work shows
that undercutting attacks are a present threat.
Time-bandit attacks are also a present and even larger
threat. They can leverage not just OO fees, but any forms of
miner-extractable value obtained by rewinding a blockchain.
Time-bandit attacks’ existence implies that DEXes and many
other contracts are inherent threats to the stability of PoW
blockchains, and the larger they grow, the bigger the threat.
A. OO fees: Measurement study
We now lower bound the severity of OO fees in DEXes.
Figure 15 shows the distribution of pure revenue OO fees
as a fraction of total miner-extractable value in Ethereum. We
conservatively estimate MEV in this context as the sum of
explicit transaction fees and pure revenue OO fees, making
14

---

## Page 15

0 0.2 0.4 0.6 0.8 10
0.05
0.1
0.15
Proportion of Transaction Fees from Pure Revenue OOFraction of Blocks
Pure Revenue OO Fee Share of Total Transaction Fees
Fig. 15. Distribution of pure revenue OO as percentage of block transaction
fees in blocks containing such transactions on the Ethereum network, blocks
3875490 to 7408826; 133,815 of 3,533,336 contain observed pure revenue
(3.6%). Since block 7,000,000 (Jan 2 2019), this has increased to 6.3%.
our distribution an underestimate of the share of MEV that
does not come from explicit fee payments in Ethereum. Note
that PGAs themselves are an indirect mechanism for miners
to claim OO fees: if miners instead claimed OO fees directly,
there would be no incentive to bid in or create a PGA.
Of all blocks since block 3,875,490 (the ﬁrst block we
observed with a pure revenue OO fee from decentralized
exchange arbitrage), approximately 3.6% contain at least one
pure revenue arbitrage transaction. Of these blocks, 17,897
blocks contain pure revenue OO proﬁts that are < 1% of
the total stealable fees, conﬁrming our earlier conclusions
that the most frequent pure revenue arbitrage opportunities
are for small price differences in the course of normal trad-
ing across exchanges. Nonetheless, many blocks do contain
substantial pure revenue fees. 36,860 observed blocks contain
pure revenue fees that exceed 20% of total stealable fees,
12,002 blocks derive the majority (over 50%) of stealable fees
from pure revenue, and 2,517 blocks derive more than 80%
of stealable fees from pure revenue.
Occasionally, these fees can be substantial and provide
substantial miner incentives to orphan blocks or otherwise
deviate from the mining protocol. Figure 16 shows the 20
blocks observed on Ethereum with the highest absolute pure
revenue OO fees.
As an example, the highest block, block 7029147 (https:
//etherscan.io/block/7029147), contained an arbitrage trade
generating a revenue of 101.6 ETH, dwarﬁng the block reward
of 3 ETH and the insigniﬁcant explicit transaction fees of
0.022 ETH. In this particular block, one transaction generated
all the pure revenue OO fees. This transaction, whose proﬁt
graph is available at https://bit.ly/2D4U57c, saw an exchange of
Bigbom token (BBO) for ETH on Bancor and Kyber; an error
in Bancor’s pricing formula allowed a user to buy BBO at
rates far under market. The bot’s order size was 101.6 ETH,
7029147
4618363
7372878
4725889
6129904
4359715
4321329
4218201
4511858
4526402
4769615
5074099
4820021
4929936
4956461
6129903
7372880
6335886
4289436
4597319
0
50
100
Block Number
Miner Revenue (ETH)
Highest Observed Pure Revenue OO Blocks
OO fees Transaction fees Block reward
08-01-19
25-11-17
15-03-19
13-12-17
11-08-18
12-10-17
29-09-17
30-08-17
08-11-17
10-11-17
21-12-17
12-02-18
29-12-17
18-01-18
23-01-18
11-08-18
15-03-19
15-09-18
19-09-17
21-11-17
0
50
100Date of Block (DD-MM-YY)
Fig. 16. Blocks with the highest pure revenue OO fees observed on Ethereum.
As is shown here, OO fees in these blocks dominate both block rewards and
transaction fees, often by more than an order of magnitude.
of which almost all was taken as pure proﬁt.
As with all our analyses, we stress that our measurements
are conservative: They represent lower bounds on arbitrage
behavior. The limitations in our instrumentation harness dis-
cussed in Section IV-A1, lead to potential underestimation.
B. Undercutting attacks
Undercutting attacks [14] represent one vector of attack that
can leverage OO fees.
It is well known that ﬁxed per-block miner rewards are
a key feature of secure and stable cryptocurrency protocols,
as originally described in [14]. In that work, the authors
analyze the incentives of blockchain miners in a regime where
transaction fees exceed the inﬂationary subsidy paid to miners
by a blockchain protocol. They observe that when the block
reward is dominated by fees, rewards have high variance. As
a result, a miner can fork a high-fee block, holding back some
fees to attract other miners to build on the fork. In extreme
cases, incentives to deviate from the protocol may lead to
disruption in miner strategies for economically rational miners,
reducing the security provided by block conﬁrmations.
Prior to our work, transaction fees have been viewed as
the only source of value for undercutting attacks, with [14]
even calling a world in which fees dominate block rewards
a “transaction-fee regime.” That regime seemed a distant
prospect. The title of [14], “On the Instability of Bitcoin
Without the Block Reward,” refers to Bitcoin block rewards
going to zero, an event anticipated around the year 2140.
Our study shows that OO fees are a form of value that
sometimes dominates explicit transaction fees today. The tail
of the distribution in Figure 15 (transaction fee proportions >
0.5) and all of the example blocks in Figure 16 represent such
15

---

## Page 16

opportunities. In other words, undercutting attacks represent a
present threat in Ethereum, and one that will grow with the
success of smart contracts that attract OO fees. Other potential
sources of OO fees are mentioned in [15].
Most importantly, our view of arbitrage remains conser-
vative, and we emphasize that pure revenue opportunities
represent a small slice of total ordering fees. There are many
possible sources of ordering fees payable to miners, includ-
ing more sophisticated arbitrage. There are also many other
forms of miner-extractable value. Miners can “steal” arbitrage
opportunities from arbitragers by taking them themselves.
Additionally, the survey in [18] describes several other sources
of MEV , including the ability to buy into proﬁtable ICOs early
and the manipulation of games of chance.
Undercutting attacks can leverage OO fees or any other
MEV from newly generated blocks. The second attack we
describe can use MEV from past blocks to subsidize an attack.
C. Time-bandit attacks
We now describe time-bandit attacks, a new, second attack
vector that can exploit miner-extractable value. They can
exploit MEV from new blocks, but more powerfully, can also
use MEV from past blocks via rewinding.
Time-bandit attacks are conceptually simple. Suppose a
blockchain has a sufﬁx (subchain) [height0, height1], with
current block height height1, in which stealable value exceeds
block rewards. An adversary can rewind to height0 and use
the resulting MEV to subsidize a proﬁtable 51% attack that
mines a fork up to or past height1.
Of course, a time-bandit attack relies on real-time access to
massive mining resources. As noted in [6], however, “rental
attacks” are feasible using cloud resources, particularly for sys-
tems such as Ethereum that rely heavily on GPUs, which are
standard cloud commodities. Sites such as http://crypto51.app/
estimate the costs. We illustrate with an example that relies
on MEV from DEX rewinding.
Example 1. Consider a price spike from 1 USD to 3 USD in
a token that trades on an on-chain automated market maker
(e.g., Bancor [1]). A miner performing a time-bandit attack
can now rewrite history such that it is on the buy side of
every trade, accruing a substantial balance in such a token at
below market rate— before the price spike .8
For example, if the attacker wishes to rewrite 24 hours of
history, and 1M USD of volume occurred in exchanges with
rewritable history in that token, then the attacker can obtain
a MEV gross proﬁt of 1 M × (3 USD - 1 USD) = 2M USD. 9
At the time of writing (March 2019), http://crypto51.app/
estimates a 24-hour 51% rental-attack cost on Ethereum of
about 1.78M USD, implying a net proﬁt of around 220K USD.
We stress that time bandit attacks are not limited to MEV
from DEXes. A variety of smart contract systems allow anyone
8The attacker can additionally use new user trades at the market 3 USD
price in the automated market maker system to ofﬂoad their tokens into ETH.
9More sophisticated reordering strategies stand to proﬁt the miner even
more. The miner can selectively include orders that manipulate the prices
received by other traders in the past .
to participate and earn proﬁt for doing so, often a desirable
design goal for the style of permissionless and open interaction
that lends itself naturally to blockchains. Any on-chain action
in the past that could have potentially proﬁted a miner today,
including actions that unconditionally earn them ETH in
the past, are thus potential sources for time-bandit attacks.
Because smart contracts are Turing complete scripts and carry
complex interactions, estimating the size of these opportunities
is a challenging problem we defer to future work.
Time-bandit attacks in Ethereum: Recent transaction statistics
suggest that Ethereum is vulnerable to time-bandit attacks.
For example, decentralized exchange volumes show a peak of
1.5 billion USD of traded assets on Ethereum’s decentralized
exchanges in July 2018 [23]. While it is hard to gauge the
total stealable value in this volume, the current estimated
one-month cost of a 51% attack on Ethereum according to
http://crypto51.app/ is approximately 56 million USD, more
than 25 times lower than this DEX volume .
We posit that the OO fees alone that we have described
threaten the security of today’s Ethereum network. As Fig-
ures 15 and 16 show, blocks with high OO fees and/or
arbitrage opportunities can already enable such attacks.
More generally and alarmingly, time-bandit attacks can be
subsidized by a malicious miner’s ability to rewrite proﬁtable
trades retroactively, stealing proﬁts from arbitrageurs and
users while still claiming gas fees on failed transactions that
attempt execution. The resulting MEV is potentially massive,
suggesting a possibly serious threat in Ethereum today .
Of course, a full analysis of the threat would require an
understanding of how time-bandit attackers might compete
against one another to harvest MEV—by analogy with PGAs.
This is a topic for future research.
VIII. O PEN QUESTIONS AND FUTURE WORK
Our results raise many important questions, some about
the arbitrage community itself. For example, it would beneﬁt
arbitrageurs to collude with miners, but we observe no such
collusion: Preliminary experiments show that bot transactions
are equally distributed across mining pools. Are there incen-
tives to avoid collusion, such as concern about the exogenous
impact of miner malfeasance coming to light?
Other questions arise from PGA modeling. Are PGAs
positive- or negative-sum games? In what ways could our
proposed model be helpfully enriched?
More broadly, it is important to observe that DEXes are
just the tip of the iceberg. At the time of writing, IDEX, the
largest, is ranked #119 by volume by coinmarketcap.com. It
has about 1M USD in 24h volume, compared with 970M USD
for Binance, the leading centralized exchange. DEX volume
is roughly 0.01% that on centralized exchanges.
Malfeasance in centralized exchanges might well be
rampant—possibly even more egregiously so than in
DEXes [5]. As activity in such exchanges takes place off-
chain, it is private, and cannot easily be ascertained without
privileged access. Additionally, while centralized exchange
16

---

## Page 17

malfeasance might seem not to impact on-chain security,
the two are inextricably linked. By altering token trading
dynamics on-chain, an adversary could manipulate and proﬁt
from centralized exchange dynamics. For example, a time-
bandit attack could accumulate cheap tokens for ofﬂoading in
a centralized exchange.
These observations raise several key follow-up questions:
• What forms do arbitrage take in centralized exchanges
and at what volumes? And frontrunning?
• Barring direct data access, what techniques can be used
to accurately measure various forms of trading activity in
centralized exchanges?
• What ﬁnancial incentives do centralized exchanges create
for malfeasances in DEXes? How might they impact
blockchain stability?
• What other insights might our data yield on DEX ar-
bitrage, especially in quantifying opportunities that are
not pure revenue? How much larger is the full arbitrage
economy than executed? Can tight bounds be developed
for the amount of MEV on Ethereum today?
IX. C ONCLUSION
We have reported on a sizable economy of bots proﬁting
from opportunities provided by transaction ordering in DEXes.
We quantify the breadth of a speciﬁc subset of arbitrage,
pure revenue opportunities , providing lower bounds on the
proﬁtability of ordering manipulation.
We have also formally modeled the behavior of bots com-
peting against each other for miner-supplied transaction prior-
ity in priority gas auctions. Our empirical study validates sev-
eral key predictions of our model, including the convergence
of bots on a form of proﬁtable cooperation involving minimal
gas-price increases. We also show that in many concrete cases,
bots’ revenue from pure revenue arbitrage alone far exceeds
the Ethereum block reward and transaction fees.
Finally, we argue that miner extractable value , particularly
in the form of order optimization fees , implicit fees from
modifying transaction order, threatens blockchain consensus
stability. Such fees are large enough to subsidize serious
attacks on the network. They constitute an economic vulnera-
bility that should be a current cause for concern in Ethereum.
ACKNOWLEDGMENTS
We would like to thank Matt Weinberg for productive
discussions surrounding our model of priority gas auctions.
This material is based upon work supported by the Na-
tional Science Foundation Graduate Research Fellowship un-
der Grant No. DGE-1650441, as well as by NSF grants CNS-
1514163, CNS-1564102, and CNS-1704615, as well as by
ARO grant W911NF16-1-0145.
We also thank IC3 industry partners for their support in
funding this work.
REFERENCES
[1] Bancor Network . www . bancor . network. Referenced
March 2019.
[2] Iddo Bentov et al. The Cost of Decentralization in 0x
and Etherdelta. http://hackingdistributed.com/2017/08/
13/cost-of-decent/. Aug. 2017.
[3] Henry Berg, Todd A. Proebsting, et al. “Hanson’s auto-
mated market maker”. In: Journal of Prediction Markets
3.1 (2009), pp. 45–59.
[4] Dan Bernhardt and Bart Taub. “Front-running dynam-
ics”. In: Journal of Economic Theory 138.1 (2008),
pp. 288–296.
[5] “Bitﬁnex’ed in an Exclusive Interview: ‘Someone Must
Warn People About Fraud’”. In: The Bitcoin News (22
June 2018).
[6] Joseph Bonneau. “Hostile blockchain takeovers (short
paper)”. In: International Conference on Financial
Cryptography and Data Security . Springer. 2018,
pp. 92–100.
[7] Lorenz Breidenbach, Philip Daian, and Florian Tramer.
GasToken. https://gastoken.io/. Mar. 2018.
[8] Eric Budish, Peter Cramton, and John Shim. “The high-
frequency trading arms race: Frequent batch auctions as
a market design response”. In: The Quarterly Journal
of Economics 130.4 (2015), pp. 1547–1621.
[9] V Buterin. “Schellingcoin: A minimal-trust universal
data feed”. In: Ethereum Blog (2014).
[10] Vitalik Buterin. Ethereum sharding faq . 2017.
[11] Vitalik Buterin. Hard Fork Completed . https : / / blog .
ethereum.org/2016/07/20/hard- fork- completed/. July
2016.
[12] Vitalik Buterin and Virgil Grifﬁth. “Casper the friendly
ﬁnality gadget”. In: arXiv preprint arXiv:1710.09437
(2017).
[13] Antonio Cabrales, Rosemarie Nagel, and Roc Armenter.
“Equilibrium selection through incomplete information
in coordination games: an experimental study”. In:
Experimental Economics 10.3 (2007), pp. 221–234.
[14] Miles Carlsten et al. “On the instability of bitcoin with-
out the block reward”. In: ACM CCS. 2016, pp. 154–
167.
[15] Jeremy Clark et al. “On Decentralizing Prediction Mar-
kets and Order Books”. In: WEIS. 2014.
[16] Phil Daian. Analysis of the DAO exploit . http : / /
hackingdistributed.com/2016/06/18/analysis- of- the-
dao-exploit/. June 2016.
[17] Phil Daian, Rafael Pass, and Elaine Shi. “Snow white:
Robustly reconﬁgurable consensus and applications to
provably secure proofs of stake”. In: Iacr. 2017, pp. 1–
64.
[18] Shayan Eskandari, Seyedehmahsa Moosavi, and
Jeremy Clark. “SoK: Transparent Dishonesty: front-
running attacks on Blockchain”. In: arXiv preprint
arXiv:1902.05164 (2019).
17

---

## Page 18

[19] Etherscan.com. https : / / etherscan . io / chart / blocktime.
Referenced Apr. 2018.
[20] Ittay Eyal and Emin G ¨un Sirer. “Majority is not enough:
Bitcoin mining is vulnerable”. In: Financial Cryptogra-
phy. Springer. 2014, pp. 436–454.
[21] Gianni Fenu et al. “The ICO phenomenon and its re-
lationships with ethereum smart contract environment”.
In: 2018 International Workshop on Blockchain Ori-
ented Software Engineering (IWBOSE) . IEEE. 2018,
pp. 26–32.
[22] Neil Gandal et al. “Price manipulation in the Bitcoin
ecosystem”. In: Journal of Monetary Economics (2018).
[23] Georgi Georgiev. Decentralized Exchange Trading Vol-
ume Hits All-Time Low . https : / / bitcoinist . com /
decentralized - exchange - trading - volume - low/. Jan.
2019.
[24] Yossi Gilad et al. “Algorand: Scaling byzantine agree-
ments for cryptocurrencies”. In: Proceedings of the 26th
Symposium on Operating Systems Principles . ACM.
2017, pp. 51–68.
[25] Ari Juels, Ahmed Kosba, and Elaine Shi. “The Ring
of Gyges: Investigating the future of criminal smart
contracts”. In: ACM CCS. 2016, pp. 283–295.
[26] Olga Kharif. “CryptoKitties mania overwhelms
Ethereum network’s processing”. In: Bloomberg (4
Dec. 2017).
[27] Aggelos Kiayias et al. “Ouroboros: A provably se-
cure proof-of-stake blockchain protocol”. In: Annual
International Cryptology Conference . Springer. 2017,
pp. 357–388.
[28] Sunny King and Scott Nadal. PPCoin: Peer-to-Peer
Crypto-Currency with Proof-of-Stake. 2012.
[29] Eleftherios Kokoris-Kogias et al. “Omniledger: A se-
cure, scale-out, decentralized ledger via sharding”. In:
2018 IEEE Symposium on Security and Privacy (SP) .
IEEE. 2018, pp. 583–598.
[30] Ahmed Kosba et al. “Hawk: The blockchain model of
cryptography and privacy-preserving smart contracts”.
In: IEEE S&P. 2016, pp. 839–858.
[31] Jae Kwon. “Tendermint: Consensus without mining”.
In: Draft v. 0.6, fall (2014).
[32] S Demian Lerner. Rootstock: Bitcoin powered smart
contracts. 2015.
[33] Michael Lewis. Flash Boys: a Wall Street revolt .
W.W. Norton & Company, 2014.
[34] Loi Luu et al. “Making smart contracts smarter”. In:
ACM CCS. ACM. 2016, pp. 254–269.
[35] Viktor Manahov. “Front-Running Scalping Strategies
and Market Manipulation: Why Does High-Frequency
Trading Need Stricter Regulation?” In: Financial Re-
view 51.3 (2016), pp. 363–402.
[36] Patrick McCorry, Siamak F Shahandashti, and Feng
Hao. “A smart contract for boardroom voting with
maximum voter privacy”. In: International Conference
on Financial Cryptography and Data Security. Springer.
2017, pp. 357–375.
[37] Patrick McCorry et al. “Pisa: Arbitration Outsourc-
ing for State Channels.” In: IACR Cryptology ePrint
Archive 2018 (2018), p. 582.
[38] Robert McMillan. “The inside story of Mt. Gox, Bit-
coin’s $460 million disaster”. In: Wired. March 3
(2014).
[39] Jonathan Meng. “Understanding Gambling Behavior
and Risk Attitudes Using Massive Online Casino Data”.
Dartmouth Univ., 2018.
[40] Rosemarie Nagel. “Unraveling in guessing games: An
experimental study”. In: The American Economic Re-
view 85.5 (1995), pp. 1313–1326.
[41] Tim Roughgarden. Lecture #2: Mechanism Design Ba-
sics. http://theory.stanford.edu/ ∼tim/f16/l/l5.pdf. Sept.
2013.
[42] Tim Roughgarden. Lecture #5: Incentives in Peer-to-
Peer Networks. http://theory.stanford.edu/∼tim/f16/l/l5.
pdf. Oct. 2016.
[43] Tuomas Sandholm et al. “Winner determination in com-
binatorial auction generalizations”. In: Proceedings of
the ﬁrst international joint conference on Autonomous
agents and multiagent systems: part 1 . ACM. 2002,
pp. 69–76.
[44] Martin Shubik. “The dollar auction game: A paradox in
noncooperative behavior and escalation”. In: Journal of
conﬂict Resolution 15.1 (1971), pp. 109–111.
[45] Nick Szabo. “Formalizing and securing relationships on
public networks”. In: First Monday 2.9 (1997).
[46] Uniswap Exchange Protocol . www.uniswap.io. Refer-
enced March 2019.
[47] Marten Van Dijk et al. “ FlipIt: The game of ‘stealthy
takeover’”. In: Journal of Cryptology 26.4 (2013),
pp. 655–713.
[48] Will Warren and Amir Bandeali. “0x: An open
protocol for decentralized exchange on the
Ethereum blockchain”. In: URl: https://github.
com/0xProject/whitepaper (2017).
[49] Gavin Wood. Ethereum: A secure decentralised gen-
eralised transaction ledger . 2014. URL: http : / /
yellowpaper.io/.
[50] Fan Zhang et al. Paralysis Proofs: Secure Dynamic
Access Structures for Cryptocurrencies and More. IACR
ePrint 2018/096. 2018.
[51] Fan Zhang et al. “Town Crier: An authenticated data
feed for smart contracts”. In: ACM CCS. ACM. 2016,
pp. 270–282.
APPENDIX A
SMART-CONTRACT -E NABLED COMPLEX
NONDETERMINISM
Although this work often focuses on pure revenue opportu-
nities, not all opportunities are pure revenue.
While arbitrage bots’ intent is often clear by inspection
of their transactions, other times, intent may be opaque,
nondeterministic, or may depend on unpredictable aspects
of the Ethereum network state. The smart contract wrappers
18

---

## Page 19

07-17 01-18 08-18 02-19
102
103
104
105
106
107
Date (MM-YY)
Daily Pure Revenue Captured (USD)
Pure Revenue Market Size (USD)
102
103ETH Price (USD)
Fig. 17. Size of the pure revenue market in USD as shown in Figure 4 for
ETH, displayed with USD/ETH price overlay.
through which bots can execute transactions enable more
than simple batching of transactions. Such contracts are actu-
ally atomically-executing programs written in Turing-complete
scripting languages, and can therefore implement complex
strategies.
For example, during, before, or after executing a set of
trades, a wrapper contract can also query prices from and
conditionally trade with automated market makers. Because
the prices offered by these automated market makers cannot
be known in advance, and because batches can revert, even
based on changes in the Ethereum global state and the success
of other batches, orders placed through smart contracts can
express complex conditional preferences on trade execution.
Complex trades can also perform arbitrary computation on
the Ethereum network. Such complex order types do not have
analogs in traditional HFT, but are similar to (and more general
than) proposals such as [43].
APPENDIX B
ADDITIONAL DATA ANALYSES
A. Pure Revenue USD Market
Figure 17 shows the ETH price and size of the pure
revenue market in USD. When compared to the equivalent
graph denominated in ETH (Figure 4), some effect of price
reductions on the market size are evident. Opportunities in
ETH are relatively consistent and well distributed, as we
expect from mechanical rents extracted due to exchange design
fundamentals. Such USD graphs appear more correlated with
the price, showing decreased revenue during price slumps and
contradicting our other data about the sophistication of the
PGA bot market increasing over time.
Because of this and the relevance of ETH to direct protocol
security analyses, we denominate the majority of our synthe-
sized results in ETH.
B. Pure Revenue, Broken Down by Bots
Figure 18 shows the size of the full pure revenue opportunity
market captured by the top 10 transaction senders; note that
the graph is very similar to the graph of the estimated proﬁts
we calculate, having a relatively constant offset and almost
identical shape for all market players.
This may reﬂect imperfections in our heuristics for calculat-
ing proﬁt; we cannot include, for example, server costs, and it
is difﬁcult to tell which on-chain transactions other than a pure
revenue transaction may have contributed to a bot’s speciﬁc
costs. We also do not include costs of failing to capture com-
petitive pure revenue opportunities, which may be signiﬁcant;
it is difﬁcult to disambiguate these failed transactions from
unrelated transactions, as they may never execute or attempt
to execute the intended trades. These matters are left to future
work and analyses of the data we publish.
APPENDIX C
PGA S AND THEIR PARTICIPANTS ’ GAMES
To provide some informal intuition for the modeling we
explore in V we now describe the perspective of both bots and
miners participating in PGAs. This also provides the basis for
our later claims that PGAs have the ability to lead to systemic
instability in blockchains, degrading their security, a notion
we explore fully in Section VII.
A. The miner perspective
From the point of view of the miner who is eventually going
to mine a block, the economic game proceeds as follows.
At some point in time (along the approximate objective time
axis displayed in Figure 2), the miner takes a snapshot of
all transactions it has seen on the peer to peer network, and
includes the highest fee transactions in a block template that
it attempts to solve the proof of work on, converting the block
template into a block able to be propagated to the network.
When this snapshot is taken, the highest n transactions
generated by PGA bots are included in the block. n is the
number of unique (account, nonce) pairs observed in the epoch
and therefore the number of unique eligible bidders: recall
each (account, nonce) can only be mined once. The highest
paying transaction is included ﬁrst, and captures the associated
revenue of the opportunity. The remaining transactions are
included in descending order of gas price, or marginal cost
per instruction.
If all “bids” are competing for the same pure revenue oppor-
tunity, transactions after the ﬁrst receive no revenue. If such
bids are complex probabilistic orders which are not inherently
mutually exclusive, we may expect to see decreasing power-
law proﬁts, the lions share of which go to the ﬁrst arbitrageur.
Note that in Figure 2, the mined block template was likely
formed immediately after the winning transaction and before
the next transaction with the same (account, nonce) pair;
otherwise, the higher fee transaction would have been included
by the miner to maximize revenue. This means that the block
template that would ﬁnally win this game was created by the
miner around second 5. Note also that arbitrageurs continue
19

---

## Page 20

07-17 08-17 10-17 11-17 01-18 03-18 04-18 06-18 08-18 09-18 11-18 01-19 02-19
10−2
10−1
100
101
102
103
104
105
Date (MM-YY)
Daily Pure Revenue Captured (USD)
Pure Revenue Per Bot, 14-Day Moving Average
Market Total
0x0000f7..
0x44e05b..
0xaa2432..
0xb3707d..
0xf13ecd..
0x5a2896..
0xbb3a8c..
0xa53170..
0x905451..
0x00bd1f..
Fig. 18. Pure revenue bot breakdown, as described in Section IV, showing revenue without subtracting transaction costs.
to bid after this result is locked in, unaware that this pool
has formed the template that will eventually constitute a valid
block, showing their imperfect information with regards to this
game. After some delay, the bots learn of the outcome, and
stop bidding in the auction.
This picture overview clearly that it is in the miner’s
best interest to refresh the block templates it is mining on
as quickly as possible. Let us assume the real block was
mined after the end of the auction, around second 15. This
assumption is reasonable, as there is no incentive for the
bots we observe to continue bidding after they are made
aware a block is discovered, and there is also substantial
incentive for miners to optimize propagation latency to the
network (see e.g. [20]. Had the miners instead included
the transactions that bid highest in this action, their total
capture proﬁt would be 231520 · 8856.24 Gwei =x ETH for
bot 0xb8D76f4BC2518F8eb508bf0Ccca76f8F9DD57a3f,
and 227534 · 7716.48 Gwei = y ETH for bot
0x6BEcAb24Ed88Ec13D0A18f20e7dC5E4d5b146542,
for a total of z ETH gained by an optimal miner. Assuming
the third bot would have bid similarly to these two bots
and would have contributed equally to the miner’s reward,
MiningPoolHub’s suboptimality in this instance cost q ETH.
It is obvious to see why substantial arbitrage opportunities
then directly alter miner strategies, by incentivizing them to
optimize on template refresh latency as described above. If
PGA opportunities increase, we expect to see such optimiza-
tions in practice.
B. The PGA bot perspective
From the perspective of the bots competing for block space
in PGAs, the game looks very different. Bots, like miners, see
transactions on the public peer to peer network performed by
their peers. They are able to simulate the execution of these
transactions, read the orderbooks of decentralized exchanges,
and issue orders. Bots should optimize on latency to other bots
to gain information more quickly about their actions. Bots
should also optimize on latency to miners, to make it more
likely that at the time when the miners form the template, their
bid was the last bid received by the miner and therefore reﬂects
the most market information. We explore the full space of
bot strategies in Section V. Our model shows that optimizing
for latency is proﬁtable for a bot participating in this market,
and draws the connection to high frequency (latency-sensitive)
trading in traditional markets.
APPENDIX D
ADDITIONAL PGA MODELING DETAILS
Proof of Observation 1. S1 counterbids after time δ. Since D
has distribution Exp(λ), the probability that any bid by S0 will
have priority in a mined block is Pr[X <δ], for X a random
variable with distribution Exp(λ). This holds with probability
1 −e−λδ. Thus, the payoff of S1 is positive if:
e−λδ$r − (1 −e−λδ)$c> 0.
The observation follows.
Proof of Observation 2. Since ∆i > δ, S0 can schedule its
bids at intervals less than ∆i. Thus, by the time P1 observes
a bid $bi, P0 has already cast a new bid $bi+1. Since S1 is
pure, P1 can choose a value $bi+1 that outbids S′
0s reactive
bid to $bi. Thus P1’s bids will always maintain the highest
bid and win the PGA.
Observation 4. There exists a ﬁnite number of intervals imax
for a cooperative PGA after which bidding is no longer
proﬁtable, even if the block has not yet been mined.
Proof. Letimax be the greatest value for which the following
inequality holds:
s × (1 +ι)imax ≤ 1 +c,
where where s is the starting bid and n is the minimum bid
increment as deﬁned in Section V.
20

---

## Page 21

Exec(S0, ∆0,S 1, ∆1, [D,ℓ ()])
1 : b∗, p, d0, d1 ← ∅;t∗,t∗
0,t∗
1 ← 0
2 : tend ←$D
3 : do
4 : if FirstBidTime(p) ≤ min(t∗
0,t∗
1, FirstTime(d0), FirstTime(d1)) then
5 : t∗ ← FirstBidTime(p)
6 : b = (ˆt, $b;i) ← PopFirstBid(p)
7 : b∗ ← b∗ ∪ b
8 : d1−i ← d1−i ∪ (ˆt + ∆1−i)
9 : if for i ∈ {0, 1}, FirstTime(di)< FirstBidTime(p) and FirstTime(di) ≤ min(t∗
0,t∗
1, FirstTime(d1−i)) then
10 : t∗ ← PopFirstTime(di)
11 : ( a,σ′
i,t w,i) ←$Si(b∗[t∗ − ∆i],σ i,t∗)
12 : σi ←σ′
i;t∗
i ←tw,i
13 : if a ̸= ⊥ then
14 : p ← p ∪ a
15 : if for i ∈ {0, 1},t∗
i < min(FirstBidTime(p), FirstTime(d0), FirstTime(d1)) and t∗
i ≤t∗
1−i then
16 : t∗ ←t∗
i
17 : ( a,σ′
i,t w,i) ←$Si(b∗[t∗ − ∆i],σ i,t∗)
18 : σi ←σ′
i;t∗
i ←tw,i
19 : p ← p ∪ a
20 : until FirstBidTime(p)>t end
21 : b ← b∗
22 : awin = (twin, $bwin;i) ← MaxBid(b)
23 : alose = (tlose, $blose; 1 −i) ← MaxBid(b1−i)
24 : if i = 0
25 : output ($r0, $r1) = ($1 − $bwin,ℓ ($blose))
26 : else
27 : output ($r0, $r1) = (ℓ($blose), $1 − $bwin)
Fig. 19. Pseudocode for Exec, the execution of a PGA. This procedure maintains a list of pending bids p awaiting transmission. Bids in the pending
list, p, are added to the current bid list, b∗, at their scheduled time, but each player will not see them until after their individual latency, ∆i. For each bid
that is cast by player Pi, a time is added to d1−i that indicates when P1−i will ﬁrst see the bid. Players are awoken to schedule bids at their speciﬁed
wake time, or earlier if they see a bid cast by the other player. For clarity, we deﬁne several functions. FirstBidTime(p) is the time t associated with the
earliest pending transaction. PopFirstBid(p) pops and outputs the earliest transaction; given two transactions with the same time, it picks one uniformly at
random. MaxBid(b) outputs the maximum price bid in b; given multiple bids at the same price, it outputs the ﬁrst in temporal order. FirstTime(di) outputs
the earliest time from a list of times; PopFirstBid(di) pops and outputs the earliest time. Although not speciﬁed here, bids must meet the validity rules –
i.e. must meet the minimum start bid s, minimum raise ι and must be staggered by a minimum time δ.
We can equivalently deﬁne a latest end time for the PGA
tend =V [imax].
where V [i]<t′ <V [i + 1].
Observation 5. Denote byptime(t) the probability that a PGA
has ended by some time t. For proof-of-work blockchains,
ptime(t) = 1 −e−λt.
Proof. Since the block interval in a proof-of-work blockchain
is exponentially distributed, we model the PGA end time as an
exponential distribution with rate parameter λ. The probability
that the auction has ended by some positive time t is given by
the CDF of the exponential distribution: 1 −e−λt.
Observation 6. Assume that miners continuously update their
blocks with the most proﬁtable set of transactions. For players
P0, P1 adhering to the cooperative strategy with parameters
D,W , the probability that Pb will win the PGA is given by
imax∑
i=2k+b
(1 −ptime(V [i])) ×ptime(V [i + 1]),
for k ∈ [0, iend
2 ].
Proof. Notice that probability that a player wins a PGA is
exactly the probability that the PGA terminates during an
interval controlled by that player. This follows since miners
continuously update their blocks with new more proﬁtable
transactions and the player in control of the interval will have
the highest bid during its interval.
We can deﬁne the probability that the game ends during a
given interval as
21

---

## Page 22

pinterval(i) = (1 −ptime(V [i])) ×ptime(V [i + 1]),
and the probability of Pb winning is the summation of
pinterval for all intervals that it controls.
For any interval i<i max, we can now deﬁne the expected
payoff for each player during that interval, conditioned on the
fact that the auction has already reached the interval j ≤i and
has not yet terminated. For each interval, we give two expected
values: one for the “bidder” — i.e., the player whose turn it is
to bid during that interval and one for the “non-bidder”. The
bidder’s expected reward is given by:
Ebidder(i,j ) =pinterval(i −j) × (1 −W [i]).
The non-bidder’s expected reward during a given interval is
given by:
Enon−bidder(i,j ) =pinterval(i −j) × −c.
Now, we deﬁne the expected payoff for each player by
continuing to follow the cooperative strategy at any point in the
game. As in our deﬁnition of the strategy, we assume without
loss of generality that P0 bids ﬁrst and P1 bids second.
Observation 7. During the jth interval, the expected payoff
for Pb to continue to cooperate for the rest of the auction is
given by:
E(Pb)
cooperate(j) =
∑
i=0,∞
Ebidder(2i +j +b,j )+
∑
i=0,∞
Enon−bidder(2i +j + (1 −b),j )+
(1 −ptime(V [iend])) × −c
Proof. This follow directly form the previous observation.
Previously, we deﬁned the expected value of a bidder and a
non-bidder in any interval. If we take an inﬁnite sum of these
expected values, alternating between bidder and non-bidder
corresponding to the intervals in which the respective players
bid, then we will get the expected payoff for the remainder of
the game.
Next, we show the cost of deviation. For the grim-trigger
cooperative strategy, each player knows that if they defect, the
other player will raise the bid to make the game unproﬁtable
– i.e., each player’s payoff will be ℓ($blose.
While intuitively this arrangement (assuming that the other
player will make good on its threat) makes deviation unwise,
deviation may still be proﬁtable if the auction ends before the
other player can respond. This can happen due to the other
player’s latency – i.e., if there is some time delay in which
the deviation goes undetected. Additionally, this can occur due
to the rate limit – i.e., the deviation was detected, but the
other player is not yet able to place a bid to make good on its
threat. For the sake of this analysis, the latency and rate limit
serve identical functions – namely, to delay the other players
response. Thus for simplicity, we deﬁne
delay(Pb) = Max[∆1−b,δ ].
Observation 8. If for all i, it holds that delay(Pb) <W [i +
1] −W [i], then under the assumption that ℓ($blose) = −c, the
expected payoff for P1−b deviating during the ith interval is
given by
E(Pb)
deviate(delay(Pb),i ) =ptime(delay(Pb)) × Max(−c, 1 −W [i + 1])
+ (1 −ptime(delay(Pb)) × −c
.
Proof. Since delay(Pb) <W [i+1] −W [i], then Pb will notice
and be able to react to P1−b’s deviation during the current
(before it issues any other bids). At this point, Pb will react by
bidding 1 +c, making the PGA unproﬁtable for both players.
Thus, P1−b’s expected proﬁt is the expected reward that it
makes during the time before the deviation is noticed, and −c
if the auction does not end during that period, which is given
by the above equation.
Lemma 1. Let Pbidder and Pnon−bidder respectively denote
the player who is and is not bidding during an interval accord-
ing to the cooperative strategy. The grim-trigger cooperative
strategy with parameters D,W will yield a Nash Equilibrium
if ∀j,
E(Pnon−bidder)
cooperate (j) ≥E(Pnon−bidder)
deviate (delay(Pbidder),j).
Proof. In order for a Nash equilibrium to hold for the grim-
trigger cooperative strategy, it must be the case that for all
points in time, it is more proﬁtable to follow the cooperative
agreement than it is to defect.
Notice that deviating is most proﬁtable at the beginning of
one’s interval since deviating later on will yield at most the
same payoff, but conditioned on the game not having ended
previously. Thus, in order for there to be an equilibrium, it
must hold that ∀j, ∀b ∈ {0, 1},
E(Pb)
cooperate(j) ≥E(Pb)
deviate(delay(Pb),j).
Notice that assuming the other player is cooperating, deviating
is only proﬁtable in intervals where one is the non-bidder.
This is clear as when one already has the top bid, bidding
again would decrease their own proﬁt. Thus in order for the
an equilibrium to hold, it must be true that the non-bidder.
APPENDIX E
OO F EES AND OTHER SYSTEM DESIGNS
We now discuss high-level consequences of OO fees in the
context of different types of blockchain systems being built
in academia and industry. The complete enumeration of their
impact is left to future work.
22

---

## Page 23

• Proof-of-stake systems In any proof of stake system
where forks are allowed (e.g. [17] [28] [27]), similar
incentives as for Proof of Work exist for miner to orphan
or rewrite history when proﬁtable OO fees exist. Re-
gardless of whether sealed-bid auctions (cf. Section V-C)
are prominent, the next miner may overtake the previous
block and replay its transactions in her block in an
optimized order. Some stake-based protocols, on the other
hand, attempt to provide a notion of ﬁnality, and feature
clients which will not revert history regardless of evi-
dence presented. For systems in which the ﬁnality notion
refers to a checkpoint that is done to cement multiple
blocks that have already been created (e.g. [12]), all of
the concerns remain the same, because rapid bidding
wars affect the appeal of short-term (in particular, single
block) forks. In blockchains that seek to ﬁnalize every
block (e.g. [24, 31]), the potential of high proﬁt OO fees
implies that the honest (super-)majority assumption of
such systems may not coincide with rational behavior.
• Permissioned blockchain systems Permissioned
blockchains are currently being explored by many
large ﬁnancial institutions, often in use-cases like
exchanges. The importance of transaction order in these
decentralized exchanges poses a variety of interesting
questions for such systems. For example, it is classically
claimed that blockchains add auditability to existing
workﬂows, but it is impossible to audit or objectively
divine the real order in which a block producer received
transactions on an asynchronous network. Furthermore,
because OO fees exist even on permissioned chains
where on-chain assets are being exchanged, block
producers in such chains must be chosen carefully and
trusted with correct operation and ordering.
• Sharded blockchain systems Several sharded blockchain
systems have been explored in both academia (e.g. [29])
and industry (e.g. [10]). One important consequence of
sharding blockchains is the reduced security of each shard
over the security of the whole system. Generally, the
effects of this reduced security are mitigated through ran-
dom sampling from a large pool of potential validators,
so an adversary would require substantial control of the
pool to have a high chance of adversarially controlling
a shard. Unfortunately, as OO fees show, the security
needs of shards may not be homogeneuous; a shard that
operates a large decentralized exchange must pay miners
higher rewards to ensure stability than a shard without
such an exchange by the analysis in [14]. Because few
sharded based systems are running in practice, substantial
future work remains to fully enumerate potential attacks
and their mitigations in sharded systems.
• Other exchange designs In other blockchain-based ex-
change designs, it may still be possible for miners of
the underlying system to manipulate prices, either in real
time or retroactively. This sets up similar incentives as
those explored in this work. One example is for channel
based networks with public watchtowers such as [37];
miners can simply participate in exchanges, collecting
old states through public watchtowers, and can selectively
publish proﬁtable states in a history rewriting attack that
works as above. Thus, it is not necessarily the case that
the abstraction achieved by Layer 2 exchange systems is
sufﬁcient to prevent ordering attacks.
23

---
