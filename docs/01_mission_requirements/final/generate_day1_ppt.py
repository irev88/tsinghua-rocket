#!/usr/bin/env python3
"""
Generate Day 1 PPT Presentation (Simplified Chinese)
12 slides, visually focused, professional unified design.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Cm
from pptx.dml.color import RGBColor as RgbColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import nsmap
from pptx.oxml import parse_xml
import os

# Output
output_path = "/home/user/tsinghua-rocket/docs/01_mission_requirements/final/Day1_Mission_Definition_Presentation.pptx"
figures_dir = "/home/user/tsinghua-rocket/figures/day01"

# Create presentation (16:9)
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color scheme (professional blue/teal theme)
PRIMARY = RgbColor(0x1A, 0x3C, 0x6E)      # Deep navy
ACCENT = RgbColor(0x00, 0x7A, 0xCC)       # Bright blue
SECONDARY = RgbColor(0x00, 0xB8, 0xA9)    # Teal
DARK = RgbColor(0x2D, 0x34, 0x36)
LIGHT_BG = RgbColor(0xF8, 0xF9, 0xFA)
WHITE = RgbColor(0xFF, 0xFF, 0xFF)

def add_title_slide(prs, title, subtitle):
    slide_layout = prs.slide_layouts[6]  # Blank
    slide = prs.slides.add_slide(slide_layout)
    
    # Background shape
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY
    bg.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.7), Inches(1.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(4.2), Inches(11.7), Inches(1.2))
    tf = sub_box.text_frame
    p = tf.paragraphs[0]
    p.text = subtitle
    p.font.size = Pt(20)
    p.font.color.rgb = RgbColor(0xCC, 0xE5, 0xFF)
    p.alignment = PP_ALIGN.CENTER
    
    # Footer
    footer = slide.shapes.add_textbox(Inches(0.8), Inches(6.5), Inches(11.7), Inches(0.5))
    tf = footer.text_frame
    p = tf.paragraphs[0]
    p.text = "清华大学暑期项目 · AI辅助可重复使用运载火箭联合设计"
    p.font.size = Pt(12)
    p.font.color.rgb = RgbColor(0xAA, 0xCC, 0xEE)
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_content_slide(prs, title, content_items=None, image_path=None, two_column=False):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Header bar
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY
    header.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12.3), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Content area
    if image_path and os.path.exists(image_path):
        if two_column:
            # Left text, right image
            text_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.4), Inches(5.5), Inches(5.5))
            tf = text_box.text_frame
            tf.word_wrap = True
            for i, item in enumerate(content_items or []):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.text = "• " + item
                p.font.size = Pt(14)
                p.font.color.rgb = DARK
                p.space_after = Pt(8)
            
            img = slide.shapes.add_picture(image_path, Inches(6.5), Inches(1.5), width=Inches(6.2))
        else:
            # Full width image with small caption
            img = slide.shapes.add_picture(image_path, Inches(0.8), Inches(1.4), width=Inches(11.7))
    else:
        # Text only
        text_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.4), Inches(12.3), Inches(5.5))
        tf = text_box.text_frame
        tf.word_wrap = True
        for i, item in enumerate(content_items or []):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = "• " + item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK
            p.space_after = Pt(10)
    
    return slide

def add_stat_slide(prs, title, stats):
    """Stats cards slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY
    header.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12.3), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Stats cards
    colors = [ACCENT, SECONDARY, PRIMARY, RgbColor(0xE6, 0x7E, 0x22)]
    for i, (label, value) in enumerate(stats):
        col = i % 2
        row = i // 2
        x = Inches(0.8 + col * 6.2)
        y = Inches(1.6 + row * 2.7)
        
        # Card background
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.8), Inches(2.3))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_BG
        card.line.color.rgb = colors[i % len(colors)]
        card.line.width = Pt(3)
        
        # Value
        val_box = slide.shapes.add_textbox(x + Inches(0.3), y + Inches(0.3), Inches(5.2), Inches(1.1))
        tf = val_box.text_frame
        p = tf.paragraphs[0]
        p.text = value
        p.font.size = Pt(32)
        p.font.bold = True
        p.font.color.rgb = colors[i % len(colors)]
        p.alignment = PP_ALIGN.CENTER
        
        # Label
        lbl_box = slide.shapes.add_textbox(x + Inches(0.3), y + Inches(1.4), Inches(5.2), Inches(0.7))
        tf = lbl_box.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(14)
        p.font.color.rgb = DARK
        p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_figure_slide(prs, title, image_path, caption=""):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1))
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY
    header.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.25), Inches(12.3), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    if os.path.exists(image_path):
        img = slide.shapes.add_picture(image_path, Inches(1.2), Inches(1.35), width=Inches(10.9))
    
    if caption:
        cap_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.8), Inches(12.3), Inches(0.5))
        tf = cap_box.text_frame
        p = tf.paragraphs[0]
        p.text = caption
        p.font.size = Pt(11)
        p.font.color.rgb = DARK
        p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_end_slide(prs):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY
    bg.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(11.7), Inches(1.2))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "感谢聆听"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    sub = slide.shapes.add_textbox(Inches(0.8), Inches(4), Inches(11.7), Inches(1.5))
    tf = sub.text_frame
    p = tf.paragraphs[0]
    p.text = "CRLV-1 任务定义与需求\n清华大学暑期AI辅助火箭设计项目 · 2026年7月"
    p.font.size = Pt(18)
    p.font.color.rgb = RgbColor(0xCC, 0xE5, 0xFF)
    p.alignment = PP_ALIGN.CENTER
    
    return slide

