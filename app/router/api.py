from fastapi import APIRouter
from . import answers, movimientos, aerolineas, aeropuerto, vuelos

router = APIRouter()

router.include_router(answers.router, prefix="/respuestas", tags=["Respuestas"])
router.include_router(movimientos.router, prefix="/movimientos", tags=["Movimientos"])
router.include_router(aerolineas.router, prefix="/aereolineas", tags=["Aereolineas"])
router.include_router(aeropuerto.router, prefix="/aereopuertos", tags=["Aereopuertos"])
router.include_router(vuelos.router, prefix="/vuelos", tags=["Vuelos"])