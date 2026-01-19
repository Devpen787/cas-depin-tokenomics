# Human Style Audit Report (AI-Neutralization)
## Scan Date: 2026-01-19

---

## Summary

| Category | Count | Severity |
|---|---|---|
| **D1: Em-Dash Abuse** (`---`) | 9 | 🔴 High |
| **C1: Passive Voice** (`is treated`, `is designed`) | 13 | 🟡 Medium |
| **D6: Template Phrases / Parallelism** (`First... Second... Third...`) | 14 | 🟡 Medium |
| **B2: Defensive Hedging** (`aims to`, `intends to`) | 2 | 🟢 Low |

**Overall Risk:** 🟡 **Medium** — The document has significant em-dash and passive voice markers that could trigger AI detection, but defensive hedging is minimal.

---

## 1. Em-Dash Abuse (D1) — 9 Instances

Em-dashes used as "logic glue" are a strong LLM signature.

| File | Line | Current Text | Suggested Fix |
|---|---|---|---|
| `personC_methodology.tex` | 69 | `Key parameters---such as cost ranges...---are varied` | Use commas: `Key parameters, such as cost ranges, are varied` |
| `personC_methodology.tex` | 144 | `scenario-specific behaviors---such as saturation...---are treated` | Use parentheses or commas |
| `personC_results.tex` | 774-775 | `leading indicators of stress---such as declining...---rather than` | Rewrite as two sentences or use commas |
| `personC_results.tex` | 1041-1042 | `perspective---mechanisms, metrics, and decision patterns---allows` | Use parentheses |
| `personC_results.tex` | 1090 | `intervene---often under time pressure` | Use comma: `intervene, often under time pressure` |
| `personC_results.tex` | 1155 | `design choices---such as emission decay...---interact` | Use commas |
| `personA_foundations.tex` | 12 | `under stress---precisely the conditions` | Use comma |

**Action:** Global find/replace `---` with `, ` or split sentences.

---

## 2. Passive Voice (C1) — 13 Instances

Passive constructions hide agency and sound template-like.

| File | Line | Current Text | Suggested Fix |
|---|---|---|---|
| `personC_methodology.tex` | 19 | `The scope is defined by...` | `We define the scope by...` |
| `personC_methodology.tex` | 23 | `demand is treated as an exogenous input` | `We treat demand as an exogenous input` |
| `personC_methodology.tex` | 36 | `practitioner input is used` | `We incorporate practitioner input` |
| `personC_methodology.tex` | 63 | `Reproducibility is treated as a core requirement` | `We treat reproducibility as a core requirement` |
| `personC_methodology.tex` | 72 | `the simulation framework is designed to support` | `We designed the simulation framework to support` |
| `personC_methodology.tex` | 86 | `stress is defined operationally` | `We define stress operationally` |
| `personC_methodology.tex` | 190 | `volatility is treated as a stress signal` | `We treat volatility as a stress signal` |
| `personC_methodology.tex` | 196 | `is defined operationally as` | `We define X operationally as` |
| `personC_results.tex` | 71 | `comparison is intended` | `we intend comparison` |
| `personC_results.tex` | 1161 | `the analysis is designed for` | `We designed the analysis for` |
| `personA_foundations.tex` | 24 | `ONO is treated as a representative...` | `We treat ONO as a representative...` |

**Action:** Ctrl+F for `is treated`, `is defined`, `is designed`. Rewrite with active voice.

---

## 3. Template Phrases & Artificial Parallelism (D6) — 14 Instances

Ordinal lists ("First... Second... Third...") and boilerplate phrases are LLM signatures.

| File | Line | Current Text | Suggested Fix |
|---|---|---|---|
| `personC_methodology.tex` | 74 | `First, demand is modeled... Second, providers are represented...` | Break into prose: "Demand is modeled as... Providers, meanwhile, are..." |
| `personC_methodology.tex` | 76 | `Third, the price formation mechanism... Fourth, the temporal resolution...` | Combine into one paragraph without ordinals |
| `personC_methodology.tex` | 157 | `Metric selection in this thesis follows three principles.` | Simplify: "We follow three principles:" |
| `personC_methodology.tex` | 159 | `First, metrics must be comparative... Second... Third...` | Use bullets or natural prose |
| `personC_results.tex` | 926-947 | `First, this work provides... Second, the stress-testing approach... Third, the framework...` | Rewrite without ordinals |
| `personA_foundations.tex` | 22 | `First, the thesis does not... Second, it does not... Finally, it does not...` | "The thesis avoids forecasting... It also avoids..." |
| `personA_foundations.tex` | 27 | `This thesis makes three contributions. First... We then apply... Finally...` | Simpler: "This thesis contributes a simulation approach..., applies it to Onocoy, and emphasizes..." |

**Action:** Rewrite ordinal lists as flowing prose.

---

## 4. Defensive Hedging (B2) — 2 Instances

Over-hedging is an LLM strategy to appear "careful." This thesis has minimal hedging, which is good.

| File | Line | Current Text | Suggested Fix |
|---|---|---|---|
| `personC_results.tex` | 998 | `the work aims to contribute responsibly` | `the work contributes responsibly` |
| `personC_results.tex` | 1049 | `it aims to improve decision quality` | `it improves decision quality` |

**Action:** Replace `aims to X` with `X`.

---

## Recommended Priority Actions

1.  **[HIGH] Em-Dash Cleanup:** Find/replace `---` → `,` or restructure sentences.
2.  **[MEDIUM] De-Passive Voice:** Find `is treated`, `is defined`, `is designed` → Rewrite with "We".
3.  **[MEDIUM] Break Ordinal Lists:** Rewrite "First/Second/Third" blocks as natural prose.
4.  **[LOW] Remove Hedging:** Replace "aims to X" with direct "X".
