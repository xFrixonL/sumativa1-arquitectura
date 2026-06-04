class PanaderiaController:
    def __init__(self, service):
        self.service = service

    def iniciar(self):
        while True:
            print("\n--- SISTEMA DE PANADERÍA (MONOLÍTICO POR CAPAS) ---")
            print("1. Ver Catálogo de Productos")
            print("2. Registrar Cliente")
            print("3. Crear Pedido y Facturar")
            print("4. Ver Todos los Pedidos")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\n--- CATÁLOGO DE PRODUCTOS ---")
                for p in self.service.listar_catalogo():
                    print(f"ID: {p['id']} | {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['stock']}")
                    
            elif opcion == "2":
                print("\n--- REGISTRAR CLIENTE ---")
                cedula = input("Cédula: ")
                nombre = input("Nombre completo: ")
                tipo = input("Tipo de cliente (Regular/VIP): ")
                self.service.registrar_cliente(cedula, nombre, tipo)
                print("Cliente registrado con éxito.")
                
            elif opcion == "3":
                print("\n--- NUEVO PEDIDO ---")
                cedula = input("Ingrese la cédula del cliente: ")
                
                items_a_comprar = []
                while True:
                    id_prod = input("ID del producto (o 'f' para finalizar): ")
                    if id_prod.lower() == 'f':
                        break
                    try:
                        cantidad = int(input("Cantidad: "))
                        items_a_comprar.append({"id": int(id_prod), "amount": cantidad} if 'amount' in id_prod else {"id": int(id_prod), "cantidad": cantidad})
                    except ValueError:
                        print("Entrada inválida.")
                        continue

                if not items_a_comprar:
                    print("Pedido cancelado.")
                    continue

                resultado = self.service.procesar_pedido(cedula, [{"id": i["id"], "cantidad": i.get("cantidad", i.get("amount"))} for i in items_a_comprar])
                
                if "error" in resultado:
                    print(f"Error: {resultado['error']}")
                    continue

                print("\n========================================")
                print("               FACTURA                 ")
                print("========================================")
                print(f"Pedido N°: {resultado['id_pedido']}")
                print(f"Cliente: {resultado['cliente']} ({resultado['tipo_cliente']})")
                print("----------------------------------------")
                for item in resultado["items"]:
                    print(f"{item['cantidad']}x {item['producto']} - ${item['total_item']:.2f}")
                print("----------------------------------------")
                print(f"Subtotal:  ${resultado['subtotal']:.2f}")
                print(f"Descuento: -${resultado['descuento']:.2f}")
                print(f"TOTAL:     ${resultado['total']:.2f}")
                print("========================================\n")
                
            elif opcion == "4":
                print("\n--- HISTORIAL DE PEDIDOS ---")
                pedidos = self.service.listar_historial_pedidos()
                if not pedidos:
                    print("No hay pedidos registrados.")
                for ped in pedidos:
                    print(f"Pedido #{ped['id_pedido']} | Cliente: {ped['cliente']} | Total: ${ped['total']:.2f}")
                    
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")