from processed_data.seedwork.aplicacion.comandos import Comando, ComandoHandler

@dataclass
class ComandoGuardarDatosProcesados(Comando):
    email: str
    password: str

class GuardarDatosProcesadosHandler(ComandoHandler):
    ...