from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='semov_index'),
    path('schedule', views.schedule, name='semov_schedule'),
]