from django.contrib.auth.decorators import login_required
from django.shortcuts import render
class PerfilController():
    @login_required
    def perfil(request):
        return render(request,'views/perfil/perfil.html')