# Uma árvore rubro-negra é um grafo cujas estrutura segue regras muito interessantes conforme a cor do vértice. Sua implementação é um pouco complexa, então vamos tentar algo mais simples: coloração de um grafo rubro-negro. O problema é simples, dado um grafo, indique se ele pode ser colorido de tal forma que todo vértice tenha uma cor (rubro ou negra) e vértices adjacentes não tenham a mesma cor.



# Entrada
# A primeira linha da entrada indica quantos são os n vértices do grafo (0≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um inteiro identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um número inteiro identificando um vértice adjacente a id.

# Saída
# Apresente a mensagem "Mais cor, por favor!" se o grafo não pode ser colorido como as regras, "Lerei O Vermelho e o Negro.", caso contrário.

# Observações
# No primeiro exemplo, cada um dos 3 vértices está ligado a outro, portanto não é possível colorir todos só com duas cores. No segundo caso, os vértices 1 e 3 podem ter uma cor e 2 e 4 outra. No último exemplo, o vértice "central" tem uma cor e os demais outra.

# For example:

# Input	Result
# 3
# 1 2 2 3
# 2 2 1 3
# 3 2 1 2
# Mais cor, por favor!
# 4
# 1 1 2
# 2 2 1 3
# 3 2 2 4
# 4 1 3 
# Lerei "O Vermelho e o Negro".
# 6
# 1 1 6
# 2 1 6
# 3 1 6
# 4 1 6
# 5 1 6
# 6 5 1 2 3 4 5
# Lerei "O Vermelho e o Negro".

graph1 = {}

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


#Checa sub
flag = 0
for key in graph1:
    if len(graph1[key]) >= 2:
        value1 = [v for v in graph1[key]]
        for key2 in value1:
            value2 = [v for v in graph1[key2]]
            for v in value2:
                if v in value1:
                    flag = 1

#Printa
if flag == 0:
    print('Lerei "O Vermelho e o Negro".')
else:
    print('Mais cor, por favor!')

    #RESPOSTA
    # O formato "básico" é um dicionário {id: [arestas]}
# grafo = {}
# for _ in range(int(input())):
#     instr, *info = input().split()
#     if instr == 'IV':
#         grafo[info[0]] = []
#     elif instr == 'IA' and info[0] in grafo and info[1] in grafo:
#         grafo[info[0]].append(info[1])
#         grafo[info[1]].append(info[0])
#     elif instr == 'RV' and info[0] in grafo:
#         del grafo[info[0]]
#         for vertice, arestas in grafo.items():
#             if info[0] in arestas:
#                 grafo[vertice] = [a for a in arestas if a != info[0]]
#     elif instr == 'RA' and info[0] in grafo and info[1] in grafo:
#             grafo[info[0]] = [a for a in grafo[info[0]] if a != info[1]]
#             grafo[info[1]] = [a for a in grafo[info[0]] if a != info[0]]

# if grafo:
#     print(max(len(arestas) for arestas in grafo.values()))
# else:
#     print(0)

#RESPOSTA
grafo = {}
for _ in range(int(input())):
    v, A, *vizinhos = map(int, input().split())
    grafo[v] = {'cor': None, 'vizinhos': vizinhos}

coloridos = []
conflito = False

def colore(v, cor):
    global coloridos, grafo, conflito
    if not conflito and v not in coloridos:
        if all(grafo[vizinho]['cor'] != cor for vizinho in grafo[v]['vizinhos']):
            grafo[v]['cor'] = cor
            coloridos.append(v)
            for vizinho in grafo[v]['vizinhos']:
                colore(vizinho, 'negro' if cor == 'rubro' else 'rubro')
        else:
            conflito = True

if grafo:
    v = list(grafo.keys())[0]
    colore(v, 'rubro')

if conflito:
    print('Mais cor, por favor!')
else:
    print('Lerei "O Vermelho e o Negro".')
