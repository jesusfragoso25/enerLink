from pydantic import BaseModel
from datetime import datetime

class GatewayCreate(BaseModel):
    id_gateway: int
    id_vivienda: int
    uuid_gateway: str
    nombre_gateway: str
    estado: bool | None = None

class GatewayCreate_sin_id_usuario(BaseModel):
    id_vivienda: int
    uuid_gateway: str
    nombre_gateway: str
    estado: bool | None = None

class GatewayUpdate(BaseModel):
    id_vivienda: int
    uuid_gateway: str
    nombre_gateway: str
    estado: bool | None = None
    

class GatewayResponse(BaseModel):
    id_gateway: int
    id_vivienda: int
    uuid_gateway: str
    nombre_gateway: str
    fecha_instalacion: datetime | None = None
    estado: bool | None = None   
    
    