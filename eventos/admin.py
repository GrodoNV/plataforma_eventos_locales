from django.contrib import admin
from .models import Organizador, Lugar, Evento, Inscripcion
from .models import Asistencia

admin.site.register(Asistencia)
admin.site.register(Organizador)
admin.site.register(Lugar)
admin.site.register(Evento)
admin.site.register(Inscripcion)
