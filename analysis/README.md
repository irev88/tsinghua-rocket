# analysis/ — Trade Studies, Sensitivity, and Uncertainty Quantification

## Purpose
Store quantitative analysis artifacts that support design decisions.

## Subdirectories
- `trade_studies/` — Propulsion trades, recovery trades, materials, etc.
- `sensitivity/` — One-at-a-time and global sensitivity results
- `uq/` — Monte Carlo, probabilistic results, margins

## Conventions
- Every study should have:
  - `*_trade.py` or notebook
  - Output tables (CSV)
  - Figures in `../figures/analysis/`
  - Short `summary.md`
- Record assumptions and limitations clearly.

## Current Status
Initial structure created 2026-07-18. Content will be added starting Day 2–3.
