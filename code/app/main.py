from fastapi import FastAPI
from app.api.v1.endpoints import recommendations

app = FastAPI(
    title="API de recomendações - xpto.com.br",
    description="API destinada a sugerir produtos para compra",
    version="1.0.0",
)

app.include_router(recommendations.router, prefix="/v1")