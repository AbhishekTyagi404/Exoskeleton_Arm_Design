# emg_cnn_classifier.py
# Future Module: EMG Pattern Classification using CNN

import numpy as np
import tensorflow as tf

# Load pre-trained CNN model (saved_model format)
def load_model(model_path="cnn_emg_model"):
    return tf.keras.models.load_model(model_path)

# Predict EMG gesture from input signal
def predict_emg_class(model, emg_segment):
    emg_input = np.expand_dims(emg_segment, axis=(0, -1))  # [batch, time, 1]
    prediction = model.predict(emg_input)
    class_idx = np.argmax(prediction)
    return class_idx
