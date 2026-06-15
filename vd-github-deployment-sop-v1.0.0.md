# VeteranDegrees — Agentic Workflow GitHub Deployment SOP
**Version:** 1.0.0  
**Environment:** GitHub Browser UI (github.com) + github.dev (online VS Code)  
**Repository:** https://github.com/hunterxx0324/veterandegrees-case-study  
**Classification:** Sequential Multi-Branch Isolated Architecture

---

## PREFLIGHT CONFIRMATION — READ BEFORE PROCEEDING

**One interpretation I am acting on — confirm or correct before executing Phase 1:**

> The instruction "For the API, I will use the GitHub" is interpreted as the **GitHub Models API** (`https://models.inference.ai.azure.com`), which is GitHub's native AI inference endpoint supporting models like GPT-4o. This is the only GitHub-native API that serves as an LLM endpoint for the trigger scenario described. If you mean a different endpoint, stop here and clarify before proceeding.

**Two prerequisites you must have in hand before touching GitHub:**

1. A GitHub Personal Access Token (PAT) with scopes: `repo` + `models:read`  
   Path to create: github.com → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token

2. All 13 project file contents available to paste (see Deployment Matrix below for which goes where)

---

## DEPLOYMENT MATRIX — FILE ROUTING TABLE

**Module Utilization Policy enforcement:** Four modules are strictly reference-only and deploy ONLY to `knowledge-base`. Their behavioral logic is extracted into each operational branch's `orchestration/master-prompt.md` and `foundational/AGENTS.md` — not deployed raw.

| # | Module File | knowledge-base | outline | content | fact-check | quality-check |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | vd-brand-positioning-v1.0.0.md | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | vd-language-control-standards-v1.0.0.md | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | vd-tone-and-style-v1.0.0.md | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | vd-pillar-architecture-v1.0.0.md | ✓ | ✓ | ✓ | — | — |
| 5 | vd-keyword-type-map-v1.0.0.md | ✓ | ✓ | ✓ | — | — |
| 6 | vd-ai-extractability-v1.0.0.md | ✓ | ✓ | ✓ | ✓ | — |
| 7 | vd-page-creation-architecture-v1.0.0.md | ✓ | ✓ | ✓ | — | — |
| 8 | vd-keyword-audit-v1.0.0.md | ✓ | ✓ | ✓ | — | — |
| 9 | vd-fact-checking-v1.0.0.md | ✓ | — | — | ✓ | — |
| 10 | vd-outline-master-prompt-system-2-v1.0.0.md | ✓ | ⊘ ref | — | — | — |
| 11 | vd-outline-workflow-system-2-v1.0.0.md | ✓ | ⊘ ref | — | — | — |
| 12 | vd-content-master-prompt-system-2-v1.0.0.md | ✓ | — | ⊘ ref | — | — |
| 13 | vd-content-workflow-system-2-v1.0.0.md | ✓ | — | ⊘ ref | — | — |

**Legend:** ✓ = full file deployed | ⊘ ref = behavioral logic extracted into master-prompt.md, raw file goes to knowledge-base only | — = excluded (context contamination risk)

**Routing rationale:**
- `outline`: Needs entity/keyword/structure context. Excludes fact-checking (separate stage) and raw master prompt/workflow modules.
- `content`: Same as outline. Excludes fact-checking. Content master prompt extracted, not deployed raw.
- `fact-check`: Needs claim-verification and brand-safety context only. Excludes keyword/architecture modules irrelevant to verification.
- `quality-check`: Structural scaffold only. Brand, language, tone, and extractability stubs for future module.

---

## DIRECTORY STRUCTURE — ALL FIVE BRANCHES

```
knowledge-base/
├── foundational/
│   ├── .gitignore
│   └── AGENTS.md
├── content-copywriting/
│   ├── vd-brand-positioning-v1.0.0.md
│   ├── vd-language-control-standards-v1.0.0.md
│   ├── vd-tone-and-style-v1.0.0.md
│   ├── vd-pillar-architecture-v1.0.0.md
│   └── vd-keyword-type-map-v1.0.0.md
├── governance/
│   ├── vd-ai-extractability-v1.0.0.md
│   ├── vd-page-creation-architecture-v1.0.0.md
│   ├── vd-keyword-audit-v1.0.0.md
│   └── vd-fact-checking-v1.0.0.md
└── orchestration/
    ├── vd-outline-master-prompt-system-2-v1.0.0.md
    ├── vd-outline-workflow-system-2-v1.0.0.md
    ├── vd-content-master-prompt-system-2-v1.0.0.md
    └── vd-content-workflow-system-2-v1.0.0.md

outline/
├── .github/
│   └── workflows/
│       └── outline-agent.yml              ← GitHub Actions workflow (manual trigger)
├── foundational/
│   ├── .gitignore
│   └── AGENTS.md
├── content-copywriting/
│   ├── vd-brand-positioning-v1.0.0.md
│   ├── vd-language-control-standards-v1.0.0.md
│   ├── vd-tone-and-style-v1.0.0.md
│   ├── vd-pillar-architecture-v1.0.0.md
│   └── vd-keyword-type-map-v1.0.0.md
├── governance/
│   ├── vd-ai-extractability-v1.0.0.md
│   ├── vd-page-creation-architecture-v1.0.0.md
│   └── vd-keyword-audit-v1.0.0.md
└── orchestration/
    └── master-prompt.md                   ← Extracted behavioral rules (NOT raw module)

content/
├── .github/
│   └── workflows/
│       └── content-agent.yml              ← GitHub Actions workflow (manual trigger)
├── foundational/
│   ├── .gitignore
│   └── AGENTS.md
├── content-copywriting/
│   ├── vd-brand-positioning-v1.0.0.md
│   ├── vd-language-control-standards-v1.0.0.md
│   ├── vd-tone-and-style-v1.0.0.md
│   ├── vd-pillar-architecture-v1.0.0.md
│   └── vd-keyword-type-map-v1.0.0.md
├── governance/
│   ├── vd-ai-extractability-v1.0.0.md
│   ├── vd-page-creation-architecture-v1.0.0.md
│   └── vd-keyword-audit-v1.0.0.md
└── orchestration/
    └── master-prompt.md                   ← Extracted behavioral rules (NOT raw module)

fact-check/
├── .github/
│   └── workflows/
│       └── fact-check-agent.yml           ← GitHub Actions workflow (manual trigger)
├── foundational/
│   ├── .gitignore
│   └── AGENTS.md
├── content-copywriting/
│   ├── vd-brand-positioning-v1.0.0.md
│   ├── vd-language-control-standards-v1.0.0.md
│   └── vd-tone-and-style-v1.0.0.md
├── governance/
│   ├── vd-ai-extractability-v1.0.0.md
│   └── vd-fact-checking-v1.0.0.md
└── orchestration/
    └── master-prompt.md                   ← Extracted behavioral rules (NOT raw module)

quality-check/
├── foundational/
│   ├── .gitignore
│   └── AGENTS.md                          ← Structural stub — RESERVED
├── content-copywriting/
│   ├── vd-brand-positioning-v1.0.0.md
│   ├── vd-language-control-standards-v1.0.0.md
│   └── vd-tone-and-style-v1.0.0.md
└── orchestration/
    └── master-prompt.md                   ← PLACEHOLDER — not operational
```

---

## PHASE 0: REPOSITORY PREPARATION

**Goal:** Confirm the existing repo is accessible and establish a baseline before creating any branches.

### Step 0.1 — Verify Repository Access

1. Navigate to: `https://github.com/hunterxx0324/veterandegrees-case-study`
2. Confirm you can see the repository with the existing `README.md` on the `main` branch.
3. Confirm the current default branch is `main` (shown in the branch selector dropdown, top-left of the file tree).
4. Do NOT modify the `main` branch at any point in this SOP. It is untouched.

### Step 0.2 — Add the Repository Secret (GH_MODELS_TOKEN)

You must do this before building the workflow files in Phases 2–4.

1. In your repository, click **Settings** (top navigation bar, rightmost tab).
2. In the left sidebar, click **Secrets and variables** → **Actions**.
3. Click **New repository secret**.
4. Set **Name** to: `GH_MODELS_TOKEN`
5. Set **Secret** to: your GitHub Personal Access Token (PAT) with `repo` + `models:read` scopes.
6. Click **Add secret**.
7. Confirm the secret now appears listed under "Repository secrets" as `GH_MODELS_TOKEN`.

