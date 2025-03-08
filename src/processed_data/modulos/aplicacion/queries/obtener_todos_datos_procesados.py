from processed_data.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid

class ObtenerTodosDatosProcesados(Query):
    ...

class ObtenerTodosDatosProcesadosHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...