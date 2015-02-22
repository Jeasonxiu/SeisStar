---
layout: docs
title: Source inversion
permalink: /docs/source_inversion/
---

# Source Inversion Workflow

The source inversion is used to update source information. In another word, provide you with better seismic source in your current model settings.For example, in the [Global CMT Project](http://www.globalcmt.org/), source inversion is done using long period seismic data on prem model. However, in the global adjoint tomography project, we want to inverse the source in 3D model and also include the short period seismic data in. Thus, we use the CMTSolution as our starting point and update the source.

To perform a CMT inversion, the following steps need to be done.

<!-- ![Image of CMT inversion](/SeisStar/img/SourceInversion.jpg =200x100) -->
<center><img src="/SeisStar/img/SourceInversion.jpg" alt="CMT Inversion" width="400" align="middle"></center>


### 1. Prepare CMT files
The CMT inversion is based on finited difference method. i.e, perturbing the paramters of CMT solution and calculate waveform difference.  For global CMT solution, we usually invert 9 paramters: Moment tensor[*Mrr, Mtt, Mpp, Mrt, Mrp, Mtp*] and location[*latitude, longitude, Depth*]. Thus, 9 perturbed CMT files should be prepared at this stage. 

### 2. Forward Simulation
Forward simulation should be done based on every perturbed CMTSolution file. For example, if you want to invert both moment tensor and location, 9 forward simulation should be done for one source inversion. The forward solver information could be found in the [**Solvers**](/SeisStar/docs/solvers) page.

### 3. Data Preprocessing
The data preprocessing generally contains several steps of signal processing. Each step should be done very carefully. Operations includes removing trend, filtering data into targeted frequency band, remove instrument response to get true ground displacement and so on. A more detailed explanation and information could be found in the [**Preprocessing**](/SeisStar/docs/preprocessing/) page.

### 4. Window Selection
Window will be selected based on a pair of observed data and synthetic data. Measurements would be made only inside windows. A more detailed explanation could be in [**Windowing**](/SeisStar/docs/windows_selection/) page.

### 5. Source Inversion 
After we select windows, misfit will be calculated in windows and we can then get the gradient. The package we used is [**cmt3d**](https://github.com/QuLogic/GRD_CMT3D), developed by *Qinya Liu* and et al. 
