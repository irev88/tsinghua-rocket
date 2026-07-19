# Day 1 Figures — Visualisations & Source Code

This folder contains **14 publication-quality PNG figures** + **2 interactive Plotly HTML pages** for the Day 1 Mission Definition deliverable.

## Regenerating

```bash
cd /home/user/tsinghua-rocket
python3 figures/day01/generate_figures.py
```

Dependencies: `numpy`, `matplotlib`, `plotly`, `kaleido`.

## Figure Index

| # | Filename | Type | Topic | Used in |
|---|----------|------|-------|---------|
| 1 | `payload_comparison.png` | Horizontal bar | LEO payload capacity of 7 vehicles (2026) | Report Fig 3, PPT 16 |
| 2 | `fom_radar.png` | **Radar / Spider** | 5-axis FoM comparison (CRLV-1 vs F9 vs Zhuque-3) | Report Fig 4, PPT 16 |
| 3 | `cost_trend.png` | Line + uncertainty band | Falcon 9 cost trajectory 2015-2026 | Report Fig 5, PPT 17 |
| 4 | `cost_uncertainty_band.png` | **Lognormal distribution** | L0-03 cost target with P(threshold) annotation | PPT 18 |
| 5 | `gri_comparison.png` | Conceptual framework | GRI unit-consistent definition (no fabricated numbers) | Report Fig 1, PPT 12 |
| 6 | `gri_levers.png` | Horizontal bar with confidence bounds | Qualitative GRI design lever ranking | Report Fig 2, PPT 13 |
| 7 | `dv_budget_sankey.png` | **Stacked horizontal bar** (Sankey-like) | Δv budget allocation for 500 km LEO | (Report § intro) |
| 8 | `requirements_treemap.png` | **Treemap (2-row)** | 14 L1 across 6 categories with sub-labels | Report Fig 11, PPT 10 |
| 9 | `requirements_tree.png` | Vertical bar | L1 count by category | (supplementary) |
| 10 | `recovery_architecture.png` | **Side-by-side schematic** | Propulsive vs net-capture recovery | Report Fig 7, PPT 15 |
| 11 | `concept_sketch.png` | **Annotated technical drawing** | CRLV-1 Day 1 strawman with spec box | Report Fig 8, PPT 19 |
| 12 | `trajectory_profile.png` | Dual-panel (ascent/descent) | Altitude-velocity flight profile | Report Fig 9 |
| 13 | `fom_weights.png` | Donut pie | Level-0 FoM weighting (30/20/25/15/10) | Report Fig 10 |
| 14 | `gantt_10day.png` | **Annotated Gantt** | 10-day programme schedule with Day 1 highlighted | Report Fig 12, PPT 22 |
| 15 | `interactive_radar.html` | **Interactive Plotly radar** | Hover for exact values; downloadable as PNG | (linked in PPT) |
| 16 | `interactive_payload.html` | **Interactive Plotly bar** | Colour-coded by indicative $/kg; hover details | (linked in PPT) |

## Design Conventions

- **Palette**: muted academic (NAVY `#1A3C6E`, TEAL, GOLD, ROSE, SAGE, VIOLET, SLATE) — accessible for color-blind readers
- **Typography**: DejaVu Sans (matplotlib default); Chinese-capable when CJK font available
- **All quantitative claims** are either sourced or explicitly labelled as *estimate* / *illustrative* / *reference*
- **No fabricated GRI numbers** — the v0 1.00/1.15/1.35 bar chart has been removed; replaced with a unit-consistent framework

## What's new vs. the v0.2 (initial) set

| Added (v1.0+ → v2.0) | Replaced / Improved |
|----------------------|---------------------|
| `fom_radar.png` (radar) | `payload_comparison.png` (cleaner typography, class bands) |
| `cost_uncertainty_band.png` (lognormal) | `cost_trend.png` (with annotations + threshold line) |
| `dv_budget_sankey.png` (Δv Sankey-like) | `gri_comparison.png` (replaced bar chart with framework) |
| `requirements_treemap.png` (treemap, 2-row) | `fom_weights.png` (donut with central annotation) |
| `recovery_architecture.png` (side-by-side schematic) | `gri_levers.png` (added confidence bands) |
| `concept_sketch.png` (annotated vehicle) | `gantt_10day.png` (clean labels, decision gates) |
| `trajectory_profile.png` (ascent + descent) | `requirements_tree.png` (color-coded by category) |
| `interactive_radar.html` (Plotly) | — |
| `interactive_payload.html` (Plotly) | — |
