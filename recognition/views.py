from django.shortcuts import render
from .forms import MonumentImageForm
#from .utils import predict  # Ensure predict function is imported correctly
from django.http import HttpResponse
from .models import MonumentImage
from django.shortcuts import render, redirect
import os
from django.core.files.storage import FileSystemStorage
from .predictor import predict  # Import the predict function from predictor.py
from tensorflow.keras.models import load_model
from .utils import load_temple_model  # Import your function to load the temple model
import traceback

def add_training_image(request):
    # Your view logic for adding training images
    return HttpResponse("Add Training Image View")

# def upload_image(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['image']
#         monument_image = MonumentImage(image=uploaded_file)
#         monument_image.save()
#         return HttpResponse("Image uploaded successfully!")
#     return render(request, 'recognition/upload_image.html')
# def results(request):
#     images = MonumentImage.objects.all()
#     return render(request, 'recognition/results.html', {'images': images})

# def upload_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         image = request.FILES['image']
#         monument_image = MonumentImage(image=image)
#         monument_image.save()

#         # Image recognition logic
#         predicted_class, confidence = predict(monument_image.image.path)

#         # Save the prediction results in the MonumentImage model
#         monument_image.predicted_class = predicted_class
#         monument_image.confidence = confidence
#         monument_image.save()

#         return redirect('results')
#     return render(request, 'recognition/upload_image.html')

# def results(request):
#     images = MonumentImage.objects.all()
#     return render(request, 'recognition/results.html', {'images': images})

# def about_us(request):
#     return render(request, 'recognition/about_us.html')

# def contact_us(request):
#     return render(request, 'recognition/contact_us.html')
#----------------------------------------------------------
# def upload_image(request):
#     if request.method == 'POST' and request.FILES['image']:
#         image = request.FILES['image']
#         monument_image = MonumentImage(image=image)
#         monument_image.save()

#         # Image recognition logic
#         predicted_class, confidence = predict(monument_image.image.path)

#         # Save the prediction results in the MonumentImage model
#         monument_image.predicted_class = predicted_class
#         monument_image.confidence = confidence
#         monument_image.save()

#         return redirect('results')
#     return render(request, 'recognition/upload_image.html')

# def results(request):
#     images = MonumentImage.objects.all()
#     return render(request, 'recognition/results.html', {'images': images})
#--------------------------------------------------------------------------------
# def upload_image(request):
#     if request.method == 'POST':
#         if 'image' in request.FILES:
#             image_file = request.FILES['image']
#             monument_image = MonumentImage(image=image_file)
#             monument_image.save()

#             # Predict the class and confidence
#             predicted_class, confidence = predict(monument_image.image.path)

#             # Save prediction results
#             monument_image.predicted_class = predicted_class
#             monument_image.confidence = confidence

#             # Add description logic here
#             if predicted_class == 'Pillar':
#                 monument_image.description = 'This is a pillar from the ancient temple architecture.'
#             elif predicted_class == 'Arch':
#                 monument_image.description = 'This is an arch commonly found in temple architecture.'
#             else:
#                 monument_image.description = 'This architectural feature is from a temple.'

#             monument_image.save()

#             return redirect('results')

#     return render(request, 'recognition/upload_image.html')
#------------------------------------------------------------------------


# def upload_image(request):
#     if request.method == 'POST':
#         uploaded_image = request.FILES['image']
#         monument_image = MonumentImage(image=uploaded_image)
#         monument_image.save()

#         try:
#             predicted_class, confidence = predict(monument_image.image.path)

#             # Add your architecture detection logic here
#             description = f"Detected architecture is a {predicted_class} with {confidence:.2f} confidence."

#             monument_image.predicted_class = predicted_class
#             monument_image.confidence = confidence
#             monument_image.description = description
#             monument_image.save()
#         except FileNotFoundError as e:
#             return HttpResponse(f"Error: {e}", status=500)
#         except OSError as e:
#             return HttpResponse(f"Error: {e}", status=500)

#         return render(request, 'recognition/results.html', {'images': [monument_image]})
#     return render(request, 'recognition/upload_image.html')

# def results(request):
#     images = MonumentImage.objects.all()
#     return render(request, 'recognition/results.html', {'images': images})

# def about_us(request):
#     return render(request, 'recognition/about_us.html')

# def contact_us(request):
#     return render(request, 'recognition/contact_us.html')

#==============================================================




def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        image_path = fs.path(filename)

        try:
            # Predict the class and confidence
            predicted_class, confidence = predict(image_path)

            # Save the image and prediction results
            monument_image = MonumentImage(image=image, predicted_class=predicted_class, confidence=confidence)
            monument_image.save()

            # Optionally add description logic based on predicted class
            if predicted_class == 'Pillar':
                monument_image.description = 'This is a pillar from the ancient temple architecture.'
            elif predicted_class == 'Arch':
                monument_image.description = 'This is an arch commonly found in temple architecture.'
            else:
                monument_image.description = 'This architectural feature is from a temple.'
            monument_image.save()

            return redirect('results')  # Redirect to results page after successful upload

        except FileNotFoundError as e:
            return render(request, 'error.html', {'error_message': f"Error: {e}"})
        except OSError as e:
            return render(request, 'error.html', {'error_message': f"Error: {e}"})

    return render(request, 'recognition/upload_image.html')

def upload_multiple_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        images = request.FILES.getlist('images')
        fs = FileSystemStorage()
        image_results = []
        
        for image in images:
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            image_path = fs.path(filename)
            
            try:
                # Predict the class and confidence
                predicted_class, confidence = predict(image_path)
                
                # Create a MonumentImage object and save prediction results
                monument_image = MonumentImage(image=image, predicted_class=predicted_class, confidence=confidence)
                monument_image.save()

                # Optionally add description logic based on predicted class
                if predicted_class == 'Pillar':
                    monument_image.description = 'This is a pillar from the ancient temple architecture.'
                elif predicted_class == 'Arch':
                    monument_image.description = 'This is an arch commonly found in temple architecture.'
                else:
                    monument_image.description = 'This architectural feature is from a temple.'
                monument_image.save()

                image_results.append({
                    'url': uploaded_file_url,
                    'predicted_class': predicted_class,
                    'confidence': confidence,
                    'description': monument_image.description  # Use saved description
                })

            except FileNotFoundError as e:
                return render(request, 'error.html', {'error_message': f"Error: {e}"})
            except OSError as e:
                return render(request, 'error.html', {'error_message': f"Error: {e}"})

        context = {
            'images': image_results,
        }
        return render(request, 'recognition/multiple_results.html', context)

    return render(request, 'recognition/upload_image.html')

def results(request):
    images = MonumentImage.objects.all()
    return render(request, 'recognition/results.html', {'images': images})

def about_us(request):
    return render(request, 'recognition/about_us.html')

def contact_us(request):
    return render(request, 'recognition/contact_us.html')

def predict_view(request):
    try:
        # Load the temple recognition model
        model = load_temple_model()

        # Example prediction logic
        # Replace this with actual prediction code based on your model's requirements
        prediction = model.predict(...)

        # Pass the prediction to the template
        return render(request, 'predict.html', {'prediction': prediction})

    except OSError as e:
        traceback.print_exc()
        error_message = f"Error loading model: {str(e)}"
        return render(request, 'error.html', {'error_message': error_message})

