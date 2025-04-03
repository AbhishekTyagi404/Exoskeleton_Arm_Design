# emg_cnn_classifier.py
# Future Module: EMG Pattern Classification using CNN
# Author: Abhishek Tyagi

import numpy as np
import tensorflow as tf

def load_model(model_path="cnn_emg_model"):
    """
    Loads a pre-trained CNN model from the given directory path.
    The model must be in TensorFlow's 'SavedModel' format.
    
    Args:
        model_path (str): Path to the directory containing the saved model.
    
    Returns:
        tensorflow.keras.Model: Loaded CNN model.
    """
    try:
        model = tf.keras.models.load_model(model_path)
        print(f"[INFO] Model loaded from: {model_path}")
        return model
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        return None

def predict_emg_class(model, emg_segment):
    """
    Predicts the EMG class label from a processed EMG signal segment.

    Args:
        model (tensorflow.keras.Model): Loaded CNN model.
        emg_segment (np.ndarray): 1D EMG signal window (e.g., 200–500 samples).

    Returns:
        int: Predicted class index.
    """
    if model is None:
        raise ValueError("Model is not loaded.")

    # Reshape: [batch_size, time_steps, channels]
    emg_input = np.expand_dims(emg_segment, axis=(0, -1))
    prediction = model.predict(emg_input, verbose=0)
    class_idx = np.argmax(prediction)
    return class_idx

# Example usage:
# model = load_model("cnn_emg_model")
# class_index = predict_emg_class(model, emg_segment_array)
# print("Predicted class:", class_index)
