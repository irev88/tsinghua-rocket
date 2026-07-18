# AI-Assisted Engineering Notebook: Reusable Rocket Co-Design
**Living Document** — Record of hypotheses, decisions, AI interactions, iterations, and rationale.

**Project**: Conceptual AI Co-Design of a Reusable Launch Vehicle  
**Team Context**: Summer program (3-5 members) + LLM copilot + mentors  
**Start Date**: 2026-07-18  
**Current Baseline Vehicle (will evolve)**: TBD — Strawman small-class reusable first stage (~1.5 t payload to LEO)

---

## Core Principles (enforced throughout)
1. Every major design choice must have:
   - Hypothesis / Assumption
   - Supporting analysis or literature
   - Alternatives considered
   - AI prompt + outcome
   - Final rationale
2. Uncertainty and margins are explicitly tracked.
3. Novel or non-conventional ideas are explored and documented even if not selected.
4. All numbers have sources or "first-order estimate" flag.

---

## Table of Contents
- [Mission Definition (Day 1)](#day-1-mission-definition)
- [Sizing (Day 2)](#day-2)
- ... (will expand)

---

## Project Metadata
- **Target Payload**: TBD (initially 1000–2000 kg to LEO)
- **Reusability Goal**: ≥10 flights with <15% refurb cost
- **Key Figures of Merit** (to be weighted):
  - Dry mass
  - Cost per flight
  - Reliability
  - Environmental impact (kg CO2e / kg payload)
  - Turnaround time

---

## Day 1: Mission Definition
**Date**: 2026-07-18 (setup + intensive research + drafting)

### Hypotheses
1. A 1,200 kg (threshold) to 2,000 kg (goal) payload to 500 km LEO / 700 km SSO is a viable sweet spot for a conceptual university/industry demonstrator-class reusable launcher (between small dedicated and Falcon 9-class).
2. Including explicit sustainability metrics (e.g., Green Reusability Index) + alternative recovery architectures (net capture) will drive non-obvious but realistic propellant and recovery trades.
3. Chinese 2025-2026 programs (Zhuque-3, Hyperbola-3, Long March 12A/10B) provide strong contemporary benchmarks showing rapid convergence on 8–18 t reusable class with methalox and novel recovery.

### Research Summary (Key Verified Insights)
- **Global benchmarks (2026)**: Falcon 9 ~22,800 kg reusable LEO (20+ flights common, ~$2,700/kg); New Glenn 45 t; Neutron ~13–15 t.
- **China 2025-2026 surge** (cross-checked SpaceNews, Ars Technica, China-in-Space):
  - Zhuque-3 (Landspace): 18,300 kg recovered (downrange), 21 t expendable. Maiden orbital Dec 2025 (recovery failed); recovery target mid-2026.
  - Hyperbola-3 (iSpace): 8,500 kg recovered. Targeting 2026 debut; drone ship procured.
  - Pallas-1 (Galactic Energy): 8,000 kg baseline + reusability. 3-core future 30 t.
  - Long March 12A: ~12 t expendable / lower with recovery. Methalox.
  - Long March 10B (Jul 2026): First Chinese orbital booster recovery via **net capture on sea platform** (novel architecture, no landing legs mass penalty).
- **Market**: Strong demand for 1–15 t dedicated/rideshare for constellations. Reusability driving costs toward $1,500–2,800/kg.
- **Sustainability**: Traditional RP-1/LOX ~19 t CO2e per tonne payload (LCAs). Methalox + high reuse preferred. Emerging GRI-style metrics.

**Full details**: `docs/01_mission_requirements/research_summary_2026.md` and `vehicle_comparison_table.md`.

### Requirements Work (Significant Progress)
- Created enriched `mission_requirements.md` (L0 objectives + L1/L2 table with rationale and verification).
- Added sustainability as top-level objective + Green Reusability Index (novel).
- Explicit requirement to evaluate **net-capture recovery** (grounded in 2026 LM-10B success).
- Methalox preference.
- Supporting artifacts: stakeholder analysis, initial CONOPS, risk register, traceability skeleton, vehicle comparison.

**Key Figures of Merit** (weighted):
1. Payload (reusable) — 30%
2. Recurring $/kg — 25%
3. Reusability (flights + turnaround) — 20%
4. Sustainability (GRI/CO2e) — 15%
5. Responsiveness — 10%

### AI Interactions
- Structured prompts used for requirements synthesis and alternative architectures (see `ai_logs/prompts/day01_mission_definition.md`).
- Outcomes incorporated: GRI, net-capture trade, methalox, threshold/goal values.

### Decisions & Rationale
- **Payload class**: 1,200 kg threshold / 2,000 kg goal (L0-01). Rationale: Realistic conceptual scale; matches gap between Electron-class and emerging Chinese 8 t+ vehicles.
- **Recovery baseline + novel option**: Propulsive + legs (standard) + formal evaluation of net capture. Rationale: LM-10B July 2026 success demonstrates feasible alternative that reduces dry mass.
- **Sustainability elevated**: L0 objective + dedicated FoM. Rationale: Most programs treat as secondary; research shows real traction (LCA papers, policy).
- **Propellant**: LOX/LCH4 preferred. Rationale: Dominant in 2025-2026 reusable designs (Zhuque-3, New Glenn, etc.) for reusability + emissions.

**Open Questions / High Uncertainty**:
- Exact recurring cost target (will model Day 8).
- Preferred launch site + recovery infrastructure.
- Weighting of sustainability vs pure performance.

### Next Steps (End of Day 1)
- AI co-pilot deep dive on alternatives.
- Expand traceability matrix.
- Initial mass budget strawman (transition to Day 2).
- Update data/inputs/mission_params.json.

**All numbers either directly cited from 2025-2026 sources or clearly labeled estimations.**

---

## Daily Log Template
```
### Day X — YYYY-MM-DD
**Focus**: ...
**Key Hypotheses Tested**:
**AI Prompts Used**:
**Major Outputs**:
**Decisions & Rationale**:
**Open Questions / High Uncertainty**:
**Next Steps**:
```

---

## Cross-Cutting Notes
### Uncertainty Quantification Approach
- Early days: qualitative + simple ± ranges
- Later: Monte Carlo in code/

### Sustainability Thread
Track lifecycle emissions where possible.

### Benchmark Vehicles
- SpaceX Falcon 9 (Block 5)
- Rocket Lab Neutron (in dev)
- Relativity Terran R
- Firefly Alpha (expendable baseline)
- Historical: DC-X, Kistler K-1

---

**This notebook will be the primary evidence of the scientific process and AI collaboration.**
