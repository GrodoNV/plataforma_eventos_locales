# 📊 Diseño de Base de Datos - Plataforma de Eventos Locales

Este documento describe la estructura de la base de datos del proyecto, incluyendo las tablas, relaciones y el script SQL para su creación.

---

## 📐 Diagrama Relacional (ASCII)

```ascii
+------------------+        +------------------+        +------------------+        +-------------------+
|    Organizador   |        |      Evento      |        |      Lugar       |        |   Inscripcion     |
+------------------+        +------------------+        +------------------+        +-------------------+
| id (PK)          |<-------| organizador_id (FK) |     | id (PK)          |        | id (PK)           |
| nombre           |        | lugar_id (FK)       |----->| nombre           |        | evento_id (FK)    |
| email            |        | nombre              |        | direccion        |        | usuario           |
| telefono         |        | descripcion         |        | capacidad        |        | fecha_inscripcion |
+------------------+        | fecha_inicio        |        +------------------+        | asistencia (bool) |
                            | fecha_fin           |                                  +-------------------+
                            +---------------------+


Script SQL para creación de tablas


CREATE TABLE Organizador (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE Lugar (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL,
    capacidad INTEGER
);

CREATE TABLE Evento (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    organizador_id INTEGER REFERENCES Organizador(id) ON DELETE CASCADE,
    lugar_id INTEGER REFERENCES Lugar(id) ON DELETE SET NULL
);

CREATE TABLE Inscripcion (
    id SERIAL PRIMARY KEY,
    evento_id INTEGER REFERENCES Evento(id) ON DELETE CASCADE,
    usuario VARCHAR(100) NOT NULL,
    fecha_inscripcion DATE DEFAULT CURRENT_DATE,
    asistencia BOOLEAN DEFAULT FALSE
);


🔗 Relaciones

    Un organizador puede crear muchos eventos.

    Un evento ocurre en un solo lugar, pero un lugar puede tener varios eventos.

    Un usuario puede estar inscrito a muchos eventos, y cada inscripción registra su asistencia.

📝 Notas

    Se usa SERIAL como tipo para claves primarias para autoincrementar.

    Las relaciones están controladas con ON DELETE CASCADE y SET NULL según corresponda.

    El campo asistencia permite el registro de presencia en el evento.