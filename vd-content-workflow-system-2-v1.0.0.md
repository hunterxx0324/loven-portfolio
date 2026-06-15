# VD Content Workflow — System 2 (Compressed)
**Source:** vd-content-workflow-system-2-v1.0.0 | **Compression version:** v1.0.0

---

## SYSTEM IDENTITY

**System 2 = Outline + Research Workflow.**
Trigger: user provides **both** an outline **AND** a research/source file.

| Condition | Action |
|-----------|--------|
| Outline only, no research | → Use System 1 |
| Research only, no outline | → Ask for outline before proceeding |
| Both present | → Use System 2 |

**Controlling hierarchy:**
1. Outline → controls structure, section order, headings, tables, FAQs, word counts, section intent
2. Research material → controls factual drafting content
3. VD reference files → control brand, language, tone, extractability, keyword audit, fact-checking
4. Guide A / Guide B → control architecture, pillar scope, entity alignment, keyword territory, strategic intent

> **Hard rule:** Do not copy unsafe, outdated, overconfident, or benefit-risky wording from any source into final content.

---

## WEB SEARCH RESTRICTION [ZERO-COMPRESSION]

> **Hard rule:** Do NOT search the web during drafting unless the user explicitly authorizes additional research.

Web search is allowed ONLY during the Fact-Check Report stage, and only to verify claims already in the draft.

**Do not use fact-checking research to:**
- add new sections, claims, FAQ answers, metadata, or schema-supported facts
- expand the article or replace the user's research document
- rewrite with outside information

Flag conflicts; recommend safer wording. Do not silently add new material.

---

## REFERENCE FILES [ZERO-COMPRESSION — HARD DEPENDENCY LIST]

1. `vd-brand-positioning-v1.0.0.md`
2. `vd-language-control-standards-v1.0.0.md`
3. `vd-tone-and-style-v1.0.0.md`
4. `vd-ai-extractability-v1.0.0.md`
5. `vd-keyword-audit-v1.0.0.md`
6. `vd-fact-checking-v1.0.0.md`
7. `vd-keyword-type-map-v1.0.0.md`
8. Guide A — Content & Webpage Creation Guide
9. Guide B — Expanded Pillar Definitions

> **Hard rule:** Guide A / Guide B = required source standards, NOT final copy. If Guide B suggests an angle the research document does not support → mark as research gap. Do not force into draft.

---

## PRE-DRAFT SEQUENCE

| Step | Action | Key Rule |
|------|--------|----------|
| 1. Input Inventory | Identify all inputs: title, slug, pillar, keywords, outline, research doc, word count, links, FAQs, tables, etc. | State assumption if missing and task can proceed; ask if missing input would materially change content. Never invent research. |
| 2. Task Type | Identify scope (full draft, section rewrite, audit, fact-check, etc.) | Do not assume full article. Match output to scope. |
| 3. Pillar & Page Type Check | Identify/infer using Guide B (pillar) and Guide A (page type) | If pillar inferred, state assumption. Page type affects structure, depth, schema needs, internal linking. |
| 4. Outline Review | Check H1/H2/H3 logic, section purposes, duplicates, required elements | If outline conflicts with research → preserve outline structure; flag unsupported content as research gap. |
| 5. Research Material Review | Map research to: confirmed facts, source-backed claims, stats, dates, school/program details, VA policy refs, housing allowance details, career/salary data, quotes, claims needing verification, unsupported items, Citable response opportunities, FAQ candidates, schema-supported fact candidates, source gaps | Research document = factual boundary for main draft. If claim not in research → do not add as fact. |

---

## RESEARCH GAP HANDLING [ZERO-COMPRESSION]

If the outline asks for information not supported by the research material:

1. Mark it as a research gap
2. Use cautious placeholder language
3. Ask focused clarification if gap materially affects content
4. Reframe the section around what the research does support

> **Never invent facts to satisfy the outline.**

**Required label:**
> **Research gap:** The provided research does not include enough support to make this claim safely.

This applies equally to: extractability angles, FAQ answers, metadata claims, schema-supported facts, JSON-LD-ready statements.

---

## DRAFTING RULES [ZERO-COMPRESSION CORE]

Use outline for structure. Use research material for facts. Apply VD rule files.

**Never add during drafting:**
- unsupported claims, invented examples, invented statistics
- invented school/program/VA policy/salary/career claims
- invented Citable response claims, FAQ answers, or schema-supported facts
- web-sourced content (restricted until fact-check stage)

If research material gives exact wording that is unsafe, promotional, outdated, or overconfident → rewrite in benefit-safe language.

**Evidence Summary Sentence Rule [ZERO-COMPRESSION]:**
Before using any of: "consistently finds/shows/demonstrates," "research confirms," "studies show," "evidence proves," "the literature agrees" — verify the research material actually supports multi-source consensus. If it supports only a directional tendency → use: "suggests," "tends to," "available evidence indicates," "findings from [specific study] and supporting literature suggest."

Applies most critically to: section openings, transitional summary sentences, Citable response blocks, FAQ answers, evidence summaries, schema-supported visible facts.

---

## COMPLIANCE PASSES [POST-DRAFT]

### C1 — Brand Positioning Pass → `vd-brand-positioning-v1.0.0.md`
VD = guidance/verification platform (not school). Reader framing: veterans, transitioning service members, working veterans, eligible family members, veteran parents managing transferred benefits, dependents on transferred benefits. Housing allowance = cautious framing. Benefits = not guaranteed. Direct reader to verify with school and official sources.

