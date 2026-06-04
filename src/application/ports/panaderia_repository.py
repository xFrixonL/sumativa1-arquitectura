from abc import ABC, abstractmethod
from typing import List
from src.domain.catalogo.producto import Producto
from src.domain.pedidos.pedido import Pedido

class PanaderiaRepositoryPort(ABC):

    @abstractmethod
    def obtener_todos_los_productos(self) -> List[Producto]:
        pass

    @abstractmethod
    def buscar_producto_por_id(self, producto_id: int) -> Producto:
        pass

    @abstractmethod
    def buscar_cliente(self, cedula: str) -> dict:
        pass

    @abstractmethod
    def guardar_pedido(self, pedido: Pedido) -> Pedido:
        pass

    @abstractmethod
    def obtener_todos_los_pedidos(self) -> List[Pedido]:
        pass