from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Date
from sqlalchemy.orm import relationship
from ..conf.database import Base


class VuelosModel(Base):
    __tablename__ = "vuelos"

    id = Column("id", Integer, primary_key=True, index=True)
    idAerolinea = Column("id_aerolinea", Integer, ForeignKey('aerolineas.id_aerolinea'))
    idAeropuerto = Column("id_aeropuerto", Integer, ForeignKey('aeropuertos.id_aeropuerto'))
    idMovimiento = Column("id_movimiento", Integer, ForeignKey('movimientos.id_movimiento'))
    dia = Column("dia", Date)

    aeropuertos = relationship('AeropuertosModel')
    aerolineas = relationship('AerolineasModel')
    movimientos = relationship('MovimientosModel')

    def to_dict(self):
        model_dict = dict(self.__dict__)
        del model_dict['_sa_instance_state']
        return model_dict