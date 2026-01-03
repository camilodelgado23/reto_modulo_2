class Motor:
    def __init__(self, serial: str, cilindraje: int) -> None:
        if not serial or len(serial.strip()) < 4:
            raise ValueError("El serial del motor no es válido.")
        if cilindraje <= 0:
            raise ValueError("El cilindraje debe ser positivo.")

        self._serial = serial.strip()
        self._cilindraje = cilindraje

    @property
    def serial(self) -> str:
        return self._serial

    @property
    def cilindraje(self) -> int:
        return self._cilindraje
