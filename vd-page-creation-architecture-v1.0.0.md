# The Page Creation Architecture: Content Creation Guide (v1.0.0-min)

**Derivative of:** vd-page-creation-architecture-v1.0.0.md. Source is canonical.

---

## Purpose
Production counterpart to the Entity & Pillar Audit Guide. Defines how to build pages that pass EAS standards before publication. Owns: title tag logic, H1, opening 150 words, body structure, page-type standards, content briefs, EAS scoring, pre-publish checklist.

Detailed rules for brand, language, fact-checking, keyword auditing, and AI extractability live in dedicated modules. Reference. Do not duplicate.

---

## Required Reference Modules
```
Page Creation Architecture | Pillar Architecture | vd-brand-positioning | vd-language-control-standards
vd-tone-and-style | vd-ai-extractability | vd-keyword-type-map
vd-keyword-audit | vd-fact-checking
```

---

## Authority and Safety Boundary
Page Creation Architecture and Pillar Architecture define structure and strategy. They do NOT override: brand safety, benefit-safe framing, platform identity, language-control standards, factual accuracy, workflow source-control, no-invention rules, fact-checking, Google structured data visibility, schema-supported claim safety.

When Page Creation Architecture or Pillar Architecture creates pressure toward unsafe, unsupported, or outdated wording: preserve strategic intent, rewrite output safely.

---

## Foundational Anchors

### Platform Identity Rule
VeteranDegrees.com = guidance and verification platform. NOT: school, degree-grantor, enrollment office, benefits administrator, VA decision-maker.

**Safe phrasing pattern:** "programs/schools listed on VeteranDegrees.com," "VeteranDegrees.com helps readers compare and verify"
**Prohibited pattern:** "our programs/schools," "enroll through," "apply to," "VeteranDegrees.com offers/pays/certifies"

### Reader Framing
Audience: veterans, transitioning service members, working veterans, eligible family members, veteran parents (transferred benefits), dependents.
Frame as: using earned or transferred benefits wisely. NOT: gaming, exploiting, hacking, chasing.

### Housing Allowance Language
Default reader-facing term: **housing allowance**
Use **BAH/MHA** only for: keyword fields, quoted source language, official terminology explanation, search-language notes, search-term comparisons.
NEVER guarantee: full housing allowance, eligibility, payment, VA approval, enrollment outcomes, or career outcomes.
Every housing allowance statement must preserve eligibility, enrollment, modality, benefit-status, school, and VA caveats.

### Five Fixed Pillars
| # | Pillar | Focus |
|---|---|---|
| P1 | Hybrid/Low-Residency Programs | Formats, schedules, structures |
| P2 | Housing Allowance / MHA Strategies | Planning, eligibility, calculation context |
| P3 | VA Compliance & Verification | WEAMS, VA approval, enrollment certification |
| P4 | GI Bill Benefits Optimization | Entitlement, planning, stacking, timing |
| P5 | Career Outcomes Enabled by Hybrid Programs | Post-service outcomes tied to hybrid education. Evidence required. |

---

## Pre-Creation Setup

**Step 1. Determine Page Type**
| Type | Role | Priority |
|---|---|---|
| Hub/Pillar | Topical authority for one pillar. Broadest treatment. | Highest. Build before clusters. |
| Cluster/Supporting | Narrow subtopic supporting one pillar. | After hub confirmed or planned. |
| School | P1 cluster + P3 verification context. One school. | Alongside P1 expansion. Must link to P1 hub. |

**Step 2. Assign the Pillar Before Writing**
One primary pillar per page. Secondary pillar touches allowed only when they support main purpose, not dilute it.

**Step 3. Define the Primary Entity Concept**
One sentence. More specific than the pillar name. More precise than a keyword phrase.

**Step 4. Plan the URL Before Writing**
Must match entity concept and pillar.
Use: `/va-weams-program-verification-guide`, `/hybrid-degree-format-for-working-veterans`
Avoid: `/benefits`, `/careers`, `/programs`
School pages: `/[school-name]` | Blog clusters: `/news/[entity-specific-topic]` | Pillar/guide pages: clearest entity-specific slug.

**Step 5. Identify Source Requirements**
| Claim Type | Handling |
|---|---|
| Stable brand/platform claim | Match brand positioning module. |
| Keyword/topic claim | Guides coverage only. Not a factual claim by itself. |
| VA rule, benefit, WEAMS, approval, certification, housing allowance | Verify against authoritative or workflow-approved sources. |
| School/program claim | Source packet, approved database, or authoritative source required. |
| Salary, labor market, ROI, career outcome, causal claim | Source + caveat + fact-check before publication. |
| Schema-supported fact | Visible, accurate, representative, source-supported. |

