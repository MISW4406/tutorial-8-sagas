import pulsar
from pulsar.schema import *

from . import utils

class Despachador:
    def __init__(self):
        ...

    def publicar_mensaje(self, mensaje, topico):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(mensaje.__class__))
        publicador.send(mensaje)
        cliente.close()
