"""Numerical integration routines with transparent error reporting."""

from __future__ import annotations

from collections.abc import Callable


def trapezoid_rule(function: Callable[[float], float], lower: float, upper: float, intervals: int) -> float:
    """Approximate an integral using the composite trapezoid rule."""
    if intervals <= 0:
        raise ValueError("intervals must be positive")

    width = (upper - lower) / intervals
    total = 0.5 * (function(lower) + function(upper))

    for index in range(1, intervals):
        total += function(lower + index * width)

    return total * width


def simpson_rule(function: Callable[[float], float], lower: float, upper: float, intervals: int) -> float:
    """Approximate an integral using the composite Simpson rule."""
    if intervals <= 0:
        raise ValueError("intervals must be positive")
    if intervals % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of intervals")

    width = (upper - lower) / intervals
    odd_sum = 0.0
    even_sum = 0.0

    for index in range(1, intervals):
        value = function(lower + index * width)
        if index % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return (width / 3.0) * (function(lower) + function(upper) + 4.0 * odd_sum + 2.0 * even_sum)


def convergence_table(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    exact_value: float,
    interval_counts: list[int],
) -> list[dict[str, float]]:
    """Return integration approximations and absolute errors for each interval count."""
    rows: list[dict[str, float]] = []

    for intervals in interval_counts:
        trapezoid = trapezoid_rule(function, lower, upper, intervals)
        simpson = simpson_rule(function, lower, upper, intervals)
        rows.append(
            {
                "intervals": float(intervals),
                "trapezoid": trapezoid,
                "trapezoid_abs_error": abs(trapezoid - exact_value),
                "simpson": simpson,
                "simpson_abs_error": abs(simpson - exact_value),
            }
        )

    return rows
