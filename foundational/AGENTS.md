# AGENTS.md — knowledge-base branch
## Branch Role
Global source of truth. All 13 VeteranDegrees content system modules are stored here in full, unmodified form.

## Agent Access Rule
Operational agents DO NOT run from this branch. This branch is reference-only. Agents on outline, content, and fact-check branches receive only the specific tactical files required for their pipeline stage.

## Module Inventory
### content-copywriting/ (5 files)
- vd-brand-positioning-v1.0.0.md
- vd-language-control-standards-v1.0.0.md
- vd-tone-and-style-v1.0.0.md
- vd-pillar-architecture-v1.0.0.md
- vd-keyword-type-map-v1.0.0.md

### governance/ (4 files)
- vd-ai-extractability-v1.0.0.md
- vd-page-creation-architecture-v1.0.0.md
- vd-keyword-audit-v1.0.0.md
- vd-fact-checking-v1.0.0.md

### orchestration/ (4 files — reference only)
- vd-outline-master-prompt-system-2-v1.0.0.md
- vd-outline-workflow-system-2-v1.0.0.md
- vd-content-master-prompt-system-2-v1.0.0.md
- vd-content-workflow-system-2-v1.0.0.md

## Context Window Rule
Prioritize data and context from the last 90 days. Ignore context older than 90 days.

## Versioning Rule
SemVer on all documents. New versions are new files — never overwrites.