> ⚠️ GITHUB_TOKEN (the auto-generated token from Actions) does NOT have GitHub Models access by default. You must use the PAT stored here.

---

## PHASE 1: BUILD THE knowledge-base BRANCH

**Goal:** Create the global source of truth branch holding all 13 modules in their full, unmodified form.

> This branch is READ-ONLY for all operational agents. No workflow YAML is deployed here. Nothing runs from this branch.

### Step 1.1 — Create the knowledge-base Branch

1. Navigate to: `https://github.com/hunterxx0324/veterandegrees-case-study`
2. Click the branch selector dropdown (currently shows `main`).
3. In the text field that appears, type exactly: `knowledge-base`
4. Click **Create branch: knowledge-base from 'main'**
5. Confirm the branch selector now shows `knowledge-base`.

### Step 1.2 — Create foundational/.gitignore

1. While on the `knowledge-base` branch, click **Add file** → **Create new file**.
2. In the filename field, type: `foundational/.gitignore`
   - The `/` after `foundational` automatically creates the directory.
3. Paste the following content into the editor:

```
# Runtime outputs — never commit agent outputs to knowledge-base
*.json
*.log
*-output.md
agent-output/
```

4. Scroll to **Commit new file**.
5. Select **Commit directly to the `knowledge-base` branch**.
6. Click **Commit new file**.

### Step 1.3 — Create foundational/AGENTS.md

1. Click **Add file** → **Create new file**.
2. Filename: `foundational/AGENTS.md`
3. Paste:

```markdown
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
```

4. Commit directly to `knowledge-base`.

### Step 1.4 — Create content-copywriting/ Files (5 files)

Repeat the following sub-steps for each of the 5 files listed. Do them one at a time.

**File 1 of 5:**
1. Click **Add file** → **Create new file**.
2. Filename: `content-copywriting/vd-brand-positioning-v1.0.0.md`
3. Paste the full, unmodified content of `vd-brand-positioning-v1.0.0.md`.
4. Commit directly to `knowledge-base`.

**File 2 of 5:**
1. Filename: `content-copywriting/vd-language-control-standards-v1.0.0.md`
2. Paste full content of `vd-language-control-standards-v1.0.0.md`.
3. Commit directly to `knowledge-base`.

**File 3 of 5:**
1. Filename: `content-copywriting/vd-tone-and-style-v1.0.0.md`
2. Paste full content of `vd-tone-and-style-v1.0.0.md`.
3. Commit directly to `knowledge-base`.

**File 4 of 5:**
1. Filename: `content-copywriting/vd-pillar-architecture-v1.0.0.md`
2. Paste full content of `vd-pillar-architecture-v1.0.0.md`.
3. Commit directly to `knowledge-base`.

**File 5 of 5:**
1. Filename: `content-copywriting/vd-keyword-type-map-v1.0.0.md`
2. Paste full content of `vd-keyword-type-map-v1.0.0.md`.
3. Commit directly to `knowledge-base`.

### Step 1.5 — Create governance/ Files (4 files)

**File 1 of 4:**
1. Filename: `governance/vd-ai-extractability-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 2 of 4:**
1. Filename: `governance/vd-page-creation-architecture-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 3 of 4:**
1. Filename: `governance/vd-keyword-audit-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 4 of 4:**
1. Filename: `governance/vd-fact-checking-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

### Step 1.6 — Create orchestration/ Files (4 files — reference only)

> These are the raw master prompt and workflow modules. They deploy to knowledge-base ONLY. They inform the extracted master-prompt.md files built in Phases 2–4 but are NOT deployed operationally.

**File 1 of 4:**
1. Filename: `orchestration/vd-outline-master-prompt-system-2-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 2 of 4:**
1. Filename: `orchestration/vd-outline-workflow-system-2-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 3 of 4:**
1. Filename: `orchestration/vd-content-master-prompt-system-2-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

**File 4 of 4:**
1. Filename: `orchestration/vd-content-workflow-system-2-v1.0.0.md`
2. Paste full content. Commit to `knowledge-base`.

### Step 1.7 — Verify knowledge-base File Count

1. Navigate to the `knowledge-base` branch root.
2. Confirm the following directory structure is visible:
   - `content-copywriting/` — 5 files
   - `foundational/` — 2 files (.gitignore, AGENTS.md)
   - `governance/` — 4 files
   - `orchestration/` — 4 files
   - Total: **15 files** (13 modules + .gitignore + AGENTS.md)
3. Also confirm the `README.md` inherited from `main` is present at root.

> ✅ Phase 1 complete when all 15 files are confirmed present.

---

## PHASE 2: BUILD THE outline BRANCH

**Goal:** Create the outline pipeline branch with its isolated runtime layer, 8 tactical modules (no raw master prompt/workflow), an extracted master-prompt.md, and the GitHub Actions workflow YAML for manual trigger.

### Step 2.1 — Create the outline Branch

1. Navigate to: `https://github.com/hunterxx0324/veterandegrees-case-study`
2. Click the branch selector → type `outline` → click **Create branch: outline from 'main'**.
3. Confirm branch selector shows `outline`.

### Step 2.2 — Create foundational/.gitignore

1. **Add file** → **Create new file**.
2. Filename: `foundational/.gitignore`
3. Content:

```
# Outline branch — exclude agent runtime outputs from source control
agent-output/
outline-output.md
*.log
*.json
__pycache__/
```

4. Commit directly to `outline`.

### Step 2.3 — Create foundational/AGENTS.md

1. Filename: `foundational/AGENTS.md`
2. Content:

```markdown
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
```

3. Commit directly to `outline`.

### Step 2.4 — Create content-copywriting/ Files (5 files)

Identical content to knowledge-base. Deploy them to the `outline` branch under the same directory path.

**File 1:** `content-copywriting/vd-brand-positioning-v1.0.0.md` → paste full content → commit to `outline`.  
**File 2:** `content-copywriting/vd-language-control-standards-v1.0.0.md` → paste → commit.  
**File 3:** `content-copywriting/vd-tone-and-style-v1.0.0.md` → paste → commit.  
**File 4:** `content-copywriting/vd-pillar-architecture-v1.0.0.md` → paste → commit.  
**File 5:** `content-copywriting/vd-keyword-type-map-v1.0.0.md` → paste → commit.

### Step 2.5 — Create governance/ Files (3 files — no fact-checking)

**File 1:** `governance/vd-ai-extractability-v1.0.0.md` → paste → commit to `outline`.  
**File 2:** `governance/vd-page-creation-architecture-v1.0.0.md` → paste → commit.  
**File 3:** `governance/vd-keyword-audit-v1.0.0.md` → paste → commit.

> ⚠️ Do NOT add vd-fact-checking-v1.0.0.md to this branch. That module belongs to the fact-check branch only.

### Step 2.6 — Create orchestration/master-prompt.md (Extracted — NOT raw module)

> This is the behavioral extraction from vd-outline-master-prompt-system-2-v1.0.0.md. It is NOT the raw file. It is formatted as a clean LLM system prompt. The raw file lives only in knowledge-base/orchestration/.

1. Filename: `orchestration/master-prompt.md`
2. Content:

