## V2 Section Quality Gate

Status: synthesis control checklist  
Date captured: 2026-02-28  
Mode: `MODE: SYNTHESIS`

### Purpose

This file is the operational gate used to judge whether a drafted V2 section is ready, needs revision, or should be rewritten from scratch.

Use it after drafting and before the section is treated as stable enough for integration into the V2 LaTeX surface.

### Decision Outcomes

Use one verdict only:

1. `ACCEPT`
2. `REVISE`
3. `REWRITE FROM SCRATCH`

### Gate Criteria

#### 1. Reader Pull

Check:

- Does the section create momentum?
- Does the opening make the reader want to continue?
- Does the text feel motivated rather than merely organized?

Fail signals:

- dry setup before the problem lands
- compliance language too early
- structure visible before meaning

Quick examples:

- `strong`: the problem or tension becomes clear immediately
- `weak`: the section explains itself before the reader cares

#### 2. Concrete Grounding

Check:

- Does the section give the reader at least one concrete grip where needed?
- Is there a real-world consequence, operational image, or example before abstraction?

Fail signals:

- abstraction piled on abstraction
- terms defined but not felt
- no operational consequence attached to the concept

Quick examples:

- `strong`: one concrete consequence, example, or image anchors the section
- `weak`: the section stays conceptual all the way through

#### 3. Sentence Variation

Check:

- Is sentence rhythm varied?
- Do paragraphs avoid repetitive openings?
- Does the prose avoid uniform, AI-clean pacing?

Fail signals:

- repeated stems like `This thesis`, `The thesis`, `This section`
- every sentence carrying the same length and cadence
- too many sequential explanation templates

Quick examples:

- `strong`: sentence rhythm changes naturally
- `weak`: every paragraph opens and moves the same way

#### 4. Claim Discipline

Check:

- Does each paragraph stay within its claim class?
- Are mechanism facts, modeled assumptions, empirical observations, and DTSE outputs kept distinct?
- Is the chapter contract respected?

Fail signals:

- simulation language mixed with empirical fact
- scope bleed across chapters
- unsupported claims smuggled in through context prose

Quick examples:

- `strong`: each paragraph stays within its evidence role
- `weak`: the section sounds precise but quietly mixes claim classes

#### 5. Non-Mechanical Tone

Check:

- Does the section sound authored?
- Does it feel written for a reader rather than assembled for compliance?

Fail signals:

- over-symmetrical subsection design
- repeated `Definition / Explanation / Limitation` cadence throughout
- prose that is correct but lifeless
- wording that sounds auto-completed rather than chosen

Quick examples:

- `strong`: the section sounds authored
- `weak`: it sounds like a thesis machine

#### 6. Over-Compression Check

Check:

- Does each paragraph do only one rhetorical job?
- Are contributions, caveats, transitions, and definitions separated where needed?

Fail signals:

- one paragraph doing too much
- no breathing room for complex ideas
- dense but unmemorable prose

Quick examples:

- `strong`: hard ideas are split into readable moves
- `weak`: one paragraph is carrying the whole section

#### 7. Early Compliance Language Check

Check:

- Does the section delay formal contracts and disclaimers until the reader is oriented?

Fail signals:

- scope statements too early
- methodological caveats before motivation
- interpretive contract language arriving before the core idea lands

Quick examples:

- `strong`: formal boundaries appear after reader orientation
- `weak`: disclaimers arrive before the point lands

#### 8. Question-Lead-In Check

Check:

- Before a research question, contribution frame, or other major analytical turn appears, does the reader understand why it is being introduced in that form?
- Does the section earn the question, or does it simply drop it in?

Fail signals:

- subsection heading followed immediately by a major question with no rationale
- the reader sees the question before understanding why it is the right question
- contribution language appears before the analytical setup has narrowed the problem

Quick examples:

- `strong`: the question feels like the natural next move in the argument
- `weak`: the section announces the question before the reader understands why it appears there

#### 9. Form-Fit Check

Check:

