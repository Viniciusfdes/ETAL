from django.forms import ModelForm, TextInput
from .models import *

class FormNovaInscricao(ModelForm):
    class Meta:
        model = NovaInscricao
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control'}),
            'nascimento': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'curso': TextInput(attrs={'class': 'form-control'})
        }