from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.

def nova_inscricao(request):
    if request.method == "GET":
        form = NovaInscricaoForm()
    elif request.method == "POST":
        form = NovaInscricaoForm(request.method.POST or None)
        if form.is_valid():
            # nome = request.POST.get('nome')
            # cpf = request.POST.get('cpf')
            # nascimento = request.POST.get('enrollment')
            # email = request.POST.get('email')
            # endereco = request.POST.get('phone')
            # sexo_masculino = request.POST.get('sexo_masculino')
            # sexo_feminino = request.POST.get('sexo_feminino')
            # curso = request.POST.get('curso')
            # minicursos = request.POST.get('minicursos')

            try: 
                form.save()
                messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
                return redirect('/home/nova_inscricao')
            except:
                pass

    return render(request, 'nova_inscricao.html', {'form': form})


# def nova_inscricao(request):
#     if request.method == 'POST':
#         form = NovaInscricaoForm(request.POST) 
#         if form.is_valid():
#             try:
#                 form.save()
#                 form = NovaInscricaoForm()
#             else:
#                 pass
#     else:
#         form = NovaInscricaoForm()

#     return render(request,'nova_inscricao.html', {'form' : form})