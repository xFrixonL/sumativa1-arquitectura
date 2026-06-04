# Sistema de Pedidos para Panadería (Código Espagueti)

Este repositorio contiene una versión de demostración de un sistema de pedidos para una panadería ejecutado en consola con Python.

> Esta rama representa la versión de **"Código Espagueti"** del proyecto.

## Descripción

En esta rama, la implementación está centrada en un único archivo principal (`main.py`) y adopta una estructura de código poco modular. El objetivo es mostrar un ejemplo de diseño con varios anti-patrones comunes.

## Características de la versión "Código Espagueti"

- Un solo archivo: toda la aplicación está en `main.py`.
- Variables y listas globales que actúan como base de datos en memoria.
- Mezcla de la interfaz de consola con la lógica de negocio en el mismo lugar.
- Mutación directa de datos globales desde múltiples funciones.
- Difícil de mantener, escalar y probar debido a la falta de separación de responsabilidades.

## Requisitos

- Python 3

## Uso

1. Navega al directorio del proyecto.
2. Ejecuta el siguiente comando:

```bash
python main.py
```

## Notas

Esta rama no está pensada como la versión final o recomendada para producción. Es una implementación de referencia para ilustrar cómo no estructurar un proyecto y para comparar con versiones posteriores más limpias y modulares.
