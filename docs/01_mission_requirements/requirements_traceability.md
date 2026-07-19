# Requirements Traceability Matrix (v1.0, refined)
**Date**: 2026-07-18 | **Status**: Refined — aligned with `mission_requirements.md` v1.0

## L0 → L1 Traceability (canonical)

| L0 ID | L0 Objective | Threshold / Goal | Linked L1 IDs | Verification Approach | Source / Rationale |
|-------|--------------|------------------|---------------|------------------------|--------------------|
| L0-01 | Payload delivery | 1,200 / 2,000 kg | L1-P01, L1-P02, L1-P03 | Trajectory sim + analysis + inspection | Market demand (constellations); Chinese 8–18 t class benchmark; Falcon 9 at 22.8 t |
| L0-02 | Reusability | 10 / 20 flights | L1-R01, L1-R02, L1-R03 | Flight test + MC + trade study | Falcon 9 20+ flights heritage; LM 10/12A family net demo 2026 (*name flagged*) |
| L0-03 | Cost efficiency | $3,500 / $2,500 per kg | L1-C01, L1-C02 | Cost model (Day 8) | Industry $2,400–2,700/kg F9 baseline; **v1.0: relaxed from $2,800/kg (optimistic for 1.2 t class)** |
| L0-04 | Sustainability | < 15 t CO₂e/t | L1-E01, L1-E02 | LCA + Day 7 model | Emerging (LCA papers 2024–2026); **v1.0: unit-consistent GRI, no fabricated numbers** |
| L0-05 | Responsiveness | 30 / 14 days | L1-O01, L1-O02 | CONOPS + ops plan | DoD responsive space; commercial constellation replenishment |
| L0-06 | Reliability | 0.95 / 0.97 compound | L1-S01, L1-O03 | RBD + MC + disposal analysis | **v1.0: ±30/±10 m landing accuracy added (L1-O03)** |

## L1 → Verification (canonical)

| L1 ID | Requirement | Threshold | Goal | Verification Method | Notes |
|-------|-------------|-----------|------|---------------------|-------|
| L1-P01 | Payload to 500 km LEO (reusable) | 1,200 kg | 2,000 kg | Trajectory sim + analysis | 1.2 t class scope |
| L1-P02 | Injection accuracy | ±20 km / ±0.05° | ±10 km / ±0.02° | Flight test + GNC analysis | Standard for SSO/LEO |
| L1-P03 | Fairing internal volume | Ø 3.4 m × 6.5 m | Ø 3.6 m × 7.0 m | Inspection | **v1.0: reduced from Ø 4.2 m × 8 m** |
| L1-R01 | Recovery success (per flight) | ≥ 0.90 | ≥ 0.98 | Flight test + Monte Carlo | **v1.0: per-flight wording made explicit** |
| L1-R02 | Reuses per first stage | 10 | 20 | Ops tracking | Falcon 9 heritage |
| L1-R03 | Recovery arch: propulsive OR net-capture | Trade closed Day 6 | — | Trade study + dynamics sim | **v1.0: net-capture explicitly evaluated** |
| L1-C01 | Recurring launch cost per flight | ≤ $4.2 M | ≤ $3.0 M | Cost model (Day 8) | **v1.0: aligned with L0-03 update** |
| L1-C02 | Refurb cost fraction of new-build | ≤ 15% | ≤ 10% | Cost model + heritage | Falcon 9 experience |
| L1-E01 | Propellant preference | LOX/LCH₄ | + bio-CH₄ option | Lifecycle assessment | **v1.0: bio-CH₄ option added** |
| L1-E02 | GRI as primary sustainability FoM | GRI ≥ 1.20×F9 (illus.) | GRI ≥ 1.35×F9 (illus.) | Day 7 quantitative model | **v1.0: unit-consistent, no fabricated values** |
| L1-S01 | Compound success, first 10 flights | ≥ 0.95 | ≥ 0.97 | RBD + Monte Carlo | Implies per-flight ≥ 0.994 / 0.997 |
| L1-O01 | Compatible launch site | Hainan (Wenchang) | + Jiuquan sea-zone | CONOPS analysis | Coastal commercial |
| L1-O02 | Dedicated + rideshare modes | Yes | Yes | Interface control doc | Market reality |
| L1-O03 | Landing accuracy (propulsive) | ±30 m | ±10 m | Flight test + MC | **v1.0: tightened from ±100 m** |

## Coverage Statistics (v1.0)

- **L0 objectives**: 6 (Payload, Reusability, Cost, Sustainability, Responsiveness, Reliability)
- **L1 requirements**: 14 (Performance 3, Reusability 3, Cost 2, Sustainability 2, Safety 1, Operations 3)
- **All L1s have**: explicit verification method
- **Novel L1s (added in v1.0)**: L1-O03 (landing accuracy), L1-R03 explicit (net-capture)

## Open Items for Day 2+

- Day 2: First-order Δv split between booster and upper stage
- Day 4: Refurb cost model with concrete materials/labour breakdown
- Day 6: Close L1-R03 propulsive vs net-capture trade
- Day 7: First quantitative GRI values to replace the illustrative multipliers
- Day 8: Cost model for L1-C01 / L1-C02 absolute values
- Day 8: Monte Carlo on L1-S01 / L1-R01 to verify per-flight success assumptions

**Reconciliation with other documents**:
- `data/inputs/mission_params.json` reflects this v1.0 weighting (30/20/25/15/10) ✓
- `engineering_notebook.md` (Day 1 entry) references these requirements ✓
- `final/Day1_Mission_Definition_Report.pdf` (v1.0) contains the same content ✓
- `final/Day1_Mission_Definition_Presentation.pptx` (v2.0, 22 slides) contains the same content ✓
- All four artefacts have been generated from a single source of truth.
