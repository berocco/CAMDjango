from django.urls import path
from . import views
urlpatterns = [
    path('', views.EstagioListView.as_view(), name='estagios'),
]