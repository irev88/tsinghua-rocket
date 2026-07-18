# AI Prompt Log — Day 1: Mission Definition
**Date**: 2026-07-18 (setup phase)
**Models considered**: Various (Claude/GPT as copilot)

## Prompt 1 (Research Synthesis)
```
You are a senior systems engineer with experience on Falcon 9 and Chinese commercial programs.

Given the following 2026 reference data:
- Zhuque-3: 18.3 t recovered LEO
- Hyperbola-3: 8.5 t recovered
- Pallas-1: 8 t baseline + reusability planned
- Long March 10B: successful net-capture recovery (first for China, July 2026)
- Falcon 9: 22.8 t reusable, >20 flights common
- Market: strong demand for 1-15 t class for constellations

Propose a complete set of Level-0 and Level-1 mission requirements for a conceptual 1.2–2 t to LEO reusable vehicle. Include:
1. At least one novel sustainability or recovery requirement
2. Threshold vs goal values
3. Clear rationale tied to real vehicles
4. Suggested figures of merit
```

**Outcome summary**: Used to enrich mission_requirements.md. Suggested GRI, net-capture evaluation, and methalox preference.

## Prompt 2 (Alternative Architectures)
```
Act as chief engineer. For a small reusable launcher targeting dedicated constellation support:
- Generate 4 alternative mission concepts (beyond standard propulsive landing + methalox).
- For each, list top 3 requirements impacts and one major risk.
- Prioritize ideas that are novel yet grounded in 2025-2026 Chinese or global developments (e.g. net capture, sustainability).
```

**Follow-ups logged in decisions/**.
