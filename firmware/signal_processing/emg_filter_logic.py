# EMG Signal Processing Logic
# Author: Abhishek Tyagi
# Description: Filters raw EMG signal and detects activation threshold

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# --- Configuration ---
EMG_THRESHOLD = 0.5  # Adjust based on your signal
SAMPLE_RATE = 1000   # Hz
HIGH_PASS = 20       # Hz
LOW_PASS = 450       # Hz

# --- Load EMG data ---
# Replace this with actual CSV input
time = np.linspace(0, 2, 2 * SAMPLE_RATE)
raw_signal = np.sin(2 * np.pi * 50 * time) + 0.5 * np.random.randn(len(time))  # synthetic EMG-like signal

# --- Filter Design ---
def bandpass_filter(signal, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

# --- Full-Wave Rectification ---
def rectify(signal):
    return np.abs(signal)

# --- Envelope Detection ---
def envelope(signal, window_size=50):
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# --- Processing Pipeline ---
filtered = bandpass_filter(raw_signal, HIGH_PASS, LOW_PASS, SAMPLE_RATE)
rectified = rectify(filtered)
smoothed = envelope(rectified)

# --- Thresholding ---
activation = smoothed > EMG_THRESHOLD

# --- Plot ---
plt.figure(figsize=(10, 4))
plt.plot(time, raw_signal, label="Raw EMG")
plt.plot(time, smoothed, label="Smoothed Envelope", linewidth=2)
plt.fill_between(time, 0, 1, where=activation, alpha=0.2, color='red', label="Activation")
plt.xlabel("Time (s)")
plt.ylabel("EMG Signal")
plt.legend()
plt.title("EMG Signal Processing")
plt.grid()
plt.tight_layout()
plt.show()
