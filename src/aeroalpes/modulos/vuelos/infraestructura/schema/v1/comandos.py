from pulsar.schema import *

from aeroalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)


class ComandoCrearReservaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records para itinerarios

class ComandoCrearReserva(ComandoIntegracion):
    data = ComandoCrearReservaPayload()