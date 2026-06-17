from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..conexion_bd import get_db
from ..models.facturas import Factura
from pydantic import BaseModel
from datetime import date

router = APIRouter(prefix="/facturas", tags=["Facturas"])

class FacturaCrear(BaseModel):
    fecha: date
    cliente_id: int
    valortotal: float

class FacturaRespuesta(BaseModel):
    id: int
    fecha: date
    cliente_id: int
    valortotal: float

    class Config:
        from_attributes = True

@router.get("/", response_model=list[FacturaRespuesta])
def listar_facturas(db: Session = Depends(get_db)):
    return db.exec(select(Factura)).all()

@router.get("/{factura_id}", response_model=FacturaRespuesta)
def obtener_factura(factura_id: int, db: Session = Depends(get_db)):
    factura = db.exec(select(Factura).where(Factura.id == factura_id)).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura

@router.post("/", response_model=FacturaRespuesta)
def crear_factura(factura: FacturaCrear, db: Session = Depends(get_db)):
    nueva = Factura(**factura.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{factura_id}", response_model=FacturaRespuesta)
def actualizar_factura(factura_id: int, datos: FacturaCrear, db: Session = Depends(get_db)):
    factura = db.exec(select(Factura).where(Factura.id == factura_id)).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    for key, value in datos.dict().items():
        setattr(factura, key, value)
    db.add(factura)
    db.commit()
    db.refresh(factura)
    return factura

@router.delete("/{factura_id}")
def eliminar_factura(factura_id: int, db: Session = Depends(get_db)):
    factura = db.exec(select(Factura).where(Factura.id == factura_id)).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    db.delete(factura)
    db.commit()
    return {"mensaje": "Factura eliminada correctamente"}
