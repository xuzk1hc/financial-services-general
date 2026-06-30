# Platform Inputs

Use this file when the source platform or export format affects ingestion.

## General Normalized Message Schema

Each message should be represented as:

```json
{"timestamp":"raw or ISO time","platform":"wechat|feishu|discord|generic","author":"speaker or alias","content":"message text","urls":[],"tickers":[],"reply_to":"","attachments":[],"reactions":{},"source_file":""}
```

Keep raw timestamps if parsing is uncertain. Do not discard attachments; describe them as placeholders such as `[image]`, `[voice]`, `[file: filename]` if content is unavailable.

## Feishu / Lark

Preferred inputs:

- exported CSV/JSON from a bot, connector, or admin export
- copied channel/thread text
- screenshots transcribed by OCR or user paste

Pay attention to:

- threaded replies, because a "hot" topic may be split across parent message and replies
- bot messages and forwarded news cards
- reactions as weak sentiment signals, not proof
- links to公告,研报,新闻, or company websites

If using Feishu API data, preserve message IDs, root message IDs, sender IDs or aliases, and create time. Do not assume the user has admin export permission; ask for an export only if no connector or pasted text is available.

## Discord

Preferred inputs:

- DiscordChatExporter JSON/CSV/TXT
- bot-exported JSON
- copied channel or thread text

Pay attention to:

- channel name and thread name as topic context
- embeds, link previews, and attachments
- reactions as sentiment or agreement signals
- deleted/edited message markers
- roles or usernames that may imply source credibility, while still avoiding personal-name exposure in final output

For DiscordChatExporter CSV, common columns include `Date`, `Author`, `Content`, `Attachments`, and `Reactions`.

## WeChat

Preferred inputs:

- copied chat transcript from desktop WeChat
- exported text/CSV produced by a backup or parser
- OCR-transcribed screenshots

Pay attention to:

- speaker and timestamp patterns vary by export tool
- voice messages, images, files, mini-program cards, and forwarded聊天记录 may contain important evidence but need transcription or user-provided context
- one user may quote another; do not double-count quoted text as independent confirmation
- stock names may appear as aliases, nicknames, or partial Chinese names

If the input is only screenshots, ask the user for OCR text or permission to inspect images when available. Do not pretend to read unprovided image content.

## Mixed Sources

When the user gives multiple platforms, normalize each source separately, then merge by time. In the final report, mark cross-platform corroboration explicitly:

- same catalyst mentioned in multiple platforms
- same ticker but different reasons
- same rumor repeated without new evidence
- platform-specific sentiment divergence
