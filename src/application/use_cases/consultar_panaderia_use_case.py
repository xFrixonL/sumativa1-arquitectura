from typing import List
from src.application.ports.panaderia_repository import PanaderiaRepositoryPort
from src.domain.catalogo.producto import Producto
from src.domain.pedidos.pedido import Pedido

class ConsultarPanaderiaUseCase:

    def __init__(self, repository: PanaderiaRepositoryPort):
        self.repository = repository

    def listar_catalogo(self) -> List[Producto]:
        return self.repository.obtener_todos_los_productos()

    def listar_historial_pedidos(self) -> List[Pedido]:
        return self.repository.obtener_todos_los_pedidos()