from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request,'index.html')

class Contacto(TemplateView):
    template_name = "contacto.html"

class About(TemplateView):
    template_name = "about.html"

class Construccion(TemplateView):
    template_name = "en_construccion.html"
