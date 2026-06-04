class Factura:
    def __init__(self, pedido_id: int, cliente_nombre: str, tipo_cliente: str, subtotal: float, lineas: list):
        self.pedido_id = pedido_id
        self.cliente_nombre = cliente_nombre
        self.tipo_cliente = tipo_cliente
        self.subtotal = subtotal
        self.lineas = lineas
        self.descuento = self._calcular_descuento(tipo_cliente, subtotal)
        self.total = self.subtotal - self.descuento

    def _calcular_descuento(self, tipo_cliente: str, subtotal: float) -> float:
        if tipo_cliente == "VIP":
            return subtotal * 0.10
        return 0.0