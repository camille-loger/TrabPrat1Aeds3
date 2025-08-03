import math
def dijkstra(grafo, origem):
    dist = {}
    prev = {}

    for v in grafo:
        dist[v] = math.inf
        prev[v] = None
    
    dist[origem] = 0
    prev[origem] = origem

    O = set(grafo.keys()) # vertices principais listados na lista de adjacencias dos vertices
    C = set() # c sao os vertices os quais todos vizinhos foram visitados

    def acha_distancia(x): #funcao pra achar menor distancia pra um vertice x
        return dist[x] 
    
    while C != set(grafo.keys()):
        u = min(O, key=acha_distancia) # procura a menor distancia dentre os vertices ainda nao explorados
        C = C + {u}
        O = O - {u}

        for v, peso in grafo[u]:
            if v not in C:
                if (dist[v] > (dist[u] + peso)):
                    dist[v] = dist[u] + peso
                    prev[v] = u
                    
    return dist, prev