from models.conductor import Conductor
from models.vehiculo import Vehiculo
from services.conductor_service import ConductorService
from services.vehiculo_service import VehiculoService

class JornadaService:
    def __init__(self, conductor_srv: ConductorService, vehiculo_srv: VehiculoService) -> None:
        self._conductor_srv = conductor_srv
        self._vehiculo_srv = vehiculo_srv

    def asignar_conductor_a_vehiculo(self, documento_conductor: str, placa_vehiculo: str) -> None:
        conductor = self._conductor_srv.obtener_conductor(documento_conductor)
        vehiculo = self._vehiculo_srv.obtener_vehiculo(placa_vehiculo)

        if conductor is None:
            raise ValueError("Conductor no encontrado.")
        if vehiculo is None:
            raise ValueError("Vehículo no encontrado.")

        vehiculo.asignar_conductor(conductor)
