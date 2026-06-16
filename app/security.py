from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db


from app.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    try:
        ph.verify(hashed_password, password)
        return True
    except VerifyMismatchError:
        return False

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update(
        {
            "exp": expire
        }
    )
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

security = HTTPBearer()

def verify_token(credentials=Depends(security)):
    token = credentials.credentials
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError :
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

#El frontend debe de almacenar el token

def get_current_user(
    payload=Depends(verify_token),
    db: Session = Depends(get_db)
):
    id_usuario = payload.get("sub")
    resultado = db.execute(
        text("""
            SELECT
                id_usuario,
                nombre,
                apellido,
                correo,
                estado
            FROM usuarios
            WHERE id_usuario = :id
        """),
        {
            "id": int(id_usuario)
        }
    )
    usuario = resultado.mappings().first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Usuario no encontrado"
        )

    return usuario

def get_current_user_perfil(
    usuario=Depends(get_current_user)
):
    return usuario
