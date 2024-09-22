# Árbol de Derivaciones usando network x

Este proyecto implementa un generador de árboles de derivaciones a partir de una gramática formal proporcionada en un archivo de texto. Utiliza **Python** junto con la 
biblioteca **NetworkX** para crear y visualizar gráficos de derivación. También incluye ejemplos de gramáticas ambiguas y no ambiguas para probar el comportamiento de las derivaciones.

## Características

- **Lectura de gramáticas** desde un archivo `.txt`.
- **Generación de árboles de derivación** utilizando las reglas de la gramática.
- **Visualización de los árboles de derivación** mediante la librería `matplotlib`.
- **Detección de gramáticas** mediante la generación de múltiples árboles de derivación para la misma cadena.

## Requisitos

- Python 3.x
- Entrono virtual
- Librerías necesarias:
  - `networkx`
  - `matplotlib`

### Instalación de Dependencias

Para instalar las dependencias, puedes ejecutar el siguiente comando:

```bash
pip install networkx matplotlib
```
## Ejemplos de gramaticas
Aquí hay ejemplos que puedes usar para probar el programa. Guárdala en un archivo llamado gramatica.txt:

```plaintext
E -> T + E | T
T -> int * T | int
---------------------
E -> E + E | E * E | ( E ) | int
---------------------------------
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> ( E ) | n
