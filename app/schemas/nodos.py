from pydantic import BaseModel
from datetime import datetime

class NodoCreate(BaseModel):
    id_gateway: int | None = None
    id_tipo_nodo: int | None = None
    uuid_nodo: str | None = None
    mac_address: str | None = None
    nombre_nodo: str | None = None
    ubicacion: str | None = None
    fecha_asociacion: datetime | None = None
    estado: bool | None = None

class NodoUpdate(BaseModel):
    id_gateway: int | None = None
    id_tipo_nodo: int | None = None
    uuid_nodo: str | None = None
    mac_address: str | None = None
    nombre_nodo: str | None = None
    ubicacion: str | None = None
    fecha_asociacion: datetime | None = None
    estado: bool | None = None
    
class NodoResponse(BaseModel):
    id_nodo: int
    id_gateway: int | None = None
    id_tipo_nodo: int | None = None
    uuid_nodo: str | None = None
    mac_address: str | None = None
    nombre_nodo: str | None = None
    ubicacion: str | None = None
    fecha_asociacion: datetime | None = None
    estado: bool | None = None
    