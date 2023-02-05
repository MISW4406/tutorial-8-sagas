from pydantic import BaseSettings
from typing import Any

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()

app_configs: dict[str, Any] = {"title": "Cliente AeroAlpes"}