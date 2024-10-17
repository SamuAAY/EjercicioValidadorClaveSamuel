import abc

from abc import ABC


class ReglaValidacion(ABC):
    @abc.abstractmethod
    def es_valida(self):
        pass

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) >= self._longitud_esperada
