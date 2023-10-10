from django.shortcuts import render,redirect
from persona.models import Persona
from persona.forms import PersonaForm
# Create your views here.

def nuevaPersona(request):
    if request.method=='POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect("ListadoPersonas")

    else:
        formaPersona=PersonaForm()
    return render(request,"nuevo.html",{'formaPersona':formaPersona})