# Style Guide: Plain English Rules for This Book

The book teaches hard things. The language must therefore be the easiest part of the reader's day. These rules apply to every sentence in all 48 courses.

---

## The voice in one paragraph

Write as if you are sitting beside one student, explaining something you both care about, with a pencil and a piece of paper. You are patient, you are concrete, and you never show off. You use "you" and "we". You give the answer before the reader gets frustrated, but not before they have had a chance to think.

---

## The rules, with before and after

### 1. Short sentences

**Before:** "The utilisation of a proportional-integral-derivative controller is frequently necessitated in circumstances wherein a system exhibits persistent steady-state error under purely proportional control."

**After:** "A proportional controller often leaves a small error. The motor never quite reaches the target. Adding an integral term removes that error. This combination is called a **PID controller**."

Four sentences instead of one. Same content. The reader now has a place to stop and think.

### 2. One idea per paragraph

If a paragraph needs the word "also" three times, it is two paragraphs.

### 3. Define before use, once, in bold

First use: "The **torque** is the turning force on the shaft, measured in newton-metres (N·m)." After that, use the word freely. Do not define it again in the same course.

### 4. Concrete before abstract

**Before:** "Perception involves the mapping from sensor measurements to state estimates."

**After:** "Your phone knows it is upside down. It does this with one small sensor that measures direction. A robot does the same thing, at a larger scale: it turns measurements into beliefs about the world. That process is **perception**."

### 5. Active voice with a real subject

| Weak | Better |
|---|---|
| The error is reduced by the controller. | The controller reduces the error. |
| It can be seen that the wheel slips. | The wheel slips. |
| Measurements are taken every 10 ms. | The sensor takes a measurement every 10 ms. |

### 6. Numbers always carry units

Never "the value is 0.5". Always "0.5 m", "0.5 s", "0.5 V", "0.5 rad".

### 7. Worked examples use real numbers

Not "let *r* be the wheel radius", but "the wheel has radius 0.1 m, so one full turn moves the robot 2π × 0.1 = 0.63 m". The reader can check this on paper. That single habit does more for understanding than any diagram.

### 8. Prefer the short word

| Do not write | Write |
|---|---|
| utilize, utilise, leverage | use |
| in order to | to |
| prior to | before |
| subsequently | then |
| approximately | about |
| sufficient | enough |
| numerous | many |
| facilitate | help |
| demonstrate | show |
| commence, initiate | start |
| terminate | end |
| ascertain | find out |
| endeavour | try |
| a number of | some |
| in the event that | if |
| it should be noted that | (delete) |
| it is important to note that | (delete) |

### 9. No idioms, no sport, no local slang

Many readers will be reading English as a second or third language. "Ballpark figure", "hit the ground running" and "piece of cake" all cost a reader time. Say what you mean.

### 10. Explain every symbol the first time it appears

"Let *d* be the distance in metres." Not "let *d* be the distance" and not a symbol with no words at all.

### 11. Do not stack three nouns

**Before:** "the robot arm joint angle sensor calibration procedure"

**After:** "the procedure for calibrating the angle sensor on the robot joint"

### 12. When a sentence is hard, ask why

If you cannot shorten a sentence, usually one of three things is happening: you do not yet understand the idea well enough, you are hiding a missing step, or you are trying to say two things at once. Fix that, and the sentence fixes itself.

---

## The eight-part chapter shape

Every chapter uses these headings, spelled exactly like this:

```
## Opening
## Big Picture
## Key Words
## The Explanation
### Step 1 - ...
### Step 2 - ...
### Step 3 - ...
## Where It Goes Wrong
## Case Note
## Mini-Lab
## Recap and Questions
```

The opening always contains the sentence "By the end of this chapter you can ...". The recap always contains three things to remember, three questions, and one thing to try next. The Case Note is a true, checkable story, and it always ends by naming the lesson for the reader's own work.

---

## Formatting conventions

- **Bold** a term the first time it is defined. Only then.
- Use `code style` for code, file names, commands and variable names.
- Tables are for comparisons of three or more things. Two things are a sentence.
- Every figure is described in words as well, so the book works as plain text and for screen readers.
- Keep lists to five items or fewer. Longer lists belong in a table.
- Headings never end in a full stop. Sentences always do.

---

## A final test for every page

Hand the page to someone who has not read the previous chapter. Ask them to read it once, then close it and tell you the main idea. If they cannot, the page is not finished yet. That is the only test that matters.
