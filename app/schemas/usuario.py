from pydantic import BaseModel
from pydantic import EmailStr

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    cedula: str
    correo: EmailStr
    password: str

class UsuarioUpdate(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
