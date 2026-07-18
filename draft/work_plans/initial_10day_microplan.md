# Initial 10-Day Micro-Plan (Draft)
**Date written**: 2026-07-18  
**Status**: Brainstorm / subject to heavy revision  
**Authors**: Setup agent + future team input

## High-Level Philosophy
- Focus on *process* over perfect numbers.
- Daily output > perfection.
- Use AI aggressively for acceleration but document everything.
- Reserve 20% time for exploration of 1-2 novel ideas.

## Day-by-Day Rough Allocation (hours are approximate)

**Day 1 (Mission Definition)** — 6-7h
- 2h: Research + requirements decomposition
- 1.5h: AI session on requirements
- 1.5h: Write first draft mission reqs
- 1h: Stakeholder map + risk register
- Evening: Log everything

**Day 2 (Fundamentals & Sizing)** — 7h
- Implement basic rocket equation + staging tool
- Run sensitivity on key params
- Produce first mass budget table
- AI: "Give me 4 alternative vehicle architectures"

**Day 3 (Propulsion)**
- Engine database
- Trade matrix (Isp vs thrust vs cost vs reusability)
- Preliminary tank sizing

**Day 4 (Mass & Materials)**
- Detailed mass roll-up
- Material trade study (focus on composites + 3D print)
- Simple structural margin calc

**Day 5 (Aero + Trajectory)**
- Simple 3DOF model
- Ascent optimization
- Descent heating envelope

**Day 6 (Reusability)**
- Choose recovery architecture
- Size legs/parachutes/grid fins
- Ops concept & turnaround model

**Day 7 (AI Optimization)**
- Multi-objective optimization run
- At least one "radical" variant proposed by AI
- Pareto analysis + selection

**Day 8 (Reliability + Economics)**
- Cost model (development + flyaway + refurb)
- Monte Carlo risk
- Business case summary

**Day 9 (Integration)**
- Close the vehicle
- Technical review prep
- Red team exercise (AI + self)

**Day 10 (Showcase)**
- Final polish
- Presentation narrative
- Repository cleanup
- Engineering notebook export

## Daily Rituals (proposed)
- Morning: 15 min review of previous AI logs + open questions
- Mid-day: 45 min structured AI session (use template)
- End of day: 20 min reflection + update notebook + commit

## Tools & Environment Setup (Day 0-1)
- [ ] Python env with scientific stack
- [ ] Git workflow (branch per major feature?)
- [ ] Shared AI prompt template
- [ ] Figure generation pipeline

## Contingency Plans
- If running behind: Drop detailed UQ on Day 8 → qualitative + simple bounds
- If ahead: Add one "stretch" novel analysis (e.g., PINN trajectory surrogate)

## Questions for Team
- Preferred payload class?
- How much time can we dedicate to code vs writing?
- Interest level in sustainability angle?

This is a *draft*. Will be refined after Day 1 requirements are set.
