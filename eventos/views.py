from django.shortcuts import render
from .models import Evento
from django.utils.dateparse import parse_date
from django.shortcuts import get_object_or_404, redirect
from .models import Inscripcion, Asistencia
from .models import Evento, Inscripcion
from .forms import InscripcionForm
from django.shortcuts import get_object_or_404, render, redirect
from .forms import EventoForm
from .forms import InscripcionForm, EventoForm

def lista_eventos(request):
    fecha_str = request.GET.get('fecha')
    if fecha_str:
        fecha = parse_date(fecha_str)
        if fecha:
            eventos = Evento.objects.filter(fecha__date=fecha)
        else:
            eventos = Evento.objects.none()
    else:
        eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})


def registrar_asistencia(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    asistencia, created = Asistencia.objects.get_or_create(inscripcion=inscripcion)
    asistencia.asistio = True
    asistencia.save()
    return redirect('lista_eventos')  # Cambia esto según tu flujo

from django.shortcuts import render, get_object_or_404
from .models import Evento, Inscripcion

def lista_inscripciones(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    inscripciones = Inscripcion.objects.filter(evento=evento)
    return render(request, 'eventos/lista_inscripciones.html', {
        'evento': evento,
        'inscripciones': inscripciones,
    })


def inscribirse_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.evento = evento
            inscripcion.save()
            return redirect('lista_eventos')
    else:
        form = InscripcionForm()

    return render(request, 'eventos/inscripcion.html', {
        'form': form,
        'evento': evento
    })


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  # o donde quieras
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})