```markdown
# VeteranDegrees — Outline Agent System Prompt
**Role:** Senior Content Architect, VeteranDegrees.com
**Function:** Build production-ready content outlines. Do not draft articles.

---

## PLATFORM IDENTITY (HARD — zero exceptions)
VeteranDegrees.com = guidance and verification platform. NOT a school, university, degree-grantor, enrollment office, benefits administrator, or VA decision-maker.
- Use: "programs listed on VeteranDegrees.com" / "schools found on VeteranDegrees.com"
- Never use: "our programs" / "our schools" / "enroll through" / "apply to VeteranDegrees.com"

---

## ACTIVATION — FOUR REQUIRED INPUTS
Do not proceed if any input is missing. State exactly what is missing. Do not infer.

1. page_type (hub / cluster / school)
2. assigned_pillar (P1–P5)
3. entity_concept (one specific sentence — the authority concept for this page)
4. url_slug (exact target URL)

---

## FIVE FIXED PILLARS (LOCKED ORDER)
P1: Hybrid/Low-Residency Programs
P2: BAH/MHA Strategies (use "housing allowance" in all reader-facing copy)
P3: VA Compliance & Verification
P4: GI Bill Benefits Optimization
P5: Career Outcomes Enabled by Hybrid Programs

---

## HARD RULES (zero exceptions)
1. Frame VeteranDegrees.com as a guidance and verification platform only.
2. Use "housing allowance" as the standard reader-facing term. Allow "BAH" only in keyword, search, metadata, quoted, or terminology-explainer contexts.
3. Never guarantee eligibility, payment, VA approval, full housing allowance, enrollment outcome, job outcome, or career success.
4. Do not frame veterans as gaming, exploiting, hacking, or chasing benefits.
5. Do not use em-dashes.
6. Do not invent missing facts, links, school details, statistics, or source claims.
7. Do not search the web. Outline is bounded by the reference files in this branch only.
8. Do not produce article copy. Outline only.
9. Use "Not provided / Not applicable / Needs confirmation / Research gap / Source gap" where appropriate.
10. EAS composite pre-score must project 4.0+ before flagging as ready for writer handoff.
11. If any EAS dimension projects below 4.0, revise the outline before completing the output.
12. Keyword Coverage Score below 3.5 requires revision before completing.
13. Avoid all banned words in vd-language-control-standards: delve, realm, harness, unlock, tapestry, paradigm, cutting-edge, revolutionize, landscape, intricate, showcasing, crucial, pivotal, surpass, meticulously, vibrant, unparalleled, underscore, leverage, synergy, innovative, game-changer, seamless, optimize, robust, empower, streamline, and all others listed in the language control standards file.
14. Avoid banned rhetorical formulas: "In a World Where," "Most People vs. The Few Who," "Stop X. Start Y.," "Here's the Truth Nobody Tells You," and all others in the language control standards file.
15. Do not use generic heading patterns: Overview, Key Things to Know, Final Thoughts, What to Consider.

---

## EVIDENCE LANGUAGE (HARD)
Never use: "research confirms," "studies show," "evidence proves," "the literature agrees"
Use instead: "suggests," "tends to," "available evidence indicates," "findings from [source] suggest"

---

## REQUIRED OUTPUT — 14 DELIVERABLES (in this order)

**Deliverable 1: Input Manifest**
Table confirming all four required inputs: Provided / Missing / Notes.
Stop here if any required input is Missing.

**Deliverable 2: Content Brief**
Table with fields: Page URL, Page Type, Assigned Pillar, Primary Entity Concept, Target Audience, Title Tag (selected), Title Tag Score, H1 (selected), Primary Topic/Question, Opening 150 Words Key Points, AI Extractability Anchor, Research-Supported Claim Targets, Research Gaps, Internal Links Outbound, Internal Links Inbound, Anti-Patterns to Avoid, Assigned Writer, Target Publish Date. Mark all unknowns as "Not provided."

**Deliverable 3: Title Tag Options (3 options)**
- Each under 60 characters
- Brand suffix format: [Topic] | VeteranDegrees
- Score each 1–5 per rubric: 5=Precise, 4=Correct, 3=Generic, 2=Diluted, 1=Rejected
- At least 1 must score 4–5. If none do, revise before proceeding.

**Deliverable 4: H1 Options (2 options)**
- Same topic as selected title tag
- Not verbatim repeat of title tag
- Veteran-reader first, keyword second
- No provider language. No outcome guarantees.

**Deliverable 5: Meta Description Draft**
- Primary keyword/concept naturally included
- Platform identity signal present
- No benefit guarantees
- Under 155 characters
- Use "housing allowance" unless search context requires otherwise

**Deliverable 6: Opening 150 Words Blueprint**
Writing spec — do NOT write the opening paragraph. Specify:
[ ] 1. What this page is about
[ ] 2. Who this page is for
[ ] 3. What the reader can do with this information
[ ] 4. VeteranDegrees.com's role as a guidance and verification platform
[ ] 5. Hybrid program connection (when relevant)
Include: Primary keyword placement within first 100 words, required caveats, research boundary.

**Deliverable 7: Section-by-Section Writer Blueprint**
For each section provide: Suggested H2, Word Count Target, Pillar Function, Keyword Signal, AI Extractability requirement (Yes/No + spec), Internal Link (target + anchor text), Hybrid Anchor Required (Yes/No), Research Support, Research Gap/Source Gap, WHAT TO WRITE (min 3 sentences), WHY THIS SECTION EXISTS (1–2 sentences), ANTI-PATTERNS TO AVOID.

**Deliverable 8: FAQ Blueprint**
For each FAQ entry: Q (search-style), Maps to long-tail keyword, Answer must include (one-sentence spec), Research boundary, AI anchor (Yes/No). If FAQ is not appropriate, state why.

**Deliverable 9: Keyword Placement Plan**
Table: Keyword | Type | Designated Placement | Section. Types: Primary, Secondary, Semantic, Long-tail, Anchor. Flag any Pillar Architecture keywords with no natural research-supported placement.

**Deliverable 10: Research Gap and Source Gap Notes**
Table: Gap Type | Missing/Unsupported Item | Why It Matters | Recommended Handling.

**Deliverable 11: Anti-Pattern Warnings**
Page-specific only. Cover: platform identity drift, benefit guarantee language, BAH overuse, forced hybrid framing, unsupported seed claims, generic veteran content, keyword stuffing, vague evidence language, invented examples, provider-style language.

**Deliverable 12: EAS Pre-Score Targets**
Table: EAS Dimension | Target Score | Outline Decision Supporting Target.
Dimensions: Title Tag | H1 Alignment | Opening 150 Words | Body Content Alignment | Hub-Cluster Structure | AI Extractability.
Composite must be 4.0+.

**Deliverable 13: Outline Keyword Coverage Report**
Sections: Primary Keyword Placement | Secondary Keyword Coverage | Semantic/LSI Term Coverage | Subheading Keyword Signal | Anchor Text Plan | Long-Tail Keyword Coverage | Outline Keyword Coverage Score (1–5 per category + Overall). Overall below 3.5 = revise before handoff.

**Deliverable 14: Outline EAS Pre-Score Report**
Table: Dimension | Projected Score 1–5 | Outline Decision. Composite EAS Projection. If any dimension below 4.0: list in "Dimensions Below 4.0" table with Required Outline Revision. Composite 4.0+ = ready for writer handoff.

---

## CONTEXT WINDOW RULE
Prioritize data from the last 90 days. Ignore context older than 90 days.
```

3. Commit directly to `outline`.

### Step 2.7 — Create .github/workflows/outline-agent.yml

> This is the GitHub Actions workflow file. It must be in `.github/workflows/` on the `outline` branch. GitHub Actions will discover and make this workflow available when you select the `outline` branch in the Actions tab.

1. **Add file** → **Create new file**.
2. Filename: `.github/workflows/outline-agent.yml`

   > Important: Type exactly `.github/workflows/outline-agent.yml` in the filename field. The leading `.` is required. GitHub will create the hidden directory automatically.

3. Paste the following content exactly:

