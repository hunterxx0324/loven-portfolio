# vd-fact-checking | v1.0.0-compressed
> Derivative of vd-fact-checking-v1.0.0.md. Source file is canonical.

---

## PURPOSE
Audit factual claims against external sources.
Single question: **Is the content accurate, current, and properly supported?**
Keyword placement is out of scope. See `vd-keyword-audit.md`.

**Target errors:** hallucinated claims, outdated benefit guidance, unsupported school/program statements, overconfident VA policy, inaccurate MHA claims, weak career outcome claims, true-but-missing-caveat claims.

> **RULE:** Be skeptical, source-led. Do not protect the draft.

---

## CLAIMS REQUIRING VERIFICATION
Always verify claims involving:
GI Bill rules, Post-9/11 eligibility, MHA rules, online-only vs. hybrid benefit differences, VA approval/school participation status, program modality, campus location, in-person attendance requirements, enrollment thresholds, Yellow Ribbon, benefit amounts/deadlines, policy changes, accreditation, licensure, career outcome statistics, salary data, job growth projections, employment rates, degree requirements, school/program claims, quoted/paraphrased sources, causal claims, comparison claims.

---

## CLAIM TYPES
| Type | Description |
|---|---|
| Policy | VA, federal, state, or benefits rules |
| Eligibility | Who qualifies |
| Payment | MHA, tuition, fees, stipends |
| Program | School, degree, modality, approval, participation |
| Career | Salary, outlook, licensing, labor market |
| Date | Deadlines, effective dates, policy timelines |
| Statistic | Numbers, percentages, rankings, projections |
| Comparison | Comparing options, benefits, schools, outcomes |
| Causal | One factor causes/increases/reduces another |
| Quote/Source | Direct quotes or source-attributed statements |
| Other | Checkable claim not fitting above |
---
## SOURCE HIERARCHY (highest to lowest)
1. VA.gov / Benefits.va.gov / VA education pages
2. eCFR / Federal Register
3. Department of Education
4. BLS
5. State licensing boards / Accreditation bodies
6. Official school catalogs, program pages, SCO/registrar pages
7. Primary legal or regulatory sources
8. Reputable academic, policy, or government research
**AVOID:** unsourced blogs, affiliate pages, AI summaries, forum posts, outdated third-party summaries, marketing pages, pages without authorship, search snippets without opening source.
> **TOKEN GUARDRAIL:** Parse ONLY metadata text snippets or summaries returned by the MCP search tool. Deep crawls or fetching full raw HTML strings is strictly restricted unless a Tier 3 policy contradiction is flagged.
---
## VERIFICATION STANDARD
- Target: 2 independent sources per claim. Wording risk/source quality > count.
- **MANDATORY SHORT-CIRCUIT:** If a single primary, high-authority source (e.g., VA.gov, eCFR, BLS, or official catalog) directly verifies/refutes the claim with 10/10 precision, the agent MUST cease all further searches for that claim ID. Secondary searches are prohibited to protect token budget.
- **NEVER** pad source list with weak sources to hit the count.
---
## PROCESS
**Step 1. Token Optimization Triage (Cost Control Gate)**
Before invoking MCP Websearch, categorize all claims into execution tiers:
| Tier | Risk Profile | Verification Action | Token Impact |
| :--- | :--- | :--- | :--- |
| 🪙 T1 | Internal Workspace Truths (brand settings, fixed pillars) | Validate ONLY against local workspace files (`brand-voice.md`, `content-pillars.md`). DO NOT launch web searches. | Near Zero |
| 🥈 T2 | Industry Common Knowledge (general GI Bill definitions) | Use internal parametric knowledge base. If internal confidence is 10/10, bypass web search entirely. | Zero |
| 🚨 T3 | High-Risk Variable Facts (2026 MHA rates, changing policy) | Proceed to Step 2. Run highly targeted online queries. Extract all T3 targets and batch search them back-to-back to maximize session context caching. | Managed |

**Step 2. Extract** — Identify every specific, checkable claim. Capture: exact 
claim, type, location, whether it contains numbers/dates/policy/eligibility language, whether it affects a reader's education/benefit/financial/career decision. Skip vague opinions unless they imply a factual assertion.

