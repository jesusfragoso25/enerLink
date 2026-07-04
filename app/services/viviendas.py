from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.viviendas import Viviendas
from app.models.usuario import Usuario
from app.schemas.viviendas import ViviendaCreate, ViviendaUpdate, ViviendaResponse, ViviendaCreate_sin_id_usuario

#CREAR VIVIENDA PARA CUALQUIER USUARIO 
def crear_vivienda(db: Session, data: ViviendaCreate ):
    nueva = Viviendas(
        id_usuario=data.id_usuario,
        nombre=data.nombre,
        direccion=data.direccion,
        ciudad=data.ciudad,
        departamento=data.departamento,
        pais=data.pais
)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

#CREAR VIVIENDA PARA EL USUARIO QUE ESTE AUTENTICADO
def crear_vivienda_ath(db: Session, data: ViviendaCreate_sin_id_usuario, id_usuario: int):
    nueva = Viviendas(
        id_usuario=id_usuario,
        nombre=data.nombre,
        direccion=data.direccion,
        ciudad=data.ciudad,
        departamento=data.departamento,
        pais=data.pais
)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
    
#MOSTRAR TODAS LAS VIVIENDAS
def obtener_viviendas(db: Session):
    return db.query(Viviendas).all()

#MOSTRAR VIVIENDA POR ID DE VIVIENDA
def obtener_vivienda(db: Session, id_vivienda: int):

    vivienda = db.query(Viviendas).filter(
        Viviendas.id_vivienda == id_vivienda
    ).first()

    if not vivienda:
        raise HTTPException(status_code=404, detail="No encontrada")

    return vivienda

#MOSTRAR VIVIENDAS POR ID DE USUARIO
def obtener_viviendas_por_usuario(db: Session,id_usuario: int):

    usuario = db.query(Usuario).filter( Usuario.id_usuario == id_usuario).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return db.query(Viviendas).filter(
        Viviendas.id_usuario == id_usuario
    ).all()

#ELIMINAR VIVIENDA POR ID DE VIVIENDA UNICAMENTE LAS QUE PERTENECEN AL USUARIO QUE ESTA AUTENTICADO
def eliminar_vivienda(db: Session, id_vivienda: int, id_usuario: int):

    vivienda = db.query(Viviendas).filter(
        Viviendas.id_vivienda == id_vivienda,
        Viviendas.id_usuario == id_usuario
    ).first()

    if not vivienda:
        raise HTTPException(status_code=404, detail="No encontrada")

    db.delete(vivienda)
    db.commit()

    return {"mensaje": "Eliminada"}



#ACTUALIZAR VIVIENDA POR ID DE VIVIENDA
"""def actualizar_vivienda(
    db: Session,
    id_vivienda: int,
    data: ViviendaUpdate
):
    vivienda = db.query(Viviendas).filter(
        Viviendas.id_vivienda == id_vivienda
    ).first()

    if not vivienda:
        raise HTTPException(404, "Vivienda no encontrada")

    datos_actualizados = data.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(vivienda, campo, valor)

    db.commit()
    db.refresh(vivienda)

    return vivienda"""