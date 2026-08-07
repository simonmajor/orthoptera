#!/usr/bin/env python3
"""Exploratory, corpus-specific acoustic survey (not a production detector).

The script deliberately retains its per-recording prominence settings in the
output.  They make candidate events inspectable; they are not a proposed
``signal.detect`` interface or a biological chirp annotation.
"""

from __future__ import annotations

import argparse
import csv
import json
import struct
import warnings
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile


ANALYSIS_VERSION = "exploratory-acoustic-survey-1"


@dataclass(frozen=True)
class DetectorSettings:
    prominence_mad: float
    minimum_separation_s: float = 0.08
    band_half_width_hz: float = 600.0
    envelope_smoothing_s: float = 0.01


# Chosen only after visually inspecting the corpus.  Keeping these explicit is
# useful evidence of sensitivity, rather than concealing tuning in a detector.
SETTINGS = {
    "XC1085943": DetectorSettings(6.0),
    "XC924802": DetectorSettings(4.0),
    "XC924980": DetectorSettings(6.0),
    "XC925129": DetectorSettings(6.0),
    "XC940663": DetectorSettings(6.0),
    "creature7s": DetectorSettings(4.0),
}


def recording_key(path: Path) -> str:
    return next(key for key in SETTINGS if key in path.name)


def pcm_to_float(samples: np.ndarray) -> np.ndarray:
    """Convert PCM/floating WAV samples without assuming a specific bit depth."""
    result = samples.astype(np.float64)
    if samples.dtype.kind in "iu":
        info = np.iinfo(samples.dtype)
        result /= max(abs(info.min), info.max)
    return result


def load_mono(path: Path) -> tuple[int, np.ndarray, np.ndarray]:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", wavfile.WavFileWarning)
        sample_rate, raw = wavfile.read(path)
    normalised = pcm_to_float(raw)
    mono = normalised.mean(axis=1) if normalised.ndim == 2 else normalised
    return sample_rate, raw, mono - np.median(mono)


def wav_encoding(path: Path) -> tuple[str, int]:
    """Read WAV ``fmt `` metadata; SciPy expands 24-bit PCM to int32."""
    with path.open("rb") as stream:
        stream.read(12)
        while True:
            chunk_id = stream.read(4)
            length_data = stream.read(4)
            if len(chunk_id) != 4 or len(length_data) != 4:
                raise ValueError(f"No fmt chunk in {path}")
            length = struct.unpack("<I", length_data)[0]
            body = stream.read(length)
            if length % 2:
                stream.read(1)
            if chunk_id == b"fmt ":
                format_code, _, _, _, _, bits = struct.unpack("<HHIIHH", body[:16])
                if format_code == 0xFFFE and len(body) >= 40:
                    # WAVE_FORMAT_EXTENSIBLE: first GUID word is the actual code.
                    format_code = struct.unpack("<H", body[24:26])[0]
                return ({1: "PCM", 3: "IEEE float"}.get(format_code, f"WAV format {format_code}"), bits)


