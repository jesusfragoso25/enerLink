from sqlalchemy import Column, func, Integer, Boolean, String, ForeignKey, DateTime
from app.database import Base
from sqlalchemy.orm import relationship


class Nodos(Base):
    __tablename__ = "nodos"
    id_nodo = Column(Integer, primary_key=True, index=True)
    id_gateway = Column(Integer, ForeignKey("gateways.id_gateway"), nullable=False)
    id_tipo_nodo = Column("id_tipo", Integer, ForeignKey("tipos_dispositivo.id_tipo"), nullable=False)
    uuid_nodo = Column(String, nullable=False, unique=True)
    mac_address = Column(String, nullable=True)
    nombre_nodo = Column(String, nullable=False)
    ubicacion = Column(String, nullable=True)
    fecha_asociacion = Column(DateTime, server_default=func.now(), nullable=True)
    estado = Column(Boolean, default=True)