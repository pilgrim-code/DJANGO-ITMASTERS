from django.shortcuts import render
from App.Models.Empleados_models import Empleados_models
class EmpleadosController():
    def index(request):
        empleados_list =  Empleados_models.empleados_list()
        context = {'empleados_list': empleados_list}
        return render(request, 'views/index/about.html',context)