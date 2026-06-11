from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from ..database import Base

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    valortotal = Column(Float, nullable=False)
