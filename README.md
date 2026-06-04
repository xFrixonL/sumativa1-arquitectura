# sumativa1-arquitectura

Proyecto académico para la materia de Arquitectura de Software. Esta rama (`feature/ddd`) representa la cúspide evolutiva del Sistema de Pedidos para una Panadería, aplicando Domain-Driven Design (DDD) junto a una Arquitectura Hexagonal de Puertos y Adaptadores.

## Descripción de la rama

En esta versión, el proyecto está organizado para reflejar un dominio bien definido y un desacoplamiento claro entre la lógica de negocio y la infraestructura.

### Estructura del proyecto

- `src/domain`: contiene los contextos acotados del dominio.
  - `catalogo`: entidades y objetos de valor relacionados con productos.
  - `pedidos`: entidades, agregados y reglas propias de la gestión de pedidos.
  - `facturacion`: entidades y objetos de valor para la generación de facturas.

- `src/application`: incluye los casos de uso y los puertos.
  - `use_cases`: la orquestación de operaciones del dominio, como procesar pedidos y consultar el catálogo.
  - `ports`: las interfaces que definen cómo interactúa la lógica de aplicación con la infraestructura.

- `src/infrastructure`: contiene adaptadores concretos y persistencia en memoria.
  - `adapters/console_ui.py`: adaptador de consola para entrada/salida de usuario.
  - `memory_db.py`: implementación de repositorio en memoria para productos, clientes y pedidos.

## Beneficios técnicos alcanzados

- Desacoplamiento completo entre la lógica de negocio y la infraestructura.
- Lógica de dominio independiente de la interfaz de usuario y de cómo se almacena la información.
- Mayor inmutabilidad y claridad en los modelos del dominio.
- Código más legible, mantenible y alineado con principios de `clean code`.
- Facilita la prueba unitaria de cada capa sin necesidad de dependencias concretas.

## Ejecución

1. Navega al directorio del proyecto.
2. Ejecuta:

```bash
python main.py
```

## Notas

Esta rama es la versión más madura del proyecto, diseñada para mostrar cómo un sistema de pedidos puede evolucionar hacia una arquitectura basada en DDD y puertos/adaptadores.
