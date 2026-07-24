from pydantic import BaseModel
from pydantic import EmailStr

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str
    
class LoginResponse(BaseModel):
    mensaje: str
    access_token: str | None=None
    token_type: str | None=None