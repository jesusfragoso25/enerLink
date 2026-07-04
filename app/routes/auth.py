from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.schemas.auth import LoginRequest
from app.security import (verify_password,create_access_token)

############# LOGIN DE USUARIO

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.get("/health")
def health():
    return {
        "status": "ok"
    }

@router.post("/login")
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    resultado = db.execute(
        text("""
            SELECT
                id_usuario,
                nombre,
                correo,
                password_hash,
                id_rol
            FROM usuarios
            WHERE correo = :correo
        """),
        {
            "correo": credentials.correo
        }
    )

    usuario = resultado.mappings().first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    if not verify_password(
        credentials.password,
        usuario["password_hash"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    token = create_access_token(
        {
            "sub": str(usuario["id_usuario"]),
            "correo": usuario["correo"],
            "id_rol": usuario["id_rol"],
        }
    )

    return {
        "mensaje": "Login exitoso",
        "access_token": token,
        "token_type": "bearer"
    }