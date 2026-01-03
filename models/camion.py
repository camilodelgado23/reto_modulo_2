from .vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(
        self,
        *args,
        planilla_carga: str,
        max_peso: float,
        peso_actual: float,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self._planilla_carga = planilla_carga
        self._max_peso = max_peso
        self._peso_actual = peso_actual

    def validar_reglas(self) -> None:
        if not self._planilla_carga:
            raise RuntimeError("El camión requiere planilla de carga.")
        if self._peso_actual > self._max_peso:
            raise RuntimeError("El camión excede el peso permitido.")

    def mover(self) -> str:
        return "El camión inicia su recorrido."
