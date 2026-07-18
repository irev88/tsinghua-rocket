# Repository Structure (Living Document)

This file describes the intended organization of `tsinghua-rocket`. It will be updated as the project evolves.

## Root
- `README.md` — High-level project description and navigation
- `10_DAY_BLUEPRINT.md` — Detailed day-by-day plan (subject to change)
- `summer_program.pdf` — Original course outline
- `engineering_notebook.md` — Primary living document: decisions, rationale, AI interactions summary
- `PROJECT_STRUCTURE.md` — This file

## docs/ — Formal Deliverables & Reports
Each day/subsystem has a dedicated folder. Content should be polished, academic style.

```
docs/
├── 01_mission_requirements/
│   ├── mission_requirements.md          # Main deliverable
│   ├── requirements_traceability.md
│   └── stakeholder_analysis.md
├── 02_rocket_fundamentals/
├── ...
├── 09_system_integration/
├── 10_final_presentation/
└── final/                               # Polished final package
    ├── executive_summary.md
    ├── full_report.md
    └── presentation_slides.md
```

## analysis/ — Quantitative Studies
- `trade_studies/` — Propulsion, recovery, materials, trajectory trades
- `sensitivity/` — Tornado plots, parameter sweeps
- `uq/` — Uncertainty quantification, Monte Carlo results

## code/ — Reusable & Versioned Code
All scripts should be well-commented and runnable with minimal setup.

```
code/
├── sizing/
├── simulation/
├── optimization/
│   └── multi_objective.py
└── utils/
    └── helpers.py
```

## simulations/ — Simulation Outputs & Models
- `trajectory/` — 3DOF/6DOF results, input decks
- `aero/` — Aerodynamic coefficients
- `structural/` — Mass & load models

## data/ — Datasets & Parameters
- `inputs/` — JSON/YAML parameter files, mission specs
- `outputs/` — Generated tables, CSVs
- `benchmarks/` — Historical vehicle data, engine catalogs

## figures/ — All Visuals
- Organized by day or topic (e.g., `figures/day05/`, `figures/trades/`)
- Include both source (`.py` scripts that generate) and final images

## ai_logs/ — AI Copilot Records (Critical Artifact)
```
ai_logs/
├── prompts/
│   └── dayXX_topic_prompt.md
├── decisions/
│   └── dayXX_decision_log.md
└── full_transcripts/   (optional, large)
```
Every significant interaction should be logged with:
- Exact prompt
- Model & date
- Key outputs
- Team decision & rationale

## subsystems/ — Deep Dives
Detailed technical notes per major subsystem (can feed into `docs/`).

## references/ — Literature & Data Sources
- PDFs or links (use `references.bib` for academic style)
- Datasheets
- Vehicle comparison tables

## draft/ — **Temporary Brainstorming Only**
**All content here will be reviewed and either moved to appropriate folders or deleted by project end (Day 10).**

Do **not** treat draft content as final. Use for:
- Raw brainstorming
- Early work plans
- Half-baked ideas
- Meeting notes
- Failed experiments

Subfolders:
- `brainstorm/`
- `work_plans/`
- `early_notes/`

## Other Conventions
- Use consistent units: SI (kg, m, s, N, Pa) unless explicitly noted.
- Every CSV/JSON should have a companion `README.md` or header explaining columns.
- Figures should be generated from code when possible (reproducibility).
- Markdown preferred for reports; use LaTeX only if needed for final PDF.

## Naming
- Use `snake_case` for files and folders.
- Date prefix major logs when helpful: `2026-07-18_mission_hypotheses.md`

Last updated: 2026-07-18
