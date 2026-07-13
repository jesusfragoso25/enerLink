from sqlalchemy import Column, func, Integer, Boolean, String, ForeignKey, DateTime

from app.database import Base

#from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

class Gateways(Base):
    __tablename__ = "gateways"
    id_gateway = Column(Integer, primary_key=True, index=True)
    id_vivienda = Column(Integer, ForeignKey("viviendas.id_vivienda"), nullable=False)
    uuid_gateway = Column(String, nullable=False, unique=True)  
    nombre_gateway = Column(String, nullable=False) 
    fecha_instalacion = Column(DateTime,server_default=func.now(),nullable=True)
    estado = Column(Boolean, default=True)
    
    vivienda = relationship("Viviendas", back_populates="gateways")
    
