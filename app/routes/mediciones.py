from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.mediciones import ConsumoResponse
from app.security import get_current_user
from app.services import mediciones

router = APIRouter(prefix="/mediciones", tags=["Mediciones"])


#CONSUMO DEL DIA ACTUAL DE UN NODO
@router.get("/_consumo_diario/{id_nodo}", response_model=ConsumoResponse)
def consumo_diario(id_nodo: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones.consumo_diario_por_nodo(db, id_nodo, usuario_actual["id_usuario"])


#CONSUMO DEL MES ACTUAL DE UN NODO
@router.get("/_consumo_mensual/{id_nodo}", response_model=ConsumoResponse)
def consumo_mensual(id_nodo: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones.consumo_mensual_por_nodo(db, id_nodo, usuario_actual["id_usuario"])

from app.schemas.mediciones import ConsumoResponse, ConsumoSemanalResponse

#CONSUMO AGRUPADO POR DIA DE LA SEMANA ACTUAL
@router.get("/_consumo_semanal/{id_nodo}", response_model=ConsumoSemanalResponse)
def consumo_semanal(id_nodo: int, usuario_actual = Depends(get_current_user), db: Session = Depends(get_db)):
    return mediciones.consumo_semanal_por_nodo(db, id_nodo, usuario_actual["id_usuario"])