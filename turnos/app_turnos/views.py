from django.http import HttpRequest
from ast import Return
from django.shortcuts import render
from app_turnos.models import Turno, Cliente, Profesionales
from django.template import Template, loader
from app_turnos.forms import Alta_turno, Alta_cliente, Alta_profesionales

# Create your views here.

def template(request):

    return render( request , "template.html" )

def inicio(request):

    return render( request , "index.html" )

def contacto(request):

    return render( request , "contacto.html" )

#LISTADO DE TURNOS
def lista_turno(request):
    turno = Turno.objects.all()
    datos = {"datos" : turno}

    return render(request , "lista_turno.html" , datos)
    
     
#LISTADO DE Clientes
def lista_cliente(request):
    cliente = Cliente.objects.all()
    datos = {"datos" : cliente}

    return render(request , "lista_cliente.html" , datos)     

#LISTADO DE Profesionales
def lista_profesionales(request):
    profesionales = Profesionales.objects.all()
    datos = {"datos" : profesionales}

    return render(request , "lista_profesionales.html" , datos)         

#ALTAS: 

def alta_turno(request):

    if request.method == "POST":

        mi_formulario = Alta_turno( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            turno = Turno(nombre=request.POST['nombre'], domicilio=request.POST['domicilio'])
            turno.save()

            return render( request , "alta_turno.html")

    return render( request, "alta_turno.html")   

def alta_cliente(request):

    if request.method == "POST":
        mi_formulario = Alta_cliente(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        cliente = Cliente(nombre=request.POST['nombre'], dni=request.POST['dni'], telefono=request.POST['telefono'], domicilio=request.POST['domicilio'], email=request.POST['email'])
        cliente.save()
     
        return render(request, "alta_cliente.html")
    return render( request, "alta_cliente.html")  

def alta_profesionales(request):

    if request.method == "POST":
        mi_formulario = Alta_profesionales(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        profesionales = Profesionales(nombre=request.POST['nombre'], telefono=request.POST['telefono'], turno=request.POST['turno'])
        profesionales.save()
     
        return render(request, "alta_profesionales.html")
    return render( request, "alta_profesionales.html") 

 #Buscar
 
def buscar_turno(request):

    return render( request , "buscar_turno.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        turno = Turno.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"turno": turno})
    else:
        return HttpResponse("Campo vacio")   