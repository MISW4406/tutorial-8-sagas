

from cliente.modulos.vuelos.dominio.eventos.reservas import ReservaCreada
from cliente.seedwork.aplicacion.handlers import Handler

class HandlerReservaDominio(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print('================ RESERVA CREADA ===========')
        

    