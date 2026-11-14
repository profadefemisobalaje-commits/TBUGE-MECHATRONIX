# How to Write This Book: From Table of Contents to the End

This file is the working plan. It answers one question: *I have 48 courses and a table of contents — how do I actually reach the last page?*

---

## 1. First, look at the size of the job

| Item | Number |
|---|---|
| Courses | 48 |
| Chapters per course | 10 |
| Chapters in total | 480 |
| Words per chapter | about 1,800 |
| Words per course | about 20,000 (18,000 in chapters, about 2,000 in the course introduction, review and glossary) |
| Words in the whole book | about 960,000 |

That is a real library, not a weekend. One person cannot "just write it" in a month without the book turning thin and repetitive. So we do not write a book. We write **one chapter, 480 times**, using the same recipe. That is the whole method.

A chapter of 1,800 words is under four pages. Almost anyone can write that in one focused morning. The trick is that you never have to invent the shape of those pages again after today.

---

## 2. Decide what "finished" means before you write a word

Write these five sentences down and keep them above your desk. A book with no definition of done will never be done.

1. **Reader:** a first-year student with secondary-school maths, no robotics lab, and a laptop.
2. **Promise:** after each course, the reader can explain the ideas in their own words and do a small practical task.
3. **Length:** every course is at least 20,000 words, measured by the word counter, not by feeling.
4. **Voice:** plain English, short sentences, one idea per paragraph, every technical word defined before it is used.
5. **Shape:** every chapter has the same seven parts, in the same order, every time.

That is the contract. Everything below is how you keep it.

---

## 3. The seven-part chapter recipe (the engine of the book)

Do not write chapters. Fill in these eight boxes. Each box has a word budget, and the budgets add up to about 2,000 words.

| Part | What goes in it | Words |
|---|---|---|
| **1. Opening** | One sentence: "By the end of this chapter you can ...". Then a hook: a real situation, a short story, or a question the reader has met. | 130 |
| **2. Big Picture** | The one idea of the chapter, in a paragraph a 15-year-old could follow. No formulas. | 220 |
| **3. Key Words** | Four to six terms, each with a plain definition. These are the only words the rest of the chapter is allowed to use freely. | 180 |
| **4. The Explanation** | Three steps, from easy to hard. Each step has an everyday comparison, then the real thing, then a worked example with real numbers. | 620 |
| **5. Where It Goes Wrong** | Three to five mistakes students really make, each with the fix. This is where teaching happens. | 200 |
| **6. Case Note** | One true story from industry or research, showing the idea meeting the world, ending with the lesson for the reader. | 210 |
| **7. Mini-Lab** | Something the reader can do in 15-45 minutes with a laptop, a phone, or paper. | 150 |
| **8. Recap and Questions** | Three things to remember, three questions, one thing to try next. | 150 |

The eight parts add up to about 1,860 words, which in practice lands near 1,800 once sentences are tightened. Ten chapters give about 18,000 words. The remaining 2,000 come from two course-level files, written once per course:

| Course file | Contents | Words |
|---|---|---|
| `00-course-introduction.md` | Why the course comes where it does, what it feeds into, a week-by-week study plan, a table of the ten chapters | 700 |
| `11-course-review-and-assessment.md` | Twelve review questions with worked answers, three lab assignments with marking criteria, one project brief, a glossary, further reading | 1,300 |


Why a fixed recipe?

- You stop staring at a blank page, because the next box is always obvious.
- The reader learns the rhythm and reads faster.
- A missing box is easy to spot in review.
- Chapters stay the same length, so the 20,000-word target takes care of itself: **10 × 2,000 = 20,000**.

Write the boxes in order, but allow yourself to write Part 4 first if the explanation is already clear in your head. The order on the page is fixed. The order in your head is free. The Case Note is written last, because you should choose the story after you know exactly which idea it has to carry.

---

## 4. Before drafting: the one-page brief

Never start typing prose on a blank file. Spend 20 minutes filling one page per chapter. This is the highest-value step in the whole method, because it stops you from writing 900 words and then discovering you have no example.

Copy this into a scratch file for each chapter:

```
Chapter brief
Course:            Machine Learning
Chapter:           6 - Overfitting and Regularisation
Reader can already: fit a straight line, read a scatter plot
Reader cannot yet: explain why a perfect fit is bad
One idea:          a model that memorises is not a model that understands
Real-life hook:    a student who memorises past exam answers
Worked example:    6 points, degree-1 and degree-9 fit, error on new points
Key words:         overfitting, underfitting, generalisation, training set, test set, regularisation
Common mistakes:   judging by training error; tuning on test set; too little data
Mini-lab:          fit polynomials to 10 noisy points, plot error vs degree
Cross-links:       Course 3 ch.3 (loss), Course 22 ch.2 (data), Course 42 ch.9 (validation)
```

