class DetalleVenta:
    def __init__(self, articulo, cantidad):
        self.articulo = articulo
        self.cantidad = cantidad
        self.subtotal = articulo.calcular_precio_venta() * cantidad


class Venta:
    def __init__(self, id_venta, cliente):
        self.__id_venta = id_venta
        self.__cliente = cliente
        self.__detalles = []
        self.__total = 0.0

    def agregar_detalle(self, articulo, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        if articulo.get_stock() < cantidad:
            raise ValueError(f"Stock insuficiente para '{articulo.get_titulo()}'. Disponible: {articulo.get_stock()}")
        
        articulo.set_stock(articulo.get_stock() - cantidad)
        
        detalle = DetalleVenta(articulo, cantidad)
        self.__detalles.append(detalle)
        self.__calcular_total()

    def __calcular_total(self):
        self.__total = sum(d.subtotal for d in self.__detalles)

    def mostrar_factura(self):
        print("========================================")
        print(f" FACTURA N°: {self.__id_venta}")
        print(f" {self.__cliente.mostrar_informacion()}")
        print("----------------------------------------")
        print(" Detalle de compra:")
        for d in self.__detalles:
            print(f" - {d.cantidad}x {d.articulo.get_titulo()} (${d.articulo.calcular_precio_venta():.2f} c/u) = Subtotal: ${d.subtotal:.2f}")
        print("----------------------------------------")
        print(f" TOTAL A PAGAR: ${self.__total:.2f}")
        print("========================================")