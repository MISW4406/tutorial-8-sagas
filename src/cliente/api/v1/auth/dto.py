from pydantic import BaseModel

class RegistrarUsuario(BaseModel):
    nombres: str
    apellidos: str
    email: str
    password: str
    es_empresarial: bool