def floydWarshall(grafo, origem, destino):
    inicio = time.time()

    num_vertices = grafo.ordem()

    dist = [[(grafo.matriz[i][j] if grafo.matriz[i][j] != 0 else float('inf')) if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)]
    pred = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if dist[i][j] != float('inf') and i != j:
                pred[i][j] = i

    for k in range(num_vertices):
        if time.time() - inicio > 600:
            print("Tempo limite excedido (600 segundos)")
            return None, None
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    fim = time.time()
    tempo_execucao = fim - inicio

    if dist[origem][destino] == float('inf'):
        print(f"Tempo de execucao: {tempo_execucao} segundos")
        return None, None

    caminho = []
    atual = destino
    while atual != origem:
        caminho.insert(0, atual)
        atual = pred[origem][atual]
    caminho.insert(0, origem)

    print(f"Tempo de execucao: {tempo_execucao} segundos")
    return dist[origem][destino], caminho