- Is the current form the best one for comprehension?
- Would the material teach better as prose, split prose, lead-in plus list, or a short numbered list?
- Is the section choosing the clearest form, or just the neatest one?

Fail signals:

- a dense paragraph that is difficult to scan
- a list inserted only because there are multiple items
- prose converted into bureaucratic mini-headings rather than clearer explanation

Quick examples:

- `strong`: the chosen form helps the reader understand faster
- `weak`: the form looks tidy but makes the prose feel schematic or harder to absorb

#### 10. Judgment and Uncertainty Check

Check:

- Does the section preserve visible authorial judgment without sounding opinionated?
- Is uncertainty calibrated clearly where the evidence is limited?
- Does the prose avoid generic “balanced” phrasing that sounds polished but says little?

Fail signals:

- every claim sounds equally weighted regardless of evidence quality
- uncertainty is either hidden or overstated
- the prose sounds careful but noncommittal in a generic way

Quick examples:

- `strong`: the section sounds selective, bounded, and intellectually responsible
- `weak`: the prose sounds smooth but empty, or over-balanced in a way that hides judgment

#### 11. Repetition and Plainness Check

Check:

- Has the section preserved useful repetition of key terms where repetition improves clarity?
- Has the revision kept plain wording where plain wording is more accurate than polished paraphrase?
- Does paragraph movement follow the thought rather than a stylistic template?

Fail signals:

- key terms are replaced with weaker synonyms only to avoid repetition
- important sentences are polished into vagueness
- paragraph progression feels templated rather than thought-driven

Quick examples:

- `strong`: repetition is used selectively and plain wording sharpens meaning
- `weak`: variation is forced and clarity gets weaker

### Quick Scoring Method

Rate each category:

- `strong`
- `acceptable`
- `weak`

Decision rule:

- `ACCEPT`: no `weak` scores
- `REVISE`: one or two `weak` scores
- `REWRITE FROM SCRATCH`: three or more `weak` scores, or clear failure in reader pull plus non-mechanical tone

### Mandatory Failure Reason

Every verdict below `ACCEPT` must name at least one explicit failure reason:

1. reader feels processed, not pulled
2. no concrete grip before abstraction
3. repeated mechanical sentence stems
4. paragraph over-compression
5. compliance language arrives too early
6. claim classes are mixed
7. section sounds assembled rather than written
8. question arrives before it is earned
9. format is neat but not teachable
10. wording sounds auto-completed rather than chosen
11. uncertainty is generic rather than calibrated
12. variation was forced and clarity got weaker

### Mandatory Red Flags

If any of the following is true, the section cannot be accepted:

1. it sounds like a thesis machine rather than a person
2. the reader experiences structure faster than meaning
3. the section is academically correct but unpleasant to read
4. the main idea does not land before the caveats arrive
5. the section introduces a question or contribution frame before the reader understands why it belongs there
6. the prose sounds polished but non-selective, as if no real judgment is being exercised

### Reviewer Prompt

When reviewing a section, ask:

1. What is the section trying to make me understand?
2. At what point did that become clear?
3. Did I feel pulled through the section, or processed by it?
4. Which paragraph first sounded mechanical?
5. Which paragraph was doing too much?
6. If this were submitted unchanged, would it read intentional or merely disciplined?
7. Did the section earn its major analytical turn before introducing it?
8. Is the current form helping comprehension, or just organizing content neatly?
9. Does the prose sound chosen rather than auto-completed?
10. Did the revision preserve useful repetition and calibrated uncertainty, or smooth them away?

### Review Output Template

When applying this gate, record:

1. `Verdict`: `ACCEPT`, `REVISE`, or `REWRITE FROM SCRATCH`
2. `Weak categories`: list only the weak ones
3. `Failure reason`: choose at least one from the mandatory failure reasons above
4. `Keep`: what should survive
5. `Rewrite focus`: what must change first

### Final Rule

Do not accept a section because it is safe.

Accept it only if it is both safe and alive on the page.
