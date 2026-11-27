# -*- coding: utf-8 -*-
"""Generate the 1200x630 social share image. Requires Pillow (dev-only)."""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "og.png"
W, H = 1200, 630

BG = "#f5f4ee"
PAPER = "#fffefa"
INK = "#173a35"
MUTED = "#61716b"
LINE = "#d9dfd6"
ACCENT = "#176952"
SOFT = "#edf0e3"

FONT_DIR = Path("C:/Windows/Fonts")
SERIF_BOLD = str(FONT_DIR / "georgiab.ttf")
CJK_BOLD = str(FONT_DIR / "msyhbd.ttc")
CJK_REGULAR = str(FONT_DIR / "msyh.ttc")


def spaced(draw, xy, text, font, fill, tracking=3):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


def main():
    data = json.loads((ROOT / "data/tools.json").read_text(encoding="utf-8"))
    cats = len({d["cat"] for d in data})
    hot = sum(1 for d in data if d.get("hot"))

    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((20, 20, W - 20, H - 20), radius=18, outline=LINE, width=2)

    # Brand
    brand = ImageFont.truetype(SERIF_BOLD, 36)
    slash = ImageFont.truetype(SERIF_BOLD, 30)
    x = 80
    draw.text((x, 62), "Agent", font=brand, fill=INK)
    x += draw.textlength("Agent", font=brand)
    draw.text((x, 68), " / ", font=slash, fill=ACCENT)
    x += draw.textlength(" / ", font=slash)
    draw.text((x, 62), "Atlas", font=brand, fill=INK)
    spaced(draw, (80, 118), "A CURATED TOOLBOX FOR AGENTS", ImageFont.truetype(CJK_REGULAR, 13), MUTED, 2)

    draw.line((80, 168, 168, 168), fill=ACCENT, width=3)

    # Title
    title = ImageFont.truetype(CJK_BOLD, 76)
    draw.text((80, 200), "好用的工具，", font=title, fill=INK)
    draw.text((80, 294), "值得放进工具箱。", font=title, fill=ACCENT)

    # Subtitle
    sub = ImageFont.truetype(CJK_REGULAR, 25)
    draw.text((80, 416), f"{len(data)} 项工具 · {cats} 个能力领域 · {hot} 项近期热门", font=sub, fill=MUTED)

    # Stats column
    draw.line((828, 224, 828, 486), fill=LINE, width=2)
    num_font = ImageFont.truetype(SERIF_BOLD, 58)
    label_font = ImageFont.truetype(CJK_REGULAR, 17)
    stats = [(str(len(data)), "项工具与运行环境"), (str(cats), "个能力领域"), (str(hot), "项近期热门")]
    for i, (num, label) in enumerate(stats):
        y = 232 + i * 90
        draw.text((872, y), num, font=num_font, fill=ACCENT)
        draw.text((872 + draw.textlength(num, font=num_font) + 12, y + 36), label, font=label_font, fill=MUTED)

    # Tool chips
    chip_font = ImageFont.truetype(CJK_REGULAR, 19)
    x, y = 80, 500
    for name in ("MinerU", "OpenMontage", "VoiceStudio", "DeepSeek Harness", "Astryx", "shadcn/ui"):
        width = draw.textlength(name, font=chip_font) + 38
        if x + width > 1120:
            break
        draw.rounded_rectangle((x, y, x + width, y + 46), radius=8, fill=SOFT)
        draw.text((x + 19, y + 11), name, font=chip_font, fill=INK)
        x += width + 10

    # Footer
    foot = ImageFont.truetype(CJK_REGULAR, 16)
    draw.text((80, 574), "jingao-shen.github.io/agent-capability-atlas", font=foot, fill=MUTED)
    tag = ImageFont.truetype(SERIF_BOLD, 15)
    draw.text((W - 80 - draw.textlength("FIELD GUIDE / 002 · 2026.11", font=tag), 576), "FIELD GUIDE / 002 · 2026.11", font=tag, fill=MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    sys.exit(main())
