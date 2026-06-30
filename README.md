# Financial Services General

Portable finance-oriented skills for AI agents.

The skills are packaged as agent-neutral `SKILL.md` folders rather than Claude-specific plugins. They do not assume Claude Cowork, slash commands, Managed Agents API, or any specific MCP provider.

## What It Contains

```text
skills/group-hotspot-digest/
  SKILL.md
  agents/openai.yaml
  references/
    investment-framework.md
    output-contract.md
    platform-inputs.md
  scripts/
    normalize_chat_export.py

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

Copy the skill folder you want into the target agent's skills directory.

For Codex-style skill loading, the folder itself is the skill package. The required entrypoint is:

```text
skills/group-hotspot-digest/SKILL.md
skills/financial-services-agent/SKILL.md
```

## Use

Invoke `group-hotspot-digest` for Feishu/Lark, Discord, WeChat, CSV, JSON, JSONL, text, or pasted stock-group messages:

```text
Use $group-hotspot-digest to summarize my Feishu, Discord, or WeChat stock group messages into a hotspot investment analysis.
```

Invoke `financial-services-agent` for broader finance workflows:

```text
Use $financial-services-agent to build a source-backed DCF and comps analysis for [Company].
```

The skills should also trigger naturally for requests involving:

- Stock, finance, trading, or investment group-message digests, hotspot ranking, rumor-vs-evidence separation, and watchlist generation.
- Equity research, earnings analysis, market research, sector overviews, screens, thesis tracking, and catalysts.
- DCF, comps, LBO, 3-statement models, spreadsheet audits, and model updates.
- Pitch decks, CIMs, teasers, one-pagers, buyer lists, merger models, and process letters.
- PE sourcing, deal screening, diligence, unit economics, returns analysis, IC memos, and portfolio monitoring.
- Wealth-management client reviews, financial plans, rebalancing, tax-loss harvesting, and client reports.
- Fund-admin reconciliation, month-end close, valuation review, statement audit, and KYC/onboarding checks.

## Design

Each entrypoint stays intentionally small. It routes the agent to focused reference files only when needed:

- `group-hotspot-digest/references/platform-inputs.md`: Feishu/Lark, Discord, WeChat, and mixed export ingestion guidance.
- `group-hotspot-digest/references/investment-framework.md`: evidence tiers, hotspot scoring, theme construction, and verification rules.
- `group-hotspot-digest/references/output-contract.md`: Chinese digest, ranking table, and watchlist output shapes.
- `data-and-integrity.md`: source priority, recency checks, citations, model integrity, compliance boundary.
- `workflow-router.md`: triage and sequencing for multi-vertical finance requests.
- `modeling-workflows.md`: comps, DCF, LBO, 3-statement models, and spreadsheet audit rules.
- `research-and-reports.md`: earnings, initiations, sector research, thesis trackers, catalysts, and screens.
- `deal-and-portfolio-workflows.md`: banking and private-equity workflows.
- `ops-and-wealth-workflows.md`: wealth, fund administration, finance operations, and KYC workflows.

## Validation

Validated locally with:

```text
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py <path-to-skill-folder>
```

Result:

```text
Skill is valid!
```

## Important Boundary

Nothing in this repository is investment, legal, tax, accounting, lending, onboarding, or transaction approval advice. These skills are designed to help agents draft analyst work product for qualified human review. They should not execute trades, approve onboarding, bind risk, post ledger entries, or claim a finance output is final.

## License

Apache-2.0. See [LICENSE](LICENSE).
