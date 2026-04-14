from grafo import grafo_kanto
from dijkstra import dijkstra

def main():
    print("=== Mapa Pokémon Kanto ===\n")
    
    for no in grafo_kanto:
        print(no)
    
    inicio = input("\nCidade inicial: ")
    destino = input("Destino: ")
    
    if inicio not in grafo_kanto or destino not in grafo_kanto:
        print("Local inválido!")
        return
    
    caminho, custo = dijkstra(grafo_kanto, inicio, destino)
    
    print("\nMelhor caminho:")
    print(" -> ".join(caminho))
    print(f"Custo total: {custo}")

if __name__ == "__main__":
    main()