from django import forms
from ..models import Perfil

class ImageForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['image']
    