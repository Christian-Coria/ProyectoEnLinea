from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib import admin
from servicio_tecnico.views import ( buscar, ListarClientes,
CrearCliente, CrearProveedor, EliminarCliente, EditarCliente,EditarProveedor,EliminarProveedor,
MostrarCliente,MostrarProveedor,ListarProveedores, EliminarIngreso, 
MostrarIngreso,EditarIngreso,CrearIngreso, ListarIngresos, ClienteMin, CheckImei,Actualizacion,)



urlpatterns = [
      
    path('listar-clientes' , ListarClientes.as_view(), name='listar_clientes'),
    path('listar-proveedores' , ListarProveedores.as_view(), name='listar_proveedores'),
    path('listar-ingresos' , ListarIngresos.as_view(), name='listar_ingresos'),

    path('buscar/', buscar, name="buscar"),
  

    path('presupuesto' , ClienteMin.as_view(), name='presupuesto'),
    path('chreck_imei' , CheckImei.as_view(), name='check_imei'),
    path('actualizacion_precios' , Actualizacion.as_view(), name='actualizacion_precios'),


    
    path('crear-cliente' , CrearCliente.as_view(), name='crear_cliente'),                
    path('crear-proveedor' , CrearProveedor.as_view(), name='crear_proveedor'),    
    path('crear-ingreso' , CrearIngreso.as_view(), name='crear_ingreso'), 

    path('eliminar-cliente/<int:pk>' , EliminarCliente.as_view(), name='eliminar_cliente'),
    path('eliminar-proveedor<int:pk>' , EliminarProveedor.as_view(), name='eliminar_proveedor'),
    path('eliminar-ingreso<int:pk>' , EliminarIngreso.as_view(), name='eliminar_ingreso'),

    path('editar-cliente/<int:pk>' , EditarCliente.as_view(), name='editar_cliente'),
    path('editar-proveedor/<int:pk>' , EditarProveedor.as_view(), name='editar_proveedor'),
    path('editar-ingreso/<int:pk>' , EditarIngreso.as_view(), name='editar_ingreso'),
    
    path('mostrar-cliente/<int:pk>/' , MostrarCliente.as_view(), name='mostrar_cliente'),
    path('mostrar-proveedor/<int:pk>/' , MostrarProveedor.as_view(), name='mostrar_proveedor'),
    path('mostrar-ingreso/<int:pk>/' , MostrarIngreso.as_view(), name='mostrar_ingreso'),
    
]

