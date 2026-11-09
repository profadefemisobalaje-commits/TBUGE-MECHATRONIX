# Two Winters, Three Ideas

In the summer of 1956, a group of about ten men spent several weeks at Dartmouth College in New Hampshire, talking about whether machines could be made to think. The proposal that brought them there, written the year before by John McCarthy, Marvin Minsky, Nathaniel Rochester and Claude Shannon, contained a sentence that has been quoted ever since: that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.

It is worth pausing on how confident that sentence is. Not “some aspects”. Not “simple features”. Every aspect, in principle, and the authors expected a generation of work to settle it.

Seventy years later, the work is still going, and the argument about how far it has got is louder than ever. But the shape of that seventy years is not a straight line of progress. It is a loop, repeated three times, and knowing the loop is the best defence against both the hype and the despair that the subject produces in equal measure.

## The Paper That Started It

The technical foundation was laid in 1936, when Alan Turing, then twenty-four, published a paper describing an abstract machine that could compute anything computable by following a finite list of simple steps. The point was not to build such a machine. The point was to give a precise meaning to the words “a procedure that can be carried out mechanically”. Once you have that meaning, the question “can a machine think?” stops being poetry and becomes something you can argue about with evidence.

Fourteen years later, Turing wrote the paper that gave the field its founding experiment. Rather than defining thinking — a definition nobody could agree on — he replaced the question with a test. Put a person, a machine and a judge in separate rooms. Let the judge type questions to both. If the judge cannot reliably tell which is which, said Turing, we have no good reason to deny that the machine thinks.

The move is characteristic of the field at its best: when a question is too vague to answer, replace it with an experiment. It is also characteristic of the field at its worst, because a machine can pass the test by being good at conversation without understanding anything, which is more or less what happened seventy years later, and which is why the test is now a footnote rather than a goal.

## Machines That Followed Rules

The first generation believed that intelligence was the manipulation of symbols. If a doctor's knowledge could be written down as rules, a program could follow the rules and give advice. This produced genuine, useful systems.

MYCIN, built at Stanford in the 1970s, advised doctors on bacterial infections of the blood. It asked questions, weighed evidence, and recommended an antibiotic. In blind tests it performed about as well as human specialists. It had roughly six hundred rules, each argued over by clinicians, and it could explain its reasoning by listing the rules it had used. It was never used routinely in hospitals, for reasons that had nothing to do with accuracy: doctors did not want to type answers to long lists of questions while a patient waited, the system ran on specialised hardware, and nobody knew who would be legally responsible if the advice was wrong.

XCON, built at Carnegie Mellon for the Digital Equipment Corporation, configured orders for VAX computers. A customer order might specify dozens of components that had to fit together physically, electrically and in software; human specialists took hours and sometimes made expensive mistakes. XCON took minutes, and by the company's own estimate saved tens of millions of dollars a year. For a while it was the flagship of an entire industry. Then each new product line needed new rules, each rule interacted with rules written years earlier by engineers who had moved on, and the knowledge base grew into the thousands. Maintaining it became a specialist job in itself. The system never became wrong. It became too expensive to keep right, which in business is the same thing.

This pattern — real success, then a wall made of maintenance, cost and common sense — is the pattern of the first wave, and it is the reason the field's history is a loop rather than a line.

## The First Winter

The first collapse came earlier than most people realise. In 1969, Marvin Minsky and Seymour Papert published a careful mathematical analysis of the perceptron, a simple learning machine built by Frank Rosenblatt a decade earlier. Their book showed that a single-layer perceptron could not compute even the logical function “exclusive or”, a case where the answer is yes if either input is yes but not both. The result was narrow. It was read, unfairly but widely, as proof that learning machines were a dead end. Funding for neural network research collapsed.

In 1973, the British government commissioned a review of the field from Sir James Lighthill, a distinguished applied mathematician. His report was sceptical, and British funding was cut. In the United States, defence funding for open-ended AI research was reduced around the same period. The years from roughly 1974 to 1980 are usually called the first AI winter: not a period in which the ideas died, but one in which the money did.

The second winter came in the late 1980s, and again the cause was economic. Expert systems were running on special-purpose computers, and those machines were expensive. When ordinary desktop workstations became fast enough to run the same software, the hardware business collapsed almost overnight. Around 1987, the market for Lisp machines disappeared. The companies that had bet on it disappeared with it, and with them a great deal of the credibility of the expert-systems wave.

Two winters taught the field a lesson it has never quite forgotten: a method can be correct, elegant and still too expensive to survive. That lesson is why every chapter in this volume asks not only whether a method works, but what it costs to keep working.