```yaml
name: "VD — Outline Agent (Manual Trigger)"

on:
  workflow_dispatch:
    inputs:
      page_type:
        description: "Page Type"
        required: true
        type: choice
        options:
          - hub
          - cluster
          - school
      assigned_pillar:
        description: "Assigned Pillar (P1–P5)"
        required: true
        type: choice
        options:
          - P1
          - P2
          - P3
          - P4
          - P5
      entity_concept:
        description: "Primary Topic / Entity Concept (one specific sentence)"
        required: true
        type: string
      url_slug:
        description: "Target URL Slug (e.g., /gi-bill-hybrid-programs-california)"
        required: true
        type: string

jobs:
  outline-agent:
    name: "Run Outline Agent"
    runs-on: ubuntu-latest

    steps:
      - name: "Checkout outline branch"
        uses: actions/checkout@v4
        with:
          ref: outline

      - name: "Verify master prompt file exists"
        run: |
          if [ ! -f "orchestration/master-prompt.md" ]; then
            echo "ERROR: orchestration/master-prompt.md not found on outline branch."
            exit 1
          fi
          echo "master-prompt.md confirmed present."
          wc -c orchestration/master-prompt.md

      - name: "Call GitHub Models API and save output"
        env:
          GH_MODELS_TOKEN: ${{ secrets.GH_MODELS_TOKEN }}
          PAGE_TYPE: ${{ github.event.inputs.page_type }}
          ASSIGNED_PILLAR: ${{ github.event.inputs.assigned_pillar }}
          ENTITY_CONCEPT: ${{ github.event.inputs.entity_concept }}
          URL_SLUG: ${{ github.event.inputs.url_slug }}
        run: |
          python3 << 'PYEOF'
          import json
          import os
          import urllib.request
          import urllib.error

          # Read system prompt from branch file
          with open("orchestration/master-prompt.md", "r", encoding="utf-8") as f:
              system_prompt = f.read()

          # Build inputs from environment variables
          page_type      = os.environ.get("PAGE_TYPE", "").strip()
          assigned_pillar = os.environ.get("ASSIGNED_PILLAR", "").strip()
          entity_concept  = os.environ.get("ENTITY_CONCEPT", "").strip()
          url_slug        = os.environ.get("URL_SLUG", "").strip()
          token           = os.environ.get("GH_MODELS_TOKEN", "").strip()

          # Validate all four required inputs
          missing = []
          if not page_type:      missing.append("page_type")
          if not assigned_pillar: missing.append("assigned_pillar")
          if not entity_concept:  missing.append("entity_concept")
          if not url_slug:        missing.append("url_slug")

          if missing:
              print(f"ERROR: Missing required inputs: {', '.join(missing)}")
              exit(1)

          user_message = f"""Page Type: {page_type}
Assigned Pillar: {assigned_pillar}
Primary Topic / Entity Concept: {entity_concept}
Target URL Slug: {url_slug}

Generate all 14 required deliverables per your system instructions."""

          payload = {
              "model": "gpt-4o",
              "messages": [
                  {"role": "system", "content": system_prompt},
                  {"role": "user",   "content": user_message}
              ],
              "max_tokens": 4000,
              "temperature": 0.3
          }

          api_url = "https://models.inference.ai.azure.com/chat/completions"
          req = urllib.request.Request(
              api_url,
              data=json.dumps(payload).encode("utf-8"),
              headers={
                  "Authorization": f"Bearer {token}",
                  "Content-Type": "application/json"
              },
              method="POST"
          )

          try:
              with urllib.request.urlopen(req, timeout=120) as resp:
                  raw = resp.read()
                  data = json.loads(raw)
          except urllib.error.HTTPError as e:
              error_body = e.read().decode("utf-8", errors="replace")
              print(f"HTTP ERROR {e.code}: {error_body}")
              exit(1)
          except Exception as e:
              print(f"REQUEST FAILED: {e}")
              exit(1)

          if "choices" not in data or not data["choices"]:
              print(f"UNEXPECTED API RESPONSE: {json.dumps(data, indent=2)}")
              exit(1)

          content = data["choices"][0]["message"]["content"]

          # Add run metadata header to output
          header = f"""---
# Outline Agent Output
**Run:** ${{ github.run_number }}
**Branch:** outline
**Triggered by:** ${{ github.actor }}
**Page Type:** {page_type}
**Assigned Pillar:** {assigned_pillar}
**Entity Concept:** {entity_concept}
**URL Slug:** {url_slug}
---

"""
          final_output = header + content

          with open("outline-output.md", "w", encoding="utf-8") as f:
              f.write(final_output)

          print(f"Output saved. Character count: {len(final_output)}")
          print("First 300 characters of output:")
          print(final_output[:300])

          PYEOF

      - name: "Upload outline output as artifact"
        uses: actions/upload-artifact@v4
        with:
          name: "outline-output-run-${{ github.run_number }}"
          path: outline-output.md
          retention-days: 30

      - name: "Print output to workflow log"
        run: |
          echo "========== OUTLINE AGENT OUTPUT =========="
          cat outline-output.md
          echo "========== END OF OUTPUT =========="
```

4. Commit directly to `outline`.

### Step 2.8 — Verify outline Branch Structure

Navigate to the `outline` branch root and confirm:
- `.github/workflows/outline-agent.yml` ✓
- `foundational/.gitignore` ✓
- `foundational/AGENTS.md` ✓
- `content-copywriting/` — 5 files ✓
- `governance/` — 3 files (no vd-fact-checking) ✓
- `orchestration/master-prompt.md` ✓
- Total: **12 files** + README.md inherited from main

> ✅ Phase 2 complete when all 12 files are confirmed present.

---

## PHASE 3: BUILD THE content BRANCH

**Goal:** Create the content drafting pipeline branch with its isolated runtime layer, 8 tactical modules, and an extracted content master-prompt.md. The workflow YAML pattern is identical to outline except it reads from the content branch and outputs a content draft.

### Step 3.1 — Create the content Branch

1. Click branch selector → type `content` → **Create branch: content from 'main'**.

### Step 3.2 — Create foundational/.gitignore

1. Filename: `foundational/.gitignore`
2. Content:

```
# Content branch — exclude agent runtime outputs
agent-output/
content-output.md
draft-output.md
*.log
*.json
__pycache__/
```

3. Commit to `content`.

### Step 3.3 — Create foundational/AGENTS.md

1. Filename: `foundational/AGENTS.md`
2. Content:

```markdown
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
```

3. Commit to `content`.

### Step 3.4 — Create content-copywriting/ Files (5 files)

Same 5 files as outline branch. Paste identical content. Commit each to `content`.

**File 1:** `content-copywriting/vd-brand-positioning-v1.0.0.md` → commit to `content`.  
**File 2:** `content-copywriting/vd-language-control-standards-v1.0.0.md` → commit.  
**File 3:** `content-copywriting/vd-tone-and-style-v1.0.0.md` → commit.  
**File 4:** `content-copywriting/vd-pillar-architecture-v1.0.0.md` → commit.  
**File 5:** `content-copywriting/vd-keyword-type-map-v1.0.0.md` → commit.

### Step 3.5 — Create governance/ Files (3 files)

**File 1:** `governance/vd-ai-extractability-v1.0.0.md` → commit to `content`.  
**File 2:** `governance/vd-page-creation-architecture-v1.0.0.md` → commit.  
**File 3:** `governance/vd-keyword-audit-v1.0.0.md` → commit.

> ⚠️ Do NOT add vd-fact-checking to this branch.

### Step 3.6 — Create orchestration/master-prompt.md

1. Filename: `orchestration/master-prompt.md`
2. Content:

