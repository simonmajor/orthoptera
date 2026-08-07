#!/usr/bin/env python

import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

filename = "creature7s.wav"

fs, x = wavfile.read(filename)

# Convert to float
if x.ndim > 1:
    x = x.mean(axis=1)

x = x.astype(float)

# Remove DC
x -= np.mean(x)

print(f"Sample rate : {fs} Hz")
print(f"Duration    : {len(x)/fs:.2f} s")

##########################################################
# Spectrum
##########################################################

f = np.fft.rfftfreq(len(x), 1/fs)
S = np.abs(np.fft.rfft(x))

mask = (f > 3500) & (f < 7000)
peak = np.argmax(S[mask])
peak_freq = f[mask][peak]

print(f"\nDominant frequency = {peak_freq:.1f} Hz")

plt.figure(figsize=(10,4))
plt.semilogx(f,S)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Spectrum")
plt.grid(True)
plt.savefig("01_spectrum.png",dpi=200)

##########################################################
# Spectrogram
##########################################################

plt.figure(figsize=(12,6))

Pxx, freqs, bins, im = plt.specgram(
    x,
    NFFT=4096,
    Fs=fs,
    noverlap=3500,
)

plt.ylim(0,12000)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram")
plt.colorbar()
plt.savefig("02_spectrogram.png",dpi=200)

##########################################################
# Bandpass around dominant frequency
##########################################################

bw = 500

low = max(100, peak_freq-bw)
high = peak_freq+bw

b,a = signal.butter(
    4,
    [low/(fs/2), high/(fs/2)],
    btype="band"
)

y = signal.filtfilt(b,a,x)

##########################################################
# Envelope
##########################################################

analytic = signal.hilbert(y)
env = np.abs(analytic)

env = signal.savgol_filter(env,501,3)

t = np.arange(len(env))/fs

plt.figure(figsize=(12,4))
plt.plot(t,env)
plt.xlabel("Time (s)")
plt.ylabel("Envelope")
plt.title("Amplitude envelope")
plt.savefig("03_envelope.png",dpi=200)

##########################################################
# Peak detection
##########################################################

height = np.mean(env)+0.5*np.std(env)

peaks,_ = signal.find_peaks(
    env,
    height=height,
    distance=int(0.02*fs)
)

plt.figure(figsize=(12,4))
plt.plot(t,env)
plt.plot(peaks/fs,env[peaks],"r.")
plt.xlabel("Time (s)")
plt.ylabel("Envelope")
plt.title("Detected pulses")
plt.savefig("04_pulses.png",dpi=200)

print(f"\nDetected pulses = {len(peaks)}")

if len(peaks)>1:
    intervals = np.diff(peaks)/fs

    print(f"Mean interval = {intervals.mean():.4f} s")
    print(f"Pulse rate    = {1/intervals.mean():.2f} Hz")

##########################################################
# Autocorrelation
##########################################################

env2 = env - np.mean(env)

ac = signal.correlate(env2,env2,mode="full")
ac = ac[len(ac)//2:]

lags = np.arange(len(ac))/fs

plt.figure(figsize=(10,4))
plt.plot(lags,ac)
plt.xlim(0,1)
plt.xlabel("Lag (s)")
plt.ylabel("Autocorrelation")
plt.title("Envelope autocorrelation")
plt.grid(True)
plt.savefig("05_autocorrelation.png",dpi=200)

print("\nFinished.")