Missing or unverifiable field: mark `Needs source`. DO NOT invent.

---

## 9-Step Creation Process

### Step 1. Write the Title Tag First
Names specific topic and primary entity concept. Platform-safe. ~50-60 chars. Brand suffix when appropriate. No generic-only titles. No provider language or outcome-guarantee language.

**Scoring Rubric**
| Score | Label | Description |
|---|---|---|
| 5 | Precise | Exact entity concept + pillar + safe platform identity. Clear and search-useful. |
| 4 | Correct | Right topic and entity. Minor element missing or slightly less specific. |
| 3 | Generic | On-topic but non-differentiated. Needs refinement. |
| 2 | Diluted | Partially correct + off-entity or provider-like terms. |
| 1 | Rejected | Brand-only, generic, misleading, unsupported, or misrepresents page. |

**GATE: Do not proceed to Step 2 with a title tag score below 4.**

### Step 2. Write the H1 Tag
Does not repeat title verbatim. Reader-first. Aligned to pillar and entity concept. No provider language. No unsupported promises. Use "housing allowance" default.

### Step 3. Write the Opening 150 Words
Must answer five questions:
1. What is this page about?
2. Who is it for?
3. What can the reader do with it?
4. What is VeteranDegrees.com's role?
5. How does the topic connect to the relevant pillar?

Sentence one = main topic. Audience named or implied. Platform framed as guidance and verification. Pillar connection appears naturally. Pillar-specific language (hybrid, housing allowance, VA, GI Bill, career) only when genuinely relevant. No unsupported benefit, salary, approval, or outcome claims.

### Step 4. Build the Body Content Structure
Required blocks: Primary Definition | Pillar-Specific Content | Source-Supported Factual Anchors | Structured Formats (tables, steps, checklists, comparisons) | Hybrid Program Anchor (when relevant) | Platform Identity Signal (at least once in body) | Internal Link to Hub | Citable Response Blocks per major distinct answer, definition, comparison, process, or decision point.

Alignment rules: Each H2 contributes to assigned pillar. Sections answer specific reader questions. Claims calibrated to evidence. Keywords do not become unsupported claims. No schema-only facts.

### Step 5. Build Hub-Cluster Architecture Into the Page
| Page Type | Must Link To | Anchor Guidance |
|---|---|---|
| Hub/Pillar | Active cluster pages within pillar. | Descriptive, topic-specific. |
| Cluster | Pillar hub required. Related clusters optional. | Describes destination. No forced exact-match. |
| School | P1 hub + relevant P3/benefits clusters when supported. | Link naturally to hybrid-program and verification resources. |
| Any | Entity hub `/gi-bill-hybrid-programs` when relevant. | Safe anchors only. |

PROHIBITED as normal reader-facing anchor text: "hybrid programs with full housing allowance," "get full BAH," "VA-verified hybrid programs with full housing allowance."

### Step 6. Build for Extractability and Structured Data
Controlling module: `vd-ai-extractability-v1.0.0.md`

**6.1 Citable Response Blocks**
Public label: `Citable response:`
Use for each major section with distinct answer, definition, comparison, eligibility rule, process, or decision point. DO NOT add merely to hit a ratio.

Standards: Visible to readers | Self-contained | Caveats preserved | Reader/brand/benefit-safe | Not schema stuffing | No unsupported claims | No provider/certifier/payer language.

**6.2 Claim Calibration**
Avoid unless evidence fully supports: "consistently finds," "research confirms," "studies show," "evidence proves," "the literature agrees."
Use when evidence is limited, directional, or mixed: "suggests," "tends to," "available evidence indicates," "findings from [study] suggest."

**6.3 Schema-Supported Visible Facts**
Must be: visible, accurate, representative, source-supported.
Structured data must NOT add: hidden facts, stronger claims, unsupported claims, misleading relationships, benefit promises, or imply platform offers degrees, operates schools, enrolls students, certifies or pays VA benefits, or guarantees housing allowance or career outcomes.

**6.4 JSON-LD Readiness**
Default format when CMS and template allow. Means: visible content is clear, complete, and structured enough for a developer to represent supported facts in JSON-LD without adding hidden claims. Writers do not produce final production JSON-LD unless specifically assigned.

**6.5 Google Structured Data Caveat**
Google Search Central = controlling source for Google Search behavior. Schema.org defines types and properties only. Structured data does NOT guarantee: rankings, rich results, featured snippets, AI citations, answer-engine inclusion, or any specific search appearance. Do not claim schema guarantees visibility internally or publicly.

