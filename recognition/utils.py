import tensorflow as tf
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np

# Load the TensorFlow model
def load_model():
    model = tf.keras.models.load_model('ml_model/temple_model.h5')
    return model

# Function to preprocess image and make predictions
def predict(image_path):
    model = load_model()
    
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.  # Normalize pixel values to [0, 1]
    
    # Make prediction
    predictions = model.predict(img_array)
    
    # Assuming your model predicts a class, you might want to return class probabilities or labels
    # Modify this according to your model's output
    return predictions
