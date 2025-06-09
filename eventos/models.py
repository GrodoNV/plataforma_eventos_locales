from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)

class Inscripcion(models.Model):
    nombre_participante = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
