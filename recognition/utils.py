# import tensorflow as tf
# from tensorflow.keras.preprocessing import image # type: ignore
# import numpy as np
# import os
# from tensorflow.keras.models import load_model

# # Load the TensorFlow model
# def load_model():
#     model = tf.keras.models.load_model('ml_model/temple_model.h5')
#     return model

# # Function to preprocess image and make predictions
# def predict(image_path):
#     model = load_model()
    
#     # Load and preprocess the image
#     img = image.load_img(image_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.  # Normalize pixel values to [0, 1]
    
#     # Make prediction
#     predictions = model.predict(img_array)
    
#     # Assuming your model predicts a class, you might want to return class probabilities or labels
#     # Modify this according to your model's output
#     return predictions
#-------------------------------------------------------------

# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os

# # Function to load the model
# def load_model():
#     model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'temple_model.h5')
#     if os.path.isfile(model_path):
#         model = tf.keras.models.load_model(model_path)
#         return model
#     else:
#         raise FileNotFoundError(f"Model file not found at {model_path}")

# # Function to preprocess image and make predictions
# def predict(image_path):
#     model = load_model()
    
#     # Load and preprocess the image
#     img = image.load_img(image_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0  # Normalize pixel values to [0, 1]
    
#     # Make prediction
#     predictions = model.predict(img_array)
    
#     # Assuming your model predicts a class, you might want to return class probabilities or labels
#     # Modify this according to your model's output
#     class_names = ['Class1', 'Class2', 'Class3']  # Update with your actual class names
#     predicted_class = class_names[np.argmax(predictions[0])]
#     confidence = np.max(predictions[0])

#     return predicted_class, confidence 
#--------------------------------------------------------------
# import tensorflow as tf
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os

# # Function to load the model
# def get_model():
#     model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'temple_model.h5')
#     if os.path.isfile(model_path):
#         model = tf.keras.models.load_model(model_path)
#         return model
#     else:
#         raise FileNotFoundError(f"Model file not found at {model_path}")

# # Function to preprocess image and make predictions
# def predict(image_path):
#     model = get_model()
    
#     # Load and preprocess the image
#     img = image.load_img(image_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0  # Normalize pixel values to [0, 1]
    
#     # Make prediction
#     predictions = model.predict(img_array)
    
#     # Assuming your model predicts a class, you might want to return class probabilities or labels
#     # Modify this according to your model's output
#     class_names = ['Class1', 'Class2', 'Class3']  # Update with your actual class names
#     predicted_class = class_names[np.argmax(predictions[0])]
#     confidence = np.max(predictions[0])

#     return predicted_class, confidence
#===================================================
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

def convert_to_grayscale(image_path):
    image = Image.open(image_path).convert('L')
    return np.array(image)


# utils.py
def load_temple_model():
    model_path = 'F:/fsd/temple_recognition/temple_recognition/recognition/ml_model/temple_model.h5'
    model = load_model(model_path)
    return model



