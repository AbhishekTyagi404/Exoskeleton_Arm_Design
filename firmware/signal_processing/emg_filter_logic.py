# EMG Signal Processing Logic
# Version: 1.1
# Author: Abhishek Tyagi
# Description: Filters raw EMG signal, extracts envelope, and detects activation threshold (MUAP aligned)

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# --- Configuration ---
SAMPLE_RATE = 1000     # Hz
HIGH_PASS = 20         # Hz (removes motion artifacts)
LOW_PASS = 450         # Hz (removes noise beyond muscle activation band)
EMG_THRESHOLD = 0.5    # Detection threshold for activation

# --- Synthetic EMG for Testing ---
time = np.linspace(0, 2, 2 * SAMPLE_RATE)
raw_signal = np.sin(2 * np.pi * 50 * time) + 0.5 * np.random.randn(len(time))

# --- Filter Design ---
def bandpass_filter(signal, lowcut, highcut, fs, order=2):
    """Applies Butterworth bandpass filter."""
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)

# --- Full-Wave Rectification ---
def rectify(signal):
    """Applies full-wave rectification."""
    return np.abs(signal)

# --- Envelope Extraction ---
def envelope(signal, window_size=50):
    """Extracts EMG envelope using moving average (low-pass equivalent)."""
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')

# --- Activation Detection ---
def detect_activation(smoothed_signal, threshold):
    """Detects regions where EMG exceeds the threshold."""
    return smoothed_signal > threshold

# --- Processing Pipeline ---
filtered = bandpass_filter(raw_signal, HIGH_PASS, LOW_PASS, SAMPLE_RATE)
rectified = rectify(filtered)
smoothed = envelope(rectified)
activation = detect_activation(smoothed, EMG_THRESHOLD)

# --- Plotting ---
plt.figure(figsize=(10, 4))
plt.plot(time, raw_signal, label="Raw EMG", alpha=0.6)
plt.plot(time, smoothed, label="Smoothed Envelope", linewidth=2)
plt.fill_between(time, 0, 1, where=activation, alpha=0.2, color='red', label="Activation")
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.title("EMG Signal Processing with MUAP Activation Detection")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
