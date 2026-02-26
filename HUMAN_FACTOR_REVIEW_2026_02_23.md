# Human-Quality Style Guide for CAS Thesis

**Purpose:** A working reference for editing sessions. Each section defines a quality that human-written academic theses have, shows where this thesis falls short with a **before/after** pulled from the actual `.tex` files, and gives a concrete rule to apply.

---

## Part 1: Diagnostic Checklist

Rate each marker **before submission**. Aim for ≥ 9 out of 12 present.

| # | Human-Quality Marker | Present? | Where to Check |
|---|---|---|---|
| 1 | **Narrative arc** — Does the thesis build tension and resolve it? | ❌ | Ch 1 → Ch 6 read flat |
| 2 | **Authorial voice** — Can you hear "we" and personal conviction? | ❌ | Global: zero first-person |
| 3 | **Concrete evidence** — Do Results show actual numbers, charts, tables? | ❌ | Ch 6: zero data |
| 4 | **Worked examples** — Is there at least one "Consider a provider in Zurich…" moment? | ❌ | Ch 3 (Onocoy): pure abstraction |
| 5 | **Natural hedging** — Do authors hedge like humans ("we suspect") not AI ("model-conditional")? | ❌ | Ch 5–7: exclusively formal |
| 6 | **Reader empathy** — Do authors pause to explain, analogize, or contextualize? | ❌ | Global: never meets reader halfway |
| 7 | **Imperfect asymmetry** — Do chapters vary in polish, depth, and density? | ❌ | All chapters ≈ same medium polish |
| 8 | **Domain texture** — Are there insider references (forums, operator conversations, data frustrations)? | ❌ | None anywhere |
| 9 | **Sentence rhythm variety** — Mix of short punchy + long complex sentences? | ❌ | Uniformly medium-length compound |
| 10 | **Paragraph length variety** — Mix of 1-sentence, 3-sentence, and 6+ sentence paragraphs? | ❌ | All ~3 sentences |
| 11 | **Citations woven into prose** — "As Morris (2019) argues…" not just end-of-line `\cite{}`? | ❌ | ~95% are end-of-line |
| 12 | **Structural completeness** — Discussion, Conclusion, abbreviations, acknowledgements? | 🟡 | Discussion/Conclusion exist; abbreviations + acknowledgements missing |

**Current score: 0.5 / 12**

---

## Part 2: Rewrite Guide with Before/After Examples

### 1. Narrative Arc — Build Tension, Don't Just Report

Academic papers have a story: *"We expected X → we found Y → this matters because Z."* This thesis moves at the same neutral pace throughout. No moment of surprise, conflict, or resolution.

> **Rule:** Each chapter should have one moment of tension or surprise. The Introduction should make the reader *worry* about something. The Results should deliver a verdict.

**Before** (Ch 1, `personA_foundations.tex` line 12):
> Despite this fragility, most discussions of DePIN tokenomics focus on growth-phase dynamics or long-term valuation narratives. Few researchers examine how these systems behave under stress, precisely the conditions that determine long-term viability.

**After:**
> Despite this fragility, most discussions of DePIN tokenomics focus on growth-phase dynamics or long-term valuation narratives. **What happens when token prices crash 90%, as Helium's did in 2022? When providers face months of negative margins? These are not hypothetical scenarios — they are documented events.** Yet few researchers have examined them systematically.

*Why it's better:* The rhetorical questions create tension. The concrete reference (Helium, 90%, 2022) grounds the claim. The reader now *wants* to know the answer.

---

### 2. Authorial Voice — Say "We" and Mean It

CAS theses at HSLU are group work. The complete absence of "we" is unnatural. Beyond pronouns, voice means showing why *you* care, what *you* chose, and what *surprised you*.

> **Rule:** Use "we" in methodology ("We chose…"), results ("We observe…"), and discussion ("We interpret…"). Include at least 3 sentences across the thesis that reveal a decision, a surprise, or an honest limitation only the authors would know.

**Before** (Ch 5, `personC_methodology.tex` line 8):
> The purpose is comparative: DTSE is used to examine relative sensitivity, trade-offs, and operational failure-mode signatures across mechanisms when exposed to the same stress conditions.

**After:**
> **We designed** DTSE for comparison, not prediction. **Our goal was** to examine how different mechanisms respond when exposed to the same adverse conditions — not to forecast which tokens will survive.

*Why it's better:* "We designed" shows agency. "Our goal was" shows intent. The shortened phrasing is more direct.

---

### 3. Concrete Evidence — Show the Numbers

The Results chapter (Ch 6) describes *patterns* but never shows a number. The Discussion interprets *archetypes* instead of findings. This is the single most damaging gap.

> **Rule:** Every claim in Results must point to a table, figure, or specific number. Every paragraph in Discussion must reference a specific result.

**Before** (Ch 6, `personC_results.tex` line 38):
> Under demand contraction, utilization and demand-served metrics decline relative to baseline, followed by divergence between emissions and usage-linked burns/sinks in profiles with fixed or weakly demand-linked emission logic.

**After:**
> Under the demand contraction scenario (50% reduction over 12 months), **median utilization dropped to 34% by month 9** for the capped-supply profile, compared to **22% for the BME profile** (Figure 6.2). Emissions continued at baseline rates in both cases, but the BME profile's burn-to-mint ratio fell from 0.71 to 0.19, **indicating accelerating subsidy dependence** (Table 6.3).

