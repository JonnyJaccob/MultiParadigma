from django.shortcuts import render
from persona.models import Persona

# Create your views here.
def index(request):
    return render(request,'bienvenido.html') 

def indexPersona(request):
    noPersonas = Persona.objects.count()
    personas = Persona.objects.order_by('id')
    #print(personas)
    return render(request,'indexPersona.html',
                  {"personas":personas,"count":noPersonas})#igual al nombre puesto en el for
 