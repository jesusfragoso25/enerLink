from sqlalchemy import Column, func, Integer, Boolean, String, ForeignKey, DateTime

from app.database import Base

#from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


class Viviendas(Base):
    __tablename__ = "viviendas"
    id_vivienda = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer,ForeignKey("usuarios.id_usuario"), nullable=False)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=True)
    ciudad = Column(String, nullable=True)
    departamento = Column(String, nullable=True)
    pais = Column(String, nullable=True)
    fecha_creacion = Column(DateTime,server_default=func.now(),nullable=True)
    estado = Column(Boolean, default=True)
    
    usuario = relationship("Usuario", back_populates="viviendas")
    gateways = relationship("Gateways", back_populates="vivienda")
    