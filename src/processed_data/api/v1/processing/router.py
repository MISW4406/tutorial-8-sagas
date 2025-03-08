from fastapi import APIRouter, status, BackgroundTasks
from processed_data.modulos.aplicacion.comandos.iniciar_procesamiento_datos import ComandoIniciarProcesamientoDatos
from processed_data.seedwork.presentacion.dto import RespuestaAsincrona
from processed_data.seedwork.aplicacion.comandos import ejecutar_commando
from processed_data.seedwork.aplicacion.queries import ejecutar_query

from .dto import ProcesarDatos


router = APIRouter()

@router.post("/procesar", status_code=status.HTTP_202_ACCEPTED, response_model=RespuestaAsincrona)
async def procesar_datos(procesar_datos: ProcesarDatos, background_tasks: BackgroundTasks) -> dict[str, str]:
    comando = ComandoIniciarProcesamientoDatos(
        nombres=procesar_datos.url_raw_data,
        )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Procesando datos")