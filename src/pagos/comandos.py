from pulsar.schema import *
from .utils import time_millis
import uuid

class PagarReservaPayload(Record):
    id_correlacion = String(),
    reserva_id = String(),
    monto = Double()
    monto_vat = Double()
    fecha_creacion = Long()
 
class RevertirPagoPayload(Record):
    id = String()
    id_correlacion = String()
    reserva_id = String()

class ComandoPagarReserva(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ComandoPagarReserva")
    datacontenttype = String()
    service_name = String(default="pagos.aeroalpes")
    data = PagarReservaPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoRevertirPago(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="RevertirPagoReserva")
    datacontenttype = String()
    service_name = String(default="pagos.aeroalpes")
    data = RevertirPagoPayload

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
