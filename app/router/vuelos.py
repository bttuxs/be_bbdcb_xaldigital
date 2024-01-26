from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Any
from ..conf.database import engine, Base, get_db
from ..repository.VuelosRepository import getVuelos, getTopAereopuerto, getTopAereolinea, getTopVuelosDia, getTopAreolineaDia
from ..models.VuelosModel import VuelosModel
from ..schema.VuelosSchema import Vuelos, TopAereopuertos, TopDia, TopAereolinea, TopVuelosAereolinea
from sqlalchemy import event
from ..seeder import seed

event.listen(VuelosModel.__table__, 'after_create', seed.initialize_table)


router = APIRouter()


@router.on_event("startup")
def configure():
    Base.metadata.create_all(bind=engine)


@router.get("", response_model=List[Vuelos])
async def vuelos(bbdd: Session = Depends(get_db)):
    return getVuelos(bbdd)


@router.get("/top/aereopuerto", response_model=List[TopAereopuertos])
async def topAereopuerto(bbdd: Session = Depends(get_db)):
    result = getTopAereopuerto(bbdd)
    return result


@router.get("/top/aereolinea", response_model=List[TopAereolinea])
async def topAereolinea(bbdd: Session = Depends(get_db)):
    result = getTopAereolinea(bbdd)
    return result

@router.get("/top/aereolinea/dia", response_model=List[TopVuelosAereolinea])
async def topAereolinea(bbdd: Session = Depends(get_db)):
    result = getTopAreolineaDia(bbdd)
    return result



@router.get("/top/dia", response_model=TopDia)
async def topVuelosDia(bbdd: Session = Depends(get_db)):
    result = getTopVuelosDia(bbdd)
    return result