Twenty minutes here saves two hours of wandering. If you cannot fill a box, the chapter is not ready — go and read one source for that box only, then come back.

### The cross-link box is not optional

With 48 courses there is a real danger that Machine Learning, Pattern Recognition, Deep Learning and Robot Learning all explain the same three ideas in slightly different words. Readers notice, and they lose trust.

**Rule: every concept has one home course.** That course explains it fully. Every other course mentions it in one sentence and points back:

> We met overfitting in Course 3, Chapter 6. Here we only need one fact from it: a model that scores well on the data it was trained on may still fail on new data.

Keep a list of "homes" in a file (`book/concept-homes.md`) as you go. When you are tempted to explain something for the fourth time, check the list.

---

## 5. The five passes: from rough to finished

Each chapter goes through five passes. Do not try to do all five at once — that is how writing becomes slow and painful.

**Pass 1 — Skeleton (15 min).** Paste the seven headings. Write one rough sentence under each. The chapter is now "there" and cannot be lost.

**Pass 2 — Dirty draft (60–90 min).** Fill the boxes. Write badly on purpose. Do not stop to fix a sentence, look up a fact, or find a nicer word. If a fact is missing, write `[CHECK: ...]` and move on. Speed here is what makes the chapter possible.

**Pass 3 — Simple-English rewrite (40 min).** This is the pass that makes the book readable. Go sentence by sentence:
- Cut every sentence over 25 words into two.
- Replace every hard word with an everyday one (see the style guide).
- Delete the first sentence of any paragraph that only announces what the paragraph will say.
- Make sure every abstract sentence is followed by a concrete one.

**Pass 4 — Truth check (30 min).** Every number, unit, formula and claim. Fix all `[CHECK: ...]` marks. Recompute the worked example by hand or in a scratch script. If a claim cannot be checked, soften it honestly: "in most small robots" instead of "in all robots".

**Pass 5 — Read aloud (15 min).** Read the chapter out loud, or have your computer read it. Where you stumble, the reader will stumble. Rewrite those places. This pass finds about half of all remaining problems and costs almost nothing.

Total per chapter: about two and a half hours, plus another half day for the course introduction and the review file. One course is roughly one working week. 48 courses is 48 working weeks — a realistic year of full-time work, or two and a half years at ten hours a week.

---

## 6. The ten rules of simple English for this book

These rules are what "simple English for clearer explanations" means in practice. They are expanded, with before-and-after examples, in `book/03-style-guide.md`.

1. **One idea per sentence.** A sentence is a box that holds one thing.
2. **Average 15 words per sentence, maximum 25.** Vary the length so it does not sound like a machine.
3. **Define before you use.** First use: **torque** — a turning force. After that, free to use.
4. **Concrete before abstract.** Show the bicycle wheel before the formula for moment of inertia.
5. **Active voice, real subject.** "The controller reduces the error", not "the error is reduced".
6. **Say who does what.** "You", "the robot", "the sensor" — not "it is understood that".
7. **Numbers carry units, always.** 0.5 m, 3 s, 12 V, 40 °C. Never a bare 0.5.
8. **Examples use real numbers.** "Suppose the wheel has radius 0.1 m" beats "let r be the radius".
9. **Repeat on purpose.** Key ideas return three times: in the chapter, in the recap, in the next chapter's opening. Repetition is teaching, not padding.
10. **Never write to fill the counter.** If a box is empty, add a worked example, a mistake, or a comparison — never adjectives.

Rule 10 matters most. You have promised 20,000 words per course. The honest way to reach it is **more examples and more mistakes**, not longer sentences. A chapter with five worked examples is worth four chapters of fine-sounding paragraphs.

---

## 7. Quality gates: what a chapter must pass before it counts

Put a tick next to each line. If a line fails, the chapter is not finished, even if the word count is fine.

- [ ] Chapter word count is 1,700–2,000; the whole course folder is 20,000 or more.
- [ ] All seven parts are present, in order.
- [ ] The opening sentence finishes this: "By the end of this chapter you can ...".
- [ ] Every key word is bold on first use and has a plain definition.
- [ ] The explanation has at least one worked example with real numbers.
- [ ] There is at least one everyday comparison.
- [ ] There are at least three common mistakes, each with a fix.
- [ ] The Case Note is true, sourced, and about this chapter's idea rather than a general essay.
- [ ] The mini-lab can be done without buying anything.
- [ ] No sentence is longer than 30 words.
- [ ] Every number has a unit.
- [ ] No `[CHECK: ...]` marks left.
- [ ] Concepts owned by another course are pointed to, not re-taught.
- [ ] You read it aloud without stumbling.

Run the automated half of this with:

```
python3 tools/booktool.py style book/courses/course-01-*/chapter-01-*.md
python3 tools/booktool.py status
```

