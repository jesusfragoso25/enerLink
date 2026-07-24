from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.nodos import NodoCreate, NodoUpdate, NodoResponse
from app.security import get_current_user
from app.services import nodos

router = APIRouter(prefix="/nodos", tags=["Nodos"])


#CREAR NODO PARA CUALQUIER GATEWAY (SIN VALIDAR PROPIETARIO)
@router.post("/_crear_nodo/", response_model=NodoResponse)
def crear_nodo(nodo: NodoCreate, db: Session = Depends(get_db)):
    return nodos.crear_nodo(db, nodo)


#CREAR NODO PARA UN GATEWAY DEL USUARIO AUTENTICADO
@router.post("/_crear_nodo_ath/", response_model=NodoResponse)
def crear_nodo_ath(nodo: NodoCreate, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return nodos.crear_nodo_ath(db, nodo, usuario_actual["id_usuario"])


#MOSTRAR TODOS LOS NODOS DEL USUARIO AUTENTICADO
@router.get("/_mis_nodos/", response_model=List[NodoResponse])
def obtener_nodos_por_usuario(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return nodos.obtener_nodos_por_usuario(db, usuario_actual["id_usuario"])


#MOSTRAR NODOS DE UN GATEWAY ESPECIFICO DEL USUARIO AUTENTICADO
@router.get("/_por_gateway/{id_gateway}", response_model=List[NodoResponse])
def obtener_nodos_por_gateway(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return nodos.obtener_nodos_por_gateway(db, id_gateway, usuario_actual["id_usuario"])


#MOSTRAR NODO POR ID DE NODO
@router.get("/_mostrar_nodo_por_id/{id_nodo}", response_model=NodoResponse)
def obtener_nodo_por_id(id_nodo: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return nodos.obtener_nodo_por_id(db, id_nodo, usuario_actual["id_usuario"])


#ELIMINAR NODO POR ID DE NODO, UNICAMENTE LOS QUE PERTENECEN AL USUARIO AUTENTICADO
@router.delete("/_eliminar_nodo/{id_nodo}")
def eliminar_nodo(id_nodo: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return nodos.eliminar_nodo(db, id_nodo, usuario_actual["id_usuario"])

