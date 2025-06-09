from django.test import TestCase
from django.urls import reverse
from .models import Evento, Lugar, Organizador, Inscripcion, Asistencia
from datetime import datetime

class EventosTests(TestCase):
    def setUp(self):
        self.lugar = Lugar.objects.create(nombre="Auditorio", direccion="Calle Falsa 123")
        self.organizador = Organizador.objects.create(nombre="Org1", email="org1@example.com")
        self.evento1 = Evento.objects.create(
            titulo="Evento 1",
            descripcion="Desc",
            fecha=datetime(2025, 6, 8, 15, 0),
            lugar=self.lugar,
            organizador=self.organizador
        )
        self.evento2 = Evento.objects.create(
            titulo="Evento 2",
            descripcion="Desc",
            fecha=datetime(2025, 6, 9, 15, 0),
            lugar=self.lugar,
            organizador=self.organizador
        )
        self.inscripcion = Inscripcion.objects.create(
            nombre_participante="Juan",
            email="juan@example.com",
            evento=self.evento1
        )

    def test_filtro_por_fecha(self):
        url = reverse('lista_eventos') + '?fecha=2025-06-08'
        response = self.client.get(url)
        self.assertContains(response, "Evento 1")
        self.assertNotContains(response, "Evento 2")

    def test_registrar_asistencia(self):
        # Registrar asistencia
        url = reverse('registrar_asistencia', args=[self.inscripcion.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirección después de marcar asistencia
        
        # Verificar que la asistencia quedó registrada
        asistencia = Asistencia.objects.get(inscripcion=self.inscripcion)
        self.assertTrue(asistencia.asistio)
