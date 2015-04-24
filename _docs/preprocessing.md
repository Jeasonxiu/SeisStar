---
layout: docs
title: Preprocessing
permalink: /docs/preprocessing/
---

# Preprocessing packages

The preprocessing stage is done so that valid comparisons of the observed and synthetic seismograms can be made.
Both synthetic and observed seismograms must have the correct station/event and timing information.
Then the seismograms are cut using the same window, the instrument response is removed from the observed seismograms, the exact same filter is applied, and resampling is done to the observed and synthetic seismograms to a common sampling rate.

The figure below illustrates the preprocessing workflow for adjoint tomography.

![Image of Preprocessing Workflow](/SeisStar/img/ASDF.png)

Example
----------------
Here is the code example:

```python
from obspy import read
st = read("/path/to/your/data")
st.detrend("linear")
st.detrend("demean")
st.taper(max_percentage=0.05, type="hann")
st.remove_response(output="DISP", pre_filt=pre_filt, zero_mean=False, taper=False)
st.detrend("linear")
st.detrend("demean")
st.taper(max_percentage=0.05, type="hann")
st.interpolate(sampling_rate=sampling_rate, starttime=starttime, npts=npts)
```

This code basically shows how we process the observed data. We first read in the data, and then we remove the trend and mean value. After tapering, we remove the instrument response of the observed data. Then we apply the detrend, demean and taper again. At last, we interpolate the data to a certain  sampling rate.

More scripts could be found in [SeisProc](https://github.com/wjlei1990/SeisProc).

