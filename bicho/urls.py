from django.urls import path
from . import views 

urlpatterns = [
    path('', views.escolhar_bicho, name='index_bicho'),
    path('', views.escolhar_bichos, name='index_bicho'),
    #path('jogo/', views.jogo, name="jogo"),
    #path('sistema/', views.sistema, name="sistema"),
    path('sorteio/', views.sorteio, name="sorteio"),
    
]