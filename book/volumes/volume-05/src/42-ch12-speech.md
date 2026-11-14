# Speech: Sound Into Words

A hands-free control station in a workshop accepted voice commands: "start cycle", "stop", "next programme". It worked for a month. Then the fitters started listening to the radio, and the station began stopping the machine at unpredictable intervals, because a chorus in the background contained something that sounded like "stop".

The fix was not a better speech recogniser. It was a wake word combined with a confirmation for destructive commands, and a microphone that rejected sound arriving from the direction of the radio. Both are engineering, and both were cheaper than any model change.

Speech is the fastest of the language interfaces and the most exposed to the physical world. This chapter covers the arithmetic of sound, the standard pipeline, and the measurements that predict whether a voice interface will be usable.

## Sound as Numbers

A microphone converts pressure to voltage, and an analogue-to-digital converter samples that voltage at a fixed rate.

Standard telephone-grade speech is sampled at 8,000 samples per second; wideband speech at 16,000. Each sample is usually quantised to 16 bits, two bytes.

> 16,000 samples/s × 2 bytes = 32,000 bytes/s = 32 kB/s

Ten seconds of speech is 320 kB, and an hour is 115 MB. That number explains why speech systems compress, transmit features rather than audio, and why a call centre recording everything is a storage project as much as an AI project.

The sampling rate sets the frequency range. The Nyquist limit says you can represent frequencies up to half the sampling rate, so 16 kHz audio carries information up to 8 kHz — enough for the consonants that distinguish "s" from "f", which telephone audio at 4 kHz often loses. That loss is why spelling a name over a landline is hard for people too.

## From Waveform to Picture

Recognisers do not consume raw samples. They consume a time-frequency representation, computed in short overlapping windows.

A typical setting: a 25-millisecond window, advanced by 10 milliseconds, gives one hundred frames per second. Within each frame, the spectrum is summarised into 128 mel-spaced frequency bands — spaced to match human hearing rather than physics.

> 128 bands × 100 frames/s = 12,800 numbers per second

So one second of audio, which was 32,000 bytes, becomes 12,800 features. A ten-second utterance is 128,000 values, which is why speech models are small compared with text models and why audio context windows are short.

The mel scaling and the logarithmic compression exist for the same reason: human hearing is more sensitive to differences at low frequencies, and loudness is perceived logarithmically. A recogniser that ignored both would be solving a harder problem than necessary.

## The Classical Pipeline, Still Instructive

Speech recognition was assembled from three components, and the division is worth knowing because the modern single model still does all three jobs.

**An acoustic model** maps features to sounds — historically phonemes, the small inventory of distinguishable units in a language. English has around forty.

**A lexicon** maps sounds to words. "Read" and "red" share sounds; "read" (past) and "read" (present) do not.

**A language model** supplies the prior probability of word sequences — the bigram and trigram models of Chapter Five, used exactly as described there, to break ties between acoustically similar candidates.

The interaction is why speech is hard: "recognise speech" and "wreck a nice beach" are acoustically close, and only the language model separates them. It is also why domain language models matter: a recogniser trained on general English has a weak prior for "torque wrench" and will prefer a phrase that sounds similar and occurs more often.

Modern systems replace the three components with one network trained end to end, which learns the acoustic mapping, the vocabulary and the prior together. The components have not disappeared; they have been absorbed.

## Measuring Recognition

The standard measure is the **word error rate**, computed from an alignment between the reference transcript and the system's output.

> WER = (substitutions + deletions + insertions) / number of reference words

Worked. A twenty-word reference, with three words misrecognised, one missing, and none inserted:

> WER = (3 + 1 + 0) / 20 = 0.20, or 20%

Two things about this number are commonly misunderstood.

It can exceed 100%. A system that inserts many spurious words has a WER above one, and reporting it as a percentage of accuracy is meaningless.

It is dominated by the errors you care about least. Function words are frequent and easy, so the headline WER can be 8% while every part number is wrong. For a command interface, the relevant measure is the **command error rate**: the fraction of utterances that result in the wrong action, which is a much smaller and much more honest number.

