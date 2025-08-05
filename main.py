from listaAdjacencias import ListaAdjacencias
from listaAdjacencias import ler_grafo
from dijkstra import dijkstra

if __name__ == "__main__":
    caminho = "toy.txt"  # Altera conforme arquivo que será testado
    grafo = ler_grafo(caminho)
    grafo.printGrafo()

    caminho, custo = dijkstra(grafo, 0, 4)
    print("\nO caminho foi:\n")
    print(caminho)
    print("\nO custo foi:\n")
    print(custo)
