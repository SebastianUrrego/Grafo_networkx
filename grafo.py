import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(filename):
    """
    Lee una gramática de un archivo de texto.
    Retorna una lista de producciones (reglas) correctamente procesadas.
    """
    with open(filename, 'r') as file:
        gramatica = []
        for line in file.readlines():
            izq, derecha = line.strip().split("->")
            izq = izq.strip()
            # Las producciones alternativas se separan por el símbolo "|"
            alternativas = derecha.split('|')
            for alternativa in alternativas:
                gramatica.append((izq, alternativa.strip().split()))
    return gramatica

def construir_arbol(gramatica):
    """
    Construye un gráfico de árbol a partir de una gramática.
    Cada no terminal y terminal será un nodo.
    Las reglas se representarán como aristas entre nodos.
    """
    G = nx.DiGraph()  # Grafo dirigido para representar las reglas

    for izq, derecha in gramatica:
        G.add_node(izq)  # Añadir el no terminal (lado izquierdo)
        for simbolo in derecha:
            G.add_node(simbolo)  # Añadir el terminal o no terminal (lado derecho)
            G.add_edge(izq, simbolo)  # Agregar una arista de la cabeza de la producción a los símbolos de la derecha

    return G

def guardar_y_mostrar_arbol(G, filename="arbol_gramatica.png"):
    """
    Dibuja el árbol generado y lo guarda en un archivo de imagen.
    """
    pos = nx.spring_layout(G)  # Disposición del grafo
    plt.figure(figsize=(8, 6))  # Tamaño de la figura
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=2000, font_size=10, arrows=True)
    plt.savefig(filename)  # Guardar el gráfico en un archivo
    plt.close()  # Cerrar la figura
    print(f"El árbol de la gramática ha sido guardado como '{filename}'")

def derivaciones_completas(G, nodo_inicial, derivacion_actual=None, visitados=None):
    """
    Muestra todas las derivaciones completas a partir de un nodo inicial.
    Utiliza recursividad para explorar las posibles derivaciones y evita ciclos.
    """
    if derivacion_actual is None:
        derivacion_actual = []

    if visitados is None:
        visitados = set()

    # Añadir el nodo inicial a la derivación actual
    derivacion_actual.append(nodo_inicial)

    # Detectar si ya hemos visitado este nodo en la misma derivación para evitar ciclos
    if nodo_inicial in visitados:
        print(f"Detectado ciclo en {nodo_inicial}. Derivación parcial: {' -> '.join(derivacion_actual)}")
        return

    # Marcar el nodo como visitado
    visitados.add(nodo_inicial)

    # Buscar los sucesores (producciones posibles) del nodo actual
    sucesores = list(G.successors(nodo_inicial))
    
    if sucesores:
        # Si el nodo tiene sucesores, seguimos derivando por cada uno
        for sucesor in sucesores:
            derivaciones_completas(G, sucesor, derivacion_actual.copy(), visitados.copy())
    else:
        # Si no tiene sucesores, imprimimos la derivación completa
        print(" -> ".join(derivacion_actual))

if __name__ == "__main__":
    # Archivo de gramática de entrada
    archivo_gramatica = 'grmatica.txt'  # Nombre del archivo que contiene las reglas gramaticales

    # Leer la gramática desde el archivo
    gramatica = leer_gramatica(archivo_gramatica)

    # Construir el árbol (grafo dirigido) a partir de la gramática
    arbol = construir_arbol(gramatica)
    
    # Guardar el árbol como una imagen y mostrarlo
    guardar_y_mostrar_arbol(arbol, "arbol_gramatica7.png")

    # Mostrar las derivaciones completas desde el nodo inicial "E"
    print("Derivaciones completas desde el nodo inicial:")
    derivaciones_completas(arbol, "E")
