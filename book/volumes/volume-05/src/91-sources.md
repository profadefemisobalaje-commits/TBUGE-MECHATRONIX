# Sources and Further Reading

The classical material in this volume is stable and well documented; the later chapters describe methods that are changing while this book is being read. The list separates the two.

**Jurafsky, D. and Martin, J. H., *Speech and Language Processing*, third edition draft.** The standard text, free online, and unusually good at explaining why a method exists before explaining how it works. Chapters on n-grams, smoothing, vector semantics and machine translation correspond directly to Parts One and Two of this volume.

**Manning, C. D., Raghavan, P. and Schütze, H., *Introduction to Information Retrieval*, Cambridge University Press, 2008.** Free online. The definitive account of inverted indexes, tf-idf and evaluation. Chapter Eight's treatment of BM25 remains the clearest.

**Firth, J. R., "A Synopsis of Linguistic Theory, 1930–1955", in *Studies in Linguistic Analysis*, 1957.** The origin of the distributional slogan, in a paper that repays reading for its caution as much as its claim.

**Mikolov, T., Sutskever, I., Chen, K., Corrado, G. and Dean, J., "Distributed Representations of Words and Phrases and their Compositionality", *NeurIPS*, 2013.** The word2vec papers, short and readable, and the source of the analogy demonstrations that were later over-interpreted.

**Koehn, P., *Statistical Machine Translation*, Cambridge University Press, 2010.** Out of date as a description of current systems and still the best explanation of alignment, phrase extraction and why translation is hard.

**Papineni, K., Roukos, S., Ward, T. and Zhu, W.-J., "BLEU: a Method for Automatic Evaluation of Machine Translation", *ACL*, 2002.** Read the paper, not the leaderboards. The authors were explicit about what the measure does not capture.

**Chen, S. F. and Goodman, J., "An Empirical Study of Smoothing Techniques for Language Modeling", *Computer Speech and Language*, 1999.** A careful comparison, and the reason Kneser-Ney is still the reference point.

**Goodfellow, I., Bengio, Y. and Courville, A., *Deep Learning*, MIT Press, 2016.** Chapters 10 and 12 cover sequence models and applications. Free online.

**Rabiner, L. and Juang, B.-H., *Fundamentals of Speech Recognition*, Prentice Hall, 1993.** Old, and the clearest treatment of the acoustic model, lexicon and language model division that modern systems absorbed.

**Bird, S., Klein, E. and Loper, E., *Natural Language Processing with Python*, O'Reilly, 2009.** Free online, dated in its APIs, and still the most practical introduction to counting things in a corpus.

**Gebru, T. et al., "Datasheets for Datasets", *Communications of the ACM*, 2021**, and **Mitchell, M. et al., "Model Cards for Model Reporting", *FAT\**, 2019.** Two short papers that formalise the documentation this volume's final chapter argues for.

**NIST, *The Text REtrieval Conference (TREC) guidelines*.** If you need to build an evaluation set for retrieval, read how TREC has done it for thirty years; the pooling method and the labelling discipline are worth copying.

On the practical side, the documentation of the libraries you use is more useful than most papers. Read the tokeniser documentation carefully: it will tell you how unknown words are handled, how whitespace is treated, and how many tokens your text will actually become — three facts that determine cost, accuracy and comparability, and three facts that are almost never written down in project notes.
