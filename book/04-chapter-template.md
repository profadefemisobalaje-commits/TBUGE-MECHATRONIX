# Chapter Template

Copy this file, rename it, and fill it in. Budgets are in words and add up to about 2,000.

---

## Skeleton (copy from here)

```
# <Chapter title>

> Course <n>: <course title> - Chapter <k> of 10

## Opening
<!-- 150 words. Goal sentence + hook. -->

By the end of this chapter you can <one clear ability>.

<hook>

## Big Picture
<!-- 250 words. The one idea. No formulas. -->

## Key Words
<!-- 200 words. 4-6 bolded terms with plain definitions. -->

- **Term** - meaning in everyday words, with a unit if it has one.

## The Explanation
<!-- 750 words. Three steps, easy to hard. Each step: comparison -> the real thing -> worked example with numbers. -->

### Step 1 - <plain name for the idea>

### Step 2 - <plain name for the idea>

### Step 3 - <plain name for the idea>

## Where It Goes Wrong
<!-- 200 words. 3-5 real mistakes + the fix for each. -->

**Mistake 1 - <name>.** <what happens>. *Fix:* <action>.

## Case Note
<!-- 210 words. One true story, with a source a reader could look up, ending in the lesson for the reader's own work. -->

## Mini-Lab
<!-- 200 words. 15-45 minutes, no shopping required. -->

**You need:** <laptop / phone / paper and pen>

**Do this:**
1.
2.
3.

**What you should see:**
...

**Why it matters:**
...

## Recap and Questions
<!-- 200 words. -->

**Three things to remember**

1.
2.
3.

**Check yourself**

1.
2.
3.

**One thing to try next**

...
```

---

## Filled example (this is what "good" looks like)

Below is a complete chapter written to the recipe. Notice the shape: ability first, one idea, definitions, three steps with real numbers, mistakes, a lab with no equipment, and a recap. Match this rhythm in every chapter and the book will feel like one voice for all 960,000 words.

---

# Measuring How Wrong a Model Is

> Course 3: Machine Learning - Chapter 3 of 10

## Opening

By the end of this chapter you can measure how wrong a prediction is, and say why the choice of measure changes what your model learns.

Suppose two weather apps both say "30 °C" for tomorrow. The real temperature turns out to be 33 °C. One app said 30, the other said 29. Both were wrong, but one was more wrong. Every machine learning model is in this position: it makes a guess, the world gives the true answer later, and we need a number that says how badly the guess missed. That number is the only thing the model uses to improve, so if you choose it badly, you teach the model the wrong lesson.

## Big Picture

A model learns by being punished for its mistakes. The punishment is a single number, the **loss**. Small loss means good model. The model adjusts itself to make that number smaller. Here is the important part: the shape of the punishment decides the shape of the model's behaviour. If you punish big misses very heavily, the model becomes careful and ignores odd data points. If you punish every miss equally, the model chases the average of everything, including the nonsense. So the loss function is not a detail you add at the end. It is a statement of what you think "good" means.

## Key Words

- **Prediction** - the model's guess, written ŷ and read "y-hat".
- **Target** - the true answer, written y.
- **Error** - prediction minus target, or target minus prediction. We square it, so the order does not matter.
- **Loss** - one number that scores the predictions on one example or a whole dataset. Smaller is better.
- **Mean squared error (MSE)** - the average of the squared errors. Strongly punishes large misses.
- **Mean absolute error (MAE)** - the average of the sizes of the errors, ignoring sign. Treats all misses in proportion.

## The Explanation

### Step 1 - Error, then square it

Start with one example. A robot arm predicts a reach of 0.52 m. The true distance is 0.50 m. The error is 0.02 m. If you just add errors up, a miss of +0.3 m cancels a miss of −0.3 m and you conclude the model is perfect. That is obviously wrong, so we remove the sign. Squaring does it: (0.02)² = 0.0004 m². Now negative and positive cannot cancel.

Squaring has a second effect, and it is the one that matters: it punishes big misses much harder than small ones. A miss of 0.1 m costs 0.01. A miss of 0.3 m costs 0.09 — nine times as much for three times the error. The model will work hard to avoid the big miss, sometimes at the cost of being mediocre everywhere else.

