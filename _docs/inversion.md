---
layout: docs
title: Seismic inversion
permalink: /docs/inversion/
---

# Model Inversion Workflow

With the development of high performance computing and seismic inversion theory in recent years, full 3D seismic inversion has become more and more popular. However, the inversion has become very complex and each step should be conducted very carefully. Thus, we want to come up with a framework for full 3D inversion. 
It serves as two goals:

```
* help to understand basic operations in the source inversion
* provide you all tools you needed to perform your own inversion
```

To perform a model inversion, the following steps need to be done.
<center><img src="/SeisStar/img/inversion_workflow.jpg" alt="Inversion Workflow" width="400" align="middle"></center>

### 1. Forward Simulation
At this step, synthetic data will be calculated on the initial model. More information about the forward solver could be found in the [**Solver**](/SeisStar/docs/solvers) page.

### 2. Data Preprocessing
The data preprocessing contains several steps of signal processing, including operations like removing mean and trend, filtering, removing instrument response and so on. Processing should be conducted in a very careful way to make sure that no artificial information is included in this step. A more detailed explanation and information could be found in the [**Preprocessing**](/SeisStar/docs/preprocessing/) page.

### 3. Generate Adjoint sources
The adjoint source is usually generated in two steps:
  1. **Window Selection**
      Window will be selected on a pair of observed trace and synthetic trace. More detialed information could be found in [**Window**](/SeisStar/docs/windows_selection) page.
  2. **Adjoint Source Calculation**
      You can choose different types of adjoint source but measurements will be only made inside those windows. Measurements includes traveltime difference, amplitude difference and waveform difference. More detailed information could be found in [**Adjoint sources**](/SeisStar/docs/adjoint_sources) page.

### 4. Adjoint simulation
Adjoint sources are used to run the adjoint simulation. Kernels are calculated. The information about adjoint solver could be found in the [**Solver**](/SeisStar/docs/solvers) page.

### 5. Postprocessing
Postprocessing includes operations on kernels, to prepare the kernel for optimization stage, for example, summarizing, perconditioning and smoothing. More detailed information could be found in the [**Postprocessing**](/SeisStar/docs/postprocessing) page.

### 6. Optimization
This Optimization involves schemas how to use properly use gradient to calculate model update. Methods includes steepest decent, conjugate gradient, L-BFGS and so on. More detailed information could be found in the [**Optimization**](/SeisStar/docs/optimization) page.
