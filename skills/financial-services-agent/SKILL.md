---
name: financial-services-agent
description: Financial-services workflow router and execution guide for AI agents. Use when the user asks for equity research, earnings analysis, DCF/comps/LBO/3-statement models, market or sector research, pitch books, CIMs, teasers, buyer lists, private equity diligence, IC memos, portfolio monitoring, wealth-management reviews or plans, fund-admin reconciliation and close tasks, valuation review, KYC/onboarding review, or any finance deliverable requiring current source-backed data, spreadsheets, documents, decks, charts, valuation, peer comparison, audit trails, or human-review-ready analyst work product.
---

# Financial Services Agent

Use this skill to turn broad finance requests into structured, source-backed workflows. It is an agent-neutral adaptation of workflow patterns from `anthropics/financial-services`; it does not assume Claude Cowork, slash commands, Managed Agents API, or any specific MCP provider.

## Core Rules

- Treat every output as draft analyst work product for qualified human review.
- Do not provide personalized investment, legal, tax, accounting, lending, onboarding, or transaction approval advice.
- Do not execute trades, approve onboarding, bind risk, post ledger entries, or claim a model/report is final.
- Prefer current, attributable primary or institutional data over memory. If recency matters, verify the current date and source dates before analyzing.
- Use `N/A`, `Not disclosed`, or an explicit assumption when data is missing. Do not fill gaps from training knowledge.
- Keep an audit trail: sources used, source dates, assumptions, formulas, adjustments, and unresolved data gaps.

## Workflow Router

Classify the user request first, then load only the relevant reference file.

- Public company valuation, spreadsheet models, Excel audits, comps, DCF, LBO, 3-statement models, deck refresh or model QA: read `references/modeling-workflows.md`.
- Earnings updates, earnings previews, initiations, sector overviews, thesis trackers, catalysts, morning notes, stock screens, market research, or written equity research: read `references/research-and-reports.md`.
- Investment banking deliverables, pitch decks, CIMs, teasers, one-pagers, buyer lists, merger models, process letters, live deal tracking, PE sourcing, deal screening, diligence, unit economics, returns, IC memos, portfolio monitoring, value creation plans, or AI-readiness reviews: read `references/deal-and-portfolio-workflows.md`.
- Wealth management, client reviews, financial plans, client reports, proposals, portfolio rebalancing, tax-loss harvesting, fund administration, GL reconciliation, month-end close, valuation review, statement audit, KYC or onboarding: read `references/ops-and-wealth-workflows.md`.
- Any workflow involving data source selection, stale data risk, citations, confidential data, assumptions, model validation, compliance boundaries, or human sign-off: read `references/data-and-integrity.md`.
- If the task spans multiple areas, read `references/workflow-router.md` to sequence the work and define the deliverables.

## Execution Pattern

1. Confirm the deliverable type, audience, date, company/security/fund/client scope, geography, currency, and format.
2. Build a source plan before analysis: user files, internal systems, configured data connectors, filings, transcripts, investor materials, market data, and public web fallback.
3. Collect raw data into task-local working files or tables before deriving metrics.
4. Normalize periods, units, currency, fiscal calendars, non-GAAP definitions, and peer inclusion rules before comparing.
5. Compute derived metrics separately from raw data. In spreadsheets, use live formulas for derived values rather than hardcoded calculations.
6. Produce the requested artifact: spreadsheet, memo, report, deck, checklist, screen, or structured markdown when tools are limited.
7. Validate dates, citations, formulas, units, assumptions, valuation sanity checks, and unresolved data gaps before delivery.

## Tool Mapping

Use whatever tools the host agent actually has. Do not mention unavailable tools as if they were available.

- Spreadsheets: build live formulas, color or label inputs vs formulas, cite hardcoded inputs, recalculate/check formulas if possible.
- Documents: produce concise analyst-style prose with tables, charts, citations, source section, and clear human-review caveats.
- Presentations: use the user's template or firm style first; otherwise keep layouts dense, sober, and decision-focused.
- Data connectors/MCP: prefer configured institutional sources for financial and market data. Record provider, retrieval date, period, and field definitions.
- Web/search: use for current public data, filings, investor relations, news, transcripts, and source verification when institutional data is unavailable.
- No file tools: provide a structured plan, normalized tables, formulas, and validation checklist in markdown.

## Deliverable Standards

Every finance deliverable should include:

- Objective and scope.
- Source list with dates and links/identifiers where possible.
- Key assumptions and what changed from prior view if applicable.
- Tables or charts for claims involving trends, comparisons, valuations, sensitivities, or portfolio allocation.
- Clear distinction between reported data, calculated metrics, consensus estimates, management guidance, and agent assumptions.
- Risk, uncertainty, and missing-data notes.
- Human-review status.

## Quality Gate

Before finalizing, check:

- Current date and source dates are explicit where time-sensitive.
- All key numeric claims are backed by a source, formula, or stated assumption.
- Peer groups are genuinely comparable and exclusions are explained.
- Valuation ranges are supported by sensitivities, not single-point false precision.
- Spreadsheet formulas do not silently hardcode derived metrics.
- Reports and decks avoid generic commentary; they answer the user's actual decision question.
- No output is framed as a direct buy/sell recommendation or professional advice.

## Provenance

This skill is an original, agent-neutral consolidation inspired by the public `anthropics/financial-services` repository, which is published under Apache-2.0. The upstream repo organizes finance workflows as agents, vertical plugins, skills, commands, connectors, and managed-agent cookbooks; this skill compresses that architecture into one portable `SKILL.md` plus reference files for other agents.
