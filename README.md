# tsinghua-rocket: AI Co-Design of a Reusable Rocket

**Project Repository for the Tsinghua Summer Program (AI-Assisted Engineering Workflow)**

## Project Overview
This repository supports the development of a **conceptual reusable launch vehicle (RLV)** using AI-assisted multidisciplinary engineering workflows. 

The focus is **not** on producing the "best" rocket in absolute terms, but on:
- Rigorous requirements decomposition
- Multidisciplinary design optimization (MDO)
- Trade-off analysis
- Uncertainty quantification (UQ)
- Engineering communication and decision documentation

Students/researchers act as a design team, using an LLM (e.g., Claude, GPT, Gemini) as an **engineering copilot**, supported by structured processes.

**Core Philosophy**: Showcase knowledge, skills, and concepts learned through the *scientific process*. Prioritize professional, academic quality over perfection or industry-grade fidelity. Novel, niche, and exploratory ideas are encouraged over clichéd approaches (e.g., avoid pure Falcon 9 clones; explore bio-inspired recovery, physics-informed AI surrogates, sustainability metrics, or explainable optimization).

## Key Deliverables (Aligned with Program)
- Mission report / requirements document
- First-order vehicle sizing & mass budgets
- Propulsion selection & analysis
- Vehicle architecture with advanced materials considerations
- Aerodynamics, trajectory & flight profile simulations
- Reusability & recovery concept
- AI-assisted design iterations
- Cost, risk & reliability analysis
- Technical review package
- Final presentation + AI-generated engineering notebook (logs of decisions + rationale)

**Potential Extensions** (for deeper exploration):
- Multi-agent AI engineering workflows
- Lightweight digital twins / surrogate models
- Evolutionary / generative design competitions
- Historical benchmarking (Falcon 9, Starship, Electron, etc.)
- Impact of emerging tech: carbon-fiber composites, 3D-printed components, metamaterials

## Repository Structure
See `PROJECT_STRUCTURE.md` (generated) and the detailed `10_DAY_BLUEPRINT.md`.

High-level layout (evolving):
```
.
├── 10_DAY_BLUEPRINT.md          # Subject-to-change daily roadmap + objectives
├── summer_program.pdf           # Original program reference
├── README.md                    # This file
├── docs/                        # Formal deliverables, reports, technical memos
│   ├── 01_mission_requirements/
│   ├── 02_rocket_fundamentals/
│   ├── ...
│   └── final/
├── analysis/                    # Trade studies, sensitivity, UQ results
├── code/                        # Reusable Python scripts, models, optimizers
├── simulations/                 # Trajectory, aero, structural sim outputs
├── data/                        # Input parameters, generated datasets, benchmarks
├── figures/                     # Plots, diagrams, CAD sketches (generated + hand)
├── references/                  # Papers, datasheets, historical data
├── ai_logs/                     # Prompt logs, LLM responses, decision rationales
├── subsystems/                  # Subsystem-specific deep dives
├── draft/                       # **Temporary** — brainstorming, early drafts, notes
│                                # (Contents to be cleaned/curated at project end)
└── engineering_notebook.md      # Living AI-assisted design log (core artifact)
```

## Getting Started
1. Read `10_DAY_BLUEPRINT.md` (this is the primary working roadmap).
2. Review `summer_program.pdf`.
3. Explore `draft/` for initial thinking and starting points.
4. Begin populating `docs/01_mission_requirements/` on Day 1.

**AI Copilot Protocol** (mandatory for academic rigor):
- Every major decision or calculation must be logged in `ai_logs/`.
- Use structured prompts: state assumptions, ask for alternatives, request trade-off matrices, challenge assumptions.
- Record: prompt, response summary, accepted/rejected rationale, impact on design.

## Scientific Process Emphasis
- Formulate hypotheses for each major choice (e.g., "Using CFRP tanks will reduce dry mass by >12% vs Al-Li at similar cost").
- Validate via modeling, literature, or simple Monte Carlo.
- Document iteration loops, failures, and pivots.
- Prioritize explainability and reproducibility.

## Current Status
- **Phase**: Initial structuring (Day 0 / setup)
- Folders and placeholders created.
- Blueprint and draft content initialized.
- Ready for Day 1 work.

**Note**: This is a living repository. Structure and plan will evolve. All work should remain professional and suitable for academic showcase.

Last updated: 2026-07-18 (setup phase)
