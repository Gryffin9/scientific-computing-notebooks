from __future__ import annotations

import math

from scicomp_demos import convergence_table


def main() -> None:
    rows = convergence_table(
        function=math.sin,
        lower=0.0,
        upper=math.pi,
        exact_value=2.0,
        interval_counts=[10, 20, 40, 80],
    )

    print("Integral of sin(x) on [0, pi]; exact value = 2.0")
    print("intervals | trapezoid error | simpson error")
    for row in rows:
        print(
            f"{int(row['intervals']):9d} | "
            f"{row['trapezoid_abs_error']:.8f}      | "
            f"{row['simpson_abs_error']:.8f}"
        )


if __name__ == "__main__":
    main()
