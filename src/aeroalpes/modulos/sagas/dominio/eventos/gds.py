from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime

from aeroalpes.seedwork.dominio.eventos import (EventoDominio)


class EventoGDS(EventoDominio):
    ...

@dataclass
class ReservaGDSConfirmada(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None

@dataclass
class ConfirmacionGDSRevertida(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None

@dataclass
class ConfirmacionFallida(EventoGDS):
    id_reserva: uuid.UUID = None
    id_correlacion: str = None
    fecha_actualizacion: datetime = None