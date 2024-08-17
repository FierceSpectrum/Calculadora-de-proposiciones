# Calculadora de Proposiciones

Este proyecto es una calculadora de proposiciones lógicas, diseñada para evaluar, simplificar, y generar tablas de verdad para expresiones lógicas. Está implementado en Python y utiliza la librería [SymPy](https://www.sympy.org) para manejar las operaciones lógicas.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **calculadora.py**: Contiene las funciones principales para gestionar y calcular las proposiciones lógicas.
- **formato.py**: Proporciona utilidades para convertir y manipular proposiciones en formatos legibles tanto por humanos como por la librería SymPy.
- **menú.py**: Implementa el menú interactivo de la calculadora, que permite al usuario seleccionar diferentes opciones para trabajar con proposiciones lógicas.

## Funcionalidades

La calculadora de proposiciones ofrece las siguientes funcionalidades:

1. **Evaluación de Proposiciones**: Permite al usuario ingresar una proposición lógica y evaluar su valor de verdad dada una asignación de valores para las variables.

2. **Simplificación de Proposiciones**: Simplifica una expresión lógica a su forma más reducida utilizando las capacidades de simplificación de SymPy.

3. **Generación de Tablas de Verdad**: Crea una tabla de verdad para una proposición lógica, mostrando todas las posibles combinaciones de valores de verdad para las variables involucradas.

## Instalación

Para utilizar esta calculadora, necesitas tener Python y la librería SymPy instalados. Puedes instalarlos usando pip:

```bash
pip install sympy
```
## Uso

El proyecto está actualmente en una fase inicial y se ejecuta desde la consola. A continuación se describen las principales funciones:

### 1. Evaluar una Proposición

La función `calcular_exprecion()` permite ingresar una proposición lógica, asignar valores a las variables, y obtener el resultado de la evaluación paso a paso.

```python
calcular_exprecion()
```

### 2. Simplificar una Proposición
La función calcular_simplificacion() toma una proposición lógica y devuelve su forma simplificada.

```python
calcular_simplificacion()
```

### 3. Generar una Tabla de Verdad
La función calcular_tabla() genera una tabla de verdad completa para una proposición lógica dada.

```python
calcular_tabla()
```

## Futuro Desarrollo
Actualmente, la calculadora funciona a través de la consola, pero se planea implementar una interfaz gráfica en futuras versiones para facilitar su uso.

## Contribuciones
Las contribuciones al proyecto son bienvenidas. Si tienes ideas para mejorar la calculadora o deseas corregir errores, siéntete libre de crear un pull request.

Licencia
Este proyecto no tiene una licencia formal y fue creado con fines educativos. No está destinado para uso comercial.

