# Workflow Router

Use this file when a task spans multiple finance verticals or the user gives a vague request such as "analyze this company", "build a model", "prepare a memo", or "review this package".

## First Triage

Identify five things before doing analysis:

- Subject: company, security, sector, fund, client, deal, portfolio company, counterparty, account, or ledger.
- User goal: valuation, investment decision support, model build, report writing, deck creation, diligence, compliance review, reporting, reconciliation, or planning.
- Audience: PM, analyst, banker, IC, board, client, advisor, controller, compliance, or operations team.
- Output: spreadsheet, document, deck, memo, checklist, model update, screen, table, or concise answer.
- Deadline and recency need: same-day earnings, live market data, month-end close, annual review, or static historical research.

## Routing Matrix

| User intent | Primary reference | Typical output |
|---|---|---|
| "Value this company" | `modeling-workflows.md` | DCF, comps, SOTP, summary memo |
| "Build/update a model" | `modeling-workflows.md` | XLSX or formula table |
| "Analyze earnings" | `research-and-reports.md` | Earnings note, model update, charts |
| "Write initiation/sector report" | `research-and-reports.md` | Long-form report with exhibits |
| "Prepare a pitch / one-pager / CIM / teaser" | `deal-and-portfolio-workflows.md` | Deck, profile, memo, process doc |
| "Screen deals / write IC memo" | `deal-and-portfolio-workflows.md` | Screening table, IC memo, diligence plan |
| "Review portfolio KPIs" | `deal-and-portfolio-workflows.md` | KPI dashboard, variance commentary |
| "Prepare client review or plan" | `ops-and-wealth-workflows.md` | Client report, plan, proposal |
| "Reconcile, close, audit statements" | `ops-and-wealth-workflows.md` | Exception log, close memo, control checklist |
| "KYC/onboarding" | `ops-and-wealth-workflows.md` | Rules-grid result, gaps, escalation list |

## Sequencing Multi-Part Work

For public market research:

1. Confirm ticker/company and report type.
2. Gather filings, latest earnings, transcript, investor presentation, market data, consensus where available.
3. Normalize key metrics and peer set.
4. Build model or tables first.
5. Write conclusions after tables and charts exist.

For banking or private equity:

1. Confirm transaction context, buyer/seller side, process stage, confidentiality constraints, and template availability.
2. Build company/profile data pack before drafting deliverables.
3. Create valuation and strategic rationale.
4. Produce the deck/memo/checklist.
5. Validate sources, assumptions, and red flags.

For operations or wealth:

1. Confirm the account/fund/client period and policy/rule set.
2. Ingest source documents and transaction/account data.
3. Reconcile against rules or expected balances.
4. Separate confirmed breaks from suspected issues.
5. Stage findings for human approval.

## Clarifying Questions

Ask only for missing details that materially change the work. Useful questions:

- What output format should I produce?
- Is there a firm template or prior example to follow?
- Which data source should be treated as authoritative?
- What time period, currency, and geography should I use?
- Is this for public equity research, banking, PE, wealth, fund admin, or operations?

If the user does not answer, proceed with reasonable defaults and state them in the output.
