# TBUGE Mechatronix — Artificial Intelligence and Robotics

A complete four-year course in AI and robotics, written as one book: **48 courses, 480 chapters, about 960,000 words**. Course codes from the original syllabus (`AI. 101`, `AI. 102`, …) are removed; every subject is identified by its plain name and its place in the running order.

## What is in this repository

```
book/
  outline.json                 single source of truth: 48 courses, 10 chapters each
  00-front-matter.md           title page, preface, how to use the book
  01-table-of-contents.md      generated from outline.json
  02-how-to-write-this-book.md THE PLAN: how to get from the table of contents to the last page
  03-style-guide.md            plain-English rules, with before/after examples
  04-chapter-template.md       the eight-part chapter recipe, with a filled example
  concept-homes.md             which course owns which concept (stops repetition)
  courses/
    course-01-introduction-to-artificial-intelligence/
      00-course-introduction.md
      chapter-01 … chapter-10 (.md)
      11-course-review-and-assessment.md
    … one folder per course as it is written
tools/
  booktool.py                  toc | scaffold | status | style | build
```

## The method in one paragraph

Never write a book. Write one chapter, 480 times, using the same eight-part recipe: Opening, Big Picture, Key Words, The Explanation (three steps, worked examples with real numbers), Where It Goes Wrong, Case Note, Mini-Lab, Recap and Questions. Each chapter is about 1,800 words; ten chapters plus a course introduction, review, assessment and glossary make **20,000+ words per course**, enforced by a word counter rather than by feel. The full method, schedules and quality gates are in `book/02-how-to-write-this-book.md`.

## Commands

```bash
python3 tools/booktool.py toc               # regenerate the table of contents
python3 tools/booktool.py scaffold --course 2   # create empty chapters for a course
python3 tools/booktool.py status            # word count per course, PASS/FAIL at 20,000
python3 tools/booktool.py style book/courses/course-01-*/*.md --strict
python3 tools/booktool.py build             # stitch the whole book into one Markdown file
```

`status` prints one line per course with the chapter count, the word count and the percentage of the 20,000-word target.

## Progress

| | |
|---|---|
| Courses outlined | 48 / 48 |
| Chapters outlined | 480 / 480 |
| Courses written | 5 / 48 — Introduction to Artificial Intelligence; Robotics Fundamentals; Machine Learning; Computer Vision; Natural Language Processing |
| Volumes published as PDF | 5 / 48 — Volume One (86 pages), Volume Two (84 pages), Volume Three (81 pages), Volume Four (86 pages), Volume Five (85 pages) |
| Words written | 109,000 |
| Book written | about 10.4% |

Course 1 is the **pilot**: it is complete, it passes the word-count gate, and it sets the voice and the shape that the other 47 courses follow. The remaining courses are written one folder at a time, in syllabus order, using `book/02-how-to-write-this-book.md`.

## Published volumes

| Volume | Title | Pages | Words | File |
|---|---|---|---|---|
| I | Introduction to Artificial Intelligence | 86 | 24,400 | `book/volumes/volume-01/out/AI-and-Robotics-Volume-1-Introduction-to-Artificial-Intelligence.pdf` |
| II | Robotics Fundamentals | 84 | 22,600 | `book/volumes/volume-02/out/AI-and-Robotics-Volume-2-Robotics-Fundamentals.pdf` |
| III | Machine Learning | 81 | 20,000 | `book/volumes/volume-03/out/AI-and-Robotics-Volume-3-Machine-Learning.pdf` |
| IV | Computer Vision | 86 | 22,200 | `book/volumes/volume-04/out/AI-and-Robotics-Volume-4-Computer-Vision.pdf` |
| V | Natural Language Processing | 85 | 20,200 | `book/volumes/volume-05/out/AI-and-Robotics-Volume-5-Natural-Language-Processing.pdf` |

Each volume is written as continuous book prose (not a templated chapter grid) and typeset to 6 × 9 inches with running heads, contents, part dividers, glossary and sources.

Build a volume's PDF:

```bash
pip install --break-system-packages reportlab pyphen pypdfium2 pillow
python3 tools/make_pdf.py book/volumes/volume-01
python3 tools/make_pdf.py book/volumes/volume-02
python3 tools/make_pdf.py book/volumes/volume-03
python3 tools/make_pdf.py book/volumes/volume-04
python3 tools/make_pdf.py book/volumes/volume-05
```

## Writing order

Write in the order the student reads, not the order that feels easy. Course 2 (Robotics Fundamentals) is next, because it turns the agent loop of Course 1 into a physical body. Courses 3–6 then build on both.
