#  Sistema de Gestión de Vehículos y Conductores

**Reto – Programación Orientada a Objetos (Módulo 2)**

##  Descripción general

Este proyecto modela digitalmente la operación básica de la empresa **Transporte Seguro S.A.**, la cual necesita gestionar conductores y distintos tipos de vehículos, aplicando reglas de negocio específicas según cada tipo.

El sistema está desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)**.

---

##  Objetivos del sistema

El sistema permite:

* Registrar **conductores** con datos validados.
* Crear distintos **vehículos** con atributos encapsulados.
* Aplicar **reglas de negocio diferenciadas** según el tipo de vehículo.
* Asignar un conductor a un vehículo (**agregación**).
* Iniciar una jornada de trabajo para cada vehículo (**polimorfismo**).

---

##  Requisitos del reto (cumplidos)

Registrar conductores con validaciones:

* Nombre
* Documento
* Licencia

Crear vehículos:

* Moto
* Carro
* Camión

Reglas por tipo de vehículo:

* **Moto** → casco obligatorio
* **Carro** → revisión técnico-mecánica vigente
* **Camión** → planilla de carga y peso máximo permitido

Implementación de:

* Clase abstracta `Vehiculo`
* Subclases `Moto`, `Carro`, `Camion`
* Interfaz `Movible` con método `mover()`
* **Composición**: cada vehículo tiene un `Motor`
* **Agregación**: un vehículo puede existir sin conductor
* **Polimorfismo** al iniciar la jornada

---

## Arquitectura del proyecto

```
proyecto_transporte/
│
├─ models/
│  ├─ __init__.py
│  ├─ movible.py
│  ├─ motor.py
│  ├─ conductor.py
│  ├─ vehiculo.py
│  ├─ moto.py
│  ├─ carro.py
│  └─ camion.py
│
├─ services/
│  ├─ __init__.py
│  ├─ conductor_service.py
│  ├─ vehiculo_service.py
│  └─ jornada_service.py
│
└─ main.py

```

###  models

Contiene las entidades del dominio y las reglas de negocio:

* Clases con atributos encapsulados
* Validaciones mediante `@property`
* Herencia, abstracción y polimorfismo

###  services

Implementa la lógica de aplicación:

* Registro y gestión de conductores
* Registro y gestión de vehículos
* Asignación de conductores
* Inicio de jornadas de trabajo

### main.py

Archivo de ejecución:

* Carga datos iniciales de prueba
* Muestra listados
* Asigna conductores
* Inicia jornadas demostrando polimorfismo y reglas de negocio

---

##  Ejecución del proyecto

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
```

---

## Salida esperada (ejemplo)

```
LISTA INICIAL DE CONDUCTORES 
- Carlos Pérez | Doc: 123456789 | Lic: B12345
- Ana Gómez | Doc: 987654321 | Lic: C99887

LISTA INICIAL DE VEHÍCULOS 
- Moto | Placa: ABC12 | Marca: Yamaha | Motor: MTR-0001
- Carro | Placa: XYZ99 | Marca: Toyota | Motor: MTR-0002
- Camion | Placa: TRK55 | Marca: Volvo | Motor: MTR-0003

INICIAR JORNADA (POLIMORFISMO)
[ABC12] La moto se pone en marcha. Conductor: Carlos Pérez
[XYZ99] El carro avanza por la vía. Conductor: Ana Gómez
[TRK55] El camión inicia su recorrido. Conductor: Carlos Pérez
```

---

## Conceptos de POO aplicados

* **Encapsulación**: atributos privados y acceso controlado mediante propiedades.
* **Herencia**: `Moto`, `Carro` y `Camion` heredan de `Vehiculo`.
* **Abstracción**: clase abstracta `Vehiculo` y método `validar_reglas`.
* **Polimorfismo**: mismo método `iniciar_jornada()` con comportamientos distintos.
* **Composición**: cada vehículo contiene un `Motor`.
* **Agregación**: un vehículo puede existir sin conductor asignado.

---

## Tecnologías usadas

* Python 3.x
* Programación Orientada a Objetos
* Módulos estándar (`abc`, `datetime`, `typing`)

---

## Conclusión

Este proyecto cumple completamente con los requerimientos del reto del **Módulo 2**, demostrando un diseño limpio, escalable y alineado con las buenas prácticas de Programación Orientada a Objetos en Python.

