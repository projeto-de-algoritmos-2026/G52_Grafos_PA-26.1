import heapq

def dijkstra(grafo, inicio, destino):
    distancias = {no: float('inf') for no in grafo}
    anteriores = {no: None for no in grafo}
    
    distancias[inicio] = 0
    fila = [(0, inicio)]
    
    while fila:
        dist_atual, no_atual = heapq.heappop(fila)

        if no_atual == destino:
            break
        
        for vizinho, peso in grafo[no_atual]:
            nova_dist = dist_atual + peso
            
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                anteriores[vizinho] = no_atual
                heapq.heappush(fila, (nova_dist, vizinho))
    
    # reconstruir caminho
    caminho = []
    atual = destino
    
    while atual:
        caminho.append(atual)
        atual = anteriores[atual]
    
    caminho.reverse()
    
    return caminho, distancias[destino]