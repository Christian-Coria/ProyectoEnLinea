from django.urls import path
from web.views import home
from web.views import Contacto
from web.views import About


urlpatterns = [
    path('',home, name="index"),  
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('about/', About.as_view(), name="about"),
   
]