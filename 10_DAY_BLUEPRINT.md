# 10-Day Blueprint: AI Co-Design of a Reusable Rocket
**Subject to change** — This is the initial roadmap (setup on 2026-07-18).  
It will evolve based on discoveries, time constraints, and team feedback.  
**Goal**: Professional, academic-quality project showcasing rigorous scientific process, AI-augmented engineering, and novel concepts rather than conventional replication.

## Guiding Principles
- **Scientific Process First**: Hypotheses → experiments/models → validation → iteration → documented rationale.
- **AI as Copilot, Not Oracle**: Use LLM for ideation, code generation, literature synthesis, sensitivity analysis, trade-offs. Always log prompts + decisions.
- **Novelty Preference**: Explore niche ideas (e.g., bio-inspired variable-geometry recovery, physics-informed neural networks for trajectory, sustainable propellant lifecycle analysis, explainable multi-objective optimization, metamaterial thermal protection).
- **Academic Professionalism**: Clear documentation, reproducible artifacts, uncertainty quantification where possible, balanced trade-offs.
- **Scope Realism**: Conceptual vehicle (not full CAD or hardware). Focus on first-order models + selective higher-fidelity pockets. Aim for 1-2 novel contributions.
- **Cross-Cutting Threads** (apply every day):
  - AI interaction logging (`ai_logs/`)
  - Uncertainty & sensitivity (even if qualitative early)
  - Sustainability / lifecycle angle
  - Comparison to real vehicles (Falcon 9, Neutron, Terran R, etc.)
  - Engineering notebook updates

## Daily Structure Template (Recommended)
1. **Morning (1-1.5h)**: Review previous day + AI log. Formulate 2-3 hypotheses/questions.
2. **Core Work (4-5h)**: Modeling, analysis, research.
3. **AI Co-Design Session (1h)**: Structured prompting for alternatives, critique, code.
4. **Synthesis & Documentation (1-1.5h)**: Update notebook, write deliverable sections, plot figures.
5. **Reflection (30min)**: What surprised you? Where is uncertainty highest? Pivot ideas?

**Tools Stack Suggestions**:
- Python (NumPy, SciPy, Matplotlib, Pandas, SymPy)
- OpenRocket / RocketPy / simple custom 2/3DOF simulators
- For novelty: PyTorch/JAX for surrogate models, DEAP or pymoo for evolutionary MDO
- Plotly for interactive trade studies
- Markdown + LaTeX for reports

---

## Day 1: Mission Definition
**Theme**: Mission requirements  
**Primary Deliverable**: `docs/01_mission_requirements/mission_requirements.md` (with stakeholder matrix, CONOPS, success criteria)

### Objectives
- Define top-level mission (payload class, orbit, launch cadence, cost target).
- Decompose into measurable requirements (performance, reliability, reusability, environmental).
- Identify stakeholders and constraints (regulatory, environmental, economic).
- Establish baseline reference vehicle (e.g., "target a 1500 kg to LEO reusable first stage").

### Suggested Novel Angles
- Include "green mission" KPI: minimize lifecycle CO2-equivalent per kg-to-orbit.
- Explore dual-use mission (scientific + commercial) or responsive launch for smallsats.
- Define "reusability figure of merit" that includes refurbishment time + environmental impact.

### Key Activities
- Research 4-6 reference missions/vehicles.
- Create requirements hierarchy (Level 0-2).
- Initial risk register.
- **AI Prompt Ideas**: "Act as chief systems engineer. Generate a complete mission requirements document template for a small reusable launcher targeting 1-2 t to LEO. Include quantitative metrics, verification methods, and 5 alternative mission scenarios."

### Folder Targets
- `docs/01_mission_requirements/` (research_summary_2026.md, mission_requirements.md, vehicle_comparison_table.md, stakeholder_analysis.md, initial_conops.md, risk_register.md, requirements_traceability.md, mission_concepts_alternatives.md)
- `data/inputs/mission_params.json` (updated with 2026 data)
- `ai_logs/prompts/day01_mission_definition.md` + `ai_logs/decisions/day01_initial.md`
- `engineering_notebook.md` (detailed Day 1 log)
- `draft/brainstorm/day1_mission_brainstorm.md`

### Success Criteria (Flexible)
- At least 12-15 well-formed requirements with rationale.
- First version of requirements traceability matrix.
- One-page mission concept illustration (hand sketch or simple diagram).

---

## Day 2: Rocket Fundamentals & First-Order Sizing
**Theme**: First-order sizing  
**Deliverable**: `docs/02_rocket_fundamentals/vehicle_sizing_report.md` + initial mass & geometry table

