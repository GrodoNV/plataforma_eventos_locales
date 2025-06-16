from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('inscripciones/<int:inscripcion_id>/asistencia/', views.registrar_asistencia, name='registrar_asistencia'),\
    
 
    path('evento/<int:evento_id>/inscribirse/', views.inscribirse_evento, name='inscribirse_evento'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('evento/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
 
    path('organizadores/', views.lista_organizadores, name='lista_organizadores'),
    path('organizadores/crear/', views.crear_organizador, name='crear_organizador'),
    path('organizadores/<int:organizador_id>/editar/', views.editar_organizador, name='editar_organizador'),
    path('organizadores/<int:organizador_id>/eliminar/', views.eliminar_organizador, name='eliminar_organizador'),
 
    path('lugares/', views.lista_lugares, name='lista_lugares'),
    path('lugares/crear/', views.crear_lugar, name='crear_lugar'),
    path('lugares/<int:lugar_id>/editar/', views.editar_lugar, name='editar_lugar'),
    path('lugares/<int:lugar_id>/eliminar/', views.eliminar_lugar, name='eliminar_lugar'),
 
    path('inscripciones/', views.lista_inscripciones, name='lista_inscripciones'),
    path('inscripciones/crear/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscripciones/<int:inscripcion_id>/editar/', views.editar_inscripcion, name='editar_inscripcion'),
    path('inscripciones/<int:inscripcion_id>/eliminar/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    path('asistencia/<int:inscripcion_id>/', views.registrar_asistencia, name='registrar_asistencia'),


]
