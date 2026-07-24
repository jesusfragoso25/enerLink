from sqlalchemy import Column, BigInteger, Integer, Numeric, DateTime, ForeignKey, func
from app.database import Base


class Mediciones(Base):
    __tablename__ = "mediciones"
    id_medicion = Column(BigInteger, primary_key=True, index=True)
    id_nodo = Column(Integer, ForeignKey("nodos.id_nodo"), nullable=False)
    voltaje = Column(Numeric, nullable=True)
    corriente = Column(Numeric, nullable=True)
    potencia = Column(Numeric, nullable=True)
    energia_kwh = Column(Numeric, nullable=True)
    factor_potencia = Column(Numeric, nullable=True)
    fecha_hora = Column(DateTime, server_default=func.now(), nullable=True)