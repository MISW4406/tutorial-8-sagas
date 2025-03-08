from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoCliente
import uuid


class ProcesarDatos(Record):
    nombres = String()
    apellidos = String()
    email = String()
    tipo_processed_data = TipoCliente
    fecha_creacion = Long()

class ValidarDatoProcesado(Record):
    id = String()
    fecha_validacion = Long()

class DesactivarDatoProcesado(Record):
    id = String()
    fecha_desactivacion = Long()

class ComandoIniciarProcesamientoDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ProcesarDatos")
    datacontenttype = String()
    service_name = String(default="processed_data.aeroalpes")
    data = ProcesarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoValidarDatoProcesado(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ValidarDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.aeroalpes")
    data = ValidarDatoProcesado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoDesactivarDatoProcesado(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="DesactivarDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.aeroalpes")
    data = DesactivarDatoProcesado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)