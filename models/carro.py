from datetime import date
from .vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, *args, revision_vigente_hasta: date, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._revision_vigente_hasta = revision_vigente_hasta

    def validar_reglas(self) -> None:
        if self._revision_vigente_hasta < date.today():
            raise RuntimeError("La revisión técnico-mecánica está vencida.")

    def mover(self) -> str:
        return "El carro avanza por la vía."
