"""Mixins reusables parte del seedwork del proyecto

En este archivo usted encontrará las Mixins reusables parte del seedwork del proyecto

"""

from .excepciones import ReglaNegocioExcepcion
from .reglas import ReglaNegocio


class ValidarReglasMixin:
    def validar_regla(self, regla: ReglaNegocio):
        if not regla.es_valido():
            raise ReglaNegocioExcepcion(regla)