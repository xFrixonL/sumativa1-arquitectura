class PanaderiaService:
    def __init__(self, repository):
        self.repository = repository

    def listar_catalogo(self):
        return self.repository.obtener_productos()

    def registrar_cliente(self, cedula, nombre, tipo):
        cliente = {"cedula": cedula, "nombre": nombre, "tipo": tipo}
        from repositories.panaderia_repository import CLIENTES
        CLIENTES.append(cliente)

    def validar_item_individual(self, producto_id, cantidad):
        producto = self.repository.buscar_producto_por_id(producto_id)
        if not producto:
            return {"error": "Producto no encontrado."}
        if cantidad > producto["stock"]:
            return {"error": f"Stock insuficiente. Quedan {producto['stock']}."}
        return {"nombre": producto["nombre"]}

    def procesar_pedido(self, cedula_cliente, items_solicitados):
        cliente = self.repository.buscar_cliente_por_cedula(cedula_cliente)
        items_pedido = []
        subtotal = 0.0

        for item in items_solicitados:
            producto = self.repository.buscar_producto_por_id(item["id"])
            self.repository.actualizar_stock(item["id"], item["cantidad"])
            
            total_item = producto["precio"] * item["cantidad"]
            subtotal += total_item
            
            items_pedido.append({
                "producto": producto["nombre"],
                "cantidad": item["cantidad"],
                "precio_unitario": producto["precio"],
                "total_item": total_item
            })

        descuento = subtotal * 0.10 if cliente["tipo"].upper() == "VIP" else 0.0
        total_final = subtotal - descuento

        nuevo_pedido = {
            "cliente": cliente["nombre"],
            "tipo_cliente": cliente["tipo"],
            "items": items_pedido,
            "subtotal": subtotal,
            "descuento": descuento,
            "total": total_final
        }
        
        return self.repository.guardar_pedido(nuevo_pedido)

    def listar_historial_pedidos(self):
        return self.repository.obtener_pedidos()