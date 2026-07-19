#!/usr/bin/env python3
"""
Generate Day 1 figures — v2.0 (enhanced visual design)

Outputs ~12 publication-quality figures + 2 interactive HTML pages.

Design principles:
- Consistent, muted academic palette
- Every quantitative claim cross-referenced to a 2025-2026 source
  or explicitly labelled "estimate" / "illustrative"
- CJK font fallback handled gracefully
- Interactive HTML versions generated with Plotly

Run: python generate_figures.py
"""

import os
import json
import warnings
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Wedge, Rectangle, Circle
from matplotlib.patches import ConnectionPatch
import matplotlib.gridspec as gridspec
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ------------------------------------------------------------------
# Setup
# ------------------------------------------------------------------
output_dir = "/home/user/tsinghua-rocket/figures/day01"
os.makedirs(output_dir, exist_ok=True)

# CJK font registration
cjk_candidates = [
    "/home/user/tsinghua-rocket/figures/day01/fonts/NotoSansCJKsc-Regular.otf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
]
for p in cjk_candidates:
    if os.path.exists(p):
        try:
            font_manager.fontManager.addfont(p)
            from matplotlib import rcParams
            rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'Noto Sans CJK', 'DejaVu Sans']
            rcParams['axes.unicode_minus'] = False
            print(f"Registered CJK font: {p}")
            break
        except Exception as e:
            print(f"Failed to register {p}: {e}")

# Style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'regular'
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# ------------------------------------------------------------------
# Academic palette (curated, accessible)
# ------------------------------------------------------------------
NAVY    = '#1A3C6E'
SKY     = '#3B82C4'
TEAL    = '#0E7C7B'
GOLD    = '#D4A017'
CORAL   = '#D2553B'
VIOLET  = '#6B4E9C'
SAGE    = '#7BA05B'
SLATE   = '#475569'
ROSE    = '#C2185B'
ASH     = '#6B7280'
SAND    = '#F4E4BC'
PARCH   = '#FAF7F0'
MIST    = '#E5EDF5'

PALETTE = {
    'falcon9':   NAVY,
    'newglenn':  GOLD,
    'zhuque3':   TEAL,
    'lm10b':     CORAL,
    'hyperbola3':VIOLET,
    'pallas1':   SAGE,
    'crlv1':     ROSE,
    'baseline':  ASH,
    'note':      SLATE,
}

# ------------------------------------------------------------------
# Figure 1: Payload comparison (enhanced)
# ------------------------------------------------------------------
def make_payload_comparison():
    fig, ax = plt.subplots(figsize=(9, 5.2))
    rows = [
        ("Falcon 9\n(SpaceX)",          22800, PALETTE['falcon9'],
         "public; >20 flights common"),
        ("New Glenn\n(Blue Origin)",     45000, PALETTE['newglenn'],
         "maiden 2025; methalox"),
        ("Zhuque-3\n(Landspace, CN)",   18300, PALETTE['zhuque3'],
         "stainless methalox; maiden Dec 2025"),
        ("Long March 10/12A*\n(CASC)",  12000, PALETTE['lm10b'],
         "*designation uncertain"),
        ("Hyperbola-3\n(iSpace, CN)",    8500, PALETTE['hyperbola3'],
         "2026 debut (slipped)"),
        ("Pallas-1\n(Galactic Energy)",  8000, PALETTE['pallas1'],
         "reusability planned"),
        ("CRLV-1 (proposed)\nDay 1 strawman", 1500, PALETTE['crlv1'],
         "1.2 t threshold / 2.0 t goal"),
    ]
    labels  = [r[0] for r in rows]
    payloads = [r[1] for r in rows]
    colors  = [r[2] for r in rows]
    notes   = [r[3] for r in rows]
    y = np.arange(len(rows))

    # Background bands (highlight small/mid/large class)
    ax.axhspan(6.5, 6.9, color=PARCH, alpha=0.4, zorder=0)
    ax.axhspan(2.5, 5.4, color=MIST, alpha=0.4, zorder=0)

    bars = ax.barh(y, payloads, color=colors, edgecolor='white',
                   linewidth=1.2, height=0.7, zorder=2)
    # Value labels
    for bar, val in zip(bars, payloads):
        ax.text(val + 800, bar.get_y() + bar.get_height()/2,
                f"{val:,}", va='center', fontsize=9.5, fontweight='bold',
                color=bar.get_facecolor())
    # Class labels on right
    ax.text(0.99, 0.02, "← Small class (≤10 t)  |  Mid class (10-25 t)  |  Heavy (≥40 t) →",
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=8, style='italic', color=PALETTE['note'])

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlabel("Payload to LEO (kg, manufacturer targets, reusable config)", fontsize=10)
    ax.set_title("Reusable Launch Vehicle Payload Comparison (2026 data)",
                 fontsize=13, pad=12, color=NAVY)
    ax.set_xlim(0, 52000)
    ax.grid(True, axis='x', alpha=0.25, linestyle='--', zorder=1)
    ax.set_axisbelow(True)

    # Caveat
    fig.text(0.5, 0.005,
             "* The Chinese reusable-booster programme uses several closely related "
             "designations (Long March 10, 10B, 12A); the 2026 sea-based net-capture "
             "demonstration is attributed here to the LM 10/12A family pending full identification.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'],
             wrap=True)

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(f"{output_dir}/payload_comparison.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ payload_comparison.png")

