# code/ — Analysis & Modeling Scripts

All reusable Python code lives here.

## Guidelines
- Keep scripts self-contained or with clear dependencies listed in comments.
- Prefer functions over one-off scripts when possible.
- Add unit tests for critical sizing/optimization functions (stretch).
- Output artifacts go to `../data/outputs/` or `../simulations/`.

## Subfolders
- `sizing/` — Mass, geometry, rocket equation models
- `simulation/` — Trajectory, aero, thermal
- `optimization/` — MDO, evolutionary, surrogate-assisted
- `utils/` — Helpers, constants, plotting

## Environment
Recommended: Python 3.11+, numpy, scipy, matplotlib, pandas, sympy, (optional) pymoo, jax, pytorch.
