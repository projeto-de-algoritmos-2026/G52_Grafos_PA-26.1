from js import document
from grafo import grafo_kanto
from dijkstra import dijkstra

def preencher_dropdowns():
    try:
        cidades = sorted(grafo_kanto.keys())
        opcoes = "".join([f"<option value='{no}'>{no}</option>" for no in cidades])
        document.getElementById("inicio").innerHTML = opcoes
        document.getElementById("destino").innerHTML = opcoes
    except Exception as e:
        print(f"Erro ao preencher: {e}")

def calcular(event):
    try:
        inicio = document.getElementById("inicio").value
        destino = document.getElementById("destino").value
        
        caminho, custo = dijkstra(grafo_kanto, inicio, destino)
        
        caminho_formatado = " → ".join([f'<span class="tag-caminho">{p}</span>' for p in caminho])
        
        document.getElementById("resultado").innerHTML = f"""
            <strong>Melhor Rota:</strong><br>
            <div style="margin-top: 8px;">{caminho_formatado}</div>
            <hr style="border: 0; border-top: 1px solid #ccc; margin: 10px 0;">
            <strong>Custo Total:</strong> {custo}
        """
    except Exception as e:
        document.getElementById("resultado").innerHTML = f"❌ Erro: {str(e)}"

# Execução
preencher_dropdowns()

# Vinculação direta
document.getElementById("btn-calcular").onclick = calcular