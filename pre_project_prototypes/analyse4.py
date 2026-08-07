#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.signal import (
    butter,
    filtfilt,
    hilbert,
    find_peaks,
)

filename = "creature7s.wav"

fs, x = wavfile.read(filename)

print(f"Sample rate : {fs} Hz")
print(f"Duration    : {len(x)/fs:.2f} s")

if x.ndim > 1:
    x = x.mean(axis=1)

x = x.astype(float)

# -------------------------------------------------------
# Band-pass around cricket carrier
# -------------------------------------------------------

low = 3500
high = 7000

b, a = butter(4,
              [low/(fs/2), high/(fs/2)],
              btype="band")

carrier = filtfilt(b, a, x)

# -------------------------------------------------------
# Carrier frequency
# -------------------------------------------------------

S = np.abs(np.fft.rfft(carrier))
f = np.fft.rfftfreq(len(carrier), 1/fs)

peak = np.argmax(S)

carrier_freq = f[peak]

print(f"\nCarrier frequency : {carrier_freq:.1f} Hz")

# -------------------------------------------------------
# Envelope
# -------------------------------------------------------

env = np.abs(hilbert(carrier))

# Smooth (~2 ms)
win = int(fs * 0.002)

if win < 1:
    win = 1

kernel = np.ones(win)/win

env = np.convolve(env, kernel, mode="same")

# -------------------------------------------------------
# Chirp detection
# -------------------------------------------------------

threshold = env.mean() + 0.8*env.std()

active = env > threshold

changes = np.diff(active.astype(int))

starts = np.where(changes == 1)[0]
ends = np.where(changes == -1)[0]

if len(ends) and len(starts):

    if ends[0] < starts[0]:
        ends = ends[1:]

    if len(starts) > len(ends):
        starts = starts[:-1]

print(f"\nDetected chirps : {len(starts)}")

chirp_lengths = []
syllable_counts = []
syllable_rates = []

plt.figure(figsize=(14,4))

t = np.arange(len(env))/fs

plt.plot(t, env)

# -------------------------------------------------------
# Analyse each chirp
# -------------------------------------------------------

for i, (s, e) in enumerate(zip(starts, ends), 1):

    seg = carrier[s:e]

    duration = (e-s)/fs

    if duration < 0.015:
        continue

    peaks, _ = find_peaks(
        np.abs(seg),
        height=np.max(np.abs(seg))*0.30,
        distance=int(fs/600)
    )

    syllables = len(peaks)

    rate = syllables/duration if duration > 0 else 0

    chirp_lengths.append(duration)
    syllable_counts.append(syllables)
    syllable_rates.append(rate)

    print(f"\nChirp {i}")
    print(f" duration : {duration*1000:.1f} ms")
    print(f" syllables: {syllables}")
    print(f" rate     : {rate:.1f} Hz")

    plt.axvspan(s/fs, e/fs,
                color="red",
                alpha=0.15)

plt.title("Detected chirps")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.savefig("10_chirps.png")

# -------------------------------------------------------
# Summary
# -------------------------------------------------------

starts_t = starts/fs

if len(starts_t) > 1:
    chirp_rep = np.diff(starts_t).mean()
else:
    chirp_rep = np.nan

print("\n------------------------------")

print(f"Mean chirp duration   : {1000*np.mean(chirp_lengths):.1f} ms")
print(f"Mean syllables/chirp  : {np.mean(syllable_counts):.1f}")
print(f"Mean syllable rate    : {np.mean(syllable_rates):.1f} Hz")

if np.isfinite(chirp_rep):
    print(f"Mean chirp repetition : {1/chirp_rep:.2f} Hz")

print("\nFinished.")
