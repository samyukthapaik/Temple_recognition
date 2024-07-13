# recognition/models.py

from django.db import models
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

class MonumentImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='monument_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')  # Example: binary classification
    ])
    
    return model
