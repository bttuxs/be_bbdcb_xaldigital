from fastapi import APIRouter
from . import answers, movimientos, aerolineas, aeropuerto

router = APIRouter()

router.include_router(answers.router, prefix="/respuestas", tags=["Respuestas"])
router.include_router(movimientos.router, prefix="/movimientos", tags=["Movimientos"])
router.include_router(aerolineas.router, prefix="/aerolineas", tags=["Aereolineas"])
router.include_router(aeropuerto.router, prefix="/aereopuertos", tags=["Aereopuertos"])