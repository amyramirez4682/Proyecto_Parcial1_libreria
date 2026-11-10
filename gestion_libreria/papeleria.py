from articulo import Articulo

class Papeleria(Articulo):
    def __init__(self, codigo, titulo, precio_base, stock, marca):
        super().__init__(codigo, titulo, precio_base, stock)
        self.set_marca(marca)

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        if not isinstance(marca, str) or not marca.strip():
            raise ValueError("La marca no puede estar vacía.")
        self.__marca = marca.strip()

    def calcular_precio_venta(self):
        return self.get_precio_base() * 1.15

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Categoría: Papelería | Marca: {self.get_marca()}"
        )