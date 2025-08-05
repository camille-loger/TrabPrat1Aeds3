import math
def dijkstra(grafo, origem, destino):
    dist = {}
    prev = {}

    for v in range(grafo.numVertices):
        dist[v] = math.inf
        prev[v] = None
    
    dist[origem] = 0
    prev[origem] = origem

    O = set(range(grafo.numVertices)) # vertices principais listados na lista de adjacencias dos vertices
    C = set() # c sao os vertices os quais todos vizinhos foram visitados

    def acha_distancia(x): #funcao pra achar menor distancia pra um vertice x
        return dist[x] 
    
    while C != set(range(grafo.numVertices)):
        u = min(O, key=acha_distancia) # procura a menor distancia dentre os vertices ainda nao explorados
        C = C | {u}
        O = O - {u}

        if u == destino:
            break

        for v, peso in grafo.vizinhos(u):
            if v not in C:
                if (dist[v] > (dist[u] + peso)):
                    dist[v] = dist[u] + peso
                    prev[v] = u

    caminho = []
    atual = destino

    if prev[atual] is None:
        return None, math.inf
    
    while atual != origem:
        caminho.append(atual)
        atual = prev[atual]
    
    caminho.append(origem)
    caminho.reverse()
                    
    return caminho, dist[destino]
