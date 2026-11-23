#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news front page (1024x1024).

Every word on the page is typeset here with real fonts (PIL), so no
headline can come out garbled: the AI picture is used only as the hero
photograph panel, labelled "Illustration" in its caption.
Writes entry.png next to this script.
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps

PAGE_W, PAGE_H = 1024, 1024
PAD = 28
TEXT_W = PAGE_W - 2 * PAD

PAPER = (253, 252, 247)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (20, 48, 92)
GREY = (90, 90, 90)
RULE = (200, 198, 190)

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_ITAL = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def fit_lines(draw, text, fnt, width):
    """Greedy wrap: return the lines of `text` that fit in `width` px."""
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def put_lines(draw, lines, x, y, fnt, fill, step):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += step
    return y


# (kicker, kicker colour, headline, body)
GRID = [
    ("CLIMATE", (0, 110, 70),
     "COP31 collapses with no climate deal",
     "UN talks in Antalya end after two days of overtime, split over "
     "fossil fuels and finance. Guterres calls it deeply disappointing."),
    ("WORLD COURT", (122, 60, 140),
     "Myanmar guilty of Rohingya genocide",
     "The UN's top court rules Myanmar committed genocide against the "
     "Rohingya minority, in a landmark verdict welcomed by survivors."),
    ("MIDDLE EAST", NAVY,
     "Iran hits Bahrain plant and Gulf tankers",
     "An Iranian strike sets fire to a plant in Sitra, Bahrain, as a "
     "tanker is seized in the Gulf of Oman and shipping fears grow."),
    ("EUROPE", (150, 90, 0),
     "UK and EU strike post-Brexit deal",
     "Britain and the EU agree closer trade and travel ties, with youth "
     "mobility and simpler food trade, six years after Brexit."),
]


def build():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, PAGE_W - 7, PAGE_H - 7], outline=INK, width=4)

    y = 20
    # Masthead
    f_mast = F(SERIF_BOLD, 62)
    mast = "THE WORLD TODAY"
    d.text(((PAGE_W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 76
    d.rectangle([PAD, y, PAGE_W - PAD, y + 4], fill=RED)
    y += 12

    # Date strip
    f_date = F(SANS_BOLD, 23)
    date_txt = "SUNDAY, 22 NOVEMBER 2026  \u2022  THE DAY IN WORLD NEWS"
    d.rectangle([PAD, y, PAGE_W - PAD, y + 40], fill=INK)
    d.text(((PAGE_W - d.textlength(date_txt, font=f_date)) / 2, y + 7),
           date_txt, font=f_date, fill=(255, 255, 255))
    y += 52

    # Hero photograph (AI illustration, cropped to fill)
    hero = Image.open("hero.png").convert("RGB")
    hero = ImageOps.fit(hero, (TEXT_W, 268), method=Image.LANCZOS)
    img.paste(hero, (PAD, y))
    d.rectangle([PAD, y, PAGE_W - PAD, y + 268], outline=INK, width=2)
    y += 268 + 6
    f_cap = F(SANS_ITAL, 14)
    cap = ("Smoke rises from the Russian corvette Merkury at Benghazi naval "
           "base, Libya, after a sea-drone strike.  Illustration.")
    d.text((PAD, y), cap, font=f_cap, fill=GREY)
    y += 24

    # Lead headline + subhead
    f_head = F(SANS_BOLD, 36)
    head = "UKRAINE DRONES HIT RUSSIAN WARSHIP OFF LIBYA"
    while d.textlength(head, font=f_head) > TEXT_W and f_head.size > 27:
        f_head = F(SANS_BOLD, f_head.size - 1)
    d.text((PAD, y), head, font=f_head, fill=INK)
    y += 47
    f_sub = F(SANS_REG, 19)
    sub = ("Libyan officials say suspected Ukrainian sea drones struck the "
           "corvette Merkury at Benghazi \u2014 six drones, two hits, the ship "
           "badly damaged. Kyiv and Moscow have not confirmed it.")
    y = put_lines(d, fit_lines(d, sub, f_sub, TEXT_W), PAD, y, f_sub, INK, 25)
    y += 8
    d.line([PAD, y, PAGE_W - PAD, y], fill=INK, width=2)
    y += 12

    # 2x2 story grid
    col_w = (TEXT_W - 24) // 2
    row_h = 132
    f_kick = F(SANS_BOLD, 14)
    f_sh = F(SANS_BOLD, 21)
    f_sb = F(SANS_REG, 16)
    for i, (kick, color, sh, sb) in enumerate(GRID):
        cx = PAD + (i % 2) * (col_w + 24)
        cy = y + (i // 2) * (row_h + 10)
        d.text((cx, cy), kick, font=f_kick, fill=color)
        y2 = put_lines(d, fit_lines(d, sh, f_sh, col_w), cx, cy + 20,
                       f_sh, INK, 26)
        put_lines(d, fit_lines(d, sb, f_sb, col_w), cx, y2 + 2,
                  f_sb, (40, 40, 40), 20)
        if i % 2 == 0:
            d.line([cx + col_w + 12, cy, cx + col_w + 12, cy + row_h - 8],
                   fill=RULE, width=1)
    y += 2 * row_h + 10 + 6
    d.line([PAD, y, PAGE_W - PAD, y], fill=INK, width=2)
    y += 10

    # West Bank strip
    f_strip = F(SANS_REG, 17)
    strip = ("WEST BANK \u2014  Israeli opposition leader Eisenkot calls "
             "settler attacks on Palestinian villages \u2018Jewish terrorism\u2019 "
             "as cars burn and Israeli forces kill two in Gaza.")
    y = put_lines(d, fit_lines(d, strip, f_strip, TEXT_W), PAD, y,
                  f_strip, INK, 22)
    y += 10

    # Ticker
    f_tick = F(SANS_BOLD, 15)
    tick = ("ALSO TODAY  \u2022  Indonesia candy factory fire: 3 dead, 34 "
            "missing  \u2022  Russian strike on Kyiv flats kills 3  \u2022  "
            "El Chapo Isidro captured in Mexico, 11 dead  \u2022  Nigeria "
            "boat capsizes, 24 dead  \u2022  BepiColombo reaches Mercury")
    tlines = fit_lines(d, tick, f_tick, TEXT_W - 16)
    th = len(tlines) * 20 + 14
    d.rectangle([PAD, y, PAGE_W - PAD, y + th], fill=INK)
    ty = y + 7
    for ln in tlines:
        d.text((PAD + 8, ty), ln, font=f_tick, fill=(255, 255, 255))
        ty += 20
    y += th + 10

    # Footer
    f_foot = F(SANS_REG, 13)
    foot = ("All stories reported on 22 November 2026.  Sources: AP, "
            "Reuters, UN, Open Chronicle, KPFA.")
    d.text(((PAGE_W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GREY)

    img.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    build()
