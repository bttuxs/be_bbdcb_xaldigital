from sqlalchemy.orm import Session
from ..models.AerolineasModel import AerolineasModel

def getAerolineas(db: Session):
    return db.query(AerolineasModel).all()
