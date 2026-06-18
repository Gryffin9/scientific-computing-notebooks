"""Small scientific-computing examples used by the public demo notebooks."""

from .integration import convergence_table, simpson_rule, trapezoid_rule
from .simulation_postprocess import (
    damped_oscillator_samples,
    summarize_samples,
    write_samples_csv,
)

__all__ = [
    "convergence_table",
    "damped_oscillator_samples",
    "simpson_rule",
    "summarize_samples",
    "trapezoid_rule",
    "write_samples_csv",
]
