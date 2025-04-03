# emg_threshold_trigger.py
# Real-time EMG Activation Trigger

def detect_activation(signal, threshold=0.5):
    """Returns True if smoothed EMG signal exceeds threshold."""
    return signal > threshold
