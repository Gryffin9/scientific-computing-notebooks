# Scientific Computing Notebooks

Reproducible Python examples for numerical methods, modelling, and simulation-style analysis.

This repo is a public collection of small, readable scientific-computing examples. The goal is to show clear explanation, clean notebooks, reproducible code, and practical numerical workflows.

## What this repo demonstrates

- Clean Python structure for scientific-computing examples
- Numerical methods explained through short scripts and notebooks
- Reproducible runs with deterministic inputs and outputs
- Tutoring-friendly code that exposes assumptions and intermediate values
- Simulation-style post-processing with clear summaries

## Example topics

- numerical integration
- optimization
- simulation post-processing
- uncertainty-aware analysis
- plotting and interpretation
- tensor/numerical-method utilities

## Repository structure

- `notebooks/`: notebook versions of selected examples
- `src/scicomp_demos/`: reusable Python utilities
- `examples/`: terminal-friendly runnable scripts
- `tests/`: checks for the numerical routines and synthetic workflows

## How to run

Run the numerical integration example:

```bash
PYTHONPATH=src python3 examples/run_numerical_integration.py
```

Run the simulation-style post-processing example:

```bash
PYTHONPATH=src python3 examples/run_simulation_postprocessing.py
```

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## Intended audience

This repo is for students, researchers, and collaborators who want examples that are easier to read, explain, and adapt than a large research codebase.

## Notes on reproducibility

The examples use synthetic or analytic inputs only. No private research data, private product data, or confidential project internals are included.
