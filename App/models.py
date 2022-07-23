from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categorias(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    Estado = models.BooleanField()

class Cursos(models.Model):
    CursoId = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True,upload_to='images/curso')
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
  #  Horas= models.IntegerField(default=0)
    Costo =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Estado = models.BooleanField()
    CategoriaID = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)    

class Equipo(models.Model):
    EId = models.AutoField(primary_key=True)
    Imagen = models.ImageField(null=True,upload_to='images/personal')
    NombreE = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=300)
    Especialidad = models.CharField(max_length=30)

class CompraProducto(models.Model):
    CursoId = models.IntegerField(default=0)
    IdCliente = models.IntegerField(default=0)
    Fecha = models.CharField(max_length=20)
    Resumen = models.TextField(default='')
'''
class Bot(models.Model):
    IdBot = models.IntegerField(primary_key=True)
    NombreBot = models.CharField(max_length=20)
    FechaAgenda = models.DateField()
    CompilarInfo = models.CharField(max_length=30)
  
class Proyecto(models.Model):
    IdProyecto = models.IntegerField(primary_key=True)
    NombreProyecto = models.CharField(max_length=30)
    EmpleadoACargo = models.ForeignKey(Equipo, blank=True, null=True, on_delete=models.CASCADE)
    CategoriaID = models.ForeignKey(Categorias, blank=True, null=True, on_delete=models.CASCADE)  
    
class Avances(models.Model):
    IdAvance = models.IntegerField(primary_key=True)
    FechaActualizacion = models.DateField()
    GifAvance = models.ImageField(null=True,upload_to='images/avances')
    Descripcion = models.CharField(max_length=300)
'''
    
class Perfil(models.Model):
    perfilId = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    image = models.ImageField(null=True,upload_to='images/perfil')