### Objectives
- Apply rocket equation and staging laws.
- Perform first-order mass & dimension estimation (wet/dry mass, propellant fraction, length/diameter).
- Identify key performance parameters (Isp, structural ratio, payload fraction).
- Create baseline "strawman" vehicle.

### Novel Ideas
- Use symbolic regression or simple ML to fit historical data for rapid sizing laws.
- Introduce "adaptive structural ratio" concept (variable based on recovery mode).

### Activities
- Implement sizing script in `code/sizing/`.
- Sensitivity study on Isp and structural coefficient.
- Generate mass breakdown pie chart.
- **AI**: Ask for alternative staging architectures (single-stage reusable vs two-stage, air-launch hybrid).

### Folder Targets
- `docs/02_rocket_fundamentals/`
- `code/sizing/first_order_sizer.py`
- `data/outputs/baseline_mass_budget.csv`
- `figures/sizing_*.png`

---

## Day 3: Propulsion System
**Theme**: Engine selection  
**Deliverable**: `docs/03_propulsion/engine_selection_trade.md`

### Objectives
- Survey candidate engines (existing + conceptual).
- Perform propulsion trade study (thrust, Isp, T/W, throttleability, reusability features).
- Size propellant tanks and feed system.
- Consider propellant choice impact on recovery (cryo vs storable).

### Novel Angles
- Evaluate "green" or high-density propellants (e.g., LOX/LCH4 vs LOX/RP-1 + novel additives).
- Explore throttleable aerospike or dual-mode engine for boost + recovery.
- Physics-informed surrogate for chamber performance.

### Activities
- Build engine database (`data/benchmarks/engines.csv`).
- Propulsion performance model.
- **AI Co-pilot**: "Compare 6 candidate engines for a reusable first stage. Include cost, heritage, and manufacturing complexity scores. Generate a weighted Pugh matrix."

### Targets
- `subsystems/propulsion/`
- `analysis/trade_studies/propulsion_trade.py`

---

## Day 4: Mass Budget and Advanced Materials
**Theme**: Vehicle architecture  
**Deliverable**: Detailed mass budget + architecture description (`docs/04_mass_budget_materials/vehicle_architecture.md`)

### Objectives
- Detailed subsystem mass breakdown (structures, tanks, TPS, avionics, recovery).
- Material selection trade (Al-Li, CFRP, Ti alloys, emerging composites).
- Structural sizing (simple beam or FEA-lite).
- Tank design (common bulkhead? composite overwrapped?).

### Novel Focus
- Investigate 3D-printed or additively manufactured tank domes + lattice structures.
- Metamaterials or functionally graded materials for TPS.
- Lifecycle mass: include refurbishment mass penalty.

### Activities
- Update mass budget spreadsheet/script with margins.
- Material property database + simple structural model.
- Architecture diagram (block or exploded view).

### Targets
- `docs/04_mass_budget_materials/`
- `subsystems/structures/`
- `data/inputs/materials_db.json`

---

## Day 5: Aerodynamics and Trajectory
**Theme**: Flight profile  
**Deliverable**: `docs/05_aerodynamics_trajectory/flight_profile_report.md` + simulation outputs

### Objectives
- Conceptual aerodynamic configuration (nose, fins, body, grid fins?).
- 3DOF or 6DOF trajectory simulation.
- Ascent + descent profiles; dynamic pressure, heating.
- Landing footprint analysis.

### Novel Ideas
- Use PINN (physics-informed NN) as fast surrogate for trajectory optimization.
- Bio-inspired variable camber or morphing surfaces for recovery.
- Monte Carlo dispersion analysis on wind/guidance errors.

### Activities
- Implement or adapt simple trajectory code (`simulations/trajectory/`).
- Generate altitude-velocity plots, heat rate, g-load.
- **AI**: Generate Python code for a 3DOF simulator + ask it to suggest 3 non-standard recovery trajectories.

### Targets
- `simulations/trajectory/`
- `analysis/trade_studies/trajectory_sensitivity/`
- `figures/trajectory_*.png`

---

## Day 6: Reusability Strategy
**Theme**: Recovery concept  
**Deliverable**: `docs/06_reusability_recovery/recovery_concept.md`

### Objectives
- Choose primary recovery method (propulsive landing, parachute + retro, wings/glider, net capture, etc.).
- Size recovery hardware (legs, chutes, grid fins, TPS).
- Define ground ops & turnaround time.
- Assess reusability number (how many flights before major overhaul).

