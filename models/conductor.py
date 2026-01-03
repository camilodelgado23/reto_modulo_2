class Conductor:
    def __init__(self, nombre: str, documento: str, licencia: str) -> None:
        self.nombre = nombre
        self.documento = documento
        self.licencia = licencia

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or len(valor.strip()) < 3:
            raise ValueError("Nombre inválido.")
        self._nombre = valor.strip().title()

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, valor: str) -> None:
        if not valor.isdigit():
            raise ValueError("Documento inválido.")
        self._documento = valor

    @property
    def licencia(self) -> str:
        return self._licencia

    @licencia.setter
    def licencia(self, valor: str) -> None:
        if not valor or len(valor.strip()) < 5:
            raise ValueError("Licencia inválida.")
        self._licencia = valor.strip().upper()
