from django.http import HttpResponse
from django.shortcuts import render
from myformsapp import *

def Cuerpo(request):
    return render(request, 'myformsapp/base.html')

def Inicio(request):
    return render(request, 'myformsapp/inicio.html')

def Catalogo(request):
    return render(request, 'myformsapp/catalogo.html')

def Fcontacto(request):
    return render(request, 'myformsapp/formularioContacto.html')

def Mcontacto(request):
    contacto="Mensaje enviado: %r" %request.get["msje"]
    return HttpResponse(contacto)
