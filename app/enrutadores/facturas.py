from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from ..conexion_bd import Sesion_dependencia
from ..modelos.clientes import Cliente
from ..modelos.facturas import Factura, FacturaCrear

rutas_facturas = APIRouter()


@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas(sesion: Sesion_dependencia):
    consulta = select(Factura)
    return sesion.exec(consulta).all()


@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, sesion: Sesion_dependencia):
    factura = sesion.get(Factura, factura_id)
    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id}, no existe.",
        )
    return factura


@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(
    cliente_id: int,
    datos_factura: FacturaCrear,
    sesion: Sesion_dependencia,
):
    cliente_encontrado = sesion.get(Cliente, cliente_id)
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El cliente con id {cliente_id}, no existe.",
        )

    # validar datos de la factura-json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)

    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val


@rutas_facturas.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura, sesion: Sesion_dependencia):
    factura = sesion.get(Factura, id_factura)
    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {id_factura}, no existe.",
        )

    datos = datos_factura.model_dump(exclude_unset=True)
    for key, value in datos.items():
        setattr(factura, key, value)

    sesion.add(factura)
    sesion.commit()
    sesion.refresh(factura)
    return factura


@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int, sesion: Sesion_dependencia):
    factura = sesion.get(Factura, id_factura)
    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {id_factura}, no existe.",
        )

    sesion.delete(factura)
    sesion.commit()
    return factura