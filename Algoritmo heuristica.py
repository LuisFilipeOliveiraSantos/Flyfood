import os

def ler_matriz():
    coordenadas = []

    os.chdir(
        "C:\\Users\\filipe\\Desktop\\Flyflood, Luis Filipe Olveira Santos\\Matriz")

    with open('coordenadas.txt', 'r') as arquivo:
        matriz = arquivo.read()

    linhas = matriz.split("\n")  # Separa linha a linha

    for linha in linhas:
        # Passa linha a linha colocando cada uma dentro de uma lista
        elemento_linhas = [elemento for elemento in linha.split()]
        if elemento_linhas:
            # Verifica se é um elemento vazio e, caso não seja, adiciona dentro da matriz coordenadas
            coordenadas.append(elemento_linhas)

    elementos_matriz = coordenadas[1:]
    dis_matriz = {}

    # Passa linha a linha na cópia da matriz e verifica se é diferente de 0, se for ele adiciona o elemento e o índice i e x no dicionário
    for i, linha in enumerate(elementos_matriz):
        for x, elemento in enumerate(linha):
            if elemento != '0':
                dis_matriz[elemento] = (i, x)

    return dis_matriz


matriz_coordenadas = ler_matriz()

print(matriz_coordenadas)
def distancia_pares(matriz_coordenadas):
    lista_de_chaves = matriz_coordenadas.keys()  # Pega as chaves do dicionário

    chaves_iniciais = [
        chave for chave in lista_de_chaves if chave.startswith('R')]

    menor_caminho = []  # Lista para armazenar o menor caminho
    menor_distancia_total = float('inf')

    for inicio in chaves_iniciais:
        caminho_atual = [inicio]
        distancia_total_atual = 0

        # Enquanto não visitamos todos os pontos
        while len(caminho_atual) < len(lista_de_chaves):
            ultima_chave = caminho_atual[-1]

            menor_distancia = float('inf')
            proxima_chave = None

            for chave in lista_de_chaves:
                if chave not in caminho_atual:
                    distancia_x = abs(
                        matriz_coordenadas[ultima_chave][0] - matriz_coordenadas[chave][0])
                    distancia_y = abs(
                        matriz_coordenadas[ultima_chave][1] - matriz_coordenadas[chave][1])
                    distancia = distancia_x + distancia_y

                    if distancia <= menor_distancia:
                        menor_distancia = distancia
                        proxima_chave = chave

            caminho_atual.append(proxima_chave)
            distancia_total_atual += menor_distancia

        # Adiciona R ao final para garantir que o caminho volte ao ponto de partida
        caminho_atual.append(chaves_iniciais[0])
        distancia_total_atual += abs(matriz_coordenadas[caminho_atual[-2]][0] - matriz_coordenadas[chaves_iniciais[0]][0]) + \
            abs(matriz_coordenadas[caminho_atual[-2]][1] -
                matriz_coordenadas[chaves_iniciais[0]][1])

        # Atualiza o menor caminho se o caminho atual for menor
        if distancia_total_atual <= menor_distancia_total:
            menor_caminho = caminho_atual
            menor_distancia_total = distancia_total_atual

    return menor_caminho, menor_distancia_total


menor_caminho, menor_distancia = distancia_pares(matriz_coordenadas)
print("Menor Caminho:", menor_caminho)
print("Menor Distância:", menor_distancia)