```markdown
# VeteranDegrees — Content Drafting Agent System Prompt
**Role:** Senior Content Strategist, VeteranDegrees.com
**Function:** Draft high-authority, entity-aligned content. System 2 activates when both an outline AND research/source material are provided.

---

## PLATFORM IDENTITY (HARD — zero exceptions)
VeteranDegrees.com = guidance and verification platform. Not a school.
- Use: "programs listed on VeteranDegrees.com" / "schools found on VeteranDegrees.com"
- Never: "our programs" / "our schools" / "enroll through" / "VeteranDegrees.com offers education"

---

## SOURCE CONTROL (HARD)
Outline controls: structure, headings, section order, tables, FAQs, word counts, section intent.
Research material controls: all factual drafting content.

Never add during drafting: facts, statistics, school claims, VA policy claims, salary data, career claims, or schema-supported facts unless supported by the provided research material.

Research gap handling: mark as "Research gap: The provided research does not include enough support to make this claim safely." Do not invent to fill gaps.

Web search: PROHIBITED during drafting. Permitted only during Fact-Check Report stage, and only to verify existing claims.

---

## CORE NON-NEGOTIABLES
1. Frame VeteranDegrees.com as guidance/verification platform only. Never as a school.
2. Use "listed on VeteranDegrees.com" or "found on VeteranDegrees.com."
3. Connect relevant topics to hybrid programs and housing allowance strategy.
4. Use "housing allowance," not "BAH," unless quoting, explaining terminology, or keyword context.
5. Never guarantee eligibility, payment, VA approval, full housing allowance, enrollment, job, or career outcome.
6. Do not frame veterans as gaming, exploiting, or chasing benefits.
7. Remove all banned words from vd-language-control-standards.
8. No em-dashes.
9. No invented facts, examples, statistics, program details, or schema-supported facts.
10. Write to the concept, not keyword density.
11. Do not use structured data, metadata, FAQ answers, or Citable responses to add hidden or stronger claims.

---

## OPENING — FIRST 150 WORDS (HARD)
Must answer all five:
1. What is this page?
2. Who is it for?
3. What can the reader do with it?
4. What is VeteranDegrees.com's role?
5. How does the topic connect to hybrid programs, housing allowance, VA verification, GI Bill, or career outcomes (when relevant)?

---

## CITABLE RESPONSE BLOCKS (HARD)
Label: `Citable response:`
Required for each major section with distinct answer, definition, comparison, eligibility rule, process, or decision point.
Must be: visible, self-contained, reader-useful, evidence-calibrated, benefit-safe, platform-safe.
Length: 40–90 words standard.
Never: unsupported claims, hidden caveats, exact-match keyword forcing, implied guaranteed outcomes.

---

## EVIDENCE LANGUAGE (HARD)
Never: "research confirms," "studies show," "evidence proves," "the literature agrees"
Use: "suggests," "tends to," "available evidence indicates," "findings from [source] suggest"

---

## BANNED STRUCTURAL PATTERNS
- Generic catch-all endings: "that variety is useful"
- Three-beat rhythm: "fast, simple, powerful"
- Question-answer crutch: "The secret? Consistency."
- Polite openers: "I hope this email finds you well."

---

## BANNED RHETORICAL FORMULAS (all prohibited)
1. "In a World Where" drama
2. "Most People vs. The Few Who" split
3. "Stop X. Start Y." switch
4. "Not This. Not That. But This." triple
5. "If You're Not Doing X, You're Already Behind" FOMO
6. "The Real Work Is..." reveal
7. "You Don't Need More X. You Need Y." smack
8. "It's Never Been Easier/Harder" paradox
9. "Here's the Truth / Nobody Tells You" fake reveal

---

## FULL DRAFT OUTPUT SEQUENCE
1. Main content draft (follows outline structure exactly)
2. Keyword Audit Report (per vd-keyword-audit standards)
3. Fact-Check Report (claims flagged — verification handled by fact-check branch)
4. Markdown Fact-Check Table

Keyword audit and fact-checking are separate sequential documents. Never merged.

---

## COMPLIANCE PASSES (POST-DRAFT, IN ORDER)
C1 — Brand Positioning: platform identity, audience framing, housing allowance caution
C2 — Language Control: required terms, banned terms, no fake urgency
C3 — Tone and Style: practical, respectful, plainspoken, varied rhythm, no em-dashes
C4 — Entity/Extractability/Structured Data: Citable blocks, schema-ready facts, entity clarity
C5 — Formatting: heading hierarchy, tables, bullet/numbered lists, FAQ format
C6 — Internal Linking: entity-rich anchors only, no generic anchors
C7 — Evidence Awareness: flag risky claims before fact-check stage

---

## CONTEXT WINDOW RULE
Prioritize data from the last 90 days. Ignore context older than 90 days.
```

3. Commit to `content`.

### Step 3.7 — Create .github/workflows/content-agent.yml

1. Filename: `.github/workflows/content-agent.yml`
2. Content (note: the inputs differ from outline — content receives outline text + research material):

```yaml
name: "VD — Content Agent (Manual Trigger)"

on:
  workflow_dispatch:
    inputs:
      page_type:
        description: "Page Type"
        required: true
        type: choice
        options:
          - hub
          - cluster
          - school
      assigned_pillar:
        description: "Assigned Pillar (P1–P5)"
        required: true
        type: choice
        options:
          - P1
          - P2
          - P3
          - P4
          - P5
      entity_concept:
        description: "Primary Topic / Entity Concept (one specific sentence)"
        required: true
        type: string
      url_slug:
        description: "Target URL Slug (e.g., /gi-bill-hybrid-programs-california)"
        required: true
        type: string

jobs:
  content-agent:
    name: "Run Content Drafting Agent"
    runs-on: ubuntu-latest

    steps:
      - name: "Checkout content branch"
        uses: actions/checkout@v4
        with:
          ref: content

      - name: "Verify master prompt file exists"
        run: |
          if [ ! -f "orchestration/master-prompt.md" ]; then
            echo "ERROR: orchestration/master-prompt.md not found on content branch."
            exit 1
          fi
          echo "master-prompt.md confirmed present."

      - name: "Call GitHub Models API and save output"
        env:
          GH_MODELS_TOKEN: ${{ secrets.GH_MODELS_TOKEN }}
          PAGE_TYPE: ${{ github.event.inputs.page_type }}
          ASSIGNED_PILLAR: ${{ github.event.inputs.assigned_pillar }}
          ENTITY_CONCEPT: ${{ github.event.inputs.entity_concept }}
          URL_SLUG: ${{ github.event.inputs.url_slug }}
        run: |
          python3 << 'PYEOF'
          import json
          import os
          import urllib.request
          import urllib.error

          with open("orchestration/master-prompt.md", "r", encoding="utf-8") as f:
              system_prompt = f.read()

          page_type       = os.environ.get("PAGE_TYPE", "").strip()
          assigned_pillar = os.environ.get("ASSIGNED_PILLAR", "").strip()
          entity_concept  = os.environ.get("ENTITY_CONCEPT", "").strip()
          url_slug        = os.environ.get("URL_SLUG", "").strip()
          token           = os.environ.get("GH_MODELS_TOKEN", "").strip()

          missing = []
          if not page_type:       missing.append("page_type")
          if not assigned_pillar: missing.append("assigned_pillar")
          if not entity_concept:  missing.append("entity_concept")
          if not url_slug:        missing.append("url_slug")

          if missing:
              print(f"ERROR: Missing required inputs: {', '.join(missing)}")
              exit(1)

          user_message = f"""Page Type: {page_type}
Assigned Pillar: {assigned_pillar}
Primary Topic / Entity Concept: {entity_concept}
Target URL Slug: {url_slug}

Generate the full content draft per your system instructions, including all compliance passes and the keyword audit report."""

          payload = {
              "model": "gpt-4o",
              "messages": [
                  {"role": "system", "content": system_prompt},
                  {"role": "user",   "content": user_message}
              ],
              "max_tokens": 4000,
              "temperature": 0.3
          }

          req = urllib.request.Request(
              "https://models.inference.ai.azure.com/chat/completions",
              data=json.dumps(payload).encode("utf-8"),
              headers={
                  "Authorization": f"Bearer {token}",
                  "Content-Type": "application/json"
              },
              method="POST"
          )

          try:
              with urllib.request.urlopen(req, timeout=120) as resp:
                  data = json.loads(resp.read())
          except urllib.error.HTTPError as e:
              print(f"HTTP ERROR {e.code}: {e.read().decode('utf-8', errors='replace')}")
              exit(1)
          except Exception as e:
              print(f"REQUEST FAILED: {e}")
              exit(1)

          if "choices" not in data or not data["choices"]:
              print(f"UNEXPECTED API RESPONSE: {json.dumps(data, indent=2)}")
              exit(1)

          content_output = data["choices"][0]["message"]["content"]
          header = f"""---
# Content Agent Output
**Run:** ${{ github.run_number }}
**Branch:** content
**Page Type:** {page_type}
**Assigned Pillar:** {assigned_pillar}
**Entity Concept:** {entity_concept}
**URL Slug:** {url_slug}
---

"""
          final_output = header + content_output

          with open("content-output.md", "w", encoding="utf-8") as f:
              f.write(final_output)

          print(f"Output saved. Character count: {len(final_output)}")

          PYEOF

      - name: "Upload content output as artifact"
        uses: actions/upload-artifact@v4
        with:
          name: "content-output-run-${{ github.run_number }}"
          path: content-output.md
          retention-days: 30

      - name: "Print output to workflow log"
        run: |
          echo "========== CONTENT AGENT OUTPUT =========="
          cat content-output.md
          echo "========== END OF OUTPUT =========="
```

3. Commit to `content`.

### Step 3.8 — Verify content Branch Structure

Confirm:
- `.github/workflows/content-agent.yml` ✓
- `foundational/.gitignore` ✓
- `foundational/AGENTS.md` ✓
- `content-copywriting/` — 5 files ✓
- `governance/` — 3 files ✓
- `orchestration/master-prompt.md` ✓

> ✅ Phase 3 complete when all 12 files are confirmed.

---

## PHASE 4: BUILD THE fact-check BRANCH

**Goal:** Sandboxed verification environment. Receives only claim-verification and brand-safety modules. No keyword or architecture modules.

### Step 4.1 — Create the fact-check Branch

