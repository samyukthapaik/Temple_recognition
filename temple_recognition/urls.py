
from django.urls import include, path
from recognition import views
from django.contrib import admin  # Adjust this import if your structure is different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload'),
    path('recognition/', include('recognition.urls')),
    path('add_training_image/', views.add_training_image, name='add_training_image'),
    path('results/', views.results, name='results'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    ]




