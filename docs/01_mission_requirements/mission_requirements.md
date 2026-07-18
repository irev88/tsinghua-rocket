# Mission Requirements Document
**Version**: 0.2 (Research-enriched draft)  
**Date**: 2026-07-18  
**Status**: Early draft — subject to iteration. Not final deliverable.  
**Purpose**: Establish measurable mission requirements for a conceptual small-to-medium reusable launch vehicle (RLV), informed by 2025-2026 global and Chinese developments.

## 1. Mission Statement
Develop a conceptual partially reusable launch vehicle capable of delivering **1,200–2,000 kg** to low Earth orbit (LEO) or sun-synchronous orbit (SSO) with **≥10 reuses** of the first stage, competitive recurring cost per kilogram (< $3,000/kg target), and explicit sustainability considerations. The vehicle shall support dedicated and rideshare missions for commercial constellations, scientific payloads, and responsive national needs.

**Rationale** (from research): Aligns with emerging Chinese commercial vehicles (Pallas-1 ~8 t baseline, Hyperbola-3 recovered ~8.5 t, Zhuque-3 recovered ~18 t) while targeting a realistic conceptual "university/industry demonstrator" class. Falcon 9 sets the benchmark at ~22.8 t reusable. Focus on 1-2 t class allows meaningful reusability trades without over-scoping.

## 2. Top-Level Objectives (L0)
- **L0-01 Payload Delivery**: Deliver 1,200 kg (threshold) to 2,000 kg (goal) payload to 500 km circular LEO or 700 km SSO at ≥95% success probability.
- **L0-02 Reusability**: First stage reusable for minimum 10 flights (threshold) / 20 flights (goal) with <15% refurbishment cost relative to new stage.
- **L0-03 Cost Efficiency**: Recurring launch cost target < $2,800/kg to LEO (threshold) / <$2,000/kg (goal) including recovery/refurb.
- **L0-04 Sustainability**: Lifecycle CO2-equivalent emissions < 15 t CO2e per tonne payload delivered (estimation based on industry LCAs; see research).
- **L0-05 Responsiveness**: Capable of launch within 30 days of payload integration for dedicated missions (goal: 14 days for high-priority).
- **L0-06 Reliability**: Overall mission success probability ≥ 0.95 for first 10 flights.

## 3. Key Requirements Hierarchy (L1 / L2 examples)
### Performance & Orbit
| ID     | Requirement                                      | Rationale (Research-backed)                                                                 | Verification Method     |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------|-------------------------|
| L1-P01 | Payload mass to 500 km LEO ≥ 1,200 kg (reusable config) | Matches small/medium class needs for constellations; below Falcon 9 but above many dedicated small launchers. Chinese Pallas-1 baseline ~8 t but scaled concept. | Analysis + simulation |
| L1-P02 | Injection accuracy: ±20 km altitude, ±0.05° inclination | Standard for commercial SSO/LEO (Falcon 9, Neutron targets). | Analysis + test        |
| L1-P03 | Fairing volume: ≥ 4.2 m diameter × 8 m height   | Accommodates multiple smallsats or single medium payload. Chinese vehicles use 4.2–5.2 m. | Inspection             |

### Reusability & Recovery
| ID     | Requirement                                      | Rationale                                                                                   | Verification |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------|--------------|
| L1-R01 | First-stage recovery success rate ≥ 90% after 5 flights | Falcon 9 >99% recent; Chinese Long March 10B demonstrated net capture July 2026 as alternative to legs. | Flight test + analysis |
| L1-R02 | Turnaround time between flights ≤ 30 days (goal 14 days) | Critical for economics (Falcon 9 rapid reuse model). Chinese programs emphasize cadence for megaconstellations. | Operations simulation |
| L1-R03 | Recovery method: Propulsive landing + grid fins (baseline); evaluate net-capture alternative | Propulsive dominant (SpaceX, Blue Origin, most Chinese). Net capture (LM-10B 2026) reduces leg mass penalty. | Trade study + sim |

