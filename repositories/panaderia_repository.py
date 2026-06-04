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

class PanaderiaRepository:
    def obtener_productos(self):
        return PRODUCTOS

    def buscar_producto_por_id(self, producto_id):
        for p in PRODUCTOS:
            if p["id"] == producto_id:
                return p
        return None

    def buscar_cliente_por_cedula(self, cedula):
        for c in CLIENTES:
            if c["cedula"] == cedula:
                return c
        return None

    def actualizar_stock(self, producto_id, cantidad):
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            producto["stock"] -= cantidad

    def guardar_pedido(self, pedido):
        pedido["id_pedido"] = len(PEDIDOS) + 1
        PEDIDOS.append(pedido)
        return pedido

    def obtener_pedidos(self):
        return PEDIDOS