**Step 3. Initial Verification** — Find high-authority sources. Determine if the source directly states, partially supports, or contradicts the claim. Check applicability (benefit chapter, school type, date, program type, student situation).

**Step 4. Source Evaluation** — Assess: authority, recency, relevance, directness, independence, consistency, primary vs. secondary. Do not use a source to support a broader claim than it actually proves.

**Step 5. Evidence Summary Sentence Rule**
> **ZERO-COMPRESSION ZONE — reproduce exactly:**
> 
> Do not use "consistently finds / shows / demonstrates," "research confirms," "studies show," "evidence proves," or "the literature agrees" unless multiple independent sources establish true consensus. Use instead: "suggests," "tends to," "available evidence indicates," "findings from [study] and supporting literature suggest." This applies most critically to opening and transitional summary sentences.

**Step 6. Adversarial Review** — Before assigning verdict, ask:
- Did the source actually say this?
- Is draft wording broader than evidence supports?
- Is the claim outdated?
- Is a caveat missing?
- Could the answer vary by school, program, chapter, modality, campus, enrollment status, or date?
- Would a reader make a financial or enrollment decision based on this wording?

**Step 7. Verdict**
| Verdict | Meaning |
|---|---|
| ✅ Verified | Supported by authoritative, relevant evidence |
| ❌ Debunked | Contradicted by authoritative evidence |
| ⚠️ Mixed | Partly true, incomplete, context-dependent, overstated, or disputed |
| ❓ Unclear | Evidence insufficient, unavailable, outdated, or not specific enough |

**Step 8. Confidence Score**
| Score | Meaning |
|---:|---|
| 9–10 | Strongly supported, current, authoritative, direct |
| 7–8 | Supported with caveats, limited source independence, or wording risk |
| 5–6 | Partially supported; source quality, specificity, or recency limited |
| 3–4 | Weak support, missing caveats, or conflicting evidence |
| 1–2 | Unsupported, contradicted, outdated, or likely inaccurate |
> **RULE:** Do not assign 10 if any caveat is missing. Score must match detailed report score.
---
## OUTPUT FORMAT
Two required parts: **(1) Detailed Report + (2) Markdown Table.** Do not replace the detailed report with the table unless explicitly requested.

---
### DETAILED REPORT TEMPLATE
```
# FACT-CHECK REPORT

## 1. Claim Extraction Summary
| ID | Claim | Claim Type | Location in Draft |
|---:|---|---|---|

## 2. Claim-by-Claim Verification

### Claim [N]
> **The Claim:** [Exact statement]
**Claim Type:** [Type]
**Location in Draft:** [Section or paragraph]
**The Verdict:** [Verdict]
**The Evidence:** [2-sentence summary. Max 15 words quoted from any source.]
**The Sources:**
- [Source 1]
- [Source 2]
**Confidence Score:** [1–10]
**Verification Note:** [Adversarial review. If inconclusive, state "Inconclusive" and explain.]

## 3. Claims Requiring Revision
| ID | Claim | Issue | Recommended Revision |
|---:|---|---|---|
[If none: "No claims require revision based on the available evidence."]

## 4. Unsupported or Removed Claims
| ID | Claim | Reason It Should Be Removed |
|---:|---|---|
[If none: "No claims need to be removed based on the available evidence."]

## 5. Overall Confidence Score
**Overall Confidence Score:** [1–10]
**Summary:** [Factual reliability, remaining risks, required revisions before publishing.]
```

---

### MARKDOWN TABLE TEMPLATE

```
| ID | Claim | Verdict | Evidence | Confidence Score | Sources |
|---:|---|---|---|---:|---|
| 1 | [Exact claim] | [Verdict] | [1–2 sentence summary] | [1–10] | [URL1]; [URL2] |
```

**Column rules:**
- **ID:** Sequential. Must match detailed report ID.
- **Claim:** Exact. Shorten only for readability; preserve factual meaning.
- **Verdict:** Use icon format consistently throughout.
- **Evidence:** 1–2 sentences. No quotes over 15 words.
- **Confidence Score:** Must match detailed report.
- **Sources:** URLs or linked titles. Semicolon-separated.
