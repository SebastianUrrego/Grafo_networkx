# Árbol de Derivaciones usando network x

Este proyecto implementa un generador de árboles de derivaciones a partir de una gramática formal proporcionada en un archivo de texto. Utiliza **Python** junto con la 
biblioteca **NetworkX** para crear y visualizar gráficos de derivación. También incluye ejemplos de gramáticas ambiguas y no ambiguas para probar el comportamiento de las derivaciones.

## Descripcion del trabajo
Este trabajo implementa un generador de árboles de derivación a partir de reglas gramaticales leídas desde un archivo de texto. Utiliza la biblioteca NetworkX para generar y visualizar los grafos que representan las derivaciones.

Objetivos:
1)Leer y procesar un archivo de gramática.
2)Generar un árbol de derivaciones basado en las reglas gramaticales.
3)Visualizar el árbol generado usando matplotlib.
4)Probar diferentes gramáticas, incluyendo gramáticas básicas y complejas.

## Características

- **Lectura de gramáticas** desde un archivo `.txt`.
- **Generación de árboles de derivación** utilizando las reglas de la gramática.
- **Visualización de los árboles de derivación** mediante la librería `matplotlib`.
- **Detección de gramáticas** mediante la generación de múltiples árboles de derivación para la misma cadena.

## Requisitos

- Python 3.x
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

Gramatica basica
```plaintext
E -> T + E | T
T -> int * T | int
```

Gramatica ambigua
```plaintext
E -> E + E | E * E | ( E ) | int
```

Gramatica compleja
```plaintext
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> ( E ) | n
```

## Uso
1) Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/SebastianUrrego/Grafo_networkx
cd Grafo_networkx
``` 

2) Crea o edita un archivo de gramática con el nombre gramatica.txt. Asegúrate de seguir el formato de reglas A -> B | C.

3) Ejecuta el script para generar el árbol de derivaciones:
 ```bash
python3 grafo.py
```
