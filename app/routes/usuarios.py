from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.database import get_db
from app.schemas.usuario import UsuarioCreate
from app.security import hash_password
from app.schemas.usuario import UsuarioUpdate
from app.security import (get_current_user)

router = APIRouter()
############################# REGISTOR DE USUSARIO

@router.post("/register")
def register_user(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    password_hash = hash_password(
        usuario.password
    )
    try:
        db.execute(
            text("""
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                cedula,
                correo,
                password_hash,
                id_rol 
            )
            VALUES
            (
                :nombre,
                :apellido,
                :cedula,
                :correo,
                :password_hash,
                :id_rol
            )
            """),
            {
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "cedula": usuario.cedula,
                "correo": usuario.correo,
                "password_hash": password_hash,
                "id_rol" : "1" # el usuario POR DEFECTO siempre sera de tipo administrador
            }
        )

        db.commit()
    #si el usuario ya tiene cedula me devuelve mensaje este mensaje de error.
    except IntegrityError as e:
        db.rollback()
        msg = str(e).lower()
        if 'usuarios_cedula_key' in msg or 'unique constraint' in msg and 'cedula' in msg:
            raise HTTPException(status_code=409, detail="cedula existente")
        raise HTTPException(status_code=400, detail="error de integridad")

    return {
        "mensaje":"Usuario registrado"
    }


@router.put("/me")
def actualizar_usuario(
    datos: UsuarioUpdate,
    usuario_actual = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resultado = db.execute(
        text("""
            UPDATE usuarios
            SET
                nombre = :nombre,
                apellido = :apellido,
                correo = :correo
            WHERE id_usuario = :id
        """),
        {
            "id": usuario_actual["id_usuario"],
            "nombre": datos.nombre,
            "apellido": datos.apellido,
            "correo": datos.correo
        }
    )

    db.commit()

    if resultado.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario actualizado"
    }

@router.delete("/me")
def eliminar_usuario(
    usuario_actual = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    resultado = db.execute(
        text("""
            DELETE FROM usuarios
            WHERE id_usuario = :id
        """),
        {
            "id": usuario_actual["id_usuario"]
        }
    )

    db.commit()

    if resultado.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "mensaje": "Usuario eliminado"
    }
    
