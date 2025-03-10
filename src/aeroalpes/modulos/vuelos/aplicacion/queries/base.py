from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaVuelos
from aeroalpes.modulos.vuelos.infraestructura.fabricas import FabricaVista
from aeroalpes.seedwork.aplicacion.queries import QueryHandler


class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    