### Step 7. Apply Keyword Placement Standard
Write to the **concept**, not the keyword string. Entity framing > density.

| Location | Standard |
|---|---|
| Title + H1 | Primary keyword concept, safely phrased. |
| Opening 150 | Primary topic/question + entity + platform role. |
| H2s | Secondary signals where they match real section meaning. |
| Body | Natural semantic terms and related entities. |
| FAQ | Long-tail question mapping. Answers must be visible, accurate, caveated. |
| Anchor text | Entity-rich and descriptive. No unsupported guarantees. |
| Citable blocks | Natural reader language. No forced exact-match keywords. |
| Schema-supported text | Visible, accurate, source-supported, consistent with copy. |

Overriding rules: Entity framing > keyword density. Platform identity signal = non-negotiable. Benefit-safe language = non-negotiable. Keywords do not auto-become Citable claims or schema facts. No provider language.

### Step 8. Apply the Anti-Pattern Check
| Anti-Pattern | Correct Approach |
|---|---|
| Provider language | "programs/schools listed on VeteranDegrees.com" |
| Generic veteran education content | Tie to assigned entity concept and pillar. |
| Forced hybrid language in unrelated sections | Hybrid framing only where it supports actual page purpose. |
| Career content with no hybrid/education tie | Tie to supported hybrid education pathways and evidence. |
| Benefits content without caveats | Preserve VA, enrollment, modality, school, and benefit-status caveats. |
| Keyword-matching instead of entity-building | Write to concept. Use keywords naturally. |
| Schema-only claims | Every schema claim must be visible, accurate, source-supported. |
| Stronger metadata/JSON-LD than page copy | Keep metadata aligned with visible copy. |
| Citable blocks that remove caveats | Keep blocks self-contained and properly caveated. |
| Evidence overstatement | Use calibrated evidence language. |

### Step 9. Complete the Pre-Publish Checklist

**Entity and Page Architecture**
- [ ] Page type defined.
- [ ] Assigned pillar documented.
- [ ] Primary entity concept specific, not just a keyword phrase.
- [ ] URL slug matches entity concept and pillar.
- [ ] Body content serves one primary pillar.
- [ ] Hub link present for cluster and school pages.
- [ ] Internal links use descriptive, safe anchor text.

**Title, H1, and Opening**
- [ ] Title tag scored 4 or higher.
- [ ] H1 consistent with title tag. Not a mechanical repeat.
- [ ] Opening 150 words answer all five questions.
- [ ] Opening establishes platform as guidance and verification.
- [ ] Pillar-specific language appears only where relevant.

**Brand, Language, and Benefit Safety**
- [ ] Platform identity correct.
- [ ] No provider language.
- [ ] "Housing allowance" default. BAH/MHA exceptions valid only per Step 1 of Foundational Anchors.
- [ ] No guaranteed housing allowance, eligibility, VA approval, enrollment, or career outcomes.
- [ ] Benefit claims preserve caveats.

**Extractability and Structured Data**
- [ ] Citable response blocks present for major distinct answers, definitions, comparisons, rules, processes, and decision points.
- [ ] Blocks: visible, self-contained, reader-useful, properly caveated.
- [ ] Blocks do not imply provider, certifier, payer, or benefits-administrator status.
- [ ] Schema-supported facts visible in page copy.
- [ ] No metadata, FAQ, or JSON-LD field requires a hidden claim.
- [ ] Structured data not stronger than visible copy.
- [ ] FAQ content visible on page if FAQ markup planned.
- [ ] Breadcrumb text matches visible site structure if BreadcrumbList planned.
- [ ] JSON-LD readiness achieved without unsupported facts.

**Source and Fact-Check**
- [ ] School/program claims source-supported.
- [ ] WEAMS, VA approval, enrollment, and benefit claims verified or marked `Needs source`.
- [ ] Salary, labor market, ROI, and career claims sourced and caveated.
- [ ] Evidence-summary sentences do not overstate consensus.
- [ ] Unsupported claims removed or marked `Needs source`.

**Keyword and Content Quality**
- [ ] Keyword placement standard applied naturally.
- [ ] No exact-match keywords forced into Citable blocks, headings, FAQ, or anchor text.
- [ ] No duplicate or near-duplicate content introduced.
- [ ] Structured formats serve the reader, not SEO appearance only.
- [ ] Draft ready for Keyword Audit Report, Fact-Check Report, and Copy QA when required by workflow.

---

## Page-Type Standards

**Hub/Pillar Pages:** Broadest pillar treatment. Establish pillar and sub-entities in opening. Link to active clusters. Address major reader decisions. Citable blocks for definitions, comparisons, decision frameworks. Schema facts visible and source-supported. Topical authority > conversion language.