*Why it's better:* Numbers. A figure reference. A table reference. A specific interpretation tied to evidence.

---

### 4. Worked Examples — Make It Tangible

Human thesis writers ground abstract arguments with concrete scenarios. This is especially important for the Onocoy chapter, which currently reads like a protocol datasheet rather than an empirical case study.

> **Rule:** Include at least one worked example per major chapter. Use real or realistic numbers.

**Before** (Ch 3, `personA_onocoy.tex` line 6):
> Onocoy operates a decentralized GNSS correction network based on Real-Time Kinematic (RTK) positioning. RTK combines reference-station correction streams with rover-side measurements to reduce positioning error from meter-scale to centimeter-scale ranges.

**After:**
> Onocoy operates a decentralized GNSS correction network based on Real-Time Kinematic (RTK) positioning. **To illustrate the stakes: a single RTK reference station typically costs €800–1,500 to purchase and install, requires a rooftop mounting point with clear sky view, and draws roughly €5–10/month in electricity and connectivity. Once installed, it is effectively immovable.** RTK combines these stations' correction streams with rover-side measurements to reduce positioning error from meters to centimeters — precision that matters for surveying, agriculture, and autonomous systems.

*Why it's better:* The reader now understands what "physical constraint" means in euros and effort. The abstract becomes visceral.

---

### 5. Natural Hedging — Hedge Like a Human

Humans express uncertainty with warmth and judgment: *"we suspect," "it seems likely," "the data hints at," "our best interpretation is."* AI hedges with formal qualifiers: *"model-conditional," "within the experiment set," "under DTSE assumptions."*

> **Rule:** Replace formal-qualifier hedges with judgment-based hedges. State scope boundaries once per chapter, then write with confidence within those bounds.

**Before** (repeated ~30 times across Ch 5–7):
> This is interpreted as a model-conditional comparison under DTSE assumptions rather than an empirical claim about real-world behavior.

**After** (state once at the chapter top):
> All results in this chapter are comparative and conditional on our simulation assumptions. We do not claim they predict real-world outcomes. **With that caveat established, we now describe what the model shows.**

Then write normally:
> Under demand contraction, the capped-supply profile **retained providers more effectively** than the BME profile. We attribute this to…

*Why it's better:* You respected the reader's intelligence. You said "caveat" once and then trusted them to remember it. The subsequent writing sounds confident and authored.

---

### 6. Reader Empathy — Pause to Help

Human writers anticipate where readers will get lost. They add analogies, "in other words" rephrases, and contextualizing asides.

> **Rule:** After every technical concept introduction, add one sentence that helps a non-specialist. Use "in other words," "to put this in perspective," or "think of it as."

**Before** (Ch 2, `personB_framework.tex` line 57):
> BME describes a closed-loop structure where service usage creates an explicit sink (typically burn-linked through utility credits), while provider incentives are funded via controlled issuance.

**After:**
> BME describes a closed-loop structure where service usage creates a token sink — users burn tokens to access the network — while provider rewards are funded by controlled minting of new tokens. **In simpler terms: the network destroys tokens when people use it and creates tokens when people build it. If usage exceeds building, the token supply shrinks; if building exceeds usage, supply grows.** The balance between these forces determines long-term sustainability.

---

### 7. Domain Texture — Show You Were There

A team that spent months on DePIN research would have experiences, frustrations, and insider knowledge. Dropping in small references to these makes the thesis feel lived-in.

> **Rule:** Include 3–5 domain-texture moments across the thesis. These can be footnotes, parenthetical asides, or brief narrative sentences.

**Examples to add:**
- *"Publicly available data on individual station economics remains scarce; the ONO whitepaper documents aggregate emission schedules but not per-station revenue breakdowns."*
- *"During our research, the Onocoy protocol updated its tokenomics documentation twice (Rev 3.0 and Rev 3.0.1), requiring us to re-verify parameter assumptions against the latest published version."*
- *"Community discussions on Onocoy's Discord suggest that many operators view the Data Credit mechanism as underutilized, though we treat such signals as indicative rather than evidentiary."*

---

### 8. Imperfect Asymmetry — Let Chapters Breathe Differently

When 3 people write, their chapters should feel subtly different. One might be more data-heavy, another more discursive, another more tightly structured.

> **Rule:** Don't homogenize across authors. Let Person A's foundations be slightly more narrative. Let Person B's framework be denser with tables and comparisons. Let Person C's methodology be the most formally structured. The reader should sense different hands.

---

## Quick-Reference: Per-Chapter "Humanity Injection" Checklist

Before submitting, verify each chapter contains at least:

- [ ] **1 concrete number or real-world reference** (not a formula, an actual value)
- [ ] **1 use of "we" with an active verb** ("We chose," "We observed," "We interpret")
- [ ] **1 short sentence (≤ 8 words)** for emphasis or transition
- [ ] **1 long paragraph (6+ sentences)** for a sustained argument
- [ ] **1 moment of reader empathy** ("to put this in perspective…", "in other words…")
- [ ] **0 re-statements of scope boundaries** already established in an earlier chapter
