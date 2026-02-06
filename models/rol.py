'''Esta clase contiene los tipos de rol que puede tener un usuario en el sistema.'''
from sqlalchemy import Integer , Column, String, Enum , Boolean
from  config.db  import Base

class Rol(Base):
    __tablename__ = 'tbc_rol'
    
    id = Column(Integer, primary_key=True, index=True)
    nombreRol = Column(String(20), unique=True, nullable=False)
    estado = Column(Enum('ACTIVO', 'INACTIVO', name='estado_enum'), default='ACTIVO', nullable=False)

    def __repr__(self):
        return f"<Rol(nombreRol={self.nombreRol }, estado={self.estado})>"