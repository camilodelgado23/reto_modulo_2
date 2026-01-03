from models.vehiculo import Vehiculo

class VehiculoService:
    def __init__(self) -> None:
        self._vehiculos: dict[str, Vehiculo] = {}

    def registrar_vehiculo(self, vehiculo: Vehiculo) -> None:
        if vehiculo.placa in self._vehiculos:
            raise ValueError("Ya existe un vehículo con esa placa.")
        self._vehiculos[vehiculo.placa] = vehiculo

    def obtener_vehiculo(self, placa: str) -> Vehiculo | None:
        return self._vehiculos.get(placa)

    def listar_vehiculos(self) -> list[Vehiculo]:
        return list(self._vehiculos.values())
