from django.contrib import admin
from .models import *

class AdminNovaInscricao(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')

class AdminMiniCurso(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(NovaInscricao, AdminNovaInscricao)
admin.site.register(MiniCurso, AdminMiniCurso)