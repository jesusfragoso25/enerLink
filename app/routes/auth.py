#from urllib import response
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException, Response
from app.security import (get_current_user)


from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.usuario import UsuarioActualResponse
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

@router.post("/login", response_model=LoginResponse)
def login(
    credentials: LoginRequest,
    response: Response,
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
    
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,   
        samesite="lax",
        max_age=3600,
        path="/"
    )
    

    return LoginResponse(
        mensaje="Login exitoso",
        access_token=token,
        token_type="bearer"
    )
    
@router.post("/logout")
def logout(
    response: Response
):

    response.delete_cookie(
        key="access_token",
        path="/"
    )

    return {
        "mensaje": "Sesión cerrada correctamente"
    }
    
@router.get("/me",response_model=UsuarioActualResponse)
def me(
    usuario=Depends(get_current_user)
):
    return usuario