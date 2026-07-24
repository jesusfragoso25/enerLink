from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.mediciones import ConsumoGatewayResponse, ConsumoSemanalGatewayResponse
from app.security import get_current_user
from app.services import mediciones_gateway
from app.schemas.mediciones import ConsumoAnualTotalResponse
from app.schemas.mediciones import ConsumoTotalResponse, ConsumoSemanalTotalResponse

router = APIRouter(prefix="/mediciones_gateway", tags=["MedicionesGateway"])


#CONSUMO DEL DIA ACTUAL DE UN GATEWAY
@router.get("/_consumo_diario/{id_gateway}", response_model=ConsumoGatewayResponse)
def consumo_diario(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_diario_por_gateway(db, id_gateway, usuario_actual["id_usuario"])


#CONSUMO DEL MES ACTUAL DE UN GATEWAY
@router.get("/_consumo_mensual/{id_gateway}", response_model=ConsumoGatewayResponse)
def consumo_mensual(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_mensual_por_gateway(db, id_gateway, usuario_actual["id_usuario"])


#CONSUMO AGRUPADO POR DIA DE LA SEMANA ACTUAL
@router.get("/_consumo_semanal/{id_gateway}", response_model=ConsumoSemanalGatewayResponse)
def consumo_semanal(id_gateway: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_semanal_por_gateway(db, id_gateway, usuario_actual["id_usuario"])

#CONSUMO TOTAL DEL DIA ACTUAL (TODOS LOS GATEWAYS DEL USUARIO)
@router.get("/_consumo_diario_total/", response_model=ConsumoTotalResponse)
def consumo_diario_total(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_diario_total_usuario(db, usuario_actual["id_usuario"])


#CONSUMO TOTAL DEL MES ACTUAL (TODOS LOS GATEWAYS DEL USUARIO)
@router.get("/_consumo_mensual_total/", response_model=ConsumoTotalResponse)
def consumo_mensual_total(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_mensual_total_usuario(db, usuario_actual["id_usuario"])


#CONSUMO TOTAL AGRUPADO POR DIA DE LA SEMANA ACTUAL (TODOS LOS GATEWAYS DEL USUARIO)
@router.get("/_consumo_semanal_total/", response_model=ConsumoSemanalTotalResponse)
def consumo_semanal_total(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_semanal_total_usuario(db, usuario_actual["id_usuario"])

#HISTORICO ANUAL AGRUPADO POR MES (TODOS LOS GATEWAYS DEL USUARIO)
@router.get("/_consumo_anual_total/", response_model=ConsumoAnualTotalResponse)
def consumo_anual_total(usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones_gateway.consumo_anual_total_usuario(db, usuario_actual["id_usuario"])