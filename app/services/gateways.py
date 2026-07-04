from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.gateways import Gateways
from app.models.viviendas import Viviendas
from app.models.usuario import Usuario
from app.schemas.gateways import    GatewayCreate, GatewayUpdate, GatewayResponse, GatewayCreate_sin_id_usuario

#CREAR GATEWAY PARA CUALQUIER USUARIO 
def crear_gateway(db: Session, data: GatewayCreate ):
    nueva = Gateways(
        id_vivienda=data.id_vivienda,
        uuid_gateway=data.uuid_gateway,
        nombre_gateway=data.nombre_gateway
        
)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

#CREAR GATEWAY DE CUALQUIER VIVIENDA PARA CUALQUIER USUARIO, PERO VERIFICANDO QUE EL UUID NO SE REPITA
def crear_gateway_ath(db: Session, data: GatewayCreate_sin_id_usuario, id_usuario: int):
    nueva = Gateways(
        
        id_vivienda=data.id_vivienda,
        uuid_gateway=data.uuid_gateway,
        nombre_gateway=data.nombre_gateway      
    )
    
           
    if db.query(Gateways.uuid_gateway).filter(Gateways.uuid_gateway == data.uuid_gateway).first():
        raise HTTPException(
            status_code=404,
            detail="Gateway ya se encuentra en uso"
        ) 
        
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
