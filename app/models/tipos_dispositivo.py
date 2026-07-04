from sqlalchemy import Column, func, Integer, Boolean, String, ForeignKey, DateTime

from app.database import Base
 
#from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


class TiposDispositivo(Base):
    __tablename__ = "tipos_dispositivo"
    id_tipo = Column(Integer, primary_key=True, index=True)
    nombre_tipo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    
    #nodos = relationship("TiposDispositivo", back_populates="nodos")
    
    
    