# Pictures, Sounds, Words

Show a person a photograph of a kitchen and they see a kettle, a mug, a window, and light coming from the left. A computer receives a grid of numbers. Nothing in that grid says “kettle”. The distance from the grid to the word is the subject of vision.

Speech presents the same problem in a different costume: a microphone measures air pressure thousands of times a second, and somewhere in that measurement is a sentence. Text presents it a third time: a string of symbols whose meaning depends on the symbols around it.

Three different inputs, three different traditions of engineering, and one shared structure. All three turn raw numbers into features, features into decisions, and decisions into meaning that depends on context. This chapter is a tour of that structure, at the level of the ideas you would need before the deeper treatment in later volumes.

## Nine Hundred Thousand Numbers

An ordinary photograph is a grid of **pixels**. A modest one, 640 by 480, contains 307,200 pixels. In colour, each pixel holds three numbers — red, green and blue — each between 0 and 255. The whole picture is therefore 921,600 numbers.

A full high-definition frame is 1920 by 1080, which comes to just over two million pixels and 6.2 million numbers. A camera producing 30 of those per second generates 186 million numbers every second.

These figures explain a great deal of engineering. They are why a robot's processor heats up, why video compression exists, and why the first step in almost every vision system is to throw information away. A feature is, by definition, a small summary that keeps what matters and discards the rest.

The first useful feature in most systems is an **edge**: a place where brightness changes sharply. Find the pixels where the number jumps from 60 to 180 and you have found the side of a door, the rim of a cup, the boundary between a road and a kerb. Edge detection is one of the oldest operations in the field and still the first step in industrial systems that measure a machined part to a hundredth of a millimetre.

The second step is to group edges into shapes, and the third is to name the shapes. The old way was to write rules: two vertical edges 0.2 m apart with a horizontal edge on top is a door. That works until the door is open, or the light changes, or the wall is the same colour as the door.

## From Edges to Objects

The modern way is to learn the grouping from examples, and the trick that made it work is small enough to describe in a paragraph.

Instead of connecting every pixel to every other pixel, a **convolutional** network slides a small filter across the image, looking at a patch of a few pixels at a time. The filter is a tiny pattern detector: a vertical edge, a corner, a patch of texture. Early layers learn filters that respond to edges. The next layers combine those responses into corners and curves. Later layers combine those into parts of objects, and the last layers combine parts into objects.

Nobody writes down the stages. They emerge from examples, because the network is rewarded for producing the right label and free to invent whatever internal features help. That freedom is why the approach works so much better than hand-written rules, and it is also why the result is hard to explain: the features are whatever minimised the error, not whatever a person would have chosen.

It is worth keeping one number in mind, because it explains a lot of behaviour. A convolutional network's first layer might have 64 filters, each 3 by 3 pixels. That is 576 weights. Its final layer might have a million. The capacity to memorise lives in the later layers, and so does the tendency to overfit. When a vision model fails on a slightly different camera, the failure is usually in the layers that learned something too specific about the training photographs.

## A Picture of Sound

Sound is a pressure wave. A microphone samples it, typically 16,000 or 44,100 times per second. One second of speech at 16 kHz is 16,000 numbers, and those numbers change completely if the same word is said louder, or by a different person, or a little faster.

The representation that solves this is the **spectrogram**. Break the sound into short slices — 25 milliseconds is typical — and for each slice record how much energy is present at each frequency. With a 10-millisecond step you get about a hundred slices per second; with 128 frequency bands per slice you get a grid of roughly 100 by 128 numbers.

That grid is a picture. Time runs left to right, frequency runs bottom to top, and brightness shows energy. Vowels produce broad horizontal bands; consonants produce short bursts of noise; a rising pitch produces a rising line.

Once speech is a picture, the tools of vision apply, and this is precisely what happened. Speech recognition improved sharply when the field began treating spectrograms with the same machinery it used for images. The problem was never really about sound. It was about patterns, and the patterns became visible once the right picture was made.

