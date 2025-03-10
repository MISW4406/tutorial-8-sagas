from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery


class ObtenerReservasCanceladas(Query):
    ...

class ObtenerReservasCanceladasHandler(QueryHandler):

    def handle(self) -> ResultadoQuery:
        ...