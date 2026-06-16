from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    cedula = Column(String)
    correo = Column(String, unique=True)
    password_hash = Column(String)
