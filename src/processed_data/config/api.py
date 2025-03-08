from pydantic import BaseSettings
from typing import Any

class Config(BaseSettings):
    APP_VERSION: str = "2"

settings = Config()

app_configs: dict[str, Any] = {"title": "Procesador de datos SaludTech"}