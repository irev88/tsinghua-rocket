# Day 1 Research Summary: Mission Definition for Reusable Launch Vehicle (RLV)
**Date compiled**: 2026-07-18 (based on searches conducted 2026-07-18)  
**Focus**: Broad & deep research on mission requirements, latest reusable launch vehicles (global + China emphasis), market drivers, benchmarks, sustainability, and requirements frameworks.  
**Sources**: Primarily recent 2025-2026 reports from SpaceNews, Ars Technica, China-in-Space, Global Times, company announcements, market analyses (Mordor, Emergen, etc.). Cross-checked across Western, Chinese, and industry sources. All claims verified where possible; estimates clearly labeled.

## 1. Global Context & Market Drivers (2025-2026)
- **Satellite constellations & small/medium payloads dominate demand**: LEO broadband (Starlink, Kuiper, Qianfan/Thousand Sails, Guowang), Earth observation, IoT. Small satellites (<500 kg) ~80% of launches in recent years (Satellite Industry Association via market reports). Mega-constellations drive need for high-cadence, dedicated, or rideshare launches.
- **Reusable launch vehicle (RLV) economics**: Falcon 9 reusable has driven costs to ~$2,700/kg LEO (list) or lower with high reuse (20+ flights per booster reported). Target industry: $1,500–2,500/kg for medium reusable by late 2020s. Small dedicated launchers still ~$20k–30k/kg (e.g., Electron historical). Reusability can reduce per-flight costs 30-50%+ via booster reuse.
- **Responsive launch & national security**: Growing demand for "launch on demand" (24-72h readiness) for defense, disaster response, constellation replenishment. U.S. DoD and allies prioritizing proliferated LEO.
- **Sustainability emerging**: Traditional RP-1/LOX ~19 t CO2 per tonne payload to orbit (various LCAs). Reusability + methalox + bio-propellants reduce footprint. EU/China policies pushing LCA in design. New Chinese/ESA studies on upper-atmosphere impacts (H2O, NOx, black carbon) beyond simple CO2.
- **China's rapid rise (2025-2026)**: Multiple state + commercial players targeting reusable first-stage recovery. Goal: support megaconstellations (Thousand Sails/Guowang), space station cargo, commercial. China achieved first orbital-class booster recovery (net capture on sea platform) with Long March 10B in July 2026. Multiple first flights/recovery attempts in 2025-2026.

**References**:
- SpaceNews (Jan 2025): "China to debut new Long March and commercial rockets in 2025" [spacenews.com/china-to-debut-new-long-march-and-commercial-rockets-in-2025/]
- Ars Technica (Jul 2026): "China recovered its first reusable rocket..." [arstechnica.com/space/2026/07/china-recovered-its-first-reusable-rocket-and-showed-a-new-way-to-do-it/]
- Market reports (Mordor Intelligence, Emergen Research, Strategic Market Research 2025-2026).

## 2. Latest Reusable / Reusability-Targeting Launch Vehicles (2025-2026 Data)
Cross-checked multiple sources. Payloads are **published targets** or demonstrated (as of mid-2026). "Reusable" often means first-stage only initially.

### Western / Established
- **SpaceX Falcon 9 Block 5** (operational):
  - LEO reusable: ~22,800 kg
  - Reusability: >500 landings by late 2025; 20+ flights per booster common. Cost ~$2,700/kg list (lower effective).
  - Recovery: Propulsive landing on drone ship or pad.
- **Blue Origin New Glenn** (maiden ~2025, ongoing):
  - LEO (reusable booster): 45,000 kg (7× BE-4 methalox first stage)
  - Larger fairing (7 m). Primary for Kuiper constellation + NASA.
- **Rocket Lab Neutron** (target first flight ~2026):
  - LEO reusable: 13,000–15,000 kg. Focus on constellation deployments.
- **Relativity Terran R** (development, ~2026+):
  - LEO reusable: ~23,500 kg (updated targets).
- **SpaceX Starship** (testing, partial operational):
  - LEO reusable (full stack target): 100–150+ t. Tower catch demonstrated.

### Chinese Developments (Strong Emphasis — Latest 2025-2026)
China has ~8-10 vehicles in various stages of reusable development, blending state (CASC/CALT/SAST) and commercial (Landspace, iSpace/Galactic Energy, CAS Space, etc.). Many target Falcon 9-class performance with methalox or kerolox. Rapid iteration noted (government support + competition).

- **Long March 12 / 12A (SAST/CASC, state-led, partially reusable)**:
  - Expendable LEO: ~12,000 kg (200 km); SSO (700 km): ~6,000–7,300 kg.
  - Reusable (12A variant, methalox engines "Longyun"): Lower payload with recovery (targets ~6,000 kg LEO reported in some updates).
  - Status: Long March 12 first flew Nov 2024 (expendable). 12A VTVL tests early 2025; recovery attempts ongoing. 3.8 m diameter, ~433–437 t liftoff mass.
