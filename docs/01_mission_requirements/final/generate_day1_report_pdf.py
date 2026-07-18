#!/usr/bin/env python3
"""
Generate the final polished Day 1 Mission Definition Report PDF.
Uses reportlab for professional academic formatting.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Output path
output_path = "/home/user/tsinghua-rocket/docs/01_mission_requirements/final/Day1_Mission_Definition_Report.pdf"
figures_dir = "/home/user/tsinghua-rocket/figures/day01"

# Create document
doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

# Styles
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=6,
    textColor=HexColor('#1a1a2e')
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=10,
    alignment=TA_CENTER,
    spaceAfter=12,
    textColor=HexColor('#4a4a4a')
)

heading1_style = ParagraphStyle(
    'Heading1Custom',
    parent=styles['Heading1'],
    fontSize=12,
    leading=14,
    spaceBefore=12,
    spaceAfter=6,
    textColor=HexColor('#1a1a2e')
)

heading2_style = ParagraphStyle(
    'Heading2Custom',
    parent=styles['Heading2'],
    fontSize=11,
    leading=13,
    spaceBefore=8,
    spaceAfter=4,
    textColor=HexColor('#2d3436')
)

body_style = ParagraphStyle(
    'BodyCustom',
    parent=styles['Normal'],
    fontSize=9.5,
    leading=12,
    alignment=TA_JUSTIFY,
    spaceAfter=6
)

caption_style = ParagraphStyle(
    'Caption',
    parent=styles['Normal'],
    fontSize=8,
    alignment=TA_CENTER,
    spaceAfter=8,
    textColor=HexColor('#555555')
)

abstract_style = ParagraphStyle(
    'Abstract',
    parent=styles['Normal'],
    fontSize=9,
    leading=11,
    alignment=TA_JUSTIFY,
    leftIndent=1*cm,
    rightIndent=1*cm,
    spaceAfter=10,
    backColor=HexColor('#f8f9fa')
)

ref_style = ParagraphStyle(
    'Reference',
    parent=styles['Normal'],
    fontSize=8,
    leading=10,
    leftIndent=0.5*cm,
    spaceAfter=2
)

# Build content
story = []

# Title
story.append(Paragraph(
    "Mission Definition and Requirements for a Conceptual Reusable Launch Vehicle (CRLV-1):<br/>A Sustainable and Responsive Design Framework",
    title_style
))
story.append(Paragraph("Research Team — Tsinghua Summer Program on AI Co-Design of Reusable Rockets<br/>18 July 2026", subtitle_style))
story.append(Spacer(1, 4*mm))

# Abstract
story.append(Paragraph("<b>Abstract</b>", heading2_style))
abstract_text = """This paper presents the mission definition and requirements for CRLV-1, a conceptual partially reusable launch vehicle targeting 1,200–2,000 kg payload to low Earth orbit (LEO) or sun-synchronous orbit (SSO). Drawing on comprehensive analysis of 2025–2026 global and Chinese reusable launch vehicle (RLV) developments, including the successful net-capture recovery of China's Long March 10B in July 2026, the requirements hierarchy integrates performance, reusability, cost, and novel sustainability metrics. A Green Reusability Index (GRI) is introduced as a primary figure of merit. The framework emphasizes realistic, verifiable requirements grounded in contemporary vehicle data from SpaceX Falcon 9, Landspace Zhuque-3, iSpace Hyperbola-3, and CASC programs. The proposed vehicle architecture prioritizes methalox propulsion and evaluates both conventional propulsive landing and net-capture recovery strategies. This work demonstrates a rigorous scientific process for early-phase conceptual design suitable for academic and educational demonstration purposes."""
story.append(Paragraph(abstract_text, abstract_style))

# 1. Introduction
story.append(Paragraph("1. Introduction", heading1_style))
intro = """The rapid advancement of reusable launch vehicle technology, led by SpaceX's Falcon 9 and accelerated by Chinese state and commercial programs in 2025–2026, has fundamentally altered the economics of access to space. As of mid-2026, multiple Chinese vehicles have achieved or approached first-stage recovery, with the Long March 10B demonstrating the first Chinese orbital-class booster recovery via a novel sea-based net-capture system on its maiden flight (Ars Technica, 2026; SpaceNews, 2025)."""
story.append(Paragraph(intro, body_style))

intro2 = """This paper documents the mission definition process for CRLV-1, a conceptual small-to-medium class RLV intended as a demonstrator for university and emerging commercial applications. The design targets the payload class between dedicated small launchers (e.g., Rocket Lab Electron) and medium-lift vehicles (e.g., Falcon 9 class). Particular emphasis is placed on integrating sustainability considerations through the proposed Green Reusability Index (GRI) and on evaluating recovery architectures informed by the latest Chinese innovations."""
story.append(Paragraph(intro2, body_style))

