from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from ..conf.database import Base


class AeropuertosModel(Base):
    __tablename__ = "aeropuertos"

    idAeropuerto = Column("id_aeropuerto", Integer, primary_key=True, index=True)
    nombreAeropuerto = Column("nombre_aeropuerto", String(250))