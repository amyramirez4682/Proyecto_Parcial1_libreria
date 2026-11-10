from libro import Libro
from persona import Cliente, Proveedor
from venta import Venta

def main():
    print("=== 1. GESTIÓN DE PROVEEDORES ===")
    proveedores = [
        Proveedor("0992345678001", "Editorial Don Bosco", "ventas@donbosco.ec", "Don Bosco Ediciones")
    ]
    for p in proveedores:
        print(p.mostrar_informacion())

    print("\n=== 2. GESTIÓN DE CLIENTES ===")
    clientes = [
        Cliente("0701112223", "Ana Torres", "ana@mail.com", "VIP")
    ]
    for c in clientes:
        print(c.mostrar_informacion())

    print("\n=== 3. GESTIÓN DE INVENTARIO ===")
    inventario = [
        Libro("L001", "Clean Code", 40.00, 10, "Robert Martin", 464)
    ]
    for art in inventario:
        print(f"{art.mostrar_informacion()} | Precio Público: ${art.calcular_precio_venta():.2f}")

    print("\n=== 4. PROCESO DE VENTA ===")
    try:
        mi_venta = Venta("V-001", clientes[0])
        mi_venta.agregar_detalle(inventario[0], 2) # Compra 2 unidades del libro
        
        mi_venta.mostrar_factura()
        
        print("\nInventario actualizado después de la venta:")
        for art in inventario:
            print(f"- {art.get_titulo()}: Stock restante = {art.get_stock()} un.")
            
    except ValueError as e:
        print(f"[Error en la Venta]: {e}")

if __name__ == "__main__":
    main()