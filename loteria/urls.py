from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index_loteria'),
    path('create_user/', views.create_user, name='create_user'),
    path('autenticar_usuario/', views.autenticar_usuario, name='autenticar_usuario'),
    path('cadastrar_cli/', views.cadastrar_cli, name='cadastrar_cli'),
    path('login_user/', views.login_user, name='login_user'),
    path('logaut_user/', views.logaut_user, name='logaut_user'),
    path('processa_formulario/', views.processa_formulario, name="processa_formulario"),
    #path('get_name/', views.get_name, name="get_name"),
    path('listar_jogo/', views.listar_jogo, name="listar_jogo"),
    path('sistema/', views.sistema, name="sistema"),
    path('sorteio/', views.sorteio, name="sorteio"),
    path('contas/', views.contas, name="contas"),
    path('criar_conta/', views.criar_conta, name="criar_conta"),
    path('listar_saldo/', views.listar_saldo, name="listar_saldo"),
    path('conta/', views.conta, name="conta"),
    path('depositos/', views.depositos, name="depositos"),
    path('deposito/', views.deposito, name="deposito"),
    path('saques/',views.saques, name="saques"),
    path('saque/',views.saque, name="saque"),


    path('jogo/', views.jogo, name="jogo"),
]