'''Esta clase contiene los tipos de servicio que puede tener un carro en el sistema.'''
from sqlalchemy import Integer , Column, String, Enum , Boolean
from  config.db  import Base
class CarService(Base):
	__tablename__ = 'tbc_car_service'

	id = Column(Integer, primary_key=True, index=True)
	nombreServicio = Column(String(100), unique=True, nullable=False)
	descripcion = Column(String(255), nullable=True)
	duracion_minutos = Column(Integer, nullable=True)
	precio = Column(Integer, nullable=False, default=0)
	disponible = Column(Boolean, default=True, nullable=False)
	estado = Column(Enum('ACTIVO', 'INACTIVO', name='estado_enum'), default='ACTIVO', nullable=False)

	def __repr__(self):
		return f"<CarService(nombreServicio={self.nombreServicio}, precio={self.precio}, estado={self.estado})>"
	
    