### Cost & Economics
| ID     | Requirement                                      | Rationale                                                                                   | Verification |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------|--------------|
| L1-C01 | Recurring cost per flight ≤ $3.5M (threshold for 1,200 kg class) | Derived from Falcon 9 ~$67-70M for 22.8 t → ~$3k/kg. Smaller vehicles higher $/kg but dedicated advantage. | Cost model |
| L1-C02 | Refurbishment cost < 10% of first-stage manufacturing cost | Falcon 9 experience: major savings from reuse (20+ flights). | Cost model + heritage data |

### Environmental & Sustainability (Novel Emphasis)
| ID     | Requirement                                      | Rationale                                                                                   | Verification |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------|--------------|
| L1-E01 | Propellant choice: LOX/LCH4 preferred (or bio-derived alternatives) | Lower carbon vs RP-1/kerosene (~19 t CO2/t payload historical). Chinese Zhuque-3, LM-12A use methalox. | Lifecycle assessment |
| L1-E02 | Include "Green Reusability Index" (GRI) as figure of merit: payload / (CO2e/flight + refurb penalty) | Emerging from LCA studies (2024-2026 papers). Not standard today but differentiates. | Model + literature |

### Reliability, Safety, Operations
| ID     | Requirement                                      | Rationale                                                                                   | Verification |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------------------|--------------|
| L1-S01 | Mission reliability ≥ 0.95 (first 10 flights)   | Falcon 9 Block 5 very high; new Chinese vehicles targeting rapid maturity. | Reliability block diagram |
| L1-O01 | Launch sites: Compatible with Hainan (Wenchang commercial) or Jiuquan-style + sea recovery | Matches Chinese commercial (Wenchang, Jiuquan) and global (Florida, New Zealand). | CONOPS analysis |
| L1-O02 | Support rideshare + dedicated modes             | Market reality: constellations use both (SpaceX Transporter rideshares + dedicated Neutron). | Interface control |

## 4. Constraints & Assumptions
- **Assumptions** (clearly labeled estimates where not sourced):
  - Target orbit class: Primarily 500–700 km LEO/SSO (most constellation demand).
  - Staging: Two-stage, reusable booster + expendable upper (common for this class per 2026 vehicles).
  - Propellant: Initially LOX/LCH4 (modern reusable standard — SpaceX Raptor, Chinese Tianque/Longyun).
  - **Estimation**: Structural coefficient ~0.08–0.10 for reusable first stage (based on Falcon 9 public trends; not exact).
  - Regulatory: Assume commercial licensing pathway similar to FAA / Chinese commercial approvals.
- **Constraints**:
  - No human rating required.
  - Use of existing or near-term technology (TRL ≥ 6 for key elements).
  - Budget realism for conceptual study.

## 5. Success Criteria
- At least 15–20 Level-1 requirements with traceability.
- Clear distinction between threshold (minimum viable) and goal (stretch) values.
- Documented trade space for recovery method, propellant, and sustainability.
- Initial comparison table vs 4–5 reference vehicles (Falcon 9, Neutron, Zhuque-3 recovered, Pallas-1, Hyperbola-3 recovered).

## 6. Figures of Merit (Weighted)
1. Payload delivered (reusable config) — 30%
2. Recurring cost per kg — 25%
3. Reusability (flights × reliability / turnaround) — 20%
4. Sustainability (GRI or CO2e/kg) — 15% (novel)
5. Responsiveness / operational flexibility — 10%

## References & Data Sources
(See full `research_summary_2026.md` for exhaustive list and cross-checks)
- SpaceNews (2025): China vehicle debut plans (Zhuque-3: 18.3 t recovered; Pallas-1: 8 t; Hyperbola-3: 8.5 t recovered).
- Ars Technica (Jul 2026): Long March 10B net recovery — first Chinese orbital booster recovery.
- Orbital Radar / company data (2026): Falcon 9 22,800 kg reusable; New Glenn 45 t.
- Market analyses (2025-2026): Cost trends $2,700/kg Falcon 9 reusable; small launchers higher.
- LCA references: Traditional RP-1 ~19 t CO2/t payload; reusability + methalox benefits.

**AI Assistance**: Prompts and decisions logged in `../../ai_logs/`.

**Next Steps**: Stakeholder analysis, detailed CONOPS, Monte Carlo on key parameters, full traceability matrix. Iterate after AI co-design session.

*This is a working draft. All quantitative values subject to refinement in later days.*
