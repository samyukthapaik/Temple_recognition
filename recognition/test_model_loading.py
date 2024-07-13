import tensorflow as tf

model_path = 'F:/fsd/TEMPLE_RECOGNITION/temple_recognition/ml_model/temple_model.h5'
try:
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