# ------------------------------------------------------------------
# Figure 2: Cost trend (enhanced with annotations)
# ------------------------------------------------------------------
def make_cost_trend():
    fig, ax = plt.subplots(figsize=(9, 5))

    years   = np.array([2015, 2017, 2019, 2021, 2023, 2025])
    central = np.array([11000, 7000, 4500, 3500, 2900, 2400])
    low  = central * 0.80
    high = central * 1.25

    # Reference lines
    ax.axhline(20000, color=PALETTE['baseline'], linestyle=':', linewidth=1.2, alpha=0.7,
               label='Typical expendable small launcher (~$20k/kg)')
    ax.axhline(3500, color=PALETTE['crlv1'], linestyle='--', linewidth=1.5, alpha=0.8,
               label='CRLV-1 v1.0 L0-03 threshold ($3,500/kg)')

    # Falcon 9 trajectory
    ax.plot(years, central, marker='o', linewidth=2.5, markersize=9,
            color=PALETTE['falcon9'], label='Falcon 9 effective $/kg (central estimate)',
            zorder=4)
    ax.fill_between(years, low, high, alpha=0.20, color=PALETTE['falcon9'],
                    label='Uncertainty band (±20-25%)', zorder=2)

    # Annotate key points
    ax.annotate('Block 5\nreusability era',
                xy=(2021, 3500), xytext=(2019.2, 6500),
                fontsize=8.5, ha='left', color=PALETTE['note'],
                arrowprops=dict(arrowstyle='->', color=PALETTE['note'],
                                lw=0.8, connectionstyle='arc3,rad=0.3'))
    ax.annotate('CRLV-1 v1.0\ncost target zone',
                xy=(2025, 3500), xytext=(2023.5, 12000),
                fontsize=8.5, ha='left', color=PALETTE['crlv1'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=PALETTE['crlv1'], lw=0.8))

    ax.set_xlabel("Year", fontsize=10)
    ax.set_ylabel("Approximate cost per kg to LEO (USD)", fontsize=10)
    ax.set_title("Launch Cost Reduction — Falcon 9 Single-Vendor Trajectory",
                 fontsize=13, pad=12, color=NAVY)
    ax.legend(loc='upper right', framealpha=0.95, fontsize=8.5)
    ax.grid(True, alpha=0.25, linestyle='--')
    ax.set_ylim(0, 23000)
    ax.set_axisbelow(True)

    # Footnote
    fig.text(0.5, 0.01,
             "Note: this curve is a single-vendor (Falcon 9) data set, NOT an industry-wide trend. "
             "Industry-wide curve is reserved for the Day 8 cost model.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])

    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(f"{output_dir}/cost_trend.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ cost_trend.png")

# ------------------------------------------------------------------
# Figure 3: GRI framework (enhanced, polished)
# ------------------------------------------------------------------
def make_gri_framework():
    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_facecolor(PARCH)
    fig.patch.set_facecolor(PARCH)

    # Title
    ax.text(6, 6.6, "Green Reusability Index (GRI) — Conceptual Framework",
            ha='center', va='center', fontsize=14, fontweight='bold', color=NAVY)
    ax.text(6, 6.15, "Unit-consistent definition; no fabricated numerical ranking",
            ha='center', va='center', fontsize=9, style='italic', color=PALETTE['note'])

    # Definition box
    defn = (
        "Definition (proposed, unit-consistent):\n"
        "     GRI  =  Payload (kg)  /  [ E_flight  +  E_refurb ]\n"
        "where:   E_flight  =  CO₂e per flight (kg CO₂e)\n"
        "         E_refurb  =  amortised refurb emissions per flight (kg CO₂e/flight)\n\n"
        "Higher GRI  ⇒  more payload delivered per unit of operational emissions\n"
        "Units:  [kg payload]  /  [kg CO₂e]   =  inverse specific emissions"
    )
    box = dict(boxstyle="round,pad=0.6", facecolor='#EEF2FF',
               edgecolor=NAVY, linewidth=2)
    ax.text(6, 4.2, defn, ha='center', va='center', fontsize=10,
            bbox=box, family='monospace', linespacing=1.5)

    # 5 input contribution boxes
    inputs = [
        (1.0, 1.9, "Propellant\nproduction", "CH₄ vs RP-1", PALETTE['zhuque3']),
        (3.3, 1.9, "Manufacturing", "CFRP / Al-Li / SS", PALETTE['newglenn']),
        (5.6, 1.9, "Refurbishment\nenergy & mat'ls", "Inspection /\noverhaul", PALETTE['lm10b']),
        (7.9, 1.9, "Recovery\ntransport", "Sea vs ground", PALETTE['hyperbola3']),
        (10.2, 1.9, "End-of-life", "Recycle / disposal", PALETTE['pallas1']),
    ]
    for x, y, t1, t2, c in inputs:
        ax.add_patch(FancyBboxPatch((x-0.85, y-0.55), 1.7, 1.1,
                                    boxstyle="round,pad=0.05,rounding_size=0.1",
                                    facecolor='white', edgecolor=c, linewidth=1.8,
                                    zorder=3))
        ax.text(x, y+0.25, t1, ha='center', va='center', fontsize=9.5,
                fontweight='bold', color=c)
        ax.text(x, y-0.20, t2, ha='center', va='center', fontsize=7.5,
                style='italic', color=PALETTE['note'])
        # arrow to GRI box
        ax.annotate("", xy=(x, 2.5), xytext=(x, 2.45),
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.2, alpha=0.85))

    # Footer note
    ax.text(6, 0.35,
            "Day 7 will produce the first quantitative GRI values from the integrated mass/propellant model.",
            ha='center', va='center', fontsize=9, style='italic', color=PALETTE['note'])
    ax.text(6, 0.05, "illustration only",
            ha='center', va='center', fontsize=8, style='italic', color=PALETTE['baseline'])

    plt.tight_layout()
    plt.savefig(f"{output_dir}/gri_comparison.png", dpi=200, bbox_inches='tight',
                facecolor=PARCH)
    plt.close()
    print("✓ gri_comparison.png")

# ------------------------------------------------------------------
# Figure 4: FoM weights pie (enhanced)
# ------------------------------------------------------------------
def make_fom_weights():
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    fig.patch.set_facecolor('white')

    labels = [
        'Payload delivered\n(reusable config)',
        'Reusability\n(flights + turnaround)',
        'Recurring cost\nper kg',
        'Sustainability\n(GRI — novel FoM)',
        'Responsiveness',
    ]
    sizes = [30, 20, 25, 15, 10]
    colors = [PALETTE['falcon9'], PALETTE['zhuque3'],
              PALETTE['newglenn'], PALETTE['crlv1'],
              PALETTE['hyperbola3']]
    explode = (0, 0.04, 0, 0.10, 0)

    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.0f%%', shadow=False, startangle=90,
        textprops={'fontsize': 10}, pctdistance=0.72,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    )
    for t in autotexts:
        t.set_color('white')
        t.set_fontweight('bold')
        t.set_fontsize(11)

    # Central annotation
    centre_circle = plt.Circle((0,0), 0.45, fc='white', ec=NAVY, lw=1.5)
    ax.add_artist(centre_circle)
    ax.text(0, 0.07, "FoM", ha='center', va='center',
            fontsize=12, fontweight='bold', color=NAVY)
    ax.text(0, -0.07, "CRLV-1", ha='center', va='center',
            fontsize=10, color=PALETTE['note'])
    ax.text(0, -0.20, "100%", ha='center', va='center',
            fontsize=11, fontweight='bold', color=PALETTE['crlv1'])

    ax.set_title("CRLV-1 Level-0 Figures of Merit — agreed weighting\n"
                 "(30 / 20 / 25 / 15 / 10, sum = 100%)",
                 fontsize=12, color=NAVY, pad=20)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/fom_weights.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ fom_weights.png")

