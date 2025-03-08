from pulsar.schema import *
from processed_data.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoCliente
import uuid



# NOTE En este caso usamos composición de eventos, donde un evento DatoProcesado es constituido 
# por los eventos hijo. Recuerde que al ser mensajes inmutables, no consideramos conceptos como
# la herencia en los registros de esquemas. Por lo que el patrón de composición de mensajes se vuelve una buena opción
# esto nos permite seguir teniendo esquemas estrictos sin la necesidad de múltiples tópicos
class DatoProcesadoRegistrado(Record):
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_processed_data = TipoCliente
    fecha_creacion = Long()

class DatoProcesadoValidado(Record):
    id = String()
    fecha_validacion = Long()

class DatoProcesadoDesactivado(Record):
    id = String()
    fecha_desactivacion = Long()

class EventoDatoProcesado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.aeroalpes")
    usuario_registrado = DatoProcesadoRegistrado
    usuario_validado = DatoProcesadoValidado
    usuario_desactivado = DatoProcesadoDesactivado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)