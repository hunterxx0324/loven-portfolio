# VD Keyword Audit | v1.0.0-compressed
**Derivative of:** vd-keyword-audit-v1.0.0.md (canonical, do not overwrite)

---

## Purpose
Verify keyword territory is used correctly, naturally, and strategically. Does NOT fact-check (see vd-fact-checking-v1.0.0.md). Does NOT qualify content for Citable blocks, metadata, JSON-LD, or schema (see vd-ai-extractability-v1.0.0.md).

---

## Required Inputs
- Planned URL/slug, Assigned pillar (P1–P5), Primary keyword
- Secondary keywords (from vd-pillar-architecture), Semantic/LSI terms (from vd-keyword-type-map)
- Long-tail keywords (if applicable), Internal links + anchor text

---

## Hard Rules

**Primary keyword MUST appear in:** Title tag, H1, first 100 words, meta description.

**NEVER use generic anchors:** click here, learn more, read this, this page, more info.

**NEVER mark exact-match absence as failure** when exact phrase would create unsafe benefit framing, unsupported certainty, or awkward reader copy.

**Unsafe keyword triggers requiring conversion:** "BAH," "full BAH," "get full BAH," "guaranteed," or similar benefit-certainty phrasing.

**Citable blocks / FAQ answers / metadata / schema-supported text must prioritize:** accuracy, visible support, benefit-safe caveats, platform-safe phrasing, natural reader language.

**Score gate:** Overall < 3.5 = required fixes before publish.

---

## Weak Heading Patterns (Flag and Revise)
Overview, Key Things to Know, Final Thoughts, What to Consider

---

## Audit Report Template

```
# KEYWORD AUDIT REPORT
Page URL: | Pillar: | Primary Keyword:

## 1. Primary Keyword Placement
| Location | Required | Present | Notes |
|---|---|---|---|
| Title Tag | Yes | | |
| H1 | Yes | | |
| First 100 words | Yes | | |
| Meta Description | Yes | | |

## 2. Secondary Keyword Coverage
| Secondary Keyword | Present | Location |
|---|---|---|

## 3. Semantic / LSI Term Coverage
| Term | Present | Notes (Natural / Forced / Missing) |
|---|---|---|

## 4. Subheading Keyword Signal
| Heading | Keyword Signal | Assessment (Strong / Weak / Generic) |
|---|---|---|

## 5. Anchor Text Audit
| Link Target | Anchor Text Used | Assessment (Entity-rich / Generic / Rejected) |
|---|---|---|

## 6. Long-Tail Keyword Coverage
| Long-Tail Keyword | Mapped To | Present |
|---|---|---|

## 7. Extractability / Schema-Safe Keyword Use
| Area | Pressure Present | Assessment (Natural / Forced / Unsafe / N/A) |
|---|---|---|
| Citable response blocks | | |
| FAQ answers | | |
| Metadata | | |
| Schema-supported visible text | | |

## 8. Keyword Audit Score
| Category | Score 1–5 | Notes |
|---|---|---|
| Primary keyword placement | | |
| Secondary keyword coverage | | |
| Semantic / LSI integration | | |
| Subheading signals | | |
| Anchor text quality | | |
| Long-tail coverage | | |
| Extractability/schema-safe use | | |
| **Overall** | **/5.0** | |
```

---

## Fix Log (Trigger: Overall < 3.5)
| Issue | Recommended Fix | Priority (High / Medium / Low) |
|---|---|---|

*Do not rewrite full article. Targeted fixes only. For Citable/FAQ/metadata/schema issues, recommend safer wording. Do not force exact-match.*

---

**Cross-doc dependencies:** vd-pillar-architecture (secondary keywords), vd-keyword-type-map (semantic/LSI terms), vd-ai-extractability (Citable/schema standards), vd-fact-checking (claim verification)