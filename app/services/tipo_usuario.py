from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.tipo_usuario import TipoUsuario
from app.models.usuario import Usuario
from app.schemas.tipo_usuario import  TipoUsuarioCreate, TipoUsuarioUpdate, TipoUsuarioResponse

#CREAR TIPO DE USUARIO   
def crear_tipo_usuario(db: Session, data: TipoUsuarioCreate, id_usuario: int):
    nueva = TipoUsuario(
        rol = data.rol
)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
    
    
    
    
    
    
    
    
    
    
    
    
    