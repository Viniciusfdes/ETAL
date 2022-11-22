from django.urls import path
from .views import *

urlpatterns = [
    path('nova_inscricao/', nova_inscricao, name='nova_inscricao')
]
