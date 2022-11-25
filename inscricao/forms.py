from django import forms
from .models import *

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class NovaInscricaoForm(forms.ModelForm):
    class Meta:
        model= NovaInscricao
        fields= '__all__'   

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
             # Bootstrap não aplicou v!
            'sexo': forms.RadioSelect(attrs={'type': 'radio'}),
            'tecnico': forms.Select(attrs={'class': 'form-select'}),
            # Bootstrap não aplicou v!
            'minicursos': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}), 
        }
