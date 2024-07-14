# ml_model/train_model.py
# from xml.parsers.expat import model
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# # Load and preprocess data, create and train the model...
# # Save the model
# model.save('ml_model/temple_model.h5')

import tensorflow as tf

# Assuming the model path is one directory above in 'ml_model'
model_path = '../ml_model/temple_model.h5'

try:
  # Check for specific error (FileNotFoundError)
  model = tf.keras.models.load_model(model_path)
  print("Model loaded successfully from:", model_path)
except FileNotFoundError as e:
  print(f"Error: Model file not found at {model_path}")

