# Sub-sub! Um grafo G=(V,A) armazena as informações de um conjunto de vértices e outro de arestas. Um subgrafo G′=(V′,A′) é um grafo tal que V′⊂V e A′⊂A. Dados dois grafos não direcionados, diga se o segundo é um subgrafo do primeiro.


# Entrada
# A primeira linha da entrada indica quantos são os n vértices do grafo (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um inteiro identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um inteiro identificando um vértice adjacente a id. Há uma linha em branco, e as informações do segundo grafo são fornecidas no mesmo formato.



# Saída
# Apresente a mensagem "Sub-sub!", se o segundo grafo for um subgrafo do primeiro, "Ue? Ue? Ue?" caso contrário.



# Observações
# Cada usuário da rede é representado por um id único, e nenhum string tem espaços ou mais de 10 caracteres. No primeiro caso, o vértice 1 esta conectado ao 2 e 3 e, portanto, o grafo do vértice 1 conectado ao vértice 3 é subgrafo. No segundo caso, o segundo grafo não é subgrafo porque não existe a conexão dos vértices 2 e 5 no primeiro grafo. No terceiro caso, o primeiro grafo é um pentagrama e o segundo, um grafo circular do mal. Portanto temos um subgrafo.  Além disso, considere que um grafo vazio é sempre um subgrafo.



# For example:

# Input	Result
# 3
# 1 2 2 3
# 2 1 1
# 3 1 1

# 2
# 1 1 3
# 3 1 1
# Resultado Sub-sub!
# 11
# 1 9 2 11 3 7 10 5 4 6 8
# 2 4 1 3 4 7
# 3 10 5 2 11 9 1 8 10 6 4 7
# 4 10 8 5 9 11 7 3 6 1 10 2
# 5 6 1 3 4 11 7 8
# 6 6 4 1 3 9 7 8
# 7 10 1 8 10 4 5 6 2 3 9 11
# 8 9 4 7 3 10 1 6 5 9 11
# 9 5 3 8 6 4 7
# 10 5 7 8 3 4 1
# 11 6 3 7 8 1 4 5

# 5
# 1 1 3
# 2 3 3 4 5
# 3 3 2 1 5
# 4 1 2
# 5 2 3 2
# Resultado Ue? Ue? Ue?
# 5
# 1 4 5 4 3 2 
# 2 4 1 5 4 3 
# 3 4 1 2 4 5 
# 4 4 5 1 2 3 
# 5 4 1 2 3 4

# 5
# 1 1 2
# 2 1 3
# 3 1 4
# 4 1 5
# 5 1 1
# ResultadoSub-sub!

graph1 = {}
graph2 = {}

number1 = int(input())
vertices1 = list()

#Preenche grafo 1
for i in range(number1):
    vertices1 = input().split(' ')

    id = vertices1[0]
    graph1[id] = list()
    for i in range(2, len(vertices1)):
        if vertices1[i] !='':
            graph1[id].append(vertices1[i])

empty_line = input()
number2 = int(input())
vertices2 = list()

#Preenche grafo 2
for i in range(number2):
    vertices2 = input().split(' ')

    id = vertices2[0]
    graph2[id] = list()
    for i in range(2, len(vertices2)):
        if vertices2[i] !='':
            graph2[id].append(vertices2[i])

#Checa sub
flag = 0
for key in graph2:
    if key in graph1:
        value2 = [v for v in graph2[key]]
        value1 = [v for v in graph1[key]]

        for v in value2:
            if v not in value1:
                flag = 1
    else:
        flag = 1

#Printa
if flag == 0:
    print('Sub-sub!')
else:
    print('Ue? Ue? Ue?')

#RESPOSTA
# grafo = {}
# for _ in range(int(input())):
#     v, A, *vizinhos = input().split()
#     grafo[v] = vizinhos

# input()

# subgrafo = {}
# for _ in range(int(input())):
#     v, A, *vizinhos = input().split()
#     subgrafo[v] = vizinhos

# if not all(v in grafo for v in subgrafo):
#     print('Ue? Ue? Ue?')
# elif not all(a in grafo[v] for v, arestas in subgrafo.items() for a in arestas):
#     print('Ue? Ue? Ue?')
# else:
#     print('Sub-sub!')
    