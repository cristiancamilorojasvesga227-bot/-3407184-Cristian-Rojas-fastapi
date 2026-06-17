from __future__ import annotations
from datetime import date
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class Factura(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: date
    cliente_id: int = Field(foreign_key="clientes.id")
    valortotal: float
    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: List["Transaccion"] = Relationship(back_populates="factura")
