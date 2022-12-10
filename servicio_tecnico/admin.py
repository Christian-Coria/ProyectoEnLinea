from django.contrib import admin
from servicio_tecnico.models import Cliente
from servicio_tecnico.models import Reparacion
from servicio_tecnico.models import Proveedores
from servicio_tecnico.models import TareasPendientes

class ReparacionInLine(admin.TabularInline):
    model = Reparacion
    extra = 0 #indicamos la cantidad que podemos agregar

class ClienteAdmin(admin.ModelAdmin): #esta clase customiza ... asocia las clases
    inlines = [ReparacionInLine]

@admin.register(Reparacion)    #el decorador reemplaza al registro:   admin.site.register(Reparacion,ReparacionAdmin )
class ReparacionAdmin(admin.ModelAdmin):   #Filtro para el panel de administracion y mostrar lo que se decida en el orden que se elija
     #fields = ['categoria', 'fecha_publicacion', 'nombre', 'imagen']
     fieldsets = [
         ("Relacion", {"fields": ["cliente"]}),
         ("Datos generales", 
              {"fields": 
                  ['marca', 'modelo' ,'imei',
                     'falla', 'imagen' ,'comentarios',
                      'precio', 'estado'
                  ]}

         )
     ]

     list_display = ['id','fecha','cliente','modelo', 'tipo_de_reparacion', 'upper_case_name'] #visualizamos en forma de columnas - pisamos el metodo __str__
     ordering = ['-fecha']    #ordenamos por fecha de publicacion en este caso el signo menos es para alterar el orden natural
     list_filter = ('cliente', 'fecha',) # list_filter es una tupla que permite filtrar
     search_fields = ('imei', 'estado', 'modelo', 'cliente',) # search_fields agrega opciones de busquedas
     list_display_links = ('cliente', 'fecha',) #agrega links a cada columna para ingreso por click
    
     @admin.display(description='Name')  #customizamos el panel con una logica ... en este caso cambia a mayuscula los objetos
     def upper_case_name(self, obj):
         return ("%s %s" % (obj.falla, obj.precio)).upper() # pasamos a mayuscula el nombre y el estado







admin.site.register(Cliente,ClienteAdmin)

#admin.site.register(Reparacion,ReparacionAdmin )
admin.site.register(Proveedores)
admin.site.register(TareasPendientes)