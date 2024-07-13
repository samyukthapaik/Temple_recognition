from django.shortcuts import render
from .forms import MonumentImageForm
from .utils import predict  # Ensure predict function is imported correctly
from django.http import HttpResponse
from .models import MonumentImage
from django.shortcuts import render, redirect


# recognition/views.py

from django.shortcuts import render
from django.http import HttpResponse

# def upload_image(request):
#     # Your view logic for uploading images
#     return HttpResponse("Upload Image View")

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

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        monument_image = MonumentImage(image=image)
        monument_image.save()

        # Image recognition logic
        predicted_class, confidence = predict(monument_image.image.path)

        # Save the prediction results in the MonumentImage model
        monument_image.predicted_class = predicted_class
        monument_image.confidence = confidence
        monument_image.save()

        return redirect('results')
    return render(request, 'recognition/upload_image.html')

def results(request):
    images = MonumentImage.objects.all()
    return render(request, 'recognition/results.html', {'images': images})

def about_us(request):
    return render(request, 'recognition/about_us.html')

def contact_us(request):
    return render(request, 'recognition/contact_us.html')

