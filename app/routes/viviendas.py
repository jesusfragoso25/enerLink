from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.viviendas import ViviendaCreate, ViviendaUpdate, ViviendaResponse, ViviendaCreate_sin_id_usuario
from app.security import (get_current_user)
from app.services import viviendas

router = APIRouter(prefix="/viviendas", tags=["Viviendas"])

#CREAR VIVIENDA PARA CUALQUIER USUARIO 
@router.post("/_crear_vivienda/", response_model=ViviendaResponse)
def crear_vivienda(vivienda: ViviendaCreate, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return viviendas.crear_vivienda(db, vivienda, usuario_actual["id_usuario"])

#CREAR VIVIENDA PARA EL USUARIO QUE ESTE AUTENTICADO 
@router.post("/_crear_vivienda_ath/", response_model=ViviendaResponse)
def crear_vivienda_ath(vivienda: ViviendaCreate_sin_id_usuario, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return viviendas.crear_vivienda_ath(db, vivienda, usuario_actual["id_usuario"])

#MOSTRAR TODAS LAS VIVIENDAS DE TODOS LOS USUARIOS
@router.get("/_mostrar_todas_viviendas/", response_model=list[ViviendaResponse])
def obtener_viviendas(usuario_actual = Depends(get_current_user),db: Session = Depends(get_db)):
    return viviendas.obtener_viviendas(db, usuario_actual["id_usuario"])

#MOSTRAR VIVIENDAS POR ID DE USUARIO SIN NECECIDAD DE INGRESAR EL ID YA QUE LO TOMA DEL TOKEN DE AUTENTICACION   
@router.get("/_mis_viviendas/")
def obtener_viviendas_por_usuario(usuario_actual = Depends(get_current_user),db: Session = Depends(get_db)):
    return viviendas.obtener_viviendas_por_usuario(db, usuario_actual["id_usuario"])

#MOSTRAR VIVIENDA POR ID DE VIVIENDA
@router.get("/_mostrar_vivienda_por_id/{id_vivienda}", response_model=ViviendaResponse)
def obtener_vivienda(id_vivienda: int,usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return viviendas.obtener_vivienda(db, id_vivienda, usuario_actual["id_usuario"])

#MOSTRAR VIVIENDAS POR ID DE USUARIO INGRENSANDO ID   
"""@router.get("_por_usuario/{id_usuario}", response_model=list[ViviendaResponse])
def obtener_viviendas_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    return viviendas.obtener_viviendas_por_usuario(db, id_usuario)"""

#ELIMINAR VIVIENDA POR ID DE VIVIENDA UNICAMENTE LAS QUE PERTENECEN AL USUARIO QUE ESTA AUTENTICADO
@router.delete("/_eliminar_vivienda/{id_vivienda}")
def eliminar_vivienda(id_vivienda: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return viviendas.eliminar_vivienda(db, id_vivienda, usuario_actual["id_usuario"])


