from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.gateways import GatewayCreate, GatewayUpdate, GatewayResponse, GatewayCreate_sin_id_usuario
from app.security import get_current_user
from app.services import gateways

router = APIRouter(prefix="/gateways", tags=["Gateways"])


#CREAR GATEWAY PARA CUALQUIER USUARIO (SIN VALIDAR PROPIETARIO)
@router.post("/_crear_gateway/", response_model=GatewayResponse)
def crear_gateway(gateway: GatewayCreate, db: Session = Depends(get_db)):
    return gateways.crear_gateway(db, gateway)


#CREAR GATEWAY PARA EL USUARIO QUE ESTE AUTENTICADO
@router.post("/_crear_gateway_ath/", response_model=GatewayResponse)
def crear_gateway_ath(gateway: GatewayCreate_sin_id_usuario, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.crear_gateway_ath(db, gateway, usuario_actual["id_usuario"])


#MOSTRAR TODOS LOS GATEWAYS DEL USUARIO AUTENTICADO
@router.get("/_mis_gateway/", response_model=List[GatewayResponse])
def obtener_gateway_por_usuario(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.obtener_gateway_por_usuario(db, usuario_actual["id_usuario"])


#MOSTRAR GATEWAY POR ID DE GATEWAY
@router.get("/_mostrar_gateway_por_id/{id_gateway}", response_model=GatewayResponse)
def obtener_gateway_por_id(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.obtener_gateway_por_id(db, id_gateway, usuario_actual["id_usuario"])


#ELIMINAR GATEWAY POR ID DE GATEWAY, UNICAMENTE LOS QUE PERTENECEN AL USUARIO AUTENTICADO
@router.delete("/_eliminar_gateway/{id_gateway}")
def eliminar_gateway(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.eliminar_gateway(db, id_gateway, usuario_actual["id_usuario"])

    #MOSTRAR GATEWAYS DE UNA VIVIENDA ESPECIFICA DEL USUARIO AUTENTICADO
@router.get("/_por_vivienda/{id_vivienda}", response_model=List[GatewayResponse])
def obtener_gateways_por_vivienda(id_vivienda: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.obtener_gateways_por_vivienda(db, id_vivienda, usuario_actual["id_usuario"])