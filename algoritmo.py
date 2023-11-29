import os
from itertools import permutations

def ler_matriz():
    coordenadas = []

    os.chdir("C:\\Users\\filipe\\Desktop\\Flyflood, Luis Filipe Olveira Santos\\Matriz")

    with open('coordenadas.txt', 'r') as arquivo:
        matriz = arquivo.read()

    linhas = matriz.split("\n")  # Separa linha a linha

    for linha in linhas:
        elemento_linhas = [elemento for elemento in linha.split()]  # Passa linha a linha colocando cada uma dentro de uma lista
        if elemento_linhas:
            coordenadas.append(elemento_linhas)   # Verifica se é um elemento vazio e, caso não seja, adiciona dentro da matriz coordenadas

    elementos_matriz = coordenadas[1:]
    dis_matriz = {}

    for i, linha in enumerate(elementos_matriz):  # Passa linha a linha na cópia da matriz e verifica se é diferente de 0, se for ele adiciona o elemento e o índice i e x no dicionário
        for x, elemento in enumerate(linha):
            if elemento != '0':
                dis_matriz[elemento] = (i, x)

    return dis_matriz

matriz_coordenadas = ler_matriz()

def distancia_pares(matriz_coordenadas):
    lista_de_chaves = matriz_coordenadas.keys()    # Pega as chaves do dicionário
    distancia_elementos = {}   # Gera um dicionário para receber a distância de cada par

    for x in lista_de_chaves:
        for y in lista_de_chaves:
            if x == y:                   # Faz a verificação para não adicionar a distância do elemento para ele mesmo.
                continue
            distancia_x = abs(matriz_coordenadas[x][0] - matriz_coordenadas[y][0])  # Calcula a distância X
            distancia_y = abs(matriz_coordenadas[x][1] - matriz_coordenadas[y][1])  # Calcula a distância Y
            distancia_elementos[x + y] = distancia_x + distancia_y   # Soma a distância X e Y para dar a distância entre pares

    return distancia_elementos

grafo_distancia = distancia_pares(matriz_coordenadas)

def caminhos_possiveis(matriz_coordenadas):
    keys_grafo = list(matriz_coordenadas.keys())
    keys_sem_R = [chave for chave in keys_grafo if chave != 'R']   # Cria uma lista em que a chave só vai ser adicionada se ela for diferente de R
    permutacoes = ['R' + ''.join(i) + 'R' for i in permutations(keys_sem_R)] # Faz permutações das chaves da lista sem R e concatena o R no início e no final da permutação
    return permutacoes

permutacao_caminhos = caminhos_possiveis(matriz_coordenadas)

def calcula_caminho_total(grafo_distancia=dict, permutacao_caminhos=list):
    distancia = 0                # Calcula a distância total
    distancia_caminho = {}

    for i in permutacao_caminhos:         # Indenta os elementos da lista em i
        for h in range(0, len(i) - 1):
            procurar_chaves = i[h] + i[h + 1]  # Pega 2 elementos da permutação atual e junta 
            distancia += grafo_distancia[procurar_chaves]  # Procura a chave dentro do dicionário e soma seu valor com a distância
        distancia_caminho[i] = distancia  # Adiciona o elemento i que estamos como uma chave que vai receber o valor da distância dentro do novo dicionário
        distancia = 0  # Redefine o valor de distância para que continuemos fazendo os cálculos sem os outros valores interferirem.

    return distancia_caminho

total_distancias = calcula_caminho_total(grafo_distancia, permutacao_caminhos)

menor_chave = min(total_distancias, key=total_distancias.get)  # Pega a chave com menor valor dentro do dicionário
menor_valor = total_distancias[menor_chave]     # Pega o valor que a menor chave está recebendo

print(f"O menor caminho é {menor_chave}: {menor_valor}")