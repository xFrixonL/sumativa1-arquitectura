# sumativa1-arquitectura

Proyecto académico para la materia de Arquitectura de Software. En esta rama (`feature/capas`) el Sistema de Pedidos para una Panadería ha evolucionado desde una versión de código espagueti hacia una Arquitectura Monolítica por Capas.

## Descripción de la rama

Esta implementación organiza el proyecto en tres capas principales para mejorar la separación de responsabilidades y el orden del código.

- `controllers`: capa de presentación y consola. Maneja la interacción con el usuario, los menús y la lectura de entradas.
- `services`: capa de lógica de negocio. Contiene las reglas de stock, validación de pedidos, cálculo de descuentos y procesamiento de la factura.
- `repositories`: capa de persistencia en memoria. Gestiona el almacenamiento de productos, clientes y pedidos usando estructuras en memoria.

## Ventajas sobre el código espagueti

- Separación clara de conceptos entre interfaz, lógica y datos.
- Código más ordenado y fácil de mantener.
- Menor acoplamiento entre la presentación y las reglas de negocio.
- Facilita la evolución hacia arquitecturas más limpias en el futuro.

## Ejecución

1. Navega al directorio del proyecto.
2. Ejecuta:

```bash
python main.py
```

## Notas

Esta rama es un paso intermedio entre la versión espagueti y la implementación basada en DDD, enfocada en un diseño monolítico más estructurado.
