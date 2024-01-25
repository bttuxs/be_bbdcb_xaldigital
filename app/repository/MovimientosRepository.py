from sqlalchemy.orm import Session
from ..models.MovimientosModel import MovimientosModel

def getMovimientos(db: Session):
    return db.query(MovimientosModel).all()
