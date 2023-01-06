from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DateDetailView
from django.views.generic import ListView, DetailView, TemplateView, View
from servicio_tecnico.models import  Task, Proveedores,Cliente,Reparacion 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.core.paginator import Paginator



def buscar(request):

    if 'q' in request.GET:
        q = request.GET['q']
        all_reparacion_list = Reparacion.objects.filter(Q(cliente__nombre_completo__icontains=q)).order_by('cliente')
        
    else:
        all_reparacion_list = Reparacion.objects.all().order_by('cliente')                
        
    return render(request, 'servicio_tecnico/buscar.html', {"reparacion":all_reparacion_list})


class ClienteMin(TemplateView):
    template_name = "presupuesto.html"

class Actualizacion(TemplateView):
    template_name = "actualizacion.html"

class CheckImei(TemplateView):
    template_name = "chrck_imei.html"


class ListarClientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "servicio_tecnico/listar_clientes.html"


class CrearCliente(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "servicio_tecnico/crear_cliente.html"
    success_url = 'listar-clientes'
    fields = ['nombre_completo','telefono']


class EditarCliente(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name ='servicio_tecnico/editar_cliente.html'
    success_url = reverse_lazy('listar_clientes')
    fields = ['nombre_completo','telefono']  


class EliminarCliente(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "servicio_tecnico/eliminar_cliente.html"
    success_url = reverse_lazy('listar_clientes')


class ListarIngresos(LoginRequiredMixin, ListView):
    model = Reparacion
    template_name = "servicio_tecnico/listar_ingresos.html"


class CrearIngreso(LoginRequiredMixin,CreateView):
    model = Reparacion
    template_name = "servicio_tecnico/crear_ingreso.html"
    success_url = 'listar-ingresos'
    fields = ['cliente','whatsApp','marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'pago_seña','precio', 'estado']


class EditarIngreso(LoginRequiredMixin,UpdateView):
    model = Reparacion
    template_name = 'servicio_tecnico/editar_ingreso.html'
    success_url = reverse_lazy('listar_ingresos')
    fields = ['cliente','marca','modelo', 'imei', 'falla',
    'imagen', 'comentarios', 'presupuesto' ,'pago_seña','precio', 'estado']

class EliminarIngreso(LoginRequiredMixin,DeleteView):
    model = Reparacion
    template_name = "servicio_tecnico/eliminar_ingreso.html"
    success_url = reverse_lazy('listar_ingresos')


class MostrarCliente(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = 'servicio_tecnico/mostrar_cliente.html'
    

class MostrarProveedor(LoginRequiredMixin,DetailView):
    model = Proveedores
    template_name = "servicio_tecnico/mostrar_proveedor.html"
    

class MostrarIngreso(LoginRequiredMixin,DetailView):
    model = Reparacion
    template_name = "servicio_tecnico/mostrar_ingreso.html"


class ListarProveedores(LoginRequiredMixin,ListView):
    model = Proveedores
    template_name = "servicio_tecnico/listar_proveedores.html"
    context_object_name = 'proveedores'


class CrearProveedor(LoginRequiredMixin,CreateView):
    model = Proveedores
    template_name = "servicio_tecnico/crear_proveedor.html"
    success_url = 'listar-proveedores'
    fields = ['nombre','telefono']


class EditarProveedor(LoginRequiredMixin,UpdateView):
    model = Proveedores
    template_name = "servicio_tecnico/editar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')
    fields = ['nombre','telefono']

class EliminarProveedor(LoginRequiredMixin,DeleteView):
    model = Proveedores
    template_name = "servicio_tecnico/eliminar_proveedor.html"
    success_url = reverse_lazy('listar_proveedores')

