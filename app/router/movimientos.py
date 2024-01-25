from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schema.MovimientosSchema import Movimientos
from ..conf.database import get_db
from typing import List
from ..repository.MovimientosRepository import getMovimientos

router = APIRouter()

@router.get("", response_model=List[Movimientos])
async def aeropuertos(bbdd: Session = Depends(get_db)):
    return getMovimientos(bbdd)
