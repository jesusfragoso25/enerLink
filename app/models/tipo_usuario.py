from sqlalchemy import Column, func, Integer, Boolean, String, ForeignKey, DateTime
from app.database import Base
from sqlalchemy.orm import relationship

class TipoUsuario(Base):
    __tablename__ = "tipo_usuario"
    id_rol = Column(Integer, primary_key=True, index=True)
    rol = Column(String, nullable=False)
    
   
    #nodos = relationship("TiposDispositivo", back_populates="nodos")
    
    
    