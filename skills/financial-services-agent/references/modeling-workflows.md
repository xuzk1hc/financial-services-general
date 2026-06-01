# Modeling Workflows

Use this reference for comps, DCF, LBO, 3-statement models, Excel audits, model updates, deck-linked charts, and spreadsheet-heavy finance tasks.

## Common Modeling Contract

1. Define the modeling question and audience.
2. Gather raw historical data and market data from authoritative sources.
3. Normalize periods, units, currency, fiscal years, and definitions.
4. Separate raw inputs, assumptions, calculations, checks, and outputs.
5. Use live formulas for every derived value.
6. Add source notes to hardcoded input cells when possible.
7. Run formula, sanity, and output checks before delivery.

## Comparable Company Analysis

Use for public valuation, peer benchmarking, IPO/funding support, sector overview tables, and valuation outlier analysis.

Minimum sections:

- Scope and peer inclusion/exclusion logic.
- Operating metrics: revenue, growth, margin, profitability/cash conversion, and industry-specific KPIs.
- Valuation metrics: market cap, enterprise value, EV/revenue, EV/EBITDA, P/E or sector-appropriate multiples.
- Statistics: max, 75th percentile, median, 25th percentile, min for comparable ratio/multiple columns.
- Methodology and source notes.

Quality rules:

- Use truly comparable companies; explain exclusions.
- Use consistent periods and definitions.
- Do not average irrelevant absolute size metrics.
- Include industry-specific metrics only when they answer the decision question.
- Prefer median/quartiles over simple averages for valuation framing.

## DCF Model

Use for intrinsic value, long-term cash flow valuation, WACC and terminal value analysis, or scenario/sensitivity valuation.

Minimum sections:

- Market data and capital structure.
- Historical revenue, margins, CapEx, D&A, working capital, tax rate, and FCF.
- Bear/base/bull operating assumptions.
- Projection schedule.
- WACC build.
- Terminal value.
- Enterprise value to equity value bridge.
- Sensitivity tables.

Quality rules:

- Terminal growth must be below WACC.
- Terminal value should be sanity-checked as a share of enterprise value.
- OpEx should generally scale from revenue, not gross profit.
- WACC should use market value weights where possible.
- Net debt can be negative; treat net cash correctly.
- Sensitivity tables should be centered on the base case.

## LBO Model

Use for sponsor acquisition analysis, debt capacity, returns, and exit sensitivity.

Minimum sections:

- Sources and uses.
- Purchase price and transaction assumptions.
- Operating forecast.
- Debt schedule, interest, amortization, cash sweep, covenant/coverage checks if relevant.
- Exit valuation.
- Sponsor returns: IRR and MOIC.
- Sensitivities: entry multiple, exit multiple, leverage, EBITDA growth, margin, debt paydown.

Quality rules:

- Sources must equal uses.
- Debt repayment cannot exceed available cash.
- Exit multiple and EBITDA must use consistent definitions.
- Separate management case, base case, downside case, and sponsor case when available.
- Flag circularity and financing assumptions.

## 3-Statement Model

Use for full financial statement projection, model update, or accounting-linked forecast.

Minimum sections:

- Income statement, balance sheet, cash flow statement.
- Revenue build and operating expense assumptions.
- Working capital schedules.
- Debt and interest schedules.
- D&A, CapEx, equity, and tax schedules.
- Balance checks and cash flow reconciliation.

Quality rules:

- Balance sheet must balance.
- Cash flow must reconcile beginning cash to ending cash.
- Interest should connect to debt schedule.
- Working capital should connect balance sheet movement to cash flow.
- Use one source of truth for historical data.

## Model Audit

Use when asked to debug, inspect, or review a spreadsheet.

Check:

- Formula errors, broken links, hidden hardcodes, inconsistent formulas across rows/columns.
- Inputs not labeled or sourced.
- Balance sheet and cash flow checks.
- Circular references.
- Date, period, unit, and currency consistency.
- Sensitivity tables and scenario switches.
- Output reasonableness vs history and peers.

Report issues by severity and give exact cell/sheet references when available.

## Spreadsheet Formatting

Default conventions:

- Inputs: visually distinct from formulas.
- Formulas: consistent font/color/style and no hidden hardcoded calculations.
- Sheet links: distinct when possible.
- Headers: clear section labels, units, dates, and source notes.
- Outputs: compact summary tables and sensitivity ranges.

Follow user or firm templates over defaults.
