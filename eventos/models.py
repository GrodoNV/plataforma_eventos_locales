from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.fecha.strftime('%d/%m/%Y %H:%M')})"


class Inscripcion(models.Model):
    nombre_participante = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_participante} - {self.evento.titulo}"


class Asistencia(models.Model):
    inscripcion = models.OneToOneField('Inscripcion', on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False)
    hora_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inscripcion.nombre_participante} - {'Asistió' if self.asistio else 'No asistió'}"
