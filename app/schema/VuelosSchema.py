from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Vuelos(BaseModel):
    id: int
    idAerolinea: int
    idAeropuerto: int
    idMovimiento: int
    dia: date


class TopAereopuertos(BaseModel):
    idAeropuerto: int
    nombreAeropuerto: str
    total: int

class TopAereolinea(BaseModel):
    idAerolinea: int
    nombreAerolinea: str
    total: int

class TopVuelosAereolinea(BaseModel):
    idAerolinea: int
    nombreAerolinea: str
    total: int
    dia: date

class TopDia(BaseModel):
    dia: date
    total: int
