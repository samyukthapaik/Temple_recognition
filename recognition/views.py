from django.shortcuts import render
from .forms import MonumentImageForm
from .utils import predict  # Ensure predict function is imported correctly
from django.http import HttpResponse
from .models import MonumentImage


# recognition/views.py

from django.shortcuts import render
from django.http import HttpResponse

# def upload_image(request):
#     # Your view logic for uploading images
#     return HttpResponse("Upload Image View")

def add_training_image(request):
    # Your view logic for adding training images
    return HttpResponse("Add Training Image View")

def upload_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        monument_image = MonumentImage(image=uploaded_file)
        monument_image.save()
        return HttpResponse("Image uploaded successfully!")
    return render(request, 'recognition/upload_image.html')

