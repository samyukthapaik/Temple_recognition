# ml_model/train_model.py
from xml.parsers.expat import model
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load and preprocess data, create and train the model...
# Save the model
model.save('ml_model/temple_model.h5')
