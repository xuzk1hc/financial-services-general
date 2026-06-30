#!/usr/bin/env python3
"""Normalize Feishu, Discord, WeChat, CSV, JSON, JSONL, or text chat exports."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


TIME_KEYS = (
    "timestamp",
    "time",
    "date",
    "datetime",
    "created_at",
    "create_time",
    "send_time",
    "发送时间",
    "时间",
    "日期",
)
AUTHOR_KEYS = (
    "author",
    "sender",
    "user",
    "username",
    "name",
    "nickname",
    "from",
    "发送人",
    "用户",
    "昵称",
    "成员",
)
CONTENT_KEYS = (
    "content",
    "message",
    "text",
    "body",
    "msg",
    "plain_text",
    "消息",
    "内容",
    "文本",
)
URL_RE = re.compile(r"https?://[^\s<>\]\)\"']+")
TICKER_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:\$\w{1,12}|[A-Z]{2,5}(?:\.[A-Z]{1,3})?|[036]\d{5}|[489]\d{5}|HK:?\d{4,5})(?![A-Za-z0-9])"
)
INLINE_RE = re.compile(
    r"^\[?(?P<time>\d{4}[-/]\d{1,2}[-/]\d{1,2}[ T]\d{1,2}:\d{2}(?::\d{2})?)\]?\s+(?P<author>.{1,60}?)[：:]\s*(?P<content>.*)$"
)
DISCORD_RE = re.compile(
    r"^\[(?P<time>[^\]]+)\]\s+(?P<author>.{1,80}?):\s*(?P<content>.*)$"
)
WECHAT_HEADER_RE = re.compile(
    r"^(?P<author>.{1,60})\s+(?P<time>\d{4}[-/]\d{1,2}[-/]\d{1,2}\s+\d{1,2}:\d{2}(?::\d{2})?)$"
)


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\ufeff", "").replace("\u200b", "")
    return re.sub(r"\s+", " ", text).strip()


def nested_get(obj: dict[str, Any], keys: Iterable[str]) -> str:
    lowered = {str(k).lower().strip(): v for k, v in obj.items()}
    for key in keys:
        if key in obj and obj[key] not in (None, ""):
            return clean_text(obj[key])
        lower_key = key.lower().strip()
        if lower_key in lowered and lowered[lower_key] not in (None, ""):
            return clean_text(lowered[lower_key])
    for key in keys:
        lower_key = key.lower().strip()
        for actual, value in lowered.items():
            if lower_key in actual and value not in (None, ""):
                return clean_text(value)
    return ""


def nested_author(value: Any) -> str:
    if isinstance(value, dict):
        return (
            nested_get(value, ("name", "nickname", "username", "display_name", "id"))
            or clean_text(value)
        )
    return clean_text(value)


def extract_record(
    raw: dict[str, Any],
    platform: str,
    source_file: str,
    index: int,
) -> dict[str, Any] | None:
    timestamp = nested_get(raw, TIME_KEYS)
    author = nested_get(raw, AUTHOR_KEYS)
    content = nested_get(raw, CONTENT_KEYS)

    if not author:
        for key in ("author", "sender", "user", "from"):
            if isinstance(raw.get(key), dict):
                author = nested_author(raw[key])
                break
    if not content and isinstance(raw.get("text"), dict):
        content = nested_get(raw["text"], ("content", "text", "plain_text"))

    attachments = []
    for key in ("attachments", "files", "images", "embed", "embeds"):
        value = raw.get(key)
        if value:
            attachments.append(clean_text(value))

    return make_record(
        platform=platform,
        timestamp=timestamp,
        author=author or "unknown",
        content=content,
        attachments=attachments,
        source_file=source_file,
        source_index=index,
    )


def make_record(
    platform: str,
    timestamp: str,
    author: str,
    content: str,
    attachments: list[str] | None,
    source_file: str,
    source_index: int,
) -> dict[str, Any] | None:
    content = clean_text(content)
    if not content and not attachments:
        return None
    return {
        "timestamp": clean_text(timestamp),
        "platform": platform,
        "author": clean_text(author) or "unknown",
        "content": content,
        "urls": URL_RE.findall(content),
        "tickers": sorted(set(TICKER_RE.findall(content))),
        "attachments": attachments or [],
        "source_file": source_file,
        "source_index": source_index,
    }


def load_csv(path: Path, platform: str) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    records = [
        record
        for idx, row in enumerate(rows, start=1)
        if (record := extract_record(row, platform, str(path), idx))
    ]
    return records


def load_json(path: Path, platform: str) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict):
        for key in ("messages", "data", "items", "records", "results"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise ValueError("JSON input must be an object, a list, or contain a messages/data/items list")
    return [
        record
        for idx, row in enumerate(data, start=1)
        if isinstance(row, dict)
        if (record := extract_record(row, platform, str(path), idx))
    ]


def load_jsonl(path: Path, platform: str) -> list[dict[str, Any]]:
    records = []
    with path.open("r", encoding="utf-8-sig") as handle:
        for idx, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if isinstance(row, dict):
                record = extract_record(row, platform, str(path), idx)
                if record:
                    records.append(record)
    return records


def flush_text_message(
    records: list[dict[str, Any]],
    platform: str,
    source_file: str,
    source_index: int,
    current: dict[str, Any] | None,
) -> None:
    if not current:
        return
    record = make_record(
        platform=platform,
        timestamp=current.get("timestamp", ""),
        author=current.get("author", "unknown"),
        content="\n".join(current.get("lines", [])),
        attachments=[],
        source_file=source_file,
        source_index=source_index,
    )
    if record:
        records.append(record)


def load_text(path: Path, platform: str) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    records: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    last_index = 0

    for idx, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        match = INLINE_RE.match(line) or DISCORD_RE.match(line)
        if match:
            flush_text_message(records, platform, str(path), last_index, current)
            current = {
                "timestamp": match.group("time"),
                "author": match.group("author"),
                "lines": [match.group("content")],
            }
            last_index = idx
            continue
        header = WECHAT_HEADER_RE.match(line)
        if header:
            flush_text_message(records, platform, str(path), last_index, current)
            current = {
                "timestamp": header.group("time"),
                "author": header.group("author"),
                "lines": [],
            }
            last_index = idx
            continue
        if current:
            current["lines"].append(line)
        else:
            current = {"timestamp": "", "author": "unknown", "lines": [line]}
            last_index = idx

    flush_text_message(records, platform, str(path), last_index, current)
    return records


def anonymize(records: list[dict[str, Any]]) -> None:
    mapping: dict[str, str] = {}
    for record in records:
        author = record.get("author") or "unknown"
        if author not in mapping:
            digest = hashlib.sha1(author.encode("utf-8")).hexdigest()[:6]
            mapping[author] = f"user_{len(mapping) + 1:03d}_{digest}"
        record["author"] = mapping[author]


def infer_format(path: Path, explicit: str) -> str:
    if explicit != "auto":
        return explicit
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".json":
        return "json"
    if suffix in (".jsonl", ".ndjson"):
        return "jsonl"
    return "text"


def write_jsonl(records: list[dict[str, Any]], output: Path | None) -> None:
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records]
    payload = "\n".join(lines)
    if payload:
        payload += "\n"
    if output:
        output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)


def write_stats(records: list[dict[str, Any]], output: Path) -> None:
    stats = {
        "message_count": len(records),
        "unique_authors": len({record.get("author") for record in records}),
        "platforms": sorted({record.get("platform") for record in records}),
        "top_tickers": {},
        "top_urls": {},
    }
    ticker_counts: dict[str, int] = {}
    url_counts: dict[str, int] = {}
    for record in records:
        for ticker in record.get("tickers", []):
            ticker_counts[ticker] = ticker_counts.get(ticker, 0) + 1
        for url in record.get("urls", []):
            url_counts[url] = url_counts.get(url, 0) + 1
    stats["top_tickers"] = dict(sorted(ticker_counts.items(), key=lambda item: item[1], reverse=True)[:30])
    stats["top_urls"] = dict(sorted(url_counts.items(), key=lambda item: item[1], reverse=True)[:30])
    output.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Chat export file: CSV, JSON, JSONL, or text")
    parser.add_argument("--platform", default="generic", choices=("generic", "feishu", "lark", "discord", "wechat"))
    parser.add_argument("--format", default="auto", choices=("auto", "csv", "json", "jsonl", "text"))
    parser.add_argument("--output", type=Path, help="Output JSONL path. Defaults to stdout.")
    parser.add_argument("--stats-output", type=Path, help="Optional JSON summary stats path.")
    parser.add_argument("--anonymize-authors", action="store_true", help="Replace author names with stable aliases.")
    parser.add_argument("--min-content-length", type=int, default=1, help="Drop messages shorter than this length.")
    args = parser.parse_args()

    fmt = infer_format(args.input, args.format)
    if fmt == "csv":
        records = load_csv(args.input, args.platform)
    elif fmt == "json":
        records = load_json(args.input, args.platform)
    elif fmt == "jsonl":
        records = load_jsonl(args.input, args.platform)
    else:
        records = load_text(args.input, args.platform)

    records = [
        record
        for record in records
        if len(clean_text(record.get("content", ""))) >= args.min_content_length or record.get("attachments")
    ]
    if args.anonymize_authors:
        anonymize(records)
    write_jsonl(records, args.output)
    if args.stats_output:
        write_stats(records, args.stats_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