## The Learning Turn

While the rule-based wave was freezing, a different idea was warming up. In 1986, a paper by David Rumelhart, Geoffrey Hinton and Ronald Williams in *Nature* popularised a practical method for training networks with more than one layer, called backpropagation. The technique had been discovered and rediscovered several times before, but 1986 was the moment it became usable and widely known. It removed the objection of 1969 at a stroke: networks could now learn things that a single layer could not represent.

The 1990s took a further step away from hand-written rules, towards statistics. Instead of asking an expert what the rules were, you collected data and estimated probabilities. This was less glamorous, far more reliable, and it worked in speech recognition, handwriting, credit scoring and machine vision. The field changed its vocabulary: fewer “knowledge bases”, more “training sets” and “error rates”.

In May 1997, in the middle of this turn, Deep Blue beat Kasparov. It is worth being precise about how: Deep Blue used special-purpose hardware to examine around two hundred million positions per second, plus an evaluation function tuned with the help of strong human players. It did not learn from data. It was the last great triumph of the search-and-rules tradition, arriving just as the statistical tradition was taking over.

## Scale Arrives

In 2009, researchers at Princeton and Stanford released ImageNet, a dataset that eventually contained more than fourteen million labelled photographs. The following years produced a competition to classify a thousand categories of object from images. In 2012, a deep network called AlexNet won that competition with an error rate of about 15%, against roughly 26% for the second-placed entry. It was trained on graphics processors built for video games.

The pattern was set: bigger networks, more data, more computing power. In 2016, AlphaGo beat Lee Sedol at Go, a game whose branching factor is so large that searching it was long considered hopeless, and it did so partly by learning an evaluation function from millions of games and then from games against itself. In 2017, a paper called “Attention Is All You Need” introduced the transformer, an architecture that processes sequences in parallel and handles context with a mechanism called attention. In November 2022, chat models built on transformers reached the public, and the argument about artificial intelligence moved from the technology pages to the family dinner table.

Notice what did not happen at any point in this story. The old ideas did not die. Chess engines still search. Rule systems still run factories, aircraft and payment systems. Learning sits on top of both. The history is not a series of replacements; it is a series of additions, each one surviving because it solved a problem the others could not.

| Period | Dominant idea | Characteristic success | Characteristic failure |
|---|---|---|---|
| 1956–1975 | Symbols and search | Puzzles, games, simple proofs | Real-world messiness |
| 1975–1987 | Expert rules | Medicine, configuration, planning | Cost, brittleness, common sense |
| 1987–2012 | Statistical learning | Speech, handwriting, recommendation | Needs labelled data |
| 2012–today | Deep learning at scale | Vision, language, games | Data hunger, opacity, expense |

## What the Loop Teaches

Three lessons follow from this history, and they are the reason it earns a chapter instead of a paragraph.

The first is that each wave was a response to the wall of the previous one. Rules failed because knowledge had to be written by hand; learning answered that. Learning failed because it needed features designed by hand; deep learning answered that. Deep learning is now meeting its own walls: data, energy, reliability and trust. The next wave will be an answer to one of those, and you can predict its shape by asking which wall it removes.

The second is that the winters were about money and maintenance, not about ideas being wrong. This matters to you personally. Most projects do not fail because the algorithm is false. They fail because the data cannot be collected, the system cannot be maintained, the integration takes longer than the research, or the organisation loses interest. Keep that in view when you plan your own work.

The third is that every wave renames itself. What was called cybernetics, then symbolic AI, then expert systems, then machine learning, then deep learning, then generative AI, is one continuous attempt to build machines that choose well. The names are useful for dating a conversation. They are not useful for deciding what is true.

## Exercises

1. Draw a horizontal line and mark it 1940, 1960, 1980, 2000, 2020. Place these on it: Turing's paper on computable numbers (1936), the Dartmouth workshop (1956), the perceptron (1958), the perceptron critique (1969), the Lighthill report (1973), MYCIN, XCON, the Lisp machine collapse (1987), backpropagation (1986), Deep Blue (1997), ImageNet (2009), AlexNet (2012), AlphaGo (2016), the transformer paper (2017), public chat models (2022). Above the line, write the dominant idea at each point. Below it, write the wall that idea ran into.

2. MYCIN matched human specialists and was never used. XCON saved millions and became unmaintainable. Write one paragraph on what these two outcomes have in common, and one on what they do not.

3. Find a news article about artificial intelligence from five years ago. Identify the wall that its predictions did not see coming. Then find one from this month and predict the wall it is not seeing. You will be wrong, but the exercise is the point.
