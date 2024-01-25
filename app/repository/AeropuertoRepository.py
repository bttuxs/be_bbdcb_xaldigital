from sqlalchemy.orm import Session
from ..models.AeropuertosModel import AeropuertosModel

def getAeropuertos(db: Session):
    return db.query(AeropuertosModel).all()
