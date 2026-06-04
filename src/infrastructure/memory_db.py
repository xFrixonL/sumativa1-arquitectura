from typing import List
from src.application.ports.panaderia_repository import PanaderiaRepositoryPort
from src.domain.catalogo.producto import Producto
from src.domain.pedidos.pedido import Pedido

PRODUCTOS_DB = [
    Producto(id=1, nombre="Pan de Hamburguesa", precio=0.50, stock=10),
    Producto(id=2, nombre="Croissant", precio=1.20, stock=5),
    Producto(id=3, nombre="Pastel de Chocolate", precio=15.00, stock=2)
]

CLIENTES_DB = [
    {"cedula": "1712345678", "nombre": "Juan Perez", "tipo": "Regular"},
    {"cedula": "1787654321", "nombre": "Maria Lopez", "tipo": "VIP"}
]

PEDIDOS_DB = []

class InMemoryPanaderiaRepository(PanaderiaRepositoryPort):

    def obtener_todos_los_productos(self) -> List[Producto]:
        return PRODUCTOS_DB

    def buscar_producto_por_id(self, producto_id: int) -> Producto:
        for p in PRODUCTOS_DB:
            if p.id == producto_id:
                return p
        return None

    def buscar_cliente(self, cedula: str) -> dict:
        for c in CLIENTES_DB:
            if c["cedula"] == cedula:
                return c
        return None

    def guardar_pedido(self, pedido: Pedido) -> Pedido:
        pedido.id = len(PEDIDOS_DB) + 1
        PEDIDOS_DB.append(pedido)
        return pedido

    def obtener_todos_los_pedidos(self) -> List[Pedido]:
        return PEDIDOS_DB