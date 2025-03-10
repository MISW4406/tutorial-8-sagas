""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass

from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.modulos.vuelos.dominio.repositorios import RepositorioProveedores, RepositorioReservas, \
    RepositorioEventosReservas
from aeroalpes.modulos.vuelos.infraestructura.vistas import VistaReserva
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.seedwork.infraestructura.vistas import Vista
from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioReservasSQLAlchemy, RepositorioProveedoresSQLAlchemy, \
    RepositorioEventosReservaSQLAlchemy


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas:
            return RepositorioReservasSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosReservas:
            return RepositorioEventosReservaSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Reserva:
            return VistaReserva()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')