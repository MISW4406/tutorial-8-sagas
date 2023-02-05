from pulsar.schema import *
from .utils import time_millis
import uuid

from enum import Enum

class ReservaPagada(Record):
    id = String()
    reserva_id = String()
    monto = Double()
    monto_vat = Double()
    fecha_creacion = Long()

class PagoRevertido(Record):
    id = String()
    reserva_id = String()
    fecha_actualizacion = Long()

class EventoPago(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoPago")
    datacontenttype = String()
    service_name = String("pagos.aeroalpes")
    reserva_pagada = ReservaPagada
    pago_revertido = PagoRevertido

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
