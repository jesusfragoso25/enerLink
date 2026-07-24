from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.gateways import Gateways
from app.models.viviendas import Viviendas
from app.schemas.gateways import GatewayCreate, GatewayUpdate, GatewayResponse, GatewayCreate_sin_id_usuario


#CREAR GATEWAY PARA CUALQUIER USUARIO (SIN VALIDAR PROPIETARIO)
def crear_gateway(db: Session, data: GatewayCreate):
    nueva = Gateways(
        id_vivienda=data.id_vivienda,
        uuid_gateway=data.uuid_gateway,
        nombre_gateway=data.nombre_gateway
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


#CREAR GATEWAY VERIFICANDO QUE LA VIVIENDA PERTENEZCA AL USUARIO AUTENTICADO Y QUE EL UUID NO SE REPITA
def crear_gateway_ath(db: Session, data: GatewayCreate_sin_id_usuario, id_usuario: int):

    vivienda = db.query(Viviendas).filter(
        Viviendas.id_vivienda == data.id_vivienda,
        Viviendas.id_usuario == id_usuario
    ).first()

    if not vivienda:
        raise HTTPException(
            status_code=404,
            detail="La vivienda no existe o no pertenece al usuario"
        )

    if db.query(Gateways.uuid_gateway).filter(Gateways.uuid_gateway == data.uuid_gateway).first():
        raise HTTPException(
            status_code=404,
            detail="Gateway ya se encuentra en uso"
        )

    nueva = Gateways(
        id_vivienda=data.id_vivienda,
        uuid_gateway=data.uuid_gateway,
        nombre_gateway=data.nombre_gateway
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


#MOSTRAR TODOS LOS GATEWAYS DEL USUARIO AUTENTICADO (VIA JOIN CON VIVIENDAS)
def obtener_gateway_por_usuario(db: Session, id_usuario: int):
    return (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Viviendas.id_usuario == id_usuario)
        .all()
    )

#MOSTRAR GATEWAYS POR ID DE VIVIENDA, VERIFICANDO QUE LA VIVIENDA PERTENEZCA AL USUARIO
def obtener_gateways_por_vivienda(db: Session, id_vivienda: int, id_usuario: int):

    vivienda = db.query(Viviendas).filter(
        Viviendas.id_vivienda == id_vivienda,
        Viviendas.id_usuario == id_usuario
    ).first()

    if not vivienda:
        raise HTTPException(status_code=404, detail="La vivienda no existe o no pertenece al usuario")

    return db.query(Gateways).filter(Gateways.id_vivienda == id_vivienda).all()


#MOSTRAR GATEWAY POR ID, VERIFICANDO QUE PERTENEZCA AL USUARIO
def obtener_gateway_por_id(db: Session, id_gateway: int, id_usuario: int):
    gateway = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Gateways.id_gateway == id_gateway, Viviendas.id_usuario == id_usuario)
        .first()
    )

    if not gateway:
        raise HTTPException(status_code=404, detail="Gateway no encontrado")

    return gateway


#ELIMINAR GATEWAY POR ID, VERIFICANDO QUE PERTENEZCA AL USUARIO
def eliminar_gateway(db: Session, id_gateway: int, id_usuario: int):
    gateway = obtener_gateway_por_id(db, id_gateway, id_usuario)
    db.delete(gateway)
    db.commit()
    return {"mensaje": "Eliminado"}