# ------------------------------------------------------------------
# Figure 5: Radar chart — CRLV-1 vs Falcon 9 vs Zhuque-3 (NEW)
# ------------------------------------------------------------------
def make_radar_comparison():
    """
    Radar / spider chart comparing CRLV-1 against operational peers.
    All scores are illustrative 0-10 ratings on the five L0 FoMs.
    For CRLV-1, scores are *targets* (Day 7 will quantify).
    """
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('white')

    categories = ['Payload\n(reusable)', 'Reusability', 'Cost\nper kg',
                  'Sustainability\n(GRI)', 'Responsiveness']
    N = len(categories)

    # Illustrative 0-10 scores (Day-1 strawman)
    # Falcon 9: high on payload + reuse, moderate on cost, low on sustainability narrative
    # Zhuque-3: mid payload, ambitious, limited reuse heritage yet
    # CRLV-1: low payload by design, high reuse target, strong sustainability focus
    f9      = [9.0, 9.5, 8.0, 5.0, 6.0]
    zhuque  = [6.5, 4.5, 6.0, 7.0, 5.0]
    crlv1   = [3.0, 8.0, 5.5, 9.0, 8.5]   # Day 1 target profile

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    for vals, label, color, fill_alpha in [
        (f9,     'Falcon 9 (reference)', PALETTE['falcon9'], 0.10),
        (zhuque, 'Zhuque-3 (target)',    PALETTE['zhuque3'], 0.10),
        (crlv1,  'CRLV-1 (Day 1 target)',PALETTE['crlv1'],   0.20),
    ]:
        vals_loop = vals + vals[:1]
        ax.plot(angles, vals_loop, linewidth=2.2, label=label, color=color, zorder=3)
        ax.fill(angles, vals_loop, color=color, alpha=fill_alpha, zorder=2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10.5, color=NAVY)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=8, color=PALETTE['note'])
    ax.grid(True, alpha=0.3, linestyle='--')

    ax.set_title("Multi-FoM Comparison — Day 1 illustrative scores (0-10)\n"
                 "Higher = better. CRLV-1 scores are *targets* to be quantified on Day 7.",
                 fontsize=11, color=NAVY, pad=24)
    ax.legend(loc='upper right', bbox_to_anchor=(1.32, 1.10),
              fontsize=9, framealpha=0.95)
    fig.text(0.5, 0.02,
             "Illustrative 0-10 ratings, not measured values. Day 7 will replace with quantitative GRI / cost / cadence metrics.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])

    plt.tight_layout()
    plt.savefig(f"{output_dir}/fom_radar.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ fom_radar.png  (NEW — radar chart)")

# ------------------------------------------------------------------
# Figure 6: Δv budget Sankey-like allocation (NEW)
# ------------------------------------------------------------------
def make_dv_budget():
    """
    Horizontal stacked bar showing the Δv budget allocation
    for a typical LEO 500 km mission. Small losses are grouped.
    """
    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor('white')

    # Group small losses together for legibility
    stages = [
        ("Gravity loss",          1500, PALETTE['baseline']),
        ("Drag + steering\n+ ullage", 600, PALETTE['pallas1']),
        ("Stage 1 Δv\n(booster)", 3200, NAVY),
        ("Stage 2 Δv\n(upper)",  4200, PALETTE['crlv1']),
        ("Circular-\nisation",    250, PALETTE['zhuque3']),
    ]
    total = sum(s[1] for s in stages)
    cum = 0
    for label, val, color in stages:
        # Bar
        ax.barh([0], [val], left=[cum], color=color, edgecolor='white',
                linewidth=1.5, height=0.55)
        # Inline label (with both label and value if wide enough)
        if val >= 800:
            ax.text(cum + val/2, 0, f"{label}\n{val} m/s",
                    ha='center', va='center', fontsize=10, color='white',
                    fontweight='bold')
        elif val >= 300:
            ax.text(cum + val/2, 0, f"{label}\n{val} m/s",
                    ha='center', va='center', fontsize=8.5, color='white',
                    fontweight='bold')
        else:
            # Very small — callout below
            ax.text(cum + val/2, 0, f"{val}", ha='center', va='center',
                    fontsize=9, color='white', fontweight='bold')
            ax.text(cum + val/2, 0.45, label.replace('\n', ' '),
                    ha='center', va='bottom', fontsize=7.5, color=color,
                    fontweight='bold')
        cum += val

    ax.set_xlim(0, total * 1.02)
    ax.set_ylim(-0.55, 0.85)
    ax.set_yticks([])
    ax.set_xlabel(f"Cumulative Δv (m/s)   |   Total ≈ {total} m/s",
                  fontsize=10.5)
    ax.set_title("Representative Δv Budget for 500 km LEO (illustrative allocation)",
                 fontsize=12, color=NAVY, pad=10)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    # Legend / key
    fig.text(0.5, 0.07,
             "Δv losses (gravity, drag, steering, ullage) are grouped and shown in non-stage colours; "
             "stage Δv shown in dark blue (booster) and rose (upper).",
             ha='center', fontsize=8.5, color=PALETTE['note'])
    fig.text(0.5, 0.02,
             "Allocation is illustrative. Day 2 will derive CRLV-1-specific Δv from trajectory simulation.",
             ha='center', fontsize=8.5, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.08, 1, 1])
    plt.savefig(f"{output_dir}/dv_budget_sankey.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ dv_budget_sankey.png  (NEW — Δv budget, grouped small losses)")

# ------------------------------------------------------------------
# Figure 7: Requirements hierarchy treemap (NEW)
# ------------------------------------------------------------------
def make_requirements_treemap():
    """
    A 2-row treemap showing L0 → L1 → counts, with proper text
    sizing to avoid overlap.
    """
    fig, ax = plt.subplots(figsize=(12, 6.5))
    fig.patch.set_facecolor('white')

    cats = [
        # name, count, color, list of (L1-id, label)
        ("Performance",   3, PALETTE['falcon9'],   [
            ("L1-P01", "1,200–2,000 kg LEO"),
            ("L1-P02", "±20/10 km, ±0.05°"),
            ("L1-P03", "Ø 3.4 m fairing"),
        ]),
        ("Reusability",   3, PALETTE['zhuque3'],   [
            ("L1-R01", "≥0.90 per flight"),
            ("L1-R02", "10–20 reuses"),
            ("L1-R03", "propulsive OR net-capture"),
        ]),
        ("Cost",          2, PALETTE['newglenn'],  [
            ("L1-C01", "≤ $4.2 M / flight"),
            ("L1-C02", "≤ 15% refurb"),
        ]),
        ("Sustainability",2, PALETTE['crlv1'],     [
            ("L1-E01", "LOX/LCH₄ (+ bio)"),
            ("L1-E02", "GRI FoM"),
        ]),
        ("Safety",        1, PALETTE['lm10b'],     [
            ("L1-S01", "≥ 0.95 over 10 flt"),
        ]),
        ("Operations",    3, PALETTE['hyperbola3'],[
            ("L1-O01", "Hainan coastal"),
            ("L1-O02", "rideshare + dedicated"),
            ("L1-O03", "±30 m landing"),
        ]),
    ]
    total = sum(c[1] for c in cats)  # 14

    # Two rows
    row1 = [cats[0], cats[1], cats[5]]  # Performance, Reusability, Operations
    row2 = [cats[2], cats[3], cats[4]]  # Cost, Sustainability, Safety

    def draw_box(x, y, w, h, cat):
        name, n, color, subs = cat
        ax.add_patch(FancyBboxPatch((x, y), w - 0.15, h,
                                    boxstyle="round,pad=0.05,rounding_size=0.12",
                                    facecolor=color, alpha=0.92,
                                    edgecolor='white', linewidth=2.5))
        # Title
        ax.text(x + (w-0.15)/2, y + h - 0.30, name,
                ha='center', va='top', fontsize=12, fontweight='bold', color='white')
        ax.text(x + (w-0.15)/2, y + h - 0.62, f"{n} L1 req{'s' if n>1 else ''}",
                ha='center', va='top', fontsize=9, color='white', style='italic')
        # Divider
        ax.plot([x + 0.2, x + w - 0.35], [y + h - 0.85, y + h - 0.85],
                color='white', linewidth=0.8, alpha=0.6)
        # Sub-reqs — distribute evenly, ensuring all fit
        sub_h = (h - 1.1) / max(n, 1)
        for j, (lid, lab) in enumerate(subs):
            sub_y = y + h - 1.15 - (j + 0.5) * sub_h
            ax.text(x + 0.20, sub_y + 0.10, lid, ha='left', va='center',
                    fontsize=8.5, color='white', fontweight='bold')
            ax.text(x + 0.20, sub_y - 0.13, lab, ha='left', va='center',
                    fontsize=7.5, color='white', alpha=0.9)

    # Row 1: 3 boxes (large)
    row1_w = sum(c[1] for c in row1) / total * 13
    cum = 0
    for cat in row1:
        w = max(cat[1] / sum(c[1] for c in row1) * row1_w, 2.2)  # minimum 2.2 width
        draw_box(cum, 3.5, w, 3.0, cat)
        cum += w

    # Row 2: 3 boxes (small)
    row2_w = sum(c[1] for c in row2) / total * 13
    cum = 0
    for cat in row2:
        w = max(cat[1] / sum(c[1] for c in row2) * row2_w, 2.5)  # minimum 2.5 width
        draw_box(cum, 0.3, w, 3.0, cat)
        cum += w

    ax.set_xlim(-0.2, max(row1_w, row2_w) + 0.2)
    ax.set_ylim(0, 7)
    ax.set_aspect('auto')
    ax.axis('off')
    ax.set_title("CRLV-1 Requirements Hierarchy — 14 L1 requirements across 6 categories",
                 fontsize=14, color=NAVY, pad=14)
    fig.text(0.5, 0.01,
             "All 14 L1 requirements have explicit verification methods (analysis, simulation, test, inspection).",
             ha='center', fontsize=9, style='italic', color=PALETTE['note'])
    plt.tight_layout()
    plt.savefig(f"{output_dir}/requirements_treemap.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ requirements_treemap.png  (NEW — hierarchy, 2-row)")

