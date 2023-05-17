from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    idade = models.IntegerField()

class Interesse(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=255)
    categoria = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    imagem = models.ImageField(upload_to="img", null=True)
