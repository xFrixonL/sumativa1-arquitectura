from src.application.use_cases.procesar_pedido_use_case import ProcesarPedidoUseCase
from src.application.use_cases.consultar_panaderia_use_case import ConsultarPanaderiaUseCase
from src.infrastructure.memory_db import CLIENTES_DB

class ConsoleUserInterface:

    def __init__(self, procesar_use_case: ProcesarPedidoUseCase, consultar_use_case: ConsultarPanaderiaUseCase):
        self.procesar_use_case = procesar_use_case
        self.consultar_use_case = consultar_use_case

    def iniciar(self):
        while True:
            print("\n--- SISTEMA DE PANADERÍA (ARQUITECTURA HEXAGONAL - DDD) ---")
            print("1. Ver Catálogo de Productos")
            print("2. Registrar Cliente")
            print("3. Crear Pedido y Facturar")
            print("4. Ver Todos los Pedidos")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\n--- CATÁLOGO DE PRODUCTOS ---")
                for p in self.consultar_use_case.listar_catalogo():
                    print(f"ID: {p.id} | {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")
                    
            elif opcion == "2":
                print("\n--- REGISTRAR CLIENTE ---")
                cedula = input("Cédula: ")
                nombre = input("Nombre completo: ")
                tipo = input("Tipo de cliente (Regular/VIP): ")
                CLIENTES_DB.append({"cedula": cedula, "nombre": nombre, "tipo": tipo})
                print("Cliente registrado con éxito.")
                
            elif opcion == "3":
                print("\n--- NUEVO PEDIDO ---")
                cedula = input("Ingrese la cédula del cliente: ")
                
                items_a_comprar = []
                catalogo_local = {p.id: p for p in self.consultar_use_case.listar_catalogo()}
                
                while True:
                    id_prod = input("ID del producto (o 'f' para finalizar): ")
                    if id_prod.lower() == 'f':
                        break
                    try:
                        id_int = int(id_prod)
                        if id_int not in catalogo_local:
                            print("Producto no encontrado.")
                            continue
                            
                        cantidad = int(input(f"Cantidad de {catalogo_local[id_int].nombre}: "))
                        
                        if cantidad > catalogo_local[id_int].stock:
                            print(f"¡Error! Stock insuficiente. Quedan {catalogo_local[id_int].stock}.")
                            continue
                            
                        items_a_comprar.append({"id": id_int, "cantidad": cantidad})
                        print(f"{catalogo_local[id_int].nombre} añadido.")
                    except ValueError:
                        print("Entrada inválida.")
                        continue

                if not items_a_comprar:
                    print("Pedido cancelado.")
                    continue

                try:
                    factura = self.procesar_use_case.ejecutar(cedula, items_a_comprar)
                    
                    print("\n========================================")
                    print("               FACTURA                 ")
                    print("========================================")
                    print(f"Pedido N°: {factura.pedido_id}")
                    print(f"Cliente: {factura.cliente_nombre} ({factura.tipo_cliente})")
                    print("----------------------------------------")
                    for item in factura.lineas:
                        print(f"{item['cantidad']}x {item['producto']} - ${item['total_item']:.2f}")
                    print("----------------------------------------")
                    print(f"Subtotal:  ${factura.subtotal:.2f}")
                    print(f"Descuento: -${factura.descuento:.2f}")
                    print(f"TOTAL:     ${factura.total:.2f}")
                    print("========================================\n")
                except ValueError as e:
                    print(f"Error: {str(e)}")
                
            elif opcion == "4":
                print("\n--- HISTORIAL DE PEDIDOS ---")
                pedidos = self.consultar_use_case.listar_historial_pedidos()
                if not pedidos:
                    print("No hay pedidos registrados.")
                for ped in pedidos:
                    print(f"Pedido #{ped.id} | Cliente: {ped.cliente_nombre} | Total: ${ped.calcular_subtotal_pedido():.2f}")
                    
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")