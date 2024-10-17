# TODO: Implementa el código del ejercicio aquí
import abc

from abc import ABC

from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, \
    NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    @abc.abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave: str):
        if len(clave) < self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("Su contraseña debe cumplir con la longtitud minima requerida")
        else:
            pass

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")


class ReglaValidacionGanimedes:
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    def contiene_caracter_especial(self, clave):
        if not any(c in '@_#$%' for c in clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un carácter especial (@, _, #, $, %)")


class ReglaValidacionCalisto:

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    calisto = ["CALISTO", "calisto"]

    def contiene_calisto(self, clave):
        for caracter in clave:
            if caracter in self.calisto:
                pass

    def es_valida(self):
        pass


class Validador:
    pass
