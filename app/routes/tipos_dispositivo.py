from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tipos_dispositivo import TiposDispositivoCreate, TiposDispositivoUpdate, TiposDispositivoResponse
from app.security import (get_current_user)
from app.services import tipos_dispositivo
from typing import List


router = APIRouter(prefix="/tipos_dispositivo", tags=["TiposDispositivo"])


@router.post("/_crear_tipo_dispositivo/", response_model=TiposDispositivoResponse)
def crear_tipo_dispositivo(tipo_dispositivo: TiposDispositivoCreate, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return tipos_dispositivo.crear_tipo_dispositivo(db, tipo_dispositivo, usuario_actual["id_usuario"])

#MOSTRAR TODOS LOS TIPOS DE DISPOSITIVO
@router.get("/_mostrar_tipos/", response_model=List[TiposDispositivoResponse])
def obtener_tipos_dispositivo(db: Session = Depends(get_db)):
    return tipos_dispositivo.obtener_tipos_dispositivo(db)


#MOSTRAR TIPO DE DISPOSITIVO POR ID
@router.get("/_mostrar_tipo_por_id/{id_tipo}", response_model=TiposDispositivoResponse)
def obtener_tipo_dispositivo_por_id(id_tipo: int, db: Session = Depends(get_db)):
    return tipos_dispositivo.obtener_tipo_dispositivo_por_id(db, id_tipo)





 