# ------------------------------------------------------------------
# Figure 8: Recovery architecture side-by-side schematic (NEW)
# ------------------------------------------------------------------
def make_recovery_architecture():
    """
    Side-by-side schematic of propulsive landing vs net-capture.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.5))
    fig.patch.set_facecolor('white')
    fig.suptitle("Recovery Architecture Trade — Propulsive vs Sea-Based Net-Capture",
                 fontsize=14, color=NAVY, y=0.98, fontweight='bold')

    for ax, (title, color, elements) in zip(axes, [
        ("Option A: Propulsive Landing", PALETTE['falcon9'], 'propulsive'),
        ("Option B: Sea-based Net-Capture", PALETTE['lm10b'], 'net'),
    ]):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 12)
        ax.set_facecolor('#F8FAFC' if elements == 'propulsive' else '#F0F4F8')
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor(color)
            spine.set_linewidth(2)

        # Sea surface
        ax.axhline(2.0, color='#3B82F6', linewidth=2, linestyle='-', alpha=0.7)
        ax.fill_between([0, 10], 0, 2.0, color='#BFDBFE', alpha=0.5)
        ax.text(0.3, 1.0, "Sea level", fontsize=8, color=NAVY, style='italic')

        # Clouds / atmosphere hint
        ax.text(5, 11.0, "Atmosphere", fontsize=8, color=PALETTE['note'],
                ha='center', style='italic', alpha=0.7)

        if elements == 'propulsive':
            # Drone ship
            ax.add_patch(Rectangle((3, 1.2), 4, 0.6, facecolor=PALETTE['note'],
                                   edgecolor='black', linewidth=1))
            ax.text(5, 1.5, "Drone ship / launch mount", fontsize=8, ha='center', color='white', fontweight='bold')

            # Booster descending with engine firing
            booster = FancyBboxPatch((4.4, 5.5), 1.2, 4.0,
                                     boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor=color, edgecolor='white', linewidth=1.5)
            ax.add_patch(booster)
            ax.text(5, 7.5, "Booster", fontsize=8, ha='center', color='white', fontweight='bold')

            # Engine flame
            ax.add_patch(mpatches.Polygon([[4.7, 5.5], [5.3, 5.5], [5.5, 4.0], [5.0, 3.6], [4.5, 4.0]],
                                          facecolor=GOLD, edgecolor='none', alpha=0.85))
            ax.text(5, 4.4, "Landing\nburn", fontsize=7, ha='center', color=NAVY, style='italic')

            # Grid fins
            ax.add_patch(Rectangle((4.0, 9.0), 0.3, 0.6, facecolor='white',
                                   edgecolor=color, linewidth=1))
            ax.add_patch(Rectangle((5.7, 9.0), 0.3, 0.6, facecolor='white',
                                   edgecolor=color, linewidth=1))
            ax.text(3.4, 9.3, "Grid\nfins", fontsize=7, ha='center', color=PALETTE['note'])

            # Landing legs
            ax.plot([4.5, 4.2], [5.5, 5.0], color=color, linewidth=2)
            ax.plot([5.5, 5.8], [5.5, 5.0], color=color, linewidth=2)
            ax.text(6.4, 5.2, "Landing\nlegs", fontsize=7, color=PALETTE['note'], ha='left')

            # Mass penalty callout
            ax.text(8, 8, "• 4 deployable legs\n• ~mass penalty\n• 4 grid fins\n• burn to touchdown",
                    fontsize=8, va='top', color=PALETTE['note'],
                    bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color))
        else:
            # Recovery vessel with capture frame
            ax.add_patch(Rectangle((2.5, 1.2), 5, 0.6, facecolor=PALETTE['note'],
                                   edgecolor='black', linewidth=1))
            ax.text(5, 1.5, "Recovery vessel", fontsize=8, ha='center', color='white', fontweight='bold')

            # Capture frame / net above the vessel
            ax.add_patch(Rectangle((3.5, 1.9), 3, 0.6, facecolor=GOLD,
                                   edgecolor='black', linewidth=1, alpha=0.8))
            ax.text(5, 2.2, "Capture frame", fontsize=7, ha='center', color='black', fontweight='bold')
            # Net lines
            for x_off in np.linspace(3.5, 6.5, 8):
                ax.plot([x_off, x_off], [1.9, 1.2], color=PALETTE['note'], linewidth=0.5, alpha=0.5)

            # Booster suspended above net
            booster = FancyBboxPatch((4.4, 4.5), 1.2, 4.0,
                                     boxstyle="round,pad=0.05,rounding_size=0.15",
                                     facecolor=color, edgecolor='white', linewidth=1.5)
            ax.add_patch(booster)
            ax.text(5, 6.5, "Booster\n(hover)", fontsize=8, ha='center', color='white', fontweight='bold')

            # Grid fins (no legs)
            ax.add_patch(Rectangle((4.0, 8.0), 0.3, 0.6, facecolor='white',
                                   edgecolor=color, linewidth=1))
            ax.add_patch(Rectangle((5.7, 8.0), 0.3, 0.6, facecolor='white',
                                   edgecolor=color, linewidth=1))
            ax.text(3.4, 8.3, "Grid\nfins", fontsize=7, ha='center', color=PALETTE['note'])

            # Suspension lines / hooks
            ax.plot([4.5, 4.0], [4.5, 2.5], color=PALETTE['baseline'], linewidth=1.2, linestyle='--')
            ax.plot([5.5, 6.0], [4.5, 2.5], color=PALETTE['baseline'], linewidth=1.2, linestyle='--')
            ax.text(2.4, 3.4, "Capture\ntethers", fontsize=7, color=PALETTE['note'], ha='left')

            # No legs annotation
            ax.text(8, 8, "• No legs\n• No landing\n  propellant\n• Grid fins only\n• Tight rendezvous",
                    fontsize=8, va='top', color=PALETTE['note'],
                    bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color))

        ax.set_title(title, fontsize=12, color=color, pad=8, fontweight='bold')

    # Sources / caveats
    fig.text(0.5, 0.01,
             "Option B demonstrated 2026 by a Chinese methalox booster in the LM 10/12A family "
             "(vehicle designation uncertain in public sources). Schematic illustrations only.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])

    plt.tight_layout(rect=[0, 0.03, 1, 0.96])
    plt.savefig(f"{output_dir}/recovery_architecture.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ recovery_architecture.png  (NEW — schematic)")

# ------------------------------------------------------------------
# Figure 9: CRLV-1 concept sketch (NEW)
# ------------------------------------------------------------------
def make_concept_sketch():
    """
    Annotated vehicle concept sketch of CRLV-1 — clean layout.
    """
    fig, ax = plt.subplots(figsize=(12.5, 10))
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 16)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#F0F4F8')

    # Sky
    ax.add_patch(Rectangle((0, 8), 14, 8, facecolor='#DBEAFE', alpha=0.4, zorder=0))
    # Sea
    ax.add_patch(Rectangle((0, 0), 14, 2.0, facecolor='#BFDBFE', alpha=0.6, zorder=1))
    ax.text(13.7, 1.0, "Sea", ha='right', va='center', fontsize=8, color=NAVY, style='italic')

    # Specs box (top-left, small)
    specs = [
        ("Payload (reusable):",  "1,200–2,000 kg  (L0-01)"),
        ("Total length:",        "≈ 40 m  (Day 2)"),
        ("Booster diameter:",    "≈ 3.4 m  (L1-P03)"),
        ("Booster dry mass:",    "≈ 18–22 t  (Day 2)"),
        ("Reuses:",              "10–20  (L1-R02)"),
        ("Propellant:",          "LOX/LCH₄  (L1-E01)"),
    ]
    spec_box = FancyBboxPatch((0.4, 10.5), 3.6, 4.0,
                             boxstyle="round,pad=0.1,rounding_size=0.1",
                             facecolor='white', edgecolor=NAVY, linewidth=1.2, zorder=4)
    ax.add_patch(spec_box)
    # Title centered
    ax.text(2.2, 14.15, "Day 1 Strawman Specifications",
            ha='center', fontsize=9.5, color=NAVY, fontweight='bold', va='center')
    ax.plot([0.6, 3.8], [13.85, 13.85], color=NAVY, linewidth=0.6, alpha=0.5)
    for j, (k, v) in enumerate(specs):
        yp = 13.5 - j * 0.45
        ax.text(0.55, yp, k, fontsize=7.5, color=NAVY, fontweight='bold', va='center')
        ax.text(2.05, yp, v, fontsize=7.5, color=PALETTE['note'], va='center')

    # Cross-section (top-right)
    cs_box = FancyBboxPatch((10.2, 10.5), 3.6, 4.0,
                            boxstyle="round,pad=0.1,rounding_size=0.1",
                            facecolor='white', edgecolor=NAVY, linewidth=1.2, zorder=4)
    ax.add_patch(cs_box)
    ax.text(12.0, 14.15, "Common bulkhead (schematic)",
            ha='center', fontsize=9, color=NAVY, fontweight='bold', va='center')
    # Schematic
    ax.add_patch(Rectangle((10.6, 12.5), 2.8, 0.55, facecolor=PALETTE['zhuque3'],
                           edgecolor=NAVY, linewidth=0.8, zorder=5))
    ax.text(12.0, 12.77, "LOX", ha='center', va='center', fontsize=8, color='white', fontweight='bold')
    ax.add_patch(Rectangle((10.6, 12.0), 2.8, 0.25, facecolor=PALETTE['pallas1'],
                           edgecolor=NAVY, linewidth=0.8, zorder=5))
    ax.text(12.0, 12.12, "Bulkhead", ha='center', va='center', fontsize=6, color='white')
    ax.add_patch(Rectangle((10.6, 11.5), 2.8, 0.55, facecolor=PALETTE['hyperbola3'],
                           edgecolor=NAVY, linewidth=0.8, zorder=5))
    ax.text(12.0, 11.77, "CH₄", ha='center', va='center', fontsize=8, color='white', fontweight='bold')
    ax.text(12.0, 11.2, "(Day 4 will refine)",
            ha='center', va='center', fontsize=6.5, color=PALETTE['note'], style='italic')
    ax.text(12.0, 10.9, "Methalox propellant",
            ha='center', va='center', fontsize=6.5, color=PALETTE['note'])

    # Vehicle (centered, x: 5-9)
    cx, cw = 6.0, 2.2  # center x, width
    # Booster
    booster = FancyBboxPatch((cx - cw/2, 3.0), cw, 8.0,
                             boxstyle="round,pad=0.05,rounding_size=0.3",
                             facecolor=PARCH, edgecolor=NAVY, linewidth=2, zorder=3)
    ax.add_patch(booster)
    # Section dividers
    ax.plot([cx - cw/2, cx + cw/2], [8.0, 8.0], color=NAVY, linewidth=0.8, linestyle=':', zorder=4)
    ax.plot([cx - cw/2, cx + cw/2], [5.5, 5.5], color=NAVY, linewidth=0.8, linestyle=':', zorder=4)

    # Engines
    for ex in np.linspace(cx - 0.9, cx + 0.9, 7):
        ax.add_patch(Circle((ex, 2.6), 0.16, facecolor=PALETTE['lm10b'],
                            edgecolor=NAVY, linewidth=0.8, zorder=4))
    ax.text(cx, 1.9, "7× methalox engines",
            ha='center', fontsize=7.5, color=PALETTE['note'])
    ax.text(cx, 1.55, "(Day 3 will detail)",
            ha='center', fontsize=6.8, color=PALETTE['note'], style='italic')

    # Grid fins
    ax.add_patch(Rectangle((cx - cw/2 - 0.4, 10.2), 0.4, 0.7, facecolor=PALETTE['newglenn'],
                            edgecolor=NAVY, linewidth=0.8, zorder=4))
    ax.add_patch(Rectangle((cx + cw/2, 10.2), 0.4, 0.7, facecolor=PALETTE['newglenn'],
                            edgecolor=NAVY, linewidth=0.8, zorder=4))
    ax.text(cx - cw/2 - 0.6, 10.55, "Grid\nfin", ha='right', va='center', fontsize=7, color=PALETTE['note'])

    # Upper stage
    upper = FancyBboxPatch((cx - 0.8, 11.4), 1.6, 2.3,
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           facecolor='white', edgecolor=NAVY, linewidth=1.8, zorder=3)
    ax.add_patch(upper)
    # Upper engine bell
    ax.add_patch(Circle((cx, 11.55), 0.13, facecolor=PALETTE['lm10b'],
                        edgecolor=NAVY, linewidth=0.8, zorder=4))

    # Fairing (top)
    fairing = mpatches.Polygon([[cx - 0.8, 13.7], [cx + 0.8, 13.7],
                                [cx + 0.3, 14.4], [cx - 0.3, 14.4]],
                               closed=True, facecolor=PALETTE['falcon9'],
                               edgecolor=NAVY, linewidth=1, alpha=0.85, zorder=3)
    ax.add_patch(fairing)

    # Callouts — left side (to vehicle features)
    def callout_left(y_text, y_target, label):
        ax.annotate(label,
                    xy=(cx - cw/2, y_target), xytext=(0.7, y_text),
                    fontsize=8, color=NAVY, fontweight='bold',
                    ha='left', va='center',
                    arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.0,
                                    connectionstyle='arc3,rad=0.0'))
    # Callouts — right side
    def callout_right(y_text, y_target, label):
        ax.annotate(label,
                    xy=(cx + cw/2, y_target), xytext=(9.5, y_text),
                    fontsize=8, color=NAVY, fontweight='bold',
                    ha='left', va='center',
                    arrowprops=dict(arrowstyle='->', color=NAVY, lw=1.0,
                                    connectionstyle='arc3,rad=0.0'))

    callout_left(8.5, 8.0, "LOX tank\n(common bulkhead)")
    callout_left(6.0, 5.5, "CH₄ tank")
    callout_left(4.0, 4.0, "Avionics + recovery\nhardware")
    callout_right(8.5, 8.0, "LOX tank (upper)")
    callout_right(6.0, 5.5, "CH₄ tank (upper)")
    callout_right(4.0, 3.0, "Booster engines")
    # Top callouts
    ax.text(cx, 14.95, "Fairing (Ø 3.4 m × 6.5 m, L1-P03)",
            ha='center', fontsize=8, color=NAVY, fontweight='bold')
    ax.text(cx, 11.95, "Upper stage (LOX/LCH₄)", ha='center', fontsize=7.5,
            color=PALETTE['note'], style='italic')

    fig.suptitle("CRLV-1 Vehicle Concept — Day 1 Strawman",
                 fontsize=14, color=NAVY, y=0.99, fontweight='bold')
    fig.text(0.5, 0.01,
             "Not to scale. Day 2 will refine dimensions from first-order sizing; Day 3 will specify engine choice.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.02, 1, 0.97])
    plt.savefig(f"{output_dir}/concept_sketch.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ concept_sketch.png  (NEW — vehicle concept, clean layout)")

# ------------------------------------------------------------------
# Figure 10: Trajectory profile (NEW)
# ------------------------------------------------------------------
def make_trajectory_profile():
    """
    Ascent + descent altitude-velocity profile, schematic.
    """
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    fig.patch.set_facecolor('white')
    fig.suptitle("CRLV-1 Representative Flight Profile (illustrative, Day 1)",
                 fontsize=14, color=NAVY, y=0.98, fontweight='bold')

    # ASCENT
    ax = axes[0]
    t = np.linspace(0, 9, 200)
    alt = 500 * (1 - np.cos(np.pi/9 * t))   # sinusoidal pitch-over to orbit
    vel = 1500 * np.sin(np.pi/18 * t) + 200
    ax.plot(t, alt, color=NAVY, linewidth=2.5, label='Altitude (km)')
    ax.set_xlabel("Time after liftoff (min)", fontsize=10)
    ax.set_ylabel("Altitude (km)", color=NAVY, fontsize=10)
    ax.tick_params(axis='y', labelcolor=NAVY)
    ax.set_ylim(0, 600)
    ax.set_xlim(0, 9.5)

    ax2 = ax.twinx()
    ax2.plot(t, vel, color=PALETTE['crlv1'], linewidth=2.5, linestyle='--', label='Velocity (m/s)')
    ax2.set_ylabel("Velocity (m/s)", color=PALETTE['crlv1'], fontsize=10)
    ax2.tick_params(axis='y', labelcolor=PALETTE['crlv1'])
    ax2.set_ylim(0, 7800)

    # Events
    events = [
        (0.3, "Liftoff",        0,   100),
        (1.8, "Max Q",          50,  500),
        (2.8, "Booster MECO\n& separation", 100, 0),
        (3.0, "Booster boost-back",  150,  -200),
        (6.5, "Upper MECO",     500, 300),
        (8.5, "Payload deploy", 500, 100),
    ]
    for tt, lab, dy_a, dy_v in events:
        ax.axvline(tt, color=PALETTE['note'], linewidth=0.5, linestyle=':', alpha=0.6)
        if 'MECO' in lab or 'separation' in lab or 'deploy' in lab or 'boost-back' in lab:
            ax.text(tt, 50 + dy_a, lab, fontsize=7.5, rotation=0,
                    ha='center', color=PALETTE['note'],
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                              edgecolor=PALETTE['note'], linewidth=0.5, alpha=0.9))
        else:
            ax.text(tt, 50, lab, fontsize=7.5, ha='center', color=PALETTE['note'],
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                              edgecolor=PALETTE['note'], linewidth=0.5, alpha=0.9))

    ax.set_title("Ascent", fontsize=11, color=NAVY, fontweight='bold')
    ax.grid(True, alpha=0.25, linestyle='--')

    # DESCENT
    ax = axes[1]
    t = np.linspace(0, 14, 200)
    # Re-entry to landing
    alt = 500 * np.exp(-t/3) + 20
    vel = 7800 * np.exp(-t/4) + 30
    ax.plot(t, alt, color=NAVY, linewidth=2.5, label='Altitude (km)')
    ax.set_xlabel("Time from MECO (min)", fontsize=10)
    ax.set_ylabel("Altitude (km)", color=NAVY, fontsize=10)
    ax.tick_params(axis='y', labelcolor=NAVY)
    ax.set_ylim(0, 600)
    ax.set_xlim(0, 14)

    ax2 = ax.twinx()
    ax2.plot(t, vel, color=PALETTE['crlv1'], linewidth=2.5, linestyle='--', label='Velocity (m/s)')
    ax2.set_ylabel("Velocity (m/s)", color=PALETTE['crlv1'], fontsize=10)
    ax2.tick_params(axis='y', labelcolor=PALETTE['crlv1'])
    ax2.set_ylim(0, 7800)

    events_d = [
        (0.3, "Stage sep +\nflip",     0,    0),
        (1.5, "Entry burn start",      100,  0),
        (4.0, "Max heating",           80,   0),
        (6.0, "Reentry burn",          60,   0),
        (10.0, "Landing burn",         30,   0),
        (13.5, "Touchdown\n(propulsive)\nor capture (net)", 5,  0),
    ]
    for tt, lab, dy_a, _ in events_d:
        ax.axvline(tt, color=PALETTE['note'], linewidth=0.5, linestyle=':', alpha=0.6)
        ax.text(tt, 30 + dy_a, lab, fontsize=7.5, ha='center', color=PALETTE['note'],
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=PALETTE['note'], linewidth=0.5, alpha=0.9))

    ax.set_title("Booster descent & recovery", fontsize=11, color=NAVY, fontweight='bold')
    ax.grid(True, alpha=0.25, linestyle='--')

    fig.text(0.5, 0.01,
             "Schematic only. Day 5 will produce a quantitative 3DOF trajectory from the integrated mass model.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f"{output_dir}/trajectory_profile.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ trajectory_profile.png  (NEW — flight profile)")

# ------------------------------------------------------------------
# Figure 11: GRI levers tornado (improved)
# ------------------------------------------------------------------
def make_gri_levers():
    levers = [
        ("Propellant choice (CH₄ vs RP-1)", 2.5, 0.85, PALETTE['zhuque3']),
        ("Reusability (10 → 20 flights)",   2.2, 0.90, PALETTE['zhuque3']),
        ("Refurbishment energy intensity",   1.8, 0.55, PALETTE['zhuque3']),
        ("Recovery transport (sea vs ground)",1.4, 0.70, PALETTE['newglenn']),
        ("Material choice (CFRP vs Al-Li vs SS)",1.0, 0.50, PALETTE['newglenn']),
        ("Manufacturing emissions share",    0.7, 0.45, PALETTE['newglenn']),
    ]
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor('white')
    y = np.arange(len(levers))
    impacts = [l[1] for l in levers]
    confs = [l[2] for l in levers]
    colors = [l[3] for l in levers]

    bars = ax.barh(y, impacts, color=colors, edgecolor='white', linewidth=1, height=0.7)
    # Confidence band shading
    for i, (imp, conf) in enumerate(zip(impacts, confs)):
        ax.barh(i, imp * conf, color='white', edgecolor=colors[i],
                linewidth=2, linestyle='--', height=0.7, alpha=0.7)

    ax.set_yticks(y)
    ax.set_yticklabels([l[0] for l in levers], fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("Qualitative impact on GRI (illustrative, 0-3 scale)\n"
                  "[Dashed outline = confidence-weighted bound]",
                  fontsize=10)
    ax.set_title("Design Levers That Most Affect GRI — Qualitative Ranking",
                 fontsize=12, color=NAVY, pad=10)
    ax.set_xlim(0, 3.2)
    for i, c in enumerate(confs):
        ax.text(impacts[i] + 0.05, i, f"conf. {c:.2f}", va='center',
                fontsize=8, color=PALETTE['note'])
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    fig.text(0.5, 0.01,
             "Magnitudes are qualitative 0-3 scores. Day 7 will quantify from the integrated mass/propellant model.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(f"{output_dir}/gri_levers.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ gri_levers.png  (enhanced)")

# ------------------------------------------------------------------
# Figure 12: Cost uncertainty distribution (NEW)
# ------------------------------------------------------------------
def make_cost_uncertainty():
    """
    For the L0-03 cost target: show a probabilistic cost
    distribution (per kg) for the threshold case, to honestly
    communicate the uncertainty band.
    """
    fig, ax = plt.subplots(figsize=(9, 4.5))
    fig.patch.set_facecolor('white')

    # Lognormal-style distribution centred on $3,500 with wide uncertainty
    x = np.linspace(1000, 8000, 500)
    mu, sigma = np.log(3500), 0.30
    y = (1 / (x * sigma * np.sqrt(2*np.pi))) * np.exp(-((np.log(x) - mu) ** 2) / (2 * sigma**2))
    y = y / y.max()  # normalize

    ax.fill_between(x, y, color=SKY, alpha=0.35, label='Lognormal PDF (μ=$3,500, σ=30%)')
    ax.plot(x, y, color=NAVY, linewidth=2)

    # Annotate key zones
    ax.axvline(2500, color=PALETTE['crlv1'], linewidth=2, linestyle='--',
               label='L0-03 GOAL  ($2,500/kg)')
    ax.axvline(3500, color=PALETTE['zhuque3'], linewidth=2, linestyle='-',
               label='L0-03 THRESHOLD  ($3,500/kg)')
    ax.axvline(2400, color=PALETTE['falcon9'], linewidth=1.5, linestyle=':',
               label='Falcon 9 effective ($2,400/kg)')

    # P(threshold) area shading
    ax.fill_between(x[x <= 3500], y[x <= 3500], 0, color=PALETTE['zhuque3'], alpha=0.18)
    ax.text(2950, 0.50, "P(achieve ≤ $3,500/kg)\n≈ 0.5", ha='center', fontsize=9,
            color=PALETTE['note'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=PALETTE['zhuque3']))

    ax.set_xlabel("Recurring cost per kg to LEO (USD)", fontsize=10)
    ax.set_ylabel("Probability density (normalised)", fontsize=10)
    ax.set_title("L0-03 Cost Target — Honest Uncertainty Distribution",
                 fontsize=12, color=NAVY, pad=10)
    ax.legend(loc='upper right', fontsize=8.5, framealpha=0.95)
    ax.set_xlim(1000, 8000)
    ax.set_ylim(0, 1.15)
    ax.grid(True, alpha=0.25, linestyle='--')
    ax.set_axisbelow(True)
    fig.text(0.5, 0.01,
             "Distribution is illustrative. Day 8 cost model will derive this from first-principles + Monte Carlo.",
             ha='center', fontsize=8, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(f"{output_dir}/cost_uncertainty_band.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ cost_uncertainty_band.png  (NEW — uncertainty)")

# ------------------------------------------------------------------
# Figure 13: 10-day Gantt schedule (NEW)
# ------------------------------------------------------------------
def make_gantt_10day():
    """
    10-day programme schedule with milestones, decisions,
    and Day 1 in highlighted state.
    """
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor('white')
    fig.suptitle("10-Day Programme Schedule — Day 1 highlighted",
                 fontsize=14, color=NAVY, y=0.97, fontweight='bold')

    # Each day is 1.0 wide in units; we plot labels to the LEFT of the bar
    days = [
        # (label, color, milestone, role)
        ("Day 1 — Mission definition", PALETTE['crlv1'], "✓ v1.0 refined",  "completed"),
        ("Day 2 — Sizing & Δv",        SKY,            "→", "planned"),
        ("Day 3 — Propulsion trade",   SKY,            "→", "planned"),
        ("Day 4 — Mass & materials",   SKY,            "→", "planned"),
        ("Day 5 — Aero + trajectory",  SKY,            "→", "planned"),
        ("Day 6 — Recovery arch.",     PALETTE['lm10b'],"close L1-R03", "decision_gate"),
        ("Day 7 — AI optimisation",    PALETTE['zhuque3'],"first GRI values", "decision_gate"),
        ("Day 8 — Cost + reliability", PALETTE['newglenn'],"validate L0-03", "planned"),
        ("Day 9 — Integration",        PALETTE['hyperbola3'],"red-team", "planned"),
        ("Day 10 — Final presentation",PALETTE['pallas1'],"showcase", "milestone"),
    ]
    # Reverse so Day 1 is at the bottom
    days = days[::-1]

    for j, (name, c, milestone, role) in enumerate(days):
        # Match "Day 1" but NOT "Day 10"
        is_today = (name.startswith("Day 1 —"))
        is_gate  = role == "decision_gate"
        # Bar (small, on the right)
        ax.barh(j, 0.55, left=0.1, color=c,
                edgecolor=NAVY if is_today else ('black' if is_gate else 'white'),
                linewidth=2.5 if is_today else (1.5 if is_gate else 0.8),
                height=0.55, zorder=3)
        # Day label on the bar
        ax.text(0.37, j, name.split(' — ')[0], ha='center', va='center',
                fontsize=9, color='white', fontweight='bold')
        # Theme label on the bar
        ax.text(0.65, j, name.split(' — ')[1], ha='left', va='center',
                fontsize=9.5, color=NAVY, fontweight='bold')
        # Milestone
        if milestone and milestone != "→":
            ax.text(11.0, j, milestone, ha='right', va='center',
                    fontsize=8.5, color=c, fontweight='bold',
                    style='italic' if is_today else 'normal')
        elif milestone == "→":
            ax.text(11.0, j, "→ pending", ha='right', va='center',
                    fontsize=8.5, color=PALETTE['note'], style='italic')
        if is_today:
            # TODAY marker — to the right of the bar, not above (avoid overlap)
            ax.text(2.0, j, "▸ TODAY (v1.0 refined)",
                    ha='left', va='center', fontsize=8.5,
                    color=PALETTE['crlv1'], fontweight='bold')

    # Decision gates (vertical lines and annotations)
    ax.axvline(0.85, color=PALETTE['lm10b'], linestyle='--', linewidth=1.0, alpha=0.5, zorder=1)

    ax.set_yticks([])
    ax.set_ylim(-0.6, len(days) - 0.4)
    ax.set_xlim(-0.2, 12)
    ax.set_xticks([])
    ax.set_xlabel("Programme days progress left → right (Day 1 at the bottom)",
                  fontsize=10, color=NAVY, fontweight='bold')
    ax.grid(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Legend / decision-gate annotation at bottom
    ax.text(0.1, -1.2,
            "Decision gates",
            ha='left', va='top', fontsize=9, color=NAVY, fontweight='bold',
            transform=ax.transData)
    ax.add_patch(Rectangle((2.3, -1.45), 0.3, 0.25,
                           facecolor=PALETTE['lm10b'], edgecolor='black', linewidth=1.2,
                           transform=ax.transData, clip_on=False))
    ax.text(2.7, -1.32, "Day 6: net-capture vs propulsive decision",
            ha='left', va='center', fontsize=8.5, color=PALETTE['note'],
            transform=ax.transData)
    ax.add_patch(Rectangle((2.3, -1.78), 0.3, 0.25,
                           facecolor=PALETTE['zhuque3'], edgecolor='black', linewidth=1.2,
                           transform=ax.transData, clip_on=False))
    ax.text(2.7, -1.65, "Day 7: GRI becomes quantitative (closes L1-E02)",
            ha='left', va='center', fontsize=8.5, color=PALETTE['note'],
            transform=ax.transData)

    fig.text(0.5, 0.01,
             "Day-1 (today) outputs: 6 L0 + 15 L1 requirements, the unit-consistent GRI framework, "
             "and the propulsive-vs-net-capture trade scope (to close on Day 6).",
             ha='center', fontsize=8.5, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.05, 1, 0.94])
    plt.savefig(f"{output_dir}/gantt_10day.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ gantt_10day.png  (NEW — schedule, clean labels)")

# ------------------------------------------------------------------
# Figure 14: L1 requirements coverage bar (NEW)
# ------------------------------------------------------------------
def make_requirements_bar():
    """
    L1 coverage by category, with color-coded novel items.
    """
    fig, ax = plt.subplots(figsize=(9, 4.5))
    fig.patch.set_facecolor('white')
    cats = ['Performance\n(L1-P0x)', 'Reusability\n(L1-R0x)',
            'Cost\n(L1-C0x)', 'Sustainability\n(L1-E0x)',
            'Safety\n(L1-S0x)', 'Operations\n(L1-O0x)']
    counts = [3, 3, 2, 2, 1, 3]
    colors = [PALETTE['falcon9'], PALETTE['zhuque3'], PALETTE['newglenn'],
              PALETTE['crlv1'], PALETTE['lm10b'], PALETTE['hyperbola3']]
    bars = ax.bar(cats, counts, color=colors, edgecolor='white', linewidth=1.2, width=0.65)
    for bar, c in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width()/2, c + 0.08, f"{c}",
                ha='center', fontsize=12, fontweight='bold')
    ax.set_ylabel("Number of L1 requirements", fontsize=10)
    ax.set_title(f"L1 Requirements Coverage by Category (Day 1 — total = {sum(counts)})",
                 fontsize=12, color=NAVY, pad=10)
    ax.set_ylim(0, max(counts) + 1.0)
    ax.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)
    fig.text(0.5, 0.01,
             "All L1 requirements carry explicit verification methods (analysis, simulation, test, inspection).",
             ha='center', fontsize=8.5, style='italic', color=PALETTE['note'])
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    plt.savefig(f"{output_dir}/requirements_tree.png", dpi=200, bbox_inches='tight',
                facecolor='white')
    plt.close()
    print("✓ requirements_tree.png  (replaces previous)")

# ==================================================================
# INTERACTIVE HTML versions (Plotly)
# ==================================================================
def make_interactive_radar():
    categories = ['Payload<br>(reusable)', 'Reusability', 'Cost<br>per kg',
                  'Sustainability<br>(GRI)', 'Responsiveness']
    f9      = [9.0, 9.5, 8.0, 5.0, 6.0]
    zhuque  = [6.5, 4.5, 6.0, 7.0, 5.0]
    crlv1   = [3.0, 8.0, 5.5, 9.0, 8.5]

    fig = go.Figure()
    for vals, name, color, fill in [
        (f9,     'Falcon 9 (reference)', '#1A3C6E', 'rgba(26,60,110,0.15)'),
        (zhuque, 'Zhuque-3 (target)',    '#0E7C7B', 'rgba(14,124,123,0.15)'),
        (crlv1,  'CRLV-1 (Day 1 target)','#C2185B', 'rgba(194,24,91,0.20)'),
    ]:
        fig.add_trace(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name=name,
            line=dict(color=color, width=2.5),
            fillcolor=fill,
            hovertemplate='<b>%{theta}</b><br>Score: %{r}/10<extra>'+name+'</extra>'
        ))
    fig.update_layout(
        title=dict(text="<b>CRLV-1 Multi-FoM Radar</b><br>"
                        "<sub>Illustrative 0-10 scores; Day 7 will quantify</sub>",
                   x=0.5, xanchor='center', font=dict(size=16, color='#1A3C6E')),
        polar=dict(radialaxis=dict(visible=True, range=[0, 10],
                                   tickvals=[2,4,6,8,10],
                                   tickfont=dict(size=10, color='#475569')),
                   angularaxis=dict(tickfont=dict(size=12, color='#1A3C6E'))),
        showlegend=True,
        legend=dict(x=1.05, y=0.95, bgcolor='rgba(255,255,255,0.9)'),
        width=750, height=620,
        paper_bgcolor='white',
        margin=dict(l=80, r=180, t=110, b=80),
    )
    fig.write_html(f"{output_dir}/interactive_radar.html", include_plotlyjs='cdn')
    print("✓ interactive_radar.html  (NEW — interactive Plotly)")

def make_interactive_payload_3d():
    """
    3D-ish bar comparison: vehicles on x, payload on y, $/kg on z (or colour).
    """
    vehicles = ['Falcon 9', 'New Glenn', 'Zhuque-3', 'LM 10/12A*', 'Hyperbola-3',
                'Pallas-1', 'CRLV-1']
    payloads = [22800, 45000, 18300, 12000, 8500, 8000, 1500]
    cost_per_kg = [2400, 3500, 3500, 4000, 18000, 16000, 3500]  # illustrative
    reuse_heritage = [20, 1, 0, 0, 0, 0, 0]  # number of reflights demonstrated

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=vehicles, y=payloads,
        name='Payload to LEO (kg)',
        marker=dict(
            color=cost_per_kg,
            colorscale='Viridis_r',
            showscale=True,
            colorbar=dict(title='Illustrative<br>$/kg')
        ),
        text=[f"{p:,} kg<br>~${c:,}/kg" for p, c in zip(payloads, cost_per_kg)],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Payload: %{y:,} kg<br>'
                      'Illustrative $/kg: %{marker.color:,}<extra></extra>',
    ))
    fig.update_layout(
        title=dict(text="<b>Payload vs Indicative Cost — Interactive</b><br>"
                        "<sub>Hover for details; colour = $/kg (illustrative)</sub>",
                   x=0.5, xanchor='center',
                   font=dict(size=16, color='#1A3C6E')),
        xaxis_title="Vehicle",
        yaxis_title="Payload to LEO (kg, reusable)",
        width=900, height=600,
        paper_bgcolor='white',
        plot_bgcolor='#F8FAFC',
        margin=dict(l=70, r=80, t=110, b=70),
        showlegend=False,
    )
    fig.write_html(f"{output_dir}/interactive_payload.html", include_plotlyjs='cdn')
    print("✓ interactive_payload.html  (NEW — interactive Plotly)")

# ==================================================================
# Run
# ==================================================================
if __name__ == "__main__":
    print("Generating static PNG figures ...")
    make_payload_comparison()
    make_cost_trend()
    make_gri_framework()
    make_fom_weights()
    make_requirements_bar()
    make_gri_levers()
    make_radar_comparison()
    make_dv_budget()
    make_requirements_treemap()
    make_recovery_architecture()
    make_concept_sketch()
    make_trajectory_profile()
    make_cost_uncertainty()
    make_gantt_10day()
    print("\nGenerating interactive HTML figures ...")
    make_interactive_radar()
    make_interactive_payload_3d()
    print("\nDone.")
