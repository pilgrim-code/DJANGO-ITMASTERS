from tkinter import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App.Models.Perfil_forms import ImageForm
class PerfilController():
    @login_required
    def perfil(request):
        context = {
            'imageForm': ImageForm()
        }
        
        return render(request,'views/perfil/perfil.html',context)