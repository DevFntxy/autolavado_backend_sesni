from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Car(Base):
    __tablename__ = 'tbb_car'

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    placas = Column(String(20), unique=True, nullable=False)

    cliente_id = Column(Integer, ForeignKey('tbc_client.id'), nullable=False)

    cliente = relationship("Client", back_populates="autos")
    servicios = relationship("CarServiceDetail", back_populates="auto")

    def __repr__(self):
        return f"<Car(placas={self.placas})>"
