# 🏆 Registro de Fútbol - Proyecto Backend

Este es un sistema web desarrollado con **Django** y **Django REST Framework**, diseñado para gestionar información de fútbol como equipos, jugadores, torneos y partidos. El proyecto incluye una API REST completa, formularios con carga de imágenes y documentación Swagger.

---

## ⚙️ Tecnologías Utilizadas

- Python 3.13+
- Django 5.2.4
- Django REST Framework
- SQLite3
- drf-yasg (Swagger)
- Django Filters
- Pillow (para imágenes)

---

## 🚀 Funcionalidades Principales

### 🔁 CRUDs completos
- Jugadores (con foto)
- Equipos (con escudo)
- Torneos
- Partidos
- Países
- Relación Equipo-Torneo

### 🔐 Autenticación y Permisos
- Token Authentication para la API
- Vista Swagger protegida
- Permisos con `IsAuthenticatedOrReadOnly`

### 🌐 API Endpoints
- `/api/jugadores/`
- `/api/equipos/`
- `/api/torneos/`
- `/api/partidos/`
- `/api/paises/<id>/`
- `/api/token/` → obtener token con login

### 🧾 Documentación Interactiva
- Swagger: `/swagger/`
- Redoc: `/redoc/`

---

## 📦 Instalación

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/registro_futbol-proyecto-backend.git

cd registro_futbol-proyecto-backend

# Crea entorno virtual
python -m venv env
source env/bin/activate      # En Windows: env\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