There is a cost worth noticing. A spectrogram throws away phase, which is part of how the wave is shaped, and it blurs events shorter than its slice. For recognising words that is acceptable. For locating a click to the microsecond, it is not, and a different representation is needed.

## Words as Points

Text arrives as characters, and the first step is to cut it into **tokens**. A token is often a word, but not always: “robotics” might become “robot” and “ics”, because the second half appears in thousands of other words and the system can learn from that.

Each token is then mapped to an **embedding**: a list of numbers, a few hundred long, positioned so that words used in similar ways end up close together. Nobody assigns those positions by hand. They are learned from enormous quantities of text, and the geometry that results is surprisingly meaningful. The distance between “torque” and “force” is smaller than the distance between either and “banana”.

Embeddings solve one problem and create another. They give a word a position, but a single position cannot capture the fact that the same word means different things in different sentences:

> The bank raised its interest rate.
>
> We sat on the bank of the river.
>
> Bank left at the next junction.

A system that gives each word one fixed vector must fail on at least two of these. What it needs is a representation that depends on the neighbours, and the mechanism that provides it is called **attention**. Each token looks at the other tokens in the sentence, decides which ones matter for its meaning, and adjusts its representation accordingly. The paper that introduced the transformer architecture in 2017 was built on this idea, and the language systems that reached the public in 2022 are large descendants of it.

The word “attention” is doing a lot of work here, and it is worth being precise. It does not mean the system is paying attention in the human sense. It means that, for each position in the sequence, the network computes a weighted average of the other positions, with weights that depend on the content. It is arithmetic with a suggestive name, and the name has caused a decade of over-interpretation.

## Three Ways These Systems Fail

Systems that see, hear and read fail in ways that are specific, and knowing them in advance is most of the defence.

**They fail on the unfamiliar.** A vision system trained in daylight degrades at dusk. A speech system trained on one accent struggles with another. A language model trained before an event does not know the event happened. The failure is not random; it is concentrated in whatever the training data did not contain.

**They fail on adversarial input.** In 2018, researchers showed that changing a few pixels — invisible to a person — could make a classifier give a confidently wrong answer. The picture still looks like a panda, and the network says “gibbon” with 99% confidence, because it is responding to a pattern that people do not perceive. In the physical world, a small sticker on a road sign has been shown to confuse some driving systems.

**They fail fluently.** A language model that does not know something will often produce a confident, well-formed, wrong answer rather than admitting ignorance. The form of the answer is learned from text; the content is generated by what is statistically plausible. Fluency and truth are different properties, and only one of them is measured by how good the sentence sounds.

There is a common thread. These systems model the data they were trained on, and they have no independent access to the world. When the world differs from the data, or when the input is crafted to exploit a pattern the model has learned, the output can be confidently wrong. The engineering response is always the same: test outside the training distribution, add a check that does not share the model's weaknesses, and keep a human able to see what the system is doing and stop it.

## Things to Try

1. Compute the number of values in a 1280 by 720 colour image. Then compute how many arrive per second from a camera running at 25 frames per second. Compare with the capacity of an ordinary phone's storage and say what this implies for a robot recording video for an hour.

2. Take a photograph on your phone and open it in any editor that shows pixel values. Find an edge and write down the approximate values on each side. Explain, in two sentences, why an edge detector can find that boundary without knowing what the object is.

3. Record yourself saying a sentence twice: once normally, once in a whisper. Look at the waveform and, if you can, at a spectrogram. Which parts stay similar, and which change? Relate your answer to why speech systems use frequency rather than raw amplitude.

4. Write three sentences in which the word “spring” has three different meanings. Then explain what a system with one fixed vector per word would get wrong, and how attention would help.

5. Find a claim that a system “understands” images or language. Rewrite it as a testable claim about a specific dataset, a specific measure and a specific failure rate.
