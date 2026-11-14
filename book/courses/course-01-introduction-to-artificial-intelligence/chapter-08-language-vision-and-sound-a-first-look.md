# Language, Vision and Sound: A First Look

> Course 1: Introduction to Artificial Intelligence - Chapter 8 of 10

## Opening

By the end of this chapter you can explain in plain terms how machines handle pictures, speech and text, and why the same three ideas keep appearing in all three.

Show a photograph to a person and they see a kitchen: a kettle, a mug, a window, light from the left. A computer receives a grid of numbers, each number saying how bright one tiny square is. Nothing in those numbers says "kettle". Turning numbers into meaning is the task of vision. Speech is a wave that must become letters, and text is a sequence of symbols with grammar and ambiguity. Three different inputs, three different problems, and yet the same methods keep working. Seeing that pattern early will save you years.

## Big Picture

All three problems begin the same way: raw input becomes numbers, numbers become **features** — small, useful summaries such as edges, pitch patterns or word frequencies — and features become decisions. The older approach had engineers design the features by hand. The modern approach learns them from data, which is what deep learning does.

The second shared idea is **context**. A word means something different depending on its neighbours. A pixel means something different depending on the pixels around it. A sound means something different depending on the sounds before it. Every modern advance in vision, speech and language has come from handling context better. When you meet a new architecture in Course 22, ask what context it is capturing.

## Key Words

- **Pixel** - one tiny square of an image, holding brightness or colour.
- **Feature** - a small summary of the raw data that is useful for a decision.
- **Token** - a small unit of text, usually a word or part of a word.
- **Embedding** - a list of numbers that represents a word or token.
- **Waveform** - the shape of a sound signal over time.
- **Spectrogram** - a picture of sound showing which frequencies are present at each moment.
- **Context** - the surrounding data that changes the meaning of the current piece.

## The Explanation

### Step 1 - Vision: from brightness to meaning

An image is a grid of pixels. A small grey image might be 640 × 480 = 307,200 pixels. Each pixel holds a number from 0 to 255, where 0 is black and 255 is white. A colour image has three such grids, one each for red, green and blue.

The first useful feature is an **edge**: a place where brightness changes sharply. You can find edges with a simple operation that compares each pixel with its neighbours. Edge detection is old, reliable, and still the first step in industrial vision systems that measure a part to a hundredth of a millimetre.

The second step is to group edges into shapes, and the third is to name the shapes. Older systems did this with hand-written rules: if there are two vertical edges 0.2 m apart and a horizontal edge on top, call it a door. That works until the door is open, or the light changes, or the wall is the same colour as the door.

Modern systems learn the grouping. A **convolutional network** (Course 11) learns which combinations of edges matter, starting with edges, then corners and textures, then parts of objects, then whole objects. The remarkable thing is that nobody writes those stages down. They emerge from examples.

The numbers here matter. A 640 × 480 colour image holds about 921,600 numbers. A single decision — "is there a person here?" — must compress that into one number. That compression is why features exist, and why a badly chosen feature makes the problem impossible no matter how clever the classifier.

### Step 2 - Sound: from pressure to words

A microphone measures air pressure many thousands of times a second. At 16,000 samples per second, one second of speech is 16,000 numbers. That is not a useful starting point, because the same word said louder or slower produces completely different numbers.

The trick is to look at frequency. A **spectrogram** breaks the sound into short slices — say 25 ms each, with a 10 ms step — and records how much energy is present at each frequency in each slice. One second of speech becomes about 100 slices of, say, 128 frequency values: a 100 × 128 picture of the sound. Speech recognition then becomes image recognition, and the methods described above apply.

This is why speech systems improved so much when deep learning arrived. The problem was never really about sound; it was about recognising patterns in a picture of sound once you had made the picture.

The same numbers give you an intuition for cost. Processing audio at 16 kHz means 16,000 samples per second, times 2 bytes, times 3600 seconds: about 115 MB for one hour of raw audio. A spectrogram of the same hour is much smaller, which is one reason edge devices compute it first.

### Step 3 - Language: from tokens to meaning

