from processed_data.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerDatoProcesado(Query):
    listing_id: uuid.UUID

class ObtenerDatoProcesadoHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...