# VD AI Extractability Standards | v1.0.0-compressed
**Source:** vd-ai-extractability-v1.0.0.md | Compression: LLM-context only. Source stays canonical.

---

## MODULE ROLE
Owns the extractability layer. Controls: Citable response blocks, AI Extractability Anchors, first-150-words standard, section-level answer clarity, entity naming, schema-supported facts, JSON-LD readiness, Google structured data alignment, FAQ extractability, extractability QA.

Does NOT replace: brand-positioning, language-control, tone-and-style, keyword-type-map, keyword-audit, fact-checking, vd-page-creation-architecture (page architecture, EAS), vd-pillar-architecture (pillar strategy), copy-QA-method.

**Conflict rule:** Preserve user task. Apply stricter rule where both can apply.

---

## CORE STANDARD [ZERO COMPRESSION]
- Every major page = entity-clear at page level + extractable at section level.
- One Citable response per major section that introduces a distinct answer, definition, comparison, eligibility rule, process, or decision point.
- No fixed ratio. No anchor-stuffing.

---

## DEFINITIONS

**AI Extractability.** Accurate interpretation, summary, citation, and classification by humans, search systems, answer engines, AI. Fails if extracted answer becomes misleading after caveats, source limits, or platform identity are removed.

**AI Extractability Anchor.** Internal editorial label. Public label = **Citable response:**. Never use "AI Extractability Anchor" in public content.

**Citable Response.** Visible self-contained answer block. Must: name topic, answer section question, include caveats, preserve benefit-safe framing, preserve platform identity, make sense out of context, use correct terminology, avoid banned phrases and schema-only claims.

**Schema-Supported Claim.** Visible page fact representable in structured data. Must be: visible, accurate, representative, current, source-supported, not broader or stronger than evidence supports.

**Schema-Only Claim.** Claim in structured data not visible to readers. PROHIBITED.

**JSON-LD Readiness.** Visible content is clear/complete enough that a developer can represent supported facts in JSON-LD without adding hidden claims.

---

## WHOLE-PAGE ENTITY EXTRACTABILITY
First 150 words must answer:
1. What is this page?
2. Who is it for?
3. What can the reader do?
4. What is VeteranDegrees.com's role?
5. How does topic connect to hybrid / housing allowance / VA verification / GI Bill / career outcomes (when relevant)?

Do not force every section to mention hybrid programs.

**Opening pattern (adapt, do not repeat mechanically):**
`[Page topic] explains [specific decision/concept] for [reader group]. It helps readers understand [practical use], compare [relevant options], and identify what must be verified before making an enrollment or benefit-related decision. VeteranDegrees.com is a guidance and verification platform. It helps readers compare programs listed on VeteranDegrees.com and verify important details with schools and official sources before enrolling.`

---

## CITABLE RESPONSE RULES [ZERO COMPRESSION ON GATES]

**Use when section introduces:** definition, eligibility/benefit rule, comparison, verification process, step-by-step process (usually), FAQ answer (if important), tool/calculator explanation (usually).

**Do NOT use for:** transitional sections, short supporting details, repeated concepts already covered.

**Required qualities:** self-contained, direct, reader-useful, evidence-calibrated, entity-clear, benefit-safe, platform-safe, visible, consistent with structured data.

**Length:** 40–90 words standard. Shorter OK for definitions. Longer only when caveat requires it. Place near section start, after 1–2 context sentences.

**Prohibited patterns:** [ZERO COMPRESSION]
- Unsupported facts
- Hidden caveats
- Exact-match keyword forcing
- Same answer repeated across pages
- Broad claims from thin evidence
- Implied guaranteed housing allowance outcomes
- Implied guaranteed eligibility, approval, payment, enrollment, or career outcomes
- VeteranDegrees.com framed as school, certifier, or benefits authority
- Seeding AI citations readers cannot verify on the page

---

## ENTITY CLARITY RULES
Name entities directly. No vague pronouns ("this," "it," "they," "the program") in quotable sentences.

**Use full names:** VeteranDegrees.com, Post-9/11 GI Bill, monthly housing allowance, hybrid program, online-only program, School Certifying Official, WEAMS, VA-approved program, Yellow Ribbon Program, Chapter 31 VR&E.

**Housing allowance:** standard reader-facing term. Use "BAH" only in: keyword fields, search-language notes, official source language, direct quotes, explanatory terminology.

---

## PLATFORM IDENTITY IN EXTRACTABLE CONTENT [ZERO COMPRESSION]

**Use:**
- "VeteranDegrees.com is a guidance and verification platform."
- "programs listed on VeteranDegrees.com"
- "schools found on VeteranDegrees.com"
- "VeteranDegrees.com helps users compare education options and verify program details."

