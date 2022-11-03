from django.shortcuts import render
from django.views.generic import View
from loteria.models import Sorteio


def home1(request):
    try:
        sorteios = Sorteio.objects.latest('numeros')
    except Sorteio.DoesNotExist:
        sorteios = {}
    return render(request, 'home1.html',{'sorteios':sorteios})

class HomeView(View):
    
    def get(self, request):
        try:
            sorteios = Sorteio.objects.latest('numeros')
        except Sorteio.DoesNotExist:
            sorteios = {}
        return render(request, 'home.html',{'sorteios':sorteios})
"""
def index(request):
    try:
        sorteios = Sorteio.objects.latest('numeros')
    except Sorteio.DoesNotExist:
        sorteios = {}
    return render(request, 'loteria/index_loteria.html', {'sorteios':sorteios})
"""

   