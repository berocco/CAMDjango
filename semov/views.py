from django.shortcuts import render
from .models import Logo, Inscricao, Capa, Edicao, Evento, Data, Patrocinador
from django.core.cache import cache
from django.views.generic import ListView
# Create your views here.
def index(request):
    logo = cache.get('logo')
    if logo is None:
        logo = Logo.objects.first()
        cache.set('logo', logo)
    
    inscricao = cache.get('inscricao')
    if inscricao is None:
        inscricao = Inscricao.objects.first()
        cache.set('inscricao', inscricao)
    
    capa = cache.get('capa')
    if capa is None:
        capa = Capa.objects.first()
        cache.set('capa', capa)
    edicoes = Edicao.objects.order_by('ano')
    patrocinadores = Patrocinador.objects.order_by('nome')
    context = {'logo': logo,
               'inscricao': inscricao,
               'capa': capa,
               'edicoes': edicoes,
               'patrocinadores': patrocinadores}
    
    return render(request, 'semov/index.html', context)

def schedule(request):
    datas = Data.objects.order_by('dia')
    context = {'datas': datas}
    return render(request, 'semov/schedule.html', context)    