from __future__ import annotations
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    telefono: Optional[str] = None
    facturas: List["Factura"] = Relationship(back_populates="cliente")
