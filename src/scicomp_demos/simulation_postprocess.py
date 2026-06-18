"""Synthetic simulation post-processing utilities."""

from __future__ import annotations

import csv
import math
from pathlib import Path


def damped_oscillator_samples(count: int = 121, dt: float = 0.05) -> list[dict[str, float]]:
    """Generate deterministic damped oscillator samples."""
    if count <= 1:
        raise ValueError("count must be greater than 1")
    if dt <= 0:
        raise ValueError("dt must be positive")

    samples: list[dict[str, float]] = []
    for index in range(count):
        time_s = index * dt
        displacement = math.exp(-0.18 * time_s) * math.cos(2.0 * math.pi * 0.7 * time_s)
        velocity = (
            -0.18 * math.exp(-0.18 * time_s) * math.cos(2.0 * math.pi * 0.7 * time_s)
            - 2.0 * math.pi * 0.7 * math.exp(-0.18 * time_s) * math.sin(2.0 * math.pi * 0.7 * time_s)
        )
        samples.append({"time_s": time_s, "displacement": displacement, "velocity": velocity})

    return samples


def summarize_samples(samples: list[dict[str, float]]) -> dict[str, float]:
    """Compute simple derived metrics from synthetic simulation samples."""
    if not samples:
        raise ValueError("samples must not be empty")

    final_time = samples[-1]["time_s"]
    peak_displacement = max(abs(sample["displacement"]) for sample in samples)
    peak_speed = max(abs(sample["velocity"]) for sample in samples)
    mean_energy_proxy = sum(
        sample["displacement"] ** 2 + sample["velocity"] ** 2 for sample in samples
    ) / len(samples)

    return {
        "sample_count": float(len(samples)),
        "final_time_s": final_time,
        "peak_abs_displacement": peak_displacement,
        "peak_abs_velocity": peak_speed,
        "mean_energy_proxy": mean_energy_proxy,
    }


def write_samples_csv(samples: list[dict[str, float]], path: Path) -> None:
    """Write synthetic samples to CSV with stable column order."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["time_s", "displacement", "velocity"])
        writer.writeheader()
        writer.writerows(samples)