- **Zhuque-3 (Landspace, commercial, stainless steel methalox)**:
  - Expendable LEO: 21,000 kg
  - Recovered (downrange): ~18,300 kg; RTLS variant ~12,500 kg
  - 4.5 m diameter, 76.6 m tall, 660 t liftoff, 9× Tianque-12B engines.
  - Status: Maiden orbital flight Dec 2025 (orbit achieved, recovery failed due to braking). Plans for successful recovery mid-2026, full config + higher cadence later 2026. VTVL tests in 2024. Potential Haolong cargo in 2026.
- **Hyperbola-3 (iSpace, commercial, kerolox/methalox transition)**:
  - Expendable LEO: ~13,400 kg
  - Recovered: 8,500 kg
  - ~69 m tall. Drone ship "Interstellar Return" (100 m) procured/tested 2025.
  - Status: Targeting 2026 debut (slipped from 2025). Multiple subsystem tests (grid fins, legs, second stage) late 2025. Significant funding ($729M round reported 2026).
- **Pallas-1 (Galactic Energy, commercial, kerolox)**:
  - LEO: 8,000 kg (expendable baseline); reusability planned (legs + grid fins).
  - Three-core variant (Pallas-1B): up to 30,000 kg LEO.
  - ~3.35 m diameter, 283 t liftoff. 7× CQ-50 engines.
  - Status: Assembly & static fires 2025; first flight targeted 2026 (Jiuquan or Hainan).
- **Kinetica-2 (CAS Space)**:
  - LEO: 12,000 kg; SSO: 7,800 kg. Reusability planned.
  - Selected for Qingzhou cargo spacecraft.
- **Others**: Tianlong-3 (Space Pioneer, ~17t LEO target), Long March 8A (expendable upgrade, 7t SSO), Nebula-1 (Deep Blue Aerospace, smaller ~2-8t).

**China-specific notes** (cross-verified):
- July 2026: Long March 10B achieved first Chinese orbital-class booster recovery via **net capture on sea platform** (not pure propulsive legs). Demonstrates alternative recovery architecture (reduces landing leg mass penalty).
- Drivers: Megaconstellations (Qianfan/Thousand Sails), Tiangong cargo, lunar ambitions (Long March 10 family).
- Materials: Increasing stainless steel (like Starship) for reusability/rapid production.
- Recovery methods: Propulsive + legs (Falcon-like), drone ships, emerging net/catch systems.

**References** (key):
- SpaceNews Jan 2025 (detailed table of Chinese vehicles).
- Ars Technica Jul 2026 (Long March 10B net recovery details).
- China-in-Space, Global Times, company WeChat (2025-2026 updates).
- Orbital Radar / New Space Economy comparisons (2026).

## 3. Typical Mission Requirements Structure (from Real Programs)
From NASA/ESA MRDs, SpaceX Falcon User's Guide, commercial practices:
- **Mission Statement / Objectives**
- **Payload & Orbit Requirements** (mass, volume, injection accuracy, multiple deployment)
- **Performance** (Δv margins, reliability >95-99%, availability/cadence)
- **Reusability** (target flights per booster, turnaround time, refurb cost <X% of new)
- **Cost** (recurring launch price target, e.g., <$3,000/kg)
- **Reliability & Safety** (failure probability, human-rating if applicable)
- **Environmental / Sustainability** (emissions, debris, end-of-life)
- **Operations / CONOPS** (launch sites, weather, ground ops, responsive timeline)
- **Interfaces & Constraints** (fairing, interfaces, regulatory)
- **Verification & Traceability** (how each requirement will be verified: analysis, test, inspection)

**Examples**:
- NASA/ESA: Numbered requirements (L0/L1/L2), traceability matrix (MRD → verification).
- Falcon User's Guide: Customer-focused performance envelopes, reusability services.
- Common for commercial: "Dedicated" vs "rideshare" modes; constellation-specific (plane phasing, high inclination).

**Sustainability angle** (niche opportunity):
- Emerging: Include lifecycle CO2e / kg-payload, propellant choice (methane vs RP-1 vs bio), refurbishment emissions.
- Reusability itself reduces manufacturing emissions per flight.

## 4. Key Figures of Merit (FoMs) for Our Project
- Payload to target orbit (primary)
- Cost per kg (recurring)
- Reusability (flights + turnaround days)
- Reliability
- Environmental impact (CO2e/kg or GRI — see brainstorm)
- Responsiveness / launch cadence
- Development risk / technology readiness

## 5. Identified Gaps & Opportunities for Our Conceptual Vehicle
- Most vehicles target 1–25 t class for constellations.
- China examples show rapid progress on "Falcon 9 clones" + novel recovery (net).
- Limited public detailed MRDs for new Chinese vehicles (mostly performance targets).
- Sustainability rarely a top-level requirement in current public docs but gaining traction.

**Next for Day 1**: Synthesize into requirements hierarchy. Use AI for alternatives.

*All data cross-checked; Chinese numbers from SpaceNews/China-in-Space/Global Times; Western from company sites via aggregators. Payloads are manufacturer-stated targets unless noted.*