1. Click branch selector → type `fact-check` → **Create branch: fact-check from 'main'**.

### Step 4.2 — Create foundational/.gitignore

1. Filename: `foundational/.gitignore`
2. Content:

```
# Fact-check branch — exclude agent runtime outputs
fact-check-output.md
agent-output/
*.log
*.json
__pycache__/
```

3. Commit to `fact-check`.

### Step 4.3 — Create foundational/AGENTS.md

1. Filename: `foundational/AGENTS.md`
2. Content:

```markdown
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
```

3. Commit to `fact-check`.

### Step 4.4 — Create content-copywriting/ Files (3 files only)

**File 1:** `content-copywriting/vd-brand-positioning-v1.0.0.md` → commit to `fact-check`.  
**File 2:** `content-copywriting/vd-language-control-standards-v1.0.0.md` → commit.  
**File 3:** `content-copywriting/vd-tone-and-style-v1.0.0.md` → commit.

> ⚠️ Do NOT add vd-pillar-architecture or vd-keyword-type-map. These are irrelevant to claim verification and would contaminate the fact-check agent's context.

### Step 4.5 — Create governance/ Files (2 files only)

**File 1:** `governance/vd-ai-extractability-v1.0.0.md` → commit to `fact-check`.  
**File 2:** `governance/vd-fact-checking-v1.0.0.md` → commit.

### Step 4.6 — Create orchestration/master-prompt.md

1. Filename: `orchestration/master-prompt.md`
2. Content:

```markdown
# VeteranDegrees — Fact-Check Agent System Prompt
**Role:** Fact-Checker / Claims Auditor, VeteranDegrees.com
**Function:** Audit factual claims against authoritative external sources. Assign verdicts and confidence scores.

---

## SINGLE CONTROLLING QUESTION
Is the content accurate, current, and properly supported?
Keyword placement is out of scope. Do not audit keywords.

---

## TARGET ERRORS
Hallucinated claims | Outdated benefit guidance | Unsupported school/program statements | Overconfident VA policy | Inaccurate housing allowance claims | Weak career outcome claims | True-but-missing-caveat claims.

---

## COST CONTROL — TIERED TRIAGE (run BEFORE web searches)

**Tier 1 — Internal Workspace Truths** (brand settings, platform identity claims)
→ Validate ONLY against local reference files. Do NOT launch web searches.

**Tier 2 — Industry Common Knowledge** (general GI Bill definitions, well-known rules)
→ Use parametric knowledge. If confidence is 10/10 internally, bypass web search.

**Tier 3 — High-Risk Variable Facts** (2026 housing allowance rates, changing policy, school status, WEAMS approval, career outcome statistics)
→ Run targeted web searches. Batch all Tier 3 targets before searching. Use source hierarchy strictly.

---

## WEB SEARCH AUTHORIZATION
Web search is AUTHORIZED at this stage. Use it only to verify existing claims.
Do NOT use web research to add new sections, expand the article, or introduce new claims.

---

## SOURCE HIERARCHY (use in order)
1. VA.gov / Benefits.va.gov / VA education pages
2. eCFR / Federal Register
3. Department of Education
4. BLS
5. State licensing boards / Accreditation bodies
6. Official school catalogs, program pages, SCO/registrar pages
7. Primary legal or regulatory sources
8. Reputable academic, policy, or government research
AVOID: blogs, affiliate pages, AI summaries, forum posts, search snippets without sourcing.

---

## VERIFICATION STANDARD
- Target: 2 independent sources per claim where possible.
- MANDATORY SHORT-CIRCUIT: If a single primary, high-authority source directly verifies/refutes the claim with 10/10 precision, cease all further searches for that claim. Do not pad with weak sources.

---

## CLAIM TYPES
Policy | Eligibility | Payment | Program | Career | Date | Statistic | Comparison | Causal | Quote/Source | Other

---

## ADVERSARIAL REVIEW (ask before assigning verdict)
- Did the source actually say this?
- Is draft wording broader than evidence supports?
- Is the claim outdated?
- Is a caveat missing?
- Could the answer vary by school, program, chapter, modality, campus, enrollment status, or date?
- Would a reader make a financial or enrollment decision based on this wording?

---

## VERDICT OPTIONS
✅ Verified — Supported by authoritative, relevant evidence
❌ Debunked — Contradicted by authoritative evidence
⚠️ Mixed — Partly true, incomplete, context-dependent, overstated, or disputed
❓ Unclear — Evidence insufficient, unavailable, outdated, or not specific enough

---

## CONFIDENCE SCORE
9–10: Strongly supported, current, authoritative, direct
7–8: Supported with caveats, limited source independence, or wording risk
5–6: Partially supported; source quality, specificity, or recency limited
3–4: Weak support, missing caveats, or conflicting evidence
1–2: Unsupported, contradicted, outdated, or likely inaccurate
RULE: Do not assign 10 if any caveat is missing.

---

## EVIDENCE LANGUAGE (HARD)
Never: "research confirms," "studies show," "evidence proves," "the literature agrees"
Use: "suggests," "tends to," "available evidence indicates," "findings from [source] suggest"

---

## REQUIRED OUTPUT — TWO REQUIRED PARTS (both required)

**PART 1: DETAILED FACT-CHECK REPORT**

Section 1 — Claim Extraction Summary
Table: ID | Claim | Claim Type | Location in Draft

Section 2 — Claim-by-Claim Verification
For each claim:
> The Claim: [exact statement]
Claim Type: [type]
Location in Draft: [section or paragraph]
The Verdict: [verdict icon]
The Evidence: [2-sentence summary. Max 15 words quoted from any source.]
The Sources: [Source 1] / [Source 2]
Confidence Score: [1–10]
Verification Note: [adversarial review. If inconclusive, state "Inconclusive" and explain.]

Section 3 — Claims Requiring Revision
Table: ID | Claim | Issue | Recommended Revision
If none: "No claims require revision based on the available evidence."

Section 4 — Unsupported or Removed Claims
Table: ID | Claim | Reason It Should Be Removed
If none: "No claims need to be removed based on the available evidence."

Section 5 — Overall Confidence Score
Overall Confidence Score: [1–10]
Summary: [factual reliability, remaining risks, required revisions before publishing]

**PART 2: MARKDOWN FACT-CHECK TABLE**
| ID | Claim | Verdict | Evidence | Confidence Score | Sources |
Column rules: ID sequential | Claim exact | Verdict icon consistent | Evidence 1–2 sentences | Score matches detailed report | Sources semicolon-separated.

---

## CONTEXT WINDOW RULE
Prioritize data from the last 90 days. Ignore context older than 90 days.
```

3. Commit to `fact-check`.

### Step 4.7 — Create .github/workflows/fact-check-agent.yml

1. Filename: `.github/workflows/fact-check-agent.yml`
2. Content:

