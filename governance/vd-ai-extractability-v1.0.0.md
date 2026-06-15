# VD AI Extractability Standards | v1.0.0-compressed
**Source:** vd-ai-extractability-v1.0.0.md | Compression: LLM-context only. Source stays canonical.

---

## CORE STANDARD [ZERO COMPRESSION]
- Every major page = entity-clear at page level + extractable at section level.
- One Citable response per major section that introduces a distinct answer, definition, comparison, eligibility rule, process, or decision point.
- No fixed ratio. No anchor-stuffing.

---

## WHOLE-PAGE ENTITY EXTRACTABILITY
First 150 words must answer:
1. What is this page?
2. Who is it for?
3. What can the reader do?
4. What is VeteranDegrees.com's role?
5. How does topic connect to hybrid / housing allowance / VA verification / GI Bill / career outcomes (when relevant)?

---

## CITABLE RESPONSE RULES [ZERO COMPRESSION ON GATES]

**Use when section introduces:** definition, eligibility/benefit rule, comparison, verification process, step-by-step process (usually), FAQ answer (if important), tool/calculator explanation (usually).

**Do NOT use for:** transitional sections, short supporting details, repeated concepts already covered.

**Required qualities:** self-contained, direct, reader-useful, evidence-calibrated, entity-clear, benefit-safe, platform-safe, visible, consistent with structured data.

**Length:** 40–90 words standard. Shorter OK for definitions. Longer only when caveat requires it. Place near section start, after 1–2 context sentences.

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
