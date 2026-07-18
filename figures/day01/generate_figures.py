#!/usr/bin/env python3
"""
Generate figures for Day 1 Mission Requirements report and presentation.
Run: python generate_figures.py
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import os

output_dir = "/home/user/tsinghua-rocket/figures/day01"
os.makedirs(output_dir, exist_ok=True)

# Set professional style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 9

# 1. Payload comparison (reusable config)
fig, ax = plt.subplots(figsize=(8, 4.5))
vehicles = ['Falcon 9\n(SpaceX)', 'New Glenn\n(Blue Origin)', 'Zhuque-3\n(Landspace)', 
            'Long March 10B\n(CASC)', 'Hyperbola-3\n(iSpace)', 'Pallas-1\n(Galactic Energy)', 'CRLV-1\n(Proposed)']
payloads = [22800, 45000, 18300, 16000, 8500, 8000, 1500]  # CRLV-1 is conceptual 1.5 t avg
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
bars = ax.barh(vehicles, payloads, color=colors)
ax.set_xlabel('Payload to LEO (kg, reusable configuration)')
ax.set_title('Comparison of Reusable Launch Vehicles (2026 Data)')
ax.bar_label(bars, fmt='%.0f', padding=3, fontsize=8)
ax.set_xlim(0, 52000)
plt.tight_layout()
plt.savefig(f"{output_dir}/payload_comparison.png", dpi=200, bbox_inches='tight')
plt.close()

# 2. Cost per kg trend (estimation based on public data)
fig, ax = plt.subplots(figsize=(7, 3.8))
years = [2015, 2018, 2021, 2024, 2026]
costs = [10000, 5500, 3200, 2700, 2200]  # Falcon 9 trend + projection; labeled as estimation
ax.plot(years, costs, marker='o', linewidth=2, markersize=8, color='#1f77b4', label='Falcon 9 trend')
ax.fill_between(years, [c*0.85 for c in costs], [c*1.15 for c in costs], alpha=0.2, color='#1f77b4')
ax.set_xlabel('Year')
ax.set_ylabel('Approximate Cost per kg to LEO (USD)')
ax.set_title('Launch Cost Reduction Trend (Reusable Vehicles)\n[Estimations based on public reports]')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_dir}/cost_trend.png", dpi=200, bbox_inches='tight')
plt.close()

# 3. Green Reusability Index concept
fig, ax = plt.subplots(figsize=(6.5, 4))
categories = ['Falcon 9\n(est.)', 'Zhuque-3\n(target)', 'Proposed CRLV-1\n(with GRI)']
gri = [1.0, 1.15, 1.35]  # Relative; CRLV-1 higher due to sustainability focus
bars = ax.bar(categories, gri, color=['#1f77b4', '#2ca02c', '#e377c2'])
ax.set_ylabel('Relative Green Reusability Index (GRI)')
ax.set_title('Illustrative GRI Comparison\n(Higher = Better sustainability-adjusted performance)')
ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.7, label='Falcon 9 baseline')
for bar, val in zip(bars, gri):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03, f'{val:.2f}', ha='center', fontsize=9)
ax.legend()
ax.set_ylim(0, 1.6)
plt.tight_layout()
plt.savefig(f"{output_dir}/gri_comparison.png", dpi=200, bbox_inches='tight')
plt.close()

# 4. Requirements hierarchy pie (simple)
fig, ax = plt.subplots(figsize=(5, 5))
labels = ['Performance\n& Orbit', 'Reusability\n& Recovery', 'Cost &\nEconomics', 'Sustainability', 'Reliability\n& Ops']
sizes = [30, 25, 15, 15, 15]
colors_pie = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']
explode = (0, 0.05, 0, 0.05, 0)
ax.pie(sizes, explode=explode, labels=labels, colors=colors_pie, autopct='%1.0f%%',
       shadow=False, startangle=90, textprops={'fontsize': 8})
ax.set_title('Proposed Figures of Merit Weighting\n(Day 1 Mission Requirements)')
plt.tight_layout()
plt.savefig(f"{output_dir}/fom_weights.png", dpi=200, bbox_inches='tight')
plt.close()

print("Figures generated successfully in", output_dir)