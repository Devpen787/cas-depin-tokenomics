# Corpus Master Index

This index tracks rebuild-corpus batches, normalized artifacts, and consolidation status. It is the durable map for repeats, later versions, and cross-links across incoming material.

## Batch Register

| Batch | Date | Source Mode | Normalized File | Status | Notes |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 001 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_001.md` | normalized | mixed conceptual, Onocoy, and DTSE material split into five normalized artifacts |
| 002 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_002.md` | normalized | split into six artifacts with strong overlap against batch 001; several formulations preferred as cleaner canonical notes |
| 003 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_003.md` | normalized | methodology-heavy batch split into ten artifacts covering limitations, extensions, governance, and verification |
| 004 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_004.md` | normalized | mixed methodology and Onocoy batch with strong implementation detail; includes flagged incomplete subtopics |
| 005 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_005.md` | normalized | first major architecture-level rebuild proposal; includes repo-checked visual inventory and Golden Thread conflict warning |
| 006 | 2026-02-28 | user-pasted thread input | `normalized/intake_batch_006.md` | normalized | high-value narrative integration batch; strong for flow and framing, not thesis-safe as written |
| 007 | 2026-02-28 | user-uploaded file drop | `normalized/intake_batch_007_file_drop.md` | normalized | first file-based corpus batch; includes a canonical markdown chapter draft, a docx sibling, and three visual assets |

## Normalized Artifact Register

| Artifact ID | Batch | Working Label | Thesis Role | Canonical Use | Current Risks |
| :-- | :-- | :-- | :-- | :-- | :-- |
| B001-A | 001 | DePIN tokenomics primer | foundations/framework concept base | use as source for physical-hardware constraint and baseline DePIN framing | citation closure required; overlaps with B001-D |
| B001-B | 001 | BME solvency explainer | mechanism definition | use as concise BME explanation | citation closure required; avoid repeating in multiple chapters |
| B001-C | 001 | Onocoy dual-layer explainer | case-study mechanism note | use as canonical Onocoy mechanism source from this batch | must align with official Onocoy documentation |
| B001-D | 001 | Rebuild narrative blueprint | thesis architecture and transition logic | use for chapter ordering and narrative reconstruction, not direct prose import | mixes claim classes and duplicates earlier content |
| B001-E | 001 | DTSE diagnostic notes | methodology/results diagnostic source | use for Stage 1/2 language, failure-signature naming, and model-scope statements | empirical/model boundaries must stay explicit |
| B002-A | 002 | Sunk-cost stickiness explainer | foundations path-dependence note | use as preferred wording for retention buffer and asymmetric recovery | Helium example requires evidence; overlaps with B001-A |
| B002-B | 002 | ONO empirical-anchor explainer | methodology mapping note | use as preferred ONO-anchor explanation and assumption-boundary source | protocol-fact versus model-assumption boundary must stay explicit |
| B002-C | 002 | BME vs capped-supply comparison | comparative mechanism note | use as preferred tradeoff framing for inflationary tail risk versus subsidy flexibility | citation closure required; ideal-type simplification risk |
| B002-D | 002 | Human intervention archetypes | governance interpretation note | use selectively in discussion as DTSE interpretive taxonomy | not yet externally grounded as empirical classification |
| B002-E | 002 | BMR below parity explainer | mechanism solvency note | use as compact burn-to-mint parity summary | overlaps with B001-B; proxy-overreach risk |
| B002-F | 002 | DTSE framework explainer | methodology architecture summary | use as preferred DTSE architecture and reproducibility summary | keep distinct from empirical results claims |
| B003-A | 003 | DTSE advantages and limitations | framework appraisal note | use as preferred strengths/limitations summary and interpretive-boundary anchor | keep contribution-forward; avoid overemphasizing limitations |
| B003-B | 003 | Structural vs reducible limitations | interpretive boundary note | use to distinguish necessary abstractions from future refinements | should support, not dilute, the current methodology |
| B003-C | 003 | Refinement roadmap | future research note | use as roadmap source for future work only | not thesis-ready prose; overlaps with multiple extension notes |
| B003-D | 003 | Endogenous demand and market behavior | model extension note | use for future extension design only | overlaps with B003-G/B003-J; forecasting-drift risk |
| B003-E | 003 | Formalizing governance interventions | governance extension note | use for counterfactual intervention formalization and boundary language | future-work only unless explicitly parameterized |
| B003-F | 003 | Provider behavior and verification enhancements | extension note | use as secondary support for richer provider/verification extensions | subordinate to B003-H for verification taxonomy |
| B003-G | 003 | Endogenous demand effects on DTSE results | interpretation note | use for explaining how extensions would change result interpretation | speculative if stated too strongly |
| B003-H | 003 | Physical verification frictions | friction taxonomy note | use as preferred verification-friction taxonomy and DePIN context source | network-specific claims require protocol evidence |
| B003-I | 003 | Governance-response latency | governance timing note | use for delayed-intervention modeling boundaries | modeled-assumption boundary must stay explicit |
| B003-J | 003 | Why DTSE cannot track organic demand yet | scope clarification note | use as preferred current-scope statement on exogenous demand | must stay clearly framed as intentional scope, not omission by mistake |
| B004-A | 004 | Investor profiles and price-signal scope | scope clarification note | use as preferred note that the price signal excludes investor-profile heterogeneity | keep separate from endogenous-demand discussion |
| B004-B | 004 | Physical data quality to reward pipeline | verification pipeline note | use as preferred stepwise explanation linking physical quality to reward eligibility | protocol-specific claims require support |
| B004-C | 004 | Stronger real-world demand modeling | extension note | use only as support for endogenous-demand future-work cluster | highly duplicative with batch 003 |
| B004-D | 004 | Governance-response latency steps | extension recipe note | use as implementation-oriented latency-modeling note | future-work only unless explicitly parameterized |
| B004-E | 004 | Calibration with historical data | calibration strategy note | use as preferred calibration-with-history note | empirical anchors still required |
| B004-F | 004 | Data Credits and user-side price stability | mechanism-modeling note | use as preferred Data Credit price-stability explanation | must stay distinct from provider-side solvency claims |
| B004-G | 004 | Liquidity-shock first-moving metrics | stress-signature note | use for diagnostic framing and results interpretation when tied to frozen outputs | exact-timing overclaim risk |
| B004-H | 004 | Reward bonus programs and retention | governance interpretation note | use for targeted-retention discussion and intervention mapping | policy-layer evidence required for Onocoy-specific claims |
| B004-I | 004 | Provider class heterogeneity | parameter-mapping note | use for provider-class abstraction and results interpretation | includes unresolved subtopics; do not overstate |
| B004-J | 004 | Onocoy annual deflation factor | mechanism note | use only after verifying the release-path description against official documentation | verification pending |
| B004-K | 004 | Sunk-cost moat implementation | method-implementation note | use as preferred implementation description of retention-buffer logic | tie claims to parameter definitions carefully |
| B004-L | 004 | Endogenous-demand consequences | implications note | use only as support for future-work interpretation | duplicative and speculative if overstated |
| B005-A | 005 | Governance-response latency recap | future-work note | use only as supporting restatement in the governance-latency cluster | heavily duplicative of prior batches |
| B005-B | 005 | Onocoy decay and long-run provider economics | mechanism interpretation note | use as preferred long-run provider-economics framing for ONO decay, subject to verification | protocol verification required |
| B005-C | 005 | Data Credit buyback-and-burn routing | mechanism note | use as preferred routing-focused Onocoy explanation | protocol verification required; keep distinct from BME equivalence claims |
| B005-D | 005 | Outcome-based rewards differentiation | verification-design note | use as preferred action-based versus outcome-based reward explanation | taxonomy/protocol support required |
| B005-E | 005 | Missing-question inventory | planning audit note | use as rebuild checklist and completeness audit | not thesis prose |
| B005-F | 005 | Full thesis restructure / replacement TOC | architecture blueprint note | use as rebuild architecture proposal only after reconciliation with THESIS_OS | Golden Thread conflict risk |
| B005-G | 005 | Charts and tables inventory + redesign plan | visual planning note | use as visual-asset planning source for rebuild | partly proposed, not fully canonical |
| B006-A | 006 | Analytical stress report | integrative summary note | use as high-value narrative integration source across chapters | mixed claim classes; not thesis-ready prose |
| B006-B | 006 | Economic gravity of hardware primer | narrative primer note | use as preferred flow/framing source for foundations rebuild | rhetorical voice and verification cleanup required |
| B006-C | 006 | Three-function robustness lens | synthesis note | use as preferred robustness framing if introduced in rebuild | internal synthesis; not externally cited framework |
| B006-D | 006 | Failure-signature checklist and governance bridge | synthesis note | use for readable failure-signature-to-governance interpretation | tie back to formal DTSE vocabulary carefully |
| B007-A | 007 | Comparative tokenomics chapter draft | markdown chapter draft | use as preferred canonical text source from the first file drop | time-sensitive market data; citation-risk sweep required |
| B007-B | 007 | Comparative tokenomics chapter draft variant | docx formatted draft | use only as layout-preserving sibling of B007-A | likely near-duplicate; version drift unverified |
| B007-C | 007 | Onocoy stress analysis slide deck | slide-deck PDF | use as visual framing and chart-design support | not primary text evidence without visual review |
| B007-D | 007 | DTSE thesis mindmap | planning visual | use for architecture/planning support only | semantic content not yet extracted; original filename uses DSTE |
| B007-E | 007 | DePIN under pressure failure-signatures visual | concept graphic | use for stress/failure-signature visual planning | semantic content not yet extracted |

## Cross-Link Rules

1. Preserve originals in `incoming/` when file-based inputs arrive.
2. Record deduplication as one of: exact duplicate, near duplicate, superseded, complementary variant, unresolved conflict.
3. Prefer one canonical source per mechanism or narrative function, with cross-links rather than repeated summaries.
4. Do not treat normalized intake files as thesis-ready prose.
5. When later batches offer cleaner formulations of existing ideas, prefer the cleaner canonical note but preserve the earlier batch as provenance.
6. Keep future-extension material subordinate to current-thesis contribution unless the rebuild explicitly expands DTSE scope.
7. Flag incomplete or embedded prompt fragments explicitly so they are not mistaken for validated corpus content.
8. When a batch proposes a new thesis architecture, check it against `THESIS_OS.md` before treating it as admissible rebuild structure.
9. Distinguish high-value narrative sources from thesis-safe prose; preserve flow insights without importing rhetorical or unsupported wording.
10. For file-based drops, preserve originals in `incoming/` and treat normalized aliases as working copies only.
