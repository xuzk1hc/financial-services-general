# Financial Services General

A portable financial-services skill for AI agents. It turns broad finance requests into structured, source-backed workflows for equity research, valuation, banking materials, private equity diligence, wealth workflows, fund administration, operations, and KYC/onboarding review.

The skill is inspired by workflow patterns in [anthropics/financial-services](https://github.com/anthropics/financial-services), but it is packaged as an agent-neutral skill rather than a Claude-specific plugin. It does not assume Claude Cowork, slash commands, Managed Agents API, or any specific MCP provider.

## What It Contains

```text
skills/financial-services-agent/
  SKILL.md
  agents/openai.yaml
  references/
    data-and-integrity.md
    workflow-router.md
    modeling-workflows.md
    research-and-reports.md
    deal-and-portfolio-workflows.md
    ops-and-wealth-workflows.md
```

## Install

Copy `skills/financial-services-agent/` into the target agent's skills directory.

For Codex-style skill loading, the folder itself is the skill package. The required entrypoint is:

```text
skills/financial-services-agent/SKILL.md
```

## Use

Invoke explicitly with:

```text
Use $financial-services-agent to build a source-backed DCF and comps analysis for [Company].
```

It should also trigger naturally for requests involving:

- Equity research, earnings analysis, market research, sector overviews, screens, thesis tracking, and catalysts.
- DCF, comps, LBO, 3-statement models, spreadsheet audits, and model updates.
- Pitch decks, CIMs, teasers, one-pagers, buyer lists, merger models, and process letters.
- PE sourcing, deal screening, diligence, unit economics, returns analysis, IC memos, and portfolio monitoring.
- Wealth-management client reviews, financial plans, rebalancing, tax-loss harvesting, and client reports.
- Fund-admin reconciliation, month-end close, valuation review, statement audit, and KYC/onboarding checks.

## Design

The entrypoint stays intentionally small. It routes the agent to focused reference files only when needed:

- `data-and-integrity.md`: source priority, recency checks, citations, model integrity, compliance boundary.
- `workflow-router.md`: triage and sequencing for multi-vertical finance requests.
- `modeling-workflows.md`: comps, DCF, LBO, 3-statement models, and spreadsheet audit rules.
- `research-and-reports.md`: earnings, initiations, sector research, thesis trackers, catalysts, and screens.
- `deal-and-portfolio-workflows.md`: banking and private-equity workflows.
- `ops-and-wealth-workflows.md`: wealth, fund administration, finance operations, and KYC workflows.

## Validation

Validated locally with:

```text
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\Admin\Documents\AI NPC\skills\financial-services-agent
```

Result:

```text
Skill is valid!
```

## Important Boundary

Nothing in this repository is investment, legal, tax, accounting, lending, onboarding, or transaction approval advice. The skill is designed to help agents draft analyst work product for qualified human review. It should not execute trades, approve onboarding, bind risk, post ledger entries, or claim a finance output is final.

## License

Apache-2.0. See [LICENSE](LICENSE).
