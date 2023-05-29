from django.db import models

class Categoria(models.Model):
    categoria = models.TextField(max_length=255)
    descricacao = models.TextField(max_length=255)

    def __str__(self):
        return self.categoria

class Interesse(models.Model):
    titulo = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    cat = models.TextField(max_length=255)
    imagem = models.FileField(upload_to="img", null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.titulo
