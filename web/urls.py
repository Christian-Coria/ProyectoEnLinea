from django.urls import path
from web.views import home
from web.views import Contacto
from web.views import About
from web.views import Construccion
from web.views import Construccion
from web.views import preguntas_frecuentes

urlpatterns = [
    path('',home, name="index"),  
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),
    path('en_construccion/', Construccion.as_view(), name="en_construccion"),
    path('preguntas_frecuentes/', preguntas_frecuentes, name="preguntas_frecuentes"),
   
]