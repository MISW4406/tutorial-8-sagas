from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager

from pydantic_settings import BaseSettings
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
tasks = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    task1 = asyncio.create_task(suscribirse_a_topico("evento-pago", "sub-pagos", EventoPago))
    task2 = asyncio.create_task(suscribirse_a_topico("comando-pagar-reserva", "sub-com-pagos-reservar", ComandoPagarReserva))
    task3 = asyncio.create_task(suscribirse_a_topico("comando-revertir-pago", "sub-com-pagos-revertir", ComandoRevertirPago))
    tasks.extend([task1, task2, task3])

    yield

    for task in tasks:
        task.cancel()

app = FastAPI(lifespan=lifespan, **app_configs)

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
