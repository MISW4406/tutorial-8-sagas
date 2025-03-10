from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime

from aeroalpes.modulos.vuelos.dominio.eventos.reservas import EventoReserva
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)


class EventoCliente(EventoDominio):
    ...


@dataclass
class ReservaCreada(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    
@dataclass
class ReservaCancelada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaAprobada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ReservaPagada(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None