### Novel Angles (Highly Encouraged)
- Hybrid: propulsive + parafoil + drone-assisted mid-air capture.
- Ocean platform landing with wave compensation.
- "Smart" recovery using onboard ML for real-time wind compensation.
- Circular economy: design recovery hardware for remanufacture.

### Activities
- Recovery system mass model.
- Landing accuracy vs propellant budget trade.
- Timeline diagram for turnaround.

### Targets
- `subsystems/recovery/`
- `docs/06_reusability_recovery/`

---

## Day 7: AI-Assisted Optimization
**Theme**: Design iteration  
**Deliverable**: `docs/07_ai_optimization/optimization_report.md` + updated baseline

### Objectives
- Run multi-objective optimization (mass vs cost vs reliability vs environmental).
- Perform at least one major design iteration.
- Use AI to explore design space (generative suggestions, surrogate models).
- Document Pareto front + selected point.

### Novel Focus
- Evolutionary algorithm + LLM "mutation operator" (LLM proposes new architectures).
- Bayesian optimization with uncertainty.
- Explainable AI for which parameters drive performance.

### Activities
- Implement or use `code/optimization/`.
- Run 2-3 optimization cases.
- **AI Session**: "Act as a multi-agent team (structures, propulsion, aero). Propose 5 radical design variants and critique each."

### Targets
- `analysis/trade_studies/`
- `code/optimization/`
- Strong updates to `engineering_notebook.md`

---

## Day 8: Reliability and Economics
**Theme**: Cost and risk analysis  
**Deliverable**: `docs/08_reliability_economics/cost_risk_analysis.md`

### Objectives
- Build first-order cost model (development + per-flight + refurb).
- Reliability block diagram or simple fault tree.
- Monte Carlo cost & schedule risk.
- Business case: price per kg vs launch cadence.

### Novel Angles
- Incorporate carbon pricing into cost model.
- "Insurance" model for reusability risk.
- Sensitivity of economics to flight rate and refurb time.

### Activities
- Cost model script.
- Risk register + mitigation.
- Sensitivity tornado plots.

### Targets
- `analysis/uq/`
- `docs/08_reliability_economics/`

---

## Day 9: Final System Integration
**Theme**: Technical review  
**Deliverable**: Integrated technical package + review slides (`docs/09_system_integration/`)

### Objectives
- Consolidate all subsystems into coherent vehicle.
- Run integrated checks (mass closure, performance closure, margin review).
- Identify remaining open issues & assumptions.
- Prepare for technical review (peer-style critique).

### Activities
- System-level mass & performance summary.
- Interface control document (light).
- **AI**: "Perform a red-team review of the current design. List 10 strongest criticisms and potential fixes."

### Targets
- `docs/09_system_integration/technical_review_package/`
- Updated `engineering_notebook.md`

---

## Day 10: Design Competition & Showcase
**Theme**: Final presentation  
**Deliverable**: Final presentation + polished repository (`docs/10_final_presentation/`, root artifacts)

### Objectives
- Prepare 10-15 min presentation (story arc: problem → process → concept → trade-offs → novel insight → conclusions).
- Create supporting visuals, interactive demo if possible.
- Final engineering notebook export.
- Package repository for review (clean `draft/`, tag key artifacts).

### Activities
- Rehearse narrative.
- Generate summary one-pager + poster elements.
- Record key AI interaction highlights.

### Targets
- `docs/final/`
- `figures/final/`
- Root-level `FINAL_PRESENTATION.md` or slides (markdown or export)

---

## Cross-Project Milestones & Checkpoints
- **End of Day 3**: Baseline vehicle exists (rough numbers).
- **End of Day 6**: Reusable concept closed.
- **End of Day 7**: At least one major AI-driven iteration complete.
- **End of Day 8**: Quantified cost/risk.
- **End of Day 9**: All subsystems integrated, ready for review.
- **End of Day 10**: Showcase ready.

## Risk Mitigation (Plan)
- Time slippage: Prioritize core deliverables over extras; use "minimum viable" models.
- Model fidelity: Always state assumptions and limitations clearly.
- AI hallucination: Cross-check numbers with literature or simple physics.
- Scope creep: Freeze requirements after Day 2 (with change log).

## How Success Will Be Measured (Academic Lens)
- Quality and transparency of decision process (notebook + logs).
- Evidence of iteration and learning.
- Clarity of communication.
- Presence of at least one novel or non-obvious insight.
- Professional formatting and reproducibility of artifacts.

**Remember**: The journey and documented reasoning matter more than achieving a "perfect" rocket.

---

*This blueprint will be updated at the end of each day or when major pivots occur.*
