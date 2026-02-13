from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from config.db import Base
from datetime import datetime


class Vehiculo(Base):
    __tablename__ = "tbc_vehiculos"

    Id = Column(Integer, primary_key=True, index=True)
    usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"))

    modelo = Column(String(45))
    marca = Column(String(45))
    placa = Column(String(45))
    serie = Column(String(45))
    color = Column(String(45))
    tipo = Column(String(45))
    anio = Column(Integer)

    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )