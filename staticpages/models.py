from django.db import models

# Create your models here.
class Membro(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='membros')
    cargo = models.CharField(max_length=100)
    ordem = models.IntegerField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Diretoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='diretorias')
    ordem = models.IntegerField()
    descricao = models.TextField(max_length=511)
    def __str__(self):
        return self.nome

class Faq(models.Model):
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField(max_length=511)
    ordem = models.IntegerField()
    def __str__(self):
        return self.pergunta

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    whatsapp = models.URLField(max_length=100)
    ordem = models.IntegerField()
    def __str__(self):
        return self.nome

class Slide(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=511)
    imagem = models.ImageField(upload_to='slides')
    link = models.URLField(max_length=100)
    ordem = models.IntegerField()
    def __str__(self):
        return self.titulo
