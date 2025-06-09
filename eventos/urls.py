from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('asistencia/<int:inscripcion_id>/', views.registrar_asistencia, name='registrar_asistencia'),
    path('inscripciones/<int:inscripcion_id>/asistencia/', views.registrar_asistencia, name='registrar_asistencia'),
    path('evento/<int:evento_id>/inscribirse/', views.inscribirse_evento, name='inscribirse_evento'),
    path('crear_evento/', views.crear_evento, name='crear_evento'),

]
