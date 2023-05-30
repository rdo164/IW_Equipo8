from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ProcesoDetailView, EmpleadoListView, EmpleadoDetailView, add_empleado, borrar_proceso, borrar_equipo, enviar_email, EquipoListView, EquipoDetailView, ProcesoListView


urlpatterns =[
    # índice principal
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # indices de los modelos
    path('equipos/', EquipoListView.as_view(), name='equipo-list'),
    path('equipos/<int:pk>/', EquipoDetailView.as_view(), name='equipo-detail'),
    path('procesos/', ProcesoListView.as_view(), name='proceso-list'),
    path('procesos/<int:pk>/', ProcesoDetailView.as_view(), name='proceso-detail'),
    path('empleados/', EmpleadoListView.as_view(), name='empleado-list'),
    path('empleados/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-detail'),

    # añadir
    path('add_empleado/', views.add_empleado, name='add_empleado'),
    path('add_equipo/', views.add_equipo, name='add_equipo'),
    path('add_proceso/', views.add_proceso, name='add_proceso'),
    
    # borrar
    path('proceso/borrar/<int:proceso_id>/', views.borrar_proceso, name='borrar_proceso'),
    path('equipo/borrar/<int:equipo_id>/', views.borrar_equipo, name='borrar_equipo'),
    path('empelado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # modificar
    path('equipo/modificar/<int:equipo_id>/', views.modificar_equipo, name='modificar_equipo'),
    path('proceso/modificar/<int:proceso_id>/', views.modificar_proceso, name='modificar_proceso'),
    path('empleado/modificar/<int:empleado_id>/', views.modificar_empleado, name='modificar_empleado'),

    # funcionalidades adicionales
    # envio de emails
    path('enviar-email/', views.enviar_email_view, name='enviar_email'),
    path('confirmacion/', views.confirmacion_envio, name='confirmacion_envio'),

    # subir archivos 
    path('subir-archivo/', views.subir_archivo, name='subir_archivo'),
    path('mostrar-archivos/', views.mostrar_archivos, name='mostrar_archivos'),
    path('descargar-archivo/<int:archivo_id>/', views.descargar_archivo, name='descargar_archivo'),
]

