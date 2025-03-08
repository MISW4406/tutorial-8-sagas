

from processed_data.modulos.vuelos.dominio.eventos.reservas import ReservaCreada
from processed_data.seedwork.aplicacion.handlers import Handler

class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print('================ RESERVA CREADA ===========')
        

    