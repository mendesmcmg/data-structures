# O saudoso Mussum seria uma webcelebridade nos dias atuais e, como todo jovem internauta, você gostaria ser amigo dele na rede social. Para isso, precisa solicitar a amizade, portanto tem de chegar a uma relação direta do Trapalhão. Dado um grafo descrevendo as relações da rede social, crie um programa que diga a quantidade mínima de contatos para chegar ao Mussum.



# Entrada
# A primeira linha da entrada indica quantos são os n vértices do grafo (2≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um inteiro identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um número inteiro identificando um vértice adjacente a id. A última linha apresenta dois ids, separados por espaço, que representam você e Mussum, respectivamente.



# Saída
# Apresente a quantidade mínima de contatos necessários para chegar ao Mussum, se possível, a mensagem "Forevis alonis..." caso contrário.



# Observações
# Cada usuário da rede é representado por um id único. No primeiro exemplo, Mussum já é um dos seus contatos. No segundo caso, é preciso passar pelos usuários 2 e 3 para chegar ao ídolo. No último caso, não é possível contactá-lo...



# For example:

# Input	Result
# 3
# 1 2 2 3
# 2 2 1 3
# 3 2 1 2
# 3 1
# 0
# 4
# 1 1 2
# 2 2 1 3
# 3 2 2 4
# 4 1 3
# 4 1
# 2
# 7
# 1 1 6
# 2 1 6
# 3 1 6
# 4 1 6
# 5 1 6
# 6 5 1 2 3 4 5
# 7 0
# 7 6
# Forevis alonis...
grafo = {}
for _ in range(int(input())):
    v, A, *vizinhos = map(int, input().split())
    grafo[v] = vizinhos
eu, mussum = map(int, input().split())

def caminho_mais_curto(origem, destino, caminho=[]):
    caminho.append(origem)
    if origem == destino:
        return caminho
    mais_curto = []
    for vizinho in grafo[origem]:
        if vizinho not in caminho:
            outro_caminho = caminho_mais_curto(vizinho, destino, caminho[:])
            if not mais_curto or (outro_caminho and outro_caminho[-1] == destino and len(outro_caminho) < len(mais_curto)):
                mais_curto = outro_caminho
    return mais_curto

caminho = caminho_mais_curto(eu, mussum)

if caminho:
    print(len(caminho) - 2)
else:
    print('Forevis alonis...')