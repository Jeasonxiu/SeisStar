---
layout: docs
title: Preprocessing
permalink: /docs/solvers/
---

# Preprocessing packages

The preprocessing stage is done so that valid comparisons of the observed and synthetic seismograms can be made.
Both synthetic and observed seismograms must have the correct station/event and timing information.
Then the seismograms are cut using the same window, the instrument response is removed from the observed seismograms, the exact same filter is applied, and resampling is done to the observed and synthetic seismograms to a common sampling rate.

The figure below illustrates the preprocessing workflow for adjoint tomography.

### img test1
![Image of Preprocessing Workflow](https://github.com/SeisStar/SeisStar/blob/gh-pages/img/ASDF.png)

### img test2
![Image of Preprocessing Workflow](../img/ASDF.png)
### img test3
![Image of Preprocessing Workflow](/SeisStar/img/ASDF.png)