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

def converterParaDF(arquivo):
    # Média das listas que formam as linhas
    for i, linha in enumerate(arquivo):
        for j, coluna in enumerate(linha):
            arquivo[i][j] = np.mean(coluna)

    # Criando os dataframes
    df = pd.DataFrame(arquivo, columns=["Bubble Sort", "Selection Sort", "Insertion Sort"])
    
    return df

df_100 = converterParaDF(teste_100)
df_200 = converterParaDF(teste_200)
df_400 = converterParaDF(teste_400)
df_800 = converterParaDF(teste_800)
df_16M = converterParaDF(teste_16M)
dataframes = (df_100, df_200, df_400, df_800, df_16M)

def plotarGraficosOrdenacoes(dataframes):
    # Criando os gráficos
    vetores_labels = ['100k', '200k', '400k', '800k', '1.6M']
    vetores_valores = [100000, 200000, 400000, 800000, 1600000]
    dados_bubble = [] 
    dados_selection = []
    dados_insertion = []

    for i, valor in enumerate(dataframes): 
        dados_bubble.append(dataframes[i].iloc[1]['Bubble Sort'])
        dados_selection.append(dataframes[i].iloc[1]['Selection Sort'])
        dados_insertion.append(dataframes[i].iloc[1]['Insertion Sort'])
    print(dados_bubble)
    y_bubble = np.poly1d(np.polyfit(vetores_valores, dados_bubble, 2))
    y_selection = np.poly1d(np.polyfit(vetores_valores, dados_selection, 2))
    y_insertion = np.poly1d(np.polyfit(vetores_valores, dados_insertion, 2))
    
    x_vals = np.linspace(min(vetores_valores), max(vetores_valores), 500)

    plt.figure(figsize=(10, 6))
    plt.plot(vetores_valores, dados_bubble, 'o', label='Bubble Sort (dados)')
    plt.plot(x_vals, y_bubble(x_vals), '-', label='Bubble Sort (parábola)')

    plt.plot(vetores_valores, dados_selection, 'o', label='Selection Sort (dados)')
    plt.plot(x_vals, y_selection(x_vals), '-', label='Selection Sort (parábola)')

    plt.plot(vetores_valores, dados_insertion, 'o', label='Insertion Sort (dados)')
    plt.plot(x_vals, y_insertion(x_vals), '-', label='Insertion Sort (parábola)')

    plt.xticks(vetores_valores, vetores_labels)

    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Ordenações")
    plt.title("Quantidade de Ordenações por Tamanho de Vetor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./graficos/grafico_de_ordenacoes.png', bbox_inches='tight')

def plotarGraficosBuscas(dataframes):
    # Labels e valores para os tamanhos dos vetores
    vetores_labels = ['100k', '200k', '400k', '800k', '1.6M']
    vetores_valores = [100000, 200000, 400000, 800000, 1600000]
    
    # Listas para armazenar os dados de buscas
    dados_bubble_BL = []
    dados_selection_BL = []
    dados_insertion_BL = []
    dados_bubble_BB = []
    dados_selection_BB = []
    dados_insertion_BB = []
    
    # Coleta dos dados de cada dataframe
    for df in dataframes: 
        dados_bubble_BL.append(df.iloc[0]['Bubble Sort'])
        dados_selection_BL.append(df.iloc[0]['Selection Sort'])
        dados_insertion_BL.append(df.iloc[0]['Insertion Sort'])
        dados_bubble_BB.append(df.iloc[2]['Bubble Sort'])
        dados_selection_BB.append(df.iloc[2]['Selection Sort'])
        dados_insertion_BB.append(df.iloc[2]['Insertion Sort'])
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax2 = ax1.twinx()
    
    ax1.plot(vetores_valores, dados_bubble_BL, 'o-', label='Busca Linear (Bubble Sort)', color='red')
    ax1.plot(vetores_valores, dados_selection_BL, 'o-', label='Busca Linear (Selection Sort)', color='green')
    ax1.plot(vetores_valores, dados_insertion_BL, 'o-', label='Busca Linear (Insertion Sort)', color='blue')
    
    ax2.plot(vetores_valores, dados_bubble_BB, 's--', label='Busca Binária (Bubble Sort)', color='orange')
    ax2.plot(vetores_valores, dados_selection_BB, 's--', label='Busca Binária (Selection Sort)', color='purple')
    ax2.plot(vetores_valores, dados_insertion_BB, 's--', label='Busca Binária (Insertion Sort)', color='brown')
    
    ax1.set_xlabel("Tamanho do Vetor")
    ax1.set_ylabel("Número de Comparações - Busca Linear", color='black')
    ax2.set_ylabel("Número de Comparações - Busca Binária", color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    ax2.tick_params(axis='y', labelcolor='black')
    
    ax1.set_xticks(vetores_valores)
    ax1.set_xticklabels(vetores_labels)
    
    ax1.grid(True)
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.title("Comparação entre Buscas Linear e Binária (Eixo Y Duplo)")
    plt.tight_layout()
    plt.savefig('./graficos/grafico_de_buscas_duplo.png', bbox_inches='tight')
    plt.show()


def plotarGraficosEquilibrio(dataframes):
    bubble_equilibrio = []
    selection_equilibrio = []
    insertion_equilibrio = []

    vetores_valores = [100000, 200000, 400000, 800000, 1600000]
    vetores_labels = ['100k', '200k', '400k', '800k', '1.6M']
    
    for df in dataframes:
        custo_ordenacao_bubble = df.iloc[1, 0]
        custo_ordenacao_selection = df.iloc[1, 1]
        custo_ordenacao_insertion = df.iloc[1, 2]

        economia_por_busca_bubble = df.iloc[0, 0] - df.iloc[2, 0]
        economia_por_busca_selection = df.iloc[0, 1] - df.iloc[2, 1]
        economia_por_busca_insertion = df.iloc[0, 2] - df.iloc[2, 2]

        num_buscas_bubble = custo_ordenacao_bubble / economia_por_busca_bubble if economia_por_busca_bubble > 0 else np.inf
        num_buscas_selection = custo_ordenacao_selection / economia_por_busca_selection if economia_por_busca_selection > 0 else np.inf
        num_buscas_insertion = custo_ordenacao_insertion / economia_por_busca_insertion if economia_por_busca_insertion > 0 else np.inf

        bubble_equilibrio.append(num_buscas_bubble)
        selection_equilibrio.append(num_buscas_selection)
        insertion_equilibrio.append(num_buscas_insertion)
    
    plt.figure(figsize=(10, 6))
    plt.plot(vetores_valores, bubble_equilibrio, 'o-', label='Bubble Sort', color='yellowgreen')
    plt.plot(vetores_valores, selection_equilibrio, 'o-', label='Selection Sort', color='blue')
    plt.plot(vetores_valores, insertion_equilibrio, 'o-', label='Insertion Sort', color='lightblue')
    
    plt.xticks(vetores_valores, vetores_labels)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Número de Buscas para Equilibrar o Custo")
    plt.title("Ponto de Equilíbrio vs. Tamanho do Vetor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./graficos/ponto_de_equilibrio_linhas.png', bbox_inches='tight')
    plt.show()

plotarGraficosOrdenacoes(dataframes)
plotarGraficosBuscas(dataframes)
plotarGraficosEquilibrio(dataframes)