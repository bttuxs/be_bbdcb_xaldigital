from fastapi import APIRouter
from pydantic import ValidationError
from ..service import Answers
from ..schema import AnswerSchema
router = APIRouter()


@router.get("", response_model=AnswerSchema.AnswersStatus, summary="Estaus de las respuesta", description="Este servicio vemos la respuesta constestadas y no contestadas")
async def status():
    try:
        return Answers.answerState()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/best", response_model=AnswerSchema.Answer, summary="Mejor respuesta", description="Este servicio se encarga de traer la mejor respuesta del listado")
async def better():
    try:
        return Answers.answerBetter()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/viewless", response_model=AnswerSchema.Answer, summary="Respuesta con menos vista", description="Este servicio se encarga de regresar la respuesta menos vista")
async def viewless():
    try:
        return Answers.answerViewLess()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/firstlast", response_model=AnswerSchema.AnswersFirstLast, summary="Respuestas mas antigua y mas nueva", description="Este servicio se encarga de traer la respuesta mas nueva y la mas antigua")
async def fistlast():
    try:
        return Answers.answerFirstAndLast()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))
