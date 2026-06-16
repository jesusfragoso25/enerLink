from fastapi import Depends
from fastapi import APIRouter
from app.security import (get_current_user)
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioUpdate


router = APIRouter()

@router.get("/me")
def obtener_mi_perfil(
    usuario_actual = Depends(get_current_user),
    db: Session = Depends(get_db)

):
  return {
    "mensaje": "Usuario consultado"
} # return usuario
