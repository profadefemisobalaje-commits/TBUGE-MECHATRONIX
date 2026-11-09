#!/usr/bin/env python3
"""Typeset a volume of 'Artificial Intelligence and Robotics' as a print-ready PDF.

Usage:  python3 tools/make_pdf.py book/volumes/volume-01

The volume directory must contain src/*.md files. The manifest below fixes the
reading order. Markdown is parsed through a deliberately small subset:
  # H1        chapter title          ## H2   section      ### H3  subsection
  > quote     aside box              - item  bullet      1. item  numbered
  | a | b |   table                  ---     scene break
Inline: **bold**, *italic*, `code`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

# ------------------------------------------------------------------ geometry

PAGE_W, PAGE_H = 6.0 * inch, 9.0 * inch
M_TOP, M_BOT = 0.74 * inch, 0.80 * inch
M_IN, M_OUT = 0.74 * inch, 0.66 * inch          # left/right (single-sided)
FRAME_W = PAGE_W - M_IN - M_OUT
FRAME_H = PAGE_H - M_TOP - M_BOT

INK = colors.HexColor("#111111")
GREY = colors.HexColor("#666666")
RULE = colors.HexColor("#999999")
LIGHT = colors.HexColor("#e8e8e8")

BODY_FONT, BODY_SIZE, LEADING = "Times-Roman", 10.4, 15.2
SANS, SANS_B = "Helvetica", "Helvetica-Bold"

# ------------------------------------------------------------------ styles

def style(name, **kw):
    return ParagraphStyle(name, fontName=kw.pop("fontName", BODY_FONT),
                          fontSize=kw.pop("fontSize", BODY_SIZE),
                          leading=kw.pop("leading", LEADING),
                          textColor=kw.pop("textColor", INK), **kw)


S_BODY = style("body", alignment=TA_JUSTIFY, firstLineIndent=0, spaceBefore=0,
               spaceAfter=0, hyphenationLang="en_GB", embeddedHyphenation=1,
               uriWasteReduce=0.3)
S_BODY_IND = style("body_ind", parent=S_BODY, firstLineIndent=13)
S_BULLET = style("bullet", parent=S_BODY, leftIndent=14, bulletIndent=2,
                 spaceBefore=3.2, spaceAfter=0)
S_NUM = style("num", parent=S_BODY, leftIndent=16, firstLineIndent=-16,
              spaceBefore=3.2)
S_H2 = style("h2", fontName="Times-Bold", fontSize=12.4, leading=15, spaceBefore=15,
             spaceAfter=5, alignment=TA_LEFT, keepWithNext=1)
S_H3 = style("h3", fontName="Times-Italic", fontSize=11, leading=14, spaceBefore=11,
             spaceAfter=3, alignment=TA_LEFT, keepWithNext=1)
S_QUOTE = style("quote", fontSize=9.5, leading=13.4, leftIndent=16, rightIndent=12,
                alignment=TA_JUSTIFY, textColor=colors.HexColor("#222222"),
                spaceBefore=8, spaceAfter=8)
S_TOC_H = style("toc_h", fontName="Times-Bold", fontSize=17, leading=22,
                alignment=TA_CENTER, spaceAfter=20)
S_TABLE = style("table", fontSize=8.5, leading=11, alignment=TA_LEFT)
S_TABLE_B = style("table_b", fontName="Times-Bold", fontSize=8.5, leading=11,
                  alignment=TA_LEFT)
S_CAP = style("cap", fontName="Times-Italic", fontSize=8.6, leading=12,
              alignment=TA_CENTER, spaceBefore=4, spaceAfter=10, textColor=GREY)
S_BIB = style("bib", fontSize=9.6, leading=13.2, leftIndent=15, firstLineIndent=-15,
             spaceBefore=5, alignment=TA_JUSTIFY)
S_GLOSS = style("gloss", fontSize=9.8, leading=13.4, leftIndent=13, firstLineIndent=-13,
                spaceBefore=3.5, alignment=TA_JUSTIFY)
S_BREAK = style("break", alignment=TA_CENTER, spaceBefore=10, spaceAfter=10)

# front matter
S_HALF = style("half", fontName="Times-Roman", fontSize=15, leading=20, alignment=TA_CENTER)
S_TITLE = style("title", fontName="Times-Bold", fontSize=30, leading=34, alignment=TA_CENTER)
S_SUBTITLE = style("subtitle", fontName="Times-Italic", fontSize=15, leading=20,
                   alignment=TA_CENTER)
S_VOL = style("vol", fontName=SANS, fontSize=9.5, leading=14, alignment=TA_CENTER,
              textColor=GREY)
S_IMPRINT = style("imprint", fontSize=8.6, leading=12.6, alignment=TA_LEFT,
                  textColor=colors.HexColor("#333333"))
S_PARTNUM = style("partnum", fontName=SANS, fontSize=9.5, leading=14,
                  alignment=TA_CENTER, textColor=GREY)
S_PARTTITLE = style("parttitle", fontName="Times-Bold", fontSize=23, leading=28,
                    alignment=TA_CENTER)

# ------------------------------------------------------------------ helpers

UNICODE_FIX = {"\u2212": "-", "\u03c0": "pi", "\u2264": "<=", "\u2265": ">=",
               "\u2248": "~", "\u00d7": "x", "\u00b7": ".", "\u2011": "-"}


def safe(text: str) -> str:
    text = "".join(UNICODE_FIX.get(ch, ch) for ch in text)
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r'<font face="Courier" size="9">\1</font>', text)
    return text


class ChapterOpen(Flowable):
    """Chapter number, title, rule; also plants a PDF bookmark and page flags."""

    def __init__(self, number: str, title: str):
        Flowable.__init__(self)
        self.number, self.title = number, title
        self.width = FRAME_W

    def wrap(self, aw, ah):
        self.height = 118
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(GREY)
        c.setFont(SANS, 8.6)
        label = "CHAPTER " + self.number.upper()
        c.drawString(0, self.height - 12, " ".join(label))
        c.setFillColor(INK)
        c.setFont("Times-Bold", 21)
        y = self.height - 46
        for line in wrap_lines(self.title, "Times-Bold", 21, FRAME_W):
            c.drawString(0, y, line)
            y -= 25
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(0, y + 12, FRAME_W, y + 12)
        c.restoreState()
        self.canv.bookmarkPage("ch-" + self.number)
        self.canv.addOutlineEntry(self.title, "ch-" + self.number, 1, 0)


class PartPage(Flowable):
    """A full-page part divider: small label above, large title, short rule."""

    def __init__(self, label: str, title: str):
        Flowable.__init__(self)
        self.label, self.title = label, title

    def wrap(self, aw, ah):
        self.height = FRAME_H - 40
        self.width = FRAME_W
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.saveState()
        mid = self.height / 2
        c.setFillColor(GREY)
        c.setFont(SANS, 8.8)
        c.drawCentredString(FRAME_W / 2, mid + 46, " ".join(self.label.upper()))
        c.setFillColor(INK)
        c.setFont("Times-Bold", 23)
        y = mid + 8
        for line in wrap_lines(self.title, "Times-Bold", 23, FRAME_W - 40):
            c.drawCentredString(FRAME_W / 2, y, line)
            y -= 29
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(FRAME_W / 2 - 34, y - 6, FRAME_W / 2 + 34, y - 6)
        c.restoreState()
        key = "part-" + self.label.replace(" ", "-").lower()
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(self.title, key, 0, 0)


class SetHead(Flowable):
    """Clears the running head (used at the start of front matter and parts)."""

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        doc = getattr(self.canv, "_doctemplate", None)
        if doc is not None:
            doc.chapter = ""


def wrap_lines(text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if stringWidth(trial, font, size) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


class TocMark(Flowable):
    """Invisible marker that registers a contents entry and a bookmark."""

    def __init__(self, title: str):
        Flowable.__init__(self)
        self.title = title

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        key = "t-" + str(abs(hash(self.title)) % 10**8)
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(self.title, key, 0, 0)
        doc = getattr(self.canv, "_doctemplate", None)
        if doc is not None:
            doc.chapter = self.title


def title_block(text, size=19, space_after=18):
    """Rule, centred title, spacing -- used for front and back matter."""
    return [Rule(width=FRAME_W, color=RULE, space=3),
            Spacer(1, 2),
            TocMark(text),
            Paragraph(safe(text), style("tb" + str(size),
                                        fontName="Times-Bold", fontSize=size,
                                        leading=size * 1.25, alignment=TA_CENTER,
                                        spaceAfter=space_after))]


class Rule(Flowable):
    def __init__(self, width=FRAME_W, thickness=0.6, color=RULE, space=6):
        Flowable.__init__(self)
        self.width, self.t, self.c, self.space = width, thickness, color, space

    def wrap(self, aw, ah):
        return (self.width, self.space * 2)

    def draw(self):
        self.canv.setStrokeColor(self.c)
        self.canv.setLineWidth(self.t)
        self.canv.line(0, self.space, self.width, self.space)


# ------------------------------------------------------------------ parsing

def parse_table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [r for r in cells if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
    if not cells:
        return None
    data = []
    for i, row in enumerate(cells):
        st = S_TABLE_B if i == 0 else S_TABLE
        data.append([Paragraph(safe(c), st) for c in row])
    ncol = max(len(r) for r in data)
    for r in data:
        while len(r) < ncol:
            r.append(Paragraph("", S_TABLE))
    col_w = FRAME_W / ncol
    t = Table(data, colWidths=[col_w] * ncol, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f2f2f2")),
        ("LINEABOVE", (0, 0), (-1, 0), 0.6, RULE),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, RULE),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, RULE),
    ]))
    return t


def parse_markdown(text: str):
    """Return list of (kind, payload) blocks."""
    lines = text.splitlines()
    blocks, i = [], 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        if not line:
            i += 1
            continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip())); i += 1; continue
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip())); i += 1; continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:].strip())); i += 1; continue
        if line in ("---", "***"):
            blocks.append(("break", "")); i += 1; continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i]); i += 1
            blocks.append(("table", rows)); continue
        if line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip()); i += 1
            blocks.append(("quote", " ".join(x for x in quote if x))); continue
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            num, first = m.group(1), m.group(2)
            body = [first]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                    r"^(#|>|\||-\s|\d+\.\s|---)", lines[i].strip()):
                body.append(lines[i].strip()); i += 1
            blocks.append(("num", (num, " ".join(body)))); continue
        if re.match(r"^[-*]\s+", line):
            body = [line[2:].strip()]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                    r"^(#|>|\||-\s|\d+\.\s|---)", lines[i].strip()):
                body.append(lines[i].strip()); i += 1
            blocks.append(("bullet", " ".join(body))); continue
        para = [line]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#|>|\||-\s|\d+\.\s|---)", lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


NUMBER_WORDS = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]


def word_number(n: int) -> str:
    return NUMBER_WORDS[n - 1] if 1 <= n <= 20 else str(n)


# ------------------------------------------------------------------ document

class Book(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, pagesize=(PAGE_W, PAGE_H),
                                 leftMargin=M_IN, rightMargin=M_OUT,
                                 topMargin=M_TOP, bottomMargin=M_BOT,
                                 title="Artificial Intelligence and Robotics: Volume One",
                                 author="TBUGE Mechatronix", subject="Artificial intelligence and robotics: a complete course in plain English", creator="TBUGE Mechatronix typesetting pipeline", **kw)
        frame_body = Frame(M_IN, M_BOT, FRAME_W, FRAME_H, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        frame_front = Frame(M_IN, M_BOT, FRAME_W, FRAME_H, id="front",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="front", frames=[frame_front], onPage=self._bg_front,
                         onPageEnd=self._fg_front),
            PageTemplate(id="body", frames=[frame_body], onPage=self._bg_body,
                         onPageEnd=self._fg_body),
        ])
        self.chapter = ""
        self.suppress = set()
        self.no_number = set()
        self.heads = []          # [(page, title)] in document order

    # -------------------------------------------------- decoration
    def _head_for(self, pn):
        title = ""
        for start, text in self.heads:
            if start <= pn:
                title = text
            else:
                break
        return title

    def _deco(self, canv, doc, number=True, head=True):
        pn = canv.getPageNumber()
        canv.saveState()
        running = doc._head_for(pn)
        if head and running and pn not in doc.suppress:
            canv.setFont(SANS, 7.6)
            canv.setFillColor(GREY)
            title = running
            if stringWidth(title, SANS, 7.6) > FRAME_W * 0.8:
                while stringWidth(title, SANS, 7.6) > FRAME_W * 0.8 and len(title) > 10:
                    title = title[:-2]
                title = title.rstrip() + "\u2026"
            canv.drawString(M_IN, PAGE_H - M_TOP + 16, title)
            canv.setStrokeColor(LIGHT)
            canv.setLineWidth(0.5)
            canv.line(M_IN, PAGE_H - M_TOP + 10, M_IN + FRAME_W, PAGE_H - M_TOP + 10)
        if number and pn not in doc.no_number:
            canv.setFont(BODY_FONT, 9.2)
            canv.setFillColor(GREY)
            canv.drawCentredString(PAGE_W / 2, M_BOT - 26, str(pn))
        canv.restoreState()

    def _bg_front(self, canv, doc):
        pass

    def _fg_front(self, canv, doc):
        self._deco(canv, doc, number=False, head=False)

    def _bg_body(self, canv, doc):
        pass

    def _fg_body(self, canv, doc):
        self._deco(canv, doc)

    def handle_documentBegin(self):
        self.heads = []
        self.suppress = set()
        self.no_number = set()
        self.chapter = ""
        BaseDocTemplate.handle_documentBegin(self)

    # -------------------------------------------------- bookmarks / toc
    def afterFlowable(self, flowable):
        if isinstance(flowable, ChapterOpen):
            self.chapter = flowable.title
            self.heads.append((self.page, flowable.title))
            self.suppress.add(self.page)
            self.notify("TOCEntry", (1, flowable.title, self.page))
        elif isinstance(flowable, TocMark):
            self.heads.append((self.page, flowable.title))
            self.notify("TOCEntry", (0, flowable.title, self.page))
        elif isinstance(flowable, PartPage):
            self.suppress.add(self.page)
            self.no_number.add(self.page)
            self.notify("TOCEntry", (0, flowable.label + "  \u00b7  " + flowable.title,
                                     self.page))


# ------------------------------------------------------------------ build

def build(volume_dir: Path):
    src = volume_dir / "src"
    out = volume_dir / "out"
    out.mkdir(parents=True, exist_ok=True)

    def md(name):
        p = src / name
        return p.read_text(encoding="utf-8") if p.exists() else ""

    doc = Book(str(out / "AI-and-Robotics-Volume-1-Introduction-to-Artificial-Intelligence.pdf"))
    story = []

    # ---- half title
    story += [Spacer(1, 150),
              Paragraph("Artificial Intelligence and Robotics", S_HALF),
              Spacer(1, 10),
              Paragraph("A Complete Course in Plain English", S_SUBTITLE),
              PageBreak()]

    # ---- title page
    story += [Spacer(1, 120),
              Paragraph("ARTIFICIAL INTELLIGENCE<br/>AND ROBOTICS", S_TITLE),
              Spacer(1, 26),
              Rule(width=90, color=RULE, space=8),
              Spacer(1, 26),
              Paragraph("Volume One", S_VOL),
              Spacer(1, 8),
              Paragraph("Introduction to Artificial Intelligence", S_SUBTITLE),
              Spacer(1, 150),
              Paragraph("TBUGE MECHATRONIX", S_VOL),
              PageBreak()]

    # ---- imprint
    story += [Spacer(1, 330)]
    for para in md("02-imprint.md").split("\n\n"):
        para = para.strip()
        if para:
            story += [Paragraph(safe(para.replace("\n", " ")), S_IMPRINT), Spacer(1, 7)]
    story += [PageBreak(), NextPageTemplate("body")]

    # ---- contents
    story += [Spacer(1, 8), Paragraph("Contents", S_TOC_H)]
    toc = TableOfContents()
    toc.levelStyles = [
        style("toc0", fontName="Times-Bold", fontSize=10.6, leading=15,
              leftIndent=0, firstLineIndent=0, spaceBefore=12, spaceAfter=2),
        style("toc1", fontSize=10.2, leading=14.4, leftIndent=12, firstLineIndent=-12,
              spaceBefore=1.6),
    ]
    toc.dotsMinLevel = 1
    story += [toc, PageBreak()]

    # ---- preface + plan
    story += [SetHead()]
    for name in ("03-preface.md", "04-plan.md"):
        text = md(name).strip()
        if not text:
            continue
        blocks = parse_markdown(text)
        first = True
        for kind, payload in blocks:
            if kind == "h1":
                story += [Spacer(1, 6)] + title_block(payload)
                first = False
            elif kind == "h2":
                story += [Paragraph(safe(payload), S_H2)]
                first = True
            elif kind == "p":
                story += [Paragraph(safe(payload), S_BODY if first else S_BODY_IND)]
                first = False
            elif kind == "quote":
                story += [Paragraph(safe(payload), S_QUOTE)]
            elif kind == "bullet":
                story += [Paragraph(safe(payload), S_BULLET, bulletText="\u2022")]

    # ---- parts and chapters
    seq = []
    for f in sorted(src.iterdir()):
        if f.suffix != ".md":
            continue
        if "-part-" in f.name:
            seq.append(("part", f))
        elif re.search(r"-ch\d", f.name):
            seq.append(("chapter", f))

    ch_no = 0
    part_no = 0
    part_titles = {}
    after_part = False
    for kind, f in seq:
        blocks = parse_markdown(f.read_text(encoding="utf-8"))
        title = next((p for k, p in blocks if k == "h1"), f.stem)
        blocks = [(k, p) for k, p in blocks if k != "h1"]

        if kind == "part":
            part_no += 1
            subtitle = next((p for k, p in blocks if k == "h2"), "")
            label = "Part " + word_number(part_no)
            story += [PageBreak(), SetHead(),
                      PartPage(label, subtitle or title), PageBreak()]
            part_titles[label] = subtitle or title
            after_part = True
            continue

        ch_no += 1
        if ch_no > 1 and not after_part:
            story += [PageBreak()]
        after_part = False
        story += [ChapterOpen(word_number(ch_no), title)]
        first_body = True
        for kind2, payload in blocks:
            if kind2 == "h2":
                story += [Paragraph(safe(payload), S_H2)]
                first_body = True
            elif kind2 == "h3":
                story += [Paragraph(safe(payload), S_H3)]
                first_body = True
            elif kind2 == "p":
                story += [Paragraph(safe(payload), S_BODY if first_body else S_BODY_IND)]
                first_body = False
            elif kind2 == "quote":
                story += [Spacer(1, 2), Paragraph(safe(payload), S_QUOTE)]
            elif kind2 == "bullet":
                story += [Paragraph(safe(payload), S_BULLET, bulletText="\u2022")]
            elif kind2 == "num":
                n, body = payload
                story += [Paragraph(f"<b>{n}.</b>&nbsp;&nbsp;{safe(body)}",
                                    style("num2", parent=S_NUM, firstLineIndent=0,
                                          leftIndent=16))]
            elif kind2 == "table":
                tb = parse_table(payload)
                if tb:
                    story += [Spacer(1, 7), tb, Spacer(1, 9)]
            elif kind2 == "break":
                story += [Paragraph("* * *", S_BREAK)]

    # ---- back matter
    for name in ("90-glossary.md", "91-sources.md"):
        text = md(name).strip()
        if not text:
            continue
        story += [PageBreak()]
        for kind, payload in parse_markdown(text):
            if kind == "h1":
                story += [Spacer(1, 6)] + title_block(payload)
            elif kind == "h2":
                story += [Paragraph(safe(payload), S_H2)]
            elif kind == "p":
                st = S_GLOSS if name.startswith("90") else S_BIB
                story += [Paragraph(safe(payload), st)]
            elif kind == "bullet":
                story += [Paragraph(safe(payload), S_BULLET, bulletText="\u2022")]

    doc.multiBuild(story)
    return out / "AI-and-Robotics-Volume-1-Introduction-to-Artificial-Intelligence.pdf"


if __name__ == "__main__":
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "book/volumes/volume-01")
    pdf = build(target)
    print("wrote", pdf)
