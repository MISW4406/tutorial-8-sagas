from fastapi import FastAPI
from processed_data.config.api import app_configs, settings
from processed_data.api.v1.router import router as v1

from processed_data.modulos.infraestructura.consumidores import suscribirse_a_topico
from processed_data.modulos.infraestructura.v1.eventos import EventoDatoProcesado, DatoProcesadoValidado, DatoProcesadoDesactivado, DatoProcesadoRegistrado, TipoCliente
from processed_data.modulos.infraestructura.v1.comandos import ComandoIniciarProcesamientoDatos, ComandoValidarDatoProcesado, ComandoDesactivarDatoProcesado, ProcesarDatos, ValidarDatoProcesado, DesactivarDatoProcesado
from processed_data.modulos.infraestructura.v1 import TipoCliente
from processed_data.modulos.infraestructura.despachadores import Despachador
from processed_data.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-dato-procesado", "sub-processed_data", EventoDatoProcesado))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-iniciar-procesamiento-datos", "sub-com-procesar-usuario", ComandoIniciarProcesamientoDatos))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-validar-usuario", "sub-com-validar-usuario", ComandoValidarDatoProcesado))
    task4 = asyncio.ensure_future(suscribirse_a_topico("comando-desactivar-usuario", "sub-com-desactivar-usuario", ComandoDesactivarDatoProcesado))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-usuario-validado", include_in_schema=False)
async def prueba_usuario_validado() -> dict[str, str]:
    payload = DatoProcesadoValidado(id = "1232321321", fecha_validacion = utils.time_millis())
    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoProcesadoValidado.__name__,
        usuario_validado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-dato-procesado")
    return {"status": "ok"}

@app.get("/prueba-usuario-registrado", include_in_schema=False)
async def prueba_usuario_registrado() -> dict[str, str]:
    payload = DatoProcesadoRegistrado(
        id = "1232321321", 
        nombres = "Juan",
        apellidos = "Urrego",
        email = "js.urrego110@aeroalpes.net",
        tipo_processed_data = TipoCliente.natural,
        fecha_creacion = utils.time_millis())

    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoProcesadoRegistrado.__name__,
        usuario_registrado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-dato-procesado")
    return {"status": "ok"}

@app.get("/prueba-usuario-desactivado", include_in_schema=False)
async def prueba_usuario_desactivado() -> dict[str, str]:
    payload = DatoProcesadoDesactivado(id = "1232321321", fecha_validacion = utils.time_millis())
    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoProcesadoDesactivado.__name__,
        usuario_desactivado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-dato-procesado")
    return {"status": "ok"}

@app.get("/prueba-procesar-usuario", include_in_schema=False)
async def prueba_procesar_datos() -> dict[str, str]:
    payload = ProcesarDatos(
        nombres = "Juan",
        apellidos = "Urrego",
        email = "js.urrego110@aeroalpes.net",
        tipo_processed_data = TipoCliente.natural,
        fecha_creacion = utils.time_millis()
    )

    comando = ComandoIniciarProcesamientoDatos(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ProcesarDatos.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-iniciar-procesamiento-datos")
    return {"status": "ok"}

@app.get("/prueba-validar-usuario", include_in_schema=False)
async def prueba_validar_usuario() -> dict[str, str]:
    payload = ValidarDatoProcesado(
        id = "1232321321", 
        fecha_validacion = utils.time_millis()
    )

    comando = ComandoValidarDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ValidarDatoProcesado.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-validar-usuario")
    return {"status": "ok"}

@app.get("/prueba-cancelar-procesar-datos", include_in_schema=False)
async def prueba_cancelar_procesar_datos() -> dict[str, str]:
    payload = DesactivarDatoProcesado(
        id = "1232321321", 
        fecha_validacion = utils.time_millis()
    )

    comando = ComandoDesactivarDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DesactivarDatoProcesado.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-desactivar-usuario")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
