from sqlalchemy.orm import Session
from ..models.VuelosModel import VuelosModel
from ..models.AeropuertosModel import AeropuertosModel
from ..models.AerolineasModel import AerolineasModel
from ..schema.VuelosSchema import TopAereopuertos
from sqlalchemy import func, desc

def getVuelos(db: Session):
    return db.query(VuelosModel).all()


def getTopAereopuerto(db:Session):
    top = db.query(func.count(VuelosModel.idMovimiento).label('top')).group_by(VuelosModel.idAeropuerto).order_by(desc('top')).limit(1).as_scalar()
    counter = db.query(VuelosModel.idAeropuerto, func.count(VuelosModel.idMovimiento).label('total'), AeropuertosModel.nombreAeropuerto) \
            .join(AeropuertosModel, VuelosModel.idAeropuerto == AeropuertosModel.idAeropuerto ) \
            .group_by(VuelosModel.idAeropuerto, AeropuertosModel.nombreAeropuerto)\
            .order_by(desc('total')) \
            .subquery('counter')

    result = db.query(counter).filter(counter.c.total == top).all()
    result = [r._asdict() for r in result]
    return result

def getTopAereolinea(db:Session):
    top = db.query(func.count(VuelosModel.idMovimiento).label('top')).group_by(VuelosModel.idAerolinea).order_by(desc('top')).limit(1).as_scalar()
    counter = db.query(VuelosModel.idAerolinea, func.count(VuelosModel.idMovimiento).label('total'), AerolineasModel.nombreAerolinea) \
            .join(AerolineasModel, VuelosModel.idAerolinea == AerolineasModel.idAerolineas) \
            .group_by(VuelosModel.idAerolinea, AerolineasModel.idAerolineas)\
            .order_by(desc('total'))\
            .subquery('counter')
    
    result = db.query(counter).filter(counter.c.total == top).all()
    result = [r._asdict() for r in result]
    return result

def getTopVuelosDia(db:Session):
    result = db.query(VuelosModel.dia, func.count(1).label('total'))\
            .group_by(VuelosModel.dia)\
            .order_by(desc('total'))\
            .limit(1).all()
    result = [r._asdict() for r in result]
    return result[0]

def getTopAreolineaDia(db:Session):
    result = db.query(VuelosModel.idAerolinea, VuelosModel.dia, func.count(1).label('total'), AerolineasModel.nombreAerolinea)\
            .join(AerolineasModel, VuelosModel.idAerolinea == AerolineasModel.idAerolineas) \
            .group_by(VuelosModel.dia, VuelosModel.idAerolinea, AerolineasModel.nombreAerolinea)\
            .having(func.count(1) > 1).all()
    result = [r._asdict() for r in result]
    return result