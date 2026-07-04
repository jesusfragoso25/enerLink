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
    
    
    
    
    
    
    