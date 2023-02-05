from cliente.seedwork.aplicacion.comandos import Comando, ComandoHandler
from cliente.seedwork.aplicacion.comandos import ejecutar_commando as comando
from cliente.modulos.dominio.entidades import ClienteNatural, ClienteEmpresa, Usuario
from cliente.modulos.dominio.objetos_valor import Cedula, Email, Nombre, Rut 
from dataclasses import dataclass
import datetime
import time

@dataclass
class ComandoRegistrarUsuario(Comando):
    nombres: str
    apellidos: str
    email: str
    password: str
    es_empresarial: bool

class RegistrarUsuarioHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoRegistrarUsuario) -> Usuario:
        params = dict(
            nombre=Nombre(comando.nombres, comando.apellidos),
            email = Email(comando.email, None, comando.es_empresarial), # TODO Lógica para procesar dominio y saber si empresarial
            fecha_creacion = datetime.datetime.now(),
            fecha_actualizacion = datetime.datetime.now()
        )

        if comando.es_empresarial:
            cliente = ClienteEmpresa(**params)
        else:
            cliente = ClienteNatural(**params)

        return cliente
        

    def handle(self, comando: ComandoRegistrarUsuario):

        usuario = self.a_entidad(comando)
        
        


@comando.register(ComandoRegistrarUsuario)
def ejecutar_comando_crear_reserva(comando: ComandoRegistrarUsuario):
    handler = RegistrarUsuarioHandler()
    handler.handle(comando)