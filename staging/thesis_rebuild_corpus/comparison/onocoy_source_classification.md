## Onocoy Source Classification

Status: synthesis control document  
Date captured: 2026-03-01  
Mode: `MODE: SYNTHESIS`

### Purpose

This memo defines the evidence hierarchy for Onocoy-related material used in V2.

It exists to stop Chapter 4 and later DTSE mapping work from blurring:
- public mechanism facts,
- dated dashboard evidence,
- bounded interview context,
- and internal synthesis artifacts.

### Layer 1: Primary / Thesis-Safe by Default

Use these for load-bearing mechanism claims when the wording matches the underlying source.

Sources:
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/sections/personA_onocoy.tex`
- official Onocoy public documentation / whitepaper referenced there
- official Tokenomics docs page: [Tokenomics](https://docs.onocoy.com/documentation/tokenomics)
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/dune/notes/onocoy_dune_qa_mapping_2026-02-26.md`
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/dune/results/onocoy_dashboard_snapshot_metrics_2026-02-25.csv`

Safe claim types:
- RTK / GNSS function
- distributed reference-station model
- provider role and quality-sensitive obligations
- ONO + Data Credits dual-layer structure
- ONO cap, 16% annual reduction, and documented token-flow logic around Data Credits, burns, and conditional buyback routing
- capped-supply / decay-path claims where explicitly documented
- dated dashboard facts such as:
  - holders
  - circulating supply
  - total buybacks
  - total burned
  - validated / online stations

### Layer 2: Strong Reservoir / Explanatory Support

Use for chapter shaping, clearer explanation, and bounded interpretation.

Source:
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/incoming/PersonA_DePIN Tokenomics Under Stress_FINAL.docx`

Best use:
- clearer RTK explanation
- user structure
- provider requirements
- industrial-demand framing
- explanatory transitions for why Onocoy is analytically useful

Rule:
- may improve prose and structure
- must not override stronger primary evidence when the two differ

### Layer 3: Bounded Interview / Context Support

Use for gap detection, calibration hints, and evidence-boundary decisions.

Source:
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/staging/thesis_rebuild_corpus/incoming/PersonA_OnocoyinterviewQ&A_Final.docx`

Useful for:
- identifying which questions public docs do not settle clearly
- identifying Dune verification targets
- bounded context on:
  - demand concentration
  - provider payback expectations
  - governance flexibility
  - buyback intuitions

Rule:
- interview answers are not mechanism facts by default
- they may inform modeling bounds or contextual caveats
- they should not become load-bearing thesis claims without stronger support

### Public Ecosystem Context (Bounded, But Separate from Interview Evidence)

Use for explaining how the ecosystem appears to support participants without turning that support layer into a formal mechanism rule.

Sources:
- public Explorer documentation
- public Ambassador / community documentation

Useful for:
- operational visibility via coverage maps and station-level explorer data
- ecosystem support and communication channels around participants

Rule:
- Explorer is treated as an operational / spatial transparency layer
- community or ambassador material is treated as ecosystem context
- neither should silently replace protocol rules, governance rules, or interview evidence

### Layer 4: Internal Synthesis Only

Use for thinking and source routing only.

Sources:
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/md/Onocoy_Intelligence_Dossier.md`
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/working_memory/ONOCOY_QA_LATEST_2026-02-25.md`
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/working_memory/ONOCOY_CONSOLIDATED_INTELLIGENCE_PART2.md`
- `/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics/output/working_memory/ONOCOY_CONSOLIDATED_INTELLIGENCE_PART3.md`

Rule:
- useful for synthesis, gap detection, and chapter design
- not admissible as thesis evidence anchors by default
- must never appear in the thesis PDF unless explicitly approved for a special reason

### Dune-Specific Rule

Dune evidence is useful but bounded:

- treat snapshot metrics as **dated evidence**
- do not infer trends from one snapshot alone
- prefer time-series query outputs where trend language is needed

This means:
- `holder count`, `price`, `market cap`, `FDV`, `buybacks`, `burned`, and `miner counts` can be used descriptively if date-stamped
- they should not be written as if they prove long-run mechanism success or failure

### Explorer vs Dune vs Interview vs Community

- `Tokenomics docs` = primary source for ONO, Data Credits, supply cap, annual reduction, and token-flow logic
- `Explorer` = operational and spatial transparency layer
- `Dune` = on-chain and accounting transparency layer
- `Interview` = bounded practitioner context
- `Community / ambassador material` = ecosystem context

These roles are distinct and should remain distinct in Chapter 4 and later chapters.

### Promoted Now vs Parked

#### Promoted now into claim control

These items are strong enough, central enough, and likely reusable enough that they should not remain only as Chapter 4 prose:

- ONO capped at `810M`
- `16%` annual reduction in newly distributed ONO
- Data Credits as non-transferable, fiat-priced units burned on use
- documented token-flow logic in which fiat revenue finances operations and may be used for ONO buybacks, with bought-back ONO split across reward, ecosystem, and burn paths
- the distinction between Explorer and Dune as different transparency layers with different evidentiary roles

Reason:
- these facts are likely to be reused in later mechanism discussion, methodological framing, or model-facing reasoning
- they therefore need explicit claim-ledger coverage rather than remaining only as descriptive chapter prose

#### Parked for later unless later chapters truly need them

- hardware cost ranges
- payback period / payback ratio
- client concentration / client counts
- informal governance-response comments
- stronger hardware-agnostic wording
- strong transparency superlatives

Reason:
- these are mostly interview- or context-driven
- they may still be useful in appendix, bounded discussion, or later methodological caveats
- they should not be promoted into load-bearing thesis facts unless stronger public support or clear later need emerges

### Typical Onocoy Claim Routing

#### Safe with primary support

- Onocoy is an RTK / GNSS correction network.
- Onocoy uses ONO plus Data Credits.
- Public docs describe a capped supply with a 16% annual reduction / decay path.
- GNSS station quality and uptime matter to participation and output quality.

#### Safe only as bounded interpretation

- dual-layer design reduces direct user-price exposure while shifting pressure elsewhere
- settlement-layer choice should be read as a time-bounded design decision, not universal superiority

#### Interview / context only unless cross-supported

- number of major clients
- provider payback period
- exact buyback ratios described informally
- “no plan yet” governance-response comments
- beliefs about what matters most for sustainability

### Governing Rule for Chapter 4

When in doubt:
- mechanism facts come from public docs or auditable dated evidence,
- context can clarify,
- interview material can bound,
- internal synthesis can guide,
- but none of those lower layers may silently upgrade into thesis fact.
