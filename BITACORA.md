# 📝 Bitácora de Desarrollo

### 📆 5 de junio 2025
- Se creó el repositorio en GitHub – Grodo(Gabriel)
- Se definió la estructura inicial del proyecto
- Se invitó a los colaboradores

---
###🗓 2025-06-06 
– Se creó la estructura inicial del proyecto, se definió el sistema de carpetas y se generó el archivo `estructura_proyecto.md` en la carpeta `docs/` – Grodo (Gabriel)  
🔧 No hubo problemas. Se definió una estructura modular para facilitar el trabajo colaborativo.

🗓 2025-06-06 – Se diseñó el esquema de la base de datos (Evento, Organizador, Lugar, Inscripción) y se agregó el diagrama en ASCII al archivo `docs/BD.md`, junto con el script SQL para la creación de las tablas – Grodo  
🔧 No hubo problemas. Se consideraron las funcionalidades requeridas (filtro por fecha y registro de asistencia) para estructurar las tablas y relaciones adecuadamente.


🗓 2025-06-08 – Se crearon los modelos: Evento, Organizador, Inscripción y Lugar, con sus respectivas relaciones. También se registraron en el panel de administración – Gabriel Rodrigo Nina Vargas  
🔧 Ningún problema. Se validó que las relaciones y registros en `models.py` y `admin.py` funcionen correctamente.

🗓 2025-06-09 – Se implementó el CRUD para el modelo Inscripción, incluyendo creación, listado y eliminación. Se agregaron vistas, formularios, rutas y plantillas. También se validó el funcionamiento correcto desde el navegador – Gabriel Rodrigo Nina Vargas
🔧 No hubo problemas. Las inscripciones se asocian correctamente con los eventos y se pueden registrar de forma individual desde el navegador.

🗓 2025-06-09 – Se añadió funcionalidad de filtro por fecha en la vista de lista de eventos. Se integró un formulario con selector de fecha en la plantilla y se ajustó la vista para filtrar los resultados – Gabriel Rodrigo Nina Vargas
🔧 No hubo problemas. El filtrado por fecha funciona correctamente y actualiza la lista de eventos mostrada al usuario.78


### Formato para nuevas entradas:
🗓 FECHA – Qué se hizo – Quién lo hizo  
🔧 Problemas (si hubo) y cómo se resolvieron
