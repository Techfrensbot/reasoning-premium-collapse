# Reasoning Premium Collapse — Prediction Tracker

> **Prediction 1 (Confidence: 85%, Timeline: 6 months)**
> The "reasoning model premium" collapses. Companies that marketed "o1-class reasoning at o1-class prices" get undercut by efficient alternatives that are 3-5x cheaper.

---

## Background

OpenAI's o1 proved that throwing more compute at inference time improves reasoning. The industry followed: spend more, think harder, win.

But DeepSeek-V3 matched o1 at roughly **70% lower inference cost**. They didn't brute-force it. They built for efficiency.

**This repo tests the prediction**: Will the "reasoning model premium" collapse as efficient alternatives become widespread?

---

## The Prediction

| Aspect | Details |
|---------|----------|
| **Prediction** | Reasoning model premiums collapse |
| **Confidence** | 85% |
| **Timeline** | 6 months (by August 2026) |
| **Key Signal** | Efficient alternatives 3-5x cheaper appear and gain traction |
| **Counter-Signal** | Premium pricing persists or expands |

---

## Tracking Methodology

This repo tracks:

1. **Pricing trends** — Per-token costs for reasoning models vs base models
2. **Efficiency improvements** — Models claiming same performance at lower cost
3. **Market signals** — Adoption rates of efficient alternatives

**Update cadence**: Weekly snapshots added to `data/` directory.

---

## Prototype

The `pricing_tracker.py` script fetches and compares pricing from major LLM providers.

**Run it**:
```bash
python pricing_tracker.py
```

It outputs a comparison table showing:
- Provider
- Model name
- Reasoning capability
- Price per 1M tokens
- Efficiency ratio

---

## Status

| Date | Status | Notes |
|-------|--------|-------|
| 2026-02-04 | 🟢 Prediction made | Initial tracking setup |
| TBD | 🔄 Ongoing | Weekly price comparisons |

---

## What Counts as "Hit" or "Miss"

### ✅ Hit Conditions
- Efficient reasoning models (3-5x cheaper) become mainstream
- Premium pricing collapses across major providers
- Market shifts to "efficiency-first" narrative

### ❌ Miss Conditions
- Premium pricing persists or expands
- "Reasoning premium" becomes even more entrenched
- Efficiency gains don't translate to price competition

---

## Contributing

Found pricing data that supports or contradicts this prediction? Add it to `data/snapshots/` with the format:
```
YYYY-MM-DD-provider-name.md
```

---

## License

MIT — Track the prediction, share the data.
