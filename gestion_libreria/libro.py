from articulo import Articulo

class Libro(Articulo):
    def __init__(self, codigo, titulo, precio_base, stock, autor, paginas):
        super().__init__(codigo, titulo, precio_base, stock)
        self.set_autor(autor)
        self.set_paginas(paginas)

    def get_autor(self):
        return self.__autor

    def get_paginas(self):
        return self.__paginas

    def set_autor(self, autor):
        if not isinstance(autor, str) or not autor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self.__autor = autor.strip()

    def set_paginas(self, paginas):
        if isinstance(paginas, bool) or not isinstance(paginas, int) or paginas <= 0:
            raise ValueError("El número de páginas debe ser positivo.")
        self.__paginas = paginas

    def calcular_precio_venta(self):
        return self.get_precio_base() + 2.50

    def mostrar_informacion(self):
        return (
            f"{super().mostrar_informacion()}\n"
            f"Categoría: Libro | Autor: {self.get_autor()} | Páginas: {self.get_paginas()}"
        )