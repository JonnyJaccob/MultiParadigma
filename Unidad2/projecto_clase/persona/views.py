from django.shortcuts import render,redirect, get_object_or_404
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

def editarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('ListadoPersonas')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request,"editarPersona.html",{"formaPersona":formaPersona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
    return redirect("ListadoPersonas")

def detallePersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,"detallePersona.html",{"persona":persona})