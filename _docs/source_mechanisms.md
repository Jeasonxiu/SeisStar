---
layout: docs
title: Earthquake source mechanisms
permalink: /docs/source_mechanisms/
---

# Earthquake source mechanisms

Accurate earthquake source mechanisms are an important prerequisite for regional or global tomography.  Even with a good source catalog, such as the [Global CMT](http://www.globalcmt.org/) catalog, it is still useful to perform the following quality control check.

Starting with Global CMT solutions, we solve a least squares problem to obtain updated source mechanisms.  In most cases, the difference between starting values and updated values is quite small.  Any large differences, however, require further investigation. 

The procedure can be further summarized as follows.



#### 1. Forward simulation
To obtain updated source mechanisms, we first compute partial derivatives of synthetic seismograms with respect to 6 moment tensor elements and 3 location parameters that comprise the Jacobian matrix.  Using forward centered finite differences, 9 forward simulations must be carried out per earthquake.


#### 2. Data processing
As with the gradient computation in Earth structure inversions, the Jacobian computation must be carried out using processed seismic traces.  Instrument response removal, bandpass filtering, and window selection are all required steps.


#### 3. Source mechanism inversion 
Once the Jacobian has been computed, it only remains to solve the corresponding linear system.  We use the machinery provided by Pycmt [link] for doing so.

