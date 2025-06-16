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
from .forms import OrganizadorForm
from .models import Organizador
from .models import Lugar
from .forms import LugarForm
from .models import Inscripcion
from .forms import InscripcionForm
from django.shortcuts import render, get_object_or_404
from .models import Evento, Inscripcion
from django.shortcuts import render, get_object_or_404, redirect

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

# CRUD EVENTOS

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')  # o donde quieras
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

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
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')

    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

    # CRUD ORGANIZADORES

def lista_organizadores(request):
    organizadores = Organizador.objects.all()
    return render(request, 'eventos/lista_organizadores.html', {'organizadores': organizadores})

def crear_organizador(request):
    if request.method == 'POST':
        form = OrganizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_organizadores')
    else:
        form = OrganizadorForm()
    return render(request, 'eventos/crear_organizador.html', {'form': form})

def editar_organizador(request, organizador_id):
    organizador = get_object_or_404(Organizador, id=organizador_id)
    if request.method == 'POST':
        form = OrganizadorForm(request.POST, instance=organizador)
        if form.is_valid():
            form.save()
            return redirect('lista_organizadores')
    else:
        form = OrganizadorForm(instance=organizador)
    return render(request, 'eventos/editar_organizador.html', {'form': form})

def eliminar_organizador(request, organizador_id):
    organizador = get_object_or_404(Organizador, id=organizador_id)
    if request.method == 'POST':
        organizador.delete()
        return redirect('lista_organizadores')
    return render(request, 'eventos/eliminar_organizador.html', {'organizador': organizador})

# CRUD LUGARES

def lista_lugares(request):
    lugares = Lugar.objects.all()
    return render(request, 'eventos/lista_lugares.html', {'lugares': lugares})

def crear_lugar(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_lugares')
    else:
        form = LugarForm()
    return render(request, 'eventos/crear_lugar.html', {'form': form})

def editar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('lista_lugares')
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'eventos/editar_lugar.html', {'form': form})

def eliminar_lugar(request, lugar_id):
    lugar = get_object_or_404(Lugar, id=lugar_id)
    if request.method == 'POST':
        lugar.delete()
        return redirect('lista_lugares')
    return render(request, 'eventos/eliminar_lugar.html', {'lugar': lugar})

# CRUD INSCRIPCIONES

def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'eventos/lista_inscripciones.html', {'inscripciones': inscripciones})

def crear_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'eventos/crear_inscripcion.html', {'form': form})

def editar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('lista_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'eventos/editar_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('lista_inscripciones')
    return render(request, 'eventos/eliminar_inscripcion.html', {'inscripcion': inscripcion})


def registrar_asistencia(request, inscripcion_id):
    inscripcion = get_object_or_404(Inscripcion, id=inscripcion_id)
    asistencia, created = Asistencia.objects.get_or_create(inscripcion=inscripcion)

    if request.method == 'POST':
        # El checkbox solo envía valor si está marcado
        asistio = 'presente' in request.POST
        asistencia.asistio = asistio
        asistencia.save()
        return redirect('lista_inscripciones')  # Cambia aquí si quieres otra URL

    # GET: mostrar formulario con estado actual
    context = {
        'inscripcion': inscripcion,
        'asistencia': asistencia,
    }
    return render(request, 'inscripciones/registro_asistencia.html', context)

