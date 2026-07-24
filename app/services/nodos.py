from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.nodos import Nodos
from app.models.gateways import Gateways
from app.models.viviendas import Viviendas
from app.schemas.nodos import NodoCreate, NodoUpdate, NodoResponse


#CREAR NODO PARA CUALQUIER GATEWAY (SIN VALIDAR PROPIETARIO)
def crear_nodo(db: Session, data: NodoCreate):
    nuevo = Nodos(
        id_gateway=data.id_gateway,
        id_tipo_nodo=data.id_tipo_nodo,
        uuid_nodo=data.uuid_nodo,
        mac_address=data.mac_address,
        nombre_nodo=data.nombre_nodo,
        ubicacion=data.ubicacion,
        estado=data.estado
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


#CREAR NODO VERIFICANDO QUE EL GATEWAY PERTENEZCA AL USUARIO AUTENTICADO Y QUE EL UUID NO SE REPITA
def crear_nodo_ath(db: Session, data: NodoCreate, id_usuario: int):

    gateway = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Gateways.id_gateway == data.id_gateway, Viviendas.id_usuario == id_usuario)
        .first()
    )

    if not gateway:
        raise HTTPException(
            status_code=404,
            detail="El gateway no existe o no pertenece al usuario"
        )

    if db.query(Nodos.uuid_nodo).filter(Nodos.uuid_nodo == data.uuid_nodo).first():
        raise HTTPException(
            status_code=404,
            detail="Nodo ya se encuentra en uso"
        )

    nuevo = Nodos(
        id_gateway=data.id_gateway,
        id_tipo_nodo=data.id_tipo_nodo,
        uuid_nodo=data.uuid_nodo,
        mac_address=data.mac_address,
        nombre_nodo=data.nombre_nodo,
        ubicacion=data.ubicacion,
        estado=data.estado
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


#MOSTRAR TODOS LOS NODOS DEL USUARIO AUTENTICADO (VIA DOBLE JOIN: NODOS -> GATEWAYS -> VIVIENDAS)
def obtener_nodos_por_usuario(db: Session, id_usuario: int):
    return (
        db.query(Nodos)
        .join(Gateways, Nodos.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Viviendas.id_usuario == id_usuario)
        .all()
    )


#MOSTRAR TODOS LOS NODOS DE UN GATEWAY ESPECIFICO, VERIFICANDO QUE EL GATEWAY PERTENEZCA AL USUARIO
def obtener_nodos_por_gateway(db: Session, id_gateway: int, id_usuario: int):

    gateway = (
        db.query(Gateways)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Gateways.id_gateway == id_gateway, Viviendas.id_usuario == id_usuario)
        .first()
    )

    if not gateway:
        raise HTTPException(status_code=404, detail="Gateway no encontrado")

    return db.query(Nodos).filter(Nodos.id_gateway == id_gateway).all()


#MOSTRAR NODO POR ID, VERIFICANDO QUE PERTENEZCA AL USUARIO
def obtener_nodo_por_id(db: Session, id_nodo: int, id_usuario: int):
    nodo = (
        db.query(Nodos)
        .join(Gateways, Nodos.id_gateway == Gateways.id_gateway)
        .join(Viviendas, Gateways.id_vivienda == Viviendas.id_vivienda)
        .filter(Nodos.id_nodo == id_nodo, Viviendas.id_usuario == id_usuario)
        .first()
    )

    if not nodo:
        raise HTTPException(status_code=404, detail="Nodo no encontrado")

    return nodo


#ELIMINAR NODO POR ID, VERIFICANDO QUE PERTENEZCA AL USUARIO
def eliminar_nodo(db: Session, id_nodo: int, id_usuario: int):
    nodo = obtener_nodo_por_id(db, id_nodo, id_usuario)
    db.delete(nodo)
    db.commit()
    return {"mensaje": "Eliminado"}