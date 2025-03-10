from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime

from aeroalpes.seedwork.dominio.eventos import (EventoDominio)


class EventoPago(EventoDominio):
    ...

@dataclass
class ReservaPagada(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None

@dataclass
class PagoFallido(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None

@dataclass
class PagoRevertido(EventoPago):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    monto: float = None
    monto_vat: float = None
    fecha_actualizacion: datetime = None