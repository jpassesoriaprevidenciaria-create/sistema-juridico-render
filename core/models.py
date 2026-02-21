from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='processos')
    numero = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Em andamento')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero} - {self.cliente.nome}"