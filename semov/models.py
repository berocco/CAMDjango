from django.db import models

# Create your models here.
class Patrocinador(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='patrocinadores')
    link = models.URLField(max_length=100)
    class Meta:
        verbose_name = 'Patrocinador'
        verbose_name_plural = 'Patrocinadores'
    def __str__(self):
        return self.nome
    
class Logo(models.Model):
    nome = models.CharField(max_length=31)
    imagem = models.ImageField(upload_to='logos_semov')
    def __str__(self):
        return self.nome

class Edicao(models.Model):
    ano = models.IntegerField()
    descricao = models.TextField()
    class Meta:
        verbose_name = 'Edição'
        verbose_name_plural = 'Edições'
    def __str__(self):
        return str(self.ano)

class Inscricao(models.Model):
    ano = models.IntegerField()
    link = models.URLField(max_length=100)
    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
    def __str__(self):
        return str(self.ano)

class Capa(models.Model):
    imagem = models.ImageField(upload_to='capas')
    ano = models.IntegerField()
    dias = models.IntegerField()
    empresas = models.IntegerField()
    eventos = models.IntegerField()
    def __str__(self):
        return str(self.ano)

class Data(models.Model):
    dia = models.DateField()
    dia_da_semana = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return str(self.dia)

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    TIPOS = (
        ('PALESTRA', 'Palestra'),
        ('WORKSHOP', 'Workshop'),
        ('PROCESSO SELETIVO', 'Processo Seletivo'),
        ('VISITA TÈCNICA', 'Visita Técnica'),
        ('RESOLUÇÂO DE CASE', 'Resolução de Case'),
        ('MINICURSO', 'Minicurso')
    )
    dia = models.ForeignKey(Data, on_delete=models.CASCADE)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    tipo = models.CharField(choices=TIPOS, max_length=20)
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    def __str__(self):
        return self.titulo