def high_frequency_peak(sample_rate: int, samples: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Return strongest Welch peak above 2 kHz, alongside the full PSD."""
    frequencies, psd = signal.welch(
        samples, sample_rate, nperseg=min(65536, len(samples)), noverlap=None
    )
    usable = (frequencies >= 2000) & (frequencies < min(20000, sample_rate / 2 - 100))
    return float(frequencies[usable][np.argmax(psd[usable])]), frequencies, psd


def smoothed_band_envelope(
    samples: np.ndarray, sample_rate: int, centre_hz: float, settings: DetectorSettings
) -> np.ndarray:
    low = max(100, centre_hz - settings.band_half_width_hz)
    high = min(sample_rate / 2 - 100, centre_hz + settings.band_half_width_hz)
    sos = signal.butter(4, [low, high], btype="bandpass", fs=sample_rate, output="sos")
    filtered = signal.sosfiltfilt(sos, samples)
    envelope = np.abs(signal.hilbert(filtered))
    window = max(5, int(round(settings.envelope_smoothing_s * sample_rate)) | 1)
    return signal.savgol_filter(envelope, window, 2), filtered


def candidates(envelope: np.ndarray, sample_rate: int, settings: DetectorSettings) -> dict[str, np.ndarray]:
    """Locate short, prominent envelope events at a modest analysis rate."""
    decimation = max(1, sample_rate // 200)
    reduced = envelope[::decimation]
    rate = sample_rate / decimation
    median = float(np.median(reduced))
    mad = float(np.median(np.abs(reduced - median)))
    peaks, properties = signal.find_peaks(
        reduced,
        prominence=settings.prominence_mad * mad,
        distance=max(1, round(settings.minimum_separation_s * rate)),
        width=1,
    )
    widths, _, left, right = signal.peak_widths(reduced, peaks, rel_height=0.5)
    return {
        "times": peaks / rate,
        "starts": left / rate,
        "ends": right / rate,
        "durations": widths / rate,
        "prominences": properties["prominences"],
        "median": np.array([median]),
        "mad": np.array([mad]),
    }


def array_summary(values: np.ndarray) -> dict[str, float | int | None]:
    if len(values) == 0:
        return {"count": 0, "median": None, "mean": None, "p10": None, "p90": None, "cv": None}
    mean = float(np.mean(values))
    return {
        "count": int(len(values)),
        "median": float(np.median(values)),
        "mean": mean,
        "p10": float(np.quantile(values, 0.1)),
        "p90": float(np.quantile(values, 0.9)),
        "cv": float(np.std(values) / mean) if mean else None,
    }


def plot_diagnostics(
    output: Path, name: str, sample_rate: int, samples: np.ndarray, filtered: np.ndarray,
    envelope: np.ndarray, events: dict[str, np.ndarray], carrier_hz: float,
) -> None:
    seconds = np.arange(len(samples)) / sample_rate
    figure, axes = plt.subplots(4, 1, figsize=(14, 14), constrained_layout=True)
    axes[0].plot(seconds[::max(1, sample_rate // 1000)], samples[::max(1, sample_rate // 1000)], lw=0.35)
    axes[0].set(title=f"{name}: waveform", ylabel="normalised amplitude", xlim=(0, seconds[-1]))
    psd_frequencies, psd = signal.welch(samples, sample_rate, nperseg=min(65536, len(samples)))
    usable_psd = (psd_frequencies > 0) & (psd_frequencies <= min(20000, sample_rate / 2))
    axes[1].semilogy(psd_frequencies[usable_psd] / 1000, psd[usable_psd], color="black", lw=0.6)
    axes[1].axvline(carrier_hz / 1000, color="cyan", lw=0.8, label="exploratory band centre")
    axes[1].set(xlabel="frequency (kHz)", ylabel="Welch PSD", title="whole-recording spectrum")
    axes[1].legend(loc="upper right")
    frequencies, times, spectrum = signal.spectrogram(
        samples, sample_rate, nperseg=min(2048, len(samples)), noverlap=1536, mode="magnitude"
    )
    keep = frequencies <= min(20000, sample_rate / 2)
    axes[2].pcolormesh(times, frequencies[keep] / 1000, 20 * np.log10(spectrum[keep] + 1e-10), shading="auto", cmap="magma")
    axes[2].axhline(carrier_hz / 1000, color="cyan", lw=0.7, label="exploratory band centre")
    axes[2].set(ylabel="frequency (kHz)", ylim=(0, min(20, sample_rate / 2000)), title="spectrogram")
    axes[2].legend(loc="upper right")
    step = max(1, sample_rate // 1000)
    axes[3].plot(seconds[::step], envelope[::step], color="black", lw=0.5, label="10 ms band envelope")
    axes[3].vlines(events["starts"], 0, np.interp(events["starts"], seconds, envelope), color="tab:blue", lw=0.6)
    axes[3].vlines(events["ends"], 0, np.interp(events["ends"], seconds, envelope), color="tab:blue", lw=0.6)
    axes[3].plot(events["times"], np.interp(events["times"], seconds, envelope), "r.", ms=3, label="candidate peaks")
    axes[3].set(xlabel="time (s)", ylabel="envelope", title="candidate-event boundaries (half prominence)")
    axes[3].legend(loc="upper right")
    figure.savefig(output / f"{name}_overview.png", dpi=150)
    plt.close(figure)

    # Envelope shape comparison aligns candidate maxima; it reveals whether a
    # nominal event is a stable unit without suggesting that it is a chirp.
    half_window = int(0.06 * sample_rate)
    chosen = np.linspace(0, len(events["times"]) - 1, min(20, len(events["times"])), dtype=int)
    figure, axis = plt.subplots(figsize=(10, 4), constrained_layout=True)
    for index in chosen:
        centre = int(events["times"][index] * sample_rate)
        start, end = centre - half_window, centre + half_window
        if start < 0 or end > len(envelope):
            continue
        segment = envelope[start:end]
        scale = np.max(segment)
        axis.plot(np.arange(-half_window, half_window) / sample_rate, segment / scale, alpha=0.45, lw=0.8)
    axis.set(title=f"{name}: normalised 120 ms windows around sampled candidate maxima", xlabel="seconds from peak", ylabel="normalised envelope")
    figure.savefig(output / f"{name}_candidate_shapes.png", dpi=150)
    plt.close(figure)


def analyse(path: Path, output: Path) -> dict[str, object]:
    key = recording_key(path)
    settings = SETTINGS[key]
    sample_rate, raw, samples = load_mono(path)
    carrier_hz, frequencies, psd = high_frequency_peak(sample_rate, samples)
    envelope, filtered = smoothed_band_envelope(samples, sample_rate, carrier_hz, settings)
    events = candidates(envelope, sample_rate, settings)
    intervals = np.diff(events["times"])
    name = path.stem.replace(" ", "_").replace("-", "_")
    plot_diagnostics(output, name, sample_rate, samples, filtered, envelope, events, carrier_hz)
    dtype = str(raw.dtype)
    encoding, bit_depth = wav_encoding(path)
    return {
        "file": path.name,
        "plot_stem": name,
        "sample_rate_hz": sample_rate,
        "sample_dtype": dtype,
        "encoding": encoding,
        "bit_depth": bit_depth,
        "channels": int(raw.shape[1]) if raw.ndim == 2 else 1,
        "duration_s": len(samples) / sample_rate,
        "peak": float(np.max(np.abs(samples))),
        "rms": float(np.sqrt(np.mean(samples ** 2))),
        "p99_abs": float(np.quantile(np.abs(samples), 0.99)),
        "exploratory_band_centre_hz": carrier_hz,
        "detector": {"prominence_mad": settings.prominence_mad, "minimum_separation_s": settings.minimum_separation_s, "band_half_width_hz": settings.band_half_width_hz, "envelope_smoothing_s": settings.envelope_smoothing_s},
        "event_duration_s": array_summary(events["durations"]),
        "inter_peak_interval_s": array_summary(intervals),
        "events": {key: value.tolist() for key, value in events.items() if key not in {"median", "mad"}},
        "envelope_median": float(events["median"][0]),
        "envelope_mad": float(events["mad"][0]),
    }


def write_events(output: Path, results: list[dict[str, object]]) -> None:
    with (output / "candidate_events.csv").open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["recording", "event", "start_s", "end_s", "peak_s", "duration_s", "prominence"])
        for result in results:
            events = result["events"]
            for index, (start, end, peak, duration, prominence) in enumerate(zip(events["starts"], events["ends"], events["times"], events["durations"], events["prominences"]), start=1):
                writer.writerow([result["file"], index, f"{start:.6f}", f"{end:.6f}", f"{peak:.6f}", f"{duration:.6f}", f"{prominence:.9g}"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("tests/data"))
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    arguments.output.mkdir(parents=True, exist_ok=True)
    results = [analyse(path, arguments.output) for path in sorted(arguments.input.glob("*.wav"))]
    write_events(arguments.output, results)
    (arguments.output / "summary.json").write_text(json.dumps({"analysis_version": ANALYSIS_VERSION, "recordings": results}, indent=2) + "\n")


if __name__ == "__main__":
    main()
