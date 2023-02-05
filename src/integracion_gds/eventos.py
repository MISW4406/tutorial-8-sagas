from pulsar.schema import *
from .utils import time_millis
import uuid

class ReservaConfirmada(Record):
    id = String(),
    id_correlacion = String(),
    reserva_id = String()
    fecha_confirmacion = Long()
 
class ConfirmacionRevertida(Record):
    id = String()
    id_correlacion = String()
    reserva_id = String()
    fecha_actualizacion = Long()

class EventoConfirmacionGDS(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoPago")
    datacontenttype = String()
    service_name = String(default="pagos.aeroalpes")
    confirmacion_revertida = ConfirmacionRevertida
    reserva_confirmada = ReservaConfirmada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
