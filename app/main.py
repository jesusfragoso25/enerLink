from fastapi import FastAPI
from app.routes.usuarios import router # Se debe de definir la ruta del endpoint cada que se agregue un aplicativo
#from app.routes.test import router as test_router
from app.routes.auth import router as auth_router
#from app.routes.security import router as security_router
from fastapi.security import HTTPBearer
from app.routes.security import router as perfil


app = FastAPI(
    title="EnerLink API"
)
#app.include_router(test_router)
app.include_router(router)
app.include_router(auth_router)
app.include_router(perfil)

security = HTTPBearer()