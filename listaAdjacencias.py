# Representacao computacional de um grafo por meio de lista de adjacencias:
class ListaAdjacencias:
    # inicializa o grafo:    
    def __init__(self, numVertices):
        self.numVertices = numVertices #inicia a variavel dentro da classe, similar ao this.
        self.numArestas = 0
        self.lista = [[] for i in range(self.numVertices)]  # cria uma lista vazia para cada vertice do grafo "for i in range(n) = for(i=0; i<n;i++)""
    
    # retorna a ordem do grafo:
    def ordem(self):
        return self.numVertices
    
    # retorna o tamanho do grafo:
    def tamanho(self):
        return self.numArestas

    # adiciona uma aresta (v1, v2) no grafo:
    # peso eh um parametro opcional
    def addAresta(self, v1, v2, peso = 1):
        self.lista[v1].append((v2,peso))
        self.numArestas += 1

    # retorna True se existe uma aresta (v1,v2) no grafo:
    def possuiAresta(self, v1, v2):
        for (j,peso) in self.lista[v1]:
            if j == v2:
                return True
        return False
    
    # retorna uma lista com os vizinhos de v:
    def vizinhos(self, v):
        return self.lista[v]

    # retorna uma lista de tuplas (vertice, peso)
    # com os vizinhos de v:
    def grau(self, v):
        return len(self.lista[v]) #lenth calcula quantos registros tem no vertice v, como a estrutura é de uma lista de adjacencias, ela vai contar a quantidade de vertices listado(vizinhos de v)

    # exibe o grafo no formato de lista de adjacencias:
    def printGrafo(self):
        for i in range(self.numVertices):
            print(f"Vertice {i}: ", end = " ")
            for j in self.lista[i]:
                print(f"{j} ", end = "")
            print()


def ler_grafo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    num_vertices, num_arestas = map(int, linhas[0].split())
    grafo = ListaAdjacencias(num_vertices)

    for linha in linhas[1:]:
        u, v, peso = map(int, linha.strip().split())
        grafo.addAresta(u,v,peso)

    return grafo

