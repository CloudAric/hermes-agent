# Hermes Intelligence & Knowledge Center — Build Plan

## Goal
Build a dynamic Intelligence & Knowledge Center that turns incoming information into structured knowledge, searchable memory, reusable workflows, and action recommendations for Archer's AI consulting, learning, and delivery work.

## Core Thesis
This should not be a passive file library. It should be an operating system for learning:

1. Ingest: capture signals from YouTube, news, RSS, PDFs, Telegram, web pages, notes, and manual ideas.
2. Normalize: convert raw content into consistent markdown/JSON records with metadata.
3. Distill: summarize, extract concepts, risks, opportunities, action items, and links.
4. Connect: link related concepts, people, companies, tools, clients, workflows, and past notes.
5. Retrieve: provide fast semantic + keyword search.
6. Act: generate playbooks, client deliverables, cron alerts, implementation plans, and decision briefs.
7. Improve: learn from usage, corrections, and repeated questions.

## Recommended Architecture

### Layer 1 — Intelligence Ingestion
Purpose: bring knowledge into the system cleanly.

Sources:
- YouTube Learning Hub transcripts and manual metadata workflow.
- AI news cronjobs and trend radars.
- Telegram forwarded messages and links.
- Web articles, PDFs, docs, GitHub repos.
- Obsidian/manual notes.
- Client project artifacts.
- Prompt Master templates and reusable workflows.

Key output:
- Raw archive.
- Normalized source record.
- Metadata: source, date, author, URL, topic, confidence, language, tags, processed status.

### Layer 2 — Knowledge Processing & Memory
Purpose: convert input into durable intelligence.

Processing modules:
- TLDR summarizer.
- Key concepts extractor.
- Entity extraction: companies, people, tools, models, regulations, countries, markets.
- Action extractor: what to build, test, watch, sell, avoid.
- Risk extractor: legal, security, vendor lock-in, cost, hallucination, data residency.
- Opportunity extractor: SME use cases, pricing angles, automation workflows.
- Linker: creates relationships between old and new notes.
- Confidence scorer: distinguishes verified facts vs assumptions.

Storage split:
- Markdown/Obsidian for human-readable knowledge.
- SQLite for structured metadata and audit logs.
- Vector DB for semantic retrieval.
- Optional graph layer later for entity/concept relationships.

### Layer 3 — Action & Delivery Layer
Purpose: make knowledge produce outcomes.

Outputs:
- Telegram briefings.
- Deep Dive reports.
- Client proposal drafts.
- SME workflow blueprints.
- Prompt packs.
- Implementation plans.
- Code/task tickets.
- Signals-to-watch alerts.
- Weekly learning review.
- Reusable playbooks.

Trigger modes:
- Manual ask: Archer asks Hermes to retrieve/synthesize.
- Scheduled cron: daily/weekly briefings.
- Event threshold: important signal detected.
- Project context: retrieved notes injected into active implementation.

## MVP Scope — 14 Days

### MVP Objective
Create a working local-first knowledge loop with minimum complexity:
Raw input -> structured markdown -> SQLite metadata -> searchable retrieval -> Telegram action brief.

### MVP Components
1. Inbox directory
   - `~/knowledge-center/inbox/`
   - Stores raw links, transcripts, pasted notes, article dumps.

2. Processed knowledge directory
   - `~/knowledge-center/notes/`
   - Obsidian-compatible markdown notes.

3. Metadata database
   - `~/knowledge-center/kc.db`
   - Tables: sources, notes, entities, tags, actions, processing_runs.

4. Processing script
   - `process_inbox.py`
   - Reads raw files, creates structured notes, extracts metadata.

5. Search script
   - `kc_search.py`
   - Keyword search first; vector search phase 2.

6. Weekly review cron
   - Summarizes new notes, top themes, opportunities, workflows to build.

7. Telegram command/prompt pattern
   - Ask Hermes: “Search KC for X and produce client-ready brief.”

## Suggested File Structure

```text
~/knowledge-center/
  inbox/
    youtube/
    articles/
    telegram/
    pdfs/
    manual/
  raw/
  notes/
    sources/
    concepts/
    playbooks/
    client-use-cases/
    market-intel/
    tool-reviews/
  indexes/
    topic-index.md
    entity-index.md
    workflow-index.md
  exports/
  logs/
  scripts/
    process_inbox.py
    kc_search.py
    weekly_review.py
  kc.db
```

## Note Template

```yaml
---
title: "..."
type: source | concept | playbook | client-use-case | market-intel | tool-review
date: YYYY-MM-DD
timezone: MYT
source_url: "..."
source_type: youtube | article | telegram | pdf | manual | cron
author: "..."
language: zh | en | mixed
tags: []
entities: []
confidence: high | medium | low
status: raw | processed | reviewed | applied
related_notes: []
---

TLDR:

Key Points:

Why It Matters:

Actionable Workflows:

SME / Client Application:

Risks / Constraints:

Signals to Watch:

Questions for Archer:

Next Action:
```

## Retrieval Design

### Phase 1 — Reliable Search
- SQLite FTS5 or ripgrep-style keyword search.
- Tag/entity filters.
- Date/source filters.

### Phase 2 — Semantic Search
- Embeddings for notes and chunks.
- Local vector DB options:
  - Chroma: easiest for MVP.
  - LanceDB: strong local file-based option.
  - SQLite vec extension: elegant but more setup.

