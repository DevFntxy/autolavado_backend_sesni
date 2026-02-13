from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    Time,
    Boolean,
    DECIMAL
)
from config.db import Base
from datetime import datetime


class AutoServicio(Base):
    __tablename__ = "tbd_vehiculos_servicios_usuarios"

    iD = Column(Integer, primary_key=True, index=True)

    vehiculo_id = Column(Integer, ForeignKey("tbb_vehiculos.Id"))
    cajero_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    operador_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))
    servicio_Id = Column(Integer, ForeignKey("tbc_servicios.Id"))

    fecha = Column(DateTime)
    hora = Column(Time)
    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )