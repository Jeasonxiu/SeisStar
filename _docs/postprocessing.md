---
layout: docs
title: Postprocessing
permalink: /docs/postprocessing/
---

The post-processing includes several operations to kernels(the kernel are calculated by the solver). Operations include: summing, smoothing and preconditioning.

After the adjoint simulations, we get kernels for diffferent events. We will conduct a series of operations to calculate the gradient. After we get the gradient, we can then enter the optimization stage.

### Summing

At this step, we sum all kernels(from different events) together.

### Smoothing

At this step, we smooth the summed up kernels.

### Preconditioning

At this step, we precondition the kernels to approximate the gradient.
