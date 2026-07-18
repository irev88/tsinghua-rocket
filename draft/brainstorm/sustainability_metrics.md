# Brainstorm: Sustainability & Lifecycle Angle (Niche Focus)
**Date**: 2026-07-18  
**Why include this?**: Most student projects ignore environmental cost. Adding it creates a strong differentiator and drives non-obvious trades.

## Proposed "Green Reusability Index" (GRI)
GRI = (Payload kg) / ( (CO2e_kg_total_lifecycle / flights) + refurb_energy_penalty )

Components to track:
- Propellant production emissions (methane vs RP-1 vs hydrogen)
- Manufacturing emissions (CFRP is energy intensive)
- Refurbishment energy + materials
- Recovery transport emissions
- End-of-life disposal / recyclability

## Interesting Trades This Enables
- LOX/LCH4 vs LOX/RP-1: methane might win on emissions but has boil-off issues for reusability.
- Use of bio-derived RP or synthetic methane.
- Preference for ground landing vs ocean (transport emissions).
- 3D-printed structures (potentially lower buy-to-fly ratio).

## Data Sources to Investigate
- Life cycle assessment papers on Falcon 9 / Ariane
- Propellant production LCA data
- Carbon price sensitivity ($/t CO2e)

## Potential Novel Contribution
Instead of just minimizing dry mass, optimize for "emissions per kg-to-orbit over 20 flights".

**Early hypothesis**: A slightly heavier vehicle using more sustainable propellants + shorter refurb time could beat a lighter but dirtier design on GRI.

**Action**: Add GRI as a 4th objective in Day 7 optimization.
