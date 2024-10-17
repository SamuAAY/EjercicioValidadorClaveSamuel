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

    def _contiene_mayuscula(self, clave) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False


class ReglaValidacionGanimedes:

