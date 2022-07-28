from tkinter.messagebox import NO
from django.shortcuts import render,HttpResponse
from App.Models.Cursos_models import Cursos_models
from django.http import HttpResponseRedirect
from ..models import CompraProducto
from datetime import date
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

class CursosController():
    def index(request):
        filtrar = None
        if request.method == 'POST':
            filtrar = request.POST.get('filtrar')
        cursos_list =  Cursos_models.cursos_list(filtrar)
        paginator = Paginator(cursos_list,2)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {'cursos_list': items}
        return render(request, 'views/productos/productos.html',context)
    def details(request,cursoid):
        objects = Cursos_models.getid(cursoid)
        context = {'curso': objects}
        return render(request,'views/productos/details.html',context)
    def obtener_curso(request):
        if request.method== 'POST':
            if request.user.is_authenticated:
                cursoid=request.POST['cursoid']
                user = request.user.id
                model = CompraProducto(
                    CursoId=cursoid,
                    IdCliente=user,
                    Fecha=date.today()
                )
                model.save()
                return HttpResponseRedirect('mis_productos')
            else:
                return HttpResponseRedirect('admin')
    
   
            
    def mis_productos(request):
        filtrar = None
        if request.method == 'POST':
            filtrar = request.POST.get('filtrar')
        productos_list = Cursos_models.mis_productos_list(request,filtrar)
        paginator = Paginator(productos_list,2)
        page = request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context = {
            'items': items,
        }
        return render(request,'views/productos/mis_productos.html',context)
                