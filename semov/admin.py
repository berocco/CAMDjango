from django.contrib import admin
from .models import Logo, Inscricao, Capa, Edicao, Patrocinador, Data, Evento
# Register your models here.
admin.site.register(Logo)
admin.site.register(Inscricao)
admin.site.register(Capa)
admin.site.register(Edicao)
admin.site.register(Patrocinador)
admin.site.register(Evento)
admin.site.register(Data)