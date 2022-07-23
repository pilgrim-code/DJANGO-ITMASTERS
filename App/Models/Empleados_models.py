from django.db import models
from ..models import Equipo
class Empleados_models():
    def empleados_list():
        empleados = Equipo.objects.order_by('NombreE')
        return empleados