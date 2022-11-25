from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.messages import constants
from django.contrib import messages


def nova_inscricao(request):
    if request.POST:
        form = NovaInscricaoForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, constants.SUCCESS, 'Inscrição realizada com sucesso')
                return redirect('/home/nova_inscricao')
            except: 
                pass
    else:
        form = NovaInscricaoForm()

    return render(request, 'nova_inscricao.html', {'form': form})

