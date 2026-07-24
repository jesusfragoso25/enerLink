from pydantic import BaseModel

class TipoUsuarioCreate(BaseModel):
    rol: str
    
class TipoUsuarioUpdate(BaseModel):
    rol: str
    
class TipoUsuarioResponse(BaseModel):
    id_rol: int
    rol: str