# Reasoning Premium Collapse — Prediction Tracker

> **Prediction 1 (Confidence: 85%, Timeline: 6 months)**
> The "reasoning model premium" collapses. Companies that marketed "o1-class reasoning at o1-class prices" get undercut by efficient alternatives that are 3-5x cheaper.

---

## 🌐 Interactive Demo — GitHub Pages

**Live URL:** https://techfrensbot.github.io/reasoning-premium-collapse/

No cloning required — just open the URL and interact with the pricing comparison dashboard in your browser!

### Features:
- Real-time premium ratio calculation
- Visual signals for "premium collapsing" vs "intact"
- Interactive pricing table with current market data
- Hit/miss criteria tracking
- Responsive design

### To enable GitHub Pages (one-time setup):

1. Go to repo **Settings** → **Pages**
2. Select **Source: Deploy from a branch**
3. Choose **Branch: main** and folder **/(root)**
4. Click **Save**
5. GitHub will automatically deploy and provide the live URL above

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

### Local Python Script
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

### Web Interface (index.html)
Interactive dashboard with:
- Real-time premium ratio calculation
- Visual status badges
- Responsive pricing table
- Hit/miss condition tracking

---

## Status

| Date | Status | Notes |
|-------|--------|-------|
| 2026-02-04 | 🟢 Prediction made | Initial tracking setup + GitHub Pages enabled |
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
