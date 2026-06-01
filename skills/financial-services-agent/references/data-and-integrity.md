# Data And Integrity

Use this reference for every finance workflow that depends on current facts, regulated data, model formulas, or professional review.

## Source Priority

Use the most authoritative available source:

1. User-provided files, firm systems, and explicitly designated authoritative data.
2. Configured institutional connectors or data providers.
3. Primary public sources: SEC/EDGAR filings, investor relations releases, call transcripts, investor presentations, fund statements, official rules, and exchange/regulator materials.
4. Reputable secondary sources for context only.
5. General web search only when primary/institutional sources are unavailable or to locate primary sources.

Do not use stale training memory for current prices, latest earnings, rates, filings, company officers, regulations, fund values, or market events.

## Recency Controls

For time-sensitive tasks:

- Write down the current date in the working notes.
- Record the source publication date and data period.
- Verify that "latest" means the latest available source as of the current date.
- If a source is older than the requested period, keep searching or flag it.
- For earnings work, align earnings release, 10-Q/10-K, transcript, investor presentation, and consensus date.

## Missing Data

Never invent missing values.

- Use `N/A` for not available.
- Use `Not disclosed` for items a company/fund does not disclose.
- Use `Assumption` only when the user permits estimation or the workflow requires a model assumption.
- Label assumptions separately from reported data.
- Explain sensitivity to assumptions when the assumption drives conclusions.

## Citation Requirements

Every key table, chart, valuation driver, and material claim should cite:

- Source name.
- Source date or period.
- Retrieval date when useful.
- Link, filing accession, document name, page, tab, or system identifier where available.
- Definition differences, such as adjusted EBITDA, ARR, free cash flow, net debt, or AUM.

For spreadsheets, add comments/notes to hardcoded input cells when the tool supports it.

## Data Normalization

Before comparing or calculating:

- Normalize currency, units, fiscal year ends, period length, LTM vs annual vs quarterly, and split/share count effects.
- Reconcile GAAP/IFRS/non-GAAP definitions.
- Keep debt, lease, minority interest, pension, cash, and non-controlling interest treatments explicit.
- Avoid mixing enterprise value and equity value metrics.
- Avoid mixing actuals, guidance, and consensus without labeling.

## Model Integrity

For spreadsheet models:

- Hardcode only raw inputs and explicit assumptions.
- Use formulas for margins, multiples, growth, WACC, FCF, IRR, MOIC, sensitivity cells, and summary outputs.
- Keep source data, assumptions, calculations, and outputs visually or structurally distinct.
- Include checks for balance sheet balance, circular references, formula errors, inconsistent periods, and broken links.
- Validate every output range after formula updates.

## Compliance Boundary

Always keep outputs framed as draft work product.

Do not:

- Tell a user to buy, sell, hold, lend, approve, onboard, or execute.
- Claim suitability for a specific person unless the user provided the required suitability context and the output is framed for advisor review.
- Provide tax, legal, accounting, or regulatory advice as final guidance.
- Expose confidential or personal data unnecessarily.
- Use private data to generate public-facing content without explicit instruction.

## Final Integrity Checklist

- Current date and source dates are checked.
- Key numbers have sources or formulas.
- Assumptions are labeled.
- Missing data is not hidden.
- Units and periods are consistent.
- Outputs are staged for human review.
- Disclaimers match the workflow risk.
