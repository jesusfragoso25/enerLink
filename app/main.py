from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.routes.usuarios import router # Se debe de definir la ruta del endpoint cada que se agregue un aplicativo
from app.routes.auth import router as auth_router
from app.routes.security import router as perfil
from app.routes.viviendas import router as router_viviendas
from app.routes.gateways import router as router_gateways
from app.routes.tipos_dispositivo import router as router_tipos_dispositivo
from app.routes.tipo_usuario import router as  router_tipo_usuario
from app.routes.nodos import router as router_nodos
from fastapi.middleware.cors import CORSMiddleware
from app.assistant.knowledge.knowledge_cache import KnowledgeCache
from app.assistant.knowledge.loader import KnowledgeLoader
from app.routes.assistant import router as router_chat
from app.routes.mediciones import router as mediciones_router
from app.routes.mediciones_gateway import router as mediciones_gateway

app = FastAPI(
    title="EnerLink API",
    description="API para el sistema EnerLink",
    version="1.0.0"
)

#app.include_router(test_router)
app.include_router(router)
app.include_router(auth_router)
app.include_router(perfil)
app.include_router(router_viviendas)
app.include_router(router_gateways)
app.include_router(router_tipos_dispositivo)
app.include_router(router_tipo_usuario)
app.include_router(router_nodos)
app.include_router(router_chat)
app.include_router(mediciones_router)
app.include_router(mediciones_gateway)



origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    KnowledgeLoader.load()