from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.gateways import GatewayCreate, GatewayUpdate, GatewayResponse, GatewayCreate_sin_id_usuario
from app.security import (get_current_user)
from app.services import gateways

router = APIRouter(prefix="/gateways", tags=["Gateways"])

#CREAR GATEWAY PARA CUALQUIER USUARIO 
@router.post("/_crear_gateway/", response_model=GatewayResponse)
def crear_gateway(gateway: GatewayCreate, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.crear_gateway(db, gateway, usuario_actual["id_usuario"])

#CREAR GATEWAY PARA EL USUARIO QUE ESTE AUTENTICADO 
@router.post("/_crear_gateway_ath/", response_model=GatewayResponse)
def crear_gateway_ath(gateway: GatewayCreate_sin_id_usuario, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return gateways.crear_gateway_ath(db, gateway, usuario_actual["id_usuario"])


"""

#MOSTRAR TODOS LOS GATEWAY DE TODOS LOS USUARIOS
@router.get("/_mostrar_todas_gateway/", response_model=list[GatewayResponse])
def obtener_gateway(usuario_actual = Depends(get_current_user),db: Session = Depends(get_db)):
    return Gateways.obtener_gateway(db, usuario_actual["id_usuario"])

#MOSTRAR GATEWAY POR ID DE USUARIO SIN NECECIDAD DE INGRESAR EL ID YA QUE LO TOMA DEL TOKEN DE AUTENTICACION   
@router.get("/_mis_gateway/")
def obtener_gateway_por_usuario(usuario_actual = Depends(get_current_user),db: Session = Depends(get_db)):
    return Gateways.obtener_gateway_por_usuario(db, usuario_actual["id_usuario"])

#MOSTRAR GATEWAY POR ID DE VIVIENDA
@router.get("/_mostrar_gateway_por_id/{id_gateway}", response_model=GatewayResponse)
def obtener_gateway_por_id(id_gateway: int,usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return Gateways.obtener_gateway_por_id(db, id_gateway, usuario_actual["id_usuario"])

#ELIMINAR GATEWAY POR ID DE GATEWAY UNICAMENTE LAS QUE PERTENECEN AL USUARIO QUE ESTA AUTENTICADO
@router.delete("/_eliminar_gateway/{id_gateway}")
def eliminar_gateway(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return Gateways.eliminar_gateway(db, id_gateway, usuario_actual["id_usuario"])
    
    
"""