**Never use:**
- "VeteranDegrees.com offers degrees"
- "our schools" / "our programs"
- "enroll through VeteranDegrees.com"
- "apply to VeteranDegrees.com"
- "VeteranDegrees.com certifies VA benefits"
- "VeteranDegrees.com guarantees housing allowance"

---

## BENEFIT-SAFE EXTRACTABILITY [ZERO COMPRESSION ON CAUTION SUBSTANCE]
Never imply: every hybrid qualifies for full housing allowance, one in-person class always triggers full amount, all students receive same amount, listed schools are auto-VA-approved, VeteranDegrees.com can determine eligibility, benefit or career outcomes are guaranteed.

**Required substance when discussing housing allowance:** outcomes depend on VA rules, school certification, enrollment status, course modality, benefit chapter, and location. Verify with SCO and official VA sources before enrolling. Do not repeat verbatim every section. Preserve substance where benefit outcomes are discussed.

---

## EVIDENCE CALIBRATION
**Avoid:** "research confirms," "studies show," "evidence proves," "the literature agrees," "consistently demonstrates/finds/shows."

**Use instead:** "suggests," "tends to," "available evidence indicates," "findings from [source] suggest," "current source material indicates," "the available data points to."

---

## GOOGLE STRUCTURED DATA [ZERO COMPRESSION ON RULES]
- Controlling source: Google Search Central (not Schema.org alone).
- Default format: JSON-LD.
- Schema describes visible content only. Never adds hidden facts, stronger claims, or misleading relationships.
- Structured data does NOT guarantee rankings, rich results, featured snippets, AI citations, or any specific search appearance.
- Every JSON-LD field must be supported by visible page content.

**Six-test gate for schema-supported claims:** visibility, accuracy, source control, representation, specificity, caveat preservation. Fail any test = do not mark up.

---

## PAGE-TYPE SCHEMA QUICK REFERENCE
| Page type | Common schema considerations |
|---|---|
| Article / guide | `Article`, `BlogPosting`, `WebPage`, `BreadcrumbList` |
| Pillar / hub | `WebPage`, `CollectionPage`, `BreadcrumbList`, possible `ItemList` |
| School page | `WebPage`, `Organization` or `CollegeOrUniversity` (if visible content supports), `BreadcrumbList` |
| Program guide | `WebPage`, possible `Course` if content supports, `BreadcrumbList` |
| Comparison | `WebPage`, possible `ItemList`, `BreadcrumbList` |
| FAQ | `FAQPage` only when current Google guidance + visible content support it |
| Tool / calculator | `WebPage`, possible software markup if technically and visibly supported |
| About / org | `Organization`, `WebSite`, `WebPage` |

Use most specific applicable type only. Do not add schema types because they exist in Schema.org.

---

## JSON-LD READINESS GATE [ZERO COMPRESSION]
Page is JSON-LD ready when:
- Primary entity is clear
- Page type is clear
- Clear title and H1
- Opening identifies topic, audience, task, platform role
- Citable responses support major section answers
- Schema-supported facts are visible
- Required caveats are visible
- Risky claims verified or flagged
- No schema-only claims needed to complete markup

---

## CONTENT-TYPE CITABLE RESPONSE RULES (COMPRESSED)

**Comparisons:** State what is compared, main difference, when each fits, what to verify, what page does not determine. No false winners. No "hybrid is better than online" without specific source support.

**Verification sections:** Name entity being verified, official/school source to check, risk of assuming without verification, limit of VeteranDegrees.com's role.

**School pages:** Name school, format/focus, benefit issue, what to verify, platform identity. Never sound like school advertisement. Never imply enrollment through VeteranDegrees.com.

**Housing allowance content:** Do not imply guaranteed payment. State that outcomes depend on: VA rules, benefit chapter, school certification, course modality, enrollment status, campus location, rate year, student circumstances. Exact amounts and rates require current source verification.

**Career outcome content:** No guaranteed job, promotion, salary increase, career change, ROI, or employer recognition. Use calibrated language tied to field, experience, degree level, labor market, employer requirements, program quality.

---

## SOURCE-CONTROL RULES BY WORKFLOW
**System 1 (Outline-Only):** External research permitted when needed, unless user gives stricter rule. Schema claims and Citable responses involving VA policy, school status, modality, housing allowance, rates, salary, accreditation, dates, or dollar amounts must be verified before publication.

**System 2 (Outline + Research):** Research document controls factual content. Citable responses must not introduce claims beyond research material, reference files, or user-provided material. If angle not supported: flag as `Research gap: The provided research does not support this claim strongly enough for a Citable response or schema-supported fact.`

