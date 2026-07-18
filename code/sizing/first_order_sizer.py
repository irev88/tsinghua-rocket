#!/usr/bin/env python3
"""
first_order_sizer.py
Placeholder / starter script for Day 2 first-order vehicle sizing.

This is a skeleton. Replace with real implementation.

Usage (future):
    python first_order_sizer.py --payload 1200 --dv 3800 --isp 335
"""

import argparse
import numpy as np

# Constants (will move to utils/constants.py)
G0 = 9.80665  # m/s²

def rocket_equation_dv(m0, mf, isp):
    """Simple Tsiolkovsky rocket equation."""
    return isp * G0 * np.log(m0 / mf)

def estimate_dry_mass(payload, propellant_mass, structural_coeff=0.08):
    """Very rough first-order dry mass estimate."""
    # structural_coeff = dry / (dry + propellant)
    dry = structural_coeff * (payload + propellant_mass) / (1 - structural_coeff)
    return dry

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", type=float, default=1200, help="Payload mass [kg]")
    parser.add_argument("--dv", type=float, default=3800, help="Delta-v budget [m/s]")
    parser.add_argument("--isp", type=float, default=335, help="Specific impulse [s]")
    args = parser.parse_args()

    print("=== First-Order Sizer (PLACEHOLDER) ===")
    print(f"Payload: {args.payload} kg")
    print(f"Target Δv: {args.dv} m/s")
    print(f"Isp: {args.isp} s")

    # Very crude back-calculation example
    # Assume propellant mass guess
    propellant_guess = 110000  # kg
    dry_guess = estimate_dry_mass(args.payload, propellant_guess)
    total_guess = args.payload + dry_guess + propellant_guess

    print(f"\nStrawman estimates (to be replaced):")
    print(f"  Propellant mass guess: {propellant_guess} kg")
    print(f"  Estimated dry mass:    {dry_guess:.0f} kg")
    print(f"  Total mass (no upper): {total_guess:.0f} kg")

    # TODO: Add real iteration, staging, sensitivity here

if __name__ == "__main__":
    main()
