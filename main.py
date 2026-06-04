from repositories.panaderia_repository import PanaderiaRepository
from services.panaderia_service import PanaderiaService
from controllers.panaderia_controller import PanaderiaController

def main():
    repository = PanaderiaRepository()
    service = PanaderiaService(repository)
    controller = PanaderiaController(service)
    
    controller.iniciar()

if __name__ == "__main__":
    main()