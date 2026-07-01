from fastapi import FastAPI

try:
    from .enrutadores.clientes import rutas_clientes
    from .enrutadores.facturas import rutas_facturas
    from .enrutadores.transacciones import rutas_transacciones
except ImportError:
    from app.enrutadores.clientes import rutas_clientes
    from app.enrutadores.facturas import rutas_facturas
    from app.enrutadores.transacciones import rutas_transacciones

app = FastAPI(title="Proyecto Clientes")

# incluir ruta de clientes
app.include_router(rutas_clientes, tags=["Clientes"])
app.include_router(rutas_facturas, tags=["Facturas"])
app.include_router(rutas_transacciones, tags=["Transacciones"])