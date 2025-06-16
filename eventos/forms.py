from django import forms
from .models import Inscripcion
from .models import Organizador
from .models import Lugar
from .models import Inscripcion

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'direccion']        

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre', 'email']  # Ajusta según tus campos reales


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombre_participante']

from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'organizador']  # Ajusta según tus campos reales



class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['evento', 'nombre_participante']
