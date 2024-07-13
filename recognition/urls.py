from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload'),  # This defines the URL as 'upload/'
    # Add more URLs as needed for your application
]