# 2. Research Methodology
story.append(Paragraph("2. Research Methodology and Data Sources", heading1_style))
method = """A systematic literature and news review was conducted focusing on 2025–2026 developments. Primary sources included SpaceNews, Ars Technica, Global Times, China-in-Space, company announcements, and market analyses. All quantitative claims were cross-verified across at least two independent sources."""
story.append(Paragraph(method, body_style))

story.append(Paragraph("<b>Key reference vehicles analyzed (reusable configuration unless noted):</b>", body_style))

refs = [
    "• SpaceX Falcon 9 Block 5: 22,800 kg to LEO (Orbital Radar, 2026).",
    "• Blue Origin New Glenn: 45,000 kg to LEO.",
    "• Landspace Zhuque-3: approximately 18,300 kg recovered (downrange) (SpaceNews, 2025).",
    "• iSpace Hyperbola-3: 8,500 kg recovered.",
    "• Galactic Energy Pallas-1: 8,000 kg baseline.",
    "• CASC Long March 10B: 16,000 kg to LEO in reusable mode with net-capture recovery demonstrated July 2026 (Ars Technica, 2026; Wikipedia, 2026)."
]
for r in refs:
    story.append(Paragraph(r, body_style))

sust = """Sustainability data were drawn from recent Life Cycle Assessment (LCA) studies indicating traditional RP-1/LOX systems produce approximately 19 tonnes CO<sub>2</sub>e per tonne of payload delivered (LCA studies 2024–2025)."""
story.append(Paragraph(sust, body_style))

# 3. Mission Statement
story.append(Paragraph("3. Mission Statement and Top-Level Objectives", heading1_style))
story.append(Paragraph("<b>Mission Statement:</b> Develop a conceptual partially reusable launch vehicle (CRLV-1) capable of delivering 1,200–2,000 kg to LEO or SSO with a minimum of 10 first-stage reuses, competitive recurring cost, and explicit lifecycle sustainability performance.", body_style))

story.append(Paragraph("<b>Level-0 Objectives:</b>", body_style))
l0_items = [
    "1. Deliver 1,200 kg (threshold) to 2,000 kg (goal) payload to 500 km LEO or 700 km SSO.",
    "2. Achieve first-stage reusability of at least 10 flights (threshold) / 20 flights (goal) with refurbishment cost below 15% of new stage.",
    "3. Target recurring launch cost below 2,800 USD/kg to LEO (threshold).",
    "4. Achieve lifecycle CO<sub>2</sub>-equivalent emissions below 15 t CO<sub>2</sub>e per tonne payload (estimation, based on industry LCA baselines).",
    "5. Support launch responsiveness within 30 days of payload integration."
]
for item in l0_items:
    story.append(Paragraph(item, body_style))

# 4. Key Requirements
story.append(Paragraph("4. Key Requirements Hierarchy", heading1_style))
req_intro = """A structured requirements breakdown (L1/L2) was developed with verification methods. Selected examples are presented below. Novel elements include the introduction of the Green Reusability Index (GRI) = Payload (kg) / (CO<sub>2</sub>e per flight + refurbishment penalty) and a formal requirement to evaluate sea-based net-capture recovery (inspired by Long March 10B July 2026 demonstration)."""
story.append(Paragraph(req_intro, body_style))

# Requirements table
req_data = [
    ['ID', 'Requirement', 'Verification'],
    ['L1-P01', 'Payload to 500 km LEO ≥ 1,200 kg (reusable)', 'Analysis + trajectory simulation'],
    ['L1-R01', 'First-stage recovery success ≥ 90% after 5 flights', 'Flight test + Monte Carlo'],
    ['L1-R03', 'Evaluate net-capture recovery architecture', 'Trade study + dynamics simulation'],
    ['L1-E01', 'Prefer LOX/LCH4 propellant', 'Lifecycle assessment'],
    ['L1-E02', 'Green Reusability Index (GRI) as primary FoM', 'Quantitative model'],
    ['L1-C01', 'Recurring cost ≤ 3.5 M USD per flight (threshold)', 'Cost model'],
]

