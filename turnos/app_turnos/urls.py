from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.inicio, name="inicio"),
    path("template/" , views.template),
    path("contacto" , views.contacto, name="contacto"),
    path("lista_turno" , views.lista_turno, name="lista_turno"),
    path("alta_turno" , views.alta_turno, name="alta_turno"),
    path("alta_cliente" , views.alta_cliente, name="alta_cliente"),
    path("alta_profesionales" , views.alta_profesionales, name="alta_profesionales"),
    path("lista_cliente" , views.lista_cliente, name="lista_cliente"),
    path("lista_profesionales" , views.lista_profesionales, name="lista_profesionales"),
    path("buscar_turno" , views.buscar_turno, name="buscar_turno"), 
    path("buscar" , views.buscar, name="buscar")

    
  

]
