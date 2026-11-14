# Sources and Further Reading

The methods in this volume are old, well documented, and mostly public. What follows is a short list of the works worth owning, with a note on what each is good for.

**Ballard, D. H. and Brown, C. M., *Computer Vision*, Prentice Hall, 1982.** Out of print and still the clearest account of the geometric view of vision. Chapters on perspective, stereo and calibration remain unsurpassed for a reader who wants the reasoning rather than a library call.

**Szeliski, R., *Computer Vision: Algorithms and Applications*, second edition, Springer, 2022.** The standard modern reference. Free to read online. Use it as a dictionary: it will tell you what a method is called and where the literature goes next.

**Hartley, R. and Zisserman, A., *Multiple View Geometry in Computer Vision*, second edition, Cambridge University Press, 2004.** The definitive treatment of calibration, homographies and reconstruction. Dense, and worth the effort if your work involves three-dimensional measurement.

**Gonzalez, R. C. and Woods, R. E., *Digital Image Processing*, fourth edition, Pearson, 2018.** The textbook for filtering, morphology and segmentation, with the arithmetic worked out. The chapters on spatial filtering pair naturally with Chapter Three here.

**Nixon, M. and Aguado, A., *Feature Extraction and Image Processing for Computer Vision*, fourth edition, Academic Press, 2019.** Practical, engineering-minded, and unusually good on the details that textbooks skip.

**Horn, B. K. P., *Robot Vision*, MIT Press, 1986.** A short, opinionated book on light, reflectance and the physics of image formation. It explains why the lighting chapters of any vision project are the ones that matter.

**Goodfellow, I., Bengio, Y. and Courville, A., *Deep Learning*, MIT Press, 2016.** Chapters 9 and 10 cover convolutional networks from first principles. Free online, and still the most careful explanation of what a convolution layer is doing.

**Russ, J. C., *The Image Processing Handbook*, seventh edition, CRC Press, 2016.** A reference of techniques with pictures. Useful when a specific operation needs a name.

**ASTM E2862 and ISO 5725** for measurement capability and repeatability in industrial settings. Dry documents, and the reason a capability figure can be defended in an argument with a customer.

On the engineering of lighting, the technical notes published by the major illumination manufacturers — Microscan, CCS, Advanced Illumination, and Keyence among them — contain more practical geometry than most textbooks, and they are free.

Two journals are worth scanning for the state of the field: *IEEE Transactions on Pattern Analysis and Machine Intelligence*, and *Journal of Real-Time Image Processing*. Neither will teach a beginner, and both will show where the subject is moving.

Finally, the documentation of the libraries you use. OpenCV's tutorials are uneven and its reference is exhaustive. Read the reference for the function you are calling at least once, particularly the parts about coordinate conventions, and you will avoid the class of error that Chapter Two describes.
