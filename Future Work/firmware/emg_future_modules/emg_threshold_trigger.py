# emg_threshold_trigger.py
# Real-Time EMG Activation Trigger
# Author: Abhishek Tyagi

def detect_activation(signal_value, threshold=0.5):
    """
    Checks if a given EMG signal value exceeds the activation threshold.

    Args:
        signal_value (float): Smoothed EMG signal value (e.g., RMS or envelope).
        threshold (float): Threshold above which actuation is triggered.

    Returns:
        bool: True if activation condition is met, False otherwise.
    """
    return signal_value > threshold

# Example usage:
# smoothed_value = 0.62  # From envelope detector
# if detect_activation(smoothed_value, threshold=0.5):
#     print("Activate actuator")
