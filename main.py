PRODUCTOS = [
    {"id": 1, "nombre": "Pan de Hamburguesa", "precio": 0.50, "stock": 10},
    {"id": 2, "nombre": "Croissant", "precio": 1.20, "stock": 5},
    {"id": 3, "nombre": "Pastel de Chocolate", "precio": 15.00, "stock": 2}
]

CLIENTES = [
    {"cedula": "1712345678", "nombre": "Juan Perez", "tipo": "Regular"},
    {"cedula": "1787654321", "nombre": "Maria Lopez", "tipo": "VIP"}
]

PEDIDOS = []

def ejecutar_sistema():
    while True:
        print("\n--- SISTEMA DE PANADERÍA (CÓDIGO ESPAGUETI) ---")
        print("1. Ver Catálogo de Productos")
        print("2. Registrar Cliente")
        print("3. Crear Pedido y Facturar")
        print("4. Ver Todos los Pedidos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n--- CATÁLOGO DE PRODUCTOS ---")
            for p in PRODUCTOS:
                print(f"ID: {p['id']} | {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")
                
        elif opcion == "2":
            print("\n--- REGISTRAR CLIENTE ---")
            cedula = input("Cédula: ")
            nombre = input("Nombre completo: ")
            tipo = input("Tipo de cliente (Regular/VIP): ")
            CLIENTES.append({"cedula": cedula, "nombre": nombre, "tipo": tipo})
            print("Cliente registrado con éxito.")
            
        elif opcion == "3":
            print("\n--- NUEVO PEDIDO ---")
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            
            cliente_encontrado = None
            for c in CLIENTES:
                if c["cedula"] == cedula_cliente:
                    cliente_encontrado = c
                    break
            
            if not cliente_encontrado:
                print("Error: El cliente no está registrado.")
                continue
                
            items_pedido = []
            subtotal = 0.0
            
            while True:
                id_prod = input("ID del producto (o 'f' para finalizar): ")
                if id_prod.lower() == 'f':
                    break
                    
                producto_encontrado = None
                for p in PRODUCTOS:
                    if str(p["id"]) == id_prod:
                        producto_encontrado = p
                        break
                        
                if not producto_encontrado:
                    print("Producto no encontrado.")
                    continue
                    
                cantidad = int(input(f"Cantidad de {producto_encontrado['nombre']}: "))
                
                if cantidad > producto_encontrado["stock"]:
                    print(f"¡Error! Stock insuficiente. Quedan {producto_encontrado['stock']}.")
                    continue
                
                producto_encontrado["stock"] -= cantidad
                total_item = producto_encontrado["precio"] * cantidad
                subtotal += total_item
                
                items_pedido.append({
                    "producto": producto_encontrado["nombre"],
                    "cantidad": cantidad,
                    "precio_unitario": producto_encontrado["precio"],
                    "total_item": total_item
                })
                print(f"{producto_encontrado['nombre']} añadido.")
            
            if not items_pedido:
                print("Pedido cancelado.")
                continue
                
            descuento = 0.0
            if cliente_encontrado["tipo"].upper() == "VIP":
                descuento = subtotal * 0.10
                
            total_final = subtotal - descuento
            
            nuevo_pedido = {
                "id_pedido": len(PEDIDOS) + 1,
                "cliente": cliente_encontrado["nombre"],
                "items": items_pedido,
                "subtotal": subtotal,
                "descuento": descuento,
                "total": total_final
            }
            PEDIDOS.append(nuevo_pedido)
            
            print("\n========================================")
            print("               FACTURA                 ")
            print("========================================")
            print(f"Pedido N°: {nuevo_pedido['id_pedido']}")
            print(f"Cliente: {nuevo_pedido['cliente']} ({cliente_encontrado['tipo']})")
            print("----------------------------------------")
            for item in nuevo_pedido["items"]:
                print(f"{item['cantidad']}x {item['producto']} - ${item['total_item']:.2f}")
            print("----------------------------------------")
            print(f"Subtotal:  ${nuevo_pedido['subtotal']:.2f}")
            print(f"Descuento: -${nuevo_pedido['descuento']:.2f}")
            print(f"TOTAL:     ${nuevo_pedido['total']:.2f}")
            print("========================================\n")
            
        elif opcion == "4":
            print("\n--- HISTORIAL DE PEDIDOS ---")
            if not PEDIDOS:
                print("No hay pedidos registrados.")
            for ped in PEDIDOS:
                print(f"Pedido #{ped['id_pedido']} | Cliente: {ped['cliente']} | Total: ${ped['total']:.2f}")
                
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_sistema()