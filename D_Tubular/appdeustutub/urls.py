from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('equipos/', views.index_equipo, name='index_equipo')
]