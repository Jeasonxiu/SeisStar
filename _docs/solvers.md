---
layout: docs
title: Forward and adjoint solvers
permalink: /docs/solvers/
---

# Forward and adjoint solvers

To perform a seismic inversion you will need a modeling package with _forward_ and _adjoint_ capabilities.

Because the elastic wave equation is _self-adjoint_, numerical code for the forward simulation can be reused for the adjoint simulation.  This is the approach taken with SPECFEM solvers.

For the forward simulation, SPECFEM users must supply a velocity model along with a number of parameter files described in the solver user manual.  The output consists of a set of seismic traces corresponding to user-supplied source and receiver locations.

For the adjoint simulation, SPECFEM users must supply a velocity model, parameter files, and a set of 'adjoint traces'.  Adjoint traces are computed from  processed observations and synthetics through a formula that depends on the objective function under consideration.  In our terminology, generating adjoint traces is the final step in preprocessing procedure.
