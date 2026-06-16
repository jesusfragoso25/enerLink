from pydantic import BaseModel
from pydantic import EmailStr

class LoginRequest(BaseModel):
    correo: EmailStr
    password: str