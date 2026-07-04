from pydantic import BaseModel
from datetime import datetime

from sqlalchemy import Column


class TiposDispositivoCreate(BaseModel):
    nombre_tipo: str | None = None
    descripcion: str | None = None

class TiposDispositivoUpdate(BaseModel):
    nombre_tipo: str | None = None
    descripcion: str | None = None
    
class TiposDispositivoResponse(BaseModel):
    id_tipo: int 
    nombre_tipo: str | None = None
    descripcion: str | None = None