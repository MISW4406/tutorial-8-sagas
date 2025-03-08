from processed_data.seedwork.aplicacion.comandos import Comando, ComandoHandler

import uuid

@dataclass
class ComandoCancelarProcesamientoDatos(Comando):
    id_usuario: uuid.UUID
    id_reserva: uuid.UUID

class CancelarProcesamientoDatosHandler(ComandoHandler):
    ...