from django.shortcuts import render

# Create your views here.
def indexPersona(request):
    # Tu lógica de vista aquí
    return render(request, 'indexPersona.html', context)