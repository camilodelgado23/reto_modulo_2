from .vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, *args, casco_obligatorio: bool, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._casco_obligatorio = casco_obligatorio

    def validar_reglas(self) -> None:
        if not self._casco_obligatorio:
            raise RuntimeError("La moto requiere casco obligatorio.")

    def mover(self) -> str:
        return "La moto se pone en marcha."
