from articulo import Articulo

class Revista(Articulo):
    def __init__(self, codigo, titulo, precio_base, stock, edicion):
        super().__init__(codigo, titulo, precio_base, stock)
        self.set_edicion(edicion)

    def get_edicion(self):
        return self.__edicion

    def set_edicion(self, edicion):
        if isinstance(edicion, bool) or not isinstance(edicion, int) or edicion <= 0:
            raise ValueError("La edición debe ser un número entero positivo.")
        self.__edicion = edicion

    def calcular_precio_venta(self):
        return self.get_precio_base() * 1.10

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Categoría: Revista | Edición N°: {self.get_edicion()}"
        )