from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from ..conf.database import Base


class AerolineasModel(Base):
    __tablename__ = "aerolineas"

    idAerolineas = Column("id_aerolinea", Integer, primary_key=True, index=True)
    nombreAerolinea = Column("nombre_aerolinea", String(250))