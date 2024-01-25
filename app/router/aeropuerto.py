from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..conf.database import get_db, Base, engine
from ..repository.AeropuertoRepository import getAeropuertos
from ..schema.AeropuertosSchema import Aeropuertos
from ..models.AeropuertosModel import AeropuertosModel
from sqlalchemy import event
from ..seeder import seed

event.listen(AeropuertosModel.__table__, 'after_create', seed.initialize_table)


router = APIRouter()

@router.on_event("startup")
def configure():
    Base.metadata.create_all(bind=engine)


@router.get("", response_model=List[Aeropuertos])
async def aeropuertos(bbdd: Session = Depends(get_db)):
    return getAeropuertos(bbdd)
