from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from vistaprevia.models import Producto



def index(request):
    params = {}
    params['nombre_sitio'] = 'EnLinea'
    producto=Producto.objects.filter( Q(estado="Publicado"), )
    params['producto']=producto
    print(producto)
    return render(request, 'web/index.html', params)