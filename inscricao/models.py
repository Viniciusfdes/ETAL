from django.db import models

CHOICES_SEXO = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]

CHOICES_TECNICO = [
    ('ALI', 'Alimentos'),
    ('API', 'Apicultura'),
    ('INF', 'Informática')
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class NovaInscricao(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14) 
    data_nascimento = models.DateTimeField()
    email = models.EmailField(max_length=150)
    endereco = models.CharField(max_length=200)
    sexo = models.CharField(max_length=9, choices= CHOICES_SEXO, default='Masculino')
    tecnico = models.CharField(max_length=11, choices=CHOICES_TECNICO)
    minicursos = models.ManyToManyField(MiniCurso)

    def __str__(self) -> str:
        return self.nome
