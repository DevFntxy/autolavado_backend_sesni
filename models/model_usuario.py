"""Esta clase permite generar el modelo para los tipos de user"""

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from config.db import Base
from datetime import datetime


class Usuario(Base):
    __tablename__ = "tbb_usuarios"

    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"))

    nombre = Column(String(60))
    primer_apellido = Column(String(60))
    segundo_apellido = Column(String(60))
    direccion = Column(String(200))
    correo_electronico = Column(String(100))
    numero_telefono = Column(String(20))
    contrasena = Column(String(40))

    estatus = Column(Boolean, default=True)

    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )