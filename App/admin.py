from django.contrib import admin
from django.utils.html import format_html
from .models import Cursos,Categorias,Equipo
# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Descripcion","Estado")
    search_fields = ('Nombre',)
    list_filter = ('Nombre', 'Estado')
    
admin.site.register(Categorias,CategoriasAdmin)

class CursosAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.Imagen != None:
           return format_html('<img width="85" height="45" src="/media/{}" />'.format(obj.Imagen))
        else:
           return format_html('<img width="85" height="85" src="/static/images/it.png" />')
       
    image_tag.short_description = 'Imagen'
    readonly_fields = ['image_tag']
    raw_id_fields = ('CategoriaID', )
    list_display = ('image_tag','Nombre','Descripcion','Costo','Estado')
    list_filter = ('Nombre', 'Estado')
    search_fields = ('Nombre','Descripcion' )

    pass


admin.site.register(Cursos,CursosAdmin)

class EquipoAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.Imagen != None:
           return format_html('<img width="85" height="45" src="/media/{}" />'.format(obj.Imagen))
        else:
           return format_html('<img width="85" height="85" src="/static/images/logo-google.png" />')
       
    image_tag.short_description = 'Imagen'
    readonly_fields = ['image_tag']
    list_display = ('image_tag','NombreE','Descripcion','Especialidad')
    list_filter = ('NombreE', 'Especialidad')
    search_fields = ('NombreE','Especialidad' )

    pass    
admin.site.register(Equipo,EquipoAdmin)
