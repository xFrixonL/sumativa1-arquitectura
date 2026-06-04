from typing import List
from src.application.ports.panaderia_repository import PanaderiaRepositoryPort
from src.domain.pedidos.pedido import Pedido
from src.domain.facturacion.factura import Factura

class ProcesarPedidoUseCase:

    def __init__(self, repository: PanaderiaRepositoryPort):
        self.repository = repository

    def ejecutar(self, cedula_cliente: str, items_solicitados: List[dict]) -> Factura:
        cliente = self.repository.buscar_cliente(cedula_cliente)
        if not cliente:
            raise ValueError("El cliente no está registrado.")

        nuevo_pedido = Pedido(
            cliente_cedula=cliente["cedula"],
            cliente_nombre=cliente["nombre"],
            tipo_cliente=cliente["tipo"]
        )

        for item in items_solicitados:
            producto = self.repository.buscar_producto_por_id(item["id"])
            if not producto:
                raise ValueError(f"Producto con ID {item['id']} no encontrado.")
            
            nuevo_pedido.agregar_item(producto, item["cantidad"])

        pedido_guardado = self.repository.guardar_pedido(nuevo_pedido)
        subtotal = pedido_guardado.calcular_subtotal_pedido()
        
        lineas_detalle = []
        for linea in pedido_guardado.lineas:
            lineas_detalle.append({
                "producto": linea.producto.nombre,
                "cantidad": linea.cantidad,
                "total_item": linea.subtotal
            })

        factura = Factura(
            pedido_id=pedido_guardado.id,
            cliente_nombre=pedido_guardado.cliente_nombre,
            tipo_cliente=pedido_guardado.tipo_cliente,
            subtotal=subtotal,
            lineas=lineas_detalle
        )
        
        return factura