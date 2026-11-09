# The Chain Around the Model

A paint shop in an automotive plant installs a vision system to find scratches on door panels. The model is excellent. In testing it finds 97% of scratches longer than two millimetres, and it raises false alarms on fewer than two panels in a thousand. The team is proud of it, and rightly; the work took a year.

Six months after launch, the line manager asks for it to be switched off. The camera housing had slowly filled with paint mist. The lighting had been replaced with a slightly cooler tube. One panel in five was now being flagged, operators had learned to override the alarm without looking, and the system had become a button that people pressed to make a noise stop.

Nothing in that story is a failure of the model. The model did exactly what it was trained to do, on inputs that had drifted away from the ones it knew. Everything that failed was outside the model, in the chain that connects a mathematical object to a factory.

## Six Links

A working system is a chain, and the model is one link in it.

**The problem.** Not “use AI to improve quality” but “find scratches longer than 2 mm on the painted surface of panel type X, at the end of the paint line, and raise an alarm within 200 ms”. The second sentence contains an object, a defect definition, a location, a deadline and an implicit benchmark: a human inspector. The first contains a wish.

**The sensing.** A camera on a bracket that vibrates, under a lamp that ages. The model was trained on images from a fixed rig in a laboratory. If the production camera sits two centimetres further away, every scale in the image changes and the model is looking at a different problem.

**The pre-processing.** Cropping, resizing, colour correction, normalisation. Every step must be identical at training time and at run time. A resize that interpolates differently in the two pipelines is enough to move accuracy by several points, silently.

**The inference.** How long does a prediction take, on the actual hardware, with the actual batch size? A model that runs in 40 ms on a workstation with a graphics card may take 300 ms on the industrial PC in the cabinet. If the requirement is 200 ms, the model is not deployable, whatever its accuracy.

**The decision.** The model outputs a number. Something must turn it into an action. That something is a threshold, and the threshold should come from the cost of the two kinds of mistake, as the previous chapters argued. A threshold chosen to maximise accuracy on a balanced test set is almost never the right threshold for a line where defects are one in a thousand.

**The feedback.** When the system is wrong, who finds out, and how does the information get back? An operator with no way to report a miss is an operator who will eventually stop caring.

| Link | Typical failure | Cheap check |
|---|---|---|
| Problem | Requirement unmeasurable | Ask the line manager to sign the measure |
| Sensing | Light, dust, vibration, ageing | Photograph a reference part every hour |
| Pre-processing | Train/run mismatch | Log the exact input array the model receives |
| Inference | Too slow on target hardware | Time a thousand predictions on the real machine |
| Decision | Threshold set for accuracy, not cost | Recompute the threshold from the cost ratio |
| Feedback | No route for corrections | One button, counted weekly |

## A Budget Measured in Milliseconds

Latency is the part of system design that students underestimate most often, because it is invisible in a notebook and brutal in a factory.

Take the paint line. Panels pass the camera at one every two seconds. The alarm must be raised before the panel reaches the next station, 200 ms after the image is captured. Inside that budget, the pipeline has to do several things in sequence:

- capture and transfer the image: 8 ms
- crop, resize and normalise: 25 ms
- run the model: 120 ms
- compare with the threshold, log and trigger: 5 ms

That totals 158 ms, leaving 42 ms of headroom for the operating system, the network and the occasional slow frame. The headroom is not waste. It is the difference between a system that meets its deadline on a good day and one that meets it always.

Now change one number. Suppose the model took 180 ms instead of 120. The total is 218 ms, and the system fails its requirement by 18 ms. The most common response at this point is to buy a faster computer. The better response is to ask which stage can be removed: a smaller input resolution, a lighter model, or a region of interest that excludes the parts of the panel where scratches cannot occur. Engineers call this reducing the work, and it is usually cheaper and more reliable than reducing the time.

The same arithmetic appears in every robot. A control loop running at 1 kHz has one millisecond for everything it does. A drone stabilising itself has less. When you read a paper that reports excellent accuracy, look for the inference time on embedded hardware. If it is absent, the result may be true and unusable.

## The Alert Nobody Read

Hospitals have been a hard testing ground for these systems, and one case is worth knowing because it involves no robot at all.

A widely used commercial system predicts which hospitalised patients are developing sepsis, a fast-moving and often fatal reaction to infection. In 2021, researchers outside the company evaluated it on patients at a single academic medical centre. The system identified about a third of the patients who went on to develop sepsis, and it raised alerts on roughly one in five of all hospitalised patients. Its measured discrimination was substantially below what the vendor's materials had suggested.

Two failures compounded. The statistical one is that a model developed and validated on one population did not transfer cleanly to another. The human one is that an alert firing on a fifth of all patients is not an alert. It is background noise, and clinicians did what people do with background noise: they stopped hearing it.

The lesson generalises to every interface in this book. A prediction is not a decision, and a decision is not an action. Between the model and the outcome sit attention, trust, timing and workload. A system that ignores those has built an accurate component and no working product.

## Who Owns It After Launch

Every deployed system needs three things that are not in the model: an owner, a review date and a retirement plan.

The **owner** is a named person, not a team, who is responsible for the system's behaviour this quarter. Without a name, maintenance becomes nobody's job, and the paint-mist problem goes unfixed for six months.

The **review date** is a calendar entry to re-measure performance on freshly labelled data. It is the only defence against drift, because drift is invisible from inside the model.

The **retirement plan** is the admission that the system will one day be wrong in a way that cannot be fixed. Products change, regulations change, cameras age, suppliers change. A system with no retirement plan is eventually switched off in a hurry by someone who has lost patience, which is exactly what happened in the paint shop.

None of these three is intellectually difficult. All three are routinely omitted, because they belong to nobody's research agenda and everybody's operational reality. The organisations that get this right treat an AI system like any other piece of production equipment: installed, maintained, inspected, and eventually replaced.

## Exercises

1. Write the one-page framing for a system that would inspect something you can see in your own environment — a wall, a page, a piece of fruit. Include the object, the defect, the sensor, the time limit, the error budget and the person who signs off.

2. Draw the six links for your system and write the biggest failure risk for each. Then write the cheapest check that would catch that failure.

3. Build a latency budget for a camera at 25 frames per second with a 400 ms alarm deadline. Allocate times to capture, pre-processing, inference and decision, and show your headroom.

4. In the sepsis case, the model identified about a third of cases and alerted on a fifth of patients. Using the definitions from the previous chapters, compute precision and recall as far as the numbers allow, state what is missing, and explain why clinicians ignored the alerts.

5. Think of a system in your school, workplace or home that was installed and then forgotten. Identify the drift that made it useless, and the review date that would have caught it.