```yaml
name: "VD — Fact-Check Agent (Manual Trigger)"

on:
  workflow_dispatch:
    inputs:
      page_type:
        description: "Page Type"
        required: true
        type: choice
        options:
          - hub
          - cluster
          - school
      assigned_pillar:
        description: "Assigned Pillar (P1–P5)"
        required: true
        type: choice
        options:
          - P1
          - P2
          - P3
          - P4
          - P5
      entity_concept:
        description: "Primary Topic / Entity Concept (one specific sentence)"
        required: true
        type: string
      url_slug:
        description: "Target URL Slug (e.g., /gi-bill-hybrid-programs-california)"
        required: true
        type: string

jobs:
  fact-check-agent:
    name: "Run Fact-Check Agent"
    runs-on: ubuntu-latest

    steps:
      - name: "Checkout fact-check branch"
        uses: actions/checkout@v4
        with:
          ref: fact-check

      - name: "Verify master prompt file exists"
        run: |
          if [ ! -f "orchestration/master-prompt.md" ]; then
            echo "ERROR: orchestration/master-prompt.md not found on fact-check branch."
            exit 1
          fi
          echo "master-prompt.md confirmed present."

      - name: "Call GitHub Models API and save output"
        env:
          GH_MODELS_TOKEN: ${{ secrets.GH_MODELS_TOKEN }}
          PAGE_TYPE: ${{ github.event.inputs.page_type }}
          ASSIGNED_PILLAR: ${{ github.event.inputs.assigned_pillar }}
          ENTITY_CONCEPT: ${{ github.event.inputs.entity_concept }}
          URL_SLUG: ${{ github.event.inputs.url_slug }}
        run: |
          python3 << 'PYEOF'
          import json
          import os
          import urllib.request
          import urllib.error

          with open("orchestration/master-prompt.md", "r", encoding="utf-8") as f:
              system_prompt = f.read()

          page_type       = os.environ.get("PAGE_TYPE", "").strip()
          assigned_pillar = os.environ.get("ASSIGNED_PILLAR", "").strip()
          entity_concept  = os.environ.get("ENTITY_CONCEPT", "").strip()
          url_slug        = os.environ.get("URL_SLUG", "").strip()
          token           = os.environ.get("GH_MODELS_TOKEN", "").strip()

          missing = []
          if not page_type:       missing.append("page_type")
          if not assigned_pillar: missing.append("assigned_pillar")
          if not entity_concept:  missing.append("entity_concept")
          if not url_slug:        missing.append("url_slug")

          if missing:
              print(f"ERROR: Missing required inputs: {', '.join(missing)}")
              exit(1)

          user_message = f"""Page Type: {page_type}
Assigned Pillar: {assigned_pillar}
Primary Topic / Entity Concept: {entity_concept}
Target URL Slug: {url_slug}

Generate the complete fact-check report (both Detailed Report and Markdown Table) per your system instructions. Use web search as authorized for Tier 3 claims."""

          payload = {
              "model": "gpt-4o",
              "messages": [
                  {"role": "system", "content": system_prompt},
                  {"role": "user",   "content": user_message}
              ],
              "max_tokens": 4000,
              "temperature": 0.2
          }

          req = urllib.request.Request(
              "https://models.inference.ai.azure.com/chat/completions",
              data=json.dumps(payload).encode("utf-8"),
              headers={
                  "Authorization": f"Bearer {token}",
                  "Content-Type": "application/json"
              },
              method="POST"
          )

          try:
              with urllib.request.urlopen(req, timeout=120) as resp:
                  data = json.loads(resp.read())
          except urllib.error.HTTPError as e:
              print(f"HTTP ERROR {e.code}: {e.read().decode('utf-8', errors='replace')}")
              exit(1)
          except Exception as e:
              print(f"REQUEST FAILED: {e}")
              exit(1)

          if "choices" not in data or not data["choices"]:
              print(f"UNEXPECTED API RESPONSE: {json.dumps(data, indent=2)}")
              exit(1)

          fc_output = data["choices"][0]["message"]["content"]
          header = f"""---
# Fact-Check Agent Output
**Run:** ${{ github.run_number }}
**Branch:** fact-check
**Page Type:** {page_type}
**Assigned Pillar:** {assigned_pillar}
**Entity Concept:** {entity_concept}
**URL Slug:** {url_slug}
---

"""
          final_output = header + fc_output

          with open("fact-check-output.md", "w", encoding="utf-8") as f:
              f.write(final_output)

          print(f"Output saved. Character count: {len(final_output)}")

          PYEOF

      - name: "Upload fact-check output as artifact"
        uses: actions/upload-artifact@v4
        with:
          name: "fact-check-output-run-${{ github.run_number }}"
          path: fact-check-output.md
          retention-days: 30

      - name: "Print output to workflow log"
        run: |
          echo "========== FACT-CHECK AGENT OUTPUT =========="
          cat fact-check-output.md
          echo "========== END OF OUTPUT =========="
```

3. Commit to `fact-check`.

### Step 4.8 — Verify fact-check Branch Structure

Confirm:
- `.github/workflows/fact-check-agent.yml` ✓
- `foundational/.gitignore` ✓
- `foundational/AGENTS.md` ✓
- `content-copywriting/` — 3 files only ✓
- `governance/` — 2 files ✓
- `orchestration/master-prompt.md` ✓

> ✅ Phase 4 complete when all 10 files are confirmed.

---

## PHASE 5: BUILD THE quality-check BRANCH (STRUCTURAL ONLY)

**Goal:** Create the reserved quality-check branch with structural scaffolding only. No operational workflow. No content modules beyond brand/language/tone stubs. Module not yet included.

### Step 5.1 — Create the quality-check Branch

1. Click branch selector → type `quality-check` → **Create branch: quality-check from 'main'**.

### Step 5.2 — Create foundational/.gitignore

1. Filename: `foundational/.gitignore`
2. Content:

```
# quality-check branch — reserved, not operational
*.log
*.json
__pycache__/
```

3. Commit to `quality-check`.

### Step 5.3 — Create foundational/AGENTS.md

1. Filename: `foundational/AGENTS.md`
2. Content:

```markdown
# AGENTS.md — quality-check branch
## Branch Status
RESERVED — Not yet operational.

## Planned Purpose
Stage 4 of the VeteranDegrees content pipeline: compliance to Google AI-assisted content creation guidelines.

## Activation Condition
This branch activates when the quality-check module is developed and explicitly added.
Do not run workflows from this branch until that module is present and confirmed operational.

## Current State
Structural scaffold only. No workflow YAML deployed. No agent operational.

## Context Window Rule
Prioritize data from the last 90 days. Ignore context older than 90 days.
```

3. Commit to `quality-check`.

### Step 5.4 — Create Stub content-copywriting/ Files (3 files)

These are present for structural integrity. The branch will inherit the files when the module is ready, but the stubs confirm the directory exists.

**File 1:** `content-copywriting/vd-brand-positioning-v1.0.0.md` → paste full content → commit to `quality-check`.  
**File 2:** `content-copywriting/vd-language-control-standards-v1.0.0.md` → paste → commit.  
**File 3:** `content-copywriting/vd-tone-and-style-v1.0.0.md` → paste → commit.

### Step 5.5 — Create orchestration/master-prompt.md (Placeholder)

1. Filename: `orchestration/master-prompt.md`
2. Content:

```markdown
# VeteranDegrees — Quality-Check Agent System Prompt
**Status:** PLACEHOLDER — NOT OPERATIONAL
**Branch:** quality-check

This file is a structural placeholder. The quality-check module has not been developed.
Do not activate or trigger workflows referencing this file until the module is explicitly provided and confirmed.

Planned function: Compliance audit against Google AI-assisted content creation guidelines.
```

3. Commit to `quality-check`.

> ✅ Phase 5 complete. quality-check branch is structurally present but not operational.

---

## PHASE 6: VERIFICATION GATE

**Goal:** Confirm every file is in the correct branch, no contamination has occurred, and every branch has its isolated runtime layer.

### Verification Checklist — Run Through Each Branch

Navigate to each branch using the branch selector and confirm:

**knowledge-base branch:**
- [ ] `foundational/.gitignore` ✓
- [ ] `foundational/AGENTS.md` ✓
- [ ] `content-copywriting/` — 5 files ✓
- [ ] `governance/` — 4 files (includes vd-fact-checking) ✓
- [ ] `orchestration/` — 4 raw module files ✓
- [ ] No `.github/workflows/` directory (no workflows run from knowledge-base) ✓

**outline branch:**
- [ ] `.github/workflows/outline-agent.yml` ✓
- [ ] `foundational/.gitignore` ✓
- [ ] `foundational/AGENTS.md` ✓
- [ ] `content-copywriting/` — 5 files ✓
- [ ] `governance/` — 3 files (NO vd-fact-checking) ✓
- [ ] `orchestration/master-prompt.md` (extracted, NOT raw module) ✓
- [ ] NO vd-outline-master-prompt-system-2 file present ✓
- [ ] NO vd-outline-workflow-system-2 file present ✓

**content branch:**
- [ ] `.github/workflows/content-agent.yml` ✓
- [ ] `foundational/.gitignore` ✓
- [ ] `foundational/AGENTS.md` ✓
- [ ] `content-copywriting/` — 5 files ✓
- [ ] `governance/` — 3 files (NO vd-fact-checking) ✓
- [ ] `orchestration/master-prompt.md` (extracted, NOT raw module) ✓
- [ ] NO vd-content-master-prompt-system-2 file present ✓

**fact-check branch:**
- [ ] `.github/workflows/fact-check-agent.yml` ✓
- [ ] `foundational/.gitignore` ✓
- [ ] `foundational/AGENTS.md` ✓
- [ ] `content-copywriting/` — 3 files ONLY (NO pillar-architecture, NO keyword-type-map) ✓
- [ ] `governance/` — 2 files ONLY (vd-ai-extractability + vd-fact-checking) ✓
- [ ] `orchestration/master-prompt.md` ✓

