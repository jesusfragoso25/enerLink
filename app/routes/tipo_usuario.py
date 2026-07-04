from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tipo_usuario import TipoUsuarioCreate, TipoUsuarioUpdate, TipoUsuarioResponse
from app.security import (get_current_user)
from app.services import tipo_usuario as tipos_usuario

router = APIRouter(prefix="/tipo_usuario", tags=["TipoUsuario"])


@router.post("/_crear_tipo_usuario/", response_model=TipoUsuarioResponse)
def crear_tipo_usuario(tipo_usuario: TipoUsuarioCreate, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return tipos_usuario.crear_tipo_usuario(db, tipo_usuario, usuario_actual["id_usuario"])



