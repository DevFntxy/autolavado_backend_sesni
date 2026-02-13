"""
Esquemas Pydantic para Usuario
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioBase(BaseModel):
    rol_Id: int

    nombre: str
    primer_apellido: str
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr
    numero_telefono: str | None = None

    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime


class UsuarioCreate(BaseModel):
    rol_Id: int

    nombre: str
    primer_apellido: str
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr
    numero_telefono: str | None = None
    contrasena: str


class UsuarioUpdate(BaseModel):
    rol_Id: int | None = None

    nombre: str | None = None
    primer_apellido: str | None = None
    segundo_apellido: str | None = None
    direccion: str | None = None
    correo_electronico: EmailStr | None = None
    numero_telefono: str | None = None
    estatus: bool | None = None


class Usuario(UsuarioBase):
    Id: int

    class Config:
        orm_mode = True
