# Scientific Computing Notebooks

Small, reproducible Python examples for scientific computing, numerical methods, and tutoring-style technical explanation.

The examples are intentionally thin and inspectable. They are designed to show method, assumptions, validation, and clean execution rather than hide the work behind a large framework.

## Contents

- `notebooks/`: notebook versions of the examples for explanation and teaching.
- `src/scicomp_demos/`: reusable Python functions used by the scripts and tests.
- `examples/`: deterministic script equivalents for running from a terminal.
- `tests/`: standard-library unit tests for the numerical routines.

## Examples

### Numerical integration

Approximates a smooth integral with trapezoidal and Simpson rules, compares against a known analytic value, and prints a convergence table.

Skill demonstrated: numerical methods, error analysis, clear explanation, and reproducible Python.

Run:

```bash
PYTHONPATH=src python3 examples/run_numerical_integration.py
```

### Simulation post-processing

Generates a synthetic damped oscillator signal, extracts summary metrics, and writes a small reproducible output table.

Skill demonstrated: simulation-style data handling, derived metrics, deterministic outputs, and documentation-friendly code.

Run:

```bash
PYTHONPATH=src python3 examples/run_simulation_postprocessing.py
```

## Validation

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## Notes

The data is synthetic. No private research data, product data, or confidential project internals are included.
