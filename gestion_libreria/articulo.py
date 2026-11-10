class Articulo:
    def __init__(self, codigo, titulo, precio_base, stock):
        self.set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_precio_base(precio_base)
        self.set_stock(stock)

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_precio_base(self):
        return self.__precio_base

    def get_stock(self):
        return self.__stock

    def set_codigo(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        self.__codigo = codigo.strip()

    def set_titulo(self, titulo):
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título no puede estar vacío.")
        self.__titulo = titulo.strip()

    def set_precio_base(self, precio_base):
        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise ValueError("El precio base debe ser positivo.")
        self.__precio_base = float(precio_base)

    def set_stock(self, stock):
        if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = stock

    def mostrar_informacion(self):
        return (
            f"Código: {self.get_codigo()} | Título: {self.get_titulo()} | "
            f"Precio Base: ${self.get_precio_base():.2f} | Stock: {self.get_stock()} un."
        )

    def calcular_precio_venta(self):
        raise NotImplementedError("Las clases hijas deben implementar este método.")