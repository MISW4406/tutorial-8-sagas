from processed_data.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerDatosProcesadosDesactivados(Query):
    status: str

class ObtenerDatosProcesadosDesactivadosHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...