### C2 — Language Control Pass → `vd-language-control-standards-v1.0.0.md`
Required terms used; banned terms/phrases/formulas removed. "Housing allowance" = standard reader-facing term. "BAH" = keyword/quoted/explanatory/source-preservation contexts only. No fake urgency or false authority. Metadata/FAQ/schema blocks are not loopholes.

### C3 — Tone & Style Pass → `vd-tone-and-style-v1.0.0.md`
Practical, respectful, plainspoken. Varied sentence rhythm. Fragments = only where appropriate. Technical = complete sentences. No em-dashes. Citable response blocks = reader-useful, not schema-stuffed.

### C4 — Entity, Extractability & Structured Data Pass → `vd-ai-extractability-v1.0.0.md`

**System 2 stricter rule:** Citable response blocks, FAQ answers, metadata, schema-supported facts, and JSON-LD-ready statements may only reflect information supported by the provided research/source packet, required reference files, or user-provided materials.

Confirm:
- First 150 words: what page is, who it's for, what reader can do, VD role, relevant connection to hybrid/housing allowance/VA/GI Bill/career outcomes
- Major sections include `Citable response:` block where research supports distinct answer, definition, comparison, eligibility rule, process, or decision point
- Citable blocks = self-contained, accurate, benefit-safe, caveated, reader-first
- Schema-supported facts present in visible copy before any structured data
- Unsupported extractability angles → marked as research gaps, not added to draft
- No schema-only claims. No stronger claims in metadata/JSON-LD than in visible copy. No new schema-supported facts added during drafting.

> **Hard rule:** Do not imply structured data guarantees rankings, rich results, featured snippets, AI citations, answer-engine inclusion, or any specific search appearance.

### C5 — Formatting Pass
Heading hierarchy, bold labels, tables, bullet/numbered lists, FAQ format, `Citable response:` format, report format, internal anchor text, mobile readability, structured-data readiness notes (if requested).

### C6 — Internal Linking Pass
Entity-rich anchor text only. Never: click here, learn more, read this, this page, more info. Do not invent targets not provided by user or reference materials.

### C7 — Evidence Awareness Pass → `vd-fact-checking-v1.0.0.md`
Flag before fact-check stage: benefit rules, payment amounts, eligibility criteria, school/program claims, VA approval, policy dates, salary/job outlook data, accreditation, licensing, comparisons, causal statements, metadata/Citable/FAQ/schema-supported visible text. Do not use web research at this stage unless user explicitly authorized it during drafting.

---

## REPORTING STAGES [ON DEMAND OR PER OPERATING INSTRUCTIONS]

### R1 — Keyword Audit → `vd-keyword-audit-v1.0.0.md`
Primary keyword placement, secondary/semantic/LSI/long-tail coverage, subheading signals, anchor quality, overall score.
> Keyword audit ≠ fact-check. Do not force exact-match phrasing into Citable/FAQ/metadata/schema fields.

### R2 — Fact-Check Report → `vd-fact-checking-v1.0.0.md`
Web search authorized at this stage only. Required sections:
1. Claim Extraction Summary
2. Claim-by-Claim Verification
3. Claims Requiring Revision
4. Unsupported or Removed Claims
5. Overall Confidence Score
6. Markdown Fact-Check Table

If external verification contradicts the research document → flag conflict; recommend safer wording. Do not silently rewrite. Do not use fact-check research to introduce new schema-supported or Citable claims unless user approves a revised draft using the new source material.

---

## CONFLICT RESOLUTION [ZERO-COMPRESSION]

If outline, research document, Guide A, Guide B, or modular rule files conflict:

1. User's explicit task scope
2. Guide A / Guide B strategic intent
3. Brand positioning (platform identity, benefit framing)
4. Language control (terminology, banned phrasing)
5. Fact-checking (accuracy, current data, policy, dollar amounts, schema-supported claims)
6. AI Extractability (visible Citable blocks, entity clarity, visible-content matching, JSON-LD readiness, no schema-only claims)
7. **Apply the stricter rule when two rules both apply.**

---

## REVISION WORKFLOW

1. Identify requested revision scope
2. Check whether the change is supported by the research material
3. Preserve sections that work
4. Fix specific issue first
5. Apply C1–C6 passes as needed
6. Check whether keyword/fact-check/structured-data outputs need updates
7. Summarize changes if helpful

> Do not rewrite the full draft for a narrow edit.

---

## SCOPE CONTROL

Match output to the user request. Do not add reports unless operating instructions or user require them. Do not produce final JSON-LD unless assignment specifically asks.

---

## COMPLETION GATE [ZERO-COMPRESSION]

System 2 is complete only when ALL of the following are true:

- [ ] Task scope satisfied
- [ ] Outline followed
- [ ] Research material used as factual drafting boundary
- [ ] No unsupported facts introduced during drafting
- [ ] Research gaps flagged
- [ ] Unsupported extractability angles / schema claims marked as research gaps, not added
- [ ] Correct reference files applied
- [ ] Guide A and Guide B strategic intent preserved
- [ ] Brand positioning correct
- [ ] Terminology correct
- [ ] Tone appropriate
- [ ] Entity/Extractability/Structured Data requirements met where applicable
- [ ] Schema-supported facts are visible, source-supported, and not stronger than the copy
- [ ] JSON-LD readiness does not depend on hidden claims
- [ ] Formatting clean
- [ ] Risky claims identified
- [ ] Required reports included per operating instructions
- [ ] Web search used only during fact-checking unless explicitly authorized earlier

---

*Compressed derivative of vd-content-workflow-system-2-v1.0.0.md. Source file remains canonical. Cross-document dependencies: vd-brand-positioning, vd-language-control-standards, vd-tone-and-style, vd-ai-extractability, vd-keyword-audit, vd-fact-checking, vd-keyword-type-map, Guide A, Guide B.*
