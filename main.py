from listaAdjacencias import ListaAdjacencias
from listaAdjacencias import ler_grafo
from dijkstra import dijkstra

if __name__ == "__main__":
    caminho = "reg1.txt"  # Altere se necessário
    grafo = ler_grafo(caminho)
    grafo.printGrafo()

    dist, prev = dijkstra(grafo, 100)
    print("\nO vetor de distancia final foi:\n")
    print(dist)
    print("\nO vetor de antecessores final foi:\n")
    print(prev)
