from django.db import models
from ..models import Cursos,Categorias,CompraProducto
class Cursos_models():
    def cursos_list(filtrar):
        if filtrar == None:
            cursos = Cursos.objects.order_by('Nombre')
        else:
            cursos = Cursos.objects.filter(Nombre__contains=filtrar)
       
        return cursos
    def getid(idcurso):
        curso = Cursos.objects.get(CursoId=idcurso)
        #for item in curso:
         
         #   categoria = Categorias.objects.get(CategoriaID=item.CategoriaID.CategoriaID)
        return curso
    def mis_productos_list(request,filtrar):
        i=0
        inscripcion = CompraProducto.objects.filter(IdCliente=request.user.id)
        producto = [[]] *len(inscripcion)
        for item in inscripcion:
            producto[i] = Cursos.objects.get(CursoId=item.CursoId)
            i+=1
        if not filtrar:
            return producto
        else:
            return list(filter(lambda x:x.Nombre.startswith(filtrar.lstrip()),producto))
        