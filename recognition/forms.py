# recognition/forms.py

from django import forms
from .models import MonumentImage

class MonumentImageForm(forms.ModelForm):
    class Meta:
        model = MonumentImage
        fields = ['title', 'image', 'description']
