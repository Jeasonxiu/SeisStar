---
layout: docs
title: Inversion workflow
permalink: /docs/inversion/
---

# Inversion workflow

Seismic inversion is by nature an iterative procedure.  At each iteration we perform the following steps.


#### 1. Forward simulation

Given a _velocity model_ as input, the forward simulation returns synthetic traces as output.  After the first iteration, forward simulations performed as part of optimization procedure can simply be carried over to the next iteration.


#### 2. Pre-processing
In our terminology, _pre-processing_ includes all operations performed on seismic traces prior to the adjoint simulation.  Signal processing operations, comparison of obervations and synthetics, and creation of adjoint traces fall into this category.


#### 3. Adjoint simulation

Given _adjoint traces_ as input, the adjoint simulations returns _sensitivity kernels_ as output.


#### 4. Post-processing
In our terminology _post-processing_ includes all operations performed on sensitivity kernels following the adjoint simulation.  Projection, regularization, and preconditioning fall into this category.


#### 5. Optimization

Given the gradient direction, the optimization procedure returns an updated model.  Conventionally, the optimization procedure consists of separate _search direction_ and _line search_ computations.