table = Table(req_data, colWidths=[1.8*cm, 7*cm, 5*cm])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2c3e50')),
    ('TEXTCOLOR', (0, 0), (-1, 0), white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8f9fa')),
    ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#bdc3c7')),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))
story.append(table)
story.append(Paragraph("Table 1: Selected Level-1 Requirements (excerpt)", caption_style))

# 5. Benchmarking
story.append(Paragraph("5. Reference Vehicle Benchmarking", heading1_style))
bench = """Figure 1 presents payload capacity comparison for reusable configurations. CRLV-1 is positioned at the lower end of the medium-lift spectrum to enable focused study of reusability and sustainability trades within a conceptual academic framework. Figure 2 illustrates the historical cost reduction trend driven by reusability (estimations derived from public reports)."""
story.append(Paragraph(bench, body_style))

# Insert payload figure
if os.path.exists(f"{figures_dir}/payload_comparison.png"):
    img = Image(f"{figures_dir}/payload_comparison.png", width=15*cm, height=8.5*cm)
    story.append(img)
    story.append(Paragraph("Figure 1: Payload capacity comparison of selected reusable launch vehicles (2026 data). CRLV-1 target shown for reference.", caption_style))

story.append(Spacer(1, 3*mm))

# Insert cost trend
if os.path.exists(f"{figures_dir}/cost_trend.png"):
    img2 = Image(f"{figures_dir}/cost_trend.png", width=13*cm, height=6.5*cm)
    story.append(img2)
    story.append(Paragraph("Figure 2: Approximate cost per kilogram to LEO trend for reusable vehicles (estimations based on published data).", caption_style))

# 6. Sustainability
story.append(Paragraph("6. Sustainability Integration", heading1_style))
sust_text = """The proposed GRI elevates environmental performance to a core design driver. Figure 3 shows an illustrative comparison. The inclusion of sustainability is supported by recent LCA studies demonstrating that reusability alone can reduce production emissions by over 95% compared to expendable designs (LCA studies 2024–2025)."""
story.append(Paragraph(sust_text, body_style))

if os.path.exists(f"{figures_dir}/gri_comparison.png"):
    img3 = Image(f"{figures_dir}/gri_comparison.png", width=11*cm, height=6.5*cm)
    story.append(img3)
    story.append(Paragraph("Figure 3: Illustrative Green Reusability Index (GRI) comparison. Higher values indicate better sustainability-adjusted performance.", caption_style))

# 7. Recovery
story.append(Paragraph("7. Recovery Architecture Considerations", heading1_style))
recov = """Two primary recovery strategies are retained for further study: (1) Conventional propulsive landing with grid fins and landing legs (baseline, demonstrated by Falcon 9 and multiple Chinese vehicles). (2) Sea-based net-capture system (novel alternative, successfully demonstrated by Long March 10B on 10 July 2026). Net capture offers potential structural mass savings by eliminating landing legs but requires dedicated recovery vessel infrastructure."""
story.append(Paragraph(recov, body_style))

# 8. FoM
story.append(Paragraph("8. Figures of Merit and Stakeholder Alignment", heading1_style))
fom = """The weighting of figures of merit (Figure 4) balances traditional performance metrics with emerging sustainability priorities. Primary stakeholders include commercial constellation operators (e.g., analogs to Guowang and Thousand Sails), government agencies, and scientific users. The requirements directly address needs for dedicated access, cost reduction through reuse, and environmental responsibility."""
story.append(Paragraph(fom, body_style))

if os.path.exists(f"{figures_dir}/fom_weights.png"):
    img4 = Image(f"{figures_dir}/fom_weights.png", width=9*cm, height=8*cm)
    story.append(img4)
    story.append(Paragraph("Figure 4: Proposed figures of merit weighting for CRLV-1 mission requirements.", caption_style))

# 9. Conclusions
story.append(Paragraph("9. Conclusions and Forward Path", heading1_style))
concl = """The mission definition for CRLV-1 establishes a coherent, evidence-based framework for a conceptual reusable launch vehicle. By grounding requirements in the latest 2025–2026 vehicle data, particularly Chinese achievements in net-capture recovery and methalox propulsion, and by introducing the GRI as a novel evaluation metric, the project positions itself to explore both conventional and innovative design pathways. Subsequent phases will refine mass budgets, propulsion trades, and recovery system sizing while maintaining traceability to the requirements presented herein. All quantitative targets for CRLV-1 remain subject to iterative refinement through modeling and analysis."""
story.append(Paragraph(concl, body_style))

# References
story.append(Paragraph("References", heading1_style))
refs_list = [
    "[1] Ars Technica (2026). “China recovered its first reusable rocket and showed a new way to do it.” 10 July 2026.",
    "[2] SpaceNews (2025). “China to debut new Long March and commercial rockets in 2025.” January 2025.",
    "[3] Orbital Radar (2026). Launch vehicle specifications database.",
    "[4] Wikipedia contributors (2026). “Long March 10B.” Accessed July 2026.",
    "[5] LCA studies (2024–2025): MaiaSpace environmental assessment; arXiv:2504.15291; Strathclyde University RLV LCA papers."
]
for ref in refs_list:
    story.append(Paragraph(ref, ref_style))

# Build PDF
doc.build(story)
print(f"PDF report generated: {output_path}")