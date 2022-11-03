from django.shortcuts import render,get_object_or_404, redirect
from bicho.models import Sorteio
from .sorteio1 import Loteria as Lt
from bicho.models import Sorteio,Cliente, JogoBicho
from .forms import EscolhaBicho, JogoBicho
from datetime import date

# Create your views here.

def index(request):
    try:
        sorteios = Sorteio.objects.latest('numeros')
    except Sorteio.DoesNotExist:
        sorteios = {}
    return render(request, 'bicho/index_bicho.html', {'sorteios':sorteios})



def sorteio(request):
    if request.method == "POST":
        lt = Lt(int(request.POST['quantidade']))
        lt.adiciona_numero()
        jogo = Sorteio(numeros=lt.numeros)
        jogo.save()
        return redirect('index_bicho')

def escolhar_bicho(request):
    form = EscolhaBicho()
    return render(request, 'bicho/index_bicho.html',{'form': form})
    
def escolhar_bichos(request):
   
    if request.method == "POST":
        form = EscolhaBicho(request.POST)
        select_bichos = request.POST.getlist('bichos', None)
        usuario = Cliente.objects.get(user__id=request.user.id)
        insert = JogoBicho.objects.create(bichos=select_bichos, data=date.today(), bilhetecliente=usuario)
        insert.save()
        return redirect('result_bichos')
    else:
        form = EscolhaBicho()
    return render(request, 'index_bichos.html', {'form': form})
