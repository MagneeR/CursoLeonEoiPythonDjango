from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Esto se refiere a lo que se vera en el navegador

def index(request):
    return HttpResponse("Buenas, aqui empieza todo")