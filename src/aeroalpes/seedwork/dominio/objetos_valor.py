"""Objetos valor reusables parte del seedwork del proyecto

En este archivo usted encontrará los objetos valor reusables parte del seedwork del proyecto

"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from .entidades import Locacion


@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):
    codigo: str

class Ruta(ABC, ObjetoValor):
    @abstractmethod
    def origen(self) -> Locacion:
        ...
    
    @abstractmethod
    def destino(self) -> Locacion:
        ...
    
    @abstractmethod
    def fecha_salida(self) -> datetime:
        ...

    @abstractmethod
    def fecha_llegada(self) -> datetime:
        ...

@dataclass(frozen=True)
class Pais(ObjetoValor):
    codigo: Codigo
    nombre: str

@dataclass(frozen=True)
class Ciudad(ObjetoValor):
    pais: Pais
    codigo: Codigo
    nombre: str


