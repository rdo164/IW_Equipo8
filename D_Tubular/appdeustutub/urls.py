from django.urls import path
from . import views
from .views import index

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

    # detalles de empleados
    # path('equipo/<int:equipo_id>/empleados/', views.show_empleado_equipo, name='detail_empleado_equipo'),
]
