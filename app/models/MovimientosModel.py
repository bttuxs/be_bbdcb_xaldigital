from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from ..conf.database import Base


class MovimientosModel(Base):
    __tablename__ = "movimientos"

    idMovimiento = Column("id_movimiento", Integer, primary_key=True, index=True)
    descripcion = Column("descripcion", String(250))