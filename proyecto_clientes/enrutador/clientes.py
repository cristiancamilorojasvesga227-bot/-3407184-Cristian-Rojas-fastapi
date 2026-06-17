from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..conexion_bd import get_db
from ..models.clientes import Cliente
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/clientes", tags=["Clientes"])

class ClienteCrear(BaseModel):
    nombre: str
    correo: str
    telefono: Optional[str] = None

class ClienteRespuesta(BaseModel):
    id: int
    nombre: str
    correo: str
    telefono: Optional[str] = None

    class Config:
        from_attributes = True

@router.get("/", response_model=list[ClienteRespuesta])
def listar_clientes(db: Session = Depends(get_db)):
    return db.exec(select(Cliente)).all()

@router.get("/{cliente_id}", response_model=ClienteRespuesta)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.exec(select(Cliente).where(Cliente.id == cliente_id)).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/", response_model=ClienteRespuesta)
def crear_cliente(cliente: ClienteCrear, db: Session = Depends(get_db)):
    nuevo = Cliente(**cliente.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{cliente_id}", response_model=ClienteRespuesta)
def actualizar_cliente(cliente_id: int, datos: ClienteCrear, db: Session = Depends(get_db)):
    cliente = db.exec(select(Cliente).where(Cliente.id == cliente_id)).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for key, value in datos.dict().items():
        setattr(cliente, key, value)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.exec(select(Cliente).where(Cliente.id == cliente_id)).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(cliente)
    db.commit()
    return {"mensaje": "Cliente eliminado correctamente"}
