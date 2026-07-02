# API REST - Gestión de Clientes, Facturas y Transacciones

## Desarrollador
- **Nombre:** Cristian Camilo Rojas Vesga
- **Programa:** ADSO
- **Institución:** SENA

## Descripción

Aplicación backend desarrollada con FastAPI y SQLModel para gestionar clientes, facturas y transacciones. El proyecto fue construido de forma progresiva, comenzando con una estructura básica y evolucionando hacia una arquitectura modular con relaciones de base de datos.

---

## Tecnologías

- Python 3.13+
- FastAPI
- SQLModel
- Pydantic v2
- SQLite
- Uvicorn

---

## Instalación y Ejecución

### Requisitos
- Python 3.13 o superior
- pip

### Pasos

1. Clonar el repositorio
```bash
git clone <URL>
cd PROYECTO_CLIENTES
```

2. Crear entorno virtual
```bash
python -m venv venv
```

3. Activar entorno
```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

4. Instalar dependencias
```bash
pip install -r requirements.txt
```

5. Ejecutar servidor
```bash
python -m fastapi dev app/main.py
```

Acceder a: http://127.0.0.1:8000/docs

---

## Proceso de Desarrollo

### ETAPA 1: Inicio sin estructura (Commit 1)

**Objetivo:** Crear los primeros archivos y endpoints sin organización

**Lo que se hizo:**
- Archivo `main.py` con código básico de FastAPI
- Primeros endpoints para clientes en el mismo archivo
- Sin separación de responsabilidades
- Pruebas básicas de funcionamiento

**Problemas identificados:**
- Código muy centralizado
- Difícil mantenimiento
- No hay modelos definidos
- Base de datos sin estructura

### ETAPA 2: Funcionamiento primario sin estructura (Commit 2)

**Objetivo:** Crear CRUD funcional con lista en memoria

**Lo que se hizo:**
- Creados archivos `listas.py` con datos temporales
- Endpoint GET, POST, PATCH, DELETE para clientes
- Validaciones básicas
- Pruebas en Swagger

**Problemas identificados:**
- Los datos se pierden al reiniciar
- Sin relacionar clientes con facturas
- Sin validaciones de base de datos
- Código aún muy junto

### ETAPA 3: Introducción de modelos con SQLModel (Commit 3)

**Objetivo:** Implementar base de datos real con SQLModel

**Lo que se hizo:**
- Creada carpeta `modelos/` con:
  - `clientes.py`: Modelo Cliente, ClienteCrear, ClienteLeer
  - `facturas.py`: Modelo Factura con relaciones
  - `transacciones.py`: Modelo Transaccion
- Archivo `conexion_bd.py` para configurar SQLModel y SQLite
- Crear tabla automáticamente al iniciar

**Desafíos:**
- Importaciones circulares entre modelos
- Relaciones bidireccionales complejas
- Configuración correcta de SQLModel

### ETAPA 4: Estructura modular completa (Commit 4)

**Objetivo:** Separar enrutadores por entidad

**Lo que se hizo:**
- Creada carpeta `enrutadores/` con:
  - `clientes.py`: CRUD cliente con sesión BD
  - `facturas.py`: CRUD factura con validación cliente
  - `transacciones.py`: CRUD transacción con validación factura
- Actualizar `main.py` para incluir routers
- Cada endpoint con validaciones y manejo de errores

**Mejoras logradas:**
- Código organizado por entidad
- Reutilización de código
- Fácil mantenimiento
- Escalabilidad

### ETAPA 5: Relaciones y campos computados (Commit 5)

**Objetivo:** Implementar relaciones completas y cálculos automáticos

**Lo que se hizo:**
- Relación Cliente → Factura (1 a N)
- Relación Factura → Transacción (1 a N)
- Campo `vr_total` computado automáticamente en Factura
- Validaciones de clientes y facturas antes de crear registros
- Foreign keys en base de datos

**Características:**
- El total de una factura se calcula sumando transacciones
- Al eliminar transacción, el total se actualiza automáticamente
- Validaciones para evitar inconsistencias

### ETAPA 6: Correcciones y optimización (Commit 6)

**Objetivo:** Solucionar errores de importación y estructura

**Lo que se hizo:**
- Arregladas importaciones circulares con TYPE_CHECKING
- Movida clase `ClienteLeer` fuera de `Cliente`
- Corregida indentación del método `vr_total`
- Actualizado `enrutadores/facturas.py` con nombre correcto de modelo
- Instaladas todas las dependencias correctamente

**Errores corregidos:**
- `ModuleNotFoundError: No module named 'sqlmodel'`
- `ImportError: cannot import name 'Factura'`
- Indentación incorrecta en métodos
- Typos en nombres de clases

---

## Estructura Final del Proyecto

```
PROYECTO_CLIENTES/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada
│   ├── conexion_bd.py          # Configuración BD
│   ├── listas.py               # Datos temporales
│   │
│   ├── modelos/                # Modelos SQLModel
│   │   ├── __init__.py
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   └── enrutadores/            # Endpoints/Rutas
│       ├── __init__.py
│       ├── clientes.py
│       ├── facturas.py
│       └── transacciones.py
│
├── bd_clientes.sqlite3
├── README.md
└── requirements.txt
```

---

## Relaciones de Base de Datos

```
CLIENTE
├── id (PK)
├── nombre
├── email
└── descripcion
    └── Relación: Cliente ─── (1:N) ───→ FACTURA


FACTURA
├── id (PK)
├── fecha
├── cliente_id (FK)
├── vr_total (computed)
└── Relación con Cliente
    └── Relación: Factura ─── (1:N) ───→ TRANSACCION


TRANSACCION
├── id (PK)
├── cantidad
├── vr_unitario
├── descripcion
├── factura_id (FK)
└── Relación con Factura
```

El campo `vr_total` en Factura se calcula como: ∑(cantidad × vr_unitario) de todas sus transacciones

---

## CRUD Endpoints

### Clientes
- GET `/clientes` - Listar todos
- GET `/clientes/{id}` - Obtener uno
- POST `/clientes` - Crear
- PATCH `/clientes/{id}` - Actualizar
- DELETE `/clientes/{id}` - Eliminar

### Facturas  
- GET `/facturas` - Listar todas
- GET `/facturas/{id}` - Obtener una
- POST `/facturas/{cliente_id}` - Crear
- PATCH `/facturas/{id}` - Actualizar
- DELETE `/facturas/{id}` - Eliminar

### Transacciones
- GET `/transacciones` - Listar todas
- GET `/transacciones/{id}` - Obtener una
- POST `/transacciones/{factura_id}` - Crear
- PATCH `/transacciones/{id}` - Actualizar
- DELETE `/transacciones/{id}` - Eliminar

---

## Commits en Git

Para revisar el proceso completo, navegar entre commits:

```bash
git log --oneline
```

Cada commit corresponde a una etapa del desarrollo documentada en este README.

---

## Lecciones Aprendidas

1. **Importaciones circulares**: Usar TYPE_CHECKING para evitarlas
2. **SQLModel**: Combina SQLAlchemy + Pydantic perfectamente
3. **Relaciones**: Las relaciones bidireccionales requieren `back_populates`
4. **Campos computados**: `@computed_field` calcula valores automáticamente
5. **Validaciones**: Pydantic v2 valida datos antes de guardar
6. **Manejo de errores**: HTTPException con status codes adecuados

---

## Despliegue

Para desplegar en producción:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

O usar Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

---

## Contacto

Cristian Camilo Rojas Vesga - ADSO SENA

