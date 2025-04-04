import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Transformando as linhas dos arquivos de texto em listas
def processar_arquivo(caminho, encoding="utf-8"):
    sentencas_filtradas = {"Tamanho do Vetor:", "Elemento a ser buscado:", "Quantidade de Testes:"}
    arr_aux = [[[], [], []], [[], [], []], [[], [], []]] # Matriz 3D para separa resultados de Busca Linear, Qtd_ordenação e Busca Binária sob as categorias de Bubble, Selection e Insertion sort
    linha_anterior = ""
    contador = 0
    posicao = 0

    with open(caminho, 'r', encoding=encoding) as arquivo:
        for item in arquivo:
            linha = item.strip()
            if linha_anterior in sentencas_filtradas:
                pass
            elif linha and linha[0] != 'B' and linha not in sentencas_filtradas:
                try:
                    linha = int(linha)
                except ValueError:
                    pass

                if contador < 3:
                    arr_aux[contador % 3][contador // 3].append(linha)
                elif 3 <= contador < 6:
                    arr_aux[contador % 3][contador // 3].append(linha)
                else:
                    arr_aux[contador % 3][contador // 3].append(linha)

                contador += 1
                if contador == 9: contador = 0
            linha_anterior = linha

    return arr_aux

teste_100 = processar_arquivo("testes/Vetor_100k.txt", encoding="utf-16")
teste_200 = processar_arquivo("testes/Vetor_200k.txt")
teste_400 = processar_arquivo("testes/Vetor_400k.txt")
teste_800 = processar_arquivo("testes/Vetor_800k.txt", encoding="utf-16")
teste_16M = processar_arquivo("testes/Vetor_1,6M.txt")

def plotarGraficos(arquivo, nome_identificador):
    # Média das listas que formam as linhas
    for i, linha in enumerate(arquivo):
        for j, coluna in enumerate(linha):
            arquivo[i][j] = np.mean(coluna)

    # Criando os dataframes
    df = pd.DataFrame(arquivo, columns=["Bubble Sort", "Selection Sort", "Insertion Sort"])

    # Criando os gráficos
    categorias = ['Média Bubble Sort', 'Média Selection Sort', 'Média Insertion Sort']
    dados = [df.iloc[0], df.iloc[1], df.iloc[2]]
    cores = ["cyan", "blue", "lightblue"]
    titulos = ["Quantidade de trocas na Busca Linear", "Quantidade de Ordenações", "Quantidade de trocas na Busca Binária"]

    # Posições das barras no eixo X
    x = np.arange(len(categorias))

    # Criando os subgráficos de barras agrupadas
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for i, ax in enumerate(axes):
        ax.bar(categorias, dados[i], color=cores[i], edgecolor="black")
        ax.set_title(titulos[i])
        ax.set_ylabel("Quantidade")
        ax.set_ylim(0, max(dados[i]) * 1.2)
        step = max(dados[i] / 8)
        ax.set_yticks(np.arange(0, max(dados[i]) + step * 2, step))
        ax.grid()

    plt.tight_layout()
    plt.savefig(f'./graficos/grafico_de_medias_{nome_identificador}.png', bbox_inches='tight')

    # Fazendo gráfico para ponto de equilíbrio
    custo_ordenacao_bubble = df.iloc[1, 0]
    custo_ordenacao_selection = df.iloc[1, 1]
    custo_ordenacao_insertion = df.iloc[1, 2]

    economia_por_busca_bubble = df.iloc[0, 0] - df.iloc[2, 0]
    economia_por_busca_selection = df.iloc[0, 1] - df.iloc[2, 1]
    economia_por_busca_insertion = df.iloc[0, 2] - df.iloc[2, 2]

    # Calculando o ponto de equilíbrio para cada algoritmo
    numero_buscas_equilibrio_bubble = custo_ordenacao_bubble / economia_por_busca_bubble if economia_por_busca_bubble > 0 else np.inf
    numero_buscas_equilibrio_selection = custo_ordenacao_selection / economia_por_busca_selection if economia_por_busca_selection > 0 else np.inf
    numero_buscas_equilibrio_insertion = custo_ordenacao_insertion / economia_por_busca_insertion if economia_por_busca_insertion > 0 else np.inf

    ponto_equilibrio_bubble = df.iloc[0, 0] * numero_buscas_equilibrio_bubble
    ponto_equilibrio_selection = df.iloc[0, 1] * numero_buscas_equilibrio_selection
    ponto_equilibrio_insertion = df.iloc[0, 2] * numero_buscas_equilibrio_insertion
    # Criando o gráfico
    plt.figure(figsize=(8, 6))
    metodos = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
    pontos_equilibrio = [ponto_equilibrio_bubble, ponto_equilibrio_selection, ponto_equilibrio_insertion]

    plt.bar(metodos, pontos_equilibrio, color=['yellowgreen', 'blue', 'lightblue'], edgecolor="black")

    # Adicionando rótulos
    plt.xlabel("Método de Ordenação")
    plt.ylabel("Número de Buscas para Equilibrar o Custo")
    plt.title("Ponto de Equilíbrio da Ordenação")
    plt.ylim(0, max(pontos_equilibrio) * 1.2)

    for i, v in enumerate(pontos_equilibrio):
        plt.text(i, v + 5, f"{v:.0f}", ha="center", fontsize=12)

    plt.savefig(f'./graficos/ponto_de_equilibrio_{nome_identificador}.png', bbox_inches='tight')

plotarGraficos(teste_100, "100K")
plotarGraficos(teste_200, "200K")
plotarGraficos(teste_400, "400K")
plotarGraficos(teste_800, "800K")
plotarGraficos(teste_16M, "1.6M")