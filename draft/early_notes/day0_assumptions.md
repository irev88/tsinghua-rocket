# Early Notes: Day 0 / Setup Assumptions & Starting Points
**Written**: 2026-07-18

## Key Starting Assumptions (to be validated/challenged)
- Payload class: ~1,200 kg to LEO (small-to-medium reusable first stage focus)
- Reusability target: 10–20 flights
- Propellant: Initially assume LOX/LCH4 (modern choice) but will trade
- Recovery: Propulsive landing (baseline), but will explore alternatives
- Vehicle architecture: Two-stage, with reusable booster + expendable upper (common for this class)
- First-order models sufficient for conceptual phase

## Literature / Reference Starting Points
- Falcon 9 Block 5 technical summaries (public data)
- Rocket equation applications in textbooks (Sutton, Humble)
- Reusable vehicle papers from AIAA, IAC
- Open-source trajectory tools: RocketPy, OpenRocket

## Open Questions from Setup
- How aggressive should we be on novel ideas vs solid fundamentals?
- Should we pick a specific launch site early (affects trajectory)?
- Interest in including avionics / GNC at any depth?

## Quick Calculations (back-of-envelope)
- Rough delta-v to LEO for reusable booster: ~3.5–4 km/s total for stage (including gravity + drag + recovery)
- Isp target: 330–340 s (sea level) for methalox

**Next**: Challenge these heavily on Day 1.