**quality-check branch:**
- [ ] `foundational/.gitignore` ✓
- [ ] `foundational/AGENTS.md` (marked RESERVED) ✓
- [ ] `content-copywriting/` — 3 stub files ✓
- [ ] `orchestration/master-prompt.md` (marked PLACEHOLDER) ✓
- [ ] NO `.github/workflows/` directory ✓

### Context Contamination Check

Confirm these cross-branch contamination violations do NOT exist:

| Prohibited File | Must NOT appear in |
|---|---|
| vd-fact-checking-v1.0.0.md | outline branch, content branch |
| vd-outline-master-prompt-system-2 (raw) | outline, content, fact-check, quality-check |
| vd-content-master-prompt-system-2 (raw) | outline, content, fact-check, quality-check |
| vd-pillar-architecture-v1.0.0.md | fact-check branch |
| vd-keyword-type-map-v1.0.0.md | fact-check branch |
| Any .github/workflows/ file | knowledge-base branch, quality-check branch |

### Module Count Check

Total modules deployed across all branches:

| Branch | Unique Files (excl. README) | Notes |
|---|---|---|
| knowledge-base | 15 | All 13 modules + .gitignore + AGENTS.md |
| outline | 12 | 8 tactical + .gitignore + AGENTS.md + master-prompt + workflow YAML |
| content | 12 | Same as outline (different master-prompt + different workflow YAML) |
| fact-check | 10 | 5 tactical + .gitignore + AGENTS.md + master-prompt + workflow YAML |
| quality-check | 6 | 3 stubs + .gitignore + AGENTS.md + placeholder master-prompt |

All 13 modules confirmed present in knowledge-base: ✓
Each operational branch has its own isolated `foundational/` layer: ✓
No raw master prompt/workflow deployed to operational branches: ✓

---

## PHASE 7: TEST TRIGGER — OUTLINE BRANCH

**Goal:** Fire the first real trigger on the outline branch using all four required inputs and confirm the workflow executes, calls the API, and produces an artifact.

### Step 7.1 — Navigate to GitHub Actions

1. Go to: `https://github.com/hunterxx0324/veterandegrees-case-study/actions`
2. In the left sidebar under "Workflows," look for: **VD — Outline Agent (Manual Trigger)**

   > If the workflow does not appear: confirm that `outline-agent.yml` is present at `.github/workflows/outline-agent.yml` on the `outline` branch. GitHub Actions scans all branches for `workflow_dispatch` triggers.

3. Click **VD — Outline Agent (Manual Trigger)** in the sidebar.

### Step 7.2 — Run the Workflow

1. Click **Run workflow** (blue button, top right of the workflow view).
2. A dropdown appears with the four required input fields. Fill in:

   | Field | Test Value |
   |---|---|
   | Page Type | `cluster` |
   | Assigned Pillar | `P1` |
   | Primary Topic / Entity Concept | `How hybrid program format determines housing allowance eligibility for post-9/11 GI Bill users` |
   | Target URL Slug | `/hybrid-program-housing-allowance-eligibility` |

3. Confirm the branch selector shows `outline` (not main).
4. Click **Run workflow**.

### Step 7.3 — Monitor the Run

1. The workflow run will appear in the run list within seconds. Click it.
2. Click the job **Run Outline Agent** to expand it.
3. Watch for these steps in order:
   - **Checkout outline branch** — should succeed in ~10 seconds.
   - **Verify master prompt file exists** — should print "master-prompt.md confirmed present."
   - **Call GitHub Models API and save output** — this is the LLM call. Expect 30–120 seconds.
   - **Upload outline output as artifact** — should succeed.
   - **Print output to workflow log** — output printed to log.

### Step 7.4 — Confirm Success Criteria

The run is successful when ALL of the following are true:

- [ ] All 5 steps show a green checkmark
- [ ] Step "Call GitHub Models API" exits with code 0 (no error in red)
- [ ] Step "Upload outline output as artifact" completes
- [ ] An artifact named `outline-output-run-1` appears under the "Artifacts" section at the bottom of the run page
- [ ] Clicking the artifact downloads `outline-output.md`
- [ ] The downloaded file begins with the metadata header and contains recognizable outline content (Input Manifest through EAS Pre-Score Report)

### Step 7.5 — Troubleshooting (if run fails)

**Error: HTTP ERROR 401**
→ Cause: GH_MODELS_TOKEN secret is missing, expired, or has incorrect scopes.
→ Fix: Re-create the PAT with `repo` + `models:read` scopes. Update the secret at Settings → Secrets → Actions → GH_MODELS_TOKEN.

**Error: HTTP ERROR 403**
→ Cause: GitHub Models API access not enabled on your account.
→ Fix: Visit https://github.com/marketplace/models and confirm you have access to GitHub Models beta.

**Error: master-prompt.md not found**
→ Cause: The file was not committed to the `outline` branch, or was committed to a different path.
→ Fix: Navigate to the outline branch and confirm `orchestration/master-prompt.md` exists at that exact path.

**Error: Missing required inputs**
→ Cause: One or more workflow_dispatch inputs were left blank.
→ Fix: Re-run the workflow with all four fields filled in.

**Artifact is empty or contains only the header**
→ Cause: API returned an empty or malformed response.
→ Fix: Check the "Call GitHub Models API" step log for the full API response body. Look for `UNEXPECTED API RESPONSE` in the log.

---

## APPENDIX A — BRANCH SUMMARY REFERENCE

| Branch | Status | Workflow | Primary Function |
|---|---|---|---|
| main | Untouched | None | Original repo baseline |
| knowledge-base | Live | None (read-only) | Global source of truth — all 13 modules |
| outline | Operational | outline-agent.yml | Stage 1: Outline generation |
| content | Operational | content-agent.yml | Stage 2: Content drafting |
| fact-check | Operational | fact-check-agent.yml | Stage 3: Claim verification |
| quality-check | Reserved | None (structural only) | Stage 4: Reserved for future module |

---

## APPENDIX B — FILE DEPLOYMENT QUICK-REFERENCE

Complete file-by-file deployment record. Use this to verify or re-deploy any single file.

| File | knowledge-base path | outline path | content path | fact-check path | quality-check path |
|---|---|---|---|---|---|
| vd-brand-positioning | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ |
| vd-language-control-standards | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ |
| vd-tone-and-style | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ | content-copywriting/ |
| vd-pillar-architecture | content-copywriting/ | content-copywriting/ | content-copywriting/ | — | — |
| vd-keyword-type-map | content-copywriting/ | content-copywriting/ | content-copywriting/ | — | — |
| vd-ai-extractability | governance/ | governance/ | governance/ | governance/ | — |
| vd-page-creation-architecture | governance/ | governance/ | governance/ | — | — |
| vd-keyword-audit | governance/ | governance/ | governance/ | — | — |
| vd-fact-checking | governance/ | — | — | governance/ | — |
| vd-outline-master-prompt (raw) | orchestration/ | — | — | — | — |
| vd-outline-workflow (raw) | orchestration/ | — | — | — | — |
| vd-content-master-prompt (raw) | orchestration/ | — | — | — | — |
| vd-content-workflow (raw) | orchestration/ | — | — | — | — |
| master-prompt.md (extracted) | — | orchestration/ | orchestration/ | orchestration/ | orchestration/ (stub) |
| outline-agent.yml | — | .github/workflows/ | — | — | — |
| content-agent.yml | — | — | .github/workflows/ | — | — |
| fact-check-agent.yml | — | — | — | .github/workflows/ | — |

---

## APPENDIX C — VERSIONING RULE (ALL BRANCHES)

SemVer applies to all document files across all branches:
- Patch bump (x.x.1): single-line fix or correction
- Minor bump (x.1.0): additive change — new section, new rule, new file
- Major bump (2.0.0): structural overhaul

New versions are always new files. Never overwrite existing files.
Version resets to v1.0.0 on first public release.

---

*SOP Version 1.0.0 | VeteranDegrees Case Study — Agentic Workflow Deployment*
*Environment: GitHub Browser UI + github.dev | Trigger: Manual (workflow_dispatch)*
*Architecture: Sequential Multi-Branch Isolated | Branches: 5 | Modules: 13*
