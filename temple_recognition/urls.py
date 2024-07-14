
from django.urls import include, path
from recognition import views
from django.contrib import admin  # Adjust this import if your structure is different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload'),
    path('recognition/', include('recognition.urls')),
    ]




