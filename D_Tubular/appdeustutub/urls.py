from django.urls import path
from . import views
from .views import index, add_empleado


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

    # formularios
    path('add_empleado/', views.add_empleado, name='add_empleado'),
    
]
