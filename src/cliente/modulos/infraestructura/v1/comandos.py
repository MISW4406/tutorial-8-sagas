from pulsar.schema import *
from dataclasses import dataclass, field
from cliente.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from cliente.seedwork.infraestructura.utils import time_millis
from cliente.modulos.infraestructura.v1 import TipoCliente
import uuid


class RegistrarUsuario(Record):
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
    fecha_creacion = Long()

class ValidarUsuario(Record):
    id = String()
    fecha_validacion = Long()

class DesactivarUsuario(Record):
    id = String()
    fecha_desactivacion = Long()

class ComandoRegistrarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="RegistrarUsuario")
    datacontenttype = String()
    service_name = String(default="cliente.aeroalpes")
    data = RegistrarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoValidarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ValidarUsuario")
    datacontenttype = String()
    service_name = String(default="cliente.aeroalpes")
    data = ValidarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoDesactivarUsuario(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="DesactivarUsuario")
    datacontenttype = String()
    service_name = String(default="cliente.aeroalpes")
    data = DesactivarUsuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)