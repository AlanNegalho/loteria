from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from loteria.models import Jogo, Sorteio,Cliente, Contas
from .forms import UserCreateForm ,User,ClienteForm,formContas,formDeposito,formSaque
from .sorteio1 import Loteria as Lt
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def jogo(request):
    return render(request, 'loteria/jogo.html',{})

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadastrar_cli')
            
    else:
        form = UserCreateForm()
    return render(request,'loteria/cadastrar_cli.html', {'form': form})

def cadastrar_cli(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            form.save()
        return redirect('home1')
    else:
        form = ClienteForm()
    return render(request, 'loteria/cadastrar_cli.html', {'form': form})

def login_user(request):
    return render(request, 'loteria/login.html', {})

def logaut_user(request):
    logout(request)
    return redirect('home')



def autenticar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            id = user.id
            user = get_object_or_404(User, pk=id)
            return redirect('home1')
        else:
           return redirect('home')

    return render(request,'loteria/home.html')


def processa_formulario(request):
    if request.method == "POST":
        bilhete0 = request.POST.get('number',None)
        bilhete1 = request.POST.get('number1',None)
        bilhete2 = request.POST.get('number2',None)
        bilhete3 = request.POST.get('number3',None)
        bilhete4 = request.POST.get('number4',None)
        bilhete5 = request.POST.get('number5',None)
        dados  = [bilhete0, bilhete1,bilhete2,bilhete3,bilhete4,bilhete5]
        cliente = Cliente.objects.get(user__id=request.user.id)
        rt = Jogo.objects.create(cliente=cliente,numeros=dados)
        rt.save()
    return redirect('jogo')


def conta(request):
    return render(request,'loteria/carteira.html',{})

def criar_conta(request):
    form = formContas()
    return render(request, 'loteria/criar_conta.html', {'form':form})


def contas(request):
    if request.method == "POST":
        form = formContas(request.POST)
        if form.is_valid():
            form.instance.cliente=Cliente.objects.get(user__id=request.user.id)
            form.save()
            return render(request, 'loteria/carteira.html', {'form':form})
        
        
    else:
        form = formContas()
        return render(request, 'loteria/index_loteria.html', {'form':form})

def depositos(request):
    form = formDeposito()
    return render(request,'loteria/deposito.html',{'form':form}) 

def deposito(request):
    if request.method == "POST":
        form = formDeposito(request.POST)
        #print(form['conta'].value())
        if form.is_valid():
            cliente=Cliente.objects.get(user__id=request.user.id)
            conta = Contas.objects.get(cliente__id=cliente.id)
            form.instance.conta = conta
            form.save()
            return redirect('conta')
    else:
        form = formDeposito()
        return render(request, 'loteria/index_loteria.html', {'form':form})

def saques(request):
    form = formSaque()
    return render(request,'loteria/saque.html',{'form':form}) 

def saque(request):
    if request.method == "POST":
        form = formSaque(request.POST)
        #print(form['conta'].value())
        if form.is_valid():
            cliente=Cliente.objects.get(user__id=request.user.id)
            conta = Contas.objects.get(cliente__id=cliente.id)
            form.instance.conta = conta
            form.save()
            return redirect('conta')
    else:
        form = formSaque()
        return render(request, 'loteria/index_loteria.html', {'form':form})

def sistema(request):
    if request.method == "POST":
        lt = Lt(int(request.POST['quantidade']))
        lt.adiciona_numero()
        jogo = Jogo(numeros=lt.numeros)
        
        jogo.save()
        return redirect('index_loteria')

def sorteio(request):
    if request.method == "POST":
        lt = Lt(int(request.POST['quantidade']))
        lt.adiciona_numero()
        jogo = Sorteio(numeros=lt.numeros)
        jogo.save()
        return redirect('index_loteria')

def listar_jogo(request):
    cliente = Cliente.objects.get(user__id=request.user.id)
    jogos = Jogo.objects.filter(cliente__id=cliente.id)
    return render(request, 'loteria/listar_jogo.html', {'jogos':jogos})

def listar_saldo(request):
    cliente = Cliente.objects.get(user__id=request.user.id)
    conta = Contas.saldo.objects.filter(cliente__id=cliente.id)
    return render(request, 'loteria/jogo.html',{'conta':conta, 'cliente':cliente})


def index(request):
    try:
        sorteios = Sorteio.objects.latest('numeros')
    except Sorteio.DoesNotExist:
        sorteios = {}
    return render(request, 'loteria/index_loteria.html', {'sorteios':sorteios})

