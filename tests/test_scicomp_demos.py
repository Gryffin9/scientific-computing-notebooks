from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path

from scicomp_demos import (
    damped_oscillator_samples,
    simpson_rule,
    summarize_samples,
    trapezoid_rule,
    write_samples_csv,
)


class ScientificComputingDemoTests(unittest.TestCase):
    def test_simpson_rule_integrates_sine_to_high_accuracy(self) -> None:
        estimate = simpson_rule(math.sin, 0.0, math.pi, 40)
        self.assertAlmostEqual(estimate, 2.0, places=6)

    def test_trapezoid_rule_converges_for_sine(self) -> None:
        coarse = abs(trapezoid_rule(math.sin, 0.0, math.pi, 10) - 2.0)
        fine = abs(trapezoid_rule(math.sin, 0.0, math.pi, 80) - 2.0)
        self.assertLess(fine, coarse)

    def test_synthetic_samples_have_stable_summary(self) -> None:
        samples = damped_oscillator_samples(count=11, dt=0.1)
        summary = summarize_samples(samples)
        self.assertEqual(summary["sample_count"], 11.0)
        self.assertAlmostEqual(summary["final_time_s"], 1.0)
        self.assertGreater(summary["peak_abs_displacement"], 0.9)

    def test_write_samples_csv_creates_expected_header(self) -> None:
        samples = damped_oscillator_samples(count=3, dt=0.2)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "samples.csv"
            write_samples_csv(samples, path)
            first_line = path.read_text(encoding="utf-8").splitlines()[0]
        self.assertEqual(first_line, "time_s,displacement,velocity")


if __name__ == "__main__":
    unittest.main()
