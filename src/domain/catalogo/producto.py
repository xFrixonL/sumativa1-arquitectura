from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int

    def tiene_stock_suficiente(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def disminuir_stock(self, cantidad: int):
        if not self.tiene_stock_suficiente(cantidad):
            raise ValueError(f"Stock insuficiente para {self.nombre}.")
        self.stock -= cantidad