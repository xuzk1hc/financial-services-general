---
name: group-hotspot-digest
description: Summarize and analyze stock, finance, trading, or investment group messages from Feishu/Lark, Discord, WeChat, pasted chat logs, CSV, JSON, JSONL, or text exports. Use when the user wants a chat-group digest, market hotspot recap, theme/sector heat ranking, ticker mention analysis, rumor-vs-evidence separation, or an investable watchlist generated from group discussion rather than from a single news article.
---

# Group Hotspot Digest

## Overview

Turn noisy finance-group messages into a structured Chinese investment digest. Preserve the boundary between what the group said, what is publicly verified, and what is only a watch item.

## Workflow

1. Identify the source platform and input form: Feishu/Lark, Discord, WeChat, pasted text, CSV, JSON, JSONL, screenshots transcribed by the user, or mixed exports.
2. Normalize the message stream before analysis.
   - If the user provides files, run `scripts/normalize_chat_export.py` when useful.
   - If the user pastes a short transcript, normalize mentally and continue.
   - Read `references/platform-inputs.md` when platform-specific parsing or export quirks matter.
3. Build a signal table with timestamp, speaker or anonymized speaker, content, mentioned tickers, mentioned sectors, links, screenshots/attachments, reactions, replies, and repeated claims.
4. Separate signal types:
   - market fact: index, price action, volume,公告,财报,政策,订单,产能,融资,监管,宏观 data
   - group interpretation: thesis, rumor, channel check, trader positioning, sentiment
   - noise: jokes,重复表态,无来源喊单,情绪宣泄
5. Score hotspots by breadth, recurrence, recency, specificity, source quality, cross-platform corroboration, and link to near-term catalysts. Do not let one loud speaker dominate the ranking.
6. Verify only what is needed for the requested output. If live facts, current prices, laws, filings, breaking news, or official confirmations matter, use browsing or available market-data tools and cite sources. If verification is not possible, label the claim as unverified.
7. Generate the digest using `references/output-contract.md`. For investment judgment and evidence tiers, read `references/investment-framework.md`.

## Guardrails

- Never present the digest as direct buy/sell advice. Frame outputs as hotspots, theses, risks, and follow-up checks.
- Keep group claims, public evidence, and your inference in separate lanes.
- Mark rumors, screenshots without source, and "friend/channel said" claims as low-confidence until independently verified.
- Protect privacy by default: summarize speaker patterns without exposing personal names unless the user explicitly needs attribution.
- For Chinese A-share discussions, normalize stock codes and company names when possible, but do not invent mappings.
- For crypto, options, leverage, or illiquid small caps, surface liquidity, volatility, and compliance risk early.

## Output Shape

Default to Chinese. Unless the user asks for a shorter note, produce:

1. `一句话结论`
2. `数据范围与可信度`
3. `今日热点排序`
4. `高频标的/概念表`
5. `核心催化剂与证据等级`
6. `多空分歧`
7. `需要排除的噪音/谣言`
8. `明日跟踪清单`

If the user asks for a file, create a Markdown report by default; create Excel only when they ask for tables, tracking, or repeated daily logging.

## Resources

- `scripts/normalize_chat_export.py`: normalize common Feishu, Discord, WeChat, CSV, JSON, JSONL, and text exports into JSONL messages.
- `references/platform-inputs.md`: source-specific ingestion guidance.
- `references/investment-framework.md`: scoring, evidence tiers, and analysis rules.
- `references/output-contract.md`: report/table templates.
