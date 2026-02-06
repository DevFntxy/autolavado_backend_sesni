from sqlalchemy import Integer , Column, String, Enum , Boolean
from  config.db  import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'tbc_usuario'
    
    id = Column(Integer, primary_key=True, index=True)
    primerNombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    genero = Column(Enum('MASCULINO', 'FEMENINO', 'OTRO', name='genero_enum'), nullable=False)
    estado = Column(Enum('ACTIVO', 'INACTIVO', name='estado_enum'), default='ACTIVO', nullable=False)

    roles = relationship("Rol", secondary="tbc_usuario_rol", back_populates="usuarios")

    def __repr__(self):
        return f"<Usuario(primerNombre={self.primerNombre}, apellido={self.apellido}, genero={self.genero}, estado={self.estado})>"
    w