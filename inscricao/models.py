from django.db import models

CHOICES_CURSOS = (
    ('inf', 'Informática'),
    ('ali', 'Alimentos'),
    ('api', 'Apicultura')    
)

class NovaInscricao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    nascimento = models.DateField()
    email = models.EmailField(max_length=40)
    endereco = models.CharField(max_length=50)
    sexo = models.BooleanField(choices=((False,"Feminino"), (True,"Masculino")))
    curso = models.CharField(max_length=3, choices=CHOICES_CURSOS)
