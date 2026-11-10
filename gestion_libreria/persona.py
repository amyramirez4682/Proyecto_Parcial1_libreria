class Persona:
    def __init__(self, identificacion, nombre, correo):
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_correo(correo)

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def set_identificacion(self, identificacion):
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")
        self.__identificacion = identificacion.strip()

    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre.strip()

    def set_correo(self, correo):
        if not isinstance(correo, str) or "@" not in correo:
            raise ValueError("Correo electrónico inválido.")
        self.__correo = correo.strip()


class Cliente(Persona):
    def __init__(self, identificacion, nombre, correo, categoria="Frecuente"):
        super().__init__(identificacion, nombre, correo)
        self.set_categoria(categoria)

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = categoria.strip()

    def mostrar_informacion(self):
        return f"[CLIENTE] Cédula: {self.get_identificacion()} | Nombre: {self.get_nombre()} | Categoría: {self.__categoria}"


class Proveedor(Persona):
    def __init__(self, identificacion, nombre, correo, editorial_empresa):
        super().__init__(identificacion, nombre, correo)
        self.set_editorial_empresa(editorial_empresa)

    def get_editorial_empresa(self):
        return self.__editorial_empresa

    def set_editorial_empresa(self, editorial_empresa):
        if not isinstance(editorial_empresa, str) or not editorial_empresa.strip():
            raise ValueError("El nombre de la empresa/editorial no puede estar vacío.")
        self.__editorial_empresa = editorial_empresa.strip()

    def mostrar_informacion(self):
        return f"[PROVEEDOR] RUC: {self.get_identificacion()} | Empresa: {self.__editorial_empresa} | Contacto: {self.get_nombre()}"