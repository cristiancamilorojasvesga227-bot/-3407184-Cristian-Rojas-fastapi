from __future__ import annotations
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

class Transaccion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descripcion: str
    factura_id: int = Field(foreign_key="facturas.id")
    factura: Optional["Factura"] = Relationship(back_populates="transacciones")
