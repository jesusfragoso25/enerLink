from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routes.usuarios import router # Se debe de definir la ruta del endpoint cada que se agregue un aplicativo
from app.routes.auth import router as auth_router
from app.routes.security import router as perfil
from app.routes.viviendas import router as router_viviendas
from app.routes.gateways import router as router_gateways
from app.routes.tipos_dispositivo import router as router_tipos_dispositivo
from app.routes.tipo_usuario import router as  router_tipo_usuario

from app.models.usuario import Usuario
from app.models.viviendas import Viviendas


app = FastAPI(
    title="EnerLink API"
)
#app.include_router(test_router)
app.include_router(router)
app.include_router(auth_router)
app.include_router(perfil)
app.include_router(router_viviendas)
app.include_router(router_gateways)
app.include_router(router_tipos_dispositivo)
app.include_router(router_tipo_usuario)
security = HTTPBearer()