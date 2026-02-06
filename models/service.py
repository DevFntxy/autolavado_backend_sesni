("""Esta clase contiene los servicios generales del sistema.""")
from sqlalchemy import Integer, Column, String, Enum, Boolean
from config.db import Base


class Service(Base):
	__tablename__ = 'tbc_service'

	id = Column(Integer, primary_key=True, index=True)
	nombre = Column(String(100), unique=True, nullable=False)
	descripcion = Column(String(255), nullable=True)
	duracion_minutos = Column(Integer, nullable=True)
	precio = Column(Integer, nullable=False, default=0)
	disponible = Column(Boolean, default=True, nullable=False)
	estado = Column(Enum('ACTIVO', 'INACTIVO', name='estado_enum'), default='ACTIVO', nullable=False)

	def __repr__(self):
		return f"<Service(nombre={self.nombre}, precio={self.precio}, estado={self.estado})>"

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class CarServiceDetail(Base):
    __tablename__ = 'tbd_car_service'

    id = Column(Integer, primary_key=True, index=True)

    auto_id = Column(Integer, ForeignKey('tbb_car.id'), nullable=False)
    servicio_id = Column(Integer, ForeignKey('tbc_car_service.id'), nullable=False)

    usuario_realiza_id = Column(Integer, ForeignKey('tbb_usuario.id'), nullable=False)
    usuario_cobra_id = Column(Integer, ForeignKey('tbb_usuario.id'), nullable=False)

    fecha_servicio = Column(DateTime, default=func.now(), nullable=False)

    estado = Column(
        Enum('PENDIENTE', 'EN_PROCESO', 'FINALIZADO', 'CANCELADO', name='estado_servicio_enum'),
        default='PENDIENTE',
        nullable=False
    )

    auto = relationship("Car", back_populates="servicios")
    servicio = relationship("CarService")

    usuario_realiza = relationship(
        "Usuario",
        foreign_keys=[usuario_realiza_id]
    )

    usuario_cobra = relationship(
        "Usuario",
        foreign_keys=[usuario_cobra_id]
    )

    def __repr__(self):
        return f"<CarServiceDetail(auto={self.auto_id}, servicio={self.servicio_id})>"
