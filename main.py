from datetime import date, timedelta

from models.conductor import Conductor
from models.motor import Motor
from models.moto import Moto
from models.carro import Carro
from models.camion import Camion

from services.conductor_service import ConductorService
from services.vehiculo_service import VehiculoService
from services.jornada_service import JornadaService


def poblar_datos_iniciales(
    conductor_srv: ConductorService,
    vehiculo_srv: VehiculoService
) -> None:
    """
    Crea conductores y vehículos de ejemplo para probar el sistema.
    """

    c1 = Conductor(nombre="Carlos Pérez", documento="123456789", licencia="B12345")
    c2 = Conductor(nombre="Ana Gómez", documento="987654321", licencia="C99887")

    conductor_srv.registrar_conductor(c1)
    conductor_srv.registrar_conductor(c2)

    moto = Moto(
        placa="ABC12",
        marca="Yamaha",
        motor=Motor(serial="MTR-0001", cilindraje=150),
        casco_obligatorio=True,
    )

    carro = Carro(
        placa="XYZ99",
        marca="Toyota",
        motor=Motor(serial="MTR-0002", cilindraje=1800),
        revision_vigente_hasta=date.today(),  # vigente
    )

    camion = Camion(
        placa="TRK55",
        marca="Volvo",
        motor=Motor(serial="MTR-0003", cilindraje=12000),
        planilla_carga="PL-2026-001",
        max_peso=20000,
        peso_actual=15000,
    )

    carro_vencido = Carro(
        placa="BAD01",
        marca="Mazda",
        motor=Motor(serial="MTR-0004", cilindraje=2000),
        revision_vigente_hasta=date.today() - timedelta(days=1),  # vencida
    )

    vehiculo_srv.registrar_vehiculo(moto)
    vehiculo_srv.registrar_vehiculo(carro)
    vehiculo_srv.registrar_vehiculo(camion)
    vehiculo_srv.registrar_vehiculo(carro_vencido)


def main() -> None:
    conductor_srv = ConductorService()
    vehiculo_srv = VehiculoService()
    jornada_srv = JornadaService(conductor_srv, vehiculo_srv)

    poblar_datos_iniciales(conductor_srv, vehiculo_srv)

    print("=== LISTA INICIAL DE CONDUCTORES ===")
    for c in conductor_srv.listar_conductores():
        print(f"- {c.nombre} | Doc: {c.documento} | Lic: {c.licencia}")

    print("\n=== LISTA INICIAL DE VEHÍCULOS ===")
    for v in vehiculo_srv.listar_vehiculos():
        print(f"- {v.__class__.__name__} | Placa: {v.placa} | Marca: {v.marca} | Motor: {v.motor.serial}")

    print("\n=== ASIGNACIÓN DE CONDUCTORES (AGREGACIÓN) ===")
    jornada_srv.asignar_conductor_a_vehiculo(documento_conductor="123456789", placa_vehiculo="ABC12")
    jornada_srv.asignar_conductor_a_vehiculo(documento_conductor="987654321", placa_vehiculo="XYZ99")
    jornada_srv.asignar_conductor_a_vehiculo(documento_conductor="123456789", placa_vehiculo="TRK55")

    print("Conductores asignados a vehículos (algunos vehículos pueden existir sin conductor).")

    print("\n=== INICIAR JORNADA (POLIMORFISMO + REGLAS POR TIPO) ===")
    for v in vehiculo_srv.listar_vehiculos():
        try:
            print(f"[{v.placa}]  {v.iniciar_jornada()}")
        except Exception as e:
            print(f"[{v.placa}]  {e}")

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