| Condition | Typical WER | Note |
|---|---|---|
| Close microphone, quiet room | 5–8% | The demonstration condition |
| Close microphone, workshop | 10–15% | Machines running |
| Far field, 3 m, reverberant | 20–30% | The real condition |
| With domain vocabulary mismatch | 30%+ | Names, codes, jargon |

The gap between the first and third rows is the whole reason voice interfaces disappoint. A system demonstrated at a desk is being evaluated in a condition that does not exist on a factory floor.

## Noise, Echo and the Physics of Failure

Four physical problems, in order of how often they break deployments.

**Background noise** reduces the signal-to-noise ratio, and the degradation is not graceful: below about 10 dB SNR, word error rises sharply. Directional microphones and close-talk headsets help more than any algorithm.

**Reverberation** smears each sound over hundreds of milliseconds in a hard room. The recogniser hears the previous syllable over the current one.

**Echo** from a loudspeaker means the system can hear itself, which is why barge-in — interrupting the system while it speaks — requires echo cancellation before anything else.

**Multiple talkers** produce overlapping speech that no current system separates reliably in a single channel.

None of these is fixed by a bigger model. All of them are addressed by microphone placement, acoustic treatment, and interface design — the same lesson as the previous volume's chapter on lighting.

## Where the Microphone Goes

Most speech projects are decided by a bracket rather than a model, and the arithmetic of placement is simple enough to do before anything is bought.

Sound intensity falls with the square of distance, so doubling the distance from a talker costs about six decibels of signal. In a workshop where the background is 70 dB and a talker at one metre produces 60 dB at the microphone, the signal-to-noise ratio is negative and no recogniser will work. Moving the microphone to thirty centimetres recovers about ten decibels, which is usually the difference between unusable and marginal.

Directivity matters as much as distance. A cardioid microphone rejects sound from behind by fifteen to twenty decibels, which is the difference between picking up the machine behind the operator and ignoring it. An array of microphones can do better by steering towards the talker, and its benefit is largest in the reverberant rooms where single microphones fail.

Three placement rules, learned expensively across the industry:

Keep the microphone out of the direct path of loudspeakers, and if the system speaks, cancel its own output before anything else.

Mount the microphone on the structure the talker is at, not on the wall behind. Vibrations and reflections both arrive from the wrong direction otherwise.

Measure the actual spectrum in the actual room. A "quiet" office has a fan; a "noisy" workshop has a band of frequencies that a directional microphone can reject.

The measurement to make is not word error rate in a laboratory, but the signal-to-noise ratio at the microphone during the noisiest shift. It takes a sound level meter and an hour, and it predicts the outcome of the project better than any demonstration.

## Speaking Back

Text-to-speech has its own arithmetic. The text must first be normalised: "3 May" read as a date, "1,200" as a number, "kg" as a unit, "Dr." as a title. Errors here are audible and embarrassing, and they come from the same ambiguity discussed in Chapter One.

Then prosody must be assigned — where the sentence stresses, where it pauses — because a synthesised sentence with flat intonation is harder to understand than a slightly mispronounced one with natural rhythm.

The measures that matter for an interface are not naturalness scores but comprehension: can a person follow the instruction while doing something else? A useful design rule is that any spoken instruction should be understandable at the first attempt, in noise, without repetition, or it should be redesigned to be shorter.

## Exercises

1. A 30-second recording at 16 kHz, 16-bit, mono: how many bytes? How many bytes if converted to 8 kHz?
2. Compute the WER for a reference of 40 words with 4 substitutions, 2 deletions and 3 insertions. Why might the system still be unusable?
3. Explain why 8 kHz audio loses information that distinguishes "s" from "f", using the Nyquist limit.
4. A voice interface must work at 2 m in a workshop. Name three changes you would make before considering a different model.
5. A command set has 40 commands. A system with 10% WER produces how many wrong actions per 1,000 commands if errors are random, and why is the real number usually different?
6. Design a confirmation policy for the commands "stop", "start" and "next". Which need confirmation, and why?
