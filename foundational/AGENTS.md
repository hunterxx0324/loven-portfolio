# AGENTS.md — outline branch
## Branch Purpose
This branch executes Stage 1 of the VeteranDegrees content pipeline: outline generation.

## Agent Job
Generate production-ready content outlines from four required inputs. Do not draft article copy.

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
- Do NOT produce draft article copy
- Do NOT produce a formal Fact-Check Report or Markdown Fact-Check Table
- Do NOT search the web during outline generation
- Do NOT infer missing required inputs — stop and report what is missing
- Do NOT force unsupported angles into the outline
- EAS composite pre-score must project 4.0 or above before handoff
- Keyword Coverage Score below 3.5 requires revision before handoff
- Flag all unsupported items as: Research gap / Source gap

## Required Inputs (all four required — stop if any is missing)
1. page_type — hub / cluster / school
2. assigned_pillar — P1 / P2 / P3 / P4 / P5
3. entity_concept — Primary Topic / Entity Concept (one specific sentence)
4. url_slug — Target URL slug (e.g., /gi-bill-hybrid-programs-california)

## Required Output (14 deliverables)
1. Input Manifest
2. Content Brief
3. Title Tag Options (3; at least 1 must score 4–5)
4. H1 Options (2)
5. Meta Description Draft
6. Opening 150 Words Blueprint
7. Section-by-Section Writer Blueprint
8. FAQ Blueprint
9. Keyword Placement Plan
10. Research Gap and Source Gap Notes
11. Anti-Pattern Warnings
12. EAS Pre-Score Targets
13. Outline Keyword Coverage Report
14. Outline EAS Pre-Score Report

## Context Window Rule
Prioritize data and context from the last 90 days. Ignore context older than 90 days.

## Output Artifact
`outline-output.md` — uploaded as GitHub Actions artifact after each run.
