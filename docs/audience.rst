===============
Target audience
===============

Who is the target audience of the UVVisPy package? Is it interesting for me?


UVVis spectroscopists aiming at reproducibility
===============================================

The UVVisPy package addresses every scientist working with UVVis data on a daily base. Usually, analysing these data is rather straight-forward and only few processing (and analysis) steps are performed, such as baseline correction (zeroth order) and scaling to a common maximum. However, the latter already often involves taking only part of the spectra into account in case of more than one absorption line.

Furthermore, full reproducibility from the raw data to the final publication-ready figure should be possible without any thinking involved. This is possible by relying on the functionality provided by the `ASpecD framework <https://www.aspecd.de/>`_.


Users focussing on science, not programming
===========================================

Scientists are trained to do science, and less so to program their analysis software themselves. Thanks to "recipe-driven data analysis", the UVVisPy package allows for focussing on the underlying science, with no programming skills needed.


Motivation and general ideas
============================

The motivation an general idea behind the UVVisPy package is to ensure reproducibility and replicability for UVVis data processing, using the `ASpecD framework <https://www.aspecd.de/>`_.

Furthermore, version 0.1.0 served as demonstration that completely implementing a comparably simple package as UVVisPy from scratch based on the ASpecD framework can be done within about 48 hours.
