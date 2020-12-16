# # João amava Teresa que amava Raimundo que amava Maria que amava Joaquim que amava Lili que não amava ninguém... Mas e se Lili amasse João? Essa quadrilha seria cíclica!

# # Dado um grafo direcionado, determine se há um ciclo nele.

# # Entrada
# # A primeira linha da entrada indica quantos são os n vértices do grafo (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um string identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um string identificando um vértice adjacente a id.



# # Saída
# # Caso haja um ciclo, apresente a mensagem "Hoje tem!", caso contrário, apresente "... que ama ninguem.".



# # Observações
# # Cada usuário da rede é representado por um id único, nenhum string tem espaços ou mais de 10 caracteres e nenhum grafo tem laços. No primeiro caso, há diversos ciclos, por exemplo João e Teresa formam um ciclo. No segundo caso, não há ciclos. No terceiro caso, um dos ciclos existentes é Pedro que ama Renata que ama Joao que ama Lili que ama Pedro.



# # For example:

# # Input	Result
# # 6
# # Joao 3 Teresa Maria Raimundo
# # Raimundo 5 Teresa Maria Drummond Joao Xuxa
# # Maria 5 Teresa Drummond Joao Raimundo Xuxa
# # Teresa 5 Joao Maria Drummond Raimundo Xuxa
# # Xuxa 4 Teresa Maria Raimundo Drummond
# # Drummond 4 Xuxa Teresa Maria Raimundo
# # Hoje tem!
# # 4
# # Joao 3 Teresa Lili Maria
# # Maria 1 Teresa
# # Teresa 1 Lili
# # Lili 0
# # ... que ama ninguem.
# # 11
# # Joao 5 Zacarias Pedro Renata Lili Santana
# # Pedro 7 Zacarias Renata Joao Terezinha Lili Dino Santana
# # Renata 8 Dino Xuxa Lili Pedro Joao Terezinha Santana Conrado
# # Lili 9 Xuxa Pedro Joao Dino Renata Terezinha Conrado Zacarias Santana
# # Terezinha 7 Dino Zacarias Lili Pedro Renata Santana Laffond
# # Xuxa 5 Lili Renata Dino Santana Zacarias
# # Dino 8 Conrado Santana Pedro Renata Terezinha Xuxa Lili Zacarias
# # Conrado 4 Renata Lili Dino Santana
# # Santana 9 Renata Zacarias Lili Terezinha Pedro Joao Conrado Xuxa Dino
# # Zacarias 7 Dino Xuxa Pedro Lili Terezinha Santana Joao
# # Laffond 1 Terezinha

# #RESPOSTA
# João amava Teresa que amava Raimundo que amava Maria que amava Joaquim que amava Lili que não amava ninguém... Mas e se Lili amasse João? Essa quadrilha seria cíclica!

# Dado um grafo direcionado, determine se há um ciclo nele.

# Entrada
# A primeira linha da entrada indica quantos são os n vértices do grafo (1≤n≤100). As n linhas seguintes representam, cada uma, a informação de um vértice no formato: id,A,v1,v2,⋯,vA, onde id é um string identificando o vértice, A é a quantidade de arestas ligadas a este vértice, e cada vi≠id é um string identificando um vértice adjacente a id.



# Saída
# Caso haja um ciclo, apresente a mensagem "Hoje tem!", caso contrário, apresente "... que ama ninguem.".



# Observações
# Cada usuário da rede é representado por um id único, nenhum string tem espaços ou mais de 10 caracteres e nenhum grafo tem laços. No primeiro caso, há diversos ciclos, por exemplo João e Teresa formam um ciclo. No segundo caso, não há ciclos. No terceiro caso, um dos ciclos existentes é Pedro que ama Renata que ama Joao que ama Lili que ama Pedro.



# For example:

# Input	Result
# 6
# Joao 3 Teresa Maria Raimundo
# Raimundo 5 Teresa Maria Drummond Joao Xuxa
# Maria 5 Teresa Drummond Joao Raimundo Xuxa
# Teresa 5 Joao Maria Drummond Raimundo Xuxa
# Xuxa 4 Teresa Maria Raimundo Drummond
# Drummond 4 Xuxa Teresa Maria Raimundo
# Hoje tem!
# 4
# Joao 3 Teresa Lili Maria
# Maria 1 Teresa
# Teresa 1 Lili
# Lili 0
# ... que ama ninguem.
# 11
# Joao 5 Zacarias Pedro Renata Lili Santana
# Pedro 7 Zacarias Renata Joao Terezinha Lili Dino Santana
# Renata 8 Dino Xuxa Lili Pedro Joao Terezinha Santana Conrado
# Lili 9 Xuxa Pedro Joao Dino Renata Terezinha Conrado Zacarias Santana
# Terezinha 7 Dino Zacarias Lili Pedro Renata Santana Laffond
# Xuxa 5 Lili Renata Dino Santana Zacarias
# Dino 8 Conrado Santana Pedro Renata Terezinha Xuxa Lili Zacarias
# Conrado 4 Renata Lili Dino Santana
# Santana 9 Renata Zacarias Lili Terezinha Pedro Joao Conrado Xuxa Dino
# Zacarias 7 Dino Xuxa Pedro Lili Terezinha Santana Joao
# Laffond 1 Terezinha
# Hoje tem!

grafo = {}
for _ in range(int(input())):
    v, A, *vizinhos = input().split()
    grafo[v] = vizinhos


def ciclico(grafo, vertice, visitados, pilha):
    visitados.add(vertice)
    pilha.add(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            if ciclico(grafo, vizinho, visitados, pilha):
                return True
        elif vizinho in pilha:
            return True

    pilha.remove(vertice)
    return False


def tem_ciclo_dfs(grafo):
    visitados = set()
    pilha = set()
    for vertice in grafo:
        if vertice not in visitados:
            if ciclico(grafo, vertice, visitados, pilha):
                return True
    return False


if tem_ciclo_dfs(grafo):
    print('Hoje tem!')
else:
    print('... que ama ninguem.')

