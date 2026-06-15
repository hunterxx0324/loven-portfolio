# AGENTS.md — content branch
## Branch Purpose
This branch executes Stage 2 of the VeteranDegrees content pipeline: article drafting.
It activates when a production-ready outline from the outline branch is provided as input.

## Agent Job
Draft, audit, and produce high-authority, entity-aligned content for VeteranDegrees.com.
System 2 activates when BOTH an outline AND research/source material are provided.

## System Prompt Location
`orchestration/master-prompt.md`

## Tactical Files Available to Agent
- content-copywriting/vd-brand-positioning-v1.0.0.md
- content-copywriting/vd-language-control-standards-v1.0.0.md
- content-copywriting/vd-tone-and-style-v1.0.0.md
- content-copywriting/vd-pillar-architecture-v1.0.0.md
- content-copywriting/vd-keyword-type-map-v1.0.0.md
- governance/vd-ai-extractability-v1.0.0.md
- governance/vd-page-creation-architecture-v1.0.0.md
- governance/vd-keyword-audit-v1.0.0.md

## Hard Constraints
- Outline controls structure. Research material controls factual content.
- Do NOT add facts not in research material during drafting.
- Do NOT search web during drafting. Web search permitted during fact-check stage only.
- Do NOT use em-dashes in any output.
- Do NOT guarantee eligibility, payment, VA approval, housing allowance, or career outcomes.
- Platform identity: VeteranDegrees.com = guidance/verification platform only.
- Use "housing allowance" not "BAH" in all reader-facing copy.
- Flag all research gaps. Do not invent to fill them.

## Required Outputs (Full Draft Sequence)
1. Main content draft
2. Keyword Audit Report
3. Fact-Check Report (claims flagged — verification in fact-check branch)
4. Markdown Fact-Check Table

## Context Window Rule
Prioritize data and context from the last 90 days. Ignore context older than 90 days.

## Output Artifact
`content-output.md`
