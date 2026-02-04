#!/usr/bin/env python3
"""
LLM Pricing Tracker — Prototype for reasoning premium collapse prediction.

This script tracks and compares pricing data from major LLM providers,
focusing on reasoning models vs base models.

Usage:
    python pricing_tracker.py
"""

import json
from datetime import datetime
from typing import Dict, List

# Sample pricing data (in production, this would fetch from APIs)
SAMPLE_PRICING = {
    "openai": {
        "gpt-4o": {"type": "base", "price_per_1m": 2.50, "reasoning": False},
        "o1-preview": {"type": "reasoning", "price_per_1m": 15.00, "reasoning": True},
        "o1": {"type": "reasoning", "price_per_1m": 20.00, "reasoning": True},
    },
    "anthropic": {
        "claude-3.5-sonnet": {"type": "base", "price_per_1m": 3.00, "reasoning": False},
        "claude-opus": {"type": "base", "price_per_1m": 15.00, "reasoning": False},
    },
    "deepseek": {
        "deepseek-v3": {"type": "reasoning", "price_per_1m": 6.00, "reasoning": True},
    },
}


def calculate_efficiency_ratio(pricing: Dict) -> float:
    """Calculate efficiency ratio (base model price / reasoning model price)."""
    base_prices = [m["price_per_1m"] for m in pricing.values() if not m["reasoning"]]
    reasoning_prices = [m["price_per_1m"] for m in pricing.values() if m["reasoning"]]

    if not base_prices or not reasoning_prices:
        return 0.0

    avg_base = sum(base_prices) / len(base_prices)
    avg_reasoning = sum(reasoning_prices) / len(reasoning_prices)

    return avg_reasoning / avg_base


def format_pricing_table(provider: str, models: Dict) -> str:
    """Format pricing table for a provider."""
    lines = [f"\n### {provider.upper()}"]
    lines.append("| Model | Type | Price/1M tokens | Reasoning |")
    lines.append("|-------|------|----------------|-----------|")

    for model_name, data in models.items():
        model_type = "Reasoning" if data["reasoning"] else "Base"
        reasoning_icon = "✅" if data["reasoning"] else "❌"
        lines.append(f"| {model_name} | {model_type} | ${data['price_per_1m']:.2f} | {reasoning_icon} |")

    return "\n".join(lines)


def save_snapshot(data: Dict, filename: str):
    """Save pricing snapshot to data directory."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n✅ Snapshot saved: {filename}")


def analyze_premium_collapse(all_pricing: Dict) -> Dict:
    """Analyze if reasoning premium is collapsing."""
    analysis = {
        "timestamp": datetime.utcnow().isoformat(),
        "providers": {},
        "summary": {},
    }

    base_prices_all = []
    reasoning_prices_all = []

    for provider, models in all_pricing.items():
        base_prices = [m["price_per_1m"] for m in models.values() if not m["reasoning"]]
        reasoning_prices = [m["price_per_1m"] for m in models.values() if m["reasoning"]]

        if base_prices and reasoning_prices:
            avg_base = sum(base_prices) / len(base_prices)
            avg_reasoning = sum(reasoning_prices) / len(reasoning_prices)
            ratio = avg_reasoning / avg_base

            analysis["providers"][provider] = {
                "avg_base_price": round(avg_base, 2),
                "avg_reasoning_price": round(avg_reasoning, 2),
                "premium_ratio": round(ratio, 2),
            }

            base_prices_all.extend(base_prices)
            reasoning_prices_all.extend(reasoning_prices)

    # Calculate overall market premium
    if base_prices_all and reasoning_prices_all:
        overall_base = sum(base_prices_all) / len(base_prices_all)
        overall_reasoning = sum(reasoning_prices_all) / len(reasoning_prices_all)
        overall_ratio = overall_reasoning / overall_base

        analysis["summary"] = {
            "overall_base_avg": round(overall_base, 2),
            "overall_reasoning_avg": round(overall_reasoning, 2),
            "overall_premium_ratio": round(overall_ratio, 2),
            "collapse_threshold": 3.0,  # 3-5x cheaper as predicted
            "premium_collapsing": overall_ratio < 3.0,
        }

    return analysis


def main():
    """Main entry point."""
    print("🔍 LLM Pricing Tracker — Reasoning Premium Collapse Prediction\n")
    print("=" * 60)

    # Display pricing tables
    for provider, models in SAMPLE_PRICING.items():
        print(format_pricing_table(provider, models))

    # Analyze premium collapse
    analysis = analyze_premium_collapse(SAMPLE_PRICING)

    print("\n" + "=" * 60)
    print("📊 ANALYSIS")
    print("=" * 60)

    summary = analysis["summary"]
    if summary:
        print(f"\nBase model average: ${summary['overall_base_avg']:.2f}/1M tokens")
        print(f"Reasoning model average: ${summary['overall_reasoning_avg']:.2f}/1M tokens")
        print(f"Premium ratio: {summary['overall_premium_ratio']}x")

        if summary["premium_collapsing"]:
            print("\n✅ SIGNAL: Premium may be collapsing (ratio < 3.0)")
        else:
            print("\n❌ SIGNAL: Premium intact (ratio ≥ 3.0)")

        print(f"\nPrediction status: 6-month timeline → {summary['collapse_threshold']}x collapse threshold")

    # Save snapshot
    save_snapshot(analysis, "data/snapshots/latest.json")


if __name__ == "__main__":
    main()
