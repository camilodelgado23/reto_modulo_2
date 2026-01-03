from abc import ABC, abstractmethod
from .movible import Movible
from .motor import Motor
from .conductor import Conductor


class Vehiculo(Movible, ABC):
    def __init__(
        self,
        placa: str,
        marca: str,
        motor: Motor,
        conductor: Conductor | None = None
    ) -> None:
        self.placa = placa
        self.marca = marca
        self._motor = motor
        self._conductor = conductor

    @property
    def placa(self) -> str:
        return self._placa

    @placa.setter
    def placa(self, valor: str) -> None:
        if not valor or len(valor.strip()) < 5:
            raise ValueError("Placa inválida.")
        self._placa = valor.strip().upper()

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Marca inválida.")
        self._marca = valor.strip().title()

    # ✅ CORRECCIÓN: propiedad para exponer el motor sin romper encapsulación
    @property
    def motor(self) -> Motor:
        return self._motor

    # (Opcional, pero útil): permitir cambiar motor con validación
    @motor.setter
    def motor(self, valor: Motor) -> None:
        if not isinstance(valor, Motor):
            raise ValueError("El motor debe ser una instancia de Motor.")
        self._motor = valor

    @property
    def conductor(self) -> Conductor | None:
        return self._conductor

    def asignar_conductor(self, conductor: Conductor) -> None:
        self._conductor = conductor

    def desasignar_conductor(self) -> None:
        self._conductor = None

    @abstractmethod
    def validar_reglas(self) -> None:
        pass

    def iniciar_jornada(self) -> str:
        self.validar_reglas()
        if self._conductor is None:
            raise RuntimeError("No hay conductor asignado.")
        return f"{self.mover()} Conductor: {self._conductor.nombre}"
