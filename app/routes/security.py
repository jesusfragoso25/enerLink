#################### CREO QUE ESTO NO ES NECESARIO####################
from fastapi import Depends
from fastapi import APIRouter
from app.security import (get_current_user)
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioUpdate


router = APIRouter()

@router.get("/me")
def obtener_mi_perfil(
    usuario_actual=Depends(get_current_user)
):
    return {
        "nombre_completo": f"{usuario_actual['nombre']} {usuario_actual['apellido']}",
        "telefono": usuario_actual["telefono"],
        "correo": usuario_actual["correo"]
    }


