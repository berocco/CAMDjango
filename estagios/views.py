from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Vaga
from django.views.generic import ListView
# Create your views here.
class EstagioListView(ListView):
    model = Vaga
    template_name = 'estagios/estagios.html'
    def get_queryset(self):
        qs = self.request.GET.get('tag')
        if qs:
            qs = Vaga.objects.filter(tags__nome__icontains=qs)
        else:
            qs = Vaga.objects.all()
        return qs