from django.contrib import admin
from .models import Jogo,Sorteio,Contas,Deposito,Cliente,Saque
#, Jogador, Categoria

# Register your models here.
admin.site.register(Jogo)
admin.site.register(Sorteio)
admin.site.register(Contas)
admin.site.register(Deposito)
admin.site.register(Cliente)
admin.site.register(Saque)

#admin.site.register(Categoria)
