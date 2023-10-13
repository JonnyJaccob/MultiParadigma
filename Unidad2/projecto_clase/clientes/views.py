from django.shortcuts import render,redirect
from clientes.models import Cliente
from clientes.forms import clienteForm
# Create your views here.
def indexClientes(request):
    clientes = Cliente.objects.order_by("id")
    return render(request,"ListadoClientes.html",{"clientes":clientes})

def agregarCliente(request):
    if request.method=='POST':
        formaCliente = clienteForm(request.POST)
        if formaCliente.is_valid():
            formaCliente.save()
            return redirect("indexCliente")
    else:
        formaCliente=clienteForm()
    return render(request,"nuevo.html",{'formaPersona':formaCliente})