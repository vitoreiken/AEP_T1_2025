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

def plotarGraficos(dataframes, nome_identificador):
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
    plt.savefig(f'./graficos/grafico_de_{nome_identificador}.png', bbox_inches='tight')

def plotarGraficos_equilibrio(df, nome_identificador):
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

plotarGraficos(dataframes, "todos")
plotarGraficos_equilibrio(df_100, "100K")
plotarGraficos_equilibrio(df_200, "200K")
plotarGraficos_equilibrio(df_400, "400K")
plotarGraficos_equilibrio(df_800, "800K")
plotarGraficos_equilibrio(df_16M, "1.6M")