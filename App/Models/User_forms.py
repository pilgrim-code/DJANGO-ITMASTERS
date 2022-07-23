from django import forms

class SignUpForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    usuario = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Email')
    contra = forms.CharField(widget=forms.PasswordInput)
    
    