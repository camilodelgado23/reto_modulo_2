from models.conductor import Conductor

class ConductorService:
    def __init__(self) -> None:
        self._conductores: dict[str, Conductor] = {}

    def registrar_conductor(self, conductor: Conductor) -> None:
        if conductor.documento in self._conductores:
            raise ValueError("Ya existe un conductor con ese documento.")
        self._conductores[conductor.documento] = conductor

    def obtener_conductor(self, documento: str) -> Conductor | None:
        return self._conductores.get(documento)

    def listar_conductores(self) -> list[Conductor]:
        return list(self._conductores.values())
