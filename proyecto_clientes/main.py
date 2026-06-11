from fastapi import FastAPI
from .database import engine, Base
from .routers import clientes, facturas, transacciones

# Genera automáticamente las tablas en SQLite si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Comercial Relacional",
    description="CRUD Clientes, Facturas y Transacciones",
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
