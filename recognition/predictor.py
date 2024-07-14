import tensorflow as tf
import os

def get_model():
    # Define the path to your model file
    model_path = r'F:\fsd\temple_recognition\temple_recognition\recognition\ml_model\temple_model.h5'
    
    # Check if the file exists
    if os.path.isfile(model_path):
        # Load the model
        model = tf.keras.models.load_model(model_path)
        return model
    else:
        raise FileNotFoundError(f"Model file not found at {model_path}")

def predict(image_path):
    model = get_model()
    
    # Load and preprocess the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to [0, 1]
    
    # Make prediction
    predictions = model.predict(img_array)
    
    # Assuming your model predicts a class, adjust this according to your model's output
    class_names = ['Class1', 'Class2', 'Class3']  # Replace with your actual class names
    predicted_class = class_names[tf.argmax(predictions[0])]
    confidence = tf.reduce_max(predictions[0]).numpy()

    return predicted_class, confidence
