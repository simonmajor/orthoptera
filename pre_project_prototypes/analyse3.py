#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal

filename = "creature7s.wav"

fs, x = wavfile.read(filename)

if x.ndim > 1:
    x = x.mean(axis=1)

x = x.astype(np.float64)
x -= np.mean(x)

print(f"Sample rate : {fs}")
print(f"Duration    : {len(x)/fs:.2f} s")

#######################################################
# Find carrier frequency (>3kHz only)
#######################################################

window = np.hanning(len(x))

S = np.abs(np.fft.rfft(x*window))

f = np.fft.rfftfreq(len(x),1/fs)

mask = (f > 3000) & (f < 7000)

carrier = f[mask][np.argmax(S[mask])]

print(f"\nCarrier frequency = {carrier:.2f} Hz")

#######################################################
# Narrow band-pass
#######################################################

bw = 150

b,a = signal.butter(
    6,
    [(carrier-bw)/(fs/2),
     (carrier+bw)/(fs/2)],
    btype="bandpass"
)

y = signal.filtfilt(b,a,x)

#######################################################
# Envelope
#######################################################

analytic = signal.hilbert(y)

env = np.abs(analytic)

b,a = signal.butter(
    4,
    80/(fs/2),
    btype="low"
)

env = signal.filtfilt(b,a,env)

env -= env.mean()

#######################################################
# FFT of envelope
#######################################################

E = np.abs(np.fft.rfft(env*np.hanning(len(env))))

fe = np.fft.rfftfreq(len(env),1/fs)

mask = fe < 100

peak = np.argmax(E[mask][1:])+1

print(f"Envelope modulation = {fe[mask][peak]:.2f} Hz")

#######################################################
# Zoomed waveform
#######################################################

start = 2.45
duration = 0.10

i0 = int(start*fs)
i1 = int((start+duration)*fs)

t = np.arange(i0,i1)/fs

plt.figure(figsize=(12,4))
plt.plot(t,y[i0:i1])
plt.title("100 ms carrier")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.savefig("06_waveform_zoom.png",dpi=200)

#######################################################
# Envelope
#######################################################

plt.figure(figsize=(12,4))
plt.plot(np.arange(len(env))/fs,env)
plt.title("Carrier envelope")
plt.xlabel("Time (s)")
plt.tight_layout()
plt.savefig("07_carrier_envelope.png",dpi=200)

#######################################################
# Envelope spectrum
#######################################################

plt.figure(figsize=(10,4))
plt.plot(fe[mask],E[mask])
plt.grid()
plt.xlabel("Hz")
plt.title("Envelope modulation spectrum")
plt.tight_layout()
plt.savefig("08_modulation_fft.png",dpi=200)

#######################################################
# High-resolution spectrogram
#######################################################

plt.figure(figsize=(12,6))

plt.specgram(
    y,
    NFFT=1024,
    Fs=fs,
    noverlap=960,
    cmap="viridis"
)

plt.ylim(4300,4900)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.savefig("09_zoom_spectrogram.png",dpi=200)

#######################################################
# Peak detection
#######################################################

pk,_ = signal.find_peaks(
    env,
    prominence=np.std(env)*0.5,
    distance=int(fs/40)
)

print(f"Detected envelope peaks : {len(pk)}")

if len(pk)>2:
    d = np.diff(pk)/fs
    print(f"Mean spacing            : {d.mean():.4f} s")
    print(f"Mean repetition rate    : {1/d.mean():.2f} Hz")

print("\nFinished.")
