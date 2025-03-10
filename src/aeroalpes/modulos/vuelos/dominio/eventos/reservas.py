from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime

from aeroalpes.seedwork.dominio.eventos import (EventoDominio)


class EventoReserva(EventoDominio):
    ...


@dataclass
class ReservaCreada(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    monto: float = None
    monto_vat: float = None
    
@dataclass
class CreacionReservaFallida(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    monto: float = None
    monto_vat: float = None

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

@dataclass
class AprobacionReservaFallida(EventoReserva):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None


