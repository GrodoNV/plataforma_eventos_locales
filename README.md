
# 🎉 Plataforma de Eventos Locales

Una aplicación web para la gestión de eventos en una comunidad local. Permite crear eventos, registrar organizadores, gestionar inscripciones, asignar lugares y llevar el control de asistencia de los participantes.

---

## 📌 Objetivo del Proyecto

Facilitar la administración y visualización de eventos presenciales mediante una plataforma que centralice la información, permita filtros por fecha, y lleve un control de asistencia para mejorar la organización comunitaria.

---

## 🛠️ Funcionalidades Principales

- Registro y visualización de eventos
- Gestión de organizadores
- Inscripción de participantes
- Asignación de lugares para eventos
- Filtro por fecha
- Registro de asistencia



## 🧰 Requisitos del Sistema

- Python 3.10 o superior
- Django 4.x
- SQLite o PostgreSQL (configurable)
- pip (gestor de paquetes de Python)



## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/plataforma-eventos-locales.git
cd plataforma-eventos-locales
```
### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones y levantar el servidor

```bash
python manage.py migrate
python manage.py runserver
```

### 5. Acceder desde el navegador

```
http://127.0.0.1:8000/
```

---

## 📁 Estructura del Proyecto

```
plataforma_eventos_locales/
│
├── plataforma_eventos_locales/       # Configuración del proyecto Django (manage.py apunta aquí)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── eventos/                          # Aplicación principal (donde van modelos, vistas, urls, etc)
│   ├── migrations/
│   ├── static/                       # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/                    # Plantillas HTML
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── docs/                             # Documentación técnica y de desarrollo
│   ├── diagrama_bd.png               # Diagrama de base de datos (puede ser PNG o PDF)
│   ├── estructura_proyecto.md        # Descripción de carpetas y módulos
│   └── decisiones_tecnicas.md        # Qué se eligió y por qué (ej: por qué usar modelos separados)
│
├── BITACORA.md                       # Cambios cronológicos o avances diarios
├── README.md                         # Descripción del proyecto (instalación, requerimientos, etc)
├── requirements.txt                  # Librerías necesarias (usar `pip freeze > requirements.txt`)
├── .gitignore                        # Para excluir archivos como `__pycache__`, `.env`, etc
└── manage.py                         # Script para ejecutar comandos Django

```

---

## 📅 Equipo de Desarrollo

* Dev 1: Modelado y backend 
* Dev 2: Vistas y funcionalidades
* Dev 3: Filtros y asistencia
* Dev 4: Documentación y estructura técnica
* Dev 5: Presentación y manual de usuario

---

## 📌 Licencia

Este proyecto es de uso académico y fue desarrollado como parte de una presentación final universitaria.



