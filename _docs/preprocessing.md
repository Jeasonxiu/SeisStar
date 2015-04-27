---
layout: docs
title: Pre-processing
permalink: /docs/preprocessing/
---

# Pre-processing

We define 'pre-processing' quite broadly as 'operations on seismic traces carried out before the adjoint simulation.' Such operations may include
- `Basic signal processing`
- `Instrument response removal`
- `Bandpass filtering`
- `Window selection`
- `Measuring fit between observed and synthetic seismograms`
- `Generating adjoint sources`


#### Basic signal processing
In this category we include simple operations such as demeaning, detrending, and tapering.

```
from obspy import read
st = read("/path/to/your/data")
st.detrend("linear")
st.detrend("demean")
st.taper(max_percentage=0.05, type="hann")
```
[include figures]

#### Instrument response removal
Seismic data are often provided as raw output from a seismometer.  In such cases, the response of the instrument must be removed before the data can be used in any meaningful way.

```
from obspy import read
st = read("/path/to/your/data")
st.remove_response(output="DISP", pre_filt=pre_filt, zero_mean=False, taper=False)
st.detrend("linear")
st.detrend("demean")
st.taper(max_percentage=0.05, type="hann")
st.interpolate(sampling_rate=sampling_rate, starttime=starttime, npts=npts)
```


#### Bandpass filtering
Seismic data are usuable only within a frequency range that depends on the characterics of the instrument, of the source, and of the noise.  Careful selection of bandpass corners is crucial to avoid problems.  

A deliberate strategy of moving from low frequencies to high frequencies over the course of an inversion can be used to ensure that updated models remain in the basis of convergence of the global miminum of the objective function.

[include code and figures]


#### Window selection
In regional and global inversion, comparison of observations and synthetics within carefully selected windows can be used to allow seismologists' expertise with classical body wave and surface wave phases to be brought to bear in the waveform inversion framework.  In this approach, window selection is made on the basis of fit between observations and synthetics, with windows chosen only where the fit is good.  In our approach, relatively few windows are chosen at the beginning.  As the inversion progresses and data fit improves, more and more are added so that eventually the whole waveform is included. 

Outside of regional and global inversion, record sections may be more complex, window selection may be less stable, and other strategies for mitigating nonlinearity and nonconvexity may be preferred.


[include text, code, and figures]


#### Measuring fit between observed and synthetic seismograms
[include text, code, and figures]


#### Generating adjoint sources
[include text, code, and figures]

