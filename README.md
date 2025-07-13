# fastapi_crud_practice

Bienvenido a **fastapi_crud_practice**, una API REST construida con [FastAPI](https://fastapi.tiangolo.com/) como práctica para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una colección de posts.

---

## Descripción

Esta aplicación permite:

- Crear posts
- Ver todos los posts
- Buscar por ID
- Actualizar información de un post
- Eliminar posts

Está desarrollada con Python y FastAPI, y usa una lista en memoria para simular una base de datos.

---

## Requisitos

- Python 3.7 o superior  
- Git (opcional, si vas a clonar el proyecto)  
- Uvicorn (para ejecutar el servidor)

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Cici160401/fastapi_crud_practice.git
cd fastapi_crud_practice

2. Instalar dependencias

pip install -r requirements.txt

Cómo ejecutar la aplicación

Opción 1: Usando Uvicorn directamente
    uvicorn app:app --reload 

app:app → se refiere al archivo app.py y al objeto app = FastAPI()

Opción 2: Usando un archivo run.py
Crea un archivo run.py con este contenido:

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

y se ejecuta con: 
python run.py



Rutas disponibles

GET /posts – Lista todos los posts

GET /posts/{id} – Ver un post por su ID

POST /posts – Crear un nuevo post

PUT /posts/{id} – Actualizar un post existente

DELETE /posts/{id} – Eliminar un post

Documentación automática:
Swagger UI: http://127.0.0.1:8000/docs


Desarrollado por: Cici160401