# ============ BUILD SLIDES ============

# Slide 1: Title
add_title_slide(
    prs,
    "CRLV-1 任务定义与需求\n概念可重复使用运载火箭任务需求报告",
    "清华大学暑期项目 · AI辅助可重复使用运载火箭联合设计\n2026年7月18日"
)

# Slide 2: 项目背景
add_content_slide(prs, "项目背景与研究目标", [
    "2025-2026年中国可重复使用火箭快速发展",
    "SpaceX Falcon 9 成功验证商业可行性",
    "中国长征10B于2026年7月首次实现海基网捕回收",
    "项目目标：制定学术级概念运载火箭CRLV-1的任务需求",
    "重点：性能 + 可重复使用 + 可持续性（创新GRI指标）",
    "规模定位：1.2-2吨级LEO/SSO有效载荷（中小型概念验证）"
])

# Slide 3: 研究方法与数据来源
add_content_slide(prs, "研究方法与数据来源", [
    "系统性文献与新闻调研（2025-2026最新数据）",
    "多源交叉验证：SpaceNews、Ars Technica、Global Times、中国航天资讯",
    "重点参考运载器：Falcon 9、New Glenn、朱雀三号、长征10B、Hyperbola-3、Pallas-1",
    "可持续性数据来源于近期生命周期评估（LCA）研究",
    "所有定量数据均经过至少两个独立来源交叉核实",
    "非公开来源数据明确标注为“估算”"
])

# Slide 4: 关键统计数据
stats = [
    ("Falcon 9 可重复使用\nLEO载荷", "22,800 kg"),
    ("长征10B 网捕回收\nLEO载荷（2026）", "16,000 kg"),
    ("朱雀三号 回收目标\nLEO载荷", "~18,300 kg"),
    ("传统RP-1/LOX\n每吨载荷CO₂e", "~19 吨")
]
add_stat_slide(prs, "2026年主要运载器关键数据", stats)

# Slide 5: 任务陈述
add_content_slide(prs, "任务陈述与L0目标", [
    "任务陈述：研制概念型部分可重复使用运载火箭CRLV-1",
    "目标有效载荷：1,200 kg（门槛）~ 2,000 kg（目标）至LEO/SSO",
    "可重复使用：一级至少10次（门槛）/20次（目标）",
    "翻新成本：低于新制造阶段的15%",
    "经济性：单次发射 recurring cost 目标 < 2,800 USD/kg",
    "可持续性：生命周期CO₂e < 15 t/吨载荷（基于LCA基线估算）",
    "响应性：载荷集成后30天内发射能力"
])

# Slide 6: 需求层次（表格风格）
add_content_slide(prs, "关键L1需求（节选）", [
    "L1-P01：500 km LEO 可重复使用载荷 ≥ 1,200 kg",
    "L1-R01：5次飞行后一级回收成功率 ≥ 90%",
    "L1-R03：必须评估海基网捕回收架构（长征10B 2026验证）",
    "L1-E01：优先采用LOX/LCH4推进剂",
    "L1-E02：引入Green Reusability Index (GRI) 作为核心评价指标",
    "L1-C01：单次发射 recurring cost ≤ 350万美元（门槛）",
    "所有需求均定义验证方法（分析、仿真、飞行试验）"
])

# Slide 7: 载荷对比图
add_figure_slide(
    prs, 
    "可重复使用运载器载荷能力对比（2026数据）",
    f"{figures_dir}/payload_comparison.png",
    "CRLV-1 定位于中小型概念验证级别，便于聚焦可重复使用与可持续性权衡研究"
)

# Slide 8: 成本趋势
add_figure_slide(
    prs,
    "发射成本下降趋势（可重复使用驱动）",
    f"{figures_dir}/cost_trend.png",
    "数据基于公开报告估算；可重复使用是成本降低的核心驱动力"
)

# Slide 9: 创新GRI指标
add_figure_slide(
    prs,
    "创新指标：Green Reusability Index (GRI)",
    f"{figures_dir}/gri_comparison.png",
    "GRI = 有效载荷 / (单次飞行CO₂e + 翻新惩罚)；将可持续性提升为一级设计驱动因素"
)

# Slide 10: 回收架构
add_content_slide(prs, "回收架构选择（基于最新验证）", [
    "方案A（基线）：推进式垂直着陆 + 栅格翼 + 着陆腿",
    "已验证：Falcon 9、朱雀三号、Hyperbola-3 等",
    "方案B（创新）：海基网捕系统",
    "长征10B 2026年7月10日首次成功演示（无着陆腿）",
    "优势：可显著降低一级结构质量（无腿质量惩罚）",
    "挑战：需要专用回收船队基础设施",
    "Day 6 将开展详细权衡研究"
])

# Slide 11: 利益相关方与FoM
add_content_slide(prs, "利益相关方与评价指标权重", [
    "主要利益相关方：商业星座运营商（类Guowang/千帆）、政府机构、科研用户",
    "核心评价指标（FoM）权重：",
    "   有效载荷（可重复使用）  30%",
    "    recurring cost/kg         25%",
    "   可重复使用性（次数+周转） 20%",
    "   可持续性（GRI）           15%  ← 创新点",
    "   响应性                    10%",
    "需求直接响应专用发射、成本降低、环境责任三大需求"
])

# Slide 12: 结论 + 结束
add_end_slide(prs)

# Save
prs.save(output_path)
print(f"PPT generated successfully: {output_path}")
print(f"Total slides: {len(prs.slides)}")