from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def contacto(request):
    return render(request,"contacto.html")

def recetas(request):
    return HttpResponse("<h1>Pagina de las recetas</h1>")

def top_10(request):
    return HttpResponse("<h1>Los postres mas vendidos</h1>")

def ofertas(request):
    return HttpResponse("<h1>OFERTONES</h1>")
