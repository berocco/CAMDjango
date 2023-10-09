from django.db import models

# Create your models here.
class Tag(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    empresa = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, verbose_name='Descrição da vaga')
    requisitos = models.TextField(blank=True)
    inscricao = models.CharField(max_length=100, verbose_name='Inscrição')
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.titulo