from pydantic import BaseModel
from datetime import datetime

class ViviendaCreate(BaseModel):
    id_usuario: int
    nombre: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    departamento: str | None = None
    pais: str | None = None
    estado: bool | None = None
    
class ViviendaCreate_sin_id_usuario(BaseModel):
    nombre: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    departamento: str | None = None
    pais: str | None = None
    estado: bool | None = None
    
class ViviendaUpdate(BaseModel):
    nombre: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    departamento: str | None = None
    pais: str | None = None
    estado: bool | None = None
    
class ViviendaResponse(BaseModel):
    id_usuario: int
    nombre: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    departamento: str | None = None
    pais: str | None = None
    fecha_creacion: datetime |None = None
    estado: bool | None = None
    
    
    
    