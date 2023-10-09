from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from staticpages.models import Membro, Diretoria, Faq, Contato, Slide
from .forms import MembroForm, DiretoriaForm, FaqForm, ContatoForm
# Create your views here.

def index(request):
    slides = Slide.objects.order_by('ordem')
    context = {'slide_list': slides}
    return render(request, 'staticpages/index.html', context)

def historia(request):
    return render(request, 'staticpages/historia.html')

class MembrosListView(ListView):
    model = Membro
    template_name = 'staticpages/carometro.html'
    def get_queryset(self):
        return Membro.objects.order_by('ordem')

class DiretoriasListView(ListView):
    model = Diretoria
    template_name = 'staticpages/diretorias.html'
    def get_queryset(self):
        return Diretoria.objects.order_by('ordem')

class FaqListView(ListView):
    model = Faq
    template_name = 'staticpages/faq.html'
    def get_queryset(self):
        return Faq.objects.order_by('ordem')

def semov_index(request):
    return render(request, 'staticpages/semov_index.html')
class ContatoListView(ListView):
    model = Contato
    template_name = 'staticpages/contato.html'
    def get_queryset(self):
        return Contato.objects.order_by('ordem')
