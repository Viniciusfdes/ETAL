from django import forms
from .models import NovaInscricao

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
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'minicursos': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
            'sexo': forms.RadioSelect(attrs={'class': 'form-check-input', 'type': 'radio'}),
            'data_nascimento': forms.TimeInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
