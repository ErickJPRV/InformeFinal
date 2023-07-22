def agregar_arista(grafo, nodo1, nodo2, peso):
    if nodo1 not in grafo:
        grafo[nodo1] = {}
    grafo[nodo1][nodo2] = peso

    if nodo2 not in grafo:
        grafo[nodo2] = {}
    grafo[nodo2][nodo1] = peso
def crear_grafo():
    grafo = {}
    # Agregar aristas y pesos al grafo
    agregar_arista(grafo, 'a', 'b', 1)
    agregar_arista(grafo, 'A', 'C', 2)
    agregar_arista(grafo, 'B', 'C', 3)
    agregar_arista(grafo, 'A', 'B', 1)
    agregar_arista(grafo, 'A', 'C', 2)
    agregar_arista(grafo, 'B', 'C', 3)
    return grafo
