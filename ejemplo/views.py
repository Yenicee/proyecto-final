from http.client import ImproperConnectionState
from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html",
    {
     "nombre":"Yenice",
      "apellido":"Vazquez Perez"
    })


def index_dos(request, nombre, apellido):
    suma = 1+1
    return render(request, "ejemplo/saludar.html",
    {
        "nombre":"yenice",
        "apellido":suma,
    })

def index_tres(request):

    return render(request, "ejemplo/saludar.html",
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def imc(request, peso, altura):
    altura_en_metros = altura / 100
    peso_en_kilos= peso / 100
    imc = peso_en_kilos / altura_en_metros * altura_en_metros


    return render(request, "ejemplo/imc.html", {"imc":imc}) 

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})  
       


    




