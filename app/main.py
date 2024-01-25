from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from .router import api

PROD = config("prod")

if eval(PROD):
    print("se inicia en modo produccion")
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Reto xaldigital",
        version="1.0.0",
        description="Esta es un reto de programancion",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.router, prefix="/api")
