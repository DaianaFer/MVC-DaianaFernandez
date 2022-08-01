from contextvars import Context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template
from .models import Familia


def familia(request):
    return HttpResponse("Bienvenidos a mi registro Familiar")

def familia1(request):
    familia2 = Familia.objects.all()
    segunda_linea = open(r"C:\Users\MSI GX70\Desktop\Django MVC\MVCDaianaFernandez\FamilyApp\models.py","r")    
    plantilla = Template(segunda_linea.read())
    segunda_linea.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
    