# 📊 EMG Processed Data

This folder contains example EMG signal data generated for visualization, validation, and system testing.

## 🧾 File: `emg_processed_data.csv`

| Column Name | Description |
|-------------|-------------|
| `time_s`    | Time in seconds |
| `raw_emg`   | Original EMG signal with noise |
| `filtered`  | Bandpass filtered EMG (20–450 Hz) |
| `smoothed`  | Envelope signal from moving average |
| `activation`| Binary value (1 if signal > threshold) |

This data can be used to:
- Test activation threshold detection logic
- Train and evaluate signal classification models
- Simulate EMG-driven actuator control in the exoskeleton

## 📷 Associated Visualizations

Visuals from this dataset are saved in the `images/` folder:

- `emg_plot_raw.png` – Raw EMG waveform  
- `emg_plot_filtered.png` – Bandpass filtered EMG  
- `emg_plot_envelope.png` – Smoothed signal + activation zones

