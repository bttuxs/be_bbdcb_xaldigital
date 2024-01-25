from fastapi import APIRouter
from . import answers

router = APIRouter()

router.include_router(answers.router, prefix="/respuestas", tags=["Respuestas"])