`status` prints a table of every course, its chapter count, its word count, and PASS/FAIL against 20,000. The target is enforced by the tool, not by memory.

---

## 8. The working loop that gets you to the end

Repeat this loop 48 times. It is deliberately boring — boring is what finishes books.

**Day 1 — Plan the course (1 hour).** Read the course's ten chapter titles. Fill one brief for each of the ten chapters (Section 4). Check the concept-homes list. Mark any chapter that is too big: if it needs more than one big idea, split it into two and merge two thin ones.

**Days 2–4 — Draft ten skeletons (3 × 1 hour).** Only skeletons: seven headings and one sentence each, for all ten chapters. Doing them together keeps the course coherent and stops repetition between neighbouring chapters.

**Days 5–14 — Two chapters a day (Passes 2–3).** Draft in the morning, simplify in the afternoon. Two chapters a day is a comfortable pace and finishes a course in ten working days.

**Day 15 — Truth pass and read-aloud, whole course (1 day).** Read the course top to bottom as a student would. Fix the joins between chapters: the end of chapter 3 should lead into the start of chapter 4.

**Day 16 — Course gate.** Run `booktool.py status`. Fix anything under 20,000 words with a new worked example or a new common-mistake section, not with padding. Run the style check. Then mark the course done in the progress table and do not touch it again until the whole book is finished.

One course every three weeks is a comfortable part-time pace: about two and a half years for all 48. One course a week is a realistic full-time pace.

---

## 9. Three honest schedules

| Schedule | People | Hours per week | Pace | Time to finish |
|---|---|---|---|---|
| **Part-time, one author** | 1 | 10 | one course per 3 weeks | about 2.5 years |
| **Full-time, one author** | 1 | 30–35 | one course per week | about 1 year |
| **Small team** | 4 authors + 1 editor | — | four courses in parallel, editor harmonises voice | 5–7 months |

If you use a helper or an AI assistant to produce first drafts, treat the output as **Pass 1 and 2 only**. You still own Passes 3–5. The rewrite pass is where the book becomes clear, and it is also where errors get caught. A machine can write 2,000 words of confident nonsense faster than you can read it, so never skip the truth check.

---

## 10. The four ways this book will try to go wrong — and the fix

**Drift.** Chapter 40 starts sounding like a different author. *Fix:* keep one short sample chapter (Course 1, Chapter 1) open beside you and match its rhythm.

**Repetition.** Four courses teach the same three ideas. *Fix:* the concept-homes rule, and a search before you write: `grep -ri "overfitting" book/courses`.

**Padding.** Word count is met with long introductions and restated definitions. *Fix:* the 20,000 words must come from examples, mistakes, case studies and labs. If you cannot name what you added, delete it.

**Front-matter creep.** You polish the preface for two weeks instead of writing Chapter 2. *Fix:* front matter is written last, in one day, from the finished chapters. It is already outlined here only so that you can stop worrying about it.

---

## 11. After the last chapter: assembling the book

1. **Run the gate on all 48 courses.** `python3 tools/booktool.py status` must show 48/48 PASS.
2. **Build the single file.** `python3 tools/booktool.py build` writes `book/Artificial-Intelligence-and-Robotics.md`.
3. **Harvest the glossary.** Collect every bolded key word with its definition into the master glossary. If a term is defined twice with different wording, unify it.
4. **Harvest the labs.** One index of every mini-lab, sorted by course, so a teacher can find practical work quickly.
5. **Write the answers.** The check-yourself questions already exist inside each chapter; the answers go in the back matter.
6. **Cross-reference pass.** Add "see Course 22, Chapter 6" wherever the reader needs it.
7. **Professional edit.** One editor reads the whole book for voice and repetition. This is not optional for a 960,000-word work.
8. **Production.** Convert Markdown to your chosen formats (DOCX, PDF, EPUB). Keep the Markdown as the master copy.

---

## 12. Start today: the next 90 minutes

1. Open `book/01-table-of-contents.md` and read Course 1 slowly (10 min).
2. Copy the seven-part recipe into a new file (5 min).
3. Fill one chapter brief for Course 1, Chapter 1 (20 min).
4. Write the skeleton — seven headings, one sentence each (15 min).
5. Draft the explanation box only (30 min).
6. Read it aloud and fix three sentences (10 min).

You now have a working method and one chapter that exists. Do that 479 more times, and the book is finished. There is no other step.

---

## Progress tracker

Update this table as courses pass the gate. Copy it as often as you like; it is the only scoreboard that matters.

| Course | Title | Words | Status |
|---|---|---|---|
| 1 | Introduction to Artificial Intelligence | see `booktool.py status` | in progress (pilot) |
| 2 | Robotics Fundamentals | | |
| 3 | Machine Learning | | |
| … | | | |
| 48 | Capstone Design Project | | |
