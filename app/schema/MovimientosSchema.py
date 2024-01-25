from pydantic import BaseModel

class Movimientos(BaseModel):
    idMovimiento: int
    descripcion: str
