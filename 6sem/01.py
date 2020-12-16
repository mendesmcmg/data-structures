# Um grafo G = (V, A) armazena as informações de um conjunto de vértices e outro de arestas. O grau máximo de um grafo é a quantidade máxima de arestas incidentes em um nó, o "D(grau)" é a quantidade de nós de ordem mínima.  Faça um programa que receba uma série e instruções e as processe para gerar um grafo não direcionado.

# IV A insere o vértice com id==A no grafo;
# IA A B insere uma aresta do vértice de id==A para o vértice de id==B, se os vértices existirem;
# RV A remove o vértice de id==A, se existir, e todas as arestas relacionadas a ele; e
# RA A B remove a aresta do vértice de id==A para o vértice de id==B, se existir;

# Entrada
# A entrada consiste de uma linha contendo o número 0≤n≤100 indicando a quantidade de operações sobre o grafo, seguida de n linhas contendo, cada uma, uma instrução conforme as apresentadas. Todo id é um string de não mais de 10 caracteres.

# Saída
# Apresente, em uma linha, o "D(grau)" do grafo.

# Observações
# As operações de inserção sobrescrevem as informações existentes. No primeiro exemplo, os dois vértices têm o mínimo de arestas. No segundo caso, o vértice A tem o mínimo de arestas. No último exemplo, os vértices A e B só tem uma aresta enquanto C tem duas.

# For example:

# Input	Result
# 4
# IV A
# IA B A
# IV B
# IA A B
# resultado: 1
# 9
# IV A
# IV B
# IV C
# IA B C
# IV D
# IV E
# IV F
# IA E D
# IA E F
# resultado: 0
# 7
# IV A
# IV B
# IA A B
# IV C
# IA A C
# IA C B
# RA A B
# resultado: 1

graph = {}

number = int(input())
vertices = list()

for i in range(number):
    getGraph = input().split()
    vertices = list()
    for x in range(0, len(getGraph)):
        if x == 0:
            tipo = getGraph[x]
        else:
            vertices.append(getGraph[x])
    if tipo == 'IV':
        graph[vertices[0]] = list()
    elif tipo == 'IA':
        if vertices[0] in graph and vertices[1] in graph:
            graph[vertices[0]].append(vertices)
            graph[vertices[1]].append(vertices)
    elif tipo == 'RV':
        if vertices[0] in graph:
            del graph[vertices[0]]
            for key in graph:
                value = graph[key]
                graph[key] = [v for v in value if v[0] != vertices[0] and v[1] != vertices[0] ]
                        
    elif tipo == 'RA':
        if vertices[0] in graph and vertices[1] in graph:

            value = graph[vertices[0]]
            graph[vertices[0]] = [v for v in value if (v[0] != vertices[0] or v[1] != vertices[1]) and (v[0] != vertices[1] or v[1] != vertices[0]) ]
            # for v in value:
            #     if v[0] == vertices[0] and v[1] == vertices[1]:
            #         value.remove(v) 

            value = graph[vertices[1]]
            graph[vertices[0]] = [v for v in value if (v[0] != vertices[0] or v[1] != vertices[1]) and (v[0] != vertices[1] or v[1] != vertices[0]) ]
            # for v in value:
            #     if v[0] == vertices[0] and v[1] == vertices[1]:
            #         value.remove(v)    

maximum = 0
for key in graph:
    if len(graph[key]) > maximum:
        maximum = len(graph[key])

print(maximum)


# 4
# IV A
# IV B
# IA A B
# RA A B


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
#             grafo[vertice] = [a for a in arestas if a != info[0]]
#     elif instr == 'RA' and info[0] in grafo and info[1] in grafo:
#         grafo[info[0]] = [a for a in grafo[info[0]] if a != info[1]]
#         grafo[info[1]] = [a for a in grafo[info[1]] if a != info[0]]


# from collections import Counter

# if grafo:
#     graus = Counter(len(arestas) for arestas in grafo.values())
#     print(min(graus.keys()))
# else:
#     print(0)