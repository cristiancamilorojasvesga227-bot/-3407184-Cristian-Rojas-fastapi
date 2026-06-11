from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.transacciones import Transaccion
from pydantic import BaseModel

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

class TransaccionCrear(BaseModel):
    descripcion: str
    factura_id: int

class TransaccionRespuesta(BaseModel):
    id: int
    descripcion: str
    factura_id: int

    class Config:
        from_attributes = True

@router.get("/", response_model=list[TransaccionRespuesta])
def listar_transacciones(db: Session = Depends(get_db)):
    return db.query(Transaccion).all()

@router.get("/{transaccion_id}", response_model=TransaccionRespuesta)
def obtener_transaccion(transaccion_id: int, db: Session = Depends(get_db)):
    t = db.query(Transaccion).filter(Transaccion.id == transaccion_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return t

@router.post("/", response_model=TransaccionRespuesta)
def crear_transaccion(transaccion: TransaccionCrear, db: Session = Depends(get_db)):
    nueva = Transaccion(**transaccion.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{transaccion_id}", response_model=TransaccionRespuesta)
def actualizar_transaccion(transaccion_id: int, datos: TransaccionCrear, db: Session = Depends(get_db)):
    t = db.query(Transaccion).filter(Transaccion.id == transaccion_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    for key, value in datos.model_dump().items():
        setattr(t, key, value)
    db.commit()
    db.refresh(t)
    return t

@router.delete("/{transaccion_id}")
def eliminar_transaccion(transaccion_id: int, db: Session = Depends(get_db)):
    t = db.query(Transaccion).filter(Transaccion.id == transaccion_id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    db.delete(t)
    db.commit()
    return {"mensaje": "Transacción eliminada correctamente"}