**Outline stage:** Extractability anchors = planned opportunities, not verified claims. Do not treat outline-stage ideas as final Citable responses until drafting and fact-checking support them.

---

## KEYWORD AND LANGUAGE-CONTROL BOUNDARIES
- Keywords guide entity coverage, section planning, FAQ planning, internal linking. They do not automatically become Citable response claims.
- Do not force exact-match keywords into Citable responses if the phrase violates brand positioning, language control, benefit-safe framing, source accuracy, reader clarity, or structured data alignment.
- Citable responses, FAQ answers, metadata, schema-supported visible content, and JSON-LD text fields must follow language-control standards. Extractability is not an exception to banned words, banned phrases, or platform-safe phrasing.

---

## CITABLE RESPONSE TEMPLATES

**Definition:**
`**Citable response:** [Term] means [plain definition] in the context of [specific reader situation]. For [VD audience], the key issue is [decision/verification need]. Readers should verify [variable details] before relying on this for enrollment or benefit decisions.`

**Benefit-safe:**
`**Citable response:** [Benefit concept] may affect [reader outcome], but the result depends on [specific variables]. VeteranDegrees.com helps readers compare options and identify what to verify, but students should confirm [approval/modality/enrollment status/benefit chapter/location/rate] with the school and official VA sources before enrolling.`

**Comparison:**
`**Citable response:** [Option A] and [Option B] differ mainly in [specific difference]. [Option A] may fit readers who need [condition], while [Option B] may fit readers who need [condition]. The better choice depends on [decision variables], and benefit-related details should be verified before enrollment.`

**Process:**
`**Citable response:** To [complete process], readers should first [step 1], then [step 2], and finally [step 3]. This process helps reduce the risk of [problem], but it does not replace verification with [school/VA source/official database/relevant authority].`

**Platform role:**
`**Citable response:** VeteranDegrees.com is a guidance and verification platform that helps veterans, transitioning service members, and eligible family members compare education options and understand what details to verify before enrolling. It does not operate as a school, certify VA benefits, determine eligibility, or guarantee housing allowance outcomes.`

---

## PROHIBITED PRACTICES [ZERO COMPRESSION]
- Hidden schema claims
- Schema for facts not visible on page
- Structured data making page appear more complete than it is
- Structured data claiming affiliation, authority, ownership, or school status that is inaccurate
- Citable responses seeding unsupported AI citations
- Exact-match keywords at expense of clarity
- Benefit caveats removed for brevity
- Same Citable response repeated across pages
- Marking up outdated rates or policy as current
- Marking up FAQ content not visible to readers
- Treating vd-pillar-architecture-v1.0.0.md extractability angles as verified claims
- Treating keyword maps as factual claim sources
- Treating valid Schema.org vocabulary as automatic Google rich result eligibility
- Implying structured data guarantees rich results or AI citation

---

## STRUCTURED DATA QA CHECKLIST (COMPRESSED)
- [ ] Clear primary entity concept
- [ ] Page type clear
- [ ] First 150 words: topic, audience, reader task, platform role
- [ ] Major sections with distinct answers have Citable responses where appropriate
- [ ] Every schema-supported fact visible on page
- [ ] No JSON-LD field introduces hidden claim
- [ ] No structured data claim stronger than visible content
- [ ] No structured data claim removes required caveat
- [ ] Time-sensitive facts current or flagged
- [ ] Benefit claims include verification logic
- [ ] FAQ markup matches visible FAQ content
- [ ] Breadcrumb markup matches visible/template navigation
- [ ] Schema type reflects main page purpose
- [ ] Required properties for Google-supported type present
- [ ] Recommended properties included only when accurate and visible
- [ ] Ready for Rich Results Test or developer validation

---

## COMPLETION STANDARD [ZERO COMPRESSION]
Page satisfies this module when:
- Page entity is clear
- First 150 words establish topic, audience, action, platform role
- Major sections contain Citable responses where appropriate
- Citable responses are self-contained and caveated
- Benefit-related statements preserve verification logic
- Evidence statements are calibrated
- Schema-supported facts are visible and accurate
- JSON-LD readiness requires no hidden claims
- Language-control standards followed
- Brand positioning preserved
- Keyword usage supports entity clarity without forcing unnatural phrasing
- Page can be summarized or cited without distorting meaning

---

## FINAL RULE [ZERO COMPRESSION]
AI extractability is not making content easy for machines at the expense of readers. It means making visible content clear enough that readers, search systems, answer engines, and AI systems identify the same accurate answer. The reader-facing page is the source of truth. Structured data may clarify that visible truth. It must not replace it.

---
*Compressed derivative of vd-ai-extractability-v1.0.0.md. Source file remains canonical. Do not publish this file or treat it as a replacement for the source.*