Recommended MVP: SQLite FTS5 first, then LanceDB or Chroma.

### Phase 3 — Graph Intelligence
Only add after MVP proves useful.

Graph links:
- Tool -> Use Case -> Client Segment -> Workflow -> Risk -> Pricing.
- News Signal -> Business Impact -> Action Playbook.
- YouTube Concept -> Implementation Pattern -> Client Demo.

## Intelligence Scoring Model

Every processed item should receive scores:

1. Relevance to Archer's work: 1-5
2. Revenue potential: 1-5
3. Cost-saving potential: 1-5
4. Risk-reduction potential: 1-5
5. Implementation effort: 1-5
6. Confidence: high/medium/low
7. Urgency: now / soon / watch

This prevents the knowledge base from becoming a graveyard of interesting but useless notes.

## Workflow Examples

### Workflow A — YouTube to Playbook
1. Transcript enters inbox.
2. Hermes extracts core ideas.
3. Concepts are linked to existing notes.
4. System generates:
   - summary note
   - implementation checklist
   - SME application angle
   - possible MYR pricing/productization angle
5. Weekly review selects top 3 ideas to convert into deliverables.

### Workflow B — News Signal to Deep Dive
1. AI news cron detects repeated signal.
2. If relevance + urgency score crosses threshold, create Deep Dive task.
3. Hermes researches official sources and market context.
4. Output:
   - executive brief
   - risks
   - client talking points
   - workflow idea
   - signals to monitor

### Workflow C — Client Delivery Reuse
1. Archer asks: “Build AI receptionist workflow for clinic SME.”
2. Hermes searches Knowledge Center for:
   - prior clinic workflows
   - vendor comparisons
   - data privacy notes
   - pricing references
   - prompt templates
3. Output becomes proposal + implementation plan.

## Build Roadmap

### Phase 0 — Decision Alignment
Decide:
- Obsidian-first or pure filesystem-first.
- Local-only vs cloud sync.
- Whether Telegram topic delivery should be part of MVP.
- Which sources are priority: YouTube, news, Telegram links, PDFs, client docs.

Recommended: local-first filesystem + Obsidian-compatible markdown + SQLite.

### Phase 1 — MVP Foundation
- Create directory structure.
- Create note template.
- Create SQLite schema.
- Build process_inbox.py.
- Build kc_search.py.
- Process 10-20 existing YouTube/news items.
- Verify search and synthesis quality.

### Phase 2 — Automation
- Add cron for daily ingestion and weekly review.
- Add deduplication by URL/content hash.
- Add processing logs.
- Add Telegram delivery to selected topic.

### Phase 3 — Semantic Layer
- Add embeddings.
- Add vector search.
- Add “retrieve top N notes and synthesize” workflow.

### Phase 4 — Action Engine
- Add scoring.
- Add playbook generation.
- Add client-ready output templates.
- Add automatic Deep Dive triggers.

### Phase 5 — Governance & Quality
- Add source confidence tagging.
- Add fact/assumption separation.
- Add review status.
- Add stale-note detection.
- Add security boundaries for untrusted content.

## Risks & Tradeoffs

### Risk 1 — Overbuilding
Mitigation: start with markdown + SQLite; postpone graph DB and complex agent memory.

### Risk 2 — Knowledge graveyard
Mitigation: every note must include “Next Action” or “Why It Matters.”

### Risk 3 — Hallucinated synthesis
Mitigation: every claim must link back to source notes and confidence level.

### Risk 4 — Cost creep
Mitigation: use local storage, cheap embeddings, scheduled batch processing, and only deep-dive high-score signals.

### Risk 5 — Sensitive client data leakage
Mitigation: separate public learning notes from client-private notes; add data classification metadata.

## Recommended Tech Stack

MVP:
- Markdown files.
- SQLite + FTS5.
- Python scripts.
- Obsidian optional.
- Hermes cron.
- Telegram delivery.

Phase 2:
- Chroma or LanceDB for semantic search.
- n8n for external ingestion workflows if needed.
- AnythingLLM/ARIA as optional UI/retrieval surface.

Do not start with:
- Full graph DB.
- Overcomplicated web app.
- Enterprise RAG stack.
- Premature vector-only architecture.

## Success Metrics

Week 1:
- 20 useful notes processed.
- Search returns relevant results in under 10 seconds.
- Weekly review produces at least 3 actionable ideas.

Month 1:
- 100+ structured notes.
- 10 reusable playbooks.
- At least 3 client-ready proposal/workflow drafts generated from stored knowledge.
- Less repeated manual research.

Business metric:
- At least one workflow directly supports MYR revenue, cost saving, or risk reduction.

## Open Questions
1. Should this be a personal learning OS, client-delivery asset, or both?
2. Should notes live in Obsidian vault, existing YouTube Learning Hub, or a new `~/knowledge-center` root?
3. Which first 3 sources matter most?
4. Do we want Telegram topic delivery for all Knowledge Center updates?
5. Should client data be stored in the same system or in a separate private vault?

## Recommended Next Step
Run a 7-day MVP sprint:
- Day 1: finalize architecture and create folders/schema/templates.
- Day 2-3: process YouTube Learning Hub content.
- Day 4: process AI/news cron outputs.
- Day 5: implement search and weekly synthesis.
- Day 6: generate first action playbook.
- Day 7: review usefulness and decide whether to add vector search.
