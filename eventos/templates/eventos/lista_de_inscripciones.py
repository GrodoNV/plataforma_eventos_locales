<!DOCTYPE html>
<html>
  <head>
    <title>Inscripciones para {{ evento.titulo }}</title>
  </head>
  <body>
    <h1>Inscripciones para {{ evento.titulo }}</h1>
    <ul>
      {% for inscripcion in inscripciones %}
      <li>
        {{ inscripcion.nombre_participante }} - {{ inscripcion.email }}
        {% if inscripcion.asistencia.asistio %}
          <strong>(Asistió)</strong>
        {% else %}
          <a href="{% url 'registrar_asistencia' inscripcion.id %}">Marcar asistencia</a>
        {% endif %}
      </li>
      {% empty %}
      <li>No hay inscripciones para este evento.</li>
      {% endfor %}
    </ul>
    <a href="{% url 'lista_eventos' %}">Volver a eventos</a>
  </body>
</html>
