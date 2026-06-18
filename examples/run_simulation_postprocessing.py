from __future__ import annotations

from pathlib import Path

from scicomp_demos import damped_oscillator_samples, summarize_samples, write_samples_csv


def main() -> None:
    samples = damped_oscillator_samples()
    summary = summarize_samples(samples)
    output_path = Path("examples/outputs/synthetic_oscillator.csv")
    write_samples_csv(samples, output_path)

    print(f"Wrote synthetic samples to {output_path}")
    for key, value in summary.items():
        print(f"{key}: {value:.6f}")


if __name__ == "__main__":
    main()
