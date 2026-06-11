# PROYECTO CLIENTES - FASTAPI

## 👤 Información del Desarrollador

* **Nombre:** Cristian Camilo Rojas Vesga
* **Ficha:** 3407184

---

# 📁 Estructura del Proyecto

```text
proyecto_clientes/
│
├── models/
│   ├── __init__.py
│   ├── clientes.py
│   ├── facturas.py
│   └── transacciones.py
│
├── routers/
│   ├── __init__.py
│   ├── clientes.py
│   ├── facturas.py
│   └── transacciones.py
│
├── venv/
├── base_datos.db
├── database.py
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 📌 Descripción

Proyecto desarrollado con FastAPI utilizando arquitectura modular, SQLite y SQLAlchemy.

La API permite administrar:

* Clientes
* Facturas
* Transacciones

Incluye operaciones CRUD completas:

* GET
* POST
* PUT
* DELETE

---

# 🛠️ Tecnologías Utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

---

# 🚀 Instrucciones de Ejecución (Windows)

## 1️⃣ Crear entorno virtual

```bash
python -m venv venv
```

## 2️⃣ Activar entorno virtual

```bash
venv\Scripts\activate
```

## 3️⃣ Instalar dependencias

```bash
pip install "fastapi[standard]" sqlalchemy
```

## 4️⃣ Ejecutar servidor

```bash
fastapi dev main.py
```

---

# 🌐 Documentación Swagger

Una vez ejecutado el servidor, ingresar a:

```
http://127.0.0.1:8000/docs
```

---

# ✅ Autor

**Cristian Camilo Rojas Vesga**
Ficha ADSO: **3407184**
