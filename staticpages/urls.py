from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('historia', views.historia, name='historia'),
    path('carometro', views.MembrosListView.as_view(), name='carometro'),
    path('diretorias', views.DiretoriasListView.as_view(), name='diretorias'),
    path('faq', views.FaqListView.as_view(), name='faq'),
    path('contato', views.ContatoListView.as_view(), name='contato'),
    #path('semov_index', views.semov_index, name='semov_index'),
]