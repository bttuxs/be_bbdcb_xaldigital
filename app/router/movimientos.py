from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schema.MovimientosSchema import Movimientos
from ..models.MovimientosModel import MovimientosModel
from ..conf.database import get_db, Base, engine
from typing import List
from ..repository.MovimientosRepository import getMovimientos
from sqlalchemy import event
from ..seeder import seed

event.listen(MovimientosModel.__table__, 'after_create', seed.initialize_table)
router = APIRouter()

@router.on_event("startup")
def configure():
    Base.metadata.create_all(bind=engine)

@router.get("", response_model=List[Movimientos])
async def aeropuertos(bbdd: Session = Depends(get_db)):
    return getMovimientos(bbdd)
