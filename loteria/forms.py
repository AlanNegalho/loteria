from dataclasses import fields
from pyexpat import model
from django import forms
from loteria.models import Cliente, Jogo,Deposito,Contas,Saque
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
        email = forms.EmailField(required=True)

        class Meta:
                model = User
                fields = ['username']
        

class ClienteForm(forms.ModelForm):
  
       class Meta:
        model = Cliente
        fields = '__all__'
    

class formContas(forms.ModelForm):

    class Meta:
        model = Contas
        fields = ('agencia','conta','saldo')

        widgets = {
            'agencia': forms.TextInput(attrs={ 'class': 'form-control'}),
            'conta': forms.TextInput(attrs={ 'class': 'form-control'}),
            'saldo': forms.TextInput(attrs={ 'class': 'form-control'}),
        }

class formDeposito (forms.ModelForm):

    class Meta:
        model = Deposito
        fields = ('valor',)
        widgets = {
            #'conta': forms.Select(attrs={ 'class': 'form-control'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control'}),
        }

class formSaque (forms.ModelForm):

    class Meta:
        model = Saque
        fields = ('chave_pix','valor')
        widgets = {
            #'conta': forms.Select(attrs={ 'class': 'form-control'}),
            'chave_pix': forms.TextInput(attrs={ 'class': 'form-control'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control'}),
        }

