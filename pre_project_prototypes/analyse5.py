#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.signal import (
    butter,
    filtfilt,
    hilbert,
    find_peaks,
    peak_widths,
)

filename = "creature7s.wav"

fs, x = wavfile.read(filename)

if x.ndim > 1:
    x = x.mean(axis=1)

x = x.astype(float)

print(f"Sample rate : {fs} Hz")
print(f"Duration    : {len(x)/fs:.2f} s")

# --------------------------------------------------------
# Band-pass around insect carrier
# --------------------------------------------------------

low = 3500
high = 7000

b, a = butter(
    4,
    [low/(fs/2), high/(fs/2)],
    btype="band"
)

carrier = filtfilt(b, a, x)

# --------------------------------------------------------
# Carrier frequency
# --------------------------------------------------------

S = np.abs(np.fft.rfft(carrier))
f = np.fft.rfftfreq(len(carrier), 1/fs)

carrier_freq = f[np.argmax(S)]

print(f"\nCarrier frequency : {carrier_freq:.1f} Hz")

# --------------------------------------------------------
# Hilbert envelope
# --------------------------------------------------------

env = np.abs(hilbert(carrier))

env /= np.max(env)

# --------------------------------------------------------
# Low-pass envelope at 30 Hz
# --------------------------------------------------------

cutoff = 30.0

b, a = butter(
    4,
    cutoff/(fs/2),
    btype="low"
)

smooth = filtfilt(b, a, env)

smooth -= smooth.min()
smooth /= smooth.max()

# --------------------------------------------------------
# Detect chirps
# --------------------------------------------------------

minimum_spacing = int(0.15 * fs)

peaks, props = find_peaks(
    smooth,
    prominence=0.15,
    distance=minimum_spacing
)

t = np.arange(len(env))/fs

print(f"\nDetected chirps : {len(peaks)}")

# --------------------------------------------------------
# Peak widths (half prominence)
# --------------------------------------------------------

results = peak_widths(
    smooth,
    peaks,
    rel_height=0.5
)

widths = results[0] / fs

# --------------------------------------------------------
# Intervals
# --------------------------------------------------------

peak_times = peaks / fs

if len(peak_times) > 1:
    intervals = np.diff(peak_times)
else:
    intervals = np.array([])

# --------------------------------------------------------
# Statistics
# --------------------------------------------------------

print()

if len(intervals):

    print(f"Mean interval       : {intervals.mean():.3f} s")
    print(f"Repetition rate     : {1/intervals.mean():.2f} Hz")
    print(f"Interval SD         : {intervals.std():.3f} s")
    print(f"CV                  : {intervals.std()/intervals.mean():.3f}")

print(f"Mean chirp width    : {1000*widths.mean():.1f} ms")
print(f"Median chirp width  : {1000*np.median(widths):.1f} ms")

# --------------------------------------------------------
# Plot envelopes
# --------------------------------------------------------

plt.figure(figsize=(14,4))

plt.plot(t, env,
         alpha=0.35,
         label="Raw envelope")

plt.plot(t, smooth,
         linewidth=2,
         label="30 Hz low-pass")

plt.scatter(
    peak_times,
    smooth[peaks],
    color="red",
    zorder=10,
    label="Detected chirps"
)

plt.xlabel("Time (s)")
plt.ylabel("Normalised amplitude")
plt.title("Raw and smoothed envelopes")
plt.legend()

plt.tight_layout()
plt.savefig("10_raw_vs_smoothed_envelope.png")

# --------------------------------------------------------
# Chirp plot
# --------------------------------------------------------

plt.figure(figsize=(14,3))

plt.plot(t, smooth)

for p in peak_times:
    plt.axvline(p,
                color="red",
                alpha=0.3)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Detected chirps")

plt.tight_layout()
plt.savefig("11_detected_chirps.png")

# --------------------------------------------------------
# Histogram
# --------------------------------------------------------

if len(intervals):

    plt.figure(figsize=(6,4))

    plt.hist(intervals, bins=10)

    plt.xlabel("Interval (s)")
    plt.ylabel("Count")
    plt.title("Chirp interval distribution")

    plt.tight_layout()
    plt.savefig("12_interval_histogram.png")

print("\nFinished.")