### Step 2 - Average over many examples

One example tells you almost nothing. Take the average over the whole dataset and you get the mean squared error:

MSE = (1/n) × sum of (ŷᵢ − yᵢ)²

With three predictions — errors of 0.02 m, 0.04 m and 0.10 m — the squares are 0.0004, 0.0016 and 0.01 m². They add to 0.012 m², and dividing by 3 gives an MSE of 0.004 m².

That number is hard to read, because it lives in square metres. So we usually take the square root and report the **root mean squared error**, 0.063 m. Now it is in metres again, and you can compare it with the thing you are measuring. A typical arm reach of half a metre with a 0.063 m error is roughly a 12% miss.

### Step 3 - Choose the loss that matches the job

Change the loss and the model changes its mind. Suppose the errors are 0.02 m, 0.04 m and 0.30 m — one wild outlier, perhaps a sensor glitch.

- Squared errors: 0.0004, 0.0016, 0.09. MSE = 0.0307 m², RMSE = 0.175 m. The outlier dominates everything.
- Absolute errors: 0.02, 0.04, 0.30. MAE = 0.12 m. The outlier matters, but it does not take over.

A model trained with MSE will bend itself towards the outlier, because that is where the punishment is. A model trained with MAE will ignore it more and fit the normal cases better. Neither is "correct". If the outlier is a faulty sensor, MAE is the better choice. If the outlier is a real event you must never miss — a person stepping in front of the robot — then you want the model to care, and MSE is the better choice.

That is the whole lesson of this chapter in one sentence: **the loss function is how you tell the model what you care about.**

## Where It Goes Wrong

**Mistake 1 - Forgetting the units.** Reporting an MSE of 0.004 and comparing it with an error of 0.02 m. *Fix:* report the root mean squared error whenever you want a number in the same units as the target.

**Mistake 2 - Using the test set to choose the loss.** Trying three losses and keeping the one that scores best on the test set. The test set is now part of training, and your score is a lie. *Fix:* choose the loss with a validation set, and touch the test set once, at the end.

**Mistake 3 - Chasing a low average and ignoring the tail.** An RMSE of 0.02 m sounds excellent until you learn the worst single error was 0.6 m. *Fix:* always report the average *and* the worst case, and look at a plot of the errors, not just one number.

**Mistake 4 - Mixing up error and loss.** Error is the difference for one example. Loss is the number the optimiser minimises, which may include extra terms such as a penalty on large weights. *Fix:* keep two words for two things; the book uses them that way throughout.

## Mini-Lab

**You need:** paper, a pen, a calculator or phone.

**Do this:**
1. Write five guesses for a robot's distance to a wall: 1.02, 0.97, 1.10, 0.95, 1.30 m. The true distance is 1.00 m.
2. Compute the five errors, then the five squared errors, then the MSE.
3. Take the square root to get the RMSE.
4. Repeat with absolute errors to get the MAE.
5. Now delete the 1.30 m case and compute both again.

**What you should see:** the MSE and RMSE drop sharply when the outlier goes, while the MAE barely changes. That gap is the difference between the two losses, measured by your own hand.

**Why it matters:** you have just felt why model choice is a statement of values, not just arithmetic.

## Recap and Questions

**Three things to remember**

1. A loss turns many errors into one number, and the model only ever sees that number.
2. Squaring punishes large errors far more than small ones, which makes the model careful about outliers.
3. Report error in units a human can read: RMSE for metres, MAE when outliers should not dominate.

**Check yourself**

1. Two models have the same MAE. Can they have different RMSE? Why?
2. You are predicting the temperature of a chemical bath that must never exceed 90 °C. Which loss do you pick, and why?
3. Why is an MSE of 0.004 m² not comparable with an error of 0.02 m?

**One thing to try next**

Take any prediction you already make in daily life — the time a journey will take, the cost of a shopping list — write down five guesses and the true values, and compute your own MAE. You will never again read "average error" the same way.
