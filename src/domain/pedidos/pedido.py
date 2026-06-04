from typing import List
from src.domain.catalogo.producto import Producto

class LineaPedido:
    def __init__(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

class Pedido:
    def __init__(self, cliente_cedula: str, cliente_nombre: str, tipo_cliente: str):
        self.id: int = None
        self.cliente_cedula = cliente_cedula
        self.cliente_nombre = cliente_nombre
        self.tipo_cliente = tipo_cliente.upper()
        self.lineas: List[LineaPedido] = []

    def agregar_item(self, producto: Producto, cantidad: int):
        if not producto.tiene_stock_suficiente(cantidad):
            raise ValueError(f"No hay suficiente stock de {producto.nombre}. Quedan {producto.stock}.")
        
        producto.disminuir_stock(cantidad)
        
        nueva_linea = LineaPedido(producto, cantidad)
        self.lineas.append(nueva_linea)

    def calcular_subtotal_pedido(self) -> float:
        return sum(linea.subtotal for linea in self.lineas)