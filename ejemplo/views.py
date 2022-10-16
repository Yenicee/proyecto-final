from http.client import ImproperConnectionState
from django.shortcuts import render

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
    imc= 1 #calcular esto
    return render(request, "ejemplo/imc.html", {"imc":imc}) 
    




