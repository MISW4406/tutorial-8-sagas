from fastapi import FastAPI
from cliente.config.api import app_configs, settings
from cliente.api.v1.router import router as v1

from cliente.modulos.infraestructura.consumidores import suscribirse_a_topico
from cliente.modulos.infraestructura.v1.eventos import EventoUsuario, UsuarioValidado, UsuarioDesactivado, UsuarioRegistrado, TipoCliente
from cliente.modulos.infraestructura.v1.comandos import ComandoRegistrarUsuario, ComandoValidarUsuario, ComandoDesactivarUsuario, RegistrarUsuario, ValidarUsuario, DesactivarUsuario
from cliente.modulos.infraestructura.v1 import TipoCliente
from cliente.modulos.infraestructura.despachadores import Despachador
from cliente.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-usuarios", "sub-cliente", EventoUsuario))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-registrar-usuario", "sub-com-registrar-usuario", ComandoRegistrarUsuario))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-validar-usuario", "sub-com-validar-usuario", ComandoValidarUsuario))
    task4 = asyncio.ensure_future(suscribirse_a_topico("comando-desactivar-usuario", "sub-com-desactivar-usuario", ComandoDesactivarUsuario))
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
    payload = UsuarioValidado(id = "1232321321", fecha_validacion = utils.time_millis())
    evento = EventoUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=UsuarioValidado.__name__,
        usuario_validado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-usuarios")
    return {"status": "ok"}

@app.get("/prueba-usuario-registrado", include_in_schema=False)
async def prueba_usuario_registrado() -> dict[str, str]:
    payload = UsuarioRegistrado(
        id = "1232321321", 
        nombres = "Juan",
        apellidos = "Urrego",
        email = "js.urrego110@aeroalpes.net",
        tipo_cliente = TipoCliente.natural,
        fecha_creacion = utils.time_millis())

    evento = EventoUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=UsuarioRegistrado.__name__,
        usuario_registrado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-usuarios")
    return {"status": "ok"}

@app.get("/prueba-usuario-desactivado", include_in_schema=False)
async def prueba_usuario_desactivado() -> dict[str, str]:
    payload = UsuarioDesactivado(id = "1232321321", fecha_validacion = utils.time_millis())
    evento = EventoUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=UsuarioDesactivado.__name__,
        usuario_desactivado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-usuarios")
    return {"status": "ok"}

@app.get("/prueba-registrar-usuario", include_in_schema=False)
async def prueba_registrar_usuario() -> dict[str, str]:
    payload = RegistrarUsuario(
        nombres = "Juan",
        apellidos = "Urrego",
        email = "js.urrego110@aeroalpes.net",
        tipo_cliente = TipoCliente.natural,
        fecha_creacion = utils.time_millis()
    )

    comando = ComandoRegistrarUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=RegistrarUsuario.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-registrar-usuario")
    return {"status": "ok"}

@app.get("/prueba-validar-usuario", include_in_schema=False)
async def prueba_validar_usuario() -> dict[str, str]:
    payload = ValidarUsuario(
        id = "1232321321", 
        fecha_validacion = utils.time_millis()
    )

    comando = ComandoValidarUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ValidarUsuario.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-validar-usuario")
    return {"status": "ok"}

@app.get("/prueba-desactivar-usuario", include_in_schema=False)
async def prueba_desactivar_usuario() -> dict[str, str]:
    payload = DesactivarUsuario(
        id = "1232321321", 
        fecha_validacion = utils.time_millis()
    )

    comando = ComandoDesactivarUsuario(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DesactivarUsuario.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-desactivar-usuario")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
