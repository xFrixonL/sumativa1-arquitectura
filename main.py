from src.infrastructure.memory_db import InMemoryPanaderiaRepository
from src.application.use_cases.procesar_pedido_use_case import ProcesarPedidoUseCase
from src.application.use_cases.consultar_panaderia_use_case import ConsultarPanaderiaUseCase
from src.infrastructure.adapters.console_ui import ConsoleUserInterface

def main():
    repository = InMemoryPanaderiaRepository()
    
    procesar_use_case = ProcesarPedidoUseCase(repository)
    consultar_use_case = ConsultarPanaderiaUseCase(repository)
    
    ui = ConsoleUserInterface(procesar_use_case, consultar_use_case)
    ui.iniciar()

if __name__ == "__main__":
    main()