"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las entidades reusables parte del seedwork del proyecto

"""

import uuid
from dataclasses import dataclass, field
from datetime import datetime

from .eventos import EventoDominio
from .excepciones import IdDebeSerInmutableExcepcion
from .mixins import ValidarReglasMixin
from .reglas import IdEntidadEsInmutable


@dataclass
class Entidad:
    id: uuid.UUID = field(hash=True)
    _id: uuid.UUID = field(init=False, repr=False, hash=True)
    fecha_creacion: datetime =  field(default=datetime.now())
    fecha_actualizacion: datetime = field(default=datetime.now())

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: uuid.UUID) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise IdDebeSerInmutableExcepcion()
        self._id = self.siguiente_id()
        

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    eventos: list[EventoDominio] = field(default_factory=list)
    eventos_compensacion: list[EventoDominio] = field(default_factory=list)

    def agregar_evento(self, evento: EventoDominio, evento_compensacion: EventoDominio = None):
        self.eventos.append(evento)

        if evento_compensacion:
            self.eventos_compensacion.append(evento_compensacion)
    
    def limpiar_eventos(self):
        self.eventos = list()
        self.eventos_compensacion = list()


@dataclass
class Locacion(Entidad):
    def __str__(self) -> str:
        ...