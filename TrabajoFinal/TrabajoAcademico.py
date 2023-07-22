import networkx as nx
import matplotlib.pyplot as plt
def agregar_arista(grafo, nodo1, nodo2, peso,calle):
    if nodo1 not in grafo:
        grafo[nodo1] = []
    grafo[nodo1].append((nodo2, peso, calle))
    if nodo2 not in grafo:
        grafo[nodo2] = []
    grafo[nodo2].append((nodo1, peso, calle))
def dijkstra(grafo, inicio, objetivo):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()

    while len(visitados) < len(grafo):
        nodo_actual = None
        min_distancia = float('inf')
        for nodo, distancia in distancias.items():
            if nodo not in visitados and distancia < min_distancia:
                nodo_actual = nodo
                min_distancia = distancia

        if nodo_actual is None:
            break

        visitados.add(nodo_actual)

        for vecino, peso, calle in grafo[nodo_actual]:
            nueva_distancia = distancias[nodo_actual] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia

    # Reconstruir el camino más corto
    camino = []
    calles_camino = []
    nodo_actual = objetivo
    while nodo_actual != inicio:
        camino.insert(0, nodo_actual)
        for vecino, peso, calle in grafo[nodo_actual]:
            if distancias[nodo_actual] == distancias[vecino] + peso:
                nodo_actual = vecino
                calles_camino.insert(0, calle)  # Agregar la calle al inicio de la lista
                break

    camino.insert(0, inicio)
    return camino, calles_camino
def graficar_grafo(grafo):
    # Crear un grafo de networkx
    G = nx.Graph()
    # Agregar las aristas del grafo creado a networkx
    for nodo, adyacentes in grafo.items():
        for vecino, peso, _ in adyacentes:
            G.add_edge(nodo, vecino, weight=peso)

    # Crear una disposición (layout) para los nodos en el gráfico
    pos = nx.kamada_kawai_layout(G)  # Layout para una forma más cuadrada

    # Ajustar el tamaño de la figura
    plt.figure(figsize=(12, 8))

    # Dibujar el grafo utilizando matplotlib
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color="skyblue", edge_color="gray")

    # Agregar las etiquetas de peso (distancia) en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el gráfico
    plt.show()
