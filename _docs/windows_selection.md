---
layout: docs
title: Windowing
permalink: /docs/windows_selection/
---

# Window Selection

Since 3D inversion is a highly non-linear problems, we then decrease the non-linearity by selecting windows on the seismograms. The basic idea here is to select windows inside which the observed data and synthetic data are not far off each other.

<center><img src="/SeisStar/img/window_selection_demo.png" alt="window selection" width="600"></center>
[*Figure Credit to Pyflex]

### Windows selection tools 
* [FLEXWIN](https://github.com/geodynamics/flexwin): original version of FLEXWIN
* [FLEXWIN_asdf](https://github.com/wjlei1990/seismo-FLEXWIN): FLEXWIN based on asdf IO
* [pyflex](https://github.com/krischer/pyflex): python export of FLEXWIN

