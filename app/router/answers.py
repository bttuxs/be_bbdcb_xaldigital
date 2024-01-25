from fastapi import APIRouter
from pydantic import ValidationError
from ..service import Answers
from ..schema import AnswerSchema
router = APIRouter()


@router.get("", response_model=AnswerSchema.AnswersStatus)
async def status():
    try:
        return Answers.answerState()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/best", response_model=AnswerSchema.Answer)
async def better():
    try:
        return Answers.answerBetter()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/viewless", response_model=AnswerSchema.Answer)
async def viewless():
    try:
        return Answers.answerViewLess()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))


@router.get("/firstlast", response_model=AnswerSchema.AnswersFirstLast)
async def fistlast():
    try:
        return Answers.answerFirstAndLast()
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))
