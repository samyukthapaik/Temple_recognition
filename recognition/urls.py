from django.urls import path
from . import views

urlpatterns = [
    #path('upload/', views.upload_image, name='upload'),# This defines the URL as 'upload/'
    path('upload/', views.upload_image, name='upload_image'),
    path('results/', views.results, name='results'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('upload_multiple/', views.upload_multiple_images, name='upload_multiple_images'),  
]