Text is a sequence of characters, which become **tokens**. A token is often a word or part of a word: "robotics" might become "robot" + "ics". A typical English sentence of 20 words might become 25 tokens.

Each token is mapped to an **embedding**: a list of numbers, usually a few hundred long, chosen so that words used in similar ways end up close together. "Torque" and "force" end up nearer each other than "torque" and "banana". Nobody assigns these positions by hand; they are learned from enormous amounts of text.

Then comes context, and this is where language is hardest. Consider these three uses of one word:

- "The bank raised its interest rate."
- "We sat on the bank of the river."
- "Bank left at the next junction."

A system that gives each word one fixed meaning must fail on at least two of these. A system that reads the whole sentence can tell them apart. Modern language models do this by letting each token look at the other tokens around it and adjust its representation, a mechanism called **attention**. That single idea, published in 2017, is the basis of the systems people now call "AI".

## Where It Goes Wrong

**Mistake 1 - Forgetting how much data a pixel or a sample is.** Students underestimate storage and compute by orders of magnitude and then wonder why the robot's processor melts. *Fix:* compute the numbers before choosing hardware.

**Mistake 2 - Treating one modality as ground truth.** A language model can describe a scene it has never seen; a camera cannot read a label on a box behind a shelf. *Fix:* combine modalities, and say which one is authoritative for which claim.

**Mistake 3 - Confusing fluency with understanding.** A model that writes confident prose may still be wrong about the world. *Fix:* test on facts, not on style.

**Mistake 4 - Training on one accent, one lighting condition, one writing style.** Performance collapses on everyone else. *Fix:* collect data that looks like the real users, including the awkward cases.

**Mistake 5 - Ignoring latency.** A vision model that takes 500 ms per frame cannot control a robot arm moving at 1 m/s. *Fix:* measure the full pipeline, from sensor to decision.

## Case Note

In 2018, a team of researchers showed that small changes to a few pixels could make an image classifier give a completely wrong answer with high confidence. The changes were invisible to people: the picture still looked like a panda to you, while the network saw a gibberish pattern and said "gibbon" with 99% confidence.

The lesson is not that vision does not work. Vision works extremely well on the data it was trained on. The lesson is that a network's confidence is a number produced by arithmetic, not a report on reality. There is no guarantee that the features it learned are the features you had in mind.

This is why serious systems combine a learned model with a check that does not share its weaknesses: a second sensor, a rule that refuses impossible outputs, or a human in the loop for high-stakes decisions. When you build a vision or language system, write down what could fool it. Then design the check before the failure happens.

## Mini-Lab

**You need:** a phone with a camera, or any image editor, and paper.

**Do this:**
1. Take a photo of a simple object on a plain background. Open it in any editor and zoom until you can see individual pixels.
2. Find an edge. Write down the approximate brightness of the pixels on each side — for example, 60 on the left and 180 on the right.
3. Estimate the size of the image in pixels: width × height × 3 for colour. Write the total.
4. Now cover the object with a cloth and repeat. Ask: which features changed, and which stayed the same?
5. In one sentence each, write what a rule-based system and a learned system would each get right and wrong on this pair of images.

**What you should see:** the edge numbers differ by a large jump, which is why edges are easy to find. The cloth changes almost everything, which is why hand-written rules are brittle.

**Why it matters:** you have connected a photograph to the numbers a network actually sees, which is the first step towards building one.

## Recap and Questions

**Three things to remember**

1. Images, sound and text all become numbers, then features, then decisions.
2. Sound is turned into a picture (a spectrogram) so that audio tools and vision tools become the same tools.
3. Context is what separates meaning from symbols, and attention is how modern systems handle it.

**Check yourself**

1. Why is a spectrogram more useful than raw audio samples for recognising a word?
2. A 1920 × 1080 colour image has how many numbers? Why does that matter for a robot with 512 MB of memory?
3. Give one task where a camera is better evidence than text, and one where text is better.

**One thing to try next**

Record yourself saying the same sentence loudly and softly, then look at the waveform in any free audio editor. The shapes will be different in height and similar in pattern. That difference is exactly why systems work on frequency, not amplitude.
