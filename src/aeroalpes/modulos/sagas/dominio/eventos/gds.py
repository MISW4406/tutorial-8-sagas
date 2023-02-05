from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

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