"""Entidades del dominio de processed_data

En este archivo usted encontrará las entidades del dominio de processed_data

"""

from datetime import datetime
from processed_data.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Cedula, Rut


@dataclass
class DatoProcesado(Entidad):
    url: str = None
    nombre: Nombre = field(default_factory=Nombre)
    email: Email = field(default_factory=Email)

@dataclass
class ClienteNatural(DatoProcesado, AgregacionRaiz):
    cedula: Cedula = None
    fecha_nacimiento: datetime = None

@dataclass
class ClienteEmpresa(DatoProcesado, AgregacionRaiz):
    rut: Rut = None
    fecha_constitucion: datetime = None
