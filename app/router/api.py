from fastapi import APIRouter
from . import answers, movimientos

router = APIRouter()

router.include_router(answers.router, prefix="/respuestas", tags=["Respuestas"])
router.include_router(movimientos.router, prefix="/movimientos", tags=["Movimientos"])
