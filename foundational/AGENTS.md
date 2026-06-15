# AGENTS.md — fact-check branch
## Branch Purpose
Sandboxed Stage 3 of the VeteranDegrees content pipeline: claim verification.
This branch audits factual claims against authoritative external sources.
It does NOT draft content, build outlines, or run keyword audits.

## Agent Job
Verify claims. Assign verdicts. Score confidence. Flag revisions and removals.
Single question: Is the content accurate, current, and properly supported?

## System Prompt Location
`orchestration/master-prompt.md`

## Tactical Files Available
- content-copywriting/vd-brand-positioning-v1.0.0.md (for brand-safety audit)
- content-copywriting/vd-language-control-standards-v1.0.0.md (for terminology violations)
- content-copywriting/vd-tone-and-style-v1.0.0.md (for tone violations in claims)
- governance/vd-ai-extractability-v1.0.0.md (for schema claim safety)
- governance/vd-fact-checking-v1.0.0.md (primary verification protocol)

## Hard Constraints
- Be skeptical, source-led. Do not protect the draft.
- Web search is AUTHORIZED at this stage. Use the source hierarchy strictly.
- Do NOT add new content to the draft. Verify existing claims only.
- Do NOT use web research to expand the article or add new sections.
- MANDATORY SHORT-CIRCUIT: If a single primary, high-authority source directly verifies/refutes a claim with 10/10 precision, cease all further searches for that claim.
- Never pad source list with weak sources to hit a count target.
- Assign verdict for every claim: Verified / Debunked / Mixed / Unclear.
- Confidence score must match detailed report score exactly.
- Do not assign score of 10 if any caveat is missing.

## Source Hierarchy (highest to lowest)
1. VA.gov / Benefits.va.gov / VA education pages
2. eCFR / Federal Register
3. Department of Education
4. BLS
5. State licensing boards / Accreditation bodies
6. Official school catalogs, program pages, SCO/registrar pages
7. Primary legal or regulatory sources
8. Reputable academic, policy, or government research
AVOID: blogs, affiliate pages, AI summaries, forum posts, outdated third-party summaries.

## Context Window Rule
Prioritize data from the last 90 days. Ignore context older than 90 days.

## Output Artifact
`fact-check-output.md`
