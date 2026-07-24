from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.tipos_dispositivo import TiposDispositivo
from app.models.usuario import Usuario
from app.schemas.tipos_dispositivo import  TiposDispositivoCreate, TiposDispositivoUpdate, TiposDispositivoResponse

#CREAR TIPO DE DISPOSITIVO 
def crear_tipo_dispositivo(db: Session, data: TiposDispositivoCreate, id_usuario: int):
    nueva = TiposDispositivo(
        nombre_tipo = data.nombre_tipo,
        descripcion = data.descripcion
)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
    
#MOSTRAR TODOS LOS TIPOS DE DISPOSITIVO
def obtener_tipos_dispositivo(db: Session):
    return db.query(TiposDispositivo).all()


#MOSTRAR TIPO DE DISPOSITIVO POR ID
def obtener_tipo_dispositivo_por_id(db: Session, id_tipo: int):
    tipo = db.query(TiposDispositivo).filter(
        TiposDispositivo.id_tipo == id_tipo
    ).first()

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de dispositivo no encontrado")

    return tipo
    
    
    
    
    