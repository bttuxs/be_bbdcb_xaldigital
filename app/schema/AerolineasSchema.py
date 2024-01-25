from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AerolineasCreate(BaseModel):
    nombreAerolinea: str

class Aerolineas(AerolineasCreate):
    idAerolineas: int

