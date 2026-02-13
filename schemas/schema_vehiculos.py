"""
Esquemas Pydantic para Vehículos
"""

from pydantic import BaseModel
from datetime import datetime


class VehiculoBase(BaseModel):
    usuario_Id: int

    modelo: str
    marca: str
    placa: str
    serie: str
    color: str
    tipo: str
    anio: int

    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


class VehiculoCreate(BaseModel):
    usuario_Id: int

    modelo: str
    marca: str
    placa: str
    serie: str
    color: str
    tipo: str
    anio: int


class VehiculoUpdate(BaseModel):
    usuario_Id: int | None = None

    modelo: str | None = None
    marca: str | None = None
    placa: str | None = None
    serie: str | None = None
    color: str | None = None
    tipo: str | None = None
    anio: int | None = None
    estatus: bool | None = None


class Vehiculo(VehiculoBase):
    Id: int

    class Config:
        orm_mode = True
