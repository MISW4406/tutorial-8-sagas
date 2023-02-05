from fastapi import FastAPI
from cliente.config.api import app_configs, settings
from cliente.api.v1.router import router as v1

from cliente.modulos.infraestructura.consumidores import suscribirse_a_topico
from .eventos import EventoUsuario, UsuarioValidado, UsuarioDesactivado, UsuarioRegistrado, TipoCliente

from cliente.modulos.infraestructura.despachadores import Despachador
from cliente.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event('startup')
async def app_startup():
    global tasks
    task = asyncio.ensure_future(suscribirse_a_topico("evento-gds", "sub-integracion", EventoUsuario))
    tasks.append(task)
