# Generated by Django 4.1.3 on 2022-11-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NovaInscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateTimeField()),
                ('email', models.EmailField(max_length=150)),
                ('endereco', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='Masculino', max_length=9)),
                ('tecnico', models.CharField(choices=[('ALI', 'Alimentos'), ('API', 'Apicultura'), ('INF', 'Informática')], max_length=11)),
                ('minicursos', models.ManyToManyField(to='inscricao.minicurso')),
            ],
        ),
    ]
