from django.urls import path
from . import views
from .views import index, add_empleado, borrar_proceso, borrar_equipo


urlpatterns =[
    # índice principal
    path('', views.index, name='index'),

    # indices de los modelos
    path('equipos/', views.index_equipo, name='index_equipo'),
    path('procesos/', views.index_proceso, name='index_proceso'),
    path('empleados/', views.index_empleado, name='index_empleado'),

    # detail
    path('equipo/<int:equipo_id>/', views.show_equipo, name='detail_equipo'),
    path('proceso/<int:proceso_id>/',views.show_proceso, name='detail_proceso'),
    path('empleado/<int:empleado_id>/', views.show_empleado, name='detail_empleado'),

    # añadir
    path('add_empleado/', views.add_empleado, name='add_empleado'),
    path('add_equipo/', views.add_equipo, name='add_equipo'),
    path('add_proceso/', views.add_proceso, name='add_proceso'),
    
    # borrar
    path('proceso/borrar/<int:proceso_id>/', views.borrar_proceso, name='borrar_proceso'),
    path('equipo/borrar/<int:equipo_id>/', views.borrar_equipo, name='borrar_equipo'),
    
    # modificar
    path('equipo/modificar/<int:equipo_id>/', views.modificar_equipo, name='modificar_equipo'),
    path('proceso/modificar/<int:proceso_id>/', views.modificar_proceso, name='modificar_proceso'),
]