def graficar_grafo_con_camino(grafo, camino):
    # Crear un grafo de networkx
    G = nx.Graph()
    # Agregar las aristas del grafo creado a networkx
    for nodo, adyacentes in grafo.items():
        for vecino, peso, calle in adyacentes:
            G.add_edge(nodo, vecino, weight=peso, calle=calle)

    # Crear una disposición (layout) para los nodos en el gráfico
    pos = nx.kamada_kawai_layout(G)  # Layout para una forma más cuadrada

    # Ajustar el tamaño de la figura
    plt.figure(figsize=(12, 8))

    # Dibujar las aristas y nodos del grafo en color gris claro
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color="lightgray", edge_color="lightgray")

    # Dibujar el camino en color azul
    edges = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="blue", width=3)

    # Dibujar los nodos del camino en color azul
    nodes = set(camino)
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_size=500, node_color="blue")

    # Agregar las etiquetas de peso y calle en las aristas
    edge_labels = {(camino[i], camino[i+1]): G.edges[camino[i], camino[i+1]]['weight'] for i in range(len(camino)-1)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el gráfico
    plt.show()
def crear_grafo():
    grafo = {}

    # Agregar aristas y pesos al grafo
    agregar_arista(grafo, 'a', 'b', 60,'A')
    agregar_arista(grafo, 'a', 'j', 201,'La limonita')
    agregar_arista(grafo, 'b', 'c', 56,'A')
    agregar_arista(grafo, 'b','d',122,'El oro')
    agregar_arista(grafo, 'c', 'e',122 ,'Av.ingenieria')
    agregar_arista(grafo, 'd', 'e', 57,'La bornita')
    agregar_arista(grafo, 'd', 'f', 50,'El oro')
    agregar_arista(grafo, 'e','g',50,'Av.ingenieria')
    agregar_arista(grafo, 'f','g',58,'Av.ingenieria')
    agregar_arista(grafo, 'f','h',29,'El oro')
    agregar_arista(grafo, 'h','i',58,'La Calcopirita')
    agregar_arista(grafo, 'g','i',29,'Av.ingenieria')
    agregar_arista(grafo, 'j','h',60,'La Calcopirita')
    agregar_arista(grafo, 'j','k',29,'La limonita')
    agregar_arista(grafo, 'k','l',60,'Av. parque')
    agregar_arista(grafo, 'h','l',30,'El oro')
    agregar_arista(grafo, 'l','m',58,'Av. parque')
    agregar_arista(grafo, 'i','m',33,'Av.ingenieria')
    agregar_arista(grafo, 'k','n',115,'La limonita')
    agregar_arista(grafo, 'n','a3',126,'Av.mineria')
    agregar_arista(grafo, 'a3','m',124,'El oro')
    agregar_arista(grafo, 'g','q',64,'La bornita')
    agregar_arista(grafo, 'i','r',62,'La Calcopirita')
    agregar_arista(grafo, 'm','s',63,'Av. parque')
    agregar_arista(grafo, 'q','r',28,'B')
    agregar_arista(grafo, 'r','s',35,'B')
    agregar_arista(grafo, 'q','p',27,'B')
    agregar_arista(grafo, 'o','p',32,'B')
    agregar_arista(grafo, 'o','t',79,'C')
    agregar_arista(grafo, 'p','u',79,'La calcocita')
    agregar_arista(grafo, 'q','v',80,'La bornita')
    agregar_arista(grafo, 'r','w',80,'La Calcopirita')
    agregar_arista(grafo, 's','x',81,'Av. parque')
    agregar_arista(grafo, 't','u',31,'Av. Fundicion')
    agregar_arista(grafo, 'u','v',27,'Av. Fundicion')
    agregar_arista(grafo, 'v','w',30,'Av. Fundicion')
    agregar_arista(grafo, 'w','x',33,'Av. Fundicion')
    agregar_arista(grafo, 'x','y',125,'Av. Fundicion')
    agregar_arista(grafo, 'a3','y',144,'Av.mineria')
    agregar_arista(grafo, 't','z',70,'C')
    agregar_arista(grafo, 'u','A',68,'La calcocita')
    agregar_arista(grafo, 'v','B',67,'La bornita')
    agregar_arista(grafo, 'w','C',67,'La Calcopirita')
    agregar_arista(grafo, 'x','D',64,'Av. parque')
    agregar_arista(grafo, 'a5','E',51,'La Silica')
    agregar_arista(grafo, 'a6','F',51,'El cobre')
    agregar_arista(grafo, 'a7','G',51,'Los minerales')
    agregar_arista(grafo, 'y','H',64,'Av.mineria')
    agregar_arista(grafo, 'z','A',31,'El hierro')
    agregar_arista(grafo, 'A','B',29,'El hierro')
    agregar_arista(grafo, 'B','C',29,'El hierro')
    agregar_arista(grafo, 'C','D',30,'El hierro')
    agregar_arista(grafo, 'D','E',28,'El hierro')
    agregar_arista(grafo, 'E','F',29,'El hierro')
    agregar_arista(grafo, 'F','G',30,'El hierro')
    agregar_arista(grafo, 'G','H',37,'El hierro')
    agregar_arista(grafo, 'A','a8',63,'La calcocita')
    agregar_arista(grafo, 'B','I',63,'La bornita')
    agregar_arista(grafo, 'C','J',64,'La Calcopirita')
    agregar_arista(grafo, 'D','K',65,'Av. parque')
    agregar_arista(grafo, 'E','L',66,'La Silica')
    agregar_arista(grafo, 'F','M',66,'El cobre')
    agregar_arista(grafo, 'G','N',66,'Los minerales')
    agregar_arista(grafo, 'H','a4',66,'Av.mineria')
    agregar_arista(grafo, 'a8','I',30,'Av.zinc')
    agregar_arista(grafo, 'I','J',28,'Av.zinc')
    agregar_arista(grafo, 'J','K',28,'Av.zinc')
    agregar_arista(grafo, 'K','L',30,'Av.zinc')
    agregar_arista(grafo, 'L','M',26,'Av.zinc')
    agregar_arista(grafo, 'M','N',30,'Av.zinc')
    agregar_arista(grafo, 'N','a4',44,'Av.zinc')
    agregar_arista(grafo, 'I','O',60,'La bornita')
    agregar_arista(grafo, 'J','P',59,'La Calcopirita')
    agregar_arista(grafo, 'K','Q',54,'Av. parque')
    agregar_arista(grafo, 'L','R',53,'La Silica')
    agregar_arista(grafo, 'M','S',54,'El cobre')
    agregar_arista(grafo, 'N','T',53,'Los minerales')
    agregar_arista(grafo, 'a4','U',59,'Av.mineria')
    agregar_arista(grafo, 'O','P',34,'El vanadio')
    agregar_arista(grafo, 'P','Q',26,'El vanadio')
    agregar_arista(grafo, 'Q','R',34,'El vanadio')
    agregar_arista(grafo, 'R','S',29,'El vanadio')
    agregar_arista(grafo, 'S','T',28,'El vanadio')
    agregar_arista(grafo, 'T','U',36,'El vanadio')
    agregar_arista(grafo, 'O','V',60,'La bornita')
    agregar_arista(grafo, 'P','W',59,'La Calcopirita')
    agregar_arista(grafo, 'Q','X',59,'Av. parque')
    agregar_arista(grafo, 'R','Y',59,'La Silica')
    agregar_arista(grafo, 'S','Z',58,'El cobre')
    agregar_arista(grafo, 'T','a1',58,'Los minerales')
    agregar_arista(grafo, 'U','a2',59,'Av.mineria')
    agregar_arista(grafo, 'V','W',28,'El molibdeno')
    agregar_arista(grafo, 'W','X',30,'El molibdeno')
    agregar_arista(grafo, 'X','Y',35,'El molibdeno')
    agregar_arista(grafo, 'Y','Z',29,'El molibdeno')
    agregar_arista(grafo, 'Z','a1',29,'El molibdeno')
    agregar_arista(grafo, 'a1','a2',31,'El molibdeno')
    #Caminos de doble via
    agregar_arista(grafo, 'b', 'a', 60,'A')
    agregar_arista(grafo, 'c', 'b', 56,'B')
    agregar_arista(grafo, 'q', 'g', 64,'La bornita')
    agregar_arista(grafo, 't', 'o', 79,'C')
    agregar_arista(grafo, 'z', 't', 70,'C')
    return grafo


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el grafo
    grafo = crear_grafo()
    graficar_grafo(grafo)
    inicio = 'a3'
    objetivo = 'a'
    camino_mas_corto, calles_camino = dijkstra(grafo, inicio, objetivo)

    # Imprimir el camino más corto
    print(f"Camino más corto desde el nodo '{inicio}' al nodo '{objetivo}': {camino_mas_corto}")
    graficar_grafo_con_camino(grafo,camino_mas_corto)
    # Imprimir las calles por las que pasa el camino más corto
    print("Calles por las que pasa el camino más corto:")
    for calle in calles_camino:
        print(calle)