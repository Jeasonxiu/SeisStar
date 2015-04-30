---
layout: docs
title: Pre-processing
permalink: /docs/preprocessing/
---

# Pre-processing

We define 'pre-processing' quite broadly as 'operations on seismic traces carried out before the adjoint simulation.' Such operations may include
- `Initial processing`
- `Instrument response removal`
- `Bandpass filtering`
- `Window selection`
- `Measuring fit between observed and synthetic seismograms`
- `Generating adjoint sources`


#### Initial processing
In this category we include simple operations such as demeaning, detrending, and tapering, which are typically carried out prior to any other operations.

[click to show sample code]()
[click to show sample figures]()


#### Instrument response removal
Seismic data are often provided as raw output from a seismometer.  In such cases, the response of the instrument must be removed before the data can be used in any meaningful way.

[click to show sample code]()
[click to show sample figures]()



#### Bandpass filtering
Seismic data are usuable only within a frequency range that depends on the characterics of the instrument, of the source, and of the noise.  Careful selection of bandpass corners is crucial to avoid problems.  

A deliberate strategy of moving from low frequencies to high frequencies over the course of an inversion can be used to ensure that updated models remain in the basis of convergence of the global miminum of the objective function.

[click to show sample code]()
[click to show sample figures]()


#### Window selection
In regional and global inversion, comparison of observations and synthetics within carefully selected windows can be used to allow seismologists' expertise with classical body wave and surface wave phases to be brought to bear in the waveform inversion framework.  In this approach, window selection is made on the basis of fit between observations and synthetics, with windows chosen only where the fit is good.  In our approach, relatively few windows are chosen at the beginning.  As the inversion progresses and data fit improves, more and more are added so that eventually the whole waveform is included. 

Outside of regional and global inversion, record sections may be more complex, window selection may be less stable, and other strategies for mitigating nonlinearity and nonconvexity may be preferred.

[click to show sample code]()
[click to show sample figures]()



#### Measuring fit between observed and synthetic seismograms
[include text, code, and figures]

[click to show sample code]()
[click to show sample figures]()



#### Generating adjoint sources
[include text, code, and figures]

[click to show sample code]()
[click to show sample figures]()


