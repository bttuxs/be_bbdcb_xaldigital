from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AeropuertosCreate(BaseModel):
    idAeropuerto: int

class Aeropuertos(BaseModel):
    idAeropuerto: int
    nombreAeropuerto: str
