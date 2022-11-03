from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11) 
    telefone = models.CharField(max_length=20)
    data_nasc = models.DateField()
    

    def __str__(self):
        return self.cliente

class Contas(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=6)
    saldo = models.DecimalField(decimal_places=2, max_digits=30, default=0.00)
    ultima_movimentacao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{str(self.agencia)}'

    def get_ultima_movimentacao(self):
        return self.ultima_movimentacao.strftime('%d/%m/%Y %H:%M')


class Deposito(models.Model):
    conta = models.ForeignKey('Contas', on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    data_deposito = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.conta)}'

    def get_data_deposito(self):
        return self.data_deposito.strftime('%d/%m/%Y %H:%M')

@receiver(post_save, sender=Deposito)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo += instance.valor
    instance.conta.save()


class Saque(models.Model):
    conta = models.ForeignKey('Contas', on_delete=models.CASCADE)
    chave_pix = models.CharField(max_length=80)
    valor = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    data_deposito = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.conta)}'

    def get_data_deposito(self):
        return self.data_deposito.strftime('%d/%m/%Y %H:%M')

@receiver(post_save, sender=Saque)
def update_saldo(sender, instance, **kwargs):
    instance.conta.saldo -= instance.valor
    instance.conta.save()


class Sorteio(models.Model):
    data = models.DateField(auto_now_add=True)
    numeros = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.data} - {str(self.numeros)}'


class Jogo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    numeros = models.CharField(max_length=120)


    def __str__(self):
        return f'{self.data} - {str(self.numeros)}'
