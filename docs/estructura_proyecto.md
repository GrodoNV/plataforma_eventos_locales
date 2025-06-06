# Estructura del Proyecto: Plataforma de Eventos Locales

Este documento explica la estructura del proyecto y la función de cada carpeta o archivo principal.

## Raíz del Proyecto

- `manage.py`: Script principal para ejecutar comandos Django.
- `requirements.txt`: Lista de dependencias instaladas necesarias para correr el proyecto.
- `README.md`: Información general sobre el proyecto, instalación, ejecución y uso.
- `BITACORA.md`: Registro de actividades del equipo.
- `docs/`: Documentación técnica.

## Carpeta `plataforma_eventos_locales/`

Contiene la configuración principal del proyecto Django:
- `settings.py`: Configuraciones generales del proyecto.
- `urls.py`: Rutas principales del proyecto.
- `asgi.py` / `wsgi.py`: Interfaces para despliegue.

## Carpeta `eventos/`

Aplicación principal del sistema.
- `models.py`: Definición de modelos como Evento, Organizador, Lugar, Inscripción.
- `views.py`: Lógica de vista (qué se muestra o procesa).
- `urls.py`: Rutas específicas de esta app.
- `templates/`: Plantillas HTML.
- `static/`: Archivos estáticos como CSS, JS o imágenes.

## Carpeta `docs/`

Documentación técnica.
- `estructura_proyecto.md`: Este documento.
- `decisiones_tecnicas.md`: Análisis de decisiones importantes (tecnologías, modelos, arquitectura, etc).
- `diagrama_bd.png`: Imagen del diagrama de base de datos.
