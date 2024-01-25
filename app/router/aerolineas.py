from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..conf.database import get_db, Base, engine
from ..models.AerolineasModel import AerolineasModel
from ..repository.AerolineasRepository import getAerolineas
from ..schema.AerolineasSchema import Aerolineas
from sqlalchemy import event
from ..seeder import seed

event.listen(AerolineasModel.__table__, 'after_create', seed.initialize_table)

router = APIRouter()

@router.on_event("startup")
def configure():
    Base.metadata.create_all(bind=engine)


@router.get("", response_model=List[Aerolineas])
async def aerolineas(bbdd: Session = Depends(get_db)):
    return getAerolineas(bbdd)
