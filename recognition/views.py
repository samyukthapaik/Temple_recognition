from django.shortcuts import render
from .forms import MonumentImageForm
from .utils import predict  # Ensure predict function is imported correctly
from django.http import HttpResponse
from .models import MonumentImage
from django.shortcuts import render, redirect
import os

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


def upload_image(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        monument_image = MonumentImage(image=uploaded_image)
        monument_image.save()

        try:
            predicted_class, confidence = predict(monument_image.image.path)

            # Add your architecture detection logic here
            description = f"Detected architecture is a {predicted_class} with {confidence:.2f} confidence."

            monument_image.predicted_class = predicted_class
            monument_image.confidence = confidence
            monument_image.description = description
            monument_image.save()
        except FileNotFoundError as e:
            return HttpResponse(f"Error: {e}", status=500)
        except OSError as e:
            return HttpResponse(f"Error: {e}", status=500)

        return render(request, 'recognition/results.html', {'images': [monument_image]})
    return render(request, 'recognition/upload_image.html')

def results(request):
    images = MonumentImage.objects.all()
    return render(request, 'recognition/results.html', {'images': images})

def about_us(request):
    return render(request, 'recognition/about_us.html')

def contact_us(request):
    return render(request, 'recognition/contact_us.html')

