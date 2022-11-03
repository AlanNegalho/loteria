from django import forms
from bicho.models import JogoBicho


class EscolhaBicho(forms.ModelForm):

    class Meta:
        model = JogoBicho
        fields = ('bichos',)

        widgets = {
            'bichos': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }