class PanaderiaService:
    def __init__(self, repository):
        self.repository = repository

    def listar_catalogo(self):
        return self.repository.obtener_productos()

    def registrar_cliente(self, cedula, nombre, tipo):
        cliente = {"cedula": cedula, "nombre": nombre, "tipo": tipo}
        self.repository.buscar_cliente_por_cedula(cedula)
        self.repository.CLIENTES.append(cliente) if hasattr(self.repository, 'CLIENTES') else None
        # Para mantener consistencia con las listas globales del repo:
        from repositories.panaderia_repository import CLIENTES
        CLIENTES.append(cliente)

    def validar_y_preparar_item(self, producto_id, cantidad):
        producto = self.repository.buscar_producto_por_id(producto_id)
        if not producto:
            return {"error": "Producto no encontrado."}
        
        if cantidad > producto["stock"]:
            return {"error": f"Stock insuficiente. Quedan {producto['stock']}."}
        
        total_item = producto["precio"] * cantidad
        return {
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"],
            "total_item": total_item,
            "producto_id": producto["id"]
        }

    def procesar_pedido(self, cedula_cliente, items_solicitados):
        cliente = self.repository.buscar_cliente_por_cedula(cedula_cliente)
        if not cliente:
            return {"error": "El cliente no está registrado."}

        items_pedido = []
        subtotal = 0.0

        for item in items_solicitados:
            res = self.validar_y_preparar_item(item["id"], item["cantidad"])
            if "error" in res:
                return res
            
            self.repository.actualize_stock(res["producto_id"], res["cantidad"]) if hasattr(self.repository, 'actualize_stock') else self.repository.actualizar_stock(res["producto_id"], res["cantidad"])
            subtotal += res["total_item"]
            items_pedido.append({
                "producto": res["producto"],
                "cantidad": res["cantidad"],
                "precio_unitario": res["precio_unitario"],
                "total_item": res["total_item"]
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