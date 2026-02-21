from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def home(request):
    clientes = Cliente.objects.all().order_by('-id')
    total_clientes = clientes.count()
    ultimos_clientes = clientes[:5]

    context = {
        'total_clientes': total_clientes,
        'ultimos_clientes': ultimos_clientes,
    }

    return render(request, 'home.html', context)


def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, 'clientes/lista_cliente.html', {'clientes': clientes})


def cadastrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'clientes/cadastra_cliente.html', {'form': form})