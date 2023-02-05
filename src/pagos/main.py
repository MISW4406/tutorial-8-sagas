from fastapi import FastAPI
# from cliente.config.api import app_configs, settings
# from cliente.api.v1.router import router as v1

# from cliente.modulos.infraestructura.consumidores import suscribirse_a_topico
# from .eventos import EventoUsuario, UsuarioValidado, UsuarioDesactivado, UsuarioRegistrado, TipoCliente

# from cliente.modulos.infraestructura.despachadores import Despachador
# from cliente.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn

from pydantic import BaseSettings
from typing import Any

from .eventos import EventoPago, PagoRevertido, ReservaPagada
from .comandos import ComandoPagarReserva, ComandoRevertirPago, RevertirPagoPayload, PagarReservaPayload
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador

from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Pagos AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-pago", "sub-pagos", EventoPago))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-pagar-reserva", "sub-com-pagos-reservar", ComandoPagarReserva))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-revertir-pago", "sub-com-pagos-revertir", ComandoRevertirPago))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-reserva-pagada", include_in_schema=False)
async def prueba_reserva_pagada() -> dict[str, str]:
    payload = ReservaPagada(
        id = "1232321321",
        id_correlacion = "389822434",
        reserva_id = "6463454",
        monto = 23412.12,
        monto_vat = 234.0,
        fecha_creacion = utils.time_millis()
    )

    evento = EventoPago(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ReservaPagada.__name__,
        reserva_pagada = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-pago")
    return {"status": "ok"}

@app.get("/prueba-pago-revertido", include_in_schema=False)
async def prueba_pago_revertido() -> dict[str, str]:
    payload = PagoRevertido(
        id = "1232321321",
        id_correlacion = "389822434",
        reserva_id = "6463454",
        fecha_actualizacion = utils.time_millis()
    )

    evento = EventoPago(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=PagoRevertido.__name__,
        pago_revertido = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-pago")
    return {"status": "ok"}
    
@app.get("/prueba-pagar-reserva", include_in_schema=False)
async def prueba_pagar_reserva() -> dict[str, str]:
    payload = PagarReservaPayload(
        id_correlacion = "389822434",
        reserva_id = "6463454",
        monto = 23412.12,
        monto_vat = 234.0,
    )

    comando = ComandoPagarReserva(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ReservaPagada.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-pagar-reserva")
    return {"status": "ok"}

@app.get("/prueba-revertir-pago", include_in_schema=False)
async def prueba_revertir_pago() -> dict[str, str]:
    payload = RevertirPagoPayload(
        id = "1232321321",
        id_correlacion = "389822434",
        reserva_id = "6463454",
    )

    comando = ComandoRevertirPago(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=RevertirPagoPayload.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-revertir-pago")
    return {"status": "ok"}