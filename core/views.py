from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def home(request):
    total_clientes = Cliente.objects.count()
    ultimos_clientes = Cliente.objects.all().order_by('-id')[:5]

    context = {
        'total_clientes': total_clientes,
        'ultimos_clientes': ultimos_clientes,
    }

    return render(request, 'home.html', context)