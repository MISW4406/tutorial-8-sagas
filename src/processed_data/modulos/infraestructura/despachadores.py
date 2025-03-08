import pulsar
from pulsar.schema import *

from processed_data.seedwork.infraestructura import utils

class Despachador:
    def __init__(self):
        ...

    def publicar_mensaje(self, mensaje, topico):
        processed_data = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = processed_data.create_producer(topico, schema=AvroSchema(mensaje.__class__))
        publicador.send(mensaje)
        processed_data.close()
