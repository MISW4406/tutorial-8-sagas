from processed_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from processed_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from processed_data.modulos.dominio.entidades import ClienteNatural, ClienteEmpresa, DatoProcesado
from processed_data.modulos.dominio.objetos_valor import Cedula, Email, Nombre, Rut 
from dataclasses import dataclass
import datetime
import time

@dataclass
class ComandoIniciarProcesamientoDatos(Comando):
    nombres: str
    apellidos: str
    email: str
    password: str
    es_empresarial: bool

class IniciarProcesamientoDatosHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoIniciarProcesamientoDatos) -> DatoProcesado:
        params = dict(
            nombre=Nombre(comando.nombres, comando.apellidos),
            email = Email(comando.email, None, comando.es_empresarial), # TODO Lógica para procesar dominio y saber si empresarial
            fecha_creacion = datetime.datetime.now(),
            fecha_actualizacion = datetime.datetime.now()
        )

        if comando.es_empresarial:
            processed_data = ClienteEmpresa(**params)
        else:
            processed_data = ClienteNatural(**params)

        return processed_data
        

    def handle(self, comando: ComandoIniciarProcesamientoDatos):

        usuario = self.a_entidad(comando)
        
        


@comando.register(ComandoIniciarProcesamientoDatos)
def ejecutar_comando_crear_reserva(comando: ComandoIniciarProcesamientoDatos):
    handler = IniciarProcesamientoDatosHandler()
    handler.handle(comando)