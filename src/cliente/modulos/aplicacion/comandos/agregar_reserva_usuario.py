from cliente.seedwork.aplicacion.comandos import Comando, ComandoHandler

import uuid

@dataclass
class ComandoAgregarReservaUsuario(Comando):
    id_usuario: uuid.UUID
    id_reserva: uuid.UUID

class AgregarReservaUsuarioHandler(ComandoHandler):
    ...