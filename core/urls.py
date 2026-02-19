from django.urls import path
from .views import home, lista_clientes, cadastrar_cliente

urlpatterns = [
    path('', home, name='home'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('clientes/cadastrar/', cadastrar_cliente, name='cadastrar_cliente'),
]