**Cluster/Supporting Pages:** One primary entity concept. Link back to hub. Unique angle not covered by hub or adjacent clusters. At least one visible answer block for distinct definition, decision point, or process. No new unsupported claims added to broaden page scope.

**School Pages (P1+P3):** Format description: source-supported only. VA/WEAMS/verification information: source-supported and caveated. Housing allowance: relevant and supported only. Link to P1 hub and verification resources. Guidance framing, not school marketing. Platform does not own, operate, certify, or enroll.

**P5 Career Outcomes:** Salary data: sourced and tied to specific degree fields or occupations. ROI claims: caveated and source-supported. Case studies: factual and sourced, or clearly labeled hypothetical. Security clearance or employment-continuity content: framed carefully, not promised. Career outcomes: NEVER guaranteed.

---

## EAS Self-Score (Draft Stage)

**GATE: Composite must be 4.0 or above before publishing.**

| Dimension | Creation Standard |
|---|---|
| Title Tag | Precise entity concept, pillar focus, safe platform identity, no unsupported claims. |
| H1 Alignment | Reinforces title tag and concept in reader-facing language. |
| Opening 150 Words | Answers what, who, reader use, platform role, pillar connection. |
| Body Content Alignment | Serves one primary pillar. No drift. No provider language. Caveats preserved. |
| Hub-Cluster Structure | Appropriate internal links. No orphaned pages. No unsafe anchor text. |
| AI Extractability | Visible Citable blocks, entity clarity, source-supported claims, schema-ready visible facts, no schema-only claims. |

**Composite Score:** __ / 5.0

**AI Extractability Scoring:**
| Score | Label | Description |
|---|---|---|
| 5 | Strong | Major answers: visible, self-contained, caveated, reader-useful, schema-ready. No schema-only claims. |
| 4 | Publishable | Main blocks present and mostly clear. Minor caveat, visibility, or schema refinements possible. |
| 3 | Needs Revision | Thin, generic, under-caveated, or not tied to visible source-supported facts. |
| 2 | Weak | Unsupported claims, keyword stuffing, hidden assumptions, or artificial snippets. |
| 1 | Rejected | Misrepresents platform, removes caveats, or includes unsupported facts. |

---

## Content Brief Template

- **Page URL (planned):**
- **Page Type:**
- **Assigned Pillar:**
- **Primary Entity Concept:**
- **Target Audience:**
- **Reader Decision/Problem:**
- **Workflow Type / Source-Control Rule:**
- **Required Source Materials:**
- **Title Tag (draft):**
- **Title Tag Score:**
- **H1 Tag (draft):**
- **Primary Topic / Question:**
- **Opening 150 Words. Key Points:**
  - What: | Who: | Reader use: | Platform role: | Pillar connection:
- **Primary Definition:**
- **Planned Citable Response Blocks:**
  - Section/H2: | Answer opportunity: | Required caveats: | Source:
- **Schema-Supported Visible Facts:**
  - Fact: | Location on page: | Source/status: | Structured data use:
- **JSON-LD Readiness Notes:**
- **FAQ Opportunities:**
  - Question: | Visible answer plan: | Source/caveat:
- **Factual Claims to Include:**
- **Factual Claims to Verify:**
- **Research/Source Gaps:**
- **Internal Links. Outbound:**
- **Internal Links. Inbound:**
- **WEAMS / VA Compliance Signal:**
- **Housing Allowance Language Notes:**
- **Content Sections Outline:**
- **Anti-Patterns to Avoid:**
- **Keyword Placement Plan:**
- **Assigned Writer:**
- **Target Publish Date:**

Missing fields: mark `Needs source` or `Not applicable`. DO NOT invent.

---

## Quick Decision Reference
1. Does this serve the assigned pillar?
2. Does this reinforce VeteranDegrees.com as a guidance and verification platform?
3. Is the primary entity concept specific enough?
4. Is pillar-specific language present only where relevant?
5. Is the claim visible, accurate, representative, and source-supported?
6. Would the claim be safe in a Citable block, FAQ answer, metadata, or JSON-LD field?
7. Does the page link correctly in the hub-cluster architecture?
8. Is it immediately useful to a veteran, veteran parent, service member, or dependent?
9. Does wording avoid benefit guarantees, provider language, and overconfident evidence summaries?
10. Are missing facts marked `Needs source` instead of invented?

---

** vd-page-creation-architecture-min-v1.0.0.md ** | Derivative of vd-page-creation-architecture-v1.0.0.md | Internal use only.
