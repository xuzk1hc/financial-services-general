# Output Contract

Default language: Chinese.

## Default Report

```markdown
# 群消息热点投资分析 - YYYY-MM-DD

## 一句话结论
- ...

## 数据范围与可信度
- 来源:
- 时间窗口:
- 消息量:
- 可信度限制:

## 今日热点排序
| 排名 | 热点/主题 | 热度 | 核心逻辑 | 证据等级 | 相关标的 | 主要风险 |
|---|---:|---:|---|---|---|---|

## 高频标的/概念表
| 标的/概念 | 被提及原因 | 情绪 | 证据 | 是否需要核验 | 下一步看点 |
|---|---|---|---|---|---|

## 核心催化剂与证据等级
| 催化剂 | 群内说法 | 公开证据 | 等级 | 备注 |
|---|---|---|---|---|

## 多空分歧
- 多头观点:
- 空头/质疑:
- 我的判断:

## 需要排除的噪音/谣言
- ...

## 明日跟踪清单
| 跟踪项 | 看什么 | 触发条件 | 可能影响 |
|---|---|---|---|
```

## Short Digest

Use this when the user asks for a quick recap:

```markdown
## 群聊速览
- 最热主题:
- 最常被提及标的:
- 最强催化剂:
- 最大疑点:
- 明天优先核验:
```

## Daily Tracking Table

Use this when the user wants repeated logging or Excel conversion:

| date | platform | theme | ticker | catalyst | evidence_tier | sentiment | confidence | watch_signal | source_note |
|---|---|---|---|---|---|---|---|---|---|

## Writing Style

- Keep the report compact and decision-useful.
- Prefer "这条线索值得跟踪" over "建议买入".
- Quote only short message fragments when necessary; otherwise paraphrase.
- Use `未核验`, `群内说法`, `公开可证`, and `我的推断` labels clearly.
