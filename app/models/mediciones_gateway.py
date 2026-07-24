from sqlalchemy import Column, BigInteger, Integer, Numeric, DateTime, ForeignKey, func
from app.database import Base


class MedicionesGateway(Base):
    __tablename__ = "mediciones_gateway"
    id_medicion_g = Column(BigInteger, primary_key=True, index=True)
    id_gateway = Column(Integer, ForeignKey("gateways.id_gateway"), nullable=False)
    fecha_hora = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    energia_kwh = Column(Numeric, nullable=True)