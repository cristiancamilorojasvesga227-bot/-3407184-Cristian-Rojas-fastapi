from fastapi import FastAPI
from .conexion_bd import engine, SQLModel
from .enrutador import clientes, facturas, transacciones

# Genera automáticamente las tablas en SQLite si no existen
SQLModel.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Comercial Relacional",
    description="CRUD Clientes, Facturas y Transacciones con SQLModel",
    version="1.0.0"
)

app.include_router(clientes.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)

@app.get("/", tags=["Inicio"])
def root():
    return {
        "mensaje": "Servidor funcionando correctamente",
        "documentacion": "/docs"
    }
