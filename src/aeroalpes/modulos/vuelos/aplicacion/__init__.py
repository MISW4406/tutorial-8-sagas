from pydispatch import dispatcher

from aeroalpes.modulos.vuelos.dominio.eventos.reservas import ReservaCreada, ReservaCancelada, ReservaAprobada, \
    ReservaPagada
from .handlers import HandlerReservaIntegracion

dispatcher.connect(HandlerReservaIntegracion.handle_reserva_creada, signal=f'